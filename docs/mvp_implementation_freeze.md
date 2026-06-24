# MVP Implementation Freeze Review

*This is the final scope review before implementation begins. The scope has been aggressively pruned. Any file or process not strictly required to prove the generative reasoning loop (`Macro Event → Principle Activation → Framework Generation`) has been removed.*

---

## 1. Final File Roster

### File 1: `knowledge/principles/core_catalog.json`
*   **Purpose:** Stores the pre-extracted, abstract Akshat principles used to evaluate macro events.
*   **Input:** Manual creation for MVP (bypassing extraction scripts).
*   **Output:** Read by the collision engine.
*   **Estimated Line Count:** ~40 lines (JSON).

### File 2: `scripts/mvp/ontology_map.json`
*   **Purpose:** Maps specific, real-world sector nouns to abstract, structural principle tags to enable generative reasoning rather than exact keyword matching.
*   **Input:** Manual creation for MVP.
*   **Output:** Read by the collision engine.
*   **Estimated Line Count:** ~20 lines (JSON).

### File 3: `scripts/mvp/macro_input.json`
*   **Purpose:** Provides the simulated macro event triggers that the engine will analyze.
*   **Input:** Manual creation for MVP.
*   **Output:** Read by the collision engine.
*   **Estimated Line Count:** ~15 lines (JSON).

### File 4: `scripts/mvp/2_collide.py`
*   **Purpose:** The core engine. It parses the macro input, translates nouns using the ontology map, matches abstract tags against the core catalog, mathematically resolves polarities (tailwinds vs. constraints), and synthesizes a framework.
*   **Input:** `macro_input.json`, `ontology_map.json`, `core_catalog.json`.
*   **Output:** Generates a markdown Reasoning Report.
*   **Estimated Line Count:** ~100 lines (Python).

### File 5: `docs/mvp_output/generated_frameworks/MACRO-TEST-02.md`
*   **Purpose:** The final output artifact proving the architecture successfully reasoned through the event.
*   **Input:** Output from `2_collide.py`.
*   **Output:** Human-readable text.
*   **Estimated Line Count:** ~25 lines (Markdown).

---

## 2. Removed Scope

To maintain the absolute minimum viable product focused *only* on framework generation, the following files originally proposed have been **removed** from the MVP scope:

*   `raw_sources/mvp_test_data/mock_transcripts.json` (Extraction is not generation).
*   `scripts/mvp/1_extract.py` (Proving extraction is a separate problem from proving collision).

---

## 3. Aggregates

*   **Total Code Estimate:** ~100 lines of Python.
*   **Total JSON Estimate:** ~75 lines of JSON.
*   **Total Test Data Estimate:** 0 lines (The `macro_input.json` serves as the sole trigger, replacing the need for a mock corpus).

**Total System Size:** Less than 200 lines across 4 active files.