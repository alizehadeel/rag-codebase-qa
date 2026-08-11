import json
import time
import os as _os
import sys, os

# Add project root and subdirectories to sys.path
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
if os.path.join(_PROJECT_ROOT, "retrieve") not in sys.path:
    sys.path.insert(0, os.path.join(_PROJECT_ROOT, "retrieve"))
if os.path.join(_PROJECT_ROOT, "generate") not in sys.path:
    sys.path.insert(0, os.path.join(_PROJECT_ROOT, "generate"))

from retrieve.retriever import retrieve
from generate.generater import generate
from generate.llm_client import call_llm

RESULTS_PATH = "eval/generation_results.jsonl"

def load_existing_results():
    if not _os.path.exists(RESULTS_PATH):
        return {}
    done = {}
    with open(RESULTS_PATH) as f:
        for line in f:
            row = json.loads(line)
            done[row["question"]] = row
    return done

def check_faithfulness_llm_judge(question, answer, retrieved_chunks):
    context = "\n\n".join(c["content"] for c in retrieved_chunks)
    judge_prompt = f"""You are a strict fact-checker. Given a QUESTION, an ANSWER, and \
the CONTEXT the answer should be based on, determine if every factual claim in the ANSWER \
is actually supported by the CONTEXT.

QUESTION: {question}

CONTEXT:
{context}

ANSWER:
{answer}

Respond with exactly one word: FAITHFUL or UNFAITHFUL."""
    verdict = call_llm("You are a precise fact-checking assistant.", judge_prompt, temperature=0.0)
    return "FAITHFUL" in verdict.upper()


def run_generation_eval(qa_set):
    existing = load_existing_results()
    rows = []

    with open(RESULTS_PATH, "a") as out_f:
        for item in qa_set:
            if item["question"] in existing:
                print(f"  skip (already done): {item['question'][:60]}...")
                rows.append(existing[item["question"]])
                continue

            retrieved = retrieve(item["question"], k=5)
            result = generate(item["question"], retrieved)
            time.sleep(1)

            expected_abstain = item.get("question_type") == "no_answer"
            row = {
                "question": item["question"],
                "type": item.get("question_type", "unlabeled"),
                "citations_valid": result["valid"],
                "abstained": result["abstained"],
                "answer": result["answer"],
            }

            if expected_abstain:
                row["correct_abstention"] = result["abstained"]
                row["faithful"] = None
            else:
                row["correct_abstention"] = not result["abstained"]
                if result["abstained"]:
                    row["faithful"] = None
                else:
                    row["faithful"] = check_faithfulness_llm_judge(item["question"], result["answer"], retrieved)
                    time.sleep(1)

            out_f.write(json.dumps(row) + "\n")
            out_f.flush()  # write immediately, don't lose it if the next call crashes
            rows.append(row)
            print(f"  done: {item['question'][:60]}...")

    return rows


def summarize(rows):
    applicable = [r for r in rows if r.get("faithful") is not None]
    citation_valid_rate = sum(r.get("citations_valid", False) for r in rows) / len(rows)
    faithfulness_rate = sum(r["faithful"] for r in applicable) / len(applicable) if applicable else None

    no_answer_rows = [r for r in rows if r.get("type") == "no_answer"]
    abstention_rate = (
        sum(r.get("abstained", False) for r in no_answer_rows) / len(no_answer_rows)
        if no_answer_rows else None
    )

    false_abstain_rows = [r for r in rows if r.get("type") != "no_answer" and r.get("abstained")]

    return {
        "citation_valid_rate": citation_valid_rate,
        "faithfulness_rate": faithfulness_rate,
        "correct_abstention_rate_on_no_answer_qs": abstention_rate,
        "false_abstentions_on_answerable_qs": len(false_abstain_rows),
    }

if __name__ == "__main__":
    from retrieval_eval import load_qa_set
    qa_set = load_qa_set()
    rows = run_generation_eval(qa_set)
    summary = summarize(rows)

    print("=== Generation Summary ===")
    for k, v in summary.items():
        if isinstance(v, float):
            print(f"  {k}: {v:.2%}")
        else:
            print(f"  {k}: {v}")

    print("\n=== Per-question detail ===")
    for r in rows:
        flag = "⚠️ " if (r.get("faithful") is False or not r.get("citations_valid", True) or not r.get("correct_abstention", True)) else "   "
        print(f"{flag}[{r.get('type')}] '{r['question']}' — valid={r.get('citations_valid')} faithful={r.get('faithful')} abstained={r.get('abstained')}")