# Test: Stock Analysis Workflow (WF-01)

## Test Case 1 — Indian Stock

**Input:** "Analyze HDFC Bank. Should I buy?"

**Expected Output Checklist:**
- [ ] Geographic classification: India
- [ ] INR depreciation adjustment performed
- [ ] Compared against US financial alternative (e.g., JPMorgan)
- [ ] EPS growth rate stated or noted as unavailable
- [ ] PE vs historical average stated
- [ ] Entry zone referenced (200DMA, post-correction, or parabolic)
- [ ] Position size recommended (5–10%)
- [ ] Output follows 8-section format
- [ ] No naked option recommendation
- [ ] No India-only nationalism bias

**Fail Conditions:**
- [ ] No geographic comparison made
- [ ] Position size > 15% recommended
- [ ] No valuation anchor provided
- [ ] Output section order violated
- [ ] INR adjustment skipped

---

## Test Case 2 — US Technology Stock

**Input:** "Analyze Microsoft (MSFT). Good buy?"

**Expected Output Checklist:**
- [ ] Geographic classification: US
- [ ] No INR adjustment (US stock)
- [ ] AI/cloud monetization thesis checked
- [ ] EPS CAGR vs price CAGR comparison made
- [ ] Margin trend stated
- [ ] 200DMA / valuation zone identified
- [ ] Thesis stated (structural compounder vs tactical trade)
- [ ] Position size 5–10%

---

## Test Case 3 — Overvalued Stock

**Input:** "Stock X is trading at 450x PE. Thoughts?"

**Expected Output Checklist:**
- [ ] Valuation WARNING issued
- [ ] "Avoid parabolic price action" rule invoked
- [ ] Comparison against earnings growth made
- [ ] Output is NOT bullish regardless of narrative quality
