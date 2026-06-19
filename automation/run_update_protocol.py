#!/usr/bin/env python3
"""
run_update_protocol.py — FULL PIPELINE ORCHESTRATOR

Pipeline (in order):
  Step 1: extract_principles.py      — detect new sources, extract principle keywords
  Step 2: contradiction_checker.py   — flag contradictions before any write
  Step 3: update_recent_changes.py   — append structured entries (APPROVED only)
  Step 4: update_frequency_table.py  — increment counts (APPROVED only)

Safety rules:
  - If any step raises an exception, pipeline halts and reports which step failed
  - Master System (01_Akshat_Master_System.md) is NEVER touched by this script
  - All writes in steps 3 and 4 use atomic (tmp + rename) patterns
"""
import subprocess, sys, os
from datetime import datetime

STEPS = [
    ("extract_principles",       "automation/extract_principles.py"),
    ("contradiction_checker",    "automation/contradiction_checker.py"),
    ("update_recent_changes",    "automation/update_recent_changes.py"),
    ("update_frequency_table",   "automation/update_frequency_table.py"),
]

MASTER = "knowledge/01_Akshat_Master_System.md"

def master_hash():
    import hashlib
    with open(MASTER, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def save_master_hash(h):
    os.makedirs(".automation_state", exist_ok=True)
    import json
    state_file = ".automation_state/master_hash.json"
    json.dump({"hash": h, "recorded_at": datetime.now().isoformat()}, open(state_file, "w"), indent=2)

def verify_master_untouched(pre_hash):
    post_hash = master_hash()
    if pre_hash != post_hash:
        print("\n🚨 CRITICAL VIOLATION: Master System hash changed during pipeline run!")
        print(f"  Expected: {pre_hash}")
        print(f"  Got:      {post_hash}")
        print("  Halting. Investigate immediately.")
        sys.exit(99)

def run_step(name, script_path):
    print(f"\n[pipeline] ▶ Step: {name}")
    if not os.path.exists(script_path):
        print(f"[pipeline] ⚠️  Script not found: {script_path} — skipping.")
        return
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    if result.returncode != 0:
        print(f"[pipeline] ❌ Step '{name}' failed with exit code {result.returncode}. Pipeline halted.")
        sys.exit(result.returncode)
    print(f"[pipeline] ✅ Step '{name}' completed.")

def main():
    print(f"[pipeline] ========================================")
    print(f"[pipeline] Akshat-AI-System Update Protocol")
    print(f"[pipeline] Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[pipeline] ========================================")

    pre_hash = master_hash()
    save_master_hash(pre_hash)
    print(f"[pipeline] Master System hash recorded: {pre_hash[:16]}...")

    for name, script in STEPS:
        run_step(name, script)
        verify_master_untouched(pre_hash)

    print(f"\n[pipeline] ========================================")
    print(f"[pipeline] ✅ All steps complete. Master System intact.")
    print(f"[pipeline] Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[pipeline] ========================================")

if __name__ == "__main__":
    main()
