# Roadmap Consistency Audit

*Objective: Verify whether the frozen architecture still supports the original goal: Find emerging trends early → Convert trends into sectors → Convert sectors into stocks → Reject bad ideas → Produce watchlists.*

---

## Phase 0: Operating System
1. **Purpose:** Establish base logic, invariants, and source data handling.
2. **What was actually built:** Rules for human-gated masters, file hierarchy (`L0-L7`), and immutable source definitions.
3. **Does it support the original goal?:** Yes, foundational truth is required to reject bad ideas.
4. **Assumptions:** Assumes the initial corpus is clean and inherently predictive.
5. **What can be removed:** Nothing at this layer; it is purely structural.

## Phase 1: Principle Extraction
1. **Purpose:** Extract recurring mental models to understand *how* Akshat thinks.
2. **What was actually built:** A Hybrid Pipeline (Concept Extraction → Theme Detection → Principle Candidate) and a JSON/Markdown catalog schema.
3. **Does it support the original goal?:** Partially. It extracts constraints to "reject bad ideas," but by requiring multi-year persistence, it explicitly fails to "find emerging trends early."
4. **Assumptions:** Assumes frequency = accuracy.
5. **What can be removed:** Absolute frequency scoring; it biases toward history over opportunity.

## Phase 1.5: Emerging Frameworks
1. **Purpose:** Catch new mental models before they have multi-year track records.
2. **What was actually built:** Velocity and Novelty scoring schemas, and a Candidate → Emerging → Core promotion lifecycle.
3. **Does it support the original goal?:** Yes. It bridges the gap to "find emerging trends early."
4. **Assumptions:** Assumes Akshat speaks about trends *before* they become consensus.
5. **What can be removed:** "News Cycle False Positive" rules that block frameworks too aggressively before they reach the Sector Discovery phase.

## Phase 1.75: Macro-to-Principle Collision
1. **Purpose:** Move from reactive parsing to proactive, generative reasoning.
2. **What was actually built:** A collision engine taking hard macro data, triggering principles, and synthesizing frameworks.
3. **Does it support the original goal?:** Yes. This is the exact engine required to "find emerging trends early" independently.
4. **Assumptions:** Assumes external macro data can be neatly mapped to abstract tags.
5. **What can be removed:** Manual JSON creation for Macro Inputs.

## Phase 2: MVP
1. **Purpose:** Build the smallest possible working reasoning loop to prove the architecture.
2. **What was actually built:** A stripped-down, two-script, rule-based tag router (`1_extract.py`, `2_collide.py`).
3. **Does it support the original goal?:** Barely. It proves the *plumbing* works, but halts at Framework Generation. It does not convert frameworks to sectors, nor sectors to stocks, and it produces no watchlists.
4. **Assumptions:** Assumes an MVP that outputs a text report proves the viability of a downstream quantitative stock screener.
5. **What can be removed:** The manual `ontology_map.json`, as it fakes the reasoning.

## Phase 2.5 & 2.75: Blueprint and Readiness Review
1. **Purpose:** Provide exact implementation instructions for developers and resolve ambiguities.
2. **What was actually built:** JSON schemas, walkthroughs, edge case matrices, and hardcoded `if/else` logic specs.
3. **Does it support the original goal?:** No. These phases optimized for *developer safety* and *system stability*, effectively nerfing the system into a static text generator rather than a dynamic discovery engine.
4. **Assumptions:** Assumes a deterministic codebase is better than a messy, generative one.
5. **What can be removed:** The hardcoded framework output strings.