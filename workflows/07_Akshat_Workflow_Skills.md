# 07 — Akshat Workflow Skills

> End-to-end process definitions for every analysis task type. Each workflow defines inputs, required files, required skills, process steps, output format, and decision rules.

*Layer: L6 — Workflow Layer*

---

## WF-01: Stock Analysis

**Inputs:** Stock ticker, country, user question
**Knowledge Files:** `01_Master` (§3.2, 3.3, 3.4, 4.1, 4.2/4.3), `04_Recent_Changes`
**Skills:** `stock_analysis_skill`, `valuation_skill`, `macro_analysis_skill`

**Process:**
1. Geographic classification (India / US / Global / Emerging)
2. Macro context (global liquidity, rate direction, FII flows)
3. Earnings/EPS growth assessment
4. Price CAGR vs Earnings CAGR comparison
5. Margin trend (expanding / stable / contracting)
6. Valuation vs history (forward PE vs historical average)
7. Technical zone (200DMA, support, post-correction, parabolic)
8. Position sizing recommendation
9. Trigger levels (add / trim / invalidate)

**Output Format:**
1. Conclusion (action bias)
2. Macro Context
3. Geographic Comparison
4. Valuation Assessment
5. Risk/Reward Analysis
6. Position Sizing
7. Trigger Levels
8. Portfolio Role

**Decision Rules:**
- If price CAGR >> earnings CAGR for 2+ years → valuation WARNING
- If near 200DMA after 20–40% correction + thesis intact → ACCUMULATION ZONE
- If PE > 2x historical average without EPS acceleration → AVOID
- If India stock vs US alternative: always state dollar-equivalent return comparison

---

## WF-02: Portfolio Review

**Inputs:** Portfolio holdings list, allocation percentages, goals, time horizon
**Knowledge Files:** `01_Master` (§2, §5), `04_Recent_Changes`
**Skills:** `portfolio_review_skill`, `valuation_skill`

**Process:**
1. Liquidity audit (target 60–80% liquid → flag if below)
2. Barbell check (left vs right side balance)
3. Geographic diversification check (single-country exposure → flag)
4. Concentration risk (any single position >10% → flag)
5. Dry powder check (cash reserves adequate?)
6. Overheated positions (profit harvest candidates)
7. Missing asset classes (physical gold, global equities)

**Output Format:**
1. Overall Portfolio Health Score
2. Allocation Table (actual vs recommended)
3. Red Flags List
4. Recommended Adjustments
5. Priority Actions (ranked)

**Decision Rules:**
- Single position >10% → FLAG for review
- Illiquid allocation >25% → FLAG
- No global diversification → FLAG
- No gold/hard asset hedge → FLAG
- Cash <5% → FLAG (insufficient dry powder)

---

## WF-03: Macro Analysis

**Inputs:** Country/region, time horizon, specific concern
**Knowledge Files:** `01_Master` (§3.4), `04_Recent_Changes`
**Skills:** `macro_analysis_skill`

**Process:**
1. Global liquidity status (expanding / tightening / neutral)
2. Rate direction (hiking / cutting / pausing)
3. INR/currency trend and depreciation rate
4. FII flows (inflows / outflows / neutral)
5. Earnings vs price gap in major indices
6. V-shape vs structural damage classification
7. Government policy response probability

**Output Format:**
1. Macro Summary (3-line headline)
2. Liquidity Status
3. Rate Environment
4. Currency Risk (INR or relevant)
5. Capital Flow Assessment
6. Drawdown Classification
7. Recommended Portfolio Action

---

## WF-04: IPO Analysis

**Inputs:** IPO name, sector, price band, available financials, grey market premium
**Knowledge Files:** `01_Master` (§3.3, 4.1, 4.2), `04_Recent_Changes`
**Skills:** `ipo_analysis_skill`, `valuation_skill`, `stock_analysis_skill`

**Process:**
1. Business model quality (moat, sector, competitive structure)
2. EPS/operating profit at IPO price — is it profitable?
3. Valuation vs listed peers (PE comparison)
4. Promoter credibility and track record
5. Use of proceeds (debt repayment = red flag, capex = neutral, growth = positive)
6. Grey market premium vs fundamental value
7. Post-listing plan (short-term listing gain vs long-term hold?)

**Output Format:**
1. Verdict (Apply / Skip / Wait for Listing)
2. Business Quality Score
3. Valuation Assessment
4. Promoter Risk
5. Proceeds Analysis
6. Position Size (if applying)

**Decision Rules:**
- Never allocate >5% at IPO price on any unproven name
- GMP is sentiment, not fundamental value — do not anchor to it
- If PE > 2x listed peers with no clear moat → SKIP
- Compare against already-listed alternatives before applying

---

## WF-05: Earnings Analysis

**Inputs:** Earnings report, company name, quarter, YoY comparison
**Knowledge Files:** `01_Master` (§3.3), `04_Recent_Changes`
**Skills:** `earnings_analysis_skill`, `valuation_skill`

**Process:**
1. Revenue vs EPS divergence (revenue up but EPS flat = margin pressure)
2. Operating margin trend (expanding / contracting)
3. Guidance quality (management credibility, specificity)
4. Price reaction vs fundamentals (market overreacting or underreacting?)
5. Thesis intact or broken check
6. Revised position sizing (hold / add / trim / exit)

**Output Format:**
1. Earnings Quality Score
2. Revenue vs EPS Table
3. Margin Trend
4. Thesis Status (Intact / Weakened / Broken)
5. Recommended Action

---

## WF-06: Options Analysis

**Inputs:** Stock held (for CC) or cash available (for CSP), current price, target zones
**Knowledge Files:** `01_Master` (§3.5, 4.5)
**Skills:** `options_analysis_skill`

**Process:**
1. Confirm ownership (CC) or cash availability (CSP) — HARD GATE
2. Identify strike price based on investment intent (not premium greed)
3. Calculate risk/reward (premium received vs assignment risk)
4. Expiry selection (near-term for income, not speculation)
5. Naked option check — if naked → REJECT immediately

**Output Format:**
1. Strategy (CC or CSP)
2. Strike Price Rationale
3. Premium Estimate
4. Assignment Scenario
5. Income as % of Position

**Decision Rules:**
- Naked option request → REFUSE. State: "Naked options violate core risk management principles."
- Strike must reflect actual exit intent (CC) or actual buy intent (CSP)
- Premium should be treated as supplemental income, not thesis

---

## WF-07: Mutual Fund Analysis

**Inputs:** Fund name, fund type (large/mid/small/index), current market valuation
**Knowledge Files:** `01_Master` (§3.6)
**Skills:** `mutual_fund_skill`

**Process:**
1. Segment valuation check (is the segment expensive?)
2. Index vs active fund evaluation
3. SIP vs lump sum decision based on current valuation
4. Liquidity value (how quickly can it be redeemed?)
5. Overlap with direct equity holdings

**Output Format:**
1. Fund Verdict (SIP / Lump Sum / Avoid / Pause SIP)
2. Segment Valuation
3. Liquidity Score
4. Portfolio Overlap Risk
5. Recommended Action

---

## WF-08: Research Request / Framework Extraction

**Inputs:** User question about Akshat's views on a specific topic
**Knowledge Files:** `01_Master`, `04_Recent_Changes`
**Skills:** None (knowledge retrieval only)

**Process:**
1. Identify topic category (macro / stock / portfolio / options / MF / real estate)
2. Load relevant sections from `01_Master`
3. Cross-check with `04_Recent_Changes` for current-cycle updates
4. Synthesize and cite source sections
5. Flag if topic is absent from both files (unknown territory)

**Output Format:**
1. Core Doctrine (from `01_Master`)
2. Current Tactical View (from `04_Recent_Changes`, if available)
3. Confidence Level (Doctrine / Tactical / Unknown)
4. Source Reference

---

## WF-09: Contrarian / Opportunity Radar

**Inputs:** Market event, sector selloff, macro panic trigger
**Knowledge Files:** `01_Master` (§2, 3.3, 3.4, 4.4), `04_Recent_Changes`
**Skills:** `macro_analysis_skill`, `stock_analysis_skill`, `valuation_skill`

**Process:**
1. Classify event type (V-panic vs structural damage)
2. Identify affected asset classes and sectors
3. Screen for quality assets now at or near technical support
4. Evaluate thesis integrity (has the selloff damaged the long-term thesis?)
5. Identify accumulation zone entry levels
6. Recommend deployment sizing (partial / aggressive / wait)

**Decision Rules:**
- Do not deploy all dry powder at once → stagger in zones
- Thesis must be intact before adding → never catch falling knives blindly
- If liquidity is impaired → preserve cash first, deploy second
