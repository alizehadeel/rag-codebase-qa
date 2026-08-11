import hashlib

def make_chunk_id(file_path, start_line, commit_sha):
    raw = f"{file_path}:{start_line}:{commit_sha}"
    return hashlib.sha1(raw.encode()).hexdigest()[:12]

def chunk_changelog_file(file_path, content, commit_sha, versions_per_chunk=5, heading_level=2):
    """
    Groups every `versions_per_chunk` consecutive version headings into one chunk,
    instead of one chunk per version. Reduces a changelog's chunk count drastically
    so it stops crowding out unrelated queries in retrieval.
    """
    lines = content.splitlines()
    heading_prefix = "#" * heading_level

    # Step 1: find all heading positions (same detection as chunk_markdown.py)
    sections = []  # list of (title, start_line, end_line_exclusive)
    current_title = None
    current_start = 1

    for i, line in enumerate(lines, start=1):
        if line.startswith(heading_prefix + " ") and not line.startswith(heading_prefix + "#"):
            if current_title is not None:
                sections.append((current_title, current_start, i - 1))
            current_title = line.lstrip("#").strip()
            current_start = i
    if current_title is not None:
        sections.append((current_title, current_start, len(lines)))

    # Step 2: group every N sections into one chunk
    chunks = []
    for i in range(0, len(sections), versions_per_chunk):
        group = sections[i:i + versions_per_chunk]
        if not group:
            continue

        group_start_line = group[0][1]
        group_end_line = group[-1][2]
        group_titles = [g[0] for g in group]

        body = "\n".join(lines[group_start_line - 1:group_end_line]).strip()
        if not body:
            continue

        # label like "0.28.1, 0.28.0, 0.27.2, 0.27.1, 0.27.0" so it's still searchable by version
        combined_title = f"Changelog: {', '.join(group_titles)}"

        chunks.append({
            "chunk_id": make_chunk_id(file_path, group_start_line, commit_sha),
            "file_path": file_path,
            "start_line": group_start_line,
            "end_line": group_end_line,
            "chunk_type": "doc",
            "chunk_method": "changelog_grouped",
            "qualified_name": combined_title,
            "docstring": None,
            "content": body,
        })

    return chunks