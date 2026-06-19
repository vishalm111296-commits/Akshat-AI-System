# Test: Portfolio Review Workflow (WF-02)

## Test Case 1 — India-Only Portfolio

**Input Portfolio:**
```
HDFC Bank: 20%
Reliance: 20%
Infosys: 20%
SBI Mutual Fund: 25%
Fixed Deposit: 15%
```

**Expected Flags:**
- [ ] FLAG: No global diversification (India-only)
- [ ] FLAG: No physical gold or hard-asset hedge
- [ ] FLAG: HDFC Bank > 10% — concentration risk
- [ ] FLAG: Reliance > 10% — concentration risk
- [ ] FLAG: Fixed Deposit (long-duration, inflation risk)
- [ ] FLAG: No US or international equity exposure
- [ ] FLAG: Insufficient dry powder (0% cash)

**Expected Recommendations:**
- [ ] Add US tech exposure (e.g., NASDAQ index ETF)
- [ ] Add 5–10% physical gold
- [ ] Reduce concentration in top 2 positions
- [ ] Shift FD to short-duration instrument

---

## Test Case 2 — Well-Diversified Portfolio

**Input Portfolio:**
```
US Tech ETF: 25%
India Large Cap: 20%
Gold: 8%
Cash: 12%
Real Estate: 20%
Southeast Asia ETF: 10%
Crypto (BTC): 5%
```

**Expected Output:**
- [ ] Overall Health: Strong or Adequate
- [ ] No major red flags
- [ ] Real estate illiquidity noted but within threshold (20%)
- [ ] Dry powder adequate (cash 12%)
