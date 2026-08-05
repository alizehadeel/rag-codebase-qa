# ingest/extract.py
import os, json

CLONE_PATH = "data/httpx"
EXTENSIONS = {".py": "code", ".md": "doc", ".rst": "doc"}
SKIP_DIRS = {".git", "__pycache__", "node_modules", "tests", ".github"}

def walk_repo(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fname in filenames:
            ext = os.path.splitext(fname)[1]
            if ext in EXTENSIONS:
                full_path = os.path.join(dirpath, fname)
                rel_path = os.path.relpath(full_path, root)
                yield full_path, rel_path, EXTENSIONS[ext]

records = []
for full_path, rel_path, ftype in walk_repo(CLONE_PATH):
    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    records.append({"path": rel_path, "content": content, "type": ftype})

with open("data/raw_files.jsonl", "w") as f:
    for r in records:
        f.write(json.dumps(r) + "\n")

print(f"Extracted {len(records)} files")