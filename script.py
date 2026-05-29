import os
import shutil
import subprocess
import tempfile
from pathlib import Path

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


def clear_directory_contents(path):
    if not os.path.isdir(path):
        return

    try:
        entries = os.listdir(path)
    except PermissionError as e:
        print(f"[!] Skipping protected directory: {path} -> {e}")
        return
    except Exception as e:
        print(f"[!] Skipping unreadable directory: {path} -> {e}")
        return

    for item in entries:
        safe_remove(os.path.join(path, item))


# ============================================================
# 1. SYSTEM CACHE CLEANUP
# ============================================================

def clean_system_cache():
    print("\n[1] Cleaning System Cache...")

    paths = [HOME / "Library/Caches"]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 2. BROWSER CACHE CLEANUP
# ============================================================

def clean_browser_cache():
    print("\n[2] Cleaning Browser Cache...")

    browser_paths = [
        HOME / "Library/Caches/Google/Chrome",
        HOME / "Library/Caches/Firefox",
        HOME / "Library/Application Support/BraveSoftware"
    ]

    for path in browser_paths:
        clear_directory_contents(path)


# ============================================================
# 3. TRASH CLEANUP
# ============================================================

def clean_trash():
    print("\n[3] Cleaning Trash...")

    trash = HOME / ".Trash"
    clear_directory_contents(trash)


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
        clear_directory_contents(app_cache / app / "Cache")


# ============================================================
# 5. MESSAGING APP CACHE CLEANUP
# ============================================================

def clean_messaging_cache():
    print("\n[5] Cleaning Messaging App Cache...")

    paths = [
        HOME / "Library/Application Support/Slack/Cache",
        HOME / "Library/Application Support/discord/Cache"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 6. MAIL CACHE CLEANUP
# ============================================================

def clean_mail_cache():
    print("\n[6] Cleaning Mail Cache...")

    paths = [
        HOME / "Library/Containers/com.apple.mail/Data/Library/Caches"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 7. LOG FILE CLEANUP
# ============================================================

def clean_logs():
    print("\n[7] Cleaning Logs...")

    paths = [HOME / "Library/Logs"]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 8. TEMPORARY FILE CLEANUP
# ============================================================

def clean_temp_files():
    print("\n[8] Cleaning Temporary Files...")

    print(f"Skipping shared temp directory: {tempfile.gettempdir()}")
    print("Shared temp cleanup can affect other apps, so it is left untouched.")


# ============================================================
# 9. FINDER CACHE CLEANUP
# ============================================================

def clean_finder_cache():
    print("\n[9] Cleaning Finder Cache...")

    paths = [
        HOME / "Library/Caches/com.apple.finder"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 10. SYSTEM JUNK CLEANUP
# ============================================================

def clean_system_junk():
    print("\n[10] Cleaning System Junk...")

    paths = [
        HOME / "Library/Saved Application State"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 11. CRASH REPORT CLEANUP
# ============================================================

def clean_crash_reports():
    print("\n[11] Cleaning Crash Reports...")

    paths = [
        HOME / "Library/Logs/DiagnosticReports"
    ]

    for path in paths:
        clear_directory_contents(path)


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

    subprocess.run(["dscacheutil", "-flushcache"], stderr=subprocess.DEVNULL)


# ============================================================
# 14. PACKAGE MANAGER CACHE CLEANUP
# ============================================================

def clean_package_manager_cache():
    print("\n[14] Cleaning Package Manager Cache...")

    subprocess.run(["brew", "cleanup"], stderr=subprocess.DEVNULL)


# ============================================================
# 16. OLD UPDATE FILE CLEANUP
# ============================================================

def clean_old_updates():
    print("\n[15] Skipping System Update Cache...")

    print("System-wide update caches are left untouched.")


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
        clear_directory_contents(path)


# ============================================================
# 18. HIDDEN SYSTEM STORAGE ANALYZER
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
# 19. RAM OPTIMIZATION
# ============================================================

def optimize_ram():
    print("\n[19] Optimizing RAM...")

    subprocess.run(["purge"], stderr=subprocess.DEVNULL)


# ============================================================
# 20. NOTIFICATION CACHE CLEANUP
# ============================================================

def clean_notification_cache():
    print("\n[20] Cleaning Notification Cache...")

    paths = [
        HOME / "Library/Application Support/NotificationCenter"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 21. CLIPBOARD CACHE CLEANUP
# ============================================================

def clean_clipboard_cache():
    print("\n[26] Cleaning Clipboard Cache...")

    subprocess.run("pbcopy < /dev/null", shell=True)


# ============================================================
# 22. BROWSER TEMPORARY STORAGE CLEANUP
# ============================================================

def clean_browser_temp_storage():
    print("\n[22] Cleaning Browser Temporary Storage...")

    paths = [
        HOME / "Library/Application Support/Google/Chrome/Default/Code Cache"
    ]

    for path in paths:
        clear_directory_contents(path)


# ============================================================
# 23. BIN DIRECTORY CLEANUP
# ============================================================

def clean_bin_directories():
    print("\n[23] Cleaning Bin Directories...")

    bin_paths = [
        HOME / "bin",
        HOME / ".local/bin"
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
    clean_package_manager_cache()
    clean_old_updates()
    clean_cloud_cache()
    analyze_hidden_storage()
    optimize_ram()
    clean_notification_cache()
    clean_clipboard_cache()
    clean_browser_temp_storage()

    print("\n" + "=" * 60)
    print(f"TOTAL RECOVERED: {format_size(TOTAL_RECOVERED)}")
    print("CLEANUP COMPLETE")
    print("=" * 60)


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    run_all_cleanups()
