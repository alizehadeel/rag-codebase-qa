# eval/extract_doc_sections.py
import json

chunks = [json.loads(l) for l in open("data/chunks.jsonl")]
doc_chunks = [c for c in chunks if c["chunk_type"] == "doc" and c["chunk_method"] == "markdown_heading"]

with open("eval/doc_sections_to_review.txt", "w", encoding="utf-8") as out:
    for i, c in enumerate(doc_chunks, 1):
        out.write(f"=== [{i}] {c['qualified_name']} ===\n")
        out.write(f"FILE: {c['file_path']}:{c['start_line']}-{c['end_line']}\n\n")
        out.write(c["content"])
        out.write("\n\n" + "-"*70 + "\n\n")

print(f"Wrote {len(doc_chunks)} sections to doc_sections_to_review.txt")