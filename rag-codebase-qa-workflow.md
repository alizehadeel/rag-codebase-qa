# Build Pipeline: RAG-Powered Codebase Q&A Assistant

Ordered so each phase produces a testable artifact before the next begins. Don't build generation until retrieval is measured; don't measure retrieval until chunking is inspected by eye.

---

## Phase 0 — Scope & Setup (half a day)

1. Pick ONE target repo to develop against. Good criteria: 5k–50k LOC, mixed Python + Markdown, active issue tracker, one you know well enough to hand-write test questions later. (e.g. `httpx`, `fastapi`, or a repo of your own.)
2. Repo layout:
   ```
   rag-codebase-qa/
     ingest/        # clone, parse, chunk
     index/         # embedding + vector store + BM25
     retrieve/      # hybrid search, rerank
     generate/       # prompt templates, LLM call, citation check
     eval/          # QA pairs, retrieval + generation metrics
     data/          # cloned repo, chunks.jsonl, indices (gitignored)
     app.py         # CLI or simple loop to query end-to-end
   ```
3. Decide the two "cheap" defaults so you're not blocked on API keys: local embeddings (`bge-small` via `sentence-transformers`) and Chroma for the vector store. Swap for OpenAI embeddings / pgvector later if you want the "production-flavored" version.
4. Pin one LLM for generation (e.g. Claude or GPT-4o-mini) — cheap model is fine, this is about pipeline correctness, not answer polish yet.

**Checkpoint:** repo cloned locally, folder structure exists, dependencies install cleanly.

---

## Phase 1 — Ingestion (0.5–1 day)

1. Clone repo with `GitPython` or plain `subprocess`, pin to a specific commit SHA (store it — you'll need it for citations).
2. Walk the tree, collect files by extension: `.py`, `.js/.ts`, `.md`, `.rst`. Skip `node_modules`, `.git`, test fixtures, generated files, vendored code.
3. Optional: pull GitHub issues via the REST API (`GET /repos/{owner}/{repo}/issues`), store title + body + comments as separate "document type."
4. Write everything to a flat intermediate format first — `data/raw_files.jsonl` with `{path, content, type}`. This gives you a debuggable checkpoint before chunking logic (which is the fiddly part) touches anything.

**Checkpoint:** `wc -l data/raw_files.jsonl` matches your expected file count. Spot-check 3 entries by hand.

---

## Phase 2 — Chunking (1–2 days — this is the part that actually matters)

This is where most homemade RAG systems quietly fail, so budget real time here.

1. **Python code:** use `ast` to walk the module, emit one chunk per top-level function/class/method. Attach: `file_path`, `start_line`, `end_line`, `qualified_name` (e.g. `MyClass.my_method`), `docstring` (pulled separately so it can also be searched as prose), and the containing class/module for context.
2. **JS/TS code:** same idea via `tree-sitter` (`tree-sitter-javascript` grammar) — walk for function/class/arrow-function declarations.
3. **Markdown/RST:** split by heading level (usually H2), keep the heading text as part of the chunk and as metadata (`section_title`) — headings are gold for keyword search.
4. **Issues:** one chunk per issue (title + body), or split very long threads by comment.
5. Fallback rule: anything that doesn't parse cleanly (weird syntax, huge single function) falls back to fixed-size splitting with overlap — don't let a parse failure kill ingestion, just flag it in metadata (`chunk_method: "fallback"`) so you can find it later in eval.
6. Every chunk gets a stable ID: `hash(file_path + start_line + commit_sha)`.

**Checkpoint — do this by hand, not with a metric:** print 20 random chunks to the terminal and read them. Ask: "if I searched for the thing this code does, would this chunk boundary make sense on its own?" If functions are getting split mid-body or docstrings are getting orphaned from their function, fix chunking now — it's cheap to fix here and expensive to fix after the index is built.

---

## Phase 3 — Embedding + Storage (0.5 day)

1. Embed each chunk. For code chunks, embed `docstring + signature + body` (not raw body alone — the docstring carries semantic intent that raw code often lacks).
2. Store in Chroma (or Qdrant) with metadata: `file_path, start_line, end_line, chunk_type (code/doc/issue), qualified_name, commit_sha`.
3. Separately, build a BM25 index (`rank_bm25` or Elasticsearch/`tantivy` if you want it faster) over the same chunks' raw text — this is what catches exact function names, error strings, and identifiers that embeddings blur.
4. Persist both indices to disk under `data/` so you're not re-embedding on every run.

**Checkpoint:** query the vector store directly with 3 hand-picked questions, print top-5 results with scores. Do the same for BM25. They should disagree on at least some queries — that disagreement is exactly why you're fusing them.

---

## Phase 4 — Retrieval (1 day)

1. **Query-time metadata filter:** if the question contains something that looks like a filename or module path (regex for `\w+\.py`, `\w+/\w+`), pre-filter to that file before ranking. Cheap, high-precision win.
2. **Hybrid search:** run vector search (top 20) and BM25 (top 20) in parallel, fuse with Reciprocal Rank Fusion:
   ```
   RRF_score(doc) = sum( 1 / (k + rank_i) )  for each ranker i, k≈60
   ```
3. **Rerank:** pass the fused top-20 through a cross-encoder (`bge-reranker-base` via `sentence-transformers` or `FlagEmbedding`), keep top-5.
4. Wrap this whole thing as one function: `retrieve(query: str, k: int = 5) -> list[Chunk]`. Everything downstream depends only on this signature.

**Checkpoint:** this is where Phase 6's retrieval metric plugs in — don't skip ahead to generation without it (see Phase 6a below, pulled forward).

---

## Phase 5 — Generation with Citations (0.5–1 day)

1. Prompt template — the load-bearing constraints:
   - Answer only from the provided chunks.
   - Every factual claim must cite `file:start_line-end_line`.
   - If the retrieved chunks don't contain the answer, say so explicitly and don't guess.
2. Format retrieved chunks in the prompt with visible line numbers so the model can cite accurately:
   ```
   [Source 1: httpx/_client.py:142-168]
   def send(self, request: Request) -> Response:
       ...
   ```
3. Post-process: regex-check that every paragraph in the answer contains at least one `file:line` citation matching a chunk you actually retrieved (not a hallucinated path). Reject/retry if not.
4. Return `{answer, citations: [{file, lines, chunk_id}]}` as structured output — makes eval and UI both easier.

**Checkpoint:** ask 5 questions you know the answer to. Check citations point to real, relevant lines — not just syntactically valid ones.

---

## Phase 6 — Evaluation (1–2 days — do not skip)

### 6a. Build the test set (do this early, in parallel with Phase 4)
Hand-write 20–30 Q/A pairs from the repo you chose:
- Mix of types: "what does function X do", "where is Y configured", "what's the error when Z happens", "how do I do W" (doc-based), "is there an open issue about V".
- For each: record the *expected chunk(s)* (file + line range) that should be retrieved, and a short reference answer.
- Store as `eval/qa_set.jsonl`: `{question, expected_chunks: [...], reference_answer}`.

### 6b. Retrieval metric (measure independently of generation)
- `recall@k`: for each question, did `retrieve(question, k=5)` return at least one expected chunk? Report recall@1, @3, @5.
- Log failures with the query + what was retrieved instead — this tells you whether it's a chunking problem, an embedding problem, or a fusion-weighting problem.

### 6c. Generation metric (measure only on questions retrieval got right)
- Faithfulness: does every claim in the answer trace back to a retrieved chunk? (write a simple LLM-judge prompt, or use RAGAS's `faithfulness` metric)
- Citation accuracy: do the cited `file:line`s actually correspond to the claim being made?
- Abstention check: for 3–5 questions with NO good answer in the repo (ask about a feature that doesn't exist), confirm the system says "not found" instead of confabulating.

**Why separate 6b/6c matters:** if recall@5 is 60%, generation quality is irrelevant for the other 40% — you're fixing the wrong layer if you tune prompts instead of chunking.

**Checkpoint:** you have two numbers (retrieval recall, generation faithfulness) and a short list of specific failing questions to iterate on.

---

## Phase 7 — Stretch (once 6b/6c numbers are acceptable)

1. **Query rewriting:** LLM call that expands vague questions ("what does that do?" → "what does the `send` method in `_client.py` do?") before retrieval — cheap, test with a before/after recall@5 comparison.
2. **Conversational memory:** carry last N turns + last-referenced entities into the rewrite step so follow-ups resolve pronouns correctly.
3. **Self-correcting loop (LangGraph):** `retrieve → generate → critique` node scores groundedness; if below threshold, reformulate query and loop (cap at 2–3 iterations to avoid infinite loops). This is the natural fusion point with your other LangGraph project.

---

## Suggested Order of Work (7–9 days total)

| Day | Phase | Exit criteria |
|---|---|---|
| 1 | 0 + 1 | Repo cloned, raw files extracted |
| 2–3 | 2 | Chunks look correct by manual read |
| 3 | 3 | Both indices built and queryable |
| 4 | 4 + start 6a | Hybrid+rerank retrieval works; QA set drafted |
| 5 | 6b | recall@5 measured, failure list in hand |
| 6 | 5 | Citations present and accurate |
| 7 | 6c | Faithfulness measured, abstention verified |
| 8–9 | 7 | Pick one stretch goal, ship it |

The two hard gates not to skip: **read chunks by eye before indexing** (Phase 2 checkpoint), and **measure retrieval and generation separately** (Phase 6b/6c) — everything else in this pipeline is standard plumbing.
