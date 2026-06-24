---
name: Earnings Analysis
description: Interpret quarterly earnings reports and assess thesis integrity.
triggers:
  - earnings
  - quarterly
  - eps
  - revenue
  - guidance
load_with: earnings_skill.py
---

# Skill: Earnings Analysis

*Layer: L1 — Core Skills*

## Purpose
Interpret a quarterly earnings report and assess whether the long-term thesis remains intact.

## Execution Steps

### Step 1: Revenue vs EPS Check
- Revenue growth rate (YoY)
- EPS growth rate (YoY)
- Divergence: Revenue up but EPS flat/down → margin compression signal

### Step 2: Operating Margin Trend
- Operating margin (this quarter vs last quarter vs same quarter last year)
- Is margin: expanding / stable / contracting?
- Any one-time items? (exclude and restate)

### Step 3: Guidance Quality
- Did management provide guidance? Is it specific or vague?
- Is guidance raised, maintained, or lowered?
- Lowered guidance + margin compression = THESIS REVIEW

### Step 4: Market Reaction Assessment
- Is the price move proportional to the fundamental change?
- Overreaction (stock down 15% on minor miss) → potential accumulation
- Underreaction (stock flat on major earnings miss) → delay entry

### Step 5: Thesis Status
- **Intact**: Fundamentals on track, guidance reasonable, margins stable
- **Weakened**: One metric off, management commentary cautious
- **Broken**: Multiple misses, margin collapse, guidance withdrawal, structural issue

## Output Format
1. Earnings Quality Score: Strong / In-Line / Weak / Miss
2. Revenue vs EPS Table
3. Margin Trend Arrow (↑ / → / ↓)
4. Thesis Status: Intact / Weakened / Broken
5. Recommended Action: Hold / Add / Trim / Exit
