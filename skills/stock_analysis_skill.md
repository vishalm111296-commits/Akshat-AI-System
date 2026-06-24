---
name: Stock Analysis
description: Analyze individual stocks using Akshat's 8-section framework.
triggers:
  - stock
  - analysis
  - equity
  - shares
  - ticker
load_with: none
---

# Skill: Stock Analysis

*Layer: L1 — Core Skills*

## Purpose
Analyze any individual stock using Akshat's framework. Output must follow the 8-section standard format.

## Input Required
- Stock name and ticker
- Country/market of listing
- User's specific question or context

## Execution Steps

### Step 1: Geographic Classification
- India / US / Global Developed / Emerging Market
- Identify currency exposure
- Default comparison: this stock vs best US alternative in same sector

### Step 2: Macro Context
- Load from `macro_analysis_skill.md`
- Rate environment, liquidity, FII flows (for India)

### Step 3: Earnings Analysis
- EPS growth rate (1Y, 3Y, 5Y)
- Revenue vs EPS divergence
- Operating margin trend
- Forward EPS estimate

### Step 4: Valuation Assessment
- Current PE vs 3-year historical average
- Price CAGR vs Earnings CAGR
- Sector PE comparison
- Flag if PE > 2x historical average with no EPS acceleration

### Step 5: Technical Zone
- Current price vs 200DMA
- Is this: below 200DMA / near 200DMA / above 200DMA / parabolic?
- Post-correction status: is this after a 20–40% drawdown?

### Step 6: INR Adjustment (India only)
- Convert expected return to USD equivalent
- Apply assumed 3–5% annual INR depreciation
- State dollar-equivalent return clearly

### Step 7: Position Sizing
- Standard: 5–10% of portfolio
- High-risk / emerging theme: 2.5–4%
- If conviction is very high AND valuation is attractive: up to 10%

### Step 8: Trigger Levels
- Add zone: [price level]
- Trim zone: [price level]
- Invalidation: [condition that breaks the thesis]

## Output Format
1. **Conclusion** — Buy / Hold / Avoid / Wait with one-line rationale
2. **Macro Context**
3. **Geographic Comparison** — vs best alternative
4. **Valuation Assessment**
5. **Risk/Reward**
6. **Position Sizing**
7. **Trigger Levels**
8. **Portfolio Role** — Growth / Hedge / Diversification / Speculative
