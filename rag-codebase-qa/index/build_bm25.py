import json
import pickle
import re
# pyrefly: ignore [missing-import]
from rank_bm25 import BM25Okapi

CHUNKS_PATH = "data/chunks.jsonl"
BM25_OUT_PATH = "data/bm25_index.pkl"

def tokenize(text):
    words = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]*", text.lower())
    versions = re.findall(r"\d+\.\d+(?:\.\d+)?", text)
    return words + versions

# Keep the imports, constants, and tokenize() function definition at the top

if __name__ == "__main__":
    print("Loading chunks...")
    chunks = [json.loads(line) for line in open(CHUNKS_PATH)]

    print("Tokenizing...")
    tokenized_corpus = [tokenize(c["content"]) for c in chunks]

    print("Building BM25 index...")
    bm25 = BM25Okapi(tokenized_corpus)

    with open(BM25_OUT_PATH, "wb") as f:
        pickle.dump({
            "bm25": bm25,
            "chunk_ids": [c["chunk_id"] for c in chunks],
            "chunks_lookup": {c["chunk_id"]: c for c in chunks},
        }, f)

    print(f"Saved BM25 index for {len(chunks)} chunks to {BM25_OUT_PATH}")
