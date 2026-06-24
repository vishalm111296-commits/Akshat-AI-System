# Goal Drift Analysis

*The original goal of the Akshat Reasoning System was: **Opportunity discovery → Trend detection → Sector conversion → Stock discovery → Watchlists**.*

*This document analyzes where the architecture drifted away from Alpha Generation and devolved into a Knowledge Management and Keyword Routing system.*

---

## Ranked Drift Risks (Highest to Lowest)

### 1. The "Reasoning Report" Drift (Severity: Critical)
**The Drift:** The MVP's final output is a Markdown text file called a "Reasoning Report."
**Why it failed the original goal:** The original goal demanded *Watchlists*. Producing a nicely formatted markdown summary of a macro event is a pure Knowledge Management/Documentation task. It halts the pipeline before any financial data is ever touched. The architecture became obsessed with *explaining* the collision rather than *capitalizing* on it.

### 2. The Ontology Dictionary Drift (Severity: Critical)
**The Drift:** To solve the MVP's inability to do semantic abstraction, we built `ontology_map.json`.
**Why it failed the original goal:** We drifted into Taxonomy Building. By forcing developers to manually map "semiconductor" to "capex", the system became a glorified hardcoded keyword router. It completely abandoned the goal of automated Trend Detection; the system can only detect what the human explicitly types into the dictionary.

### 3. The Extraction Bias Drift (Severity: High)
**The Drift:** Phase 1 focused heavily on scraping transcripts, counting evidence, calculating frequencies, and building a `core_catalog.json`.
**Why it failed the original goal:** We built a Search/Archive tool. By weighting "Frequency" and "Time Persistence," the system became an expert at telling the user what Akshat said 3 years ago. It drifted entirely away from "finding emerging trends early," requiring the panicked addition of Phase 1.5 (Emerging Frameworks) to patch the mistake.

### 4. The "Missing Last Mile" Drift (Severity: High)
**The Drift:** In the ruthless MVP audit, we stripped out the Opportunity Scanner and the Stock Discovery Engine to make the code "less than 200 lines."
**Why it failed the original goal:** We cut off the actual utility. By declaring success at "Framework Generation" (e.g., "State-Sponsored Catch-Up Narrative"), the system fails to convert trends into sectors, and sectors into stocks. It is an incomplete pipeline masquerading as a finished product.

### 5. The Polarity Math Drift (Severity: Medium)
**The Drift:** The Collision engine resolves frameworks by counting Positive vs. Negative principles (`len(pos) > len(neg)`).
**Why it failed the original goal:** We drifted into simplistic symbolic logic. The original goal requires "Rejecting bad ideas." A single, massive valuation constraint (e.g., 200x P/E) should veto 10 positive macro tailwinds. By treating all tags equally, the system loses the nuance required for real Opportunity Discovery.