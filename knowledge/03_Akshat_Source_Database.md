# 03 — Akshat Source Database

> **APPEND-ONLY** — Sources are never deleted. Mark retired sources as `Archived`.
> Individual source IDs are required for each video/post — batch entries are deprecated.

*Last Updated: 2026-06-19*
*Audit Pass 2: Expanded with individual source ID placeholders; batch entries annotated.*

---

## Source Naming Convention

See `operating_system/source_naming_rules.md`

Format: `[TYPE]-[YYYY-MM-DD]-[SLUG]`

Examples:
- `YT-2026-01-15-india-vs-usa-allocation` — YouTube video published Jan 15 2026
- `CP-2026-03-10-barbell-portfolio-update` — Community post March 10 2026
- `PP-2026-04-22-paid-options-strategy` — Paid post April 22 2026

---

## Source Registry

### YouTube Transcripts

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| YT-2026-001 | [Transcript Batch 2 — Multiple Videos — DEPRECATED batch entry] | Various | 2026-06-17 | `raw_sources/youtube_transcripts/` | Active |
| YT-2026-002 | [Transcript Batch 3 — Multiple Videos — DEPRECATED batch entry] | Various | 2026-06-17 | `raw_sources/youtube_transcripts/` | Active |
| YT-2026-003 | [PLACEHOLDER — Add next individual YouTube video here] | YYYY-MM-DD | — | `raw_sources/youtube_transcripts/YT-YYYY-MM-DD-slug.txt` | Pending |

> ⚠️ **Action Required:** Batch entries YT-2026-001 and YT-2026-002 must be split into individual source IDs. Each video in the batch should receive its own row with a date-based ID (e.g., `YT-2026-01-15-title-slug`). Until this is done, frequency counts citing these batch IDs cannot be independently verified.

---

### Community Posts (Public)

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| CP-2026-001 | Community Post Batch 1 — DEPRECATED batch entry | Various | 2026-06-17 | `raw_sources/community_posts/` | Active |
| CP-2026-002 | Community Post Batch 2 — DEPRECATED batch entry | Various | 2026-06-17 | `raw_sources/community_posts/` | Active |
| CP-2026-003 | [PLACEHOLDER — Add next individual community post here] | YYYY-MM-DD | — | `raw_sources/community_posts/CP-YYYY-MM-DD-slug.txt` | Pending |

> ⚠️ **Action Required:** Community post batches must be split into individual source IDs.

---

### Paid Posts

| Source ID | Title | Published | Ingested | File Path | Status |
|---|---|---|---|---|---|
| PP-2026-001 | Paid Community Post Batch — DEPRECATED batch entry | Various | 2026-06-17 | `raw_sources/paid_posts/` | Active |
| PP-2026-002 | [PLACEHOLDER — Add next individual paid post here] | YYYY-MM-DD | — | `raw_sources/paid_posts/PP-YYYY-MM-DD-slug.txt` | Pending |

> ⚠️ **Action Required:** Paid post batch must be split into individual source IDs.

---

## How to Add a New Source

1. Assign the next sequential Source ID for the type using date format: `YT-YYYY-MM-DD-slug`
2. Add the raw file to the correct `raw_sources/` subdirectory
3. Add a row to this table with: Source ID, Title, Published date, Ingested date, File path, Status=Active
4. Run `python automation/run_update_protocol.py`
5. Commit with message: `source: add [SOURCE-ID] — [title]`

---

## Source Count Integrity

> The Frequency Table requires **8+ independent sources** per principle before Doctrine promotion.
> Each frequency count must be traceable to a unique Source ID in this database.
> Wildcard references (`YT-*`) in the Frequency Table are a known debt item and must be replaced with specific IDs as batches are split.

---

## Archived Sources

| Source ID | Reason | Archived Date |
|---|---|---|
| — | — | — |
