import hashlib

def make_chunk_id(issue_number, commit_sha):
    raw = f"issue:{issue_number}:{commit_sha}"
    return hashlib.sha1(raw.encode()).hexdigest()[:12]

def chunk_issue(issue, commit_sha):
    content = f"Issue #{issue['number']}: {issue['title']}\n\n{issue['body']}"
    return {
        "chunk_id": make_chunk_id(issue["number"], commit_sha),
        "file_path": f"issue #{issue['number']}",
        "start_line": None,
        "end_line": None,
        "chunk_type": "issue",
        "chunk_method": "whole_issue",
        "qualified_name": issue["title"],
        "docstring": None,
        "content": content,
    }