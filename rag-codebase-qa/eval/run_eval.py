from retrieval_eval import load_qa_set, run_retrieval_eval
from generation_eval import run_generation_eval, summarize

qa_set = load_qa_set()

print(f"Loaded {len(qa_set)} Q/A pairs\n")

print("Running retrieval eval...")
retrieval_summary, retrieval_log = run_retrieval_eval(qa_set)

print("Running generation eval (calls Groq per question, may take a few minutes for 50 questions)...")
generation_rows = run_generation_eval(qa_set)
generation_summary = summarize(generation_rows)

print("\n" + "="*50)
print("BASELINE REPORT")
print("="*50)
print("\n-- Retrieval --")
for k, v in retrieval_summary.items():
    print(f"  {k}: {v:.2%}")
print("\n-- Generation --")
for k, v in generation_summary.items():
    print(f"  {k}: {v:.2%}" if isinstance(v, float) else f"  {k}: {v}")