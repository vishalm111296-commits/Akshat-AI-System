# Dynamic Stock Selection MVP Design

*Mission: Design the absolute smallest dynamic system to replace the failed static stock routing layer, relying entirely on live fundamental data and deterministic constraint filtering without introducing AI/LLMs.*

---

## TASK 1: Minimum Live Data Required

To execute constraint-based filtering, the system must query live financial endpoints. The absolute minimum fields required for a single ticker are:

1.  **Forward P/E Ratio:** (To execute the valuation constraint).
2.  **5-Year Mean P/E Ratio:** (To establish the baseline relative valuation).
3.  **ROCE (Return on Capital Employed) %:** (To execute the capital execution efficiency constraint).
4.  **Debt-to-Equity Ratio:** (To execute the portfolio survival constraint).
5.  **Promoter Classification / Shareholding %:** (To execute the PSU / Skin-in-the-game constraint).
6.  **Revenue Segmentation / Segment %:** (To verify if the stock actually operates in the activated macro sector).

---

## TASK 2: Metric Classification (Akshat's Logic)

Based on the core principles (e.g., "Earnings, not excitement," "Avoid Execution Traps," "Buy fair value"):

**Mandatory (Gatekeepers):**
*   *Valuation Gap:* `Forward P/E` vs `Historical Mean P/E`. (You can never overpay).
*   *ROCE:* (Capital must not be destroyed in the pursuit of growth).
*   *Promoter Classification:* (PSUs are automatic vetoes unless a monopsony framework overrides).
*   *Debt/Equity:* (Bankruptcy protection).

**Useful (Tie-Breakers / Quality Indicators):**
*   *Revenue Growth YoY:* (Proves the macro tailwind is actually hitting the balance sheet).
*   *Operating Margin %:* (Proves the company possesses pricing power).

**Optional (Nice-to-Haves):**
*   *Market Cap:* (Only matters for liquidity rules and position sizing).
*   *Order Book to Bill Ratio:* (Only mandatory for Defense/Infrastructure sectors).

---

## TASK 3: Dynamic Stock Selection Checklist

*A deterministic filtering funnel. A stock must return TRUE on every boolean check to survive.*

*   [ ] **The Domain Check:** Does Sector Revenue > 50% of Total Revenue? (Prevents conglomerates from triggering on a tiny subsidiary).
*   [ ] **The Governance Check:** Is `Promoter != "Government"`? (Unless the framework explicitly activates `[Follow Monopsony Buyers]`).
*   [ ] **The Survival Check:** Is `Debt/Equity < 1.0`?
*   [ ] **The Efficiency Check:** Is `ROCE > 15%`?
*   [ ] **The Valuation Check:** Is `Forward P/E <= (5yr Mean P/E * 1.2)`? (Allowing a slight 20% premium for a confirmed macro tailwind, but blocking 200x parabolic hype cycles).

---

## TASK 4: Preventing Bad Recommendations via Live Data

Reviewing the previous static failures:

**1. BHEL (Nuclear Test)**
*   *Static Failure:* The system recommended it despite the "Avoid PSUs" rule.
*   *Dynamic Prevention:* The live data query would return `Promoter: "Government of India"`. The system would cross-reference the active `[Avoid PSUs]` principle constraint. BHEL fails the **Governance Check** and is automatically dropped from the candidate list.

**2. CG Power (Semiconductor Test)**
*   *Static Failure:* The system recommended a Capital Goods company for a Semiconductor tailwind.
*   *Dynamic Prevention:* The live data query for Revenue Segmentation would return `Capital Goods: 95%, Semiconductors: <5%`. The stock fails the **Domain Check** and is dropped, preventing a false-positive entry into a stock masquerading as a tech play.

**3. "Terminal Value Trap" tests (Logistics, Data Centers, Water)**
*   *Static Failure:* Produced static lists of generic "Risk" stocks.
*   *Dynamic Prevention:* A live query on the actual sector tickers would reveal if a specific company has managed to maintain an ROCE > 15% *despite* the structural trap of the industry. If it does, it proves exceptional management and survives the filter.

---

## TASK 5: The Smallest Possible Implementation

The smallest possible implementation to transform `Sector → Candidate Stocks` without AI reasoning requires:

1.  **A Sector-to-Ticker Ticker List:** Keep `stock_map.json`, but use it *only* as a directory of ticker symbols (e.g., `NSE:DIXON`, `NSE:BHEL`), not as a finalized recommendation list.
2.  **A Financial API Call:** A Python script (e.g., `yfinance` library wrapper) that loops through the tickers in the activated sector and fetches the 6 mandatory data points.
3.  **A Boolean Filter Function:** A simple `filter_stocks(ticker_data, activated_principles)` function that runs the 5-point Checklist. Stocks that return `False` on any mandatory gate are removed from the array.

---

## FINAL VERDICT

**Can stock selection be solved using: Principles + Live Financial Data + Constraint Filtering?**

**YES.**

**Evidence:**
Stock selection, unlike Macro Trend discovery, is fundamentally a mathematical exercise of risk elimination. Akshat's stock selection frameworks ("Avoid high P/E," "Require high ROCE," "Avoid PSUs") are explicit, quantitative boundaries.

While generating a *Macro Framework* requires semantic synthesis and contextual awareness (hence why the routing MVP failed without an LLM), selecting a *Stock* requires strict adherence to mathematical safety rails. If you have the live data (ROCE, Debt, P/E), a deterministic Python `if/else` filter is actually **superior** to an LLM, because LLMs hallucinate numbers and struggle with exact mathematical boundaries.

Deeper reasoning is required to figure out *what* game to play (Macro/Sector). But once the sector is chosen, figuring out *who* survives the cut (Stock) is purely a matter of Principles + Live Financial Data + Constraint Filtering.