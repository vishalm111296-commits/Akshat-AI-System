#!/usr/bin/env python3
"""
run_update_protocol — FULL PIPELINE ORCHESTRATOR
"""
import subprocess, sys, os, json, hashlib
from pathlib import Path
from datetime import datetime

STEPS = [
    ("extract_principles", "automation/extract_principles.py"),
    ("contradiction_checker", "automation/contradiction_checker.py"),
    ("update_recent_changes", "automation/update_recent_changes.py"),
    ("update_frequency_table", "automation/update_frequency_table.py"),
]

MASTER = "knowledge/01_Akshat_Master_System.md"


def master_hash():
    return hashlib.sha256(Path(MASTER).read_bytes()).hexdigest()


def save_master_hash(h):
    os.makedirs('.automation_state', exist_ok=True)
    state_file = '.automation_state/master_hash.json'
    Path(state_file).write_text(
        json.dumps({"hash": h, "recorded_at": datetime.now().isoformat()}, indent=2),
        encoding='utf-8'
    )


def verify_master_untouched(pre_hash):
    if pre_hash != master_hash():
        print('CRITICAL VIOLATION: Master System hash changed during pipeline run')
        sys.exit(99)


def run_step(name, script_path):
    print(f'[pipeline] Step: {name}')
    if not os.path.exists(script_path):
        print(f'[pipeline] Script not found: {script_path}')
        return
    result = subprocess.run([sys.executable, script_path])
    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    pre_hash = master_hash()
    save_master_hash(pre_hash)
    for name, script in STEPS:
        run_step(name, script)
        verify_master_untouched(pre_hash)
    print('[pipeline] Complete')


if __name__ == '__main__':
    main()
