# Open Decisions

This file tracks unresolved design tensions, missing requirements, and ambiguities
in the Akshat-AI-System. Every AI agent (Jules, Claude, Copilot, Gemini) working
on this repo MUST read this file before starting any task.

When you encounter a new ambiguity, add it here using the template below.
Do NOT silently resolve ambiguities — surface them here and wait for human decision.

---

## How to Add an Entry

```markdown
### OD-NNN — [Short Title]
- **Date:** YYYY-MM-DD
- **Description:** [What is the ambiguity?]
- **Status:** OPEN / RESOLVED
- **Decision:** [Wait for human]
```

---

## Current Open Decisions

### OD-001 — Directory Inconsistency: raw_source/ vs raw_sources/
- **Date:** 2026-06-24
- **Description:** Both `raw_source/` and `raw_sources/` exist in the root. `system_rules.md` and `constants.py` refer to `raw_sources/`, but some files were committed to `raw_source/`.
- **Status:** OPEN
- **Decision:** PENDING HUMAN. Do not consolidate or delete until confirmed.

### OD-002 — Promotion Threshold Mismatch: constants.py vs system_rules.md
- **Date:** 2026-06-24
- **Description:** `operating_system/constants.py` sets `PROMOTION_THRESHOLD = 3`, but `operating_system/system_rules.md` (Rule 5) and `knowledge/02_Akshat_Principle_Frequency_Table.md` state it is 8.
- **Status:** OPEN
- **Decision:** PENDING HUMAN. Currently following the higher threshold (8) for safety.

### OD-003 — Implementation of AGENTS.md and SESSION_TEMPLATE.md
- **Date:** 2026-06-24
- **Description:** Need to formalize how AI agents log their work to prevent context drift. `AGENTS.md` is in draft state but not merged.
- **Status:** OPEN
- **Decision:** PENDING HUMAN. Adding these files now to enforce discipline.

### OD-004 — Master System Automation Guardrails
- **Date:** 2026-06-24
- **Description:** Rule 1 says Master System is human-gated, but `constants.py` has `auto_modify_master: false` in `config.yaml`. Need absolute certainty on whether any automation should EVER propose a direct write vs a PR.
- **Status:** OPEN
- **Decision:** PENDING HUMAN. Strictly PR-only for now.
