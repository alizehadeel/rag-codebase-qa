# ingest/fetch_issues.py — needs no auth for public repo read, but rate-limited without a token
import requests, json

def fetch_issues(owner, repo, max_pages=5):
    issues = []
    for page in range(1, max_pages + 1):
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        resp = requests.get(url, params={"state": "all", "per_page": 50, "page": page})
        batch = resp.json()
        if not batch:
            break
        issues.extend([i for i in batch if "pull_request" not in i])  # exclude PRs
    return issues

issues = fetch_issues("encode", "httpx")
with open("data/issues.jsonl", "w") as f:
    for i in issues:
        f.write(json.dumps({"number": i["number"], "title": i["title"], "body": i.get("body") or ""}) + "\n")

print(f"Fetched {len(issues)} issues")