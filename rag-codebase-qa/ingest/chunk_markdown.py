import re
import hashlib

def make_chunk_id(file_path, start_line, commit_sha):
    raw = f"{file_path}:{start_line}:{commit_sha}"
    return hashlib.sha1(raw.encode()).hexdigest()[:12]

def chunk_markdown_file(file_path, content, commit_sha, heading_level=2):
    """Split markdown by heading level (default: ## sections). Keeps parent H1 as context."""
    lines = content.splitlines()
    chunks = []

    heading_prefix = "#" * heading_level
    top_level_title = None
    current_section = {"title": None, "start": 1, "lines": []}

    def flush(end_line):
        if current_section["lines"]:
            body = "\n".join(current_section["lines"]).strip()
            if body:
                full_title = current_section["title"] or file_path
                if top_level_title and current_section["title"]:
                    full_title = f"{top_level_title} > {current_section['title']}"
                chunks.append({
                    "chunk_id": make_chunk_id(file_path, current_section["start"], commit_sha),
                    "file_path": file_path,
                    "start_line": current_section["start"],
                    "end_line": end_line,
                    "chunk_type": "doc",
                    "chunk_method": "markdown_heading",
                    "qualified_name": full_title,
                    "docstring": None,
                    "content": body,
                })

    for i, line in enumerate(lines, start=1):
        if line.startswith("# ") and not top_level_title:
            top_level_title = line.lstrip("#").strip()
        if line.startswith(heading_prefix + " ") and not line.startswith(heading_prefix + "#"):
            flush(end_line=i - 1)
            current_section = {"title": line.lstrip("#").strip(), "start": i, "lines": [line]}
        else:
            current_section["lines"].append(line)

    flush(end_line=len(lines))
    return chunks