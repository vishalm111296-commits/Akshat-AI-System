# Next 12-Month Roadmap

*The shortest path to bridge the MVP back to the original goal: Trend Discovery → Sector Discovery → Stock Discovery → Watchlists.*
*Constraint: No new architecture allowed. We must implement the existing conceptual engines.*

---

## Q1: Unblock Generative Reasoning (The Semantic Upgrade)
**Goal:** Replace the brittle keyword router with actual generative synthesis.
*   **Milestone 1:** Delete `ontology_map.json` and hardcoded `if/else` framework strings.
*   **Milestone 2:** Implement a local, lightweight open-source embedding model (e.g., SentenceTransformers) to replace exact tag matching. Allow "Chips" to semantically trigger the "Semiconductor" → "Capex" principle pathway.
*   **Milestone 3:** Connect a local LLM to `2_collide.py` to ingest the Activated Principles and generate a unique Framework Title and Reasoning Paragraph dynamically, rather than concatenating static strings.

## Q2: Build the Trend-to-Sector Bridge (Opportunity Scanner V1)
**Goal:** Prove the generated framework has actual financial validity in the real world.
*   **Milestone 4:** Implement the first leg of the Opportunity Scanner. It will take the LLM-generated Framework and map it to specific GICS sectors or sub-industries.
*   **Milestone 5:** Connect an external financial data API (e.g., Yahoo Finance, AlphaVantage).
*   **Milestone 6:** Query the API to check if the identified sector is showing Aggregate Revenue/Margin expansion over the Trailing Twelve Months (TTM). If False, trigger the Doubt Engine to halt the pipeline.

## Q3: Sector-to-Stock Discovery
**Goal:** Filter the validated sector for specific companies using Akshat's constraints.
*   **Milestone 7:** Program the Stock Discovery Engine constraints. Translate `[Avoid Capital Execution Traps]` into a hard financial query: `Filter: Debt-to-Equity < X, ROCE > Y`.
*   **Milestone 8:** Program the Valuation constraints. Translate `[Price-to-Earnings Disconnect]` into `Filter: Fwd P/E < 5yr Historical Mean`.
*   **Milestone 9:** Run the surviving sector list through the programmed constraints to yield a final list of ticker symbols.

## Q4: Watchlist Generation & Automation
**Goal:** Close the original goal loop by outputting actionable lists.
*   **Milestone 10:** Update the output logic to append the discovered ticker symbols to the `Reasoning Report`.
*   **Milestone 11:** Implement formatting logic to auto-generate a `WATCHLIST_YYYYMMDD.md` containing the Framework Title, the triggering Macro Event, and the list of surviving stocks with their current P/E and ROCE.
*   **Milestone 12:** Build the `macro_input.json` generator. Connect an RSS feed of financial news to automatically extract `trigger_tags` and feed them into `2_collide.py` on a daily cron job, fully automating the pipeline.