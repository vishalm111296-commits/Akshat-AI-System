#!/usr/bin/env python3
"""
promote_to_master.py — PROMOTION VALIDATION + PR HELPER

Usage:
  python scripts/promote_to_master.py --principle PC-01
  python scripts/promote_to_master.py --principle PC-01 --create-pr

This script:
  1. Reads the Frequency Table and validates the principle meets promotion criteria
  2. Checks Source Database for individual source traceability
  3. Checks for open contradictions in contradiction_report.md
  4. Prints a pass/fail report
  5. With --create-pr: generates a ready-to-use Git branch + PR description

NEVER writes to 01_Akshat_Master_System.md directly.
Master System is human-edited only via a PR that passes the protect_master_system workflow.
"""
import argparse, os, re, json
from datetime import datetime

FREQ      = "knowledge/02_Akshat_Principle_Frequency_Table.md"
SOURCE_DB = "knowledge/03_Akshat_Source_Database.md"
CONTRA    = "knowledge/contradiction_report.md"
MASTER    = "knowledge/01_Akshat_Master_System.md"
CHANGELOG = "CHANGELOG.md"

PROMOTION_THRESHOLD = 8
TIME_PERIODS_REQUIRED = 2


def read_file(path):
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def find_principle_row(freq_content, pid):
    """Return the table row for the given principle ID, or None."""
    pattern = re.compile(
        r'^\|\s*' + re.escape(pid) + r'\s*\|([^|]+)\|\s*(\d+)\s*\|([^|]+)\|([^|]+)\|',
        re.MULTILINE
    )
    m = pattern.search(freq_content)
    if not m:
        return None
    return {
        "id": pid,
        "name": m.group(1).strip(),
        "count": int(m.group(2)),
        "status": m.group(3).strip(),
        "sources": m.group(4).strip()
    }


def check_already_in_master(master_content, principle_name):
    return principle_name.lower()[:30] in master_content.lower()


def check_contradictions_open(contra_content):
    return "⚠️" in contra_content and "No Contradictions" not in contra_content


def count_source_entries(source_db_content):
    """Count individual (non-batch) source rows."""
    rows = re.findall(r'^\|\s*(YT|CP|PP)-\d{4}-\d+', source_db_content, re.MULTILINE)
    return len(rows)


def generate_pr_description(pid, row):
    return (
        f"## Promotion Request: {pid} — {row['name']}\n\n"
        f"**Principle ID:** {pid}\n"
        f"**Current Count:** {row['count']} independent sources\n"
        f"**Current Status:** {row['status']}\n"
        f"**Promotion Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
        f"### Checklist\n"
        f"- [x] {row['count']} >= {PROMOTION_THRESHOLD} independent sources\n"
        f"- [ ] 2+ distinct time periods confirmed by human reviewer\n"
        f"- [ ] No open contradictions\n"
        f"- [ ] Not already present in Master System\n"
        f"- [ ] Evidence log attached to this PR\n\n"
        f"### Instructions\n"
        f"1. Manually add principle to appropriate section in `knowledge/01_Akshat_Master_System.md`\n"
        f"2. Update `CHANGELOG.md` with promotion record\n"
        f"3. Update status in `knowledge/02_Akshat_Principle_Frequency_Table.md` to `Doctrine`\n"
        f"4. PR will be reviewed by `protect_master_system.yml` workflow\n"
    )


def main():
    parser = argparse.ArgumentParser(description="Validate and prepare Master System promotion")
    parser.add_argument("--principle", required=True, help="Principle ID, e.g. PC-01")
    parser.add_argument("--create-pr", action="store_true", help="Output PR description for this promotion")
    args = parser.parse_args()
    pid = args.principle.upper()

    print("=" * 60)
    print(f"PROMOTION VALIDATION REPORT: {pid}")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    freq_content   = read_file(FREQ)
    source_content = read_file(SOURCE_DB)
    contra_content = read_file(CONTRA)
    master_content = read_file(MASTER)

    row = find_principle_row(freq_content, pid)
    if not row:
        print(f"\n❌ FAIL: Principle '{pid}' not found in Frequency Table.")
        print(f"   Verify the ID exists in: {FREQ}")
        return

    print(f"\nPrinciple  : {row['name']}")
    print(f"Count      : {row['count']} (required: {PROMOTION_THRESHOLD}+)")
    print(f"Status     : {row['status']}")
    print(f"Sources    : {row['sources']}")

    checks = []

    # Check 1: count threshold
    if row["count"] >= PROMOTION_THRESHOLD:
        checks.append((True,  f"Count {row['count']} >= {PROMOTION_THRESHOLD} ✅"))
    else:
        checks.append((False, f"Count {row['count']} < {PROMOTION_THRESHOLD} — needs {PROMOTION_THRESHOLD - row['count']} more sources ❌"))

    # Check 2: not already doctrine / in master
    if check_already_in_master(master_content, row["name"]):
        checks.append((False, "Principle already appears in Master System — no promotion needed ❌"))
    else:
        checks.append((True,  "Not yet in Master System ✅"))

    # Check 3: no open contradictions
    if contra_content and check_contradictions_open(contra_content):
        checks.append((False, "Open contradictions detected — resolve before promoting ❌"))
    else:
        checks.append((True,  "No open contradictions ✅"))

    # Check 4: source DB traceability
    n_sources = count_source_entries(source_content)
    if n_sources >= row["count"]:
        checks.append((True,  f"Source DB has {n_sources} entries — sufficient ✅"))
    else:
        checks.append((False, f"Source DB has only {n_sources} individual entries vs claimed {row['count']} — expand Source DB ❌"))

    print("\nChecklist:")
    all_pass = True
    for ok, msg in checks:
        print(f"  {'✅' if ok else '❌'} {msg}")
        if not ok:
            all_pass = False

    print("\n" + "=" * 60)
    if all_pass:
        print(f"✅ PROMOTION APPROVED for {pid}")
        print("   Create a branch: git checkout -b promote/{pid.lower()}")
        print("   Edit Master System manually, then open a PR.")
        if args.create_pr:
            pr_desc = generate_pr_description(pid, row)
            pr_file = f".automation_state/pr_description_{pid}.md"
            os.makedirs(".automation_state", exist_ok=True)
            with open(pr_file, "w", encoding="utf-8") as f:
                f.write(pr_desc)
            print(f"\n   PR description saved to: {pr_file}")
    else:
        print(f"❌ PROMOTION BLOCKED for {pid} — resolve all failing checks above.")
    print("=" * 60)


if __name__ == "__main__":
    main()
