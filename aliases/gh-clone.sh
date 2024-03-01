# # gh-clone - clone directly from GitHub
## Usage:
# ```bash
# gh-clone <username>/<repo>
# ```

## Intended use:
# Clone a repository directly from GitHub,
# without having to copy the URL and then clone it

git config --global alias.gh-clone '!f() { git clone https://github.com/$1.git; }; f'
