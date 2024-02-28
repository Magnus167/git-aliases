# # logp - pretty log
# ## Usage:
# ```bash
# git logp
# ```
# Output:
# ```bash
# 8349514 - (HEAD -> main, origin/main, origin/HEAD) added logl - log with one line (2 minutes ago) [Palash Tyagi]
# cb11940 - added description (6 minutes ago) [Palash Tyagi]
# 939c655 - appended description (6 minutes ago) [Palash Tyagi]
# 5f4efe9 - Create branchc.sh (18 hours ago) [Palash Tyagi]
# 5279dd5 - Create pmerge.sh (18 hours ago) [Palash Tyagi]
# 8f83cd7 - Create README.md (18 hours ago) [Palash Tyagi]
# ```
# ## Intended use:
# Shorten the command to show the git log with a pretty format.

git config --global alias.logp !git log --pretty=format:\"%C(magenta)%h%Creset -%C(red)%d%Creset %s %C(dim green)(%cr) [%an]\" --abbrev-commit -30