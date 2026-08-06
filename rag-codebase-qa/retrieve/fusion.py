def reciprocal_rank_fusion(ranked_lists, k=60):
    """
    ranked_lists: list of ranked lists, each a list of chunk_ids in rank order (best first)
    Returns: list of (chunk_id, fused_score) sorted best-first
    """
    scores = {}
    for ranked_list in ranked_lists:
        for rank, chunk_id in enumerate(ranked_list):
            scores[chunk_id] = scores.get(chunk_id, 0.0) + 1.0 / (k + rank + 1)
    fused = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return fused