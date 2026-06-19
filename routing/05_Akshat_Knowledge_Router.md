# 05 — Akshat Knowledge Router

> Maps incoming task types to the **minimum required knowledge files**. Load only what is needed. Do not load everything for every query.

*Layer: L5 — Routing Layer*

---

## Router Decision Tree

```
INPUT: Task
  ↓
STEP 1: Classify task type
  ├─ QUERY task (analysis, research, opinion)
  ├─ UPDATE task (ingestion, protocol run)
  └─ SYSTEM task (routing, validation, audit)
  ↓
STEP 2: Identify required knowledge
  ↓
STEP 3: Load minimum context budget
  └─ SHORT = single section of one file
  └─ MEDIUM = multiple sections from 1–2 files
  └─ FULL = both 01 and 04 files
  ↓
OUTPUT: [File list] + [Sections] + [Skill list] + [Workflow ID]
```

---

## Task → File Mapping

| Task Type | Load | Sections | Skip |
|---|---|---|---|
| Stock Analysis | `01_Master`, `04_Recent_Changes` | §3.2, 3.3, 3.4, 4.1, 4.2, 4.3 | `02_FreqTable`, `raw_sources/` |
| Portfolio Review | `01_Master`, `04_Recent_Changes` | §2, §5 | `02_FreqTable`, `raw_sources/` |
| Macro Analysis | `01_Master`, `04_Recent_Changes` | §3.4 | `02_FreqTable`, `raw_sources/` |
| IPO Analysis | `01_Master`, `04_Recent_Changes` | §3.3, 4.1, 4.2 | `02_FreqTable`, `raw_sources/` |
| Earnings Analysis | `01_Master`, `04_Recent_Changes` | §3.3 | `02_FreqTable`, `raw_sources/` |
| Options Analysis | `01_Master` | §3.5, 4.5 | `04_Recent_Changes`, `02_FreqTable`, `raw_sources/` |
| Mutual Fund Analysis | `01_Master` | §3.6 | `04_Recent_Changes`, `02_FreqTable`, `raw_sources/` |
| Real Estate Analysis | `01_Master` | §3.7 | `04_Recent_Changes`, `02_FreqTable`, `raw_sources/` |
| Research Request | `01_Master`, `04_Recent_Changes` | Full | `02_FreqTable`, `raw_sources/` |
| Framework Extraction | `02_FreqTable`, `03_SourceDB`, `08_UpdateProtocol` | Full | `01_Master` (read-only reference) |
| Update Protocol Run | `02_FreqTable`, `03_SourceDB`, `08_UpdateProtocol` | Full | `01_Master` (never write) |
| Promotion Review | `01_Master`, `02_FreqTable`, `CHANGELOG` | Full | `raw_sources/` |

---

## Context Budget Rules

- **SHORT**: Single-section load. Use for narrow, specific questions (e.g., "What are options rules?").
- **MEDIUM**: 2–3 sections from 1–2 files. Use for standard analysis tasks.
- **FULL**: Both `01_Master` and `04_Recent_Changes` in full. Use for comprehensive research or portfolio review.

## Forbidden Loads at Query Time

These files are **never loaded** during query/analysis tasks:
- `raw_sources/**` — raw material only; never for runtime inference
- `02_Akshat_Principle_Frequency_Table.md` — metadata file; not needed for analysis
- `03_Akshat_Source_Database.md` — registry file; not needed for analysis
- `update_engine/**` — protocol files; not needed for analysis
- `automation/**` — scripts; not needed for analysis
