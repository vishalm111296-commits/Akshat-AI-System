# System Rules — Non-Negotiable

These rules govern every layer of the Akshat-AI-System. They cannot be overridden by any workflow, automation script, or AI agent.

---

## Rule 1 — Master System Is Human-Gated

`knowledge/01_Akshat_Master_System.md` may ONLY be modified by a human, via a manual PR, after running `scripts/promote_to_master.py` and reviewing the evidence log.

Automation scripts that attempt to write to this file must be rejected at the PR level.

---

## Rule 2 — Raw Sources Are Immutable After Ingestion

Once a file is committed to `raw_sources/`, it may never be edited. If a correction is needed, add a new annotated version and mark the old one as superseded in `knowledge/03_Akshat_Source_Database.md`.

---

## Rule 3 — AI Output Is Never a Source

No AI-generated summary, analysis, or synthesized document may be stored in `raw_sources/` or counted as an independent source in `knowledge/02_Akshat_Principle_Frequency_Table.md`.

---

## Rule 4 — One Source = One Count

Each independent published source (video, post, article) may increment a principle's frequency count by 1, regardless of how many times that principle appears within that source.

---

## Rule 5 — One Mention Never Updates Doctrine

A principle must appear in 8+ independent sources across 2+ distinct time periods before it can be nominated for promotion to `01_Akshat_Master_System.md`.

---

## Rule 6 — No Unnecessary Abstractions

Do not create meta-systems, super-systems, AI-brain layers, or redundant wrapper files. Every file must have a distinct, irreplaceable purpose.

---

## Rule 7 — Changelog Is Append-Only

`CHANGELOG.md` is never edited retroactively. Entries are always appended. Errors in past entries are corrected by adding a correction entry, not editing the original.

---

## Rule 8 — Automation Scope Is Bounded

Automation (GitHub Actions + Python) may:
- Fetch new content
- Store to `raw_sources/`
- Update `04_Akshat_Recent_Changes.md`
- Update `02_Akshat_Principle_Frequency_Table.md`
- Generate changelog entries
- Open GitHub Issues for promotion candidates

Automation may NEVER:
- Modify `01_Akshat_Master_System.md`
- Delete any file in `raw_sources/`
- Merge PRs automatically
- Count its own outputs as sources
