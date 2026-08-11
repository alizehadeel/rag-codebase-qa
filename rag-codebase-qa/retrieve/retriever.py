# pyrefly: ignore [missing-import]
import chromadb
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

from metadata_filter import extract_filename_mention
from fusion import reciprocal_rank_fusion
from rerank import rerank
import pickle
from index.build_bm25 import tokenize  # reuse the same tokenizer from Phase 3


CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "codebase_chunks"
BM25_PATH = "data/bm25_index.pkl"

_embed_model = SentenceTransformer("BAAI/bge-small-en-v1.5")
_client = chromadb.PersistentClient(path=CHROMA_PATH)
_collection = _client.get_collection(COLLECTION_NAME)

# retrieve/retriever.py — add near the top
GENERIC_FILE_PENALTY = {
    "docs/quickstart.md": 0.5,       # halve its fused score
    "docs/troubleshooting.md": 0.5,
    "readme.md": 0.6,
}

def apply_generic_penalty(fused, chunks_lookup):
    adjusted = []
    for chunk_id, score in fused:
        chunk = chunks_lookup.get(chunk_id)
        if chunk:
            file_key = chunk["file_path"].lower().replace("\\", "/")
            penalty = GENERIC_FILE_PENALTY.get(file_key, 1.0)
            score = score * penalty
        adjusted.append((chunk_id, score))
    adjusted.sort(key=lambda x: x[1], reverse=True)
    return adjusted

with open(BM25_PATH, "rb") as f:
    _bm25_data = pickle.load(f)
_bm25 = _bm25_data["bm25"]
_chunk_ids = _bm25_data["chunk_ids"]
_chunks_lookup = _bm25_data["chunks_lookup"]


def _vector_search_ids(query, k=20, where=None):
    query_emb = _embed_model.encode(query).tolist()
    kwargs = {"query_embeddings": [query_emb], "n_results": k}
    if where:
        kwargs["where"] = where
    results = _collection.query(**kwargs)
    return results["ids"][0] if results["ids"] else []


def _bm25_search_ids(query, k=20, allowed_file_paths=None):
    scores = _bm25.get_scores(tokenize(query))
    scored = list(zip(_chunk_ids, scores))
    if allowed_file_paths:
        scored = [(cid, s) for cid, s in scored if _chunks_lookup[cid]["file_path"] in allowed_file_paths]
    scored.sort(key=lambda x: x[1], reverse=True)
    return [cid for cid, s in scored[:k]]


def retrieve(query, k=5, candidate_pool=20):
    """Main entry point. Returns top-k chunk dicts, best-first, each with
    a 'rerank_score' key. This is the only function Phase 5 (generation) calls."""

    # 1. metadata pre-filter, if query mentions a specific file
    matched_files = extract_filename_mention(query)
    chroma_where = {"file_path": {"$in": list(matched_files)}} if matched_files else None

    # 2. run both rankers over the (optionally filtered) pool
    vector_ids = _vector_search_ids(query, k=candidate_pool, where=chroma_where)
    bm25_ids = _bm25_search_ids(query, k=candidate_pool, allowed_file_paths=matched_files)

    # 3. fuse rankings
    fused = reciprocal_rank_fusion([vector_ids, bm25_ids])
    fused = apply_generic_penalty(fused, _chunks_lookup)   # ← add this line
    fused_ids = [cid for cid, score in fused][:candidate_pool]

    # 4. gather full chunk dicts for the fused candidates
    candidates = [_chunks_lookup[cid] for cid in fused_ids if cid in _chunks_lookup]

    # 5. rerank with cross-encoder, keep true top-k
    final = rerank(query, candidates, top_k=k)
    return final


if __name__ == "__main__":
    import json
    results = retrieve("how does the client handle timeouts", k=5)
    for r in results:
        print(f"{r['rerank_score']:.3f}  {r['qualified_name']}  ({r['file_path']}:{r['start_line']}-{r['end_line']})")