import json

chunks = [json.loads(l) for l in open("data/chunks.jsonl", encoding="utf-8")]

for c in chunks:
    if "third_party" in c["file_path"].lower() or "third party" in c["content"].lower():
        print(f"FILE: {c['file_path']} | QN: {c.get('qualified_name')}\n{c['content'][:300]}\n---\n")
