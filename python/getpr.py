import json
import urllib.request
import sys

# get repo and branch from sys.argv
if len(sys.argv) < 3:
    print("Usage: python getpr.py <repo> <branch>")
    sys.exit(1)

REPO = sys.argv[1].strip()
BRANCH = sys.argv[2].strip()

repo = REPO.replace(".git", "").replace("https://github.com/", "")
print("\nrepo:", repo, "\nbranch:", BRANCH, "\n")

found = False
groups = [[], []]
for ix, ux in enumerate(
    [
        {
            "url": dx["html_url"],
            "title": dx["title"],
            "base": dx["base"]["ref"],
            "head": dx["head"]["ref"],
        }
        for dx in json.loads(
            urllib.request.urlopen(
                urllib.request.Request(f"https://api.github.com/repos/{repo}/pulls")
            )
            .read()
            .decode("utf-8")
        )
        # if (dx["head"]["ref"] == BRANCH or dx["base"]["ref"] == BRANCH)
    ]
):
    if BRANCH in [ux["base"], ux["head"]]:
        found = True
        groups[0 if ux["head"] == BRANCH else 1].append(ux)


if not found:
    print("No pull request found for branch", BRANCH, "in", REPO)
    sys.exit(1)


def _fprint(group: list, msg: str):
    if len(group) == 0:
        return
    print(msg)
    for ix, ux in enumerate(group):
        print("\t", f"{ix+1}. ", end="")
        print(ux["title"], "#" + ux["url"].split("/")[-1])
        print("\t\t", f"[{ux['base']} ← {ux['head']}]")
        print("\t\t", "URL:", ux["url"], "\n")


_fprint(groups[0], "PRs from branch:")
_fprint(groups[1], "PRs to branch:")
