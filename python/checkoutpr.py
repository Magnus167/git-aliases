import json
import urllib.request
import sys

# get repo and branch from sys.argv
if len(sys.argv) < 3:
    print("Usage: python getpr.py <repo> <branch>")
    sys.exit(1)

REPO = sys.argv[1].strip()
PRNUM = sys.argv[2].strip()

repo = REPO.replace(".git", "").replace("https://github.com/", "")

found = False
groups = [[], []]
for ix, ux in enumerate(
    [
        # branch name:
        dx["head"]["ref"]
        for dx in json.loads(
            urllib.request.urlopen(
                urllib.request.Request(f"https://api.github.com/repos/{repo}/pulls")
            )
            .read()
            .decode("utf-8")
        )
        if dx["number"] == int(PRNUM)
    ]
):
    print(ux, end="")
    found = True
    
if not found:
    print(f"No PR found for {REPO} and {PRNUM}")
    sys.exit(1)
