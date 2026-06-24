# Evidence Coverage Audit

*Review of the 7 existing principles in the repository to determine their evidence backing.*

## 1. PRIN-001: Follow Government Subsidies
*   **Status:** **Unsupported**
*   **Exact Gaps:** The system requires `knowledge/principles/principle_evidence_map.md` to map principles to raw sources. This file was created as an empty placeholder in Phase 1, but was never populated with `[TYPE]-[YYYY-MM-DD]-[SHORT_SLUG].txt` references. There is no proof Akshat actually relies on this principle.

## 2. PRIN-002: Avoid Capital-Intensive Execution Traps
*   **Status:** **Unsupported**
*   **Exact Gaps:** No timestamps, no quotes, no file links. We lack the specific definition of what constitutes an "execution trap" (e.g., is >10% Debt/Equity the trigger?).

## 3. PRIN-003: Follow Geopolitical Supply-Chain Shifts
*   **Status:** **Unsupported**
*   **Exact Gaps:** No specific source mapping. The repository does not define the difference between a minor geopolitical event and a structural supply-chain shift using historical Akshat commentary.

## 4. PRIN-004: Avoid State-Owned Enterprises (PSUs)
*   **Status:** **Unsupported**
*   **Exact Gaps:** No evidence mapped. Furthermore, the repository's `core_catalog.json` claims "outside of strict monopolies", but no evidence is provided to substantiate when Akshat grants this exception.

## 5. PRIN-005: Follow Monopsony Buyers
*   **Status:** **Unsupported**
*   **Exact Gaps:** No source file references. It is unknown if Akshat applies this globally or strictly to the Indian Defense sector.

## 6. PRIN-006: Follow Demographic Destiny
*   **Status:** **Unsupported**
*   **Exact Gaps:** Zero evidence. The difference between "demographics" (slow-moving) and an actionable macro catalyst is completely unmapped.

## 7. PRIN-007: Avoid Sunset / ESG Restricted Industries
*   **Status:** **Unsupported**
*   **Exact Gaps:** Zero source quotes. The timeline for what makes an industry "sunset" is not backed by any extracted transcript data.

---

### Audit Conclusion
The repository currently functions entirely on **Assumed Principles**. The developer hardcoded 7 common-sense investing heuristics to test the routing logic of `2_collide.py`, completely bypassing the `1_extract.py` logic. Because the Principle Evidence Map was never populated, **100% of the principles are Unsupported.**