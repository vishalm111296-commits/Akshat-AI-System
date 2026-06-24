# Implementation Blockers

## Overview
This document catalogs every ambiguity, contradiction, and missing definition that prevents immediate implementation of the Phase 2 MVP.

---

## 1. Data Blockers
- **Blocker ID:** D-01
- **Description:** Missing actual MVP JSON data files.
- **Why it blocks:** The MVP Build Blueprint specifies `core_catalog.json` and `ontology_map.json`, but these files do not exist in the repository; only markdown precursors exist. A developer cannot run `collide.py` without sample data.
- **Severity:** CRITICAL
- **Recommended resolution:** A human or data-prep step must translate `02_Akshat_Principle_Frequency_Table.md` into the exact JSON format required by `core_catalog.json`.

---

## 2. Schema Blockers
- **Blocker ID:** S-01
- **Description:** No defined taxonomy relationship field in JSON.
- **Why it blocks:** The Taxonomy Review defined Parent, Child, Tactic, and Constraint, but did not define how `core_catalog.json` maps these. If a Constraint overrides a Tactic, how does the engine know *which* Tactic it overrides?
- **Severity:** CRITICAL
- **Recommended resolution:** Add a `parent_id` and `overrides` field to the principle JSON schema.

- **Blocker ID:** S-02
- **Description:** `activation_tags` matching rules are undefined.
- **Why it blocks:** Does an event need to match *all* tags or *any* tag in a Principle's `activation_tags` array? This changes the entire collision output.
- **Severity:** HIGH
- **Recommended resolution:** Define exact boolean logic for tag matching (e.g., OR vs AND).

---

## 3. Ontology Blockers
- **Blocker ID:** O-01
- **Description:** Unknown baseline ontology dictionary.
- **Why it blocks:** `ontology_map.json` maps hard words to abstract tags. But what is the universe of abstract tags? If it is unbounded, `activation_tags` will never match the ontology output.
- **Severity:** CRITICAL
- **Recommended resolution:** Hardcode a strict enum list of allowed `activation_tags` (e.g., `["liquidity_up", "margin_expansion", "geopolitics_risk"]`).

---

## 4. Principles Blockers
- **Blocker ID:** P-01
- **Description:** Conflicting principles logic.
- **Why it blocks:** If event X triggers "Buy near 200DMA" (Tactic) and "Never catch a falling knife" (Constraint) without explicit hierarchy mapping, the engine cannot resolve the conflict natively.
- **Severity:** HIGH
- **Recommended resolution:** Hardcode resolution rule: Constraints always return `False` for execution, suppressing all child Tactics.

---

## 5. Collision Engine Blockers
- **Blocker ID:** C-01
- **Description:** Missing definition of "Conflict Resolution" algorithm.
- **Why it blocks:** The Blueprint says `resolve_conflicts(active_principles)`. But what is the exact pseudo-code? Does it drop the tactic, output a warning, or abort the run?
- **Severity:** HIGH
- **Recommended resolution:** Define standard behavior: Output the tactic but strike it through, appending the Constraint text as a blocker.

---

## 6. Testing Blockers
- **Blocker ID:** T-01
- **Description:** Lack of explicit pass/fail asserts in test inputs.
- **Why it blocks:** `tests/mvp/macro_input.json` contains test data, but no expected output schema for PyTest to assert against.
- **Severity:** MEDIUM
- **Recommended resolution:** Add `expected_principles` array to the test input JSON for automated assertion.

---

## 7. Outputs Blockers
- **Blocker ID:** OUT-01
- **Description:** Generation string templating is undefined.
- **Why it blocks:** How does `collide.py` turn an array of JSON objects into the "Barbell Formatting" text? Without an LLM (excluded in MVP), it requires explicit string templates.
- **Severity:** HIGH
- **Recommended resolution:** Provide a rigid f-string or Jinja2 markdown template in `collide.py`.

---

## 8. User Workflow Blockers
- **Blocker ID:** UW-01
- **Description:** Unknown trigger mechanism.
- **Why it blocks:** How does a user feed a new macro event into `macro_input.json`? Manual edit? CLI flag?
- **Severity:** LOW
- **Recommended resolution:** Make `collide.py` accept a CLI argument `--event-file` that defaults to `tests/mvp/macro_input.json`.
