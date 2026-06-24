---
name: Options Analysis
description: Execute covered call or cash-secured put strategies for income.
triggers:
  - options
  - covered call
  - cash-secured put
  - derivatives
  - premium
load_with: options_skill.py
---

# Skill: Options Analysis

*Layer: L1 — Core Skills*

## Purpose
Execute covered call or cash-secured put strategies as supplemental income tools, strictly within Akshat's options framework.

## Hard Gates (Check Before Anything Else)

1. **Covered Call Gate**: Do you already own the underlying shares? If NO → STOP. Do not proceed.
2. **Cash-Secured Put Gate**: Do you hold the full cash required to buy shares at the strike price? If NO → STOP. Do not proceed.
3. **Naked Option Check**: If neither condition above is met → REFUSE. State: *"Naked options violate core risk management principles and are not analyzed in this system."*

## Covered Call Execution

1. Identify the zone where you would **happily trim** the position anyway
2. Set strike price at or above that zone
3. Select near-term expiry (monthly preferred for income consistency)
4. Calculate: premium received as % of current stock value
5. Confirm: premium income is small and safe, not suspiciously large
6. Assignment scenario: "If assigned, I sell at [strike]. Is this acceptable?"

## Cash-Secured Put Execution

1. Identify the price zone where you would **happily buy** the stock
2. Set strike price at or near that zone
3. Ensure cash = strike price × 100 shares (per contract) is held in account
4. Calculate: premium received + effective buy price if assigned
5. Confirm: assignment is welcomed, not feared

## Output Format
1. Strategy Type (CC / CSP)
2. Gate Check Result (Passed / Failed)
3. Strike Price Rationale
4. Premium Estimate
5. Assignment Scenario (acceptable/unacceptable)
6. Income as % of Position Value
7. Risk Summary
