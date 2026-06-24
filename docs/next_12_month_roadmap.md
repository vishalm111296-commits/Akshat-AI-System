# Next 12-Month Implementation Roadmap

## Objective
Design the absolute shortest implementation path from the current brittle MVP to the original goal: **Trend Discovery → Sector Discovery → Stock Discovery → Watchlists**, without inventing new architecture.

---

## Milestone 1: Fix the Core (Months 1-2)
*Goal: Replace the hardcoded dictionary with semantic routing.*
- **Action 1.1:** Delete `ontology_map.json` and the naive string-matching in `collide.py`.
- **Action 1.2:** Implement standard text embeddings for `core_catalog.json` principles.
- **Action 1.3:** Rewrite the input parser to embed the `raw_text` of the Macro Event and perform cosine similarity against the Catalog to trigger `activation_tags`.
- *(Result: The system can now understand synonyms and unknown industries without human hardcoding).*

## Milestone 2: Actual Framework Generation (Months 3-4)
*Goal: Move from Markdown Templates to Generative Reasoning.*
- **Action 2.1:** Delete the `generate_markdown` f-string template in `collide.py`.
- **Action 2.2:** Pass the output of the Conflict Resolver (the filtered list of Principles + the raw Macro Event) into an LLM context window.
- **Action 2.3:** Prompt the LLM to synthesize the *interaction* between the event and the principles, forcing it to deduce the logical sector impact.
- *(Result: The system stops returning Mad Libs and starts outputting actual macro-theses).*

## Milestone 3: Sector Discovery Pipeline (Months 5-7)
*Goal: Bridge the gap between Principles and Tradable Sectors.*
- **Action 3.1:** Implement the "Opportunity Scanner" defined in the original architecture.
- **Action 3.2:** Connect a basic financial API (e.g., Yahoo Finance, AlphaVantage) to pull real-time GICS sector performance.
- **Action 3.3:** Have the Generative Framework (from M2) output a rigid JSON array of `["Target_Sectors"]`.
- *(Result: The framework translates "K-shaped margin expansion" into `"GICS: Healthcare Equipment"`).*

## Milestone 4: Stock Discovery & Filtering (Months 8-10)
*Goal: Convert Sectors into specific tickers using the Constraints.*
- **Action 4.1:** Implement the "Stock Discovery Engine".
- **Action 4.2:** Query the financial API for all tickers within the `Target_Sectors`.
- **Action 4.3:** Programmatically apply the Activated Constraints (e.g., `SS-04: Buy near 200DMA`, `SS-06: Avoid extreme PE`).
- **Action 4.4:** Filter the raw ticker list through these hard metric constraints.
- *(Result: A universe of 500 sector stocks is reduced to 12 stocks that actually obey Akshat's valuation rules).*

## Milestone 5: Watchlist Output (Months 11-12)
*Goal: Deliver the final user value.*
- **Action 5.1:** Format the output of Milestone 4 into a trackable Watchlist format.
- **Action 5.2:** Add a cron job to re-run the `Stock Discovery Filtering` on the watchlist daily to alert the user when a stock finally hits the required entry parameter (e.g., drops to the 200DMA).
- *(Result: The Original Goal is achieved).*
