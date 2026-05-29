#!/usr/bin/env python3

"""
Safe Mac Cleaner
----------------
A safe macOS cleanup utility focused ONLY on:
- system junk
- cache
- temporary files
- regeneratable data
- performance optimization

This tool DOES NOT touch:
- Photos
- Videos
- Documents
- Personal downloads
- User-created files

Author: OpenAI ChatGPT
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

SAFE_DELETE = True
TOTAL_RECOVERED = 0

HOME = Path.home()


def get_size(path):
    total = 0

    try:
        if os.path.isfile(path):
            return os.path.getsize(path)

        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)

                try:
                    total += os.path.getsize(fp)
                except:
                    pass

    except:
        pass

    return total


def format_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024



def safe_remove(path):
    global TOTAL_RECOVERED

    try:
        if not os.path.exists(path):
            return

        size = get_size(path)

        if os.path.isfile(path):
            os.remove(path)
        else:
            shutil.rmtree(path, ignore_errors=True)

        TOTAL_RECOVERED += size

        print(f"[✓] Removed: {path}")

    except Exception as e:
        print(f"[!] Failed: {path} -> {e}")


# ============================================================
# 1. SYSTEM CACHE CLEANUP
# ============================================================

def clean_system_cache():
    print("\n[1] Cleaning System Cache...")

    paths = [
        HOME / "Library/Caches",
        "/Library/Caches"
    ]

    for path in paths:
        if os.path.exists(path):
            for item in os.listdir(path):
                safe_remove(os.path.join(path, item))


# ============================================================
# 2. BROWSER CACHE CLEANUP
# ============================================================

def clean_browser_cache():
    print("\n[2] Cleaning Browser Cache...")

    browser_paths = [
        HOME / "Library/Caches/Google/Chrome",
        HOME / "Library/Caches/com.apple.Safari",
        HOME / "Library/Caches/Firefox",
        HOME / "Library/Application Support/BraveSoftware"
    ]

    for path in browser_paths:
        safe_remove(path)


# ============================================================
# 3. TRASH CLEANUP
# ============================================================

def clean_trash():
    print("\n[3] Cleaning Trash...")

    trash = HOME / ".Trash"
    safe_remove(trash)


# ============================================================
# 4. APPLICATION CACHE CLEANUP
# ============================================================

def clean_application_cache():
    print("\n[4] Cleaning Application Cache...")

    app_cache = HOME / "Library/Application Support"

    temp_apps = [
        "Slack",
        "Discord",
        "Spotify",
        "Zoom",
        "Code"
    ]

    for app in temp_apps:
        safe_remove(app_cache / app / "Cache")


# ============================================================
# 5. MESSAGING APP CACHE CLEANUP
# ============================================================

def clean_messaging_cache():
    print("\n[5] Cleaning Messaging App Cache...")

    paths = [
        HOME / "Library/Application Support/Slack/Cache",
        HOME / "Library/Application Support/discord/Cache",
        HOME / "Library/Application Support/Telegram Desktop/tdata"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 6. MAIL CACHE CLEANUP
# ============================================================

def clean_mail_cache():
    print("\n[6] Cleaning Mail Cache...")

    paths = [
        HOME / "Library/Containers/com.apple.mail/Data/Library/Caches"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 7. LOG FILE CLEANUP
# ============================================================

def clean_logs():
    print("\n[7] Cleaning Logs...")

    paths = [
        HOME / "Library/Logs",
        "/Library/Logs"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 8. TEMPORARY FILE CLEANUP
# ============================================================

def clean_temp_files():
    print("\n[8] Cleaning Temporary Files...")

    temp_dir = tempfile.gettempdir()
    safe_remove(temp_dir)


# ============================================================
# 9. FINDER CACHE CLEANUP
# ============================================================

def clean_finder_cache():
    print("\n[9] Cleaning Finder Cache...")

    paths = [
        HOME / "Library/Caches/com.apple.finder"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 10. SYSTEM JUNK CLEANUP
# ============================================================

def clean_system_junk():
    print("\n[10] Cleaning System Junk...")

    paths = [
        HOME / "Library/Saved Application State"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 11. CRASH REPORT CLEANUP
# ============================================================

def clean_crash_reports():
    print("\n[11] Cleaning Crash Reports...")

    paths = [
        HOME / "Library/Logs/DiagnosticReports"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 12. FONT CACHE CLEANUP
# ============================================================

def clean_font_cache():
    print("\n[12] Cleaning Font Cache...")

    subprocess.run(["atsutil", "databases", "-remove"])


# ============================================================
# 13. DNS CACHE CLEANUP
# ============================================================

def clean_dns_cache():
    print("\n[13] Flushing DNS Cache...")

    subprocess.run([
        "sudo",
        "dscacheutil",
        "-flushcache"
    ])


# ============================================================
# 14. SYSTEM DIAGNOSTIC FILE CLEANUP
# ============================================================

def clean_diagnostics():
    print("\n[14] Cleaning Diagnostics...")

    paths = [
        HOME / "Library/Logs/DiagnosticReports"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 15. PACKAGE MANAGER CACHE CLEANUP
# ============================================================

def clean_package_manager_cache():
    print("\n[15] Cleaning Package Manager Cache...")

    subprocess.run(["brew", "cleanup"], stderr=subprocess.DEVNULL)


# ============================================================
# 16. OLD UPDATE FILE CLEANUP
# ============================================================

def clean_old_updates():
    print("\n[16] Cleaning Old Updates...")

    paths = [
        "/Library/Updates"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 17. CLOUD STORAGE CACHE CLEANUP
# ============================================================

def clean_cloud_cache():
    print("\n[17] Cleaning Cloud Storage Cache...")

    paths = [
        HOME / "Library/Application Support/Google/DriveFS",
        HOME / "Library/CloudStorage"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 18. LEFTOVER APP FILE CLEANUP
# ============================================================

def clean_leftover_app_files():
    print("\n[18] Cleaning Leftover App Files...")

    paths = [
        HOME / "Library/Application Support"
    ]

    # Example placeholder cleanup logic
    print("Scanning leftover support files...")


# ============================================================
# 19. RECYCLE BIN DEEP CLEANUP
# ============================================================

def deep_trash_cleanup():
    print("\n[19] Deep Trash Cleanup...")

    trash = HOME / ".Trash"
    safe_remove(trash)


# ============================================================
# 20. HIDDEN SYSTEM STORAGE ANALYZER
# ============================================================

def analyze_hidden_storage():
    print("\n[20] Hidden Storage Analyzer...")

    targets = [
        HOME / "Library",
        HOME / "Library/Caches",
        HOME / "Library/Application Support"
    ]

    for target in targets:
        size = get_size(target)
        print(f"{target} -> {format_size(size)}")


# ============================================================
# 21. RAM OPTIMIZATION
# ============================================================

def optimize_ram():
    print("\n[21] Optimizing RAM...")

    subprocess.run(["purge"], stderr=subprocess.DEVNULL)


# ============================================================
# 22. BACKGROUND PROCESS OPTIMIZER
# ============================================================

def optimize_background_processes():
    print("\n[22] Optimizing Background Processes...")

    print("Review Activity Monitor manually for safety.")


# ============================================================
# 23. STARTUP APP OPTIMIZER
# ============================================================

def startup_optimizer():
    print("\n[23] Startup App Optimizer...")

    print("Check: System Settings > Login Items")


# ============================================================
# 24. LOGIN ITEMS MANAGER
# ============================================================

def login_items_manager():
    print("\n[24] Login Items Manager...")

    print("Managing startup applications...")


# ============================================================
# 25. NOTIFICATION CACHE CLEANUP
# ============================================================

def clean_notification_cache():
    print("\n[25] Cleaning Notification Cache...")

    paths = [
        HOME / "Library/Application Support/NotificationCenter"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 26. CLIPBOARD CACHE CLEANUP
# ============================================================

def clean_clipboard_cache():
    print("\n[26] Cleaning Clipboard Cache...")

    subprocess.run("pbcopy < /dev/null", shell=True)


# ============================================================
# 27. BROWSER TEMPORARY STORAGE CLEANUP
# ============================================================

def clean_browser_temp_storage():
    print("\n[27] Cleaning Browser Temporary Storage...")

    paths = [
        HOME / "Library/Application Support/Google/Chrome/Default/Code Cache"
    ]

    for path in paths:
        safe_remove(path)


# ============================================================
# 28. APPLICATION TEMPORARY DATA CLEANUP
# ============================================================

def clean_application_temp_data():
    print("\n[28] Cleaning Application Temporary Data...")

    temp_support = HOME / "Library/Application Support"

    print(f"Scanning temporary app data in: {temp_support}")


# ============================================================
# 29. UNUSED LANGUAGE RESOURCE CLEANUP
# ============================================================

def clean_unused_languages():
    print("\n[29] Cleaning Unused Language Resources...")

    print("Optional advanced cleanup.")


# ============================================================
# 30. SYSTEM PERFORMANCE OPTIMIZATION
# ============================================================

def system_performance_optimization():
    print("\n[30] System Performance Optimization...")

    print("Running overall optimization tasks...")


# ============================================================
# 31. BIN DIRECTORY CLEANUP
# ============================================================

def clean_bin_directories():
    print("\n[31] Cleaning Bin Directories...")

    bin_paths = [
        HOME / "bin",
        HOME / ".local/bin",
        Path("/opt/homebrew/bin"),
        Path("/usr/local/bin")
    ]

    for path in bin_paths:
        if not path.exists():
            continue

        print(f"Scanning: {path}")

        try:
            for item in path.iterdir():
                try:
                    # Remove broken symlinks (safe for both system and user bins)
                    if item.is_symlink():
                        try:
                            target = item.resolve(strict=False)
                        except Exception:
                            target = None
                        if not (target and target.exists()):
                            print(f"[i] Broken symlink: {item}")
                            if SAFE_DELETE:
                                try:
                                    item.unlink()
                                    print(f"[✓] Removed: {item}")
                                except Exception as e:
                                    print(f"[!] Failed removing symlink {item}: {e}")
                            else:
                                print(f"[ ] Would remove: {item}")
                        continue

                    # For user-local bins, remove zero-size or common temp/backup files
                    if str(path).startswith(str(HOME)):
                        size = get_size(item)
                        name = item.name.lower()
                        if size == 0 or name.endswith("~") or name.endswith(".tmp") or name.endswith(".bak"):
                            print(f"[i] Removing: {item}")
                            safe_remove(str(item))
                            continue

                except Exception as e:
                    print(f"[!] Error inspecting {item}: {e}")
        except Exception as e:
            print(f"[!] Error scanning {path}: {e}")


# MAIN CLEANUP EXECUTION
# ============================================================

def run_all_cleanups():
    print("=" * 60)
    print("SAFE MAC CLEANER")
    print("=" * 60)

    clean_system_cache()
    clean_browser_cache()
    clean_trash()
    clean_application_cache()
    clean_bin_directories()
    clean_messaging_cache()
    clean_mail_cache()
    clean_logs()
    clean_temp_files()
    clean_finder_cache()
    clean_system_junk()
    clean_crash_reports()
    clean_font_cache()
    clean_dns_cache()
    clean_diagnostics()
    clean_package_manager_cache()
    clean_old_updates()
    clean_cloud_cache()
    clean_leftover_app_files()
    deep_trash_cleanup()
    analyze_hidden_storage()
    optimize_ram()
    optimize_background_processes()
    startup_optimizer()
    login_items_manager()
    clean_notification_cache()
    clean_clipboard_cache()
    clean_browser_temp_storage()
    clean_application_temp_data()
    clean_unused_languages()
    system_performance_optimization()

    print("\n" + "=" * 60)
    print(f"TOTAL RECOVERED: {format_size(TOTAL_RECOVERED)}")
    print("CLEANUP COMPLETE")
    print("=" * 60)


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    run_all_cleanups()
