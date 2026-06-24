# Project Red Team Audit
*Auditor: Hostile CTO Review. Objective: Project Kill/Harden.*

This audit reviews the frozen generative reasoning architecture (Principle Extraction, Emerging Frameworks, Macro Collision, MVP Spec).

## 1. Hidden Assumptions
*   **Problem:** The architecture assumes macro events (e.g., "Government launches subsidies") arrive as clean, discrete JSON packets with obvious trigger tags.
*   **Why it matters:** The real world does not emit JSON. Macro events are noisy, conflicting, and spread across weeks of news cycles.
*   **Probability:** High | **Severity:** Critical
*   **Mitigation:** The system needs an external, robust Data Engineering pipeline before the MVP routing logic can be applied to reality.

## 2. Failure Modes
*   **Problem:** The "Over-Constrained Null Output" in the Collision Engine.
*   **Why it matters:** If an event triggers 3 tailwinds and 3 constraints, the math may cancel out to exactly 0, causing the system to output nothing during massive market shifts.
*   **Probability:** Medium | **Severity:** High
*   **Mitigation:** Introduce "Tie-Breaker Priorities" where fundamental constraints (e.g., Extreme Valuation) automatically override any number of structural tailwinds.

## 3. Scalability Problems
*   **Problem:** O(N^2) Semantic Matching in the Principle Catalog.
*   **Why it matters:** The MVP relies on hardcoded `ontology_map.json`, but the production system intends to use semantic distance. Running live pairwise distance checks for every new macro input against a growing principle catalog will throttle the system.
*   **Probability:** High | **Severity:** High
*   **Mitigation:** Move from in-memory matching to a lightweight localized vector index (like FAISS) *after* the MVP phase.

## 4. Data Quality Risks
*   **Problem:** Source Contamination in `raw_sources`.
*   **Why it matters:** The extraction engine assumes Tier 1 and Tier 2 sources are purely Akshat's objective reasoning. If he quotes a guest, reads a headline, or uses heavy sarcasm, the extraction engine will ingest bad data.
*   **Probability:** High | **Severity:** Critical
*   **Mitigation:** The NLP extraction pipeline must feature explicit "Sarcasm/Quote Masking" before saving to the `core_catalog.json`.

## 5. Principle Extraction Risks
*   **Problem:** The "Platitude vs. Framework" dilemma.
*   **Why it matters:** Abstracting concepts too far (e.g., "Government + Semiconductors" -> "Strategic Manufacturing") risks creating generic principles like "Buy good companies," rendering the engine useless for alpha generation.
*   **Probability:** High | **Severity:** Medium
*   **Mitigation:** Strict enforcement of the "Polarity" and "Constraint" schema fields. A principle must explicitly dictate an action or a block.

## 6. Framework Generation Risks
*   **Problem:** The "Frankenstein Framework."
*   **Why it matters:** Combining disjointed principles (e.g., "Demographic Shift" + "Short-Term Yield Curve Inversion") might generate a syntactically valid but economically nonsensical framework.
*   **Probability:** Medium | **Severity:** High
*   **Mitigation:** The Ontology Map must restrict collisions to cross-compatible ontological domains (e.g., Macro-to-Macro, Micro-to-Micro).

## 7. False Positive Risks
*   **Problem:** The Velocity Scoring Trap in the Emerging Framework Engine.
*   **Why it matters:** A 30-day spike in news regarding a "Green Energy" summit will trigger high Velocity and Novelty, promoting it to a Candidate Framework, causing the system to chase a narrative with zero fundamental backing.
*   **Probability:** High | **Severity:** Critical
*   **Mitigation:** The Opportunity Scanner feedback loop must enforce a hard block if trailing ROCE across the sector does not align with the narrative.

## 8. False Negative Risks
*   **Problem:** The Backward-Looking Anchor on Core Principles.
*   **Why it matters:** If a trend (like AI Infrastructure) requires a "Picks and Shovels" principle, but the system has never extracted that principle before, the Macro Collision Engine will silently ignore the event.
*   **Probability:** High | **Severity:** Critical
*   **Mitigation:** The engine must flag "Orphaned Macro Events" (high-impact events that triggered 0 principles) for human review to generate new principles.

## 9. Overfitting Risks
*   **Problem:** Over-indexing on the Indian Macro Environment.
*   **Why it matters:** The historical corpus is heavily Indian-centric. The ontology map might incorrectly apply Indian constraints (like high capital cost) to US tech inputs, causing the engine to reject valid global frameworks.
*   **Probability:** High | **Severity:** Medium
*   **Mitigation:** Principles must be tagged with explicit `Geographic_Scope` metadata to prevent cross-contamination.

## 10. User Workflow Risks
*   **Problem:** The system is a "Black Box" oracle.
*   **Why it matters:** If the user cannot easily trace *why* the Collision Engine prioritized Geopolitics over Valuation, they will not trust the output and will abandon the tool.
*   **Probability:** Medium | **Severity:** High
*   **Mitigation:** The final Output Report must include an "Audit Trail" linking the synthesized framework back to the specific `core_catalog.json` IDs and the raw macro input tags.