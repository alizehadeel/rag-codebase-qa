import json
from chunk_python import chunk_python_file
from chunk_markdown import chunk_markdown_file
from chunk_issues import chunk_issue

with open("data/commit_sha.txt") as f:
    commit_sha = f.read().strip()

all_chunks = []

# code + markdown from raw_files.jsonl
with open("data/raw_files.jsonl") as f:
    for line in f:
        record = json.loads(line)
        path, content, ftype = record["path"], record["content"], record["type"]

        if ftype == "code" and path.endswith(".py"):
            all_chunks.extend(chunk_python_file(path, content, commit_sha))
        elif ftype == "doc":
            all_chunks.extend(chunk_markdown_file(path, content, commit_sha))

# issues (optional file, only if you ran fetch_issues.py in Phase 1)
try:
    with open("data/issues.jsonl") as f:
        for line in f:
            issue = json.loads(line)
            all_chunks.append(chunk_issue(issue, commit_sha))
except FileNotFoundError:
    print("No issues.jsonl found, skipping issue chunks.")

with open("data/chunks.jsonl", "w") as f:
    for chunk in all_chunks:
        f.write(json.dumps(chunk) + "\n")

print(f"Wrote {len(all_chunks)} chunks to data/chunks.jsonl")

# quick breakdown by type/method — useful sanity check
from collections import Counter
methods = Counter(c["chunk_method"] for c in all_chunks)
print("Breakdown by chunk_method:", dict(methods))