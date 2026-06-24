# Root Cause Analysis: Routing vs. Reasoning

*Mission: Perform a Root Cause Analysis on why the MVP operates as a deterministic router rather than a generative reasoning system, without proposing new architectures or LLM integrations.*

---

## TASK 1: Where Reasoning Disappears

*Tracing the data flow to identify the exact point of intellectual failure.*

1.  **Macro Input (`trigger_tags`):** The user provides an event. *Reasoning exists here*, as the human intelligently extracted the relevant nouns (e.g., "semiconductor", "incentive") from the messy real-world headline.
2.  **Ontology Translation:** The script looks up "semiconductor" in `ontology_map.json` and outputs `["capex", "geopolitics", "supply_chain"]`. **Reasoning disappears here.** The system does not understand *why* a semiconductor requires capex. It merely executes a 1:1 dictionary lookup.
3.  **Principle Activation:** The script uses Python's `set().intersection()` to see if `["capex"]` is in `PRIN-002`'s list of `activation_tags`. It is a binary True/False mathematical operation. No contextual reasoning occurs.
4.  **Framework Generation:** The script counts `positive = 2`, `negative = 1`. It executes an `if pos > 0 and neg > 0` condition, returning a hardcoded title and concatenating the pre-written `description` fields from the JSON. It generates no new text, synthesizes no new logic, and provides no specific application of the principle to the macro event.

**Conclusion:** Reasoning disappears the moment the human input hits the `ontology_map.json`. From that exact line of code onward, the system is executing rigid, binary Boolean logic.

---

## TASK 2: Macro Test Analysis

For each test, the system behaved as a router because it lacked situational context.

*   **Test 1 (Semiconductor incentives):** Expected synthesis. Happened: Triggered expected principles. Reason: Manual mapping in ontology was reverse-engineered for this exact test.
*   **Test 2 (Defense indigenization):** Expected synthesis. Happened: Triggered PSUs and Monopsony. Reason: Ontology explicitly mapped "defense" to "psu", blindly forcing the collision.
*   **Test 3 (Nuclear incentives):** Expected execution constraint + subsidy. Happened: Exactly that. Reason: Ontology mapped "nuclear" to "capex", triggering the exact same generic constraint as semiconductors.
*   **Test 4 (Logistics corridors):** Expected infrastructure tailwinds. Happened: Only triggered execution constraints. Reason: "Logistics" was mapped to "capex", but the core catalog lacked an "Infrastructure Tailwind" principle, making it impossible to route to a positive outcome.
*   **Test 5 (Hospital expansion):** Expected necessity vs capex. Happened: Exactly that. Reason: Hardcoded dictionary mapping.
*   **Test 6 (Data center growth):** Expected AI/digital infrastructure tailwind. Happened: Only triggered "Terminal Value Trap" (capex). Reason: The catalog lacked digital principles, so it defaulted to the generic physical manufacturing constraint.
*   **Test 7 (Power grid upgrades):** Expected necessity vs ESG. Happened: Triggered ESG and Demographic necessity. Reason: Hardcoded mapping in ontology.
*   **Test 8 (Water infrastructure):** Expected necessity. Happened: Terminal Value Trap. Reason: "Water" was not in the ontology, so it routed purely on the word "infrastructure" (which triggers the negative capex rule).
*   **Test 9 (Robotics adoption):** Expected efficiency/automation tailwind. Happened: Terminal Value Trap. Reason: Robotics mapped to "manufacturing" in the ontology, triggering the negative execution trap rule without understanding automation reduces long-term opex.
*   **Test 10 (Unknown industry):** Expected graceful degradation. Happened: Null output. Reason: String not found in dictionary.

---

## TASK 3: The Smallest Possible Change Toward Reasoning (No LLMs)

**The Change:** Introduce Contextual Tag Weighting.

Currently, the system treats all tags as equal binary triggers (1 or 0).
Instead of mapping `semiconductor -> ["capex"]`, change the schema to:
`semiconductor -> {"capex": 0.9, "geopolitics": 0.8, "demographics": 0.0}`
`hospital -> {"capex": 0.6, "demographics": 0.9, "geopolitics": 0.1}`

**Why it moves toward reasoning:**
By replacing Boolean sets with continuous weights, the collision engine can perform *Gradient Resolution*. If a macro event is 90% driven by demographics and only 60% driven by capex, the engine can mathematically prioritize the Demographic Tailwind over the Capex Constraint, synthesizing a dominant theme rather than relying on a flat `if pos > 0 and neg > 0` integer tally.

---

## TASK 4: Top 10 Causes of Non-Generative Behavior
*(Ranked by impact on system intelligence)*

1.  **Boolean Collision Logic:** Treating all activated principles as equal (1 vote each) forces the engine to rely on simplistic integer counting rather than nuanced conflict resolution.
2.  **Static Dictionary Ontology:** The 1:1 mapping forces the system to be blind to any word a human developer hasn't explicitly hardcoded.
3.  **String Concatenation for "Reasoning":** Merely appending pre-written strings together prevents the system from contextualizing the principle to the specific macro event.
4.  **Lack of Semantic Context:** The system ignores the *relationship* between words in the macro event. "Government taxes semiconductors" and "Government subsidizes semiconductors" will trigger identical principles if the user just inputs `["government", "semiconductor"]`.
5.  **No Magnitude Scoring:** The macro input lacks a severity score. A $1B subsidy triggers the exact same logic as a $100B subsidy.
6.  **Missing "Domain" Tagging:** Applying the "Avoid Capital Execution Traps" principle (designed for Indian heavy manufacturing) blindly to US tech infrastructure because both map to "capex."
7.  **No Extrapolation Engine:** The system cannot infer secondary effects (e.g., Data Centers require Power).
8.  **Flat Principle Hierarchy:** The MVP ignored the Parent/Child taxonomy designed in Phase 2, treating massive structural forces and minor tactical constraints as equal peers.
9.  **Hardcoded Framework Strings:** The `2_collide.py` script literally contains the string `"State-Sponsored Catch-Up Narrative"`.
10. **Ignored `evidence_count`:** The system abandons historical conviction weighting, treating a principle mentioned once exactly the same as a principle mentioned 500 times.

---

## TASK 5: Can the current architecture eventually become a reasoning system?

**NO.**

**Defend your answer:**
The current architecture (Macro Event → Ontology Map → Principle Catalog → Integer Math Collision) is fundamentally a **classification tree**. No matter how many thousands of principles you add to the catalog, and no matter how many tens of thousands of words you add to the `ontology_map.json`, it will only ever be a massive `switch/case` statement.

Reasoning requires *synthesis* (creating a new thought from the collision of two existing thoughts) and *contextual awareness* (understanding that "capex" means something different for Nvidia than it does for Tata Steel). A classification tree can only retrieve pre-written data; it cannot synthesize novel data. To become a reasoning system, the architectural foundation of `2_collide.py` must be rewritten.

---

## FINAL VERDICT

**If you had to spend only one week improving the system: What exact improvement would you build first? Why?**

**Build: The Semantic Multiplier Matrix (Contextual Weighting).**

*Why:* I cannot add LLMs or new architectural engines. Therefore, the highest leverage action to escape the "Boolean Trap" is to upgrade the mathematical sophistication of `2_collide.py`.

By converting the binary `activation_tags` into a weighted matrix, and converting the `core_catalog.json` polarities into continuous scores (e.g., `-1.0` to `+1.0`), the system can calculate a "Net Synthesis Vector."

If `(Demographic Tailwind * 0.9) + (Capex Constraint * -0.4) > 0`, the system explicitly reasons that the tailwind absorbs the constraint. This introduces rudimentary mathematical reasoning (Magnitude and Priority) into the collision engine, breaking the reliance on simplistic integer counting without violating the "no new architecture" constraint.