# Schema Validation Manual

## Overview
This document reviews the missing, ambiguous, and unused fields from the initial architecture, producing the final recommended JSON schemas required for the MVP build.

---

## 1. Core Catalog Schema (`knowledge/principles/core_catalog.json`)

### Validation Notes
- **Missing:** `parent_id` (crucial for hierarchical resolution), `activation_condition` (ANY vs ALL tags).
- **Ambiguous:** `type` (needs strict enum).
- **Unused:** `source_count` (relevant for L7 extraction, but useless to the Collision Engine).

### Final Recommended Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": { "type": "string" },
      "name": { "type": "string" },
      "type": { "enum": ["parent", "child", "tactic", "constraint"] },
      "parent_id": { "type": ["string", "null"] },
      "domain": { "type": "string" },
      "activation_tags": {
        "type": "array",
        "items": { "type": "string" }
      },
      "activation_condition": { "enum": ["ANY", "ALL"] }
    },
    "required": ["id", "name", "type", "parent_id", "domain", "activation_tags", "activation_condition"]
  }
}
```

---

## 2. Ontology Map Schema (`scripts/mvp/ontology_map.json`)

### Validation Notes
- **Missing:** Exact array of allowable output tags (the enum).
- **Duplicate:** Multiple hard keywords might map to the same tag.
- **Ambiguous:** Regex support? (No, MVP should be simple substring match).

### Final Recommended Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "additionalProperties": {
    "type": "array",
    "items": { "type": "string" }
  },
  "description": "Keys are substring matches (e.g. 'rate cut'), values are the unified activation tags."
}
```

---

## 3. Macro Input Schema (`tests/mvp/macro_input.json`)

### Validation Notes
- **Missing:** Explicit separation of raw text vs extracted test tags (for unit testing the ontology map).
- **Unused:** `description` is often just duplicate text of `event_name`.
- **New Field Added:** `expected_principles` for automated testing.

### Final Recommended Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "event_id": { "type": "string" },
    "date": { "type": "string" },
    "raw_text": { "type": "string" },
    "hard_data_metrics": {
      "type": "object",
      "additionalProperties": { "type": "string" }
    },
    "expected_principles": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["event_id", "raw_text"]
}
```

---

## 4. Intermediate Structure: Active Principles JSON (In-Memory)

### Validation Notes
This represents the structure passed from `fetch_active_principles()` to `resolve_conflicts()`.

### Final Recommended Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "principle_id": { "type": "string" },
      "matched_tags": { "type": "array", "items": { "type": "string" } },
      "type": { "type": "string" },
      "status": { "enum": ["active", "suppressed_by_constraint"] },
      "suppressing_constraint_id": { "type": ["string", "null"] }
    }
  }
}
```
