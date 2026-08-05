import ast
import json
import hashlib

def make_chunk_id(file_path, start_line, commit_sha):
    raw = f"{file_path}:{start_line}:{commit_sha}"
    return hashlib.sha1(raw.encode()).hexdigest()[:12]

def chunk_python_file(file_path, content, commit_sha):
    """Yield one chunk per top-level function/class and per method inside a class."""
    chunks = []
    try:
        tree = ast.parse(content)
    except SyntaxError:
        # fallback: whole file as one chunk, flagged for later inspection
        chunks.append({
            "chunk_id": make_chunk_id(file_path, 1, commit_sha),
            "file_path": file_path,
            "start_line": 1,
            "end_line": len(content.splitlines()),
            "chunk_type": "code",
            "chunk_method": "fallback_syntax_error",
            "qualified_name": file_path,
            "docstring": None,
            "content": content,
        })
        return chunks

    def get_source(node):
        return ast.get_source_segment(content, node)

    def visit_node(node, qualname_prefix=""):
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                qualname = f"{qualname_prefix}{child.name}" if not qualname_prefix else f"{qualname_prefix}.{child.name}"
                src = get_source(child)
                if src:
                    chunks.append({
                        "chunk_id": make_chunk_id(file_path, child.lineno, commit_sha),
                        "file_path": file_path,
                        "start_line": child.lineno,
                        "end_line": child.end_lineno,
                        "chunk_type": "code",
                        "chunk_method": "ast_function",
                        "qualified_name": qualname,
                        "docstring": ast.get_docstring(child),
                        "content": src,
                    })
                # don't recurse into function bodies — nested defs rarely need their own chunk

            elif isinstance(child, ast.ClassDef):
                qualname = f"{qualname_prefix}{child.name}" if not qualname_prefix else f"{qualname_prefix}.{child.name}"
                src = get_source(child)
                class_doc = ast.get_docstring(child)

                # Chunk 1: the class signature + docstring + attributes (skip full body if huge)
                if src:
                    chunks.append({
                        "chunk_id": make_chunk_id(file_path, child.lineno, commit_sha),
                        "file_path": file_path,
                        "start_line": child.lineno,
                        "end_line": child.end_lineno,
                        "chunk_type": "code",
                        "chunk_method": "ast_class",
                        "qualified_name": qualname,
                        "docstring": class_doc,
                        "content": src,
                    })

                # Chunk per method too, so a specific method is independently retrievable
                visit_node(child, qualname_prefix=f"{qualname}")

    visit_node(tree)

    # module-level docstring as its own small chunk (helps "what does this file do" queries)
    module_doc = ast.get_docstring(tree)
    if module_doc:
        chunks.append({
            "chunk_id": make_chunk_id(file_path, 0, commit_sha),
            "file_path": file_path,
            "start_line": 1,
            "end_line": 1,
            "chunk_type": "doc",
            "chunk_method": "module_docstring",
            "qualified_name": file_path,
            "docstring": module_doc,
            "content": module_doc,
        })

    return chunks