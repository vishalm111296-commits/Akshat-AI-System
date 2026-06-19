#!/usr/bin/env python3
"""
generate_changelog_entry.py
Appends the latest automation run entries to the master CHANGELOG.md.
"""

import os
import glob
from datetime import datetime

CHANGELOG_FILE = "CHANGELOG.md"
ENTRIES_DIR = "changelog/entries"


def get_unmerged_entries():
    """Get all entry files not yet merged into CHANGELOG.md."""
    merged_marker = ".automation_state/last_merged_entry.txt"
    all_entries = sorted(glob.glob(os.path.join(ENTRIES_DIR, "*.md")))
    last_merged = ""
    if os.path.exists(merged_marker):
        with open(merged_marker) as f:
            last_merged = f.read().strip()
    return [e for e in all_entries if e > last_merged], merged_marker


def append_to_changelog(entries):
    """Append entries to CHANGELOG.md."""
    if not entries:
        print("  No new entries to merge.")
        return

    with open(CHANGELOG_FILE, "a") as changelog:
        changelog.write("\n---\n")
        for entry_file in entries:
            with open(entry_file) as f:
                changelog.write(f.read())
    print(f"  Merged {len(entries)} entry(ies) into CHANGELOG.md")


def main():
    print("[generate_changelog_entry] Starting...")
    entries, marker = get_unmerged_entries()
    append_to_changelog(entries)
    if entries:
        with open(marker, "w") as f:
            f.write(sorted(entries)[-1])
    print("[generate_changelog_entry] Done.")


if __name__ == "__main__":
    main()
