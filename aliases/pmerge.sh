# # pmerge
# ## Usage:
# ```bash
# git checkout featureX
# git pmerge main
# ```
# ## Intended use
# When merging branch `main` into `featureX`, 
# one often has to pull from `main` to ensure 
# merging into the correct head.
# Assume you're on branch `featureX`
# ```bash
# git pmerge main
# ```
# executes:
# ```bash
# BRANCH=$(git branch --show-current) # BRANCH is featureX
# git checkout main
# git pull
# git checkout BRANCH
# git merge main
# ```

git config --global alias.pmerge '!f() { BRANCH=$(git branch --show-current); git checkout "$1" && git pull && git checkout "$BRANCH" && git merge "$1"; }; f'
