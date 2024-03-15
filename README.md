# git-aliases
Cool git aliases that I find useful in daily life

# `.gitconfig`

```gitconfig
[alias]
	fame = !python -m gitfame
	pmerge = "!f() { BRANCH=$(git branch --show-current); git checkout $1 && git pull && git checkout $BRANCH && git merge $1; }; f"
	staash = stash --all
	github = "!f() { URL=$(git remote get-url origin); python -m webbrowser -t $URL; }; f"
	branchc = branch --show-current
	clonegh = "!f() { git clone https://github.com/$1.git; }; f"
	co = checkout
	cop = "!f() { git checkout $1 && git pull; }; f"
	cob = checkout -b
	branchr = branch --sort=-committerdate
	pr = "!f() { BRANCH=$(git branch --show-current); REPOURL=$(git config --get remote.origin.url); python ~/Code/work_HK/getpr.py $REPOURL $BRANCH; }; f"
	co-pr = "!f() { REPOURL=$(git config --get remote.origin.url); BRANCH=$(python ~/Code/work_HK/checkoutpr.py $REPOURL $1); git checkout $BRANCH; git pull; }; f"
```
