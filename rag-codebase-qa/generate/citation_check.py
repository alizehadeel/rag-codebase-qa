import re

def extract_citations(answer_text):
    """Pull out every [Source: ...] label the model actually used."""
    return re.findall(r"\[Source:\s*([^\]]+)\]", answer_text)


def validate_citations(answer_text, retrieved_chunks):
    """
    Checks every citation in the answer corresponds to a chunk that was actually
    retrieved (not hallucinated). Returns (is_valid, list_of_bad_citations).
    """
    from prompt import citation_label
    valid_labels = set(citation_label(c).replace("\\", "/") for c in retrieved_chunks)

    cited = extract_citations(answer_text)
    bad = [c for c in cited if c.strip().replace("\\", "/") not in valid_labels]

    return (len(bad) == 0, bad, cited)


def has_any_citation(answer_text):
    return len(extract_citations(answer_text)) > 0


def is_abstention(answer_text):
    """Rough check: did the model say it couldn't answer, rather than confabulate?"""
    markers = ["does not contain enough information", "cannot answer", "not enough context"]
    return any(m in answer_text.lower() for m in markers)