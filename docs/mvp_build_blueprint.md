# MVP Build Blueprint

## Overview
This document is the final implementation blueprint for the Phase 2 MVP of the Akshat Reasoning System. It focuses exclusively on the generative reasoning loop (Macro Event -> Principle Activation -> Framework Generation). All complex NLP, continuous learning, databases, and extraction features are explicitly excluded.

This blueprint must be strictly followed. Do not add files, libraries, or external services outside this scope.

---

## File 1: Core Principles Catalog

- **Filename:** `knowledge/principles/core_catalog.json`
- **Responsibility:** Serves as the static database of all "Doctrine" and "Tactical" principles extracted from the human knowledge base. It is the core truth layer for the collision engine.
- **Input:** Human-curated static JSON data.
- **Output:** Parsable JSON array used by the Collision Engine.
- **Functions:** N/A (Static Data File)
- **Dependencies:** None.
- **Structure Requirements:** Must follow the Parent-Child-Tactic-Constraint taxonomy. Each object must have fields for `id`, `name`, `type` (Parent/Child/Tactic/Constraint), `domain`, and `activation_tags` (keywords that trigger it).
- **Estimated line count:** 200 - 300 lines (Data only)

---

## File 2: Semantic Abstraction Map

- **Filename:** `scripts/mvp/ontology_map.json`
- **Responsibility:** Maps hard, real-world macro events (e.g., "Interest rate cut by 50bps") to abstract thematic tags (e.g., `["liquidity_expansion", "risk_on"]`) that match the `activation_tags` in the core catalog.
- **Input:** Human-curated static JSON data.
- **Output:** Parsable JSON object.
- **Functions:** N/A (Static Data File)
- **Dependencies:** None.
- **Structure Requirements:** A key-value map where the key is a specific macro condition or term and the value is a list of standardized activation tags used in `core_catalog.json`.
- **Estimated line count:** 100 - 150 lines (Data only)

---

## File 3: Test Event Input

- **Filename:** `tests/mvp/macro_input.json`
- **Responsibility:** Simulates an incoming macro event (e.g., geopolitical crisis, central bank action, demographic shift) to trigger the system.
- **Input:** Human-written test scenario data.
- **Output:** Parsable JSON object representing the event state.
- **Functions:** N/A (Static Data File)
- **Dependencies:** None.
- **Structure Requirements:** Must contain fields for `event_name`, `date`, `description`, `hard_data` (e.g., metrics or rates changed), and `inferred_tags` (if pre-mapped).
- **Estimated line count:** 20 - 50 lines (Data only)

---

## File 4: The Collision Engine

- **Filename:** `scripts/mvp/collide.py`
- **Responsibility:** The core logic executable. It reads the test macro event, maps it to tags via the ontology map, queries the core catalog for matching principles, resolves conflicts (e.g., ensuring a Constraint overrides a Tactic), and generates the final reasoning output.
- **Input:** Reads `tests/mvp/macro_input.json`, `scripts/mvp/ontology_map.json`, and `knowledge/principles/core_catalog.json`.
- **Output:** Writes text/markdown to `docs/mvp_output/generated_frameworks/reasoning_report.md`.
- **Functions:**
  1. `load_data()`: Loads the three JSON inputs.
  2. `map_event_to_tags(event, ontology)`: Extracts relevant tags based on the macro input.
  3. `fetch_active_principles(tags, catalog)`: Returns all principles whose `activation_tags` match the event tags.
  4. `resolve_conflicts(active_principles)`: Filters out Tactics that are explicitly blocked by activated Constraints.
  5. `generate_report(event, final_principles)`: Formats the collision result into the standard markdown framework.
  6. `main()`: Orchestrates the flow and handles file I/O.
- **Dependencies:** Built-in Python libraries only (`json`, `os`, `sys`, `argparse`). No external LLM APIs are used in this barebones script logic.
- **Estimated line count:** 150 - 250 lines

---

## File 5: Generated Reasoning Report

- **Filename:** `docs/mvp_output/generated_frameworks/reasoning_report.md`
- **Responsibility:** The final, human-readable output of the generative reasoning loop.
- **Input:** Text strings passed from `collide.py`.
- **Output:** Markdown file on disk.
- **Functions:** N/A (Generated Output File)
- **Dependencies:** `scripts/mvp/collide.py` (which creates it).
- **Structure Requirements:** Must follow the standardized "Barbell Output Format":
  - 1. Summary of Macro Event
  - 2. Activated Constraints (Hard Boundaries)
  - 3. Activated Tactics (Offensive Actions)
  - 4. Final Proposed Framework (What to do, e.g., "Shift 5% to Gold, Hold US Tech")
- **Estimated line count:** Variable (Generated), typically 30 - 70 lines.
