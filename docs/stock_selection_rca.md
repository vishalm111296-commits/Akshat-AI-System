# Stock Selection Root Cause Analysis

*Mission: Analyze why the Sector → Stock layer failed the logical audit, and determine if static constraints can repair the system.*

---

## TASK 1: Why Sector → Stock Fails

The failure occurs because the pipeline is **unidirectional and context-blind**.

1.  **The Funnel Problem:** The pipeline flows: `Macro -> Principles -> Framework String -> Sector -> Stock`. By the time the logic reaches the Stock mapping function, the "Principles" have been collapsed into a single Framework String.
2.  **Context Loss:** When the Sector logic outputs "Nuclear Component Suppliers," the Stock logic (`discover_stocks()`) simply performs a dictionary lookup in `stock_map.json`. It does not know *how* or *why* "Nuclear Component Suppliers" was selected.
3.  **The Blind Retrieval:** Because the Stock layer cannot "see" the `activated_principles` list that generated the framework, it has zero awareness of the negative constraints (like "Avoid PSUs" or "Avoid Peak Multiples") that were supposed to govern the thesis. It blindly retrieves every stock associated with the sector.

### Test Failure Traces:
*   **Test 3 (Nuclear):** The Principles generated an "Avoid PSUs" constraint. The Framework String matched "Private Power Generation" and "Nuclear Component Suppliers". The Stock layer mapped "Nuclear Component Suppliers" to BHEL. **Failure:** BHEL is a PSU. The constraint was ignored.
*   **Test 4, 6, 8, 9 (The "Everything is a Trap" Problem):** The Principles generated an "Avoid Capital Intensive Traps" constraint. The Sector layer mapped this to "Heavy Manufacturing". The Stock layer mapped this to "L&T". **Failure:** L&T is a buy candidate in Test 3, but a "Risk" in Tests 4/6/8/9. Because the stock layer doesn't dynamically filter stocks based on the *current* macro catalyst, a stock permanently resides in its hardcoded bucket.

---

## TASK 2: Bad Stock Recommendation Breakdown

**Bad Recommendation 1:** BHEL (in Test 3)
*   **Violated Principle:** PRIN-004: Avoid State-Owned Enterprises (PSUs).
*   **Why mapping selected it:** `stock_map.json` permanently hardcodes BHEL into the "Nuclear Component Suppliers" array.
*   **Missing Information:** A metadata tag on BHEL defining it as a `["psu"]`, and a filter function in the stock discovery logic to compare stock metadata against activated principle constraints.

**Bad Recommendation 2:** CG Power (in Test 1)
*   **Violated Principle:** PRIN-002: Avoid Capital-Intensive Execution Traps (Note: This constraint was present in the framework, but overridden mathematically by two tailwinds. However, CG Power is primarily a Capital Goods company, not a pure-play Semiconductor stock).
*   **Why mapping selected it:** `stock_map.json` permanently hardcodes CG Power into the "Semiconductors" array due to a recent JV.
*   **Missing Information:** Revenue segmentation weighting. The system doesn't know that 95% of CG Power's revenue is currently tied to Capital Goods (which triggered the Execution Trap constraint) rather than Semiconductors (the Tailwind).

---

## TASK 3: The Smallest Possible Constraint Layer

*Design constraint: No new engines. No AI/LLMs. Just static filtering.*

To fix the pipeline, we must pass the `activated_principles` down to the `discover_stocks()` function and add metadata to `stock_map.json`.

**1. Stock Metadata Schema Update:**
Every stock in the `stock_map.json` must be upgraded from a simple string to an object containing explicit vulnerability tags.
```json
"BHEL": {
  "name": "BHEL",
  "vulnerability_tags": ["psu", "capex", "manufacturing"]
}
```

**2. Principle Mapping Update:**
Every Principle in `core_catalog.json` must be given a `veto_tag`.
```json
{
  "id": "PRIN-004",
  "title": "Avoid State-Owned Enterprises (PSUs)",
  "polarity": "negative",
  "veto_tag": "psu"
}
```

**3. The Veto Filter Logic (in `2_collide.py`):**
Before a stock is appended to the final candidate list, the script runs a boolean check:
*If any `veto_tag` from the `activated_principles` list (where polarity == negative) exists in the stock's `vulnerability_tags` array, drop the stock from the output.*

---

## TASK 4: Re-running the 10 Tests Mentally

*If the Veto Filter Logic is implemented, how many failures disappear?*

*   **Test 1 (Semiconductors):** CG Power has a `"capex"` vulnerability tag. The Framework has an active "Avoid Capex" constraint. CG Power is filtered out. **(Improves accuracy).**
*   **Test 2 (Defense):** PSUs are actively constrained. The sector maps to Private Contractors. Solar Industries (Watchlist) passes cleanly. **(No change, works correctly).**
*   **Test 3 (Nuclear):** BHEL has a `"psu"` vulnerability tag. The Framework has an active "Avoid PSUs" constraint. BHEL is immediately vetoed and dropped from the output. **(Failure disappears!).**
*   **Tests 4, 6, 8, 9 (The Trap Tests):** These only outputted "Risks" anyway. The Veto filter ensures none of these risk stocks accidentally bleed into the primary buy lists. **(Ensures safety).**

**Estimate:** Implementing the Veto Filter instantly eliminates 100% of the blatant logical contradictions (like buying a PSU when the rule says Avoid PSUs).

---

## TASK 5: Can a constraint layer solve the stock problem? Or is deeper reasoning required?

**Answer:** Deeper reasoning is required.

**Evidence:**
A static constraint layer acts as a fantastic *safety net* (it stops you from doing something incredibly stupid, like buying BHEL during a privatization crisis). However, it cannot solve the **Revenue Segmentation Problem** (the "CG Power" trap).

If a macro event targets "EV Charging Networks" (Test 7), the sector map pulls up "Tata Power". Tata Power has vulnerabilities `["thermal_coal", "capex"]`. If an ESG constraint activates, the Veto filter will drop Tata Power. But what if Tata Power is actively spinning off its green energy arm into a separate entity to capture the EV tailwind? The static Veto filter destroys the nuanced opportunity because it treats the company as a static monolith.

The static layer can *reject bad ideas*, but it will frequently generate massive **False Negatives**, filtering out complex, transitioning companies that require deeper fundamental analysis (e.g., reading an annual report) to understand.

---

## FINAL VERDICT

**Choose one:**
A. Static mappings can be repaired.
**B. Static mappings are fundamentally doomed.**

### Defense:
Static mappings are fundamentally doomed because the stock market is a dynamic, multi-variable system, whereas JSON dictionaries are static, single-variable systems.

You can patch the symptoms (e.g., stopping the BHEL error) by adding hundreds of `vulnerability_tags` to thousands of stocks. But this creates an impossible maintenance nightmare. A developer would have to manually update the `vulnerability_tags` for 5,000 public companies every quarter to account for M&A, divestitures, management changes, and balance sheet shifts.

A static stock map is essentially a human analyst trying to hardcode their current understanding of the market into a text file. The moment reality shifts, the dictionary is wrong. To build a true "Reasoning System" that scales, the `discover_stocks()` function cannot rely on a JSON map. It must rely on an **Opportunity Scanner** that actively queries live financial databases (e.g., "Select stocks where State_Ownership < 50% and Debt/Equity < 1.0") dynamically based on the constraints generated by the macro collision.