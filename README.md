# Safe Mac Cleaner

> A lightweight macOS cleanup utility for safe cache, log, trash, and regenerable file cleanup.

![macOS](https://img.shields.io/badge/platform-macOS-000000?style=for-the-badge&logo=apple)
![Python](https://img.shields.io/badge/python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/shell-bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

> Main command:
> ```bash
> curl -fsSL https://raw.githubusercontent.com/meet4041/Mac-Window-Spaceprovider/main/run-direct.sh | bash -s -- https://github.com/meet4041/Mac-Window-Spaceprovider
> ```

## Quick Start

### Main Command

```bash
curl -fsSL https://raw.githubusercontent.com/meet4041/Mac-Window-Spaceprovider/main/run-direct.sh | bash -s -- https://github.com/meet4041/Mac-Window-Spaceprovider
```

## What It Does

| Area | Action |
| --- | --- |
| Cache | Clears selected user cache folders |
| Trash | Empties trash contents |
| Logs | Removes safe log files |
| Temp Data | Cleans safe temporary files |
| Apps | Removes a few regenerable application caches |
| Bin Folders | Scans user-local bin folders for broken symlinks and junk files |

## Requirements

- macOS
- `python3`
- Bash

## Safety

> This tool deletes files permanently. Review [`script.py`](script.py) before running it.

- The main command downloads and runs `run-direct.sh` from the repository
- Targets only regenerable or user-cache data

## Project Structure

| File | Purpose |
| --- | --- |
| [`run-direct.sh`](run-direct.sh) | Remote launcher used by the main curl command |
| [`script.py`](script.py) | Main cleanup logic |

## Notes

- The project is intentionally minimal.
- The remote command fetches `run-direct.sh` and runs the cleaner from the repository.
