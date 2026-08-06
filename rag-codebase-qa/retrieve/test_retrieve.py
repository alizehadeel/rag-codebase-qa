from .retrieve import retrieve

test_queries = [
    "how does the client handle timeouts",       # semantic
    "AsyncClient.send",                              # exact identifier
    "what happens on connection error",              # semantic
    "httpx/_client.py request method",                 # filename-mention, tests metadata filter
]

for q in test_queries:
    print(f"\n=== Query: '{q}' ===")
    results = retrieve(q, k=5)
    for r in results:
        print(f"  {r['rerank_score']:.3f}  {r['qualified_name']}  ({r['file_path']}:{r['start_line']}-{r['end_line']})")