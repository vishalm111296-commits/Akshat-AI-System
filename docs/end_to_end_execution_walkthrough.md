# End-to-End Execution Walkthrough

*This document simulates the execution of the final, debugged MVP code sequence step-by-step, ensuring the developer understands data transformation states.*

## Inputs Loaded
1.  **Macro Event:** `{"event_id": "M-01", "description": "Government launches major semiconductor manufacturing incentives.", "trigger_tags": ["semiconductor", "incentive", "manufacturing"]}`
2.  **Ontology Map:** `{ "semiconductor": ["capex", "geopolitics", "supply_chain"] }`
3.  **Core Catalog:** (Loaded with PRIN-001 [Subsidies], PRIN-002 [Execution Trap], PRIN-003 [Geopolitics]).

---

## Step 1: Ontology Translation
*Function:* `abstract_tags()`
*   Reads `trigger_tags`: `["semiconductor", "incentive", "manufacturing"]`
*   Passes "semiconductor" through Ontology Map. Replaces with `["capex", "geopolitics", "supply_chain"]`.
*   "incentive" and "manufacturing" do not exist in map. Kept as is.
*   **Intermediate State (Abstracted Tags Set):** `{"capex", "geopolitics", "supply_chain", "incentive", "manufacturing"}`

---

## Step 2: Activated Principles
*Function:* `find_activated_principles()`
*   Scans `core_catalog.json` using the Abstracted Tags Set.
*   Matches "incentive" -> Activates **PRIN-001: Follow Government Subsidies** (Polarity: Positive)
*   Matches "capex", "manufacturing" -> Activates **PRIN-002: Avoid Capital-Intensive Execution Traps** (Polarity: Negative)
*   Matches "geopolitics", "supply_chain" -> Activates **PRIN-003: Follow Geopolitical Supply-Chain Shifts** (Polarity: Positive)
*   **Intermediate State (Active List):** `[PRIN-001, PRIN-002, PRIN-003]`

---

## Step 3: Principle Collision
*Function:* `synthesize_framework()`
*   Parses the Active List for polarities.
*   Positive Count: 2 (PRIN-001, PRIN-003)
*   Negative Count: 1 (PRIN-002)
*   *Resolved Collision State:* Conflict exists, but positive structural tailwinds mathematically outweigh negative execution constraints (2 > 1).

---

## Step 4: Framework Generation
*Function:* `synthesize_framework()` (Continued)
*   *Framework Title Generation:* Instead of hardcoding, the system derives the framework from the dominant principles.
    *   Title: "Convergence of Follow Government Subsidies & Follow Geopolitical Supply-Chain Shifts"
*   *Reasoning Generation:* Concatenates the `description` strings from the activated principles.
    *   Text: "Government incentives provide a structural catalyst... Global supply chain derisking forces capital... HOWEVER: Heavy manufacturing historically traps capital..."

---

## Step 5: Final Report Output
*Function:* `generate_report()`
*   Output written to: `docs/mvp_output/generated_frameworks/M-01.md`

```markdown
# Reasoning Report: M-01

**Event:** Government launches major semiconductor manufacturing incentives.

**Activated Principles:**
- [x] Follow Government Subsidies (Tailwind)
- [x] Follow Geopolitical Supply-Chain Shifts (Tailwind)
- [!] Avoid Capital-Intensive Execution Traps (Constraint)

**Synthesized Framework:** *Convergence of Follow Government Subsidies & Follow Geopolitical Supply-Chain Shifts*

**Reasoning:** Government incentives provide a structural catalyst that offsets traditional cost-of-capital burdens. Global supply chain derisking forces capital into specific domestic sectors regardless of immediate valuations.

**Risk Constraint:** Heavy manufacturing historically traps capital in India due to execution delays and high interest rates.
```