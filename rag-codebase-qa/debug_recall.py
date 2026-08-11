import sys

sys.path.append("retrieve")

from retrieve.retriever import retrieve


def normalize(p):
    return p.lower().replace("\\", "/")


qa_item = {
    "expected_files": ["docs/advanced/extensions.md"],
    "expected_qualified_names": ["Extensions > Request Extensions"],
}

expected_files = {
    normalize(f) for f in qa_item["expected_files"]
}

expected_names = set(qa_item["expected_qualified_names"])

print("expected_files:", expected_files)
print("expected_names:", expected_names)

retrieved = retrieve(
    "what are request extensions in httpx",
    k=5
)

for c in retrieved:
    fp_norm = normalize(c["file_path"])
    qname = c.get("qualified_name")

    file_match = fp_norm in expected_files
    name_match = qname in expected_names

    print(
        f"{fp_norm!r} | "
        f"qname={qname!r} | "
        f"file_match={file_match} | "
        f"name_match={name_match}"
    )