# # logl - log with one line
# ## Usage:
# ```bash
# git logl
# ```
# Output:
# ```bash
# cb11940 (HEAD -> main) added description
# 939c655 appended description
# 5f4efe9 (origin/main, origin/HEAD) Create branchc.sh
# 5279dd5 Create pmerge.sh
# 8f83cd7 Create README.md
# ```
# ## Intended use:
# Shorten the command to show the git log with one line
# per commit.

git config --global alias.logl 'log --oneline'