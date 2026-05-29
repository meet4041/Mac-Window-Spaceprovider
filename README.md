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

### Local Run

1. Make the launcher executable:

   ```bash
   chmod +x run
   ```

2. Run the cleaner:

   ```bash
   ./run
   ```

3. Optional setup flow:

   ```bash
   ./setup.sh
   ./setup.sh --run
   ```

Windows:

```powershell
.\run.ps1
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

- Designed for local use only
- The main command downloads and runs `run-direct.sh` from the repository
- Targets only regenerable or user-cache data

## Project Structure

| File | Purpose |
| --- | --- |
| [`run`](run) | Local launcher for the cleaner |
| [`setup.sh`](setup.sh) | Makes `run` executable and can launch the cleaner |
| [`run-direct.sh`](run-direct.sh) | Remote launcher used by the main curl command |
| [`run.ps1`](run.ps1) | PowerShell launcher |
| [`script.py`](script.py) | Main cleanup logic |

## Notes

- `run` launches `script.py` through `python3 -m script`.
- `setup.sh` is intentionally minimal.
- The project is meant to stay local and simple.
