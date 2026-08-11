# eval/extract_code_sections.py
import json

chunks = [json.loads(l) for l in open("data/chunks.jsonl")]
code_chunks = [c for c in chunks if c["chunk_type"] == "code" and c["chunk_method"] in ("ast_function", "ast_class")]

# sort by file so related functions/classes are grouped together while browsing
code_chunks.sort(key=lambda c: (c["file_path"], c["start_line"]))

with open("eval/code_sections_to_review.txt", "w", encoding="utf-8") as out:
    for c in code_chunks:
        out.write(f"=== {c['qualified_name']} ({c['chunk_method']}) ===\n")
        out.write(f"FILE: {c['file_path']}:{c['start_line']}-{c['end_line']}\n\n")
        if c.get("docstring"):
            out.write(f"DOCSTRING:\n{c['docstring']}\n\n")
        else:
            out.write("DOCSTRING: (none)\n\n")
        # show first ~5 lines of body as a peek, not the whole function — keeps the file scannable
        body_preview = "\n".join(c["content"].splitlines()[:5])
        out.write(f"CODE PREVIEW:\n{body_preview}\n...\n")
        out.write("\n" + "-"*70 + "\n\n")

print(f"Wrote {len(code_chunks)} code sections to eval/code_sections_to_review.txt")