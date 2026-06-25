# AGENTS.md — Akshat AI System Boot Instructions

## What this repository is
A living knowledge brain that captures and reasons with Akshat Shrivastava's
investing philosophy. It answers investing questions the way Akshat would,
based only on verified sources.

## Read these files in this exact order before answering anything
1. operating_system/ — rules of the system
2. knowledge/01_Akshat_Master_System.md — core doctrine
3. knowledge/04_Akshat_Recent_Changes.md — latest updates
4. routing/05_Akshat_Knowledge_Router.md — how to route questions
5. routing/06_Skill_Router.md — which skill to use

## Folder map
| Folder | Purpose |
|--------|---------|
| raw_sources/ | Verbatim Akshat content. NEVER modify. NEVER treat as AI output. |
| knowledge/ | Synthesized doctrine. Only update through update_engine/ or automation/. |
| skills/ | Python analysis tools. Each has a matching .md spec file. |
| routing/ | Routing logic for questions and skills. |
| automation/ | Scripts that promote raw sources into knowledge. |
| tests/ | Integrity tests. Run before every merge. |
| changelog/ | Dated log of every system change. |

## Hard rules — never break these
1. Never modify knowledge/01_Akshat_Master_System.md directly or via automation.
2. Never accept AI-generated text as a raw source.
3. Never delete from raw_sources/ — only archive to raw_sources/other/.
4. Never commit directly to main — always use a PR.
5. All automated changes go through staging branch + PR review.

## Source tier system
| Tier | Source type | Auto-promote? |
|------|------------|---------------|
| 1 | Akshat's YouTube video or community post | Yes |
| 2 | Akshat's tweet or short-form content | Yes |
| 3 | Akshat interview on someone else's channel | Human review |
| 4 | Third-party article summarising Akshat | Human review |
| 5 | AI-generated summary | Never — permanently banned |

## Python version
3.11

## Key libraries
See automation/requirements.txt