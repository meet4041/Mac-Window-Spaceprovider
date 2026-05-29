#!/usr/bin/env bash
set -euo pipefail
# install.sh — bootstrap installer
# Usage (interactive):
#   curl -fsSL https://raw.githubusercontent.com/<username>/<repo>/main/install.sh | bash -s -- https://github.com/<username>/<repo>.git
# Usage (non-interactive):
#   curl -fsSL https://raw.githubusercontent.com/<username>/<repo>/main/install.sh | bash -s -- https://github.com/<username>/<repo>.git --run --yes

repo_url=""
run_now=false
auto_yes=false
keep=false
branch=""

usage() {
  cat <<EOF
Usage: $0 <repo-url> [--run] [--yes] [--keep] [--branch BRANCH]

This script clones <repo-url> into a temporary directory and then
optionally runs the repository's ./setup.sh (which in turn can run the cleaner).

Options:
  --run        Run './setup.sh --run' after cloning (still asks unless --yes set)
  --yes, -y    Skip interactive prompts (DANGEROUS)
  --keep       Do not remove the cloned temporary directory after running
  --branch BR  Clone a specific branch

When piping this script via curl|bash you must pass the repo URL as the first
argument after `-s --` (see examples above).
EOF
  exit 2
}

if [ $# -eq 0 ]; then
  usage
fi

while [ $# -gt 0 ]; do
  case "$1" in
    --run) run_now=true; shift ;;
    --yes|-y) auto_yes=true; shift ;;
    --keep) keep=true; shift ;;
    --branch) branch="$2"; shift 2 ;;
    -h|--help) usage ;;
    *)
      if [ -z "$repo_url" ]; then
        repo_url="$1"
        shift
      else
        echo "Unknown argument: $1" >&2
        usage
      fi
      ;;
  esac
done

if [ -z "$repo_url" ]; then
  echo "No repository URL provided." >&2
  usage
fi

echo
echo "WARNING: This installer will clone '$repo_url' and may execute code from it."
echo "It will ask for confirmation before running destructive actions unless --yes is given."
echo

if ! $auto_yes; then
  if [ -t 0 ] || [ -e /dev/tty ]; then
    if [ -e /dev/tty ]; then
      read -r -p "Proceed with cloning and optional setup? [y/N] " ans </dev/tty
    else
      read -r -p "Proceed with cloning and optional setup? [y/N] " ans
    fi
    case "$ans" in
      [Yy]*) ;;
      *) echo "Aborted."; exit 0 ;;
    esac
  else
    echo "No TTY available and --yes not set. Aborting for safety." >&2
    exit 1
  fi
fi

tmpdir=$(mktemp -d)
cleanup() {
  if [ "$keep" = true ]; then
    echo "Keeping cloned repo at: $tmpdir/repo"
  else
    rm -rf "$tmpdir" || true
  fi
}
trap cleanup EXIT

echo "Cloning into temporary directory..."
if [ -n "$branch" ]; then
  git clone --depth 1 -b "$branch" "$repo_url" "$tmpdir/repo"
else
  git clone --depth 1 "$repo_url" "$tmpdir/repo"
fi

cd "$tmpdir/repo"

echo "Repository cloned. Files:"
ls -la --color=auto || ls -la

if [ ! -f ./setup.sh ]; then
  echo "No ./setup.sh found in repository; nothing to run." >&2
  exit 1
fi

chmod +x ./setup.sh || true

if $run_now || $auto_yes; then
  echo "Running ./setup.sh --run (non-interactive)"
  ./setup.sh --run --yes || { echo "setup.sh failed" >&2; exit 1; }
else
  if [ -t 0 ] || [ -e /dev/tty ]; then
    if [ -e /dev/tty ]; then
      read -r -p "About to run './setup.sh --run' (may delete files). Continue? [y/N] " ans </dev/tty
    else
      read -r -p "About to run './setup.sh --run' (may delete files). Continue? [y/N] " ans
    fi
    case "$ans" in
      [Yy]*) ./setup.sh --run ;;
      *) echo "Skipped running setup.sh."; exit 0 ;;
    esac
  else
    echo "No TTY available and --yes not set. Aborting before running setup.sh." >&2
    exit 1
  fi
fi

echo "Done."
