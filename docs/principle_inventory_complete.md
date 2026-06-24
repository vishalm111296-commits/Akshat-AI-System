# Complete Principle Inventory

*Based exclusively on `knowledge/principles/core_catalog.json` (7 principles).*

---

### PRIN-001
*   **Title:** Follow Government Subsidies
*   **Activation Tags:** `["incentive", "government", "subsidy", "pli"]`
*   **Type:** Tailwind (Positive)
*   **Dependencies:** None explicit in schema. Conceptually depends on state fiscal capacity.
*   **Related Principles:** PRIN-005 (Follow Monopsony Buyers), PRIN-004 (Avoid PSUs - related by Government entity).
*   **Potential Duplicate Principles:** PRIN-005.
*   **Potential Conflicts:** PRIN-002 (Subsidies often target Heavy Manufacturing, triggering the Capex trap).

### PRIN-002
*   **Title:** Avoid Capital-Intensive Execution Traps
*   **Activation Tags:** `["capex", "manufacturing", "infrastructure"]`
*   **Type:** Constraint (Negative)
*   **Dependencies:** None.
*   **Related Principles:** PRIN-007 (Sunset Industries often require high maintenance capex).
*   **Potential Duplicate Principles:** None.
*   **Potential Conflicts:** PRIN-001 (Subsidies), PRIN-006 (Demographics require infrastructure).

### PRIN-003
*   **Title:** Follow Geopolitical Supply-Chain Shifts
*   **Activation Tags:** `["geopolitics", "supply_chain", "china_plus_one", "indigenization"]`
*   **Type:** Tailwind (Positive)
*   **Dependencies:** None.
*   **Related Principles:** PRIN-001 (Subsidies often follow geopolitical shifts).
*   **Potential Duplicate Principles:** None.
*   **Potential Conflicts:** PRIN-002 (Supply chain shifts require massive physical capex).

### PRIN-004
*   **Title:** Avoid State-Owned Enterprises (PSUs)
*   **Activation Tags:** `["psu", "government"]`
*   **Type:** Constraint (Negative)
*   **Dependencies:** None.
*   **Related Principles:** PRIN-001, PRIN-005.
*   **Potential Duplicate Principles:** None.
*   **Potential Conflicts:** PRIN-005 (Monopsony buyers are usually the State, and state-owned entities often fulfill those orders, creating a logical collision).

### PRIN-005
*   **Title:** Follow Monopsony Buyers
*   **Activation Tags:** `["monopsony", "order_book"]`
*   **Type:** Tailwind (Positive)
*   **Dependencies:** None.
*   **Related Principles:** PRIN-001, PRIN-004.
*   **Potential Duplicate Principles:** PRIN-001 (State-sponsored capital allocation).
*   **Potential Conflicts:** PRIN-004 (Vetoes the exact entities that benefit from Monopsony environments).

### PRIN-006
*   **Title:** Follow Demographic Destiny
*   **Activation Tags:** `["demographics", "necessity"]`
*   **Type:** Tailwind (Positive)
*   **Dependencies:** None.
*   **Related Principles:** None.
*   **Potential Duplicate Principles:** None.
*   **Potential Conflicts:** PRIN-002 (Hospitals/Real Estate require heavy capex but have demographic tailwinds).

### PRIN-007
*   **Title:** Avoid Sunset / ESG Restricted Industries
*   **Activation Tags:** `["sunset"]`
*   **Type:** Constraint (Negative)
*   **Dependencies:** None.
*   **Related Principles:** None.
*   **Potential Duplicate Principles:** None.
*   **Potential Conflicts:** PRIN-006 (Necessity overrides ESG in power crises).