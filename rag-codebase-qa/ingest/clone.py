# ingest/clone.py
import git, os

REPO_URL = "https://github.com/encode/httpx.git"
CLONE_PATH = "data/httpx"

if not os.path.exists(CLONE_PATH):
    repo = git.Repo.clone_from(REPO_URL, CLONE_PATH)
else:
    repo = git.Repo(CLONE_PATH)

commit_sha = repo.head.commit.hexsha
print(f"Cloned at commit {commit_sha}")

with open("data/commit_sha.txt", "w") as f:
    f.write(commit_sha)
    #Saves the commit SHA into it so you know exactly which version of the repository was indexed.