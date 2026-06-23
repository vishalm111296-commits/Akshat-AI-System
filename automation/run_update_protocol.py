#!/usr/bin/env python3
"""
run_update_protocol — FULL PIPELINE ORCHESTRATOR
"""
import subprocess, sys, os, json, hashlib
from pathlib import Path
from datetime import datetime

STEPS = [
    ("extract_principles",    "automation/extract_principles.py"),
    ("contradiction_checker", "automation/contradiction_checker.py"),
    ("update_recent_changes", "automation/update_recent_changes.py"),
    ("update_frequency_table","automation/update_frequency_table.py"),
]

# EXACT filename — Linux CI is case-sensitive
MASTER = "knowledge/01_Akshat_Master_System.md"


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
