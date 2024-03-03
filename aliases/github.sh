# github - go to the repository's home page (GitHub)
# ## Usage:
# ```bash
# git github
# ```
# Output:
# Opens the repository's home page in the default browser
# ## Intended use:
# Quickly open the repository's home page in the default browser
# **NOTE:** Requires Python to be installed

git config --global alias.github '!f() { URL=$(git remote get-url origin); python -m webbrowser -t $URL; }; f'



