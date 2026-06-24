# Duplicate Principle Audit

*A strict review of the 7 principles in `core_catalog.json` against the taxonomy rules established in Phase 2.*

### 1. Duplicates & Near Duplicates
*   **PRIN-001 (Follow Government Subsidies) vs. PRIN-005 (Follow Monopsony Buyers)**
    *   *Conflict:* These are near-duplicates. A government subsidy (PLI) is the state funneling capital to a sector. A monopsony buyer (Defense) is the state funneling capital to a sector by being the sole customer.
    *   *Resolution Required:* Both should be merged under a single parent principle: `[State-Sponsored Capital Allocation]`.

### 2. Taxonomy Conflicts (Flat Hierarchy)
*   **The Conflict:** The `core_catalog.json` schema currently defines all 7 principles as flat peers. It completely ignored the `docs/principle_taxonomy_review.md` rules which mandated `Parent -> Child -> Tactic/Constraint` structures.
*   **Example:** `PRIN-006 (Follow Demographic Destiny)` is a massive multi-decade **Parent** structural force. `PRIN-004 (Avoid PSUs)` is a micro-economic **Constraint**. They are currently stored and treated identically by the collision engine.

### 3. Missing Parent-Child Relationships
*   `PRIN-002 (Avoid Capital-Intensive Execution Traps)` currently sits alone. It is mathematically a child constraint of the missing parent node `[Require High Return on Capital Employed (ROCE)]`.
*   `PRIN-003 (Follow Geopolitical Supply-Chain Shifts)` is a child tactic of a broader missing parent node `[Global Capital Flow Routing]`.

### Audit Conclusion
The `core_catalog.json` is a flat, unorganized list. It violates the repository's own taxonomy rules. It contains near-duplicates (Subsidies vs Monopsony) and conflates 30-year macro trends with 1-year corporate governance constraints.