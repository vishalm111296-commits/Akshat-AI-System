#!/usr/bin/env python3
"""
contradiction_checker.py
Detects potential contradictions between recent source extractions
and established doctrine. Writes a contradiction report.
Never modifies Master System or Frequency Table.
"""
import os, json
from datetime import datetime

PENDING = "knowledge/extracted_principles_pending.json"
REPORT = "knowledge/contradiction_report.md"

# Pairs: if BOTH terms appear in same source file → flag as potential conflict
CONTRADICTION_PAIRS = [
    ("naked option", "covered call only"),
    ("naked call", "covered call"),
    ("long-duration bond", "avoid long-duration bond"),
    ("blind sip", "valuation matters for sip"),
    ("buy real estate heavily", "20% illiquid maximum"),
    ("ignore valuation", "valuation"),
    ("all in", "diversif"),
]

# Negation markers — if keyword appears near these, likely a contradiction
NEGATION_MARKERS = [
    "never", "avoid", "do not", "don't", "prohibited", "banned",
    "against", "not recommended", "stay away", "stop"
]

def check_negation_context(text, keyword):
    idx = text.lower().find(keyword.lower())
    if idx == -1:
        return False
    window = text[max(0, idx - 80):idx].lower()
    return any(neg in window for neg in NEGATION_MARKERS)

def main():
    """
    # ⚠️ DDD GATE: Non-trivial write operation.
    # Before modifying this function's logic, follow Doubt-Driven Development:
    # 1. Write a CLAIM: what this function guarantees
    # 2. Extract the smallest reviewable artifact (this function's diff)
    # 3. Invoke adversarial review: "Find what is WRONG with this. Assume overconfidence."
    # 4. Log the decision in docs/ddd-decision-log.md
    # CONTRACT: Must identify and report potential contradictions in knowledge/contradiction_report.md before any doctrine updates.
    """
    if not os.path.exists(PENDING):
        print("[contradiction_checker] No pending extractions found. Run extract_principles.py first.")
        return

    try:
        records = json.load(open(PENDING))
    except Exception as e:
        print(f"[contradiction_checker] Could not read pending file: {e}")
        return

    flags = []

    for record in records:
        fpath = record.get("file", "")
        if not os.path.exists(fpath):
            continue
        try:
            with open(fpath, encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception:
            continue

        # Check contradiction pairs
        for kw_a, kw_b in CONTRADICTION_PAIRS:
            if kw_a.lower() in text.lower() and kw_b.lower() in text.lower():
                flags.append({
                    "file": fpath,
                    "conflict": f"Both '{kw_a}' and '{kw_b}' appear together",
                    "severity": "HIGH",
                    "timestamp": datetime.now().isoformat()
                })

        # Check negation context for detected principles
        for kw in record.get("principles_detected", []):
            if check_negation_context(text, kw):
                flags.append({
                    "file": fpath,
                    "conflict": f"Keyword '{kw}' appears near negation language",
                    "severity": "MEDIUM",
                    "timestamp": datetime.now().isoformat()
                })

    lines = [
        f"# Contradiction Report\n",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')} UTC*\n",
        f"*Files scanned: {len(records)}*\n",
        "\n---\n"
    ]

    if flags:
        lines.append(f"## ⚠️ {len(flags)} Potential Contradiction(s) Detected\n")
        lines.append("> All items below require **human review** before any frequency increment.\n")
        for i, fl in enumerate(flags, 1):
            lines.append(
                f"\n### Flag {i} — {fl['severity']}\n"
                f"- **File:** `{fl['file']}`\n"
                f"- **Issue:** {fl['conflict']}\n"
                f"- **Detected:** {fl['timestamp']}\n"
                f"- **Action Required:** Review source file. If genuine contradiction → update Contradiction Log in `02_Akshat_Principle_Frequency_Table.md`.\n"
            )
    else:
        lines.append("## ✅ No Contradictions Detected\n")
        lines.append("> All pending sources appear consistent with existing doctrine.\n")

    # Atomic write
    tmp = REPORT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    os.replace(tmp, REPORT)

    print(f"[contradiction_checker] Done. {len(flags)} flag(s). Report: {REPORT}")

if __name__ == "__main__":
    main()
