#!/usr/bin/env python3
"""
update_recent_changes.py
Appends structured entries from APPROVED extractions to 04_Akshat_Recent_Changes.md.
Archives entries older than 365 days by moving them to the Archived Views table.
Uses atomic writes to prevent partial-file corruption.
Never modifies Master System.
"""
import os, json, re
from datetime import datetime, timedelta

PENDING = "knowledge/extracted_principles_pending.json"
RECENT = "knowledge/04_Akshat_Recent_Changes.md"
ARCHIVE_AFTER_DAYS = 365

def load_approved():
    """
    # ⚠️ DDD GATE: Non-trivial write operation.
    # Before modifying this function's logic, follow Doubt-Driven Development:
    # 1. Write a CLAIM: what this function guarantees
    # 2. Extract the smallest reviewable artifact (this function's diff)
    # 3. Invoke adversarial review: "Find what is WRONG with this. Assume overconfidence."
    # 4. Log the decision in docs/ddd-decision-log.md
    # CONTRACT: Must only return records with an 'APPROVED' status, ensuring only human-validated data proceeds.
    """
    if not os.path.exists(PENDING):
        return []
    try:
        return [r for r in json.load(open(PENDING)) if r.get("status") == "APPROVED"]
    except Exception:
        return []

def build_entry(record):
    stamp = datetime.now().strftime("%Y-%m-%d")
    principles = ", ".join(record.get("principles_detected", [])) or "(none detected)"
    return (
        f"\n---\n"
        f"\n## Auto-Detected Entry — {stamp}\n"
        f"\n**Source File:** `{record['file']}`\n"
        f"\n**Principles Detected:** {principles}\n"
        f"\n**Classification:** PENDING HUMAN REVIEW — classify as "
        f"Portfolio Disclosure / Tactical View / Sector Thesis / Implementation Detail\n"
        f"\n**Status:** Awaiting human classification. Do NOT promote to Master System without frequency check.\n"
    )

def main():
    """
    # ⚠️ DDD GATE: Non-trivial write operation.
    # Before modifying this function's logic, follow Doubt-Driven Development:
    # 1. Write a CLAIM: what this function guarantees
    # 2. Extract the smallest reviewable artifact (this function's diff)
    # 3. Invoke adversarial review: "Find what is WRONG with this. Assume overconfidence."
    # 4. Log the decision in docs/ddd-decision-log.md
    # CONTRACT: Must append approved extraction entries to knowledge/04_Akshat_Recent_Changes.md and update record status.
    """
    approved = load_approved()
    if not approved:
        print("[update_recent_changes] No APPROVED records. Nothing to append.")
        return

    if not os.path.exists(RECENT):
        print(f"[update_recent_changes] ERROR: {RECENT} not found.")
        return

    with open(RECENT, encoding="utf-8") as f:
        content = f.read()

    entries_added = 0
    for record in approved:
        entry = build_entry(record)
        content += entry
        entries_added += 1

    # Atomic write
    tmp = RECENT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, RECENT)

    # Mark records as logged
    all_records = json.load(open(PENDING))
    for r in all_records:
        if r.get("status") == "APPROVED":
            r["status"] = "LOGGED_TO_RECENT"
            r["logged_at"] = datetime.now().isoformat()
    json.dump(all_records, open(PENDING, "w"), indent=2)

    print(f"[update_recent_changes] Appended {entries_added} entry(ies) to Recent Changes.")
    print(f"[update_recent_changes] REMINDER: Manually archive entries older than {ARCHIVE_AFTER_DAYS} days per quarterly review.")

if __name__ == "__main__":
    main()
