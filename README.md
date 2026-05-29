# Safe Mac Cleaner — Run instructions

Quick start

- macOS / Linux:
  1. Make the launcher executable: `chmod +x run`
  2. Run: `./run`

- Alternative (module):
  - `python3 -m script`

- Windows (PowerShell):
  - `.\run.ps1`

Notes
- The `run` wrapper simply runs `script` as a module so you don't need to type `python script.py`.
- I did not execute the cleaner; run it locally when you're ready.

Publishing to GitHub
--------------------

Quick steps (recommended):

1. Configure git (if not already):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

2. Initialize, commit, and create a public repo using the GitHub CLI (fast):

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
# Replace <repo-name> with the name you want (e.g. mac-cleanup)
gh repo create <repo-name> --public --source=. --remote=origin --push
```

3. If you don't have `gh`, create the repo on github.com/new then run:

```bash
# using SSH
git remote add origin git@github.com:<username>/<repo>.git
# or using HTTPS
# git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Notes
- `gh` is optional but makes creating a public repo and pushing easier.
- Replace placeholders (`Your Name`, `you@example.com`, `<repo-name>`, `<username>`) before running.
- The repository will be public when you create it with `--public` or set visibility on the website.

