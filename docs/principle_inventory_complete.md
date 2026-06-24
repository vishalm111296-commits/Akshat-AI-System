# Principle Inventory Complete

This document lists every principle found in `knowledge/principles/core_catalog.json` and evaluates its exact schema attributes and dependencies.

---

### 1. P-EarningsGravity
* **ID:** P-EarningsGravity
* **Title:** Earnings Gravity
* **Activation Tags:** `margin_expansion`, `earnings_growth`
* **Type:** parent
* **Dependencies:** None (`parent_id` is null).
* **Related Principles:** SS-03 (Child).
* **Potential Duplicate Principles:** CP-04 (Earnings and valuation matter more than narratives - from Frequency Table).
* **Potential Conflicts:** GF-04 (GDP growth is not an investment thesis) - can conflict if GDP growth is mistakenly mapped to earnings growth.

### 2. SS-03
* **ID:** SS-03
* **Title:** Prefer margin expansion
* **Activation Tags:** `margin_expansion`, `pricing_power`
* **Type:** child
* **Dependencies:** P-EarningsGravity (`parent_id`).
* **Related Principles:** GF-05 (Child Tactic).
* **Potential Duplicate Principles:** GF-05 (Heavy overlap in execution).
* **Potential Conflicts:** SS-02 (Compare price CAGR to earnings CAGR) - A stock can have margin expansion but still be drastically overpriced.

### 3. GF-05
* **ID:** GF-05
* **Title:** K-shaped economy: buy profit-expansion segments
* **Activation Tags:** `capex_cycle`, `margin_expansion`
* **Type:** tactic
* **Dependencies:** SS-03 (`parent_id`).
* **Related Principles:** SS-03.
* **Potential Duplicate Principles:** SS-03 (They share the `margin_expansion` tag, meaning they fire simultaneously in almost all cases).
* **Potential Conflicts:** CP-01 (Diversify globally) - K-shaped targeting implies heavy concentration in luxury/top-tier beneficiaries, violating broad diversification.

### 4. P-AsymmetryLoss
* **ID:** P-AsymmetryLoss
* **Title:** The Asymmetry of Loss
* **Activation Tags:** `concentration_risk`, `leverage`, `liquidity_crisis`
* **Type:** parent
* **Dependencies:** None (`parent_id` is null).
* **Related Principles:** RM-02 (Child), RM-03 (Child).
* **Potential Duplicate Principles:** None directly.
* **Potential Conflicts:** Any high-beta growth tactic.

### 5. RM-02
* **ID:** RM-02
* **Title:** Avoid concentration risk
* **Activation Tags:** `tech_hardware`, `concentration_risk`
* **Type:** constraint
* **Dependencies:** P-AsymmetryLoss (`parent_id`).
* **Related Principles:** CP-01 (Diversify).
* **Potential Duplicate Principles:** CP-01 (Diversify across countries/asset classes is identical in spirit to avoiding concentration).
* **Potential Conflicts:** PC-06 (Build around ~20 core holdings - a 20 stock portfolio is relatively concentrated compared to an index).

### 6. RM-03
* **ID:** RM-03
* **Title:** NEVER sell naked options
* **Activation Tags:** `options_margin`, `naked_calls`, `naked_puts`
* **Type:** constraint
* **Dependencies:** P-AsymmetryLoss (`parent_id`).
* **Related Principles:** OP-01, OP-02.
* **Potential Duplicate Principles:** OP-03 (NEVER sell naked options - from Frequency Table. This is an exact 1:1 duplicate that was flagged in the previous audit but remains unfixed).
* **Potential Conflicts:** OP-04 (Treat option premium as supplemental income - if applied to non-covered assets, it violates RM-03).
