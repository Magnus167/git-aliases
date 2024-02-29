# # graph - Show a pretty git log with graph
# ## Usage:
# ```bash
# git graph
# ```
# Output:
# ```bash
# * 1aa688f (HEAD -> main, origin/main, origin/add_branchr, origin/HEAD, add_branchr) added branchr w comment
# * 13e46a5 (origin/add_graph, add_graph) added graph.sh
# * 0d2deab added logp
# * 8349514 added logl - log with one line
# * cb11940 added description
# * 939c655 appended description
# * 5f4efe9 Create branchc.sh
# * 5279dd5 Create pmerge.sh
# * 8f83cd7 Create README.md
# ```
# ## Intended use:
# Shorten the command to show the git log with graph

git config --global alias.graph 'log --oneline --graph --decorate'