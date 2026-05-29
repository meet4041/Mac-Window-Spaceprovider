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

Clone & run (for repo visitors)
--------------------------------

After someone clones your repo they can wire and run quickly:

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
./setup.sh --run
```

One-liner (runs the cleaner after wiring; will prompt for confirmation unless you pass `--yes`):

```bash
git clone https://github.com/<username>/<repo>.git && cd <repo> && ./setup.sh --run
```

Notes & safety
- `./setup.sh` makes `run` executable. `--run` will execute the cleaner and may delete files.
- Do NOT pipe remote scripts to `bash` from unknown sources. If you want a curl|bash one-liner, add it explicitly but be aware of the risks.
- Replace `<username>` and `<repo>` with your GitHub values before publishing.

Remote install (one-liner)
--------------------------

If you want visitors to be able to copy your GitHub URL and run a single command, provide the following one-liner (replace placeholders):

```bash
# Interactive (recommended):
curl -fsSL https://raw.githubusercontent.com/<username>/<repo>/main/install.sh | bash -s -- https://github.com/<username>/<repo>.git

# Non-interactive (DANGEROUS — will skip prompts):
curl -fsSL https://raw.githubusercontent.com/<username>/<repo>/main/install.sh | bash -s -- https://github.com/<username>/<repo>.git --run --yes
```

What the one-liner does:
- Downloads `install.sh` from the repository and runs it with `bash`.
- `install.sh` clones the repository to a temporary directory and (if confirmed) runs `./setup.sh --run` from the cloned repo.

Safety notes
- Never encourage running these one-liners on untrusted machines or from untrusted sources.
- The installer prompts by default; `--yes` disables prompts and is only for automation where you explicitly accept the risk.
- If you'd prefer not to support direct piping, users can still run the safe clone-and-run sequence documented above.



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

