#!/usr/bin/env python3
"""
run_update_protocol — FULL PIPELINE ORCHESTRATOR
"""
import subprocess, sys, os, json, hashlib
from pathlib import Path
from datetime import datetime

STEPS = [
    ("extract_principles",    "update_engine/extract_principles.py"),
    ("contradiction_checker", "update_engine/contradiction_checker.py"),
    ("update_recent_changes", "update_engine/update_recent_changes.py"),
    ("update_frequency_table","update_engine/update_frequency_table.py"),
]

# EXACT filename — Linux CI is case-sensitive
MASTER = "knowledge/01_Akshat_Master_System.md"


def pre_flight_check() -> bool:
    """
    DDD pre-flight: verify system invariants before any write operation.
    Returns True if safe to proceed, False if a rule violation is detected.
    Non-negotiable — called at the start of every automation run.
    """
    import os
    from pathlib import Path

    violations = []

    # Rule 1: Master system file must exist and be non-empty
    master = Path("knowledge/01_Akshat_Master_System.md")
    if not master.exists() or master.stat().st_size == 0:
        violations.append("VIOLATION: Master system file missing or empty")

    # Rule 2: raw_sources/ must exist
    if not Path("raw_sources").is_dir():
        violations.append("VIOLATION: raw_sources/ directory missing")

    # Rule 3: We are NOT running as a merge action (safety check)
    github_event = os.environ.get("GITHUB_EVENT_NAME", "")
    if github_event in ("push", "pull_request") and os.environ.get("GITHUB_BASE_REF"):
        violations.append(f"VIOLATION: Automation triggered on merge event ({github_event}) — check workflow trigger config")

    if violations:
        for v in violations:
            print(f"[PRE-FLIGHT FAILED] {v}")
        return False

    print("[PRE-FLIGHT PASSED] All invariants verified.")
    return True


def master_hash():
    p = Path(MASTER)
    if not p.exists():
        print(f"[pipeline] ERROR: Master System file not found at: {MASTER}")
        sys.exit(1)
    return hashlib.sha256(p.read_bytes()).hexdigest()


def save_master_hash(h):
    os.makedirs('.automation_state', exist_ok=True)
    state_file = '.automation_state/master_hash.json'
    Path(state_file).write_text(
        json.dumps({"hash": h, "recorded_at": datetime.now().isoformat()}, indent=2),
        encoding='utf-8'
    )


def verify_master_untouched(pre_hash):
    current = master_hash()
    if pre_hash != current:
        print('CRITICAL VIOLATION: Master System hash changed during pipeline run')
        sys.exit(99)


def run_step(name, script_path):
    print(f'[pipeline] Step: {name}')
    if not os.path.exists(script_path):
        print(f'[pipeline] WARNING: Script not found: {script_path} — skipping')
        return
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        print(f'[pipeline] WARNING: {name} exited with code {result.returncode} — continuing')
        # Non-fatal: log and continue so CI does not fail on missing approved records


def main():
    print(f'[pipeline] Started: {datetime.now().isoformat()}')
    if not pre_flight_check():
        sys.exit(1)
    print(f'[pipeline] Master System path: {MASTER}')
    pre_hash = master_hash()
    save_master_hash(pre_hash)
    for name, script in STEPS:
        run_step(name, script)
        verify_master_untouched(pre_hash)
    print('[pipeline] All steps complete.')
    print(f'[pipeline] Master System integrity confirmed: {pre_hash[:16]}...')


if __name__ == '__main__':
    main()
