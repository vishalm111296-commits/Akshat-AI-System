# Repository Cleanup Plan

## Overview
This document categorizes the current repository files and systems into KEEP, MERGE, DELETE, or REFACTOR, explaining why each decision improves system simplicity, mitigates risk, and enforces the "Evidence-driven" architecture. No files have been deleted.

---

## KEEP (Core Doctrine & System Architecture)

- `knowledge/01_Akshat_Master_System.md`
  - **Why:** This is the immutable core doctrine. It is the destination for all promoted principles and the ultimate reference point for the AI reasoning engine.
- `knowledge/02_Akshat_Principle_Frequency_Table.md`
  - **Why:** The fundamental evidence tracker. Essential for mapping source counts to principles.
- `knowledge/03_Akshat_Source_Database.md`
  - **Why:** Ensures traceability of the Frequency Table. Protects against hallucinations and duplicate counting.
- `update_engine/08_Akshat_Update_Protocol.md`
  - **Why:** Defines the critical immune system of the knowledge base. Explicitly defines human-in-the-loop requirements.
- `scripts/promote_to_master.py`
  - **Why:** Enforces process constraints and generates correct PR instructions for human gatekeepers.
- `docs/architecture_overview.md`
  - **Why:** Clear, concise mapping of the system layers (L0 to L9).

---

## MERGE (Fragmentation & Redundancy)

- `docs/ai_query_interface.md` & `scripts/query_interface.py` -> **MERGE into `workflows/`**
  - **Why:** Querying is a workflow execution. Having separate docs and scripts scattered creates cognitive load. Merge into a single execution workflow definition.
- `docs/how_to_add_source.md` -> **MERGE into `operating_system/source_naming_rules.md`**
  - **Why:** Redundant documentation. Instructions for adding a source should live immediately next to the naming rules for those sources.

---

## REFACTOR (Structural & Taxonomic Changes)

- `knowledge/04_Akshat_Recent_Changes.md`
  - **Why:** Currently acts as a flat holding pen for tactical views. **Refactor** to explicitly separate "New Ideas" (future principle candidates) from "Temporary Opinions" (tactical trades that expire). Add a mandatory `[Expiry Date]` field to temporary opinions.
- `knowledge/contradiction_report.md`
  - **Why:** Currently a static markdown file. **Refactor** to be dynamically generated during the update run, perhaps output as JSON, so it can programmatically block PRs rather than relying purely on text parsing in scripts.
- `skills/` Directory (e.g., `macro_skill.py`, `valuation_skill.py`)
  - **Why:** The skills are fragmented between `.md` context definitions and `.py` files. **Refactor** into strict classes or standard JSON/YAML interfaces that explicitly map to the new Taxonomy (Parent/Child/Tactic/Constraint). They currently lack unified structural constraints.
- `raw_sources/`
  - **Why:** The `03_Source_Database` notes that batch entries (like `YT-2026-001`) are deprecated. **Refactor** the raw sources folder to split all batch files into individual files corresponding to unique IDs.

---

## DELETE (Dead Ends & Noise)

- `raw_source/` (Directory)
  - **Why:** Duplicate directory of `raw_sources/`. `raw_sources/` is defined in the architecture and update protocol. `raw_source/` is an empty or abandoned artifact.
- `skills/__init__.py` (If it imports all skills globally)
  - **Why:** Memory specifies "Do not import all skills in `skills/__init__.py`. Use `skills.load_skill` to inject only relevant markdown context." Delete the global imports to enforce context token efficiency.
- Any future "Automated PR merging" scripts.
  - **Why:** Explicitly forbidden by the L0 Constitution. Delete on sight.
