# Dynamic Stock Selection Implementation Plan

## Overview
This document outlines the implementation plan for the Dynamic Stock Selection MVP. Following the failure of the static stock mapper, this plan details the required data sources, the exact filtering sequence, and the testing methodology needed to build the final layer of the Akshat Reasoning System.

---

## TASK 1: Live Data Source Identification

To avoid complex enterprise licensing, the MVP will utilize `yfinance` (Yahoo Finance API) as the primary data source.

| Metric | Source (`yfinance` field) | Availability | Update Frequency |
|---|---|---|---|
| **Price vs 200DMA** | `info.regularMarketPrice` vs `info.twoHundredDayAverage` | High (Most global equities) | Real-time / Daily |
| **TTM Operating Margin** | `info.operatingMargins` (compared historically via `financials`) | High | Quarterly |
| **Forward PE** | `info.forwardPE` | High | Real-time / Daily |
| **5-Year Avg PE** | Derived via historical `info.trailingPE` | Medium (Requires basic historical math) | Quarterly/Daily |
| **EPS Growth** | `info.earningsGrowth` | Medium (Analyst estimates) | Quarterly |
| **Debt-to-Equity** | `info.debtToEquity` | High | Quarterly |

---

## TASK 2: Exact Filtering Sequence

The filtering engine operates as a unidirectional funnel. A stock is dropped the moment it fails a step.

1. **Sector Input:** System receives target sectors (e.g., `["Semiconductors", "Power Generation"]`) from `2_collide.py`.
2. **Universe Generation:** Query `stock_map.json` (static universe) to fetch all ticker symbols mapped to the input sectors (e.g., `["NVDA", "INTC", "TSM"]`).
3. **API Fetch:** System bulk-downloads the 6 mandatory metrics for the universe tickers.
4. **The Parabola Filter (Momentum):** Reject if `Current Price > (200DMA * 1.3)`.
5. **The Survival Filter (Debt):** Reject if `Debt-to-Equity > 2.0`.
6. **The Profitability Filter (Moat):** Reject if `TTM Operating Margin < Previous Year Operating Margin`.
7. **The Growth Filter (Earnings):** Reject if `EPS Growth <= 0`.
8. **The Valuation Filter (Gravity):** Reject if `Forward PE > (5-Year Avg PE * 1.2)`.
9. **Final Output:** Return the surviving tickers as "Candidate Stocks".

---

## TASK 3: Test Plan (Dynamic vs. Static)

**The Methodology: The Historical Trap Test**

To prove Dynamic > Static, we must prove the Dynamic system avoids "Value Traps" and "Parabolic Traps" that the Static system blindly recommends.

1. **Setup:**
   - Define Sector: `Software & SaaS`.
   - Define Static Universe: `[MSFT, CRM, SNOW, ZOOM]`.
   - Run the Static system: It recommends all 4 equally.
2. **The "Value Trap" Test:**
   - Modify the `yfinance` mock data so `ZOOM` has negative EPS growth and compressing margins.
   - Run Dynamic System.
   - **Pass Criteria:** `ZOOM` is rejected at Step 6/7.
3. **The "Parabolic Trap" Test:**
   - Modify the `yfinance` mock data so `SNOW` is trading at 200x Forward PE and 1.8x its 200DMA.
   - Run Dynamic System.
   - **Pass Criteria:** `SNOW` is rejected at Step 4/8.
4. **Final Proof:** If the Dynamic system outputs only `[MSFT, CRM]` while the Static system outputs all four, we have mathematically proven that Dynamic Selection mitigates risk.

---

## TASK 4: Implementation Complexity Estimates

| Component | Difficulty | Risk | Time |
|---|---|---|---|
| **API Integration (`yfinance`)** | Low | High (Yahoo Finance frequently throttles or changes undocumented API structures). | 1 Day |
| **Static Universe Mapping (`stock_map.json`)** | Low | Low (Manual data entry). | 1 Day |
| **Boolean Filter Loop Engine** | Low | Low (Standard Python `if/else` logic). | 1 Day |
| **PyTest Suite for Filtering** | Medium | Low (Requires mocking API responses to ensure stable tests). | 2 Days |

---

## TASK 5: Smallest Possible Build

**What is the smallest possible build that can generate better stock candidates than the current static mapper?**

A single Python script (`3_filter.py`) that accepts an array of ticker symbols, pings Yahoo Finance for exactly three data points (`forwardPE`, `operatingMargins`, `twoHundredDayAverage`), and executes three `if` statements to filter out egregious overvaluation, unprofitability, and parabolic charts.

Even this ultra-minimal 30-line script is infinitely superior to the static mapper because it grounds the abstract sector theory in live financial reality.

---

## FINAL VERDICT

**Is Dynamic Stock Selection the next phase?**

**NO.**

**Defense:**
While Dynamic Stock Selection *is* required to fix the bottom of the funnel, building it now violates the core principle of sequential layer validation.

As established in the `stock_selection_root_cause_analysis.md` and the `reality_gap_report.md`, the upstream layers (Macro Event → Ontology → Framework → Sector) are fundamentally broken and brittle because they rely on deterministic, hardcoded substring matching.

If we build Dynamic Stock Selection now, we are attaching a brilliant quantitative filter to a broken qualitative pipe. The system will flawlessly filter stocks for the *wrong sector*, because the ontology map misunderstood the macro event.

**The actual next phase must be:** Fixing the NLP/Ontology layer (Milestone 1 of the 12-Month Roadmap) to ensure the system correctly extracts semantic meaning from macro events. Only when we can reliably output the *correct sector* should we build the engine to output the *correct stock*.