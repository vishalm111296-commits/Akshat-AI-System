# Principle Quality Audit

## Objective
Score the quality of the principles currently implemented in the Phase 2 MVP (`core_catalog.json`) on a scale of 0-10 based on Specificity, Reusability, Actionability, and Evidence Support.

---

### 1. P-EarningsGravity (Earnings Gravity)
*   **Specificity:** 3/10 (Too abstract)
*   **Reusability:** 10/10 (Applies to all equities)
*   **Actionability:** 0/10 (Cannot be executed directly)
*   **Evidence Support:** 0/10 (Structurally manufactured; not in Frequency Table)
*   **Overall Score:** **3.25/10**

### 2. SS-03 (Prefer margin expansion)
*   **Specificity:** 7/10 (Clear metric to track)
*   **Reusability:** 10/10 (Applies globally)
*   **Actionability:** 8/10 (Can be programmed into a screener)
*   **Evidence Support:** 0/10 (Relies on deprecated batch IDs)
*   **Overall Score:** **6.25/10**

### 3. GF-05 (K-shaped economy: buy profit-expansion segments)
*   **Specificity:** 6/10 (Requires secondary deduction to define what "profit-expansion" is currently)
*   **Reusability:** 10/10 (Macro-agnostic)
*   **Actionability:** 4/10 (Hard to programmatically define a "K-shape" without an LLM)
*   **Evidence Support:** 0/10 (Relies on deprecated batch IDs)
*   **Overall Score:** **5.0/10**

### 4. P-AsymmetryLoss (The Asymmetry of Loss)
*   **Specificity:** 2/10 (Philosophical concept)
*   **Reusability:** 10/10 (Universal)
*   **Actionability:** 0/10 (Requires tactical child principles to execute)
*   **Evidence Support:** 0/10 (Structurally manufactured)
*   **Overall Score:** **3.0/10**

### 5. RM-02 (Avoid concentration risk)
*   **Specificity:** 4/10 (What defines "concentration"? 5%? 20%? Unclear)
*   **Reusability:** 10/10 (Universal)
*   **Actionability:** 7/10 (Can be coded as a portfolio weight limit if defined)
*   **Evidence Support:** 0/10 (Relies on deprecated batch IDs)
*   **Overall Score:** **5.25/10**

### 6. RM-03 (NEVER sell naked options)
*   **Specificity:** 10/10 (Binary, absolute rule)
*   **Reusability:** 10/10 (Universal)
*   **Actionability:** 10/10 (Can be programmed as a hard boolean blocker)
*   **Evidence Support:** 0/10 (Relies on deprecated batch IDs)
*   **Overall Score:** **7.5/10**

---

## Conclusion
The highest quality principles are the absolute tactical constraints (e.g., NEVER sell naked options). The lowest quality principles are the manufactured Parent themes, which lack actionability. However, every single principle fails on Evidence Support due to the current repository state, dragging all scores down.
