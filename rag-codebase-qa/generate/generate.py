from prompt import build_prompt, citation_label
from llm_client import call_llm
from citation_check import validate_citations, has_any_citation, is_abstention


def generate(query, retrieved_chunks):
    """
    Main entry point. Takes a query and the chunks retrieve() returned,
    calls the LLM, validates citations, returns a structured result.
    """
    if not retrieved_chunks:
        return {
            "answer": "The provided context does not contain enough information to answer this.",
            "citations": [],
            "valid": True,
            "abstained": True,
            "bad_citations": [],
        }

    system_prompt, user_prompt = build_prompt(query, retrieved_chunks)
    raw_answer = call_llm(system_prompt, user_prompt)

    is_valid, bad_citations, cited_labels = validate_citations(raw_answer, retrieved_chunks)
    abstained = is_abstention(raw_answer)

    # map cited labels back to full chunk info, for a clean structured citations list
    label_to_chunk = {citation_label(c): c for c in retrieved_chunks}
    citations = []
    for label in cited_labels:
        chunk = label_to_chunk.get(label.strip())
        if chunk:
            citations.append({
                "file": chunk["file_path"],
                "start_line": chunk.get("start_line"),
                "end_line": chunk.get("end_line"),
                "chunk_id": chunk["chunk_id"],
            })

    return {
        "answer": raw_answer,
        "citations": citations,
        "valid": is_valid,
        "abstained": abstained,
        "bad_citations": bad_citations,  # non-empty means the model hallucinated a source label
    }