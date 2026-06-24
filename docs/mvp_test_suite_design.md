# MVP Test Suite Design

## Overview
This document defines the comprehensive test suite for `collide.py`, validating the generative reasoning loop across Happy paths, Negative paths, Stress tests, Ambiguity tests, and Contradiction tests.

---

## 1. Happy Path Tests

**Test ID:** HP-01: Perfect Match
- **Input:** `raw_text`: "Fed cuts rates." (Ontology maps to `liquidity_up`). Catalog has Principle CP-01 requiring `liquidity_up`.
- **Expected output:** Reasoning report generated containing CP-01.
- **Pass criteria:** `CP-01` is strictly present in `expected_principles` output array and written to disk.

**Test ID:** HP-02: Multi-Tag Match
- **Input:** `raw_text`: "Govt subsidizes semiconductor capex." Maps to `["capex", "tech"]`.
- **Expected output:** Multiple principles mapped to both tags activate correctly.
- **Pass criteria:** Output report groups both Tactics under correct Parent domains.

---

## 2. Negative Tests

**Test ID:** NEG-01: Empty Text
- **Input:** `raw_text`: ""
- **Expected output:** Script catches empty input, generates "No actionable principles" report.
- **Pass criteria:** No Python runtime crashes (`KeyError`, `IndexError`); clean exit code 0.

**Test ID:** NEG-02: Garbage Text
- **Input:** `raw_text`: "asdflkjasd fasdf qwe"
- **Expected output:** Ontology returns empty tag array.
- **Pass criteria:** No principles activated; output gracefully handles zero tags.

---

## 3. Stress Tests

**Test ID:** STR-01: Maximum Tag Overload
- **Input:** `raw_text` containing every single keyword in the `ontology_map.json` dictionary.
- **Expected output:** Engine extracts all tags, deduplicates them, and processes all principles.
- **Pass criteria:** Execution completes in <2.0 seconds.

**Test ID:** STR-02: Missing Schema References
- **Input:** Pass `core_catalog.json` with 500 principles missing the `parent_id` field.
- **Expected output:** JSON validator catches schema failure *before* engine starts.
- **Pass criteria:** Fails with explicit `ValidationError`, not a downstream `KeyError`.

---

## 4. Ambiguity Tests

**Test ID:** AMB-01: ANY vs ALL Boolean Logic
- **Input:** Principle requires `ALL: ["A", "B"]`. Input triggers only `["A"]`.
- **Expected output:** Principle does NOT activate.
- **Pass criteria:** Strict adherence to boolean logic operators; false positives suppressed.

**Test ID:** AMB-02: Substring Edge Matching
- **Input:** Ontology key is "rate cut". Text is "corporate rate cut".
- **Expected output:** Substring matches and fires tag.
- **Pass criteria:** Engine successfully extracts the tag without demanding exact full-string isolation.

---

## 5. Contradiction Tests

**Test ID:** CON-01: Constraint Suppresses Tactic
- **Input:** Text triggers Tactic "Buy Naked Calls" and Constraint "Never Sell Naked Options".
- **Expected output:** Engine loads both, conflict resolver strikes Tactic, leaves Constraint.
- **Pass criteria:** Final report does NOT recommend the Tactic.

**Test ID:** CON-02: Unrelated Constraint
- **Input:** Text triggers Tactic "Buy Tech" and Constraint "Limit Real Estate".
- **Expected output:** Engine loads both; they do not suppress each other.
- **Pass criteria:** Both appear in the final report in their respective sections.
