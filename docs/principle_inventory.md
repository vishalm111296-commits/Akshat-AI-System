# Principle Inventory

This document maps every principle currently hardcoded into the MVP implementation (`knowledge/principles/core_catalog.json`) against the actual evidence claims found in the Frequency Table (`knowledge/02_Akshat_Principle_Frequency_Table.md`).

---

| ID | Name | Category | Claimed Evidence Count | Missing Evidence Count | Confidence Assessment |
|---|---|---|---|---|---|
| **P-EarningsGravity** | Earnings Gravity | Parent | N/A | N/A | **Low** - Manufactured for the MVP schema. Does not exist in the Frequency Table. |
| **SS-03** | Prefer margin expansion | Child | 9 | 9 | **Zero** - Frequency table claims 9, but relies entirely on deprecated batch IDs (`YT-2026-001`, `YT-2026-002`, `CP-2026-001`). No unique, verifiable source IDs exist. |
| **GF-05** | K-shaped economy: buy profit-expansion segments | Tactic | 8 | 8 | **Zero** - Frequency table claims 8, but relies on deprecated batch IDs (`YT-2026-002`, `CP-2026-001`, `CP-2026-002`). |
| **P-AsymmetryLoss** | The Asymmetry of Loss | Parent | N/A | N/A | **Low** - Manufactured for the MVP schema. Does not exist in the Frequency Table. |
| **RM-02** | Avoid concentration risk | Constraint | 8 | 8 | **Zero** - Frequency table claims 8, but relies on deprecated batch IDs (`YT-2026-001`, `CP-2026-001`, `CP-2026-002`). |
| **RM-03** | NEVER sell naked options | Constraint | 7 | 7 | **Zero** - Frequency table claims 7 (promoted via manual override logic in log), but relies entirely on `YT-2026-001`, `CP-2026-001`. |

> **Conclusion on Inventory:** The MVP catalog consists of 6 principles. 2 are purely structural inventions. 4 are drawn from the Frequency Table. Of those 4, **100% of their claimed evidence is unverifiable** due to the batch-ID data corruption in the Source Database.
