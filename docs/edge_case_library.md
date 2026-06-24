# Edge Case Library

This document outlines exactly 100 edge cases to test the structural integrity of the MVP Collision Engine.

### 1. Unknown Industry
- **Input:** "Govt subsidizes asteroid mining."
- **Expected Behavior:** Empty tag array; output returns "No actionable principles."
- **Failure Risk:** Hallucinating a random tech principle.

### 2. Unknown Country
- **Input:** "Estonia raises interest rates."
- **Expected Behavior:** Match general rate tag; output generic liquidity principle.
- **Failure Risk:** Assuming US/India specific rules apply to Estonia.

### 3. Conflicting Tactics
- **Input:** "Market crashes 30% but VIX hits 90."
- **Expected Behavior:** Trigger "Buy 200DMA" AND "Wait for V-shape invalidation".
- **Failure Risk:** Contradictory report telling user to both buy and wait.

### 4. Missing Tags
- **Input:** `tests/mvp/macro_input.json` has an empty `raw_text`.
- **Expected Behavior:** Script catches empty input and exits cleanly.
- **Failure Risk:** Python `KeyError` or null pointer exception.

### 5. Empty Ontology Match
- **Input:** "The sky is blue today."
- **Expected Behavior:** Zero tags matched, zero principles activated.
- **Failure Risk:** Engine forces a default output.

### 6. Constraint Overrides Tactic
- **Input:** "Retail option margin requirement drops to zero."
- **Expected Behavior:** Tactic triggered, but "NEVER sell naked options" Constraint suppresses it.
- **Failure Risk:** Constraint fails to suppress, recommending naked options.

### 7. Multiple Framework Matches
- **Input:** "AI boom causes severe power grid shortage."
- **Expected Behavior:** Output framework combining AI Infrastructure AND Power Utilities.
- **Failure Risk:** Output merges them into a nonsensical combined asset class.

### 8. Contradictory Macro Signals
- **Input:** "Fed cuts rates but prints $2T in bonds."
- **Expected Behavior:** Both liquidity expansion and inflation tags hit; output Barbell recommendation.
- **Failure Risk:** Cancels out to zero action.

### 9. Typo in Raw Text
- **Input:** "Intrest rets ar cut."
- **Expected Behavior:** No ontology match unless fuzzy matching is built (MVP is exact match).
- **Failure Risk:** Misses obvious macro signal.

### 10. Capitalization Mismatch
- **Input:** "RATE CUT"
- **Expected Behavior:** Ontology map is case-insensitive, matches correctly.
- **Failure Risk:** Fails to match lowercase dictionary key.

### 11. Overloaded Input
- **Input:** 50-page text dump of Fed meeting minutes.
- **Expected Behavior:** Matches 100+ tags, triggers 20+ principles.
- **Failure Risk:** Output report becomes unreadable text wall.

### 12. Recursive Suppressions
- **Input:** Constraint A suppresses Tactic B; Constraint C suppresses A.
- **Expected Behavior:** MVP does not support recursive suppression; strict 1-level hierarchy.
- **Failure Risk:** Infinite loop in conflict resolution.

### 13. Null Expected Principles
- **Input:** `expected_principles` array is `null`.
- **Expected Behavior:** PyTest skips the assertion.
- **Failure Risk:** PyTest crashes trying to iterate null.

### 14. Broken JSON Format
- **Input:** `macro_input.json` missing a trailing comma.
- **Expected Behavior:** `json.load()` throws clear error before engine starts.
- **Failure Risk:** Silent failure.

### 15. Duplicate Activation Tags
- **Input:** Core catalog lists `["risk_on", "risk_on"]`.
- **Expected Behavior:** Tag deduplicated in memory.
- **Failure Risk:** Principle counted twice in output.

### 16. Parent Principle Triggered without Child
- **Input:** Tag matches Parent only.
- **Expected Behavior:** Output Parent as a structural theme, no tactics proposed.
- **Failure Risk:** Engine demands a tactic and fails.

### 17. Tactic Triggered without Parent
- **Input:** Tag matches Tactic only.
- **Expected Behavior:** Automatically fetch and display the Parent principle for context.
- **Failure Risk:** Tactic displayed without underlying logic.

### 18. All Constraints Triggered
- **Input:** Input text explicitly targets all known risk vectors.
- **Expected Behavior:** Report outputs only Constraints (Hard NO on everything).
- **Failure Risk:** Framework forces a "Buy" recommendation.

### 19. No Constraints Triggered
- **Input:** Perfect Goldilocks scenario.
- **Expected Behavior:** Constraints section is explicitly marked "None triggered."
- **Failure Risk:** UI breaks due to empty array.

### 20. Event Date in the Future
- **Input:** "2030-01-01"
- **Expected Behavior:** Processes normally.
- **Failure Risk:** Date validation crashes.

### 21. Event Date in the Past
- **Input:** "2008-09-15"
- **Expected Behavior:** Processes normally.
- **Failure Risk:** None.

### 22. Maximum Tag Threshold Exceeded
- **Input:** Event triggers 50 unique tags.
- **Expected Behavior:** Processes all tags.
- **Failure Risk:** Output formatting overflows readable space.

### 23. Special Characters in Text
- **Input:** "Cuts rates by 50bps! @ # $%^"
- **Expected Behavior:** Regex/split ignores punctuation.
- **Failure Risk:** Ontology matching fails due to attached punctuation.

### 24. Multi-word Ontology Match
- **Input:** "quantitative easing"
- **Expected Behavior:** Matches exact phrase.
- **Failure Risk:** Only matches "quantitative".

### 25. Sub-word Ontology Match
- **Input:** "inflationary" vs map "inflation"
- **Expected Behavior:** Exact match requirement fails (MVP constraint).
- **Failure Risk:** False negative.

### 26. `ALL` Condition with 1 Missing Tag
- **Input:** Principle requires `["A", "B"]`, input has `["A"]`.
- **Expected Behavior:** Principle does NOT activate.
- **Failure Risk:** Incorrect activation.

### 27. `ANY` Condition with 1 Tag
- **Input:** Principle requires `["A", "B"]`, input has `["A"]`.
- **Expected Behavior:** Principle activates.
- **Failure Risk:** Fails to activate.

### 28. Empty Tag Array in Principle
- **Input:** Principle in catalog has `activation_tags: []`.
- **Expected Behavior:** Never activates.
- **Failure Risk:** Activates on every event.

### 29. Null Domain
- **Input:** Principle lacks a domain.
- **Expected Behavior:** JSON schema validation fails at load.
- **Failure Risk:** Runtime error during sorting.

### 30. Unrecognized Principle Type
- **Input:** Type is "hybrid_tactic".
- **Expected Behavior:** JSON schema validation fails at load.
- **Failure Risk:** Engine doesn't know how to format it.

### 31. Two Identical Tactics
- **Input:** Core catalog has two identical objects with different IDs.
- **Expected Behavior:** Both activate and print.
- **Failure Risk:** Confuses the user.

### 32. Circular Parent Reference
- **Input:** P1 parent is P2, P2 parent is P1.
- **Expected Behavior:** Infinite loop in hierarchy resolution.
- **Failure Risk:** High; script hangs.

### 33. Missing Parent ID
- **Input:** Child principle references non-existent parent ID.
- **Expected Behavior:** Resolves child, prints warning for missing parent.
- **Failure Risk:** Fatal crash.

### 34. Extremely Long Raw Text
- **Input:** 1MB text file string.
- **Expected Behavior:** Processes slowly but succeeds.
- **Failure Risk:** Memory overflow.

### 35. Very Short Raw Text
- **Input:** "Buy"
- **Expected Behavior:** Zero matches.
- **Failure Risk:** Over-matches on short substrings.

### 36. Foreign Language Input
- **Input:** "Banco Central baja tasas."
- **Expected Behavior:** Zero matches (English ontology only).
- **Failure Risk:** Fails to read the macro event.

### 37. Emojis in Input
- **Input:** "Fed cuts rates 📉"
- **Expected Behavior:** Ignores emoji, matches "Fed cuts rates".
- **Failure Risk:** Unicode parsing error.

### 38. Numeric Ontology Keys
- **Input:** "200DMA"
- **Expected Behavior:** Matches correctly if in map.
- **Failure Risk:** Type cast error.

### 39. Overlapping Ontology Keys
- **Input:** Map has "rate cut" and "interest rate cut".
- **Expected Behavior:** Both match if text has "interest rate cut".
- **Failure Risk:** Double tags extracted.

### 40. Extracted Tag Not in Catalog
- **Input:** Ontology outputs `["space_mining"]` but catalog has no such tag.
- **Expected Behavior:** Tag ignored during collision.
- **Failure Risk:** Crash on lookup.

### 41. Catalog Tag Not in Ontology
- **Input:** Catalog has `["quantum_computing"]` but ontology map never outputs it.
- **Expected Behavior:** Dead principle, never activates.
- **Failure Risk:** None, just bad data.

### 42. Output Directory Missing
- **Input:** `docs/mvp_output/` deleted.
- **Expected Behavior:** Script creates directory (`os.makedirs`).
- **Failure Risk:** File write `FileNotFoundError`.

### 43. Read-Only Output File
- **Input:** Output markdown file locked.
- **Expected Behavior:** Graceful exception print.
- **Failure Risk:** Hard crash.

### 44. Concurrency Test
- **Input:** Two users trigger `collide.py` simultaneously.
- **Expected Behavior:** Second overwrites first (MVP is single-threaded local).
- **Failure Risk:** Race condition on output file.

### 45. Zero Core Principles Load
- **Input:** `core_catalog.json` is `[]`.
- **Expected Behavior:** No principles activate.
- **Failure Risk:** Crash iterating empty array.

### 46. Valid JSON, Wrong Structure
- **Input:** `core_catalog.json` is `{"key": "value"}` instead of Array.
- **Expected Behavior:** Type error caught immediately.
- **Failure Risk:** Silent type failure downstream.

### 47. Trailing Whitespace in Tags
- **Input:** Tag is `" risk_on "`.
- **Expected Behavior:** Fails to match `"risk_on"` (strict string).
- **Failure Risk:** Missed match due to bad data hygiene.

### 48. Case Mismatch in Tags
- **Input:** Catalog uses `"Risk_On"`, ontology outputs `"risk_on"`.
- **Expected Behavior:** Fails to match (JSON is case sensitive).
- **Failure Risk:** Data architecture failure.

### 49. Contradictory Test Assertion
- **Input:** `expected_principles: ["SS-01"]` but input triggers `["GF-01"]`.
- **Expected Behavior:** PyTest flags as FAILED.
- **Failure Risk:** Test suite reports false positive.

### 50. Missing Expected Principles Array
- **Input:** Key `expected_principles` not in JSON.
- **Expected Behavior:** Skip assertion.
- **Failure Risk:** Test crash.

### 51. Output Formatting Overflow
- **Input:** 50 principles activate.
- **Expected Behavior:** Markdown generates massive list.
- **Failure Risk:** Unreadable output.

### 52. Only Domain "Geography" Triggered
- **Input:** Event entirely geographical.
- **Expected Behavior:** Other sections empty but present.
- **Failure Risk:** Markdown layout shifts weirdly.

### 53. Unmatched Constraint Override
- **Input:** Constraint claims to override Tactic ID "XYZ", but XYZ not active.
- **Expected Behavior:** Constraint prints, override ignored.
- **Failure Risk:** Crash checking null.

### 54. Tactic Overrides Tactic
- **Input:** Bad data defines a Tactic suppressing another Tactic.
- **Expected Behavior:** Ignored. Only Constraints can suppress.
- **Failure Risk:** Engine logic broken.

### 55. Null Event ID
- **Input:** `event_id` is null.
- **Expected Behavior:** Auto-generate UUID or fallback string.
- **Failure Risk:** Overwrites default file named `null.md`.

### 56. Special Chars in Event ID
- **Input:** `event_id`: "../../../etc/passwd"
- **Expected Behavior:** Path traversal failure if used as filename.
- **Failure Risk:** Security vulnerability.

### 57. Empty Ontology File
- **Input:** `ontology_map.json` is `{}`.
- **Expected Behavior:** Zero matches always.
- **Failure Risk:** Crash on load.

### 58. Large Nested Input Data
- **Input:** `hard_data_metrics` contains 5 levels of nesting.
- **Expected Behavior:** Ignored by MVP (MVP only reads `raw_text`).
- **Failure Risk:** Memory spike.

### 59. Incorrect Schema URL
- **Input:** `$schema` points to 404 URL.
- **Expected Behavior:** Local validator ignores network.
- **Failure Risk:** Validation crash if strictly resolving.

### 60. Missing Required Field 'name'
- **Input:** Principle lacks `name`.
- **Expected Behavior:** Schema load fails.
- **Failure Risk:** Output prints `None` or crashes on f-string.

### 61. Duplicate Principle IDs
- **Input:** Two principles share ID `CP-01`.
- **Expected Behavior:** Dictionary key overwrite (last wins).
- **Failure Risk:** Data loss.

### 62. Negative Numbers in Tags
- **Input:** Tag is integer `-1`.
- **Expected Behavior:** Type mismatch (expects string).
- **Failure Risk:** Tag engine exception.

### 63. "False" as String Tag
- **Input:** Tag is `"false"`.
- **Expected Behavior:** Processes as literal string.
- **Failure Risk:** Interpreted as boolean.

### 64. Extracted Tags Count == 0
- **Input:** Script runs but text matches no dictionary keys.
- **Expected Behavior:** Clean exit, report notes "No tags".
- **Failure Risk:** System attempts to search `None`.

### 65. Hyphenated Tags
- **Input:** `risk-on` vs `risk_on`.
- **Expected Behavior:** Missed match unless sanitized.
- **Failure Risk:** Inconsistent taxonomy.

### 66. Empty Output String
- **Input:** Template assembly fails.
- **Expected Behavior:** Write empty `.md` file.
- **Failure Risk:** Write lock.

### 67. File Permissions 777
- **Input:** `collide.py` run in open dir.
- **Expected Behavior:** Runs normally.
- **Failure Risk:** Security risk on server.

### 68. File Permissions 000
- **Input:** Catalog file is unreadable.
- **Expected Behavior:** PermissionError raised.
- **Failure Risk:** Silent failure.

### 69. Missing `tests/` directory
- **Input:** Dir deleted before run.
- **Expected Behavior:** FileNotFoundError.
- **Failure Risk:** None.

### 70. CLI Arg Missing
- **Input:** `python collide.py --event` (no file).
- **Expected Behavior:** Argparse throws error.
- **Failure Risk:** Script hangs.

### 71. Invalid JSON encoding
- **Input:** File saved as UTF-16.
- **Expected Behavior:** UnicodeDecodeError.
- **Failure Risk:** Fatal crash.

### 72. Extremely High Match Count
- **Input:** Phrase matches 100 times in text.
- **Expected Behavior:** Set() deduplicates tags.
- **Failure Risk:** Array overflow.

### 73. Blank Lines in Text
- **Input:** String with `\n\n\n`.
- **Expected Behavior:** Handled correctly.
- **Failure Risk:** Regex breaks.

### 74. Tab Characters
- **Input:** `\t` instead of space.
- **Expected Behavior:** Treated as whitespace.
- **Failure Risk:** Word matching fails.

### 75. Non-String Value in Ontology Array
- **Input:** `{"key": [123]}`
- **Expected Behavior:** Schema validation fails.
- **Failure Risk:** Type cast error in matching.

### 76. Nested Arrays in Tags
- **Input:** `[["risk_on"]]`
- **Expected Behavior:** Schema validation fails.
- **Failure Risk:** Unhashable type error.

### 77. Null Match Array
- **Input:** `{"key": null}`
- **Expected Behavior:** Schema load fails.
- **Failure Risk:** Iteration over NoneType.

### 78. Missing `collide.py`
- **Input:** User tries to execute missing script.
- **Expected Behavior:** bash `No such file`.
- **Failure Risk:** None.

### 79. Python 2.7 Environment
- **Input:** Executed with old python.
- **Expected Behavior:** SyntaxError on f-strings.
- **Failure Risk:** Total failure.

### 80. Missing `pytest`
- **Input:** `pytest` not installed.
- **Expected Behavior:** `command not found`.
- **Failure Risk:** Pipeline fails.

### 81. Output Directory is File
- **Input:** `docs/mvp_output` exists as a text file.
- **Expected Behavior:** `NotADirectoryError`.
- **Failure Risk:** Cannot save report.

### 82. Long Event ID
- **Input:** `event_id` is 1000 characters.
- **Expected Behavior:** OS rejects filename creation.
- **Failure Risk:** OSOSError.

### 83. Trailing Slash in Paths
- **Input:** Script internally uses `path/` + `/file`.
- **Expected Behavior:** Path resolution handles `//`.
- **Failure Risk:** Malformed file path.

### 84. `activation_condition` typo
- **Input:** `"ANYY"` instead of `"ANY"`.
- **Expected Behavior:** Schema rejection.
- **Failure Risk:** Defaults to wrong logic.

### 85. Event with No `raw_text` Field
- **Input:** Key is entirely missing.
- **Expected Behavior:** Schema rejection / KeyError.
- **Failure Risk:** Fatal.

### 86. Multiple Events in One Run
- **Input:** Input JSON is an array of events.
- **Expected Behavior:** Fails (MVP schema expects single object).
- **Failure Risk:** Wrong loop logic.

### 87. Principle Modifies Input
- **Input:** Code accidentally overwrites input dictionary.
- **Expected Behavior:** N/A (Python dict mutability).
- **Failure Risk:** Downstream logic corruption.

### 88. Hardcoded Path Failure
- **Input:** Run from different working directory.
- **Expected Behavior:** Script uses relative paths incorrectly.
- **Failure Risk:** FileNotFoundError.

### 89. Tag Extracted is Empty String
- **Input:** `[""]`
- **Expected Behavior:** Matches nothing.
- **Failure Risk:** Matches every string via substring logic.

### 90. Output Template Missing Section
- **Input:** Code forgets "Constraints" block.
- **Expected Behavior:** Report is generated but flawed.
- **Failure Risk:** Critical data lost to user.

### 91. Overriding Non-Tactic
- **Input:** Constraint suppresses a Parent.
- **Expected Behavior:** Ignores override (Parents can't be suppressed).
- **Failure Risk:** Logic tree collapse.

### 92. Tactic With No Domain
- **Input:** Field missing.
- **Expected Behavior:** JSON schema rejection.
- **Failure Risk:** F-string crash during sorting.

### 93. Unescaped Quotes in Text
- **Input:** `"The "Fed" cuts"`
- **Expected Behavior:** If JSON valid, works.
- **Failure Risk:** Invalid JSON parse.

### 94. Hex-encoded strings
- **Input:** `\u0041`
- **Expected Behavior:** Python `json` handles it.
- **Failure Risk:** None.

### 95. Parent ID equals Own ID
- **Input:** `parent_id == id`.
- **Expected Behavior:** Circular reference.
- **Failure Risk:** Infinite loop.

### 96. Maximum Recursion Depth
- **Input:** 1000 nested Parent-Child links.
- **Expected Behavior:** RecursionError.
- **Failure Risk:** Crash.

### 97. `pytest` Output Redirected
- **Input:** `pytest > /dev/null`.
- **Expected Behavior:** Silent execution.
- **Failure Risk:** Hidden test failures.

### 98. Event Name vs ID
- **Input:** `event_id` has spaces.
- **Expected Behavior:** Spaces in output filename.
- **Failure Risk:** Bash scripting annoyance downstream.

### 99. Floating Point Hard Data
- **Input:** `"rate": 5.25`
- **Expected Behavior:** Processed as string (if schema enforces).
- **Failure Risk:** Type failure if strict string expected.

### 100. System Exhaustion
- **Input:** Script run in `while true` loop.
- **Expected Behavior:** Maxes out CPU.
- **Failure Risk:** I/O bottleneck.
