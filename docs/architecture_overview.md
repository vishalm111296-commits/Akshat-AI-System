# Architecture Overview

## System Design Philosophy

This repository follows three core design principles:
1. **Evidence-driven**: Nothing becomes doctrine without recurring evidence
2. **Human-gated at the top**: The Master System can only be modified by a human
3. **Minimal and scalable**: No redundant abstractions, designed for 5+ year maintenance

## Layer Summary

```
L0  operating_system/     → Constitution and rules
L1  skills/               → Analytical modules
L2  knowledge/01, 02      → Permanent doctrine + evidence counts
L3  knowledge/04          → Tactical/dynamic memory
L4  raw_sources/          → Verbatim evidence archive
L5  routing/              → What to load for each task
L6  workflows/            → How to execute each task
L7  update_engine/        → How evidence becomes doctrine
L8  automation/ + .github/→ Free automation (GitHub Actions + Python)
L9  docs/ + scripts/      → Human and AI query interface
```

## Data Flow

```
New Content Published
  ↓
GitHub Actions detects (weekly cron)
  ↓
fetch_youtube_transcripts.py downloads
  ↓
Stored in raw_sources/ (verbatim)
  ↓
run_update_protocol.py classifies
  ↓
02_Frequency_Table updated
04_Recent_Changes updated
  ↓
CHANGELOG entry generated
  ↓
If count ≥ 8: GitHub Issue opened
  ↓
Human reviews → promote_to_master.py
  → Manual PR → 01_Master_System updated
```

## What Never Changes Automatically

`knowledge/01_Akshat_Master_System.md` — This is the immutable doctrine layer. It only changes through deliberate human action backed by evidence.
