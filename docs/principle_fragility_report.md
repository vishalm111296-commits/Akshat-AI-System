# Principle Fragility Report

This document audits the blast radius if any of the 6 core principles implemented in the MVP are fundamentally wrong, poorly mapped, or obsolete.

---

### P-EarningsGravity
*   **What happens if it is wrong?** The system will fail to understand that valuation matters.
*   **Would the system function?** Yes. The system routing engine doesn't mathematically care if parents exist; it just prints strings.
*   **Future phases dependent on it:** Stock Selection (Valuation constraints).
*   **Blast radius:** The entire growth portfolio becomes a value trap.
*   **Score:** **Critical**

### SS-03 (Prefer margin expansion)
*   **What happens if it is wrong?** The system will aggressively recommend companies whose margins are artificially bloated due to one-time accounting tricks or cyclical commodity peaks.
*   **Would the system function?** Yes.
*   **Future phases dependent on it:** Sector mapping.
*   **Blast radius:** Will cause the sector mapper to recommend cyclical "Risk" sectors at the top of the market cycle.
*   **Score:** **High**

### GF-05 (K-shaped economy: buy profit-expansion segments)
*   **What happens if it is wrong?** If government policy structurally shifts to wealth redistribution (e.g., universal basic income, massive corporate taxes), the K-shape reverses. The system will continue to blindly recommend luxury auto and premium retail while mass-market FMCG explodes in value.
*   **Would the system function?** Yes. It will functionally output the exact wrong answer.
*   **Future phases dependent on it:** Trend Discovery, Sector Discovery.
*   **Blast radius:** Wipes out the consumer discretionary portfolio.
*   **Score:** **Critical**

### P-AsymmetryLoss
*   **What happens if it is wrong?** (Philosophically unlikely, but if misapplied): The system becomes overly defensive, moving to cash during minor V-shaped liquidity panics, missing decade-defining compounding runs.
*   **Would the system function?** Yes.
*   **Future phases dependent on it:** Portfolio Construction (Barbell weightings).
*   **Blast radius:** Severe underperformance against the benchmark index (opportunity cost).
*   **Score:** **Medium**

### RM-02 (Avoid concentration risk)
*   **What happens if it is wrong?** If avoiding concentration risk is hardcoded as a blocker to the "Barbell Strategy" (which requires heavy concentration in a few asymmetrical AI bets), the system will force broad diversification, destroying alpha.
*   **Would the system function?** Yes, but it would suppress high-conviction tactics.
*   **Future phases dependent on it:** Framework Conflict Resolution.
*   **Blast radius:** Complete dilution of returns.
*   **Score:** **High**

### RM-03 (NEVER sell naked options)
*   **What happens if it is wrong?** If a user employs advanced portfolio margin or dynamic hedging where selling naked options is mathematically safe within a larger delta-neutral book, this hard constraint will falsely block valid trades.
*   **Would the system function?** Yes.
*   **Future phases dependent on it:** The "Yield/Options" engine (Phase 7+).
*   **Blast radius:** Minimal for long-term equity compounding; limits supplemental yield.
*   **Score:** **Low**
