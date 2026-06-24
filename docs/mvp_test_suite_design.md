# MVP Test Suite Design

*This test suite validates the core functionality of `2_collide.py`.*

## 1. Happy Path Tests

*   **Test ID:** `TEST-HAPPY-01`
    *   *Type:* Basic Match
    *   *Input:* `macro_input.json` with `["government", "subsidy"]`.
    *   *Expected Output:* Activates PRIN-001. Framework title contains "Tailwind".
    *   *Pass Criteria:* Output file generated correctly, no errors, principles listed.
*   **Test ID:** `TEST-HAPPY-02`
    *   *Type:* Ontology Abstraction
    *   *Input:* `["semiconductor"]`
    *   *Expected Output:* Activates PRIN-002, PRIN-003.
    *   *Pass Criteria:* System correctly resolves "semiconductor" to abstract tags and finds multiple principles.

## 2. Negative Tests

*   **Test ID:** `TEST-NEG-01`
    *   *Type:* Unmapped Input
    *   *Input:* `["flying_cars"]`
    *   *Expected Output:* No framework generated.
    *   *Pass Criteria:* Script exits cleanly with code 0 and logs "0 principles activated."
*   **Test ID:** `TEST-NEG-02`
    *   *Type:* Bad JSON
    *   *Input:* `macro_input.json` missing trailing brace.
    *   *Expected Output:* `json.decoder.JSONDecodeError`
    *   *Pass Criteria:* Script catches exception and prints "Invalid JSON Input."

## 3. Ambiguity & Contradiction Tests

*   **Test ID:** `TEST-AMB-01`
    *   *Type:* The Null Collision
    *   *Input:* Tags that trigger exactly 1 Positive and 1 Negative principle.
    *   *Expected Output:* Framework string states "Deadlocked".
    *   *Pass Criteria:* Math resolves equality correctly without defaulting to Tailwind.
*   **Test ID:** `TEST-AMB-02`
    *   *Type:* Case Sensitivity
    *   *Input:* `["SeMiConDuctor"]`
    *   *Expected Output:* Matches "semiconductor" in ontology.
    *   *Pass Criteria:* `abstract_tags()` function enforces `.lower()` on all inputs before dictionary lookup.

## 4. Stress Tests

*   **Test ID:** `TEST-STR-01`
    *   *Type:* Tag Overload
    *   *Input:* 1,000 randomized trigger tags.
    *   *Expected Output:* Activates all available principles.
    *   *Pass Criteria:* Executes in under 1.0 seconds. Proves the `set()` intersection math is fast enough for the MVP.