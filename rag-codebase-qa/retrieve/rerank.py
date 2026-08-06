# pyrefly: ignore [missing-import]
from sentence_transformers import CrossEncoder

print("Loading reranker model (bge-reranker-base)...")
_reranker = CrossEncoder("BAAI/bge-reranker-base")

def rerank(query, candidates, top_k=5):
    """
    candidates: list of chunk dicts (must have 'content' key)
    Returns: top_k chunk dicts, sorted best-first, with 'rerank_score' added
    """
    if not candidates:
        return []
    pairs = [[query, c["content"]] for c in candidates]
    scores = _reranker.predict(pairs)
    for c, s in zip(candidates, scores):
        c["rerank_score"] = float(s)
    ranked = sorted(candidates, key=lambda c: c["rerank_score"], reverse=True)
    return ranked[:top_k]