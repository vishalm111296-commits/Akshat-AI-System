# 06 — Skill Router

> Maps incoming task types to the **required analytical skill modules** in `skills/`.

*Layer: L5 — Routing Layer*

---

## Skill Index

| Skill File | Purpose |
|---|---|
| `stock_analysis_skill.md` | End-to-end stock analysis framework |
| `macro_analysis_skill.md` | Global macro and liquidity analysis |
| `options_analysis_skill.md` | Covered call and CSP strategy execution |
| `valuation_skill.md` | PE, EPS, margin, and valuation comparison |
| `ipo_analysis_skill.md` | IPO-specific analysis and red flags |
| `mutual_fund_skill.md` | Fund selection, segment valuation, SIP logic |
| `earnings_analysis_skill.md` | Earnings report interpretation |
| `portfolio_review_skill.md` | Portfolio health, allocation, and rotation |

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
| Research Request | All relevant skills | — |
| Framework Extraction | None (knowledge task — use update protocol) | — |

---

## Skill Dependency Rules

- `valuation_skill` is always available as a sub-module to any other skill
- `macro_analysis_skill` may be called as context-setter before any equity skill
- `options_analysis_skill` requires `stock_analysis_skill` as prerequisite context

## Skill Conflict Rules

- Do NOT run `ipo_analysis_skill` and `earnings_analysis_skill` simultaneously for the same company (different stages)
- Do NOT run `mutual_fund_skill` and `stock_analysis_skill` for the same instrument (classify first)
