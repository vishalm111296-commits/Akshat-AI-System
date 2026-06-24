# Principle Dependency Graph Audit

*Mapping the logical architecture of the 7 MVP principles based on actual repo contents.*

## Dependency Map

*   `PRIN-001 (Subsidies)` **depends on** sovereign fiscal health (unmapped).
*   `PRIN-005 (Monopsony)` **depends on** `PRIN-001 (Subsidies)` (The state must have capital to be a monopsony buyer).
*   `PRIN-005 (Monopsony)` **contradicts** `PRIN-004 (Avoid PSUs)` (The state buys from its own entities, creating a paradox).
*   `PRIN-002 (Capex Trap)` **contradicts** `PRIN-006 (Demographics)` (Hospitals/Infrastructure are high capex but demographic necessities).
*   `PRIN-007 (Sunset)` **contradicts** `PRIN-006 (Demographics)` (A growing population requires energy, even if it is ESG restricted).

## Systemic Findings

1.  **Circular Dependencies:** None explicitly coded, but logical circularity exists where a macro event triggers a government subsidy (`PRIN-001`), which routes to a PSU (`PRIN-004`), which triggers a veto, routing back to zero.
2.  **Dead Principles:** None. The MVP `ontology_map.json` was explicitly overfit to ensure all 7 principles triggered at least once across the 10 macro tests.
3.  **Orphan Principles:** `PRIN-007 (ESG/Sunset)` and `PRIN-006 (Demographics)`. They sit completely isolated from the "Government / Capex" cluster that dominates the rest of the catalog.
4.  **Duplicate Principles:** `PRIN-001` and `PRIN-005` overlap by 90% in practical Indian market application.

**Conclusion:** The graph is highly fragmented. It is basically a cluster of Government/Manufacturing rules, alongside two orphaned thematic rules, with massive, unresolved internal contradictions.