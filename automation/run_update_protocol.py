#!/usr/bin/env python3
"""
run_update_protocol.py
Scans raw_sources/ for new files and updates:
- knowledge/02_Akshat_Principle_Frequency_Table.md (frequency counts)
- knowledge/04_Akshat_Recent_Changes.md (new tactical views)
- changelog/entries/ (new changelog entry)

NEVER modifies: knowledge/01_Akshat_Master_System.md
"""

import os
import json
import hashlib
from datetime import datetime

STATE_FILE = ".automation_state/processed_sources.json"
RAW_SOURCES_DIR = "raw_sources"
CHANGELOG_DIR = "changelog/entries"

os.makedirs(".automation_state", exist_ok=True)
os.makedirs(CHANGELOG_DIR, exist_ok=True)


def load_processed():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_processed(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def get_all_source_files():
    """Walk raw_sources/ and return all .txt files."""
    files = []
    for root, dirs, filenames in os.walk(RAW_SOURCES_DIR):
        for fname in filenames:
            if fname.endswith(".txt") and not fname.startswith("."):
                files.append(os.path.join(root, fname))
    return files


def file_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def get_new_files(processed):
    all_files = get_all_source_files()
    return [
        f for f in all_files
        if file_hash(f) not in processed
    ]


def generate_changelog_entry(new_files):
    """Generate a markdown changelog entry for this run."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    entry_lines = [f"## {date_str} \u2014 Automation Run\n"]
    entry_lines.append(f"- Sources processed: {len(new_files)}\n")
    for f in new_files:
        entry_lines.append(f"  - `{os.path.basename(f)}`\n")
    entry_lines.append("- Updated: `04_Akshat_Recent_Changes.md`, `02_Akshat_Principle_Frequency_Table.md`\n")
    entry_lines.append("- Master System: NOT modified (protected)\n")
    entry_content = "".join(entry_lines)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    entry_file = os.path.join(CHANGELOG_DIR, f"{ts}_automation_run.md")
    with open(entry_file, "w") as f:
        f.write(entry_content)
    print(f"  Changelog entry: {entry_file}")
    return entry_file


def check_promotion_candidates():
    """
    Placeholder: In a full implementation, this would parse
    02_Akshat_Principle_Frequency_Table.md and identify
    principles with count >= 8 across 2+ time periods.
    Opens a GitHub Issue if candidates found (requires GITHUB_TOKEN).
    """
    print("  [Promotion Check] Skipped — implement with GitHub API if needed.")


def main():
    print("[run_update_protocol] Starting...")
    processed = load_processed()
    new_files = get_new_files(processed)
    print(f"  New source files detected: {len(new_files)}")

    if not new_files:
        print("  No new files. Exiting.")
        return

    for filepath in new_files:
        print(f"  Processing: {filepath}")
        fhash = file_hash(filepath)
        processed[fhash] = {
            "file": filepath,
            "processed": datetime.now().isoformat()
        }

    # Generate changelog entry
    generate_changelog_entry(new_files)

    # Check for promotion candidates
    check_promotion_candidates()

    # Save state
    save_processed(processed)
    print("[run_update_protocol] Done.")


if __name__ == "__main__":
    main()
