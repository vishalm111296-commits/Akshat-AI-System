# Root Cause Analysis

## Overview
This document analyzes the root cause of why the Phase 2 MVP functions as a deterministic key-value router rather than a generative reasoning system.

---

## TASK 1: Where Reasoning Disappears

Let's trace the exact pipeline to see where reasoning is lost.

**1. Macro Input (`raw_text`)**
*What happens:* A complex, nuanced sentence is ingested.
*Where reasoning disappears:* Reasoning has not yet disappeared; the context is fully present in the string.

**2. Ontology (`extract_tags()`)**
*What happens:* The system iterates over a hardcoded dictionary (`ontology_map.json`). If a key exists as a substring in the input, the system adds the mapped tags to a list.
*Where reasoning disappears:* **Reasoning disappears here.** The system instantly destroys all context, syntax, negation, and nuance. It collapses the entire sentence into an array of isolated strings (e.g., `["capex_cycle", "tech_hardware"]`). The context of *who* is doing the capex, or *why*, is permanently deleted from memory.

**3. Principles (`fetch_active_principles()`)**
*What happens:* The system loops over `core_catalog.json`. If a principle's `activation_tags` array contains any of the tags from Step 2, the principle is added to a list.
*Where reasoning disappears:* There is no reasoning here to lose. The system is performing a simple SQL-style `WHERE tag IN tags` query. It does not evaluate *how* the principle applies to the event; it only checks if the pre-assigned tags match.

**4. Framework (`generate_markdown()`)**
*What happens:* The system takes the list of activated principles and dumps their pre-written `name` fields into a rigid f-string Markdown template.
*Where reasoning disappears:* The final opportunity for reasoning is bypassed. The system concatenates static strings instead of synthesizing a relationship between the principles and the original macro event.

**Conclusion:** Reasoning is annihilated in **Step 2 (Ontology)** when contextual human language is irreversibly flattened into discrete, context-blind tags.

---

## TASK 2: Analysis of the 10 Macro Tests

**1. Semiconductor incentives**
* **Expected:** System identifies tech capex and connects it to margin expansion and concentration risk.
* **Happened:** Exactly as expected.
* **Why routing occurred:** Because "semiconductor" and "manufacturing incentives" were meticulously pre-programmed in the dictionary to map to those exact tags.

**2. Defense indigenization**
* **Expected:** System flags sovereign survival capex.
* **Happened:** Exactly as expected.
* **Why routing occurred:** "Defense indigenization" was explicitly mapped to `defense_capex`.

**3. Nuclear incentives**
* **Expected:** System links "incentives" and "energy" to capex and power grids.
* **Happened:** Zero principles activated.
* **Why routing occurred:** "Nuclear" was not hardcoded in the dictionary. The router failed the exact-match lookup.

**4. Logistics corridors**
* **Expected:** System identifies infrastructure expansion.
* **Happened:** Zero principles activated.
* **Why routing occurred:** "Logistics corridors" was missing from the dictionary.

**5. Hospital expansion**
* **Expected:** System identifies healthcare and K-shaped wealth splits.
* **Happened:** Exactly as expected.
* **Why routing occurred:** "Hospital expansion" was explicitly typed into the dictionary mapping to `k_shaped_economy`.

**6. Data center growth**
* **Expected:** System links AI infrastructure to the power grid constraints.
* **Happened:** Success.
* **Why routing occurred:** Both "data center" and "power grid" were explicitly pre-programmed in the ontology.

**7. Power grid upgrades**
* **Expected:** System identifies the base-load bottleneck.
* **Happened:** Success.
* **Why routing occurred:** "Power grid" was in the dictionary.

**8. Water infrastructure**
* **Expected:** System identifies capex cycles.
* **Happened:** Zero principles activated.
* **Why routing occurred:** "Water infrastructure" was missing from the dictionary.

**9. Robotics adoption**
* **Expected:** System identifies margin expansion and automation.
* **Happened:** Success.
* **Why routing occurred:** "Robotics adoption" was explicitly mapped.

**10. Unknown industry**
* **Expected:** System fails gracefully.
* **Happened:** Zero principles activated.
* **Why routing occurred:** The dictionary did not contain "Dyson sphere".

**Takeaway:** Every "success" was merely a successful dictionary lookup of a pre-written answer. Every "failure" was a `KeyError`.

---

## TASK 3: The Smallest Minimal Change Toward Reasoning

**The Constraint:** Do NOT propose LLMs, agents, embeddings, or new architectures.

**The Smallest Minimal Change:** Implement **"Combinatorial Synthesis Rules" (CSR)**.

Currently, the Framework generation is a flat list. The system prints Principle A, then Principle B.
To move toward reasoning, `collide.py` must define logic for what happens when specific *combinations* of principles activate simultaneously.

**Example Change:**
Instead of just listing `SS-04: The Base-Load Bottleneck` and `MF-03: Monitor AI cycle monetization` independently, the code should include a combinatorial rule:
```python
if "SS-04" in active_ids and "MF-03" in active_ids:
    synthesis = "Because AI monetization requires immense power, AI capex will bottleneck at the grid level. Prioritize utility-scale power financing over direct GPU hardware."
```
*Why this moves toward reasoning:* It shifts the output from a decoupled list of generic rules into a specific, conditional insight derived from the intersection of two distinct domains.

---

## TASK 4: Top 10 Causes of Non-Generative Behavior

*Ranked by impact on destroying generative capability.*

1. **Context-Destructive Tagging:** Converting a full sentence into isolated, context-free tags (`["capex"]`) removes all information necessary to reason.
2. **Hardcoded Ontology Dictionary:** Exact substring matching means the system cannot infer synonyms, forcing human developers to anticipate every word in the English language.
3. **Template-Based Output:** Using an f-string to print pre-written `name` properties guarantees the system can never say anything novel.
4. **Boolean `ANY/ALL` Logic:** Forcing principles to activate on rigid true/false tag overlap prevents nuanced, probabilistic weighting of relevance.
5. **Lack of Inter-Principle Logic:** Principles do not "know" about each other during the output phase. They are printed as independent silos.
6. **Naive Conflict Resolution:** Suppressing a tactic merely because it shares a tag with a constraint (without mapping specific domains) leads to illogical deletions.
7. **No Negative Tag Logic:** The inability to parse "deactivation tags" means the system cannot handle negation in text (e.g., "Not a rate cut").
8. **Flat Output Generation:** Ignoring the `parent_id` hierarchy in the output code prevents the system from displaying structured logical trees (Parent theme → Child strategy → Tactic execution).
9. **No Second-Order Inference:** If A leads to B, and B leads to C, the system only outputs A. It cannot chain logic.
10. **Data Starvation:** The `macro_input.json` contains only `raw_text`. It lacks structured contextual variables (like current interest rates or PE ratios) that could fuel conditional reasoning.

---

## TASK 5: Can the current architecture eventually become a reasoning system?

**Answer:** NO.

**Justification:**
The current architecture is fundamentally built on **deterministic routing**. Its DNA is: `Input String -> Dictionary Match -> Array Filter -> F-string Print`.

No matter how many millions of words you add to the dictionary, and no matter how many principles you add to the catalog, it will only ever be a massive lookup table. A lookup table cannot reason. It cannot deduce that a new, unmapped event shares structural characteristics with a past event. It cannot combine two distinct concepts into a novel third concept. It is conceptually identical to a 1990s chatbot. To achieve reasoning, the deterministic tag-matching architecture must be thrown away and replaced with semantic/probabilistic architecture.

---

## FINAL VERDICT

**If you had to spend only one week improving the system, what exact improvement would you build first?**

**Improvement:** Implement the **Combinatorial Synthesis Matrix.**

**Why:** Because LLMs and embeddings are banned by the project constraints, we cannot fix the *input* layer (the hardcoded ontology dictionary). We are stuck with rigid tags. Therefore, the highest leverage point is the *output* layer.

By building a matrix that hardcodes the *intersections* of principles (e.g., When `SS-03` intersects with `RM-02`, output specific insight `Z`), the system will finally output cohesive, multi-variable strategies rather than disjointed lists. It simulates reasoning by creating deterministic rules for the *relationships* between concepts, moving the system from a "Knowledge Router" to an "Insight Compiler."
