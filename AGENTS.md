# AGENTS.md — Persistent AI Agent Rules

This file is the highest-leverage context for every AI agent (Jules, Claude, Copilot, Gemini) working on this repo. It MUST be loaded first in every session.

---

### Section 1 — Project Identity
Akshat-AI-System is a production-grade, modular, evidence-driven knowledge system designed to replicate and continuously update Akshat Shrivastava's investing philosophy.

**Purpose:** A knowledge management + AI orchestration system for Akshat's trading/investing philosophy.

---

### Section 2 — Tech Stack
- **Python Version:** 3.11+
- **Dependencies:**
  - `youtube-transcript-api`: Fetch YouTube video transcripts (free, no API key)
  - `feedparser`: Parse RSS feeds for community posts
  - `pyyaml`: Read config.yaml
  - `requests`: HTTP library for fetching web content
  - `pytest`: Test framework
- **Key Directories:**
  - `operating_system/`: config, constants, rules, glossary
  - `skills/`: domain-specific callable modules (.py) + context docs (.md)
  - `knowledge/`: the master knowledge base (human-gated)
  - `raw_sources/`: immutable committed source material (Rule 2 in system_rules.md)
  - `raw_source/`: status UNCLEAR, possible staging area (see OD-001 in docs/open-decisions.md — do not consolidate or delete)
  - `automation/`: GitHub Actions workflows and scheduled scripts
  - `update_engine/`: logic to process and update knowledge
  - `routing/`: decision routing between skills/workflows
  - `workflows/`: multi-step orchestration definitions
  - `scripts/`: utility and promotion scripts
  - `tests/`: test suite
  - `docs/`: documentation
  - `changelog/`: append-only session logs

---

### Section 3 — Commands
- Run tests: `pytest tests/`
- Promote a principle: `python scripts/promote_to_master.py`
- Run automation locally: `python automation/run_update_protocol.py`
- Lint: `ruff check .` (install with: `pip install ruff`)

---

### Section 4 — Non-Negotiable System Rules (Verbatim from system_rules.md)

#### Rule 1 — Master System Is Human-Gated
`knowledge/01_Akshat_Master_System.md` may ONLY be modified by a human, via a manual PR, after running `scripts/promote_to_master.py` and reviewing the evidence log.

Automation scripts that attempt to write to this file must be rejected at the PR level.

#### Rule 2 — Raw Sources Are Immutable After Ingestion
Once a file is committed to `raw_sources/`, it may never be edited. If a correction is needed, add a new annotated version and mark the old one as superseded in `knowledge/03_Akshat_Source_Database.md`.

#### Rule 3 — AI Output Is Never a Source
No AI-generated summary, analysis, or synthesized document may be stored in `raw_sources/` or counted as an independent source in `knowledge/02_Akshat_Principle_Frequency_Table.md`.

#### Rule 4 — One Source = One Count
Each independent published source (video, post, article) may increment a principle's frequency count by 1, regardless of how many times that principle appears within that source.

#### Rule 5 — One Mention Never Updates Doctrine
A principle must appear in 8+ independent sources across 2+ distinct time periods before it can be nominated for promotion to `01_Akshat_Master_System.md`.

#### Rule 6 — No Unnecessary Abstractions
Do not create meta-systems, super-systems, AI-brain layers, or redundant wrapper files. Every file must have a distinct, irreplaceable purpose.

#### Rule 7 — Changelog Is Append-Only
`CHANGELOG.md` is never edited retroactively. Entries are always appended. Errors in past entries are corrected by adding a correction entry, not editing the original.

#### Rule 8 — Automation Scope Is Bounded
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

---

### Section 5 — Code Conventions
- **Naming conventions for skill files:** `<domain>_skill.py` and `<domain>_skill.md` always paired.
- **Source naming rules:** Files must follow `[TYPE]-[YYYY-MM-DD]-[SHORT_SLUG].txt`, using lowercase slugs, hyphens only, and the original publication date.
- **Glossary terms:**
  - **Doctrine:** A principle that has been promoted to `01_Akshat_Master_System.md` after meeting the frequency threshold (8+ independent sources, 2+ time periods).
  - **Raw Source:** A verbatim, unprocessed primary document stored in `raw_sources/`.
  - **Independent Source:** A separately published piece of content by Akshat Shrivastava.
  - **Frequency Count:** The number of independent sources in which a given principle has appeared.
  - **Promotion Candidate:** A principle that has met the frequency threshold and is eligible for human review for promotion to the Master System.

---

### Section 6 — Context Hierarchy for AI Agents
When working on this repo, load context in this order:
1. AGENTS.md (this file) — always loaded first, every session
2. operating_system/ relevant files — per task
3. The specific skill files relevant to the task
4. Error output / test results — per iteration
5. Conversation history — summarize after every 10 messages

Aim for 2,000 lines of focused context per task. Do NOT load all skills at once.

---

### Section 7 — Confusion Surface Points
When you encounter ambiguity during a task, STOP and surface it using this format:

CONFUSION: [describe the conflict in 2 lines]
Options:
A. [option A]
B. [option B]
C. Ask the human

Do NOT silently resolve ambiguity. Surface it every time.

---

### Section 8 — Boundaries (Things Agents Must Never Do)
- Never modify `knowledge/01_Akshat_Master_System.md` directly
- Never delete files in `raw_sources/` or `raw_source/`
- Never merge PRs automatically
- Never count AI-generated content as a source
- Never create meta-layers or wrapper files without a distinct irreplaceable purpose
- Never commit secrets or API keys
