#!/usr/bin/env python3
"""
update_frequency_table.py
Increments frequency counts in 02_Akshat_Principle_Frequency_Table.md
ONLY from human-APPROVED extraction records.
Never modifies Master System.
Uses atomic writes to prevent partial corruption.
"""
import os, json, re
from datetime import datetime

PENDING = "knowledge/extracted_principles_pending.json"
FREQ = "knowledge/02_Akshat_Principle_Frequency_Table.md"

# Maps detected keywords → Principle IDs in frequency table
KEYWORD_TO_PID = {
    "barbell": "PC-01",
    "barbell portfolio": "PC-01",
    "position sizing": "RM-01",
    "200dma": "SS-04",
    "200 dma": "SS-04",
    "20-40% correction": "SS-04",
    "covered call": "OP-01",
    "cash-secured put": "OP-02",
    "cash secured put": "OP-02",
    "naked option": "OP-03",
    "naked call": "OP-03",
    "real return": "CP-03",
    "inr depreciation": "GF-02",
    "INR depreciation": "GF-02",
    "earnings growth": "SS-01",
    "EPS": "SS-01",
    "global liquidity": "MF-01",
    "dry powder": "PC-04",
    "diversif": "CP-01",
    "valuation": "CP-04",
    "portfolio weight": "PC-05",
    "parabolic": "SS-05",
    "moat": "SS-07",
    "k-shaped": "GF-05",
    "20 stocks": "PC-06",
    "structural damage": "MF-02",
    "v-shaped": "MF-02",
    "operating leverage": "SS-03",
    "margin expansion": "SS-03",
    "hard asset": "CP-01",
}

def load_approved():
    if not os.path.exists(PENDING):
        return []
    try:
        return [r for r in json.load(open(PENDING)) if r.get("status") == "APPROVED"]
    except Exception:
        return []

def increment_count(content, pid):
    """Find the table row for pid and increment its Count column."""
    pattern = re.compile(
        r'(\|\s*' + re.escape(pid) + r'\s*\|[^|]+\|\s*)(\d+)(\s*\|)',
        re.MULTILINE
    )
    changed = False
    def bump(m):
        nonlocal changed
        changed = True
        return m.group(1) + str(int(m.group(2)) + 1) + m.group(3)
    new_content = pattern.sub(bump, content)
    return new_content, changed

def main():
    """
    # ⚠️ DDD GATE: Non-trivial write operation.
    # Before modifying this function's logic, follow Doubt-Driven Development:
    # 1. Write a CLAIM: what this function guarantees
    # 2. Extract the smallest reviewable artifact (this function's diff)
    # 3. Invoke adversarial review: "Find what is WRONG with this. Assume overconfidence."
    # 4. Log the decision in docs/ddd-decision-log.md
    # CONTRACT: Principle counts in knowledge/02_Akshat_Principle_Frequency_Table.md must only be incremented for human-approved records.
    """
    approved = load_approved()
    if not approved:
        print("[update_frequency_table] No APPROVED records found. Set status='APPROVED' in pending JSON.")
        return

    with open(FREQ, encoding="utf-8") as f:
        content = f.read()

    updated_ids = set()
    for record in approved:
        for kw in record.get("principles_detected", []):
            pid = KEYWORD_TO_PID.get(kw) or KEYWORD_TO_PID.get(kw.lower())
            if pid and pid not in updated_ids:
                content, changed = increment_count(content, pid)
                if changed:
                    updated_ids.add(pid)
                    print(f"  [freq] Incremented {pid} (keyword: {kw})")

    if updated_ids:
        # Atomic write
        tmp = FREQ + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp, FREQ)
        print(f"[update_frequency_table] Updated {len(updated_ids)} principle(s).")

        # Mark processed records
        all_records = json.load(open(PENDING))
        for r in all_records:
            if r.get("status") == "APPROVED":
                r["status"] = "PROCESSED"
                r["processed_at"] = datetime.now().isoformat()
        json.dump(all_records, open(PENDING, "w"), indent=2)
    else:
        print("[update_frequency_table] No matching principle IDs found — no changes made.")

if __name__ == "__main__":
    main()
