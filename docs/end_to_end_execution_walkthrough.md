# End-to-End Execution Walkthrough

## Scenario
Macro Event: "Government launches major semiconductor manufacturing incentives."

---

## Step 0: Input JSON (`tests/mvp/macro_input.json`)
```json
{
  "event_id": "EVT-2026-100",
  "date": "2026-08-15",
  "raw_text": "Government launches major semiconductor manufacturing incentives.",
  "hard_data_metrics": {},
  "expected_principles": ["GF-05", "SS-03"]
}
```

---

## Step 1: Ontology Translation (In-Memory)
The `collide.py` engine scans `raw_text` against `ontology_map.json`.

**Ontology Map Snippet:**
```json
{
  "manufacturing incentives": ["capex_cycle", "margin_expansion"],
  "semiconductor": ["ai_infrastructure", "tech_hardware"]
}
```

**Ontology Output JSON:**
```json
{
  "event_id": "EVT-2026-100",
  "extracted_tags": ["capex_cycle", "margin_expansion", "ai_infrastructure", "tech_hardware"]
}
```

---

## Step 2: Activated Principles (In-Memory)
The engine queries `core_catalog.json` for principles matching any of the extracted tags.

**Activated Principles JSON:**
```json
[
  {
    "id": "SS-03",
    "name": "Prefer margin expansion",
    "type": "child",
    "parent_id": "P-EarningsGravity",
    "domain": "Equity Valuation",
    "activation_tags": ["margin_expansion", "pricing_power"],
    "activation_condition": "ANY"
  },
  {
    "id": "GF-05",
    "name": "K-shaped economy: buy profit-expansion segments",
    "type": "tactic",
    "parent_id": "SS-03",
    "domain": "Geography",
    "activation_tags": ["capex_cycle", "margin_expansion"],
    "activation_condition": "ANY"
  },
  {
    "id": "RM-02",
    "name": "Avoid concentration risk",
    "type": "constraint",
    "parent_id": "P-AsymmetryLoss",
    "domain": "Risk Management",
    "activation_tags": ["tech_hardware"],
    "activation_condition": "ANY"
  }
]
```

---

## Step 3: Principle Collision (In-Memory)
The engine evaluates hierarchy and constraints. `RM-02` (Constraint) acts on the domain.

**Collision Result JSON:**
```json
[
  {
    "principle_id": "SS-03",
    "matched_tags": ["margin_expansion"],
    "type": "child",
    "status": "active",
    "suppressing_constraint_id": null
  },
  {
    "principle_id": "GF-05",
    "matched_tags": ["capex_cycle", "margin_expansion"],
    "type": "tactic",
    "status": "active",
    "suppressing_constraint_id": null
  },
  {
    "principle_id": "RM-02",
    "matched_tags": ["tech_hardware"],
    "type": "constraint",
    "status": "active",
    "suppressing_constraint_id": null
  }
]
```

*(Note: In this specific scenario, RM-02 does not explicitly suppress GF-05 because they don't share a direct parent/child suppression link, but RM-02 will enforce sizing in the final output).*

---

## Step 4: Framework Generation (In-Memory String Assembly)
The engine applies a string template to the Collision Result JSON.

**Template Output:**
```text
EVENT: Government launches major semiconductor manufacturing incentives.
TAGS: capex_cycle, margin_expansion, ai_infrastructure, tech_hardware

CONSTRAINTS:
- RM-02: Avoid concentration risk

TACTICS:
- GF-05: K-shaped economy: buy profit-expansion segments

STRUCTURAL THEMES:
- SS-03: Prefer margin expansion
```

---

## Step 5: Final Report (`docs/mvp_output/generated_frameworks/reasoning_report.md`)
```markdown
# Reasoning Report: EVT-2026-100
**Date:** 2026-08-15

## 1. Summary of Macro Event
Government launches major semiconductor manufacturing incentives.

## 2. Activated Constraints (Hard Boundaries)
- **RM-02:** Avoid concentration risk (Triggered by: tech_hardware). Do not exceed standard sizing caps despite the narrative.

## 3. Activated Tactics (Offensive Actions)
- **GF-05:** K-shaped economy: buy profit-expansion segments. Look for specific beneficiaries of the capex cycle, not broad indices.

## 4. Final Proposed Framework
We are entering a `capex_cycle` driving `margin_expansion` in `tech_hardware`.
Action: Identify profit-expanding companies (SS-03), buy them as tactical allocations (GF-05), but strictly cap sizing to avoid concentration risk (RM-02).
```
