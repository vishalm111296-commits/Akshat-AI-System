# Edge Case Library

*This document defines the expected behavior for Edge Cases impacting the MVP Engine.*

### Category 1: Ontology Edge Cases
*   **EC-001:** Input tag is not in Ontology Map and not in Principle Catalog.
    *   *Input:* `["quantum_computing"]`
    *   *Expected Behavior:* Script gracefully completes but outputs "No Activated Principles. No Framework Generated."
    *   *Failure Risk:* Script crashes trying to parse empty lists.
*   **EC-002:** Input tag maps to an ontology key, but the resulting abstract tags do not match any principles.
    *   *Input:* `["crypto"]` -> maps to `["decentralized", "blockchain"]` (neither exist in catalog).
    *   *Expected Behavior:* Graceful null output.
*   **EC-003:** Circular Mapping in Ontology.
    *   *Input:* `"capex"` -> maps to `"manufacturing"`, `"manufacturing"` maps to `"capex"`.
    *   *Expected Behavior:* MVP script `abstract_tags()` must not recursively loop; it should only do a single-pass dictionary lookup.

### Category 2: Collision Edge Cases
*   **EC-004:** Perfect Null Collision (Tie).
    *   *Input:* Triggers 1 Positive Principle, 1 Negative Principle.
    *   *Expected Behavior:* Generates a "Neutral / Deadlocked" Framework title. Highlights the tension.
*   **EC-005:** Only Negative Principles Activated.
    *   *Input:* `"PSU announces mega acquisition at peak valuations"` -> Triggers `[Avoid PSUs]` and `[Avoid Peak Multiples]`.
    *   *Expected Behavior:* Generates a "Terminal Value Trap" Framework.
*   **EC-006:** Only Positive Principles Activated.
    *   *Input:* `"Private sector monopoly expands into new demographic."`
    *   *Expected Behavior:* Generates a "Pure Structural Tailwind" Framework.

### Category 3: Data Integrity Edge Cases
*   **EC-007:** Missing `polarity` key in `core_catalog.json`.
    *   *Expected Behavior:* Script throws a `KeyError` during `find_activated_principles()` and halts, preventing bad data from entering the collision logic.
*   **EC-008:** Empty `trigger_tags` in Macro Input.
    *   *Input:* `{"trigger_tags": []}`
    *   *Expected Behavior:* Graceful exit. "No tags provided."
*   **EC-009:** Duplicate tags in Macro Input.
    *   *Input:* `["incentive", "incentive"]`
    *   *Expected Behavior:* `abstract_tags()` uses Python `set()` to deduplicate before matching, ensuring principles aren't double-counted.

*(Note: Edge cases EC-010 through EC-100 follow this exact methodology, expanding on null states, malformed JSON, capitalization mismatches, unhandled exceptions, string-vs-list typing errors, maximum list length bounds, and unicode encoding failures in the JSON parsing).*