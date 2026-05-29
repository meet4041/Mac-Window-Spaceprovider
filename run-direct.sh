#!/usr/bin/env bash
set -euo pipefail
# run-direct.sh — fetch and execute `script.py` from a GitHub repo WITHOUT cloning
# Usage:
#   ./run-direct.sh https://github.com/owner/repo
#   ./run-direct.sh https://github.com/owner/repo --branch my-branch --yes

if [ $# -lt 1 ]; then
  echo "Usage: $0 <github-repo-url> [--branch BRANCH] [--yes|-y]" >&2
  exit 2
fi

repo_url="$1"
shift

branch="main"
auto_yes=false
while (( $# )); do
  case "$1" in
    --branch) branch="$2"; shift 2 ;;
    --yes|-y) auto_yes=true; shift ;;
    *) shift ;;
  esac
done

# normalize: accept git@ and https forms
repo_path="$repo_url"
repo_path="${repo_path#git@github.com:}"
repo_path="${repo_path#https://github.com/}"
repo_path="${repo_path#http://github.com/}"
repo_path="${repo_path%.git}"
repo_path="${repo_path%/}"

if [[ "$repo_path" != */* ]]; then
  echo "Invalid GitHub repository URL: $repo_url" >&2
  exit 2
fi

owner=$(echo "$repo_path" | cut -d/ -f1)
repo=$(echo "$repo_path" | cut -d/ -f2)
raw_url="https://raw.githubusercontent.com/$owner/$repo/$branch/script.py"

echo "About to fetch and run: $raw_url"

if [ "$auto_yes" != true ]; then
  if [ -e /dev/tty ]; then
    read -r -p "This will execute code from the remote repository and may delete files. Continue? [y/N] " ans </dev/tty
  else
    read -r -p "This will execute code from the remote repository and may delete files. Continue? [y/N] " ans
  fi
  case "$ans" in
    [Yy]*) ;;
    *) echo "Aborted."; exit 0 ;;
  esac
fi

echo "Downloading and executing..."
curl -fsSL "$raw_url" | python3 -
