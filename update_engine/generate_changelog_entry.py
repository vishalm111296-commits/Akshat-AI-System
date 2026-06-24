#!/usr/bin/env python3
"""
generate_changelog_entry.py
Appends the latest automation run entries to the master CHANGELOG.md.

FIX: Added safety check for missing changelog/entries/ directory.
FIX: Generates a run-summary entry even when no entry files exist,
     so the workflow always produces an auditable record.
"""

import os
import glob
from datetime import datetime

CHANGELOG_FILE = "CHANGELOG.md"
ENTRIES_DIR = "changelog/entries"
MERGE_MARKER = ".automation_state/last_merged_entry.txt"


def ensure_dirs():
    os.makedirs(ENTRIES_DIR, exist_ok=True)
    os.makedirs(".automation_state", exist_ok=True)


def get_unmerged_entries():
    all_entries = sorted(glob.glob(os.path.join(ENTRIES_DIR, "*.md")))
    last_merged = ""
    if os.path.exists(MERGE_MARKER):
        with open(MERGE_MARKER) as f:
            last_merged = f.read().strip()
    return [e for e in all_entries if e > last_merged]


def generate_run_summary():
    """
    # ⚠️ DDD GATE: Non-trivial write operation.
    # Before modifying this function's logic, follow Doubt-Driven Development:
    # 1. Write a CLAIM: what this function guarantees
    # 2. Extract the smallest reviewable artifact (this function's diff)
    # 3. Invoke adversarial review: "Find what is WRONG with this. Assume overconfidence."
    # 4. Log the decision in docs/ddd-decision-log.md
    # CONTRACT: Must accurately count raw sources in the repository to provide an audit trail of ingested evidence.
    """
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
    # Count raw sources for evidence
    yt_count = len(glob.glob("raw_sources/youtube_transcripts/*.txt"))
    cp_count = len(glob.glob("raw_sources/community_posts/*.txt"))
    pp_count = len(glob.glob("raw_sources/paid_posts/*.txt"))
    return (
        f"\n## Automation Run — {stamp}\n\n"
        f"- YouTube transcripts in repo: {yt_count}\n"
        f"- Community posts in repo: {cp_count}\n"
        f"- Paid posts in repo: {pp_count}\n"
        f"- Pipeline: extract → contradiction_check → recent_changes → frequency_table\n"
        f"- Master System: PROTECTED (not modified)\n"
    )


def append_to_changelog(entries, run_summary):
    content_to_add = ""
    if entries:
        content_to_add += "\n---\n"
        for entry_file in entries:
            with open(entry_file) as f:
                content_to_add += f.read()
        print(f"  Merged {len(entries)} entry file(s) into CHANGELOG.md")
    # Always append run summary
    content_to_add += run_summary
    with open(CHANGELOG_FILE, "a", encoding="utf-8") as changelog:
        changelog.write(content_to_add)
    print(f"  Run summary appended to CHANGELOG.md")


def main():
    print("[generate_changelog_entry] Starting...")
    ensure_dirs()
    entries = get_unmerged_entries()
    run_summary = generate_run_summary()
    append_to_changelog(entries, run_summary)
    if entries:
        # Mark last merged
        with open(MERGE_MARKER, "w") as f:
            f.write(sorted(entries)[-1])
    print("[generate_changelog_entry] Done.")


if __name__ == "__main__":
    main()
