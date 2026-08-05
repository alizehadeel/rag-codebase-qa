import pickle
# pyrefly: ignore [missing-import]
import chromadb
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer
from build_bm25 import tokenize

CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "codebase_chunks"
BM25_PATH = "data/bm25_index.pkl"

model = SentenceTransformer("BAAI/bge-small-en-v1.5")
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(COLLECTION_NAME)

with open(BM25_PATH, "rb") as f:
    bm25_data = pickle.load(f)
bm25 = bm25_data["bm25"]
chunk_ids = bm25_data["chunk_ids"]
chunks_lookup = bm25_data["chunks_lookup"]

def vector_search(query, k=5):
    query_emb = model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_emb], n_results=k)
    print(f"\n[VECTOR] top {k} for: '{query}'")
    for doc_id, meta, dist in zip(results["ids"][0], results["metadatas"][0], results["distances"][0]):
        print(f"  {meta['qualified_name']} ({meta['file_path']}:{meta['start_line']}) dist={dist:.3f}")

def bm25_search(query, k=5):
    scores = bm25.get_scores(tokenize(query))
    top_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    print(f"\n[BM25] top {k} for: '{query}'")
    for i in top_idx:
        cid = chunk_ids[i]
        chunk = chunks_lookup[cid]
        print(f"  {chunk['qualified_name']} ({chunk['file_path']}:{chunk['start_line']}) score={scores[i]:.2f}")

if __name__ == "__main__":
    test_queries = [
        "how does the client send a request",       # semantic phrasing
        "AsyncClient",                                 # exact identifier — BM25 should win here
        "timeout configuration",
    ]
    for q in test_queries:
        vector_search(q)
        bm25_search(q)