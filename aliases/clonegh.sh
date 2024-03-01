# # clonegh - clone directly from GitHub
## Usage:
# ```bash
# git clonegh <username>/<repo>
# ```
## Intended use:
# Clone a repository directly from GitHub,
# without having to copy the URL and then clone it

git config --global alias.clonegh '!f() { git clone https://github.com/$1.git; }; f'
