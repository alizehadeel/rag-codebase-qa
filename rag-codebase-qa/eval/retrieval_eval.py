import json
import sys, os

# Add project root (so `index` package is found) and retrieve/ (so sibling imports work)
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)
if os.path.join(_PROJECT_ROOT, "retrieve") not in sys.path:
    sys.path.insert(0, os.path.join(_PROJECT_ROOT, "retrieve"))

from retrieve.retriever import retrieve

def normalize(path):
    return path.lower().replace("\\", "/")

def load_qa_set(path="eval/qa_set.jsonl"):
    return [json.loads(l) for l in open(path)]

def check_recall(qa_item, retrieved_chunks, k):
    expected_files = set(normalize(f) for f in qa_item.get("expected_files", []))
    expected_names = set(qa_item.get("expected_qualified_names", []))

    top_k = retrieved_chunks[:k]
    for chunk in top_k:
        # if normalize(chunk["file_path"]) in expected_files:
        #     return True
        if chunk.get("qualified_name") in expected_names:
            return True
    return False

def run_retrieval_eval(qa_set, k_values=(1, 3, 5)):
    results = {k: [] for k in k_values}
    per_question_log = []

    for item in qa_set:
        if item.get("question_type") == "no_answer":
            continue

        retrieved = retrieve(item["question"], k=max(k_values))
        row = {"question": item["question"], "type": item.get("question_type", "unlabeled")}

        for k in k_values:
            hit = check_recall(item, retrieved, k)
            results[k].append(hit)
            row[f"recall@{k}"] = hit

        row["retrieved_top5"] = [
            f"{c['file_path']}:{c.get('start_line')}" for c in retrieved[:5]
        ]
        per_question_log.append(row)

    summary = {f"recall@{k}": sum(v) / len(v) if v else 0.0 for k, v in results.items()}
    return summary, per_question_log


if __name__ == "__main__":
    qa_set = load_qa_set()
    summary, log = run_retrieval_eval(qa_set)

    print("=== Retrieval Summary ===")
    for k, score in summary.items():
        print(f"  {k}: {score:.2%}")

    print("\n=== By question type ===")
    from collections import defaultdict
    by_type = defaultdict(list)
    for row in log:
        by_type[row["type"]].append(row["recall@5"])
    for qtype, hits in by_type.items():
        print(f"  {qtype}: {sum(hits)}/{len(hits)} ({sum(hits)/len(hits):.0%})")

    print("\n=== Failures (recall@5 miss) ===")
    for row in log:
        if not row["recall@5"]:
            print(f"  [{row['type']}] '{row['question']}'")
            print(f"    got: {row['retrieved_top5']}")