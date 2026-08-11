import json
# pyrefly: ignore [missing-import]
import chromadb
# pyrefly: ignore [missing-import]
from sentence_transformers import SentenceTransformer

CHUNKS_PATH = "data/chunks.jsonl"
CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "codebase_chunks"

print("Loading embedding model (bge-small)...")
model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def build_embedding_text(chunk):
    parts = []
    if chunk.get("qualified_name"):
        parts.append(chunk["qualified_name"])

    # For API-reference style doc chunks (dense bullet lists), add a
    # synthetic natural-language framing sentence so it matches
    # conversational questions better.
    if chunk["chunk_type"] == "doc" and chunk.get("qualified_name"):
        name = chunk["qualified_name"].split(">")[-1].strip().strip("`")
        parts.append(f"This section describes the attributes, methods, and features of {name}.")

    if chunk.get("docstring"):
        parts.append(chunk["docstring"])
    parts.append(chunk["content"])
    return "\n".join(parts)

print("Loading chunks...")
chunks = [json.loads(line) for line in open(CHUNKS_PATH)]
print(f"Loaded {len(chunks)} chunks")

texts = [build_embedding_text(c) for c in chunks]

print("Embedding chunks (this may take a minute)...")
embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)

print("Writing to Chroma...")
client = chromadb.PersistentClient(path=CHROMA_PATH)
# recreate collection fresh each run, so re-running this script after chunking changes doesn't leave stale entries
try:
    client.delete_collection(COLLECTION_NAME)
except Exception:
    pass
collection = client.create_collection(COLLECTION_NAME)

# Chroma metadata values must be str/int/float/bool — None is not allowed, so we sanitize
def clean_metadata(chunk):
    return {
        "file_path": chunk["file_path"],
        "start_line": chunk["start_line"] if chunk["start_line"] is not None else -1,
        "end_line": chunk["end_line"] if chunk["end_line"] is not None else -1,
        "chunk_type": chunk["chunk_type"],
        "chunk_method": chunk["chunk_method"],
        "qualified_name": chunk["qualified_name"] or "",
    }

BATCH = 500  # Chroma has a max batch size for adds
for i in range(0, len(chunks), BATCH):
    batch_chunks = chunks[i:i+BATCH]
    batch_embeddings = embeddings[i:i+BATCH]
    collection.add(
        ids=[c["chunk_id"] for c in batch_chunks],
        embeddings=[e.tolist() for e in batch_embeddings],
        documents=[c["content"] for c in batch_chunks],
        metadatas=[clean_metadata(c) for c in batch_chunks],
    )

print(f"Stored {collection.count()} chunks in Chroma at {CHROMA_PATH}")