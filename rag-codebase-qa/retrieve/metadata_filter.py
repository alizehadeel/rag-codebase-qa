import re
import pickle

BM25_PATH = "data/bm25_index.pkl"

with open(BM25_PATH, "rb") as f:
    _bm25_data = pickle.load(f)
_all_chunks = list(_bm25_data["chunks_lookup"].values())
_all_file_paths = set(c["file_path"] for c in _all_chunks)

# retrieve/metadata_filter.py

def extract_filename_mention(query):
    candidates = re.findall(r"[\w/\\]+\.py|\b[a-z_]+/[a-z_]+\b", query.lower())
    matched_files = set()
    for cand in candidates:
        cand_norm = cand.replace("\\", "/")  # normalize slashes
        for fp in _all_file_paths:
            fp_norm = fp.lower().replace("\\", "/")  # normalize slashes
            if cand_norm in fp_norm:
                matched_files.add(fp)  # keep original fp for downstream lookups
    return matched_files or None