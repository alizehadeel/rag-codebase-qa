def citation_label(chunk):
    """Build the exact label the model should cite, matching chunk type."""
    fp = chunk["file_path"].replace("\\", "/")
    if chunk["chunk_type"] == "issue":
        return fp  # already formatted as "issue #123" in chunk_issues.py
    start, end = chunk.get("start_line"), chunk.get("end_line")
    if start is None or end is None or start == -1 or end == -1:
        return fp
    return f"{fp}:{start}-{end}"


def format_chunks_for_prompt(chunks):
    blocks = []
    for c in chunks:
        label = citation_label(c)
        header = f"[Source: {label}]"
        if c.get("qualified_name"):
            header += f" ({c['qualified_name']})"
        blocks.append(f"{header}\n{c['content']}")
    return "\n\n---\n\n".join(blocks)


SYSTEM_PROMPT = """You are a codebase Q&A assistant. You answer questions using ONLY the \
provided source excerpts below — never from general knowledge or assumptions about the codebase.

Rules:
1. Every factual claim in your answer MUST be followed by a citation in the exact form \
[Source: <label>], copied verbatim from the "[Source: ...]" labels given to you below. \
Do not invent, reformat, or guess at a citation.
2. If the provided excerpts do not contain enough information to answer the question, \
say so explicitly: "The provided context does not contain enough information to answer this." \
Do not fill gaps with general knowledge.
3. Be concise. Answer the question directly, then support it with citations — don't pad \
with restated context.
4. If multiple sources are relevant, cite each one where it supports a specific claim."""


def build_prompt(query, chunks):
    context = format_chunks_for_prompt(chunks)
    user_prompt = f"""Question: {query}

Source excerpts:

{context}

Answer the question above using only these excerpts, with citations as instructed."""
    return SYSTEM_PROMPT, user_prompt