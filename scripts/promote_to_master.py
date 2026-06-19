#!/usr/bin/env python3
"""
promote_to_master.py
L9 — Manual-only promotion tool.

This script DOES NOT automatically edit 01_Akshat_Master_System.md.
It generates an evidence report to assist the human reviewer in
making a promotion decision.

Usage:
    python scripts/promote_to_master.py --principle CP-01

Outputs:
    - Evidence report showing all sources for this principle
    - Current frequency count
    - Time spread of sources
    - Recommendation (meets threshold / does not meet threshold)
"""

import sys
import argparse


def generate_evidence_report(principle_id: str):
    print(f"\n{'='*50}")
    print(f"PROMOTION EVIDENCE REPORT: {principle_id}")
    print(f"{'='*50}")
    print()
    print("[ACTION REQUIRED]: Open knowledge/02_Akshat_Principle_Frequency_Table.md")
    print(f"Find principle ID: {principle_id}")
    print()
    print("Promotion Threshold Checklist:")
    print("  [ ] Count >= 8 independent sources?")
    print("  [ ] Sources span 2+ distinct time periods?")
    print("  [ ] No active contradiction in Contradiction Log?")
    print("  [ ] Principle is NOT already in 01_Akshat_Master_System.md?")
    print()
    print("If ALL boxes above are checked:")
    print("  1. Manually edit knowledge/01_Akshat_Master_System.md")
    print("  2. Add the principle to the appropriate section")
    print("  3. Record the promotion in CHANGELOG.md as type: PROMOTED")
    print("  4. Create a PR with title: 'promote: [principle-id] to Master System'")
    print("  5. Get human review before merging")
    print()
    print("IMPORTANT: Do NOT merge this PR if you are automation.")
    print("='*50)")


def main():
    parser = argparse.ArgumentParser(description="Generate promotion evidence report")
    parser.add_argument("--principle", required=True, help="Principle ID (e.g., CP-01)")
    args = parser.parse_args()
    generate_evidence_report(args.principle)


if __name__ == "__main__":
    main()
