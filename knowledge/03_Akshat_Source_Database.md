# 03 — Akshat Source Database

> **APPEND-ONLY** — Sources are never deleted. Mark retired sources as `Archived`.

*Last Updated: 2026-06-19*

---

## Source Naming Convention

See `operating_system/source_naming_rules.md`

Format: `[TYPE]-[YYYY-MM-DD]-[SLUG]`

---

## Source Registry

### YouTube Transcripts

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| YT-2026-001 | [Transcript Batch 2 — Multiple Videos] | Various | 2026-06-17 | `raw_sources/youtube_transcripts/` | Active |
| YT-2026-002 | [Transcript Batch 3 — Multiple Videos] | Various | 2026-06-17 | `raw_sources/youtube_transcripts/` | Active |

### Community Posts (Public)

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| CP-2026-001 | Community Post Batch 1 | Various | 2026-06-17 | `raw_sources/community_posts/` | Active |
| CP-2026-002 | Community Post Batch 2 | Various | 2026-06-17 | `raw_sources/community_posts/` | Active |

### Paid Posts

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| PP-2026-001 | Paid Community Post Batch | Various | 2026-06-17 | `raw_sources/paid_posts/` | Active |

---

## How to Add a New Source

1. Assign the next sequential Source ID for the type (e.g., `YT-2026-003`)
2. Add the raw file to the correct `raw_sources/` subdirectory
3. Add a row to this table
4. Run `python automation/run_update_protocol.py`
5. Commit with message: `source: add [SOURCE-ID] — [title]`

---

## Archived Sources

| Source ID | Reason | Archived Date |
|---|---|---|
| — | — | — |
