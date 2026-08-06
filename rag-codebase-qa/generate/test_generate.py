import sys
from pathlib import Path

# Add project root and subdirectories to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "retrieve"))
sys.path.insert(0, str(PROJECT_ROOT / "generate"))

from retrieve import retrieve
from generate import generate

test_queries = [
    "how does the client handle timeouts",
    "what happens on connection error",
    "does httpx support websockets",  # deliberately something httpx likely does NOT support well — tests abstention
]

for q in test_queries:
    print(f"\n{'='*70}\nQuery: {q}\n{'='*70}")
    chunks = retrieve(q, k=5)
    result = generate(q, chunks)

    print(f"\nAnswer:\n{result['answer']}")
    print(f"\nCitations valid: {result['valid']}")
    if result["bad_citations"]:
        print(f"[WARNING] Hallucinated citations: {result['bad_citations']}")
    print(f"Abstained: {result['abstained']}")
    print(f"Structured citations: {result['citations']}")