---
name: Valuation
description: Assess whether an asset is cheap, fair, or expensive relative to history.
triggers:
  - valuation
  - pe ratio
  - intrinsic value
  - cheap
  - expensive
load_with: valuation_skill.py
---

# Skill: Valuation

*Layer: L1 — Core Skills*

## Purpose
Assess whether an asset is cheap, fair, or expensive relative to its own history and global alternatives.

## Execution Steps

### Step 1: Earnings Multiple
- Current PE (trailing and forward)
- 3-year and 5-year average PE
- PE premium/discount vs sector average
- Flag: PE > 2x historical average = expensive

### Step 2: Earnings Growth Comparison
- EPS CAGR (1Y, 3Y)
- Price CAGR vs EPS CAGR
- If price CAGR significantly exceeds EPS CAGR for 2+ years → valuation risk

### Step 3: Margin Quality
- Operating margin (current vs 3Y average)
- Trend: expanding / stable / contracting
- Any one-time items inflating margins?

### Step 4: Global Alternative Comparison
- Identify best comparable listed globally (especially US)
- Compare: PE, EPS growth, margin quality, currency strength
- State clearly: is this stock better value than the US alternative?

### Step 5: Valuation Verdict
- **Cheap**: Forward PE < historical average AND earnings growing
- **Fair**: Forward PE near historical average with steady earnings
- **Expensive**: PE > 1.5x historical average, price outpacing earnings
- **Avoid**: PE > 2x historical average, parabolic price, no earnings acceleration
