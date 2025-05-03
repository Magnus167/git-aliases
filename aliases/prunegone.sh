# # prunegone
# ## Usage:
# ```bash
# git prunegone
# ```
# ## Intended use
# Use this alias to delete all branches that are gone on the remote.
# It does not delete branches that are not gone on the remote, or are
# not on the remote at all.
# 
# Running this alias executes:
# ```bash
# git fetch --prune
# git branch -vv | awk "/: gone]/{print \$1}" | xargs -r git branch -d
# ```

git config --global alias.prunegone '!git fetch --prune && git branch -vv | awk "/: gone]/{print \$1}" | xargs -r git branch -d'
