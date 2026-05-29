#!/usr/bin/env bash
set -euo pipefail
# Setup script: make 'run' executable and optionally execute it.
# Usage:
#   ./setup.sh            # make 'run' executable only
#   ./setup.sh --run      # prompt and then run the cleaner
#   ./setup.sh --run --yes  # run non-interactively (DANGEROUS)

chmod +x run || true
echo "Wired: 'run' is executable."

run_now=false
auto_yes=false
run_args=()

for arg in "$@"; do
  case "$arg" in
    --run) run_now=true ;;
    --yes|-y) auto_yes=true ;;
    *) run_args+=("$arg") ;;
  esac
done

if [ "$run_now" = true ]; then
  if [ "$auto_yes" = true ]; then
    echo "Running without confirmation..."
    ./run "${run_args[@]}"
  else
    printf "This will run the cleaner which may remove files. Continue? [y/N] "
    read -r ans
    case "$ans" in
      [Yy]*) ./run "${run_args[@]}" ;;
      *) echo "Aborted." ; exit 0 ;;
    esac
  fi
else
  echo "To run now: ./setup.sh --run"
fi
