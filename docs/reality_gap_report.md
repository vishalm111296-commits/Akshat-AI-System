# Reality Gap Report

*A brutal comparison of what the architecture claims it can do versus what the frozen MVP will actually execute.*

---

### Gap 1: Discovery vs. Dictionary
*   **Architecture Claim:** The Emerging Framework Engine will discover novel mental models and structural shifts before broad consensus.
*   **MVP Reality:** The MVP relies entirely on a hardcoded `ontology_map.json`. If a structural shift involves a noun not manually mapped by the developer in advance, the system triggers a null output. It discovers nothing; it only routes pre-defined keywords.

### Gap 2: Synthesis vs. Conditionals
*   **Architecture Claim:** The Macro-to-Principle Collision Engine synthesizes conflicting structural tailwinds and execution constraints into a unique, generative thesis.
*   **MVP Reality:** `2_collide.py` counts the number of positive vs. negative tags and triggers one of three hardcoded `if/elif` string returns (e.g., if pos > 0 and neg > 0: return "State-Sponsored Catch-Up"). There is zero generative synthesis.

### Gap 3: Intelligence vs. Tallying
*   **Architecture Claim:** The Principle Extraction Engine detects sophisticated recurring mental models by semantically analyzing years of transcripts and assigning confidence scores.
*   **MVP Reality:** The MVP extraction script (`1_extract.py`) was stripped. The system simply loads `core_catalog.json` into memory. The "confidence" and "evidence" metrics are inert integers that do not impact the collision math.

### Gap 4: Output vs. Action
*   **Architecture Claim:** The system converts macro trends into actionable sector and stock-level insights, generating watchlists while rejecting bad ideas via the Doubt Engine.
*   **MVP Reality:** The system outputs a `.md` text file containing a generic paragraph formed by concatenating JSON description strings. It connects to zero financial databases, scans zero stocks, and produces zero watchlists.

### Gap 5: Automation vs. Manual Labor
*   **Architecture Claim:** An automated reasoning loop that continuously ingests macro inputs and spits out opportunities.
*   **MVP Reality:** The user must manually write a `macro_input.json` file containing explicit `trigger_tags` and manually run a local Python script to get a text file back.

### Gap 6: Abstraction vs. Exact Match
*   **Architecture Claim:** The system uses semantic distance (Embeddings/LLMs) to map messy real-world events to abstract core principles.
*   **MVP Reality:** The system uses Python's `set().intersection()` to see if string "A" exactly equals string "A". Case sensitivity was patched, but synonymous phrasing (e.g., "capex" vs "capital expenditure") will silently break the collision.