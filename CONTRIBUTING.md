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
4. Run `python automation/run_update_protocol.py`
5. Commit with message: `source: add [TYPE]-[DATE] — [title]`

## What You May NOT Do

- Do NOT edit `knowledge/01_Akshat_Master_System.md` directly
- Do NOT modify existing raw sources after ingestion
- Do NOT create AI-generated summaries in `raw_sources/`
- Do NOT auto-merge any PR that touches `01_Akshat_Master_System.md`

## Branch Naming

- `source/add-[source-id]` — for adding new raw sources
- `fix/[component]` — for fixing routing or automation bugs
- `promote/[principle-id]` — for human-approved Master System promotions

## PR Rules

- PRs touching `knowledge/01_Akshat_Master_System.md` require manual review with evidence log
- All other PRs may be merged after passing tests
