# RAG-Powered Codebase Q&A Assistant

Ask natural-language questions about a real GitHub repository — its code, docs, and changelog — and get grounded answers with exact `file:line` citations. Built as an end-to-end RAG pipeline over [encode/httpx](https://github.com/encode/httpx), with a hand-built evaluation harness that measures retrieval and generation quality independently.

## What this project actually demonstrates

Most "RAG demos" stop at "it retrieves some chunks and an LLM answers." This project goes further:

- **Structure-aware chunking** — Python code is split by function/class using `ast`, not naive fixed-size splitting; markdown is split by heading; a repo changelog gets its own coarser chunking strategy after discovering fine-grained changelog chunks were polluting unrelated retrieval results.
- **Hybrid retrieval** — BM25 (keyword) + vector search (semantic), combined with Reciprocal Rank Fusion, then re-ranked with a cross-encoder for final precision.
- **Enforced, validated citations** — every claim in a generated answer must cite `file:line`, and citations are checked in code against what was actually retrieved (not just trusted from the LLM).
- **Deliberate abstention** — the system is instructed and tested to say "I don't know" when the retrieved context doesn't support an answer, rather than guessing.
- **A real evaluation harness, not vibes** — 50 hand-written Q/A pairs across four question types (semantic, exact-identifier, filename-scoped, unanswerable), with retrieval recall and generation faithfulness measured *separately*, because most "RAG doesn't work" complaints are retrieval failures being misdiagnosed as generation failures.

## Results

| Metric | Before | After |
|---|---|---|
| Retrieval recall@5 | 70.83% | **89.58%** |
| Retrieval recall@5 (by type) | — | semantic 91%, exact-identifier 85%, filename-scoped 100% |
| Citation validity rate | — | 96% |
| Generation faithfulness | — | 100% |

Improvements came from three concrete fixes, not general tuning:
1. **BM25 tokenizer fix** — the regex tokenizer dropped digit-leading tokens (`"0.28.1"`), making version-number queries unretrievable.
2. **Changelog re-chunking** — the changelog was originally chunked one entry per version (60-100+ tiny, generic-sounding chunks), which crowded out unrelated queries in search. Re-chunked into groups of 5 versions per chunk, cutting the chunk count to 16 and eliminating most of the pollution.
3. **Eval-metric bug fix** — the recall-checking function itself had a bug (a file-level match check was accidentally disabled during debugging), which was undercounting real retrieval successes. Restoring it revealed the true baseline was already higher than first measured — a reminder to trust but verify your own measurement code.

## Architecture

```
Query
  │
  ▼
[Metadata filter] ── if query mentions a filename, restrict search to it
  │
  ▼
[Vector search] + [BM25 keyword search]   ← run in parallel
  │
  ▼
[Reciprocal Rank Fusion]   ← merge both rankings
  │
  ▼
[Cross-encoder reranking]   ← precise top-5 from fused top-20
  │
  ▼
[Prompt construction]   ← chunks formatted with [Source: file:line] labels
  │
  ▼
[LLM generation via Groq]   ← answer with mandatory citations
  │
  ▼
[Citation validation]   ← reject/flag hallucinated sources
  │
  ▼
Answer + verified citations
```

## Project structure

```
rag-codebase-qa/
  ingest/
    clone.py                # clone target repo, pin to commit SHA
    extract.py                 # walk repo, extract .py/.md/.rst files
    fetch_issues.py               # pull GitHub issues via REST API
    chunk_python.py                 # AST-based function/class chunking
    chunk_markdown.py                 # heading-based doc chunking
    chunk_changelog.py                  # coarser grouped chunking for CHANGELOG.md
    chunk_issues.py                       # one chunk per issue
    chunk.py                                # orchestrator → data/chunks.jsonl
  index/
    embed_store.py           # embed chunks (bge-small), store in Chroma
    build_bm25.py               # build BM25 keyword index
  retrieve/
    metadata_filter.py       # detect filename mentions in query
    fusion.py                   # Reciprocal Rank Fusion
    rerank.py                      # cross-encoder reranking
    retriever.py                      # orchestrator: retrieve(query, k)
  generate/
    prompt.py                # prompt construction, citation formatting
    llm_client.py                # Groq API wrapper
    citation_check.py               # validate citations against retrieved chunks
    answer_generator.py                # orchestrator: generate(query, chunks)
  eval/
    qa_set.jsonl              # 50 hand-written Q/A pairs, ground truth
    retrieval_eval.py            # recall@1/3/5, by question type
    generation_eval.py              # faithfulness, citation validity, abstention
    run_eval.py                        # orchestrator, full baseline report
  data/                        # cloned repo, chunks, indices (gitignored)
```

## Tech stack

| Purpose | Tool |
|---|---|
| Embeddings | `sentence-transformers` (`bge-small-en-v1.5`) — free, local |
| Reranking | `sentence-transformers` (`bge-reranker-base`) — free, local |
| Vector store | `chromadb` — local, embedded |
| Keyword search | `rank_bm25` |
| LLM | Groq API (`llama-3.3-70b-versatile`) — free tier |
| Code parsing | `ast` (Python stdlib) |
| Repo access | `GitPython`, GitHub REST API |

Everything runs on a free tier — no paid API keys required.

## Setup

```bash
git clone <this-repo>
cd rag-codebase-qa
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install sentence-transformers chromadb rank_bm25 groq gitpython requests

# set your free Groq API key
export GROQ_API_KEY="your-key-here"  # or $env:GROQ_API_KEY on PowerShell
```

## Running the pipeline

```bash
# 1. Ingest
python ingest/clone.py
python ingest/extract.py
python ingest/fetch_issues.py      # optional

# 2. Chunk
python ingest/chunk.py

# 3. Index
python index/embed_store.py
python index/build_bm25.py

# 4. Query directly
python retrieve/retriever.py       # sanity-check retrieval
python generate/test_generate.py    # end-to-end: retrieve → generate

# 5. Evaluate
python eval/run_eval.py
```

## Known limitations

Documented honestly, not swept under the rug:

- **API-reference-style doc chunks under-rank against conversational queries.** Dense bullet-list sections (e.g. `docs/api.md`'s attribute listings) sometimes lose out to raw source code chunks for questions like "what attributes does X have" — likely because list-style text doesn't embed as well against natural-language questions as prose does.
- **Generic pages occasionally out-compete specific ones.** Pages like `quickstart.md` and `troubleshooting.md` mention many topics in passing and sometimes crowd out the one page that's actually authoritative on a narrow topic.
- **Closely related concepts can get confused.** E.g. "connection error" questions sometimes retrieve timeout documentation instead of the specific `ConnectError` exception — a genuinely hard case since the two topics share real semantic overlap.
- **Free-tier Groq has a daily token cap**, which constrained how large the generation eval could run in one sitting — the harness includes checkpointing (`eval/generation_results.jsonl`) specifically to survive this.

## What I'd do with more time

- LLM-generated natural-language summaries for API-reference doc chunks (rather than the template-sentence workaround used here) to close the Pattern A gap
- A learned or tuned down-weighting for generic/introductory pages instead of a hand-picked penalty list
- Query rewriting before retrieval, for vague or conversational follow-ups
- Conversational memory for multi-turn sessions ("what does *that* function call?")
- A critique/self-correction loop (retrieve → generate → check groundedness → reformulate and retry if ungrounded)
