# Implementation Blockers

*This document catalogs every ambiguity, contradiction, and missing definition that would block a developer from immediately building the MVP based on the current blueprint.*

## 1. Data & Ontology Blockers
*   **Blocker ID:** BLK-DATA-01
*   **Description:** Missing Ontology Fallback Logic.
*   **Why it blocks:** The blueprint says "If a tag doesn't exist in the ontology, it adds the original tag." However, if a user inputs "AI Chips" and it is not in the ontology, the system searches for "AI Chips" in the Core Catalog. The Core Catalog explicitly forbids specific sector nouns. Thus, unmapped inputs will *always* silently fail to trigger principles.
*   **Severity:** Critical.
*   **Recommended Resolution:** Implement an explicit Exception/Warning output if an input tag fails to map to *any* ontology key and simultaneously fails to match any catalog tag.

## 2. Principle Catalog Blockers
*   **Blocker ID:** BLK-PRIN-01
*   **Description:** Ambiguous Polarity Math.
*   **Why it blocks:** The blueprint states `positive > 0 and negative > 0` generates "State-Sponsored Catch-Up Narrative with Execution Risk." What if the activated principles are "Follow Demographic Shifts" (Positive) and "Avoid High P/E" (Negative)? Generating a "State-Sponsored" framework makes zero sense for a healthcare/valuation collision. The MVP collision logic is hardcoded to a single specific scenario rather than being generic.
*   **Severity:** Critical.
*   **Recommended Resolution:** The `synthesize_framework()` function must dynamically concatenate the *Titles* of the activated principles to generate the framework, rather than relying on a hardcoded string designed for only one specific test case.

## 3. Collision Engine Blockers
*   **Blocker ID:** BLK-COL-01
*   **Description:** Weighting / Scoring Omission.
*   **Why it blocks:** The Core Catalog schema includes `"evidence_count": 5`. The `2_collide.py` logic never mentions how `evidence_count` is used during a collision. If two positive principles collide with one negative principle, does a negative principle with an `evidence_count` of 500 override two positive principles with counts of 5? The math is undefined.
*   **Severity:** High.
*   **Recommended Resolution:** Explicitly define the tie-breaker logic in `synthesize_framework()`. For the MVP, explicitly ignore `evidence_count` and state that Polarity count (`len(positive)` vs `len(negative)`) is the sole resolving variable.

## 4. Schemas Blockers
*   **Blocker ID:** BLK-SCH-01
*   **Description:** Missing `polarity` validation definition.
*   **Why it blocks:** The schema defines `"polarity"` as a string, but the collision engine math checks if `positive > 0`. A developer doesn't know if the string should be exact case `"positive"`, `"Positive"`, `1`, or `-1`.
*   **Severity:** Medium.
*   **Recommended Resolution:** Enforce strict enum `["positive", "negative"]` in `principle_schema.json` and cast to lowercase during runtime.

## 5. Outputs & User Workflow Blockers
*   **Blocker ID:** BLK-OUT-01
*   **Description:** "Reasoning Paragraph" Source.
*   **Why it blocks:** The Output Report requires a `**Reasoning:** {reasoning_paragraph}`. The blueprint does not explain *where* this paragraph comes from. Does the developer hardcode it? Does the script generate it from the principle descriptions? A developer cannot write code for a variable with an undefined origin.
*   **Severity:** High.
*   **Recommended Resolution:** The MVP must concatenate the predefined descriptions of the Activated Principles to form the Reasoning Paragraph, requiring a new `"description"` field to be added back to the `core_catalog.json` schema.