# Roadmap Consistency Audit

## Objective
Verify whether the built systems support the Original Goal:
*Find emerging trends early → Convert trends into sectors → Convert sectors into stocks → Reject bad ideas → Produce watchlists.*

---

## Phase 0: Operating System
1. **Purpose:** Establish base rules, guardrails, directory structure, and non-negotiable constraints.
2. **What was actually built:** `operating_system/`, strict naming conventions, human-gated constraints, and foundational rule sets.
3. **Does it support the original goal?** **Weakly.** It protects the system from hallucination but focuses heavily on data immutability rather than forward-looking discovery.
4. **Assumptions:** Assuming extreme strictness on source ingestion leads to better alpha generation.
5. **What can be removed:** Nothing safely, but it must be refocused to serve outputs, not just inputs.

---

## Phase 1: Principle Extraction
1. **Purpose:** Reverse-engineer Akshat's mental models from YouTube transcripts.
2. **What was actually built:** Frequency tables, contradiction checkers, rule-based extraction architectures, and promotion logic.
3. **Does it support the original goal?** **Indirectly.** It built an encyclopedia. Knowing "Akshat likes margins" does not find a new trend; it only provides the filter for when a trend is found.
4. **Assumptions:** Assuming past principles perfectly map to future unknown trends.
5. **What can be removed:** The manual human promotion PR step (`08_Akshat_Update_Protocol.md`) is a massive bottleneck that slows down real-time trend detection.

---

## Phase 1.5: Emerging Frameworks
1. **Purpose:** Detect new mental models before they hit the 8-source Doctrine threshold.
2. **What was actually built:** Architectural claims, velocity/novelty scoring logic (theoretical).
3. **Does it support the original goal?** **Yes.** This is the closest step to "Find emerging trends early."
4. **Assumptions:** Assuming an LLM can score novelty accurately against a massive historical graph without hallucinating.
5. **What can be removed:** The complex velocity formula. A simple "Never seen before in corpus" boolean check is faster and less brittle.

---

## Phase 1.75: Macro-to-Principle Collision
1. **Purpose:** Actively combine hard macro news with core principles to generate actionable strategies.
2. **What was actually built:** The design logic for combining domains (Macro Event + Principle = Strategy).
3. **Does it support the original goal?** **Yes.** It is the bridge between the outside world and the internal encyclopedia.
4. **Assumptions:** Assuming macro events are discrete, legible data points rather than continuous, messy narratives.
5. **What can be removed:** Nothing. This is the core reasoning loop.

---

## Phase 2: MVP
1. **Purpose:** Prove the Macro-to-Principle Collision loop without LLMs or databases.
2. **What was actually built:** A keyword-based matching script (`collide.py`) and static JSON files.
3. **Does it support the original goal?** **No.** It completely abandoned the goal. It finds nothing. It maps hardcoded strings to hardcoded strings.
4. **Assumptions:** Assuming that proving the data *pipes* work is the same as proving the *reasoning* works.
5. **What can be removed:** `ontology_map.json`. It is a dead-end attempt at building an English-to-Concept dictionary.

---

## Phase 2.5: Blueprint
1. **Purpose:** Provide exact instructions for a developer to build Phase 2.
2. **What was actually built:** A detailed schema and execution plan for the keyword matching engine.
3. **Does it support the original goal?** **No.** It perfectly documented a flawed system.
4. **Assumptions:** Assuming the architectural constraints ("No LLMs") would yield a useful MVP.
5. **What can be removed:** The constraint against using embeddings.

---

## Phase 2.75: Readiness Review
1. **Purpose:** Adversarially attack the blueprint before coding.
2. **What was actually built:** Red team audits, edge cases, Go/No-Go reports.
3. **Does it support the original goal?** **Yes.** It successfully identified that the system was broken before massive engineering hours were wasted.
4. **Assumptions:** Assuming the developer would read the "NO" and stop, rather than forcing the implementation.
5. **What can be removed:** Irrelevant edge cases (e.g., "Python 2.7" tests). Focus testing entirely on reasoning failure modes.
