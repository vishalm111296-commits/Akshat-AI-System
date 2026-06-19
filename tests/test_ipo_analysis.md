# Test: IPO Analysis Workflow (WF-04)

## Test Case 1 — Expensive IPO with OFS

**Input:**
- Company: FashionX
- Sector: D2C Fashion
- PE at upper band: 120x
- Listed peer PE: 45x
- Use of proceeds: 80% OFS
- GMP: +60%

**Expected Output:**
- [ ] Verdict: SKIP
- [ ] Valuation flag: PE > 2x listed peers
- [ ] Proceeds flag: OFS = promoters selling, not building
- [ ] GMP noted as sentiment signal only, NOT fundamental basis
- [ ] No allocation recommended

---

## Test Case 2 — Reasonable IPO

**Input:**
- Company: InfraTech Ltd
- Sector: Data Center Infrastructure
- PE at upper band: 28x
- Listed peer PE: 32x
- Use of proceeds: 90% capex
- Track record: Profitable for 5+ years

**Expected Output:**
- [ ] Verdict: Apply or Wait for Listing
- [ ] Valuation: Cheap or Fair vs peers
- [ ] Proceeds: Clean
- [ ] Allocation: 2–5% recommended (IPO-stage cap)
