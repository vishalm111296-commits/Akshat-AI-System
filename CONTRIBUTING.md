# Contributing to Akshat-AI-System

## Who Can Contribute

This repository is maintained by its owner. External contributors may submit:
- New raw source files (transcripts, posts)
- Bug reports in routing logic
- Test case failures

## How to Add a New Source

1. Read `docs/how_to_add_source.md` fully before proceeding
2. Place the raw file in the correct `raw_sources/` subdirectory
3. Use the naming convention: `[TYPE]-[YYYY-MM-DD]-[SHORT_TITLE].txt`
   - Example: `YT-2026-07-14-india-vs-usa-portfolio.txt`
4. Add an individual row to `knowledge/03_Akshat_Source_Database.md` (no batch entries)
5. Run `python automation/run_update_protocol.py`
6. Commit with message: `source: add [TYPE]-[DATE] — [title]`

## Quarterly Keyword Review (REQUIRED)

Every quarter, a maintainer must:
1. Review the `PRINCIPLE_KEYWORDS` list in `automation/extract_principles.py`
2. Add any new terminology Akshat Shrivastava has introduced in recent videos/posts
3. Review the `CONTRADICTION_PAIRS` list in `automation/contradiction_checker.py`
4. Add any new pairs of potentially conflicting stances
5. Update `last_reviewed` in `operating_system/config.yaml` under `keyword_review`
6. Commit with message: `maintenance: quarterly keyword review [YYYY-QN]`

This cadence ensures the extraction system keeps up with evolving language.

## Running Tests

Before any PR, run the executable test suite:
```bash
pip install pytest pyyaml
pytest tests/test_pipeline_integrity.py -v
```
All tests must pass. Do not open a PR with failing tests.

## What You May NOT Do

- Do NOT edit `knowledge/01_Akshat_Master_System.md` directly
- Do NOT modify existing raw sources after ingestion
- Do NOT create AI-generated summaries in `raw_sources/`
- Do NOT auto-merge any PR that touches `01_Akshat_Master_System.md`
- Do NOT add batch source entries — use individual Source IDs only

## Branch Naming

- `source/add-[source-id]` — for adding new raw sources
- `fix/[component]` — for fixing routing or automation bugs
- `promote/[principle-id]` — for human-approved Master System promotions
- `maintenance/keyword-review-[YYYY-QN]` — for quarterly keyword expansions

## PR Rules

- PRs touching `knowledge/01_Akshat_Master_System.md` require:
  - Manual execution of `scripts/promote_to_master.py --principle [ID] --create-pr`
  - All checks in the generated PR description must pass
  - Manual review and merge only (automation is blocked by `protect_master_system.yml`)
- All other PRs must pass `pytest tests/test_pipeline_integrity.py`
