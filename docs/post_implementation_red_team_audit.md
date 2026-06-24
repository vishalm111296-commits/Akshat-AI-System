# Post-Implementation Red Team Audit

> **CRITICAL CONTEXT NOTE:** This audit evaluates the *actual, physical implementation* of the MVP just executed in the repository (`scripts/mvp/collide.py`, `core_catalog.json`, `ontology_map.json`). It is not based on blueprints, but on running code.

---

## TASK 1: Hardcoded, Brittle, and Fake Reasoning

**Where the system is Hardcoded:**
- `ontology_map.json`: "semiconductor" is hardcoded directly to `["ai_infrastructure", "tech_hardware"]`. It does not "understand" what a semiconductor is.

**Where the system is Overfit:**
- The conflict resolver (`collide.py:44`): `if t_tags.intersection(c_tags):` - The system assumes a Tactic only conflicts with a Constraint if they share the exact same abstract tag. It is overfit to a perfect tag-overlap scenario that rarely happens in real text.

**Where the system is Brittle:**
- `extract_tags()` uses `if keyword.lower() in text_lower:`. If the text says "semiconductors" (plural), it will match because "semiconductor" is a substring. But if the text says "manufacturing incentive" (singular), it will *not* match the map's plural "manufacturing incentives". It breaks on standard grammar.

**Where the system is Circular:**
- There are no circular loops causing crashes *yet*, but only because `collide.py` explicitly ignores the `parent_id` hierarchy. It flattens everything. The intended circularity of the design was mitigated by the developer (me) writing a flattened list in Markdown.

**Where the system is Producing Fake Reasoning:**
- The markdown output (`collide.py:75`): `md += f"- **{c['principle_id']}**: {c['name']} (Triggered by: {', '.join(c['matched_tags'])})\n"`. The report looks intelligent, but it is just a `for` loop printing JSON properties. No inference is occurring.

---

## TASK 2: Keyword vs. Reasoning

**Determine whether the system is actually doing:**
Macro Event → Principle Activation → Framework Generation

**OR merely:**
Keyword → Keyword → Template

**Verdict:** It is merely **Keyword → Keyword → Template.**

**Evidence from Code:**
1. `tags.update(matched_tags)` inside `extract_tags`: Takes a hardcoded dictionary value based on a substring (Keyword -> Keyword).
2. `tags_set.intersection(p_tags)` inside `fetch_active_principles`: Takes the first Keyword and matches it to an array in `core_catalog.json` (Keyword -> Keyword).
3. `generate_markdown()` string assembly: `md += f"- **{t['principle_id']}**: {t['name']}\n"`: Dumps the result into a static file (Template).
There is zero generative text, contextual analysis, or reasoning.

---

## TASK 3: Adversarial Tests (Execution Results)

*Note: These tests simulate modifying `macro_input.json` and running the current `collide.py`.*

### 1. Semiconductor incentives
* **Input:** "Government launches major semiconductor manufacturing incentives."
* **Activated principles:** P-EarningsGravity, SS-03, GF-05, RM-02.
* **Generated framework:** Generated successful report listing RM-02 as a constraint and GF-05 as a tactic.
* **Failure analysis:** "Success" is an illusion. It worked perfectly only because the exact substrings "semiconductor" and "manufacturing incentives" were seeded in the ontology map.

### 2. Nuclear energy incentives
* **Input:** "Govt subsidizes nuclear energy capex."
* **Activated principles:** None (assuming "capex" isn't in ontology directly as a key; "manufacturing incentives" is).
* **Generated framework:** "No actionable principles."
* **Failure analysis:** Without "manufacturing incentives" explicitly written, the system misses the entire capex cycle.

### 3. Water infrastructure spending
* **Input:** "Massive spending bill passed for water infrastructure."
* **Activated principles:** None.
* **Generated framework:** "No actionable principles."
* **Failure analysis:** The ontology does not contain "water", "infrastructure", or "spending". The engine goes blind.

### 4. Logistics corridor expansion
* **Input:** "Railways building a new freight logistics corridor."
* **Activated principles:** None.
* **Generated framework:** "No actionable principles."
* **Failure analysis:** System cannot read synonyms.

### 5. Unknown industry
* **Input:** "Dyson sphere construction authorized."
* **Activated principles:** None.
* **Generated framework:** "No actionable principles."
* **Failure analysis:** Handled gracefully, but highlights that the system relies entirely on hardcoded dictionary lookups.

---

## TASK 4: Can this MVP discover a framework that does not already exist?

**Answer:** NO.

**Justification:**
Looking at the source code of `collide.py`, the function `fetch_active_principles()` iterates exclusively over `catalog`. It returns `p["id"]` and `p["name"]`. The `generate_markdown()` function then directly prints `p["name"]`. The code does not contain an LLM API call. It does not contain string synthesis. It does not combine two principles into a new string. It mathematically cannot output a framework that is not literally typed into `core_catalog.json`.

---

## TASK 5: Top 10 Weaknesses (Ranked by Severity)

1. **Zero Semantic Inference:** `if keyword.lower() in text_lower` is a 1990s-era keyword scraper. It cannot understand syntax, context, or negation (e.g., "NO rate cut").
2. **Conflict Resolution is Broken:** `resolve_conflicts()` only suppresses a Tactic if it shares the *exact* same abstract tag as a Constraint. Real-world conflicts span different tags (e.g., Risk triggers on "Tech", Tactic triggers on "Capex" - system fails to suppress).
3. **Hierarchy Ignored:** `collide.py` completely ignores `parent_id`. It prints Parents and Children side-by-side as peers, rendering the complex JSON taxonomy useless.
4. **Maintenance Nightmare:** To handle real inputs, `ontology_map.json` must grow to tens of thousands of lines of manual substring maps.
5. **Plurals/Typos Break It:** Exact substring matching means "rate cuts" vs "rate cut" causes silent data drops.
6. **No "Why" Generation:** The Markdown report gives a list of principles but cannot synthesize a cohesive paragraph explaining *why* they interact.
7. **No Negative Tag Logic:** The schema uses `activation_tags` but lacks `deactivation_tags` (e.g., if "war" is present, ignore "margin_expansion").
8. **Static Output:** The Markdown template is completely hardcoded.
9. **Boolean Brittle Logic:** `ALL` logic requires perfect tag overlaps, ensuring false negatives.
10. **Test Suite is Self-Fulfilling:** `test_collide.py` just tests if Python standard libraries (dictionaries, sets) work. It doesn't test the quality of reasoning.

---

## FINAL VERDICT

### Scores
* **Reasoning Authenticity:** 0/10 *(It is `if string in text` logic).*
* **Framework Generation:** 1/10 *(It prints a list; it generates nothing).*
* **Generalization:** 0/10 *(Fails instantly on synonyms).*
* **Maintainability:** 2/10 *(Scaling the ontology map will break the system).*
* **Expansion Readiness:** 1/10 *(Requires total rewrite to integrate LLMs).*

### Answer to the Final Question
**If we had to throw away 50% of the MVP tomorrow, what would we delete first?**

Throw away `ontology_map.json` and the `extract_tags()` function in `collide.py`.

The attempt to build a deterministic, substring-based translation layer for complex macroeconomic events is the root cause of every failure in this audit. The system must use an LLM/embeddings engine to convert the `raw_text` into abstract tags, otherwise the remaining collision logic will forever starve for data.
