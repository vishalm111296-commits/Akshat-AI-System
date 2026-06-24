# One-Week Improvement Plan: MVP Optimization

*Mission: Squeeze maximum generative reasoning out of the current hardcoded MVP without introducing any new architecture, LLMs, or vector databases. All improvements are restricted to Python logic and JSON schema modifications within the existing 4 files.*

---

## Part 1: Ranked Improvement List (By ROI)

### 1. Contextual Weighting Matrix (The Gradient Resolution)
*   **Description:** Update `ontology_map.json` and `core_catalog.json` to replace binary strings with float values. Instead of `"semiconductor": ["capex"]`, use `"semiconductor": {"capex": 0.9, "geopolitics": 0.8}`. Update `2_collide.py` to multiply the Input Vector by the Principle Polarity Vector (`+1.0` or `-1.0`) to generate a net score, rather than simply counting the number of activated principles.
*   **Expected Impact:** Destroys the "Over-Constrained Null Output" failure mode. A massive macroeconomic tailwind (score 0.9) will mathematically override a minor tactical constraint (score -0.2), simulating actual conflict resolution.
*   **Complexity:** Low (purely Python float math and JSON restructuring).
*   **Risk:** Low.

### 2. Dynamic Framework Title Generation
*   **Description:** Remove the hardcoded `if/elif` string concatenation (`"Convergence of..."`) from `synthesize_framework()`. Instead, write a function that selects a prefix (e.g., "State-Sponsored", "Structural", "Cyclical") based on the highest-scoring `[PARENT]` principle, and a suffix based on the highest-scoring `[CHILD]` principle.
*   **Expected Impact:** The output framework title will no longer look like a clumsy concatenated list. It will appear synthesized (e.g., "State-Sponsored Manufacturing Catch-Up" instead of "Convergence of Follow Subsidies and Avoid Traps").
*   **Complexity:** Medium (requires implementing the parent/child hierarchy logic inside the script).
*   **Risk:** Low.

### 3. Wildcard / Root-Node Routing (The "Water" Fix)
*   **Description:** Currently, if an exact noun (like "water") isn't in the ontology, the system crashes or defaults to generic "infrastructure". Add a generic root-node mapping in `ontology_map.json` (e.g., `"__unknown_infrastructure__": ["capex", "necessity"]`). Update the script to fall back to root-node mappings if an exact match fails but a broad category tag is detected.
*   **Expected Impact:** Provides graceful degradation for unknown industries. Test 8 (Water) and Test 9 (Robotics) will no longer fail purely because they weren't explicitly hardcoded.
*   **Complexity:** Medium.
*   **Risk:** Medium (Risk of false positives if the fallback node is too generic).

### 4. Re-activate the Evidence/Conviction Multiplier
*   **Description:** The MVP schema currently stores `"evidence_count": 5`, but the script ignores it. Update the collision math to use `evidence_count` as a multiplier. A principle Akshat stated 50 times should carry 10x the mathematical weight of a principle stated 5 times during a collision.
*   **Expected Impact:** Re-aligns the MVP with the original goal of discovering *how Akshat thinks*. Strong historical biases will correctly dominate weak tactical observations.
*   **Complexity:** Low.
*   **Risk:** Low.

### 5. Contradiction Veto (The "Fatal Flaw" Logic)
*   **Description:** Introduce an explicit `veto_tags` array into the `core_catalog.json`. If a macro event contains a specific veto tag (e.g., `"fraud"`, `"hyper-valuation"`), `2_collide.py` immediately halts the synthesis and returns a "Fatal Flaw" framework, regardless of how many tailwinds exist.
*   **Expected Impact:** Introduces a strict risk-management layer. Prevents the system from outputting a "Buy" framework just because a stock has 5 tailwinds but is trading at 500x P/E.
*   **Complexity:** Low.
*   **Risk:** Low.

---

## Part 2: Recommended Implementation Order

*A strict 5-day coding sprint.*

1.  **Monday:** Implement Improvement 1 (Contextual Weighting). Rewrite the JSON schemas to use floats and update the core loop in `2_collide.py` to calculate the "Net Synthesis Vector."
2.  **Tuesday:** Implement Improvement 4 (Evidence Multiplier). Add the historical frequency back into the math equation built on Monday.
3.  **Wednesday:** Implement Improvement 5 (Contradiction Veto). Add the hard-block logic to the start of the collision function to ensure risk management overrides math.
4.  **Thursday:** Implement Improvement 2 (Dynamic Titles). Re-write the string output function to use the new mathematically ranked principles to build grammatically correct titles.
5.  **Friday:** Implement Improvement 3 (Wildcard Routing). Update the ontology dictionary and write the fallback loops to handle unknown inputs.

---

## Part 3: Expected Change in Behavior

**Before the One-Week Sprint:**
The system acts as a rigid, brittle text router. It requires exact keyword matches, treats all principles as equal, blindly concatenates strings, and fails spectacularly when handed a noun it hasn't seen before.

**After the One-Week Sprint:**
The system will act as a **Weighted Logic Engine**. It will still not use AI, but it will simulate intelligence by mathematically prioritizing structural macro forces over minor tactical constraints. It will generate human-readable framework titles dynamically. It will degrade gracefully when handed unknown inputs by relying on category root-nodes, and it will enforce strict risk management through the veto system.

---

## Part 4: What Will Still Remain Unsolved

*Be brutally realistic.*

1.  **The Ontology Bottleneck:** The system still requires a human to manually update `ontology_map.json`. It will never "discover" a completely novel paradigm (like Web3 in 2016) because it lacks semantic zero-shot understanding.
2.  **No Financial Reality:** The system will still just output a Markdown file. Without the Opportunity Scanner, it cannot verify if the "Framework" actually exists in the stock market.
3.  **The Sarcasm/Context Trap:** Because there is no NLP layer, if an input says "The government *cancels* semiconductor subsidies," the system will see the tags `["government", "subsidy", "semiconductor"]` and blindly trigger the *Positive* subsidy tailwind, completely misunderstanding the negation.

**Conclusion:** The one-week sprint maximizes the potential of a purely deterministic system, moving it from a "router" to an "expert system calculator." However, it hits the absolute hard ceiling of non-NLP architecture.