import json

chunks = [json.loads(l) for l in open("data/chunks.jsonl", encoding="utf-8")]

targets = [
    "BaseClient.__init__",
    "Client.__init__",
    "BaseClient.build_request",
    "Client.send",
    "Client.request",
    "AsyncClient.request",
    "Response.raise_for_status",
    "HTTPError",
    "HTTPStatusError",
    "RequestError",
    "TimeoutException",
    "Response.json"
]

for c in chunks:
    qn = c.get("qualified_name", "")
    for t in targets:
        if qn == t or qn.endswith("." + t):
            fp = c["file_path"]
            sl = c["start_line"]
            el = c["end_line"]
            doc = (c.get("docstring") or "").strip().replace("\n", " ")[:200]
            print(f"QN: {qn}\nFILE: {fp}:{sl}-{el}\nDOC: {doc}\n---\n")
