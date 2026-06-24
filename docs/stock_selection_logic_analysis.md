# Stock Selection Logic Analysis

*Mission: Perform a Root Cause Analysis defining exactly where Akshat's stock-selection logic begins, why the static MVP failed, and what minimum quantitative inputs are required to succeed.*

---

## TASK 1: Separating the Logic Layers

A fundamental error in the MVP was treating Stock Selection as a continuation of Macro logic. They are distinct reasoning domains.

### A. Trend Selection Logic (The "Why")
*   *Domain:* Macroeconomics, Policy, Demographics.
*   *Akshat's Focus:* Identifying undeniable, multi-year tailwinds (e.g., "India needs infrastructure," "The West is derisking from China").
*   *Output:* A directional bias.

### B. Sector Selection Logic (The "Where")
*   *Domain:* Value chains and profit pools.
*   *Akshat's Focus:* Identifying which part of the value chain actually captures the margin. (e.g., "Don't buy the EV maker; buy the EV charging infrastructure or the battery chemical supplier").
*   *Output:* A specific sub-industry.

### C. Stock Selection Logic (The "Who")
*   *Domain:* Microeconomics, Corporate Governance, Valuation.
*   *Akshat's Focus:* Ruthless elimination. Trend and Sector provide the tailwind, but Stock Selection is entirely about surviving execution risks and not overpaying.
*   *Output:* A singular, investable ticker.

---

## TASK 2: Minimum Required Information

To choose a stock, a macro tailwind is insufficient. Akshat's framework requires explicit, mandatory financial and governance data to clear the "Stock Selection" hurdle.

**Mandatory Quantitative Data:**
1.  **Valuation (Fwd P/E vs Historical Mean):** A great company in a great sector is a "Reject" if priced for perfection (e.g., trading at 150x P/E).
2.  **Capital Efficiency (ROCE):** Must be historically proven or visibly expanding. A company destroying capital during a boom is uninvestable.
3.  **Debt (Debt/Equity):** High leverage in a rising interest rate environment violates portfolio survival principles.

**Mandatory Qualitative/Governance Data:**
4.  **Promoter Integrity/Ownership:** Is the business founder-led with skin in the game, or a PSU/bureaucratic entity?
5.  **Capital Allocation History:** Does the management reinvest intelligently or squander cash on unrelated acquisitions?

*Order Book and Growth are secondary confirmation metrics; Valuation, Debt, and ROCE are the absolute mandatory gatekeepers.*

---

## TASK 3: Stock Evaluation Checklist

*This is a strict sequential checklist. A stock must pass every layer to be selected.*

1.  [ ] **Sector Alignment:** Does the company derive >50% of its forward revenue from the specifically identified Framework Sector?
2.  [ ] **Governance Gate:** Is the company free of State-Ownership (PSU) constraints (unless explicitly overridden by a Monopsony framework)?
3.  [ ] **Leverage Gate:** Is Debt/Equity < 1.0 (or manageable within sector norms)?
4.  [ ] **Efficiency Gate:** Is ROCE > 15% (or showing a multi-quarter trajectory of expanding operating margins)?
5.  [ ] **Valuation Gate:** Is the current price trading at or below its 5-year historical average valuation multiple relative to its expected earnings growth?

*Failure on any single checkbox results in rejection, regardless of the Macro Trend.*

---

## TASK 4: Review of Failed Stock-Discovery Tests

**Bad Recommendation 1: BHEL (Nuclear Test)**
*   *The Failure:* The system recommended a PSU despite an explicit "Avoid PSUs" framework constraint.
*   *Missing Information that would have prevented it:* The **Governance Gate**. If the system had access to a basic data tag identifying "Promoter = Government of India", it would have checked this against the Framework constraint and vetoed the stock immediately.

**Bad Recommendation 2: CG Power (Semiconductor Test)**
*   *The Failure:* The system recommended a heavy Capital Goods company for a Semiconductor tailwind.
*   *Missing Information that would have prevented it:* The **Sector Alignment Gate**. If the system had access to a "Revenue Segmentation" breakdown, it would see that semiconductors represent near 0% of current trailing revenue, preventing a premature entry based purely on JV headlines.

---

## TASK 5: The Smallest Possible Stock Selection MVP

The smallest possible MVP capable of selecting stocks inside a sector is **a basic fundamental API filter**.

It does not require an LLM or an AI Agent. It requires:
1.  A list of tickers belonging to the target sector.
2.  A script that calls a financial API (e.g., Yahoo Finance) for those specific tickers.
3.  A Python function that drops any ticker where `Debt/Equity > 1.5` or `Forward P/E > 80`.

This transforms the layer from "Static Routing" into "Quantitative Filtering."

---

## FINAL VERDICT

"The system fails at Stock Discovery because **it substitutes static dictionary lookups for dynamic fundamental analysis**."

**The Single Most Important Missing Ingredient:**
**Live Financial Data.**

You cannot execute Akshat's stock selection logic using text files. His stock selection is fundamentally rooted in *valuation* and *capital efficiency* (ROCE/Debt). Without the ability to query live P/E ratios and balance sheet metrics, the system is permanently blind to the very constraints that define his investing philosophy.