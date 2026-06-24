# Evidence Gap Matrix

This matrix evaluates the verifiable evidence supporting the 6 principles physically implemented in the MVP's `core_catalog.json`.

**Scoring Guide (0-10):**
*   **Evidence Coverage:** Amount of granular, verifiable source files mapping to the principle.
*   **Evidence Diversity:** Spread of evidence across different formats (YT, Community Posts, Paid).
*   **Historical Coverage:** Time spread of the evidence.
*   **Contradictory Evidence:** Lower score means higher contradiction or unresolved conflicts.
*   **Real World Validation:** Does the principle actually work when backtested?

---

| Principle ID | Name | Evidence Coverage | Evidence Diversity | Historical Coverage | Contradictory Evidence | Real World Validation |
|---|---|---|---|---|---|---|
| **P-EarningsGravity** | Earnings Gravity | 0 | 0 | 0 | 5 | 0 |
| **SS-03** | Prefer margin expansion | 0 | 0 | 0 | 3 | 0 |
| **GF-05** | K-shaped economy | 0 | 0 | 0 | 4 | 0 |
| **P-AsymmetryLoss** | Asymmetry of Loss | 0 | 0 | 0 | 5 | 0 |
| **RM-02** | Avoid concentration risk | 0 | 0 | 0 | 2 | 0 |
| **RM-03** | NEVER sell naked options | 0 | 0 | 0 | 0 | 0 |

---

### Brutal Justification for the Zeros:

As discovered in Phase 1 audits (`docs/evidence_coverage_audit.md`), **100% of the evidence supporting these principles is fake or deprecated.**

The Frequency Table claims 7 to 12 sources for these items, but cites `YT-2026-001` or `CP-2026-001`, which are explicitly marked as "DEPRECATED batch entries" in the `03_Source_Database.md`. Because there is no granular source file (e.g., `YT-2022-04-12-transcript.txt`), there is zero verifiable evidence coverage, diversity, or historical spread. Real-world validation is 0 because the stock selection layer was proven broken in the `stock_selection_rca.md`.

**RM-03 Contradiction Score (0/10):** This principle has a massive unresolved contradiction in the Frequency Table where it exists simultaneously as RM-03 and OP-03, splitting the fake evidence counts across two different logical silos.
