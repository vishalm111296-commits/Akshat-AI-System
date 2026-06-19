# 06 — Skill Router

> Maps incoming task types to the **required analytical skill modules** in `skills/`.
> Includes fallback handling for unknown or unrecognized task types.

*Layer: L5 — Routing Layer*
*Last Updated: 2026-06-19 — Added fallback handler and skill completeness check.*

---

## Skill Index

| Skill File | Type | Status |
|---|---|---|
| `stock_analysis_skill.md` | Markdown spec | ✅ |
| `macro_analysis_skill.md` | Markdown spec | ✅ |
| `macro_skill.py` | Python implementation | ✅ |
| `options_analysis_skill.md` | Markdown spec | ✅ |
| `options_skill.py` | Python implementation | ✅ |
| `valuation_skill.md` | Markdown spec | ✅ |
| `valuation_skill.py` | Python implementation | ✅ |
| `ipo_analysis_skill.md` | Markdown spec | ✅ |
| `mutual_fund_skill.md` | Markdown spec | ✅ |
| `earnings_analysis_skill.md` | Markdown spec | ✅ |
| `earnings_skill.py` | Python implementation | ✅ |
| `portfolio_review_skill.md` | Markdown spec | ✅ |
| `dma_skill.py` | Python implementation | ✅ |
| `geographic_filter_skill.py` | Python implementation | ✅ |
| `position_sizing_skill.py` | Python implementation | ✅ |
| `real_returns_skill.py` | Python implementation | ✅ |

> **Missing .py implementations** (spec exists, implementation pending):
> - `stock_analysis_skill.py` — needed for programmatic routing
> - `ipo_analysis_skill.py` — needed for programmatic routing
> - `mutual_fund_skill.py` — needed for programmatic routing
> - `portfolio_review_skill.py` — needed for programmatic routing

---

## Task → Skill Mapping

| Task | Required Skills | Optional Skills |
|---|---|---|
| Stock Analysis | `stock_analysis`, `valuation`, `macro_analysis` | `options_analysis` |
| Portfolio Review | `portfolio_review`, `valuation` | `macro_analysis` |
| Macro Analysis | `macro_analysis` | — |
| IPO Analysis | `ipo_analysis`, `valuation`, `stock_analysis` | `macro_analysis` |
| Earnings Analysis | `earnings_analysis`, `valuation` | `macro_analysis` |
| Options Analysis | `options_analysis` | `stock_analysis` |
| Mutual Fund Analysis | `mutual_fund` | `macro_analysis` |
| Real Estate Analysis | `portfolio_review` | `macro_analysis` |
| DMA / Technical Entry | `dma_skill` | `valuation` |
| Geographic Filter | `geographic_filter_skill` | `macro_analysis` |
| Position Sizing | `position_sizing_skill` | `valuation` |
| Real Returns Calculation | `real_returns_skill` | `geographic_filter_skill` |
| Research Request | All relevant skills | — |
| Framework Extraction | None (knowledge task — use update protocol) | — |

---

## Fallback Handler

If an incoming task type does NOT match any row in the Task → Skill Mapping above:

**Step 1:** Check if the task contains keywords that partially match a known skill:
- Contains "stock" / "equity" / "share" → route to `stock_analysis`
- Contains "macro" / "liquidity" / "interest rate" → route to `macro_analysis`
- Contains "option" / "call" / "put" → route to `options_analysis`
- Contains "fund" / "SIP" / "MF" → route to `mutual_fund`
- Contains "IPO" / "listing" / "grey market" → route to `ipo_analysis`
- Contains "portfolio" / "allocation" / "rebalance" → route to `portfolio_review`
- Contains "valuation" / "PE" / "earnings" / "EPS" → route to `valuation`
- Contains "real estate" / "property" / "land" → route to `portfolio_review` + `macro_analysis`
- Contains "DMA" / "200 day" / "support" / "moving average" → route to `dma_skill`
- Contains "return" / "inflation" / "INR" / "currency" → route to `real_returns_skill`

**Step 2:** If no keyword match found → apply **Default Response**:
```
I could not identify a specific skill module for this task.
Please rephrase your query using one of these task categories:
  Stock Analysis | Portfolio Review | Macro Analysis |
  IPO Analysis | Earnings Analysis | Options Analysis |
  Mutual Fund Analysis | Real Estate Analysis | DMA/Technical Entry |
  Position Sizing | Real Returns | Geographic Filter

Alternatively, for open-ended research, I will load all relevant skills.
```

**Step 3:** Log unmatched task to `.automation_state/unmatched_tasks.log` for quarterly review.
This allows the Skill Router to expand over time as new task categories emerge.

---

## Skill Dependency Rules

- `valuation_skill` is always available as a sub-module to any other skill
- `macro_analysis_skill` may be called as context-setter before any equity skill
- `options_analysis_skill` requires `stock_analysis_skill` as prerequisite context
- `dma_skill` may be called independently or as part of `stock_analysis`
- `geographic_filter_skill` should be called before any cross-border comparison
- `real_returns_skill` should be called when comparing India vs. global opportunities

---

## Skill Conflict Rules

- Do NOT run `ipo_analysis_skill` and `earnings_analysis_skill` simultaneously for the same company (different stages)
- Do NOT run `mutual_fund_skill` and `stock_analysis_skill` for the same instrument (classify first)
- Do NOT use `options_analysis_skill` without first confirming ownership (covered call) or cash availability (CSP)

---

## Skill Completeness Standard

Every skill should have BOTH:
1. A **Markdown spec** (`.md`) — defines what the skill does, inputs, outputs, framework
2. A **Python implementation** (`.py`) — programmatic execution for automated pipelines

Skills missing their `.py` implementation are marked as **incomplete** in the Skill Index above.
This is a known technical debt item to be resolved in the next development sprint.
