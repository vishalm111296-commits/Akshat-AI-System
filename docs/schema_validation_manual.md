# Schema Validation Manual

*This manual reviews the schemas defined in the MVP Blueprint, identifies missing or unused fields, and provides the final, developer-ready JSON schemas.*

## 1. Principle Schema (`core_catalog.json`)

**Audit Findings:**
*   *Missing Field:* The Output Blueprint requires a "Reasoning Paragraph", but the Principle schema lacks a `description` or `reasoning_text` field to populate it.
*   *Unused Field:* `evidence_count` is defined in the schema but explicitly unused by the `2_collide.py` MVP logic. It creates developer confusion.
*   *Ambiguous Field:* `polarity` lacks enum enforcement.

**Final Recommended Schema:**
```json
[
  {
    "id": "PRIN-001",
    "title": "Follow Government Subsidies",
    "description": "Government incentives provide a structural catalyst that offsets traditional cost-of-capital burdens.",
    "activation_tags": ["incentive", "government", "subsidy", "pli"],
    "polarity": "positive"
  },
  {
    "id": "PRIN-002",
    "title": "Avoid Capital-Intensive Execution Traps",
    "description": "Heavy manufacturing historically traps capital in India due to execution delays and high interest rates.",
    "activation_tags": ["capex", "manufacturing"],
    "polarity": "negative"
  },
  {
    "id": "PRIN-003",
    "title": "Follow Geopolitical Supply-Chain Shifts",
    "description": "Global supply chain derisking forces capital into specific domestic sectors regardless of immediate valuations.",
    "activation_tags": ["geopolitics", "supply_chain", "china_plus_one"],
    "polarity": "positive"
  }
]
```

## 2. Ontology Schema (`ontology_map.json`)

**Audit Findings:**
*   *Naming Inconsistencies:* Nouns must be strictly lowercase. Arrays must be strictly lowercase.

**Final Recommended Schema:**
```json
{
  "semiconductor": ["capex", "geopolitics", "supply_chain"],
  "defense": ["government", "psu", "monopsony"],
  "hospital": ["demographics", "pricing_power", "capex"],
  "data center": ["capex", "power", "real_estate"]
}
```

## 3. Macro Input Schema (`macro_input.json`)

**Audit Findings:**
*   *Duplicate Fields:* `description` is used to store the human-readable text, but there is no field to pass the raw string into the script if the script is supposed to parse tags itself. However, the blueprint explicitly states `trigger_tags` are passed manually. We will keep it manual for the MVP.
*   *Missing Fields:* None.

**Final Recommended Schema:**
```json
{
  "event_id": "MACRO-TEST-02",
  "description": "Government launches large semiconductor manufacturing incentives.",
  "trigger_tags": ["semiconductor", "incentive", "government"]
}
```