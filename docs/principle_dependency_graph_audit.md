# Principle Dependency Graph Audit

This audit maps the logical and structural dependencies of the 6 implemented principles without creating new architecture.

---

## 1. Mapped Dependencies (Parent/Child)

*   **P-EarningsGravity**
    *   *Child:* **SS-03** (Prefer margin expansion).
    *   *Grandchild:* **GF-05** (K-shaped economy). *Note: GF-05 has `parent_id`: `SS-03`.*
*   **P-AsymmetryLoss**
    *   *Child:* **RM-02** (Avoid concentration risk).
    *   *Child:* **RM-03** (NEVER sell naked options).

---

## 2. Structural Anomalies

### Circular Dependencies
*   **None technically implemented.** The MVP script `2_collide.py` explicitly ignores the `parent_id` field. Because the script flattens everything into a list, true circular dependencies cannot form in the runtime execution. However, conceptually, the ontology mapping (`ai_infrastructure` mapped from "semiconductor") creates circular reasoning where the input string dictates the conclusion without evaluation.

### Dead Principles
*   **P-EarningsGravity** and **P-AsymmetryLoss**.
    *   Because `collide.py` only filters on `activation_tags`, and these Parent principles have tags that almost perfectly overlap their children (e.g., `margin_expansion`, `concentration_risk`), they do not do anything structurally independent. They just print a duplicate line under "Structural Themes" whenever a child fires.

### Orphan Principles
*   **None in the JSON.** All 4 Tactical/Constraint principles correctly point to a Parent.

### Duplicate Principles
*   **RM-03 (NEVER sell naked options)**. This principle is a known exact duplicate of **OP-03**, representing a massive taxonomy failure in the Frequency Table.

### Overlaps
*   **SS-03** overlaps heavily with **GF-05**. They both share the `margin_expansion` activation tag. In almost every macro event that triggers one (e.g., "Semiconductor incentives"), the other triggers automatically, artificially inflating the weight of the recommendation in the final output report.
