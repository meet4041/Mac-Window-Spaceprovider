#!/usr/bin/env bash
set -euo pipefail

chmod +x run || true
echo "Wired: 'run' is executable."

run_now=false
auto_yes=false

for arg in "$@"; do
  case "$arg" in
    --run) run_now=true ;;
    --yes|-y) auto_yes=true ;;
    *)
      echo "Unknown argument: $arg" >&2
      exit 2
      ;;
  esac
done

if [ "$run_now" = true ]; then
  if [ "$auto_yes" = true ]; then
    echo "Running without confirmation..."
    ./run
  else
    printf "This will run the cleaner which may remove files. Continue? [y/N] "
    read -r ans
    case "$ans" in
      [Yy]*) ./run ;;
      *) echo "Aborted." ; exit 0 ;;
    esac
  fi
else
  echo "To run now: ./setup.sh --run"
fi
