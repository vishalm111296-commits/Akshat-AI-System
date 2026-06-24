# One-Week Improvement Plan (MVP Optimization)

## Overview
This plan outlines a strict, 5-day engineering effort to optimize the existing deterministic MVP (`2_collide.py`). It adheres entirely to the frozen architecture constraints: No LLMs, no embeddings, no vector databases, and no new engines.

The goal is to push the deterministic router to its absolute maximum utility.

---

## Part 1: Ranked Improvement List (By ROI)

### 1. Upgrade Ontology Matching to Regex (Fuzzy Router)
* **Description:** Replace the naive substring match (`if keyword in text`) in `extract_tags()` with regular expressions (Regex). This allows the dictionary keys to handle plurals, verb conjugations, and minor variations (e.g., `rate cuts?`, `manufactur\w* incentiv\w*`).
* **Expected Impact:** Instantly solves 50% of the false-negative routing failures caused by basic grammatical variations.
* **Complexity:** Low (Python `re` module).
* **Risk:** Medium (Poorly written regex can cause catastrophic backtracking or excessive false positives).

### 2. Implement Combinatorial Synthesis Rules (CSR)
* **Description:** Add a new JSON array to `core_catalog.json` defining `synthesis_rules`. If specific Principle IDs trigger simultaneously (e.g., `SS-04` + `MF-03`), output a pre-written, highly specific synthesis string (e.g., "AI capex will bottleneck the power grid.").
* **Expected Impact:** Creates the illusion of reasoning by replacing isolated bullet points with contextual, multi-variable logic statements.
* **Complexity:** Medium (Requires JSON schema update and combinatorial checking in `collide.py`).
* **Risk:** Low.

### 3. Domain-Aware Conflict Resolution
* **Description:** Currently, constraints blindly suppress any tactic sharing an underlying tag. Update the conflict resolver to only suppress tactics if the Constraint and Tactic share the *same domain* (e.g., both are in "Options" or "Geography") OR if the Constraint explicitly lists the Tactic in a new `suppresses_ids` array.
* **Expected Impact:** Prevents illogical suppression (e.g., a Real Estate constraint deleting an AI infrastructure tactic just because they both shared an "infrastructure" tag).
* **Complexity:** Low (Simple attribute matching).
* **Risk:** Low.

### 4. Implement Negative Tag Logic (`deactivation_tags`)
* **Description:** Add an array to the ontology map representing negative sentiment (e.g., "halt", "cancel", "ban", "end"). If the event contains these words, negate the activation of the primary tag.
* **Expected Impact:** Prevents the system from incorrectly saying "Buy AI" when the headline reads "Government *bans* AI infrastructure."
* **Complexity:** Medium (Requires two-pass parsing over the text).
* **Risk:** High (Very brittle. The word "ban" might be in a different sentence, causing unrelated tags to deactivate).

### 5. Hierarchical Markdown Output Formatting
* **Description:** Modify the `generate_markdown()` f-string logic to respect the `parent_id` field. Group Tactics physically underneath their Parent Themes in the Markdown document, using indentation.
* **Expected Impact:** Massively improves human readability and logical flow of the output report.
* **Complexity:** Low (Recursive or nested loop printing).
* **Risk:** Low.

---

## Part 2: Recommended Implementation Order

This order minimizes blocking dependencies and sequences the work logically over one week:

**Day 1:** Implement *Hierarchical Markdown Output Formatting* (Quick win, visually verifies hierarchy).
**Day 2:** Implement *Domain-Aware Conflict Resolution* (Fixes the broken logic of the current suppression engine).
**Day 3:** Upgrade *Ontology Matching to Regex* (Expands the input catch-rate massively).
**Day 4:** Implement *Combinatorial Synthesis Rules* (Adds the final "insight" layer).
**Day 5:** Implement *Negative Tag Logic* (Save for last due to highest brittleness risk).

---

## Part 3: Expected Change in Behavior

Post-implementation, the system will shift from a "Fragile Dictionary" to a "Robust Expert System."

1. **Input Resiliency:** It will successfully route inputs like "Nuclear incentives" or "Semiconductor subsidies" even if phrased differently, significantly reducing the "No actionable principles" errors.
2. **Cohesive Output:** Instead of printing a flat, disconnected list of rules, the Markdown report will group tactics logically under macro themes.
3. **Simulated Insight:** When two interacting trends appear, the Combinatorial Synthesis will print a targeted insight, giving the user a unified strategy paragraph rather than isolated rules.

---

## Part 4: What Will Still Remain Unsolved (Brutally Realistic)

Even after this perfect one-week optimization, the MVP will still hit a hard ceiling:

1. **It Still Cannot Reason:** It remains a deterministic `if-then` router. It cannot infer that "Dyson Sphere" equals "Massive Capex" unless a human explicitly types "Dyson Sphere" into the regex dictionary.
2. **Maintenance Nightmare:** While Regex helps with plurals, it does not help with synonyms. The `ontology_map.json` will still require a human to manually map thousands of financial terms.
3. **No Market Awareness:** The script still has no connection to live market data. It will happily recommend buying a semiconductor stock that is already trading at 300x PE because it cannot read valuations.
4. **No Alpha Generation:** The system will output incredibly structured, logical, and readable reports about *past* Akshat Shrivastava frameworks. It will not, and mathematically cannot, discover a trend that hasn't already been pre-programmed into the JSON arrays.

**Final Verdict:** This one-week sprint perfectly polishes the router, but it is the final terminus of this architecture. To progress beyond this, the "No LLM / No Embeddings" constraint must be lifted.