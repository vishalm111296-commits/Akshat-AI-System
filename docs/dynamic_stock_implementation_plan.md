# Dynamic Stock Selection: Implementation Plan

*Mission: Prepare the first implementation plan to build the Dynamic Stock Selection MVP, replacing the failed static stock routing layer.*

---

## TASK 1: Live Data Source Identification

To execute constraint-based filtering without heavy enterprise subscriptions (like Bloomberg Terminal), we will rely on open/accessible API providers (e.g., `yfinance` or an aggregator like `AlphaVantage` / `FinancialModelingPrep`).

| Metric | Primary Source | Availability | Update Frequency |
| :--- | :--- | :--- | :--- |
| **Forward P/E Ratio** | `yfinance` (info['forwardPE']) | High (Large/Mid Caps), Low (Micro Caps) | Daily (Price dependent) |
| **Trailing P/E Ratio** | `yfinance` (info['trailingPE']) | High | Daily |
| **ROCE %** | `yfinance` / Fundamental APIs | Medium (Often requires deriving from EBIT / Capital Employed) | Quarterly (Earnings releases) |
| **Debt-to-Equity Ratio** | `yfinance` (info['debtToEquity']) | High | Quarterly (Balance sheets) |
| **Promoter Holding / Classification** | `yfinance` (info['heldPercentInsiders']) / NSE India API | Medium (Granular PSU classification requires manual tagging or specific India-focused APIs like Screener.in) | Quarterly (Shareholding patterns) |
| **Revenue Segmentation** | Annual Reports / specialized fundamental APIs | Low (Very difficult to extract cleanly via free APIs) | Annually / Quarterly |

---

## TASK 2: Exact Filtering Sequence

The filter acts as a strict "drop-down" funnel. A stock must pass every gate to reach the bottom.

1.  **Step 1: The Sector Universe.** (Input from Layer 3). Retrieve the broad list of all tickers mapped to the identified Sector.
2.  **Step 2: The Principle Veto Gate.** Parse `activated_principles`. If a principle contains a `veto_tag` (e.g., "psu", "esg_restricted"), check the stock's basic classification metadata. If it matches, *Drop*.
3.  **Step 3: The Efficiency Gate (ROCE Filter).** Query fundamental API. Is `ROCE >= 15%` (or sector historical mean)? If False, *Drop*.
4.  **Step 4: The Survival Gate (Debt Filter).** Query fundamental API. Is `Debt/Equity <= 1.0` (excluding Financials)? If False, *Drop*.
5.  **Step 5: The Valuation Gate (P/E Filter).** Query fundamental API. Is `Forward P/E < (5yr Trailing Mean P/E * 1.2)`? If False, *Drop*.
6.  **Step 6: Output.** Return the surviving tickers.

---

## TASK 3: Test Plan (Dynamic vs. Static)

**Hypothesis:** The Dynamic filter will eliminate false positives (expensive/bad stocks) and circular logic (violating principles) that the Static mapper allowed.

**Test Execution:**
1.  Run the 10 Macro Event tests from the MVP phase.
2.  Record the stocks outputted by the old `stock_map.json` (Static List).
3.  Run the exact same 10 tests through the new Dynamic Filter script.
4.  Record the surviving stocks (Dynamic List).

**Evaluation Metrics:**
*   **The Contradiction Catch:** Did the Dynamic filter drop BHEL during the Nuclear test? (Proves Governance/Principle veto works).
*   **The Valuation Catch:** Did the Dynamic filter drop high-growth stocks currently trading at >100x P/E? (Proves Valuation gate works).
*   **The Zombie Catch:** Did the Dynamic filter drop legacy manufacturing stocks with <8% ROCE and high debt during the Capex tests? (Proves Efficiency/Survival gates work).
*   **Success:** The Dynamic List must be smaller, higher quality, and strictly compliant with all activated principles compared to the Static List.

---

## TASK 4: Implementation Complexity Estimates

| Component | Difficulty | Risk | Time to Implement |
| :--- | :--- | :--- | :--- |
| **Sector-to-Ticker Database** (Expanding `sector_map.json` to hold exhaustive arrays of base tickers) | Low | Low (Tedious manual entry) | 1 Day |
| **API Integration** (Wiring `yfinance` to fetch the 4 core fundamental metrics) | Medium | Medium (Rate limits, missing data fields for Indian small-caps) | 2 Days |
| **Boolean Filtering Logic** (The Python sequential funnel) | Low | Low (Basic if/else math) | 1 Day |
| **Veto Tag Alignment** (Updating `core_catalog.json` with veto tags) | Low | Low | 0.5 Days |

---

## TASK 5: The Smallest Possible Build

The smallest possible build that can generate better candidates than the static mapper is:
**A static Sector-to-Ticker list + a live Valuation/Debt API filter.**

We can temporarily skip the complex "Revenue Segmentation" and detailed "Promoter Classification" data pulls (which are notoriously hard to get for free). By simply passing a list of 50 sector stocks through an API that checks `Forward P/E` and `Debt/Equity`, we immediately eliminate 70% of the market's garbage and strictly enforce Akshat's two most immutable laws: "Don't overpay" and "Don't buy bankruptcy risk."

---

## FINAL VERDICT

**Is Dynamic Stock Selection the next phase?**

**NO.**

### Defense:
While Dynamic Stock Selection is mathematically necessary to produce a valid watchlist, it is *not* the correct next phase to build.

**You must fix the Framework Generation layer first.**

As proven in the previous Root Cause Analysis, the system currently outputs hardcoded framework strings and relies on a highly brittle, static `ontology_map.json`. If you input "Water," the system generates a "Terminal Value Trap" framework, which leads to a "Heavy Manufacturing" sector map, which leads to Heavy Manufacturing stocks.

If you build the Dynamic Stock Filter now, it will simply run beautiful, complex financial math to find the very best Heavy Manufacturing stocks to buy when the user actually wanted to invest in Water Treatment.

*Garbage in, garbage out.* You cannot build a high-fidelity quantitative stock screener on top of a broken, non-generative, hardcoded text router. The immediate next phase must be unblocking the Generative Reasoning layer (incorporating semantic embeddings / LLMs) to ensure the `Framework -> Sector` handoff is actually accurate. Only once the system can reliably map "Water" to "Water Utilities" should we build the API logic to filter those utility stocks.