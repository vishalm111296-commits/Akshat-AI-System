"""
L1 — Valuation Skill
Assesses whether an asset is fairly priced relative to earnings and history.
Based on Akshat Master System Section 3.3 and 4.1.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operating_system.constants import PE_EXTREME_WARNING, PRICE_EARNINGS_CAGR_DIVERGENCE


class ValuationSkill:
    """
    Inputs: current_pe, historical_avg_pe, price_cagr_3y, eps_cagr_3y,
            forward_pe, sector_pe
    Output: valuation_verdict dict
    """

    def assess(self, current_pe: float, historical_avg_pe: float,
               price_cagr_3y: float = None, eps_cagr_3y: float = None,
               forward_pe: float = None) -> dict:

        flags = []
        score = 0  # Higher = more overvalued

        # Rule 1: PE vs extreme threshold
        if current_pe > PE_EXTREME_WARNING:
            flags.append(f"EXTREME_PE: {current_pe} exceeds danger zone {PE_EXTREME_WARNING}")
            score += 3

        # Rule 2: PE vs historical average
        if historical_avg_pe and current_pe > (historical_avg_pe * 1.5):
            flags.append(f"STRETCHED_PE: Current {current_pe} is >1.5x historical avg {historical_avg_pe}")
            score += 2
        elif historical_avg_pe and current_pe <= historical_avg_pe:
            flags.append("FAIR_OR_BELOW_HIST_AVG")
            score -= 1

        # Rule 3: Price CAGR vs EPS CAGR divergence
        if price_cagr_3y and eps_cagr_3y and eps_cagr_3y > 0:
            ratio = price_cagr_3y / eps_cagr_3y
            if ratio > PRICE_EARNINGS_CAGR_DIVERGENCE:
                flags.append(f"PRICE_RUNS_AHEAD_OF_EARNINGS: ratio={ratio:.2f}")
                score += 2

        # Rule 4: Forward PE check
        if forward_pe and forward_pe > PE_EXTREME_WARNING:
            flags.append(f"HIGH_FORWARD_PE: {forward_pe}")
            score += 1

        verdict = "AVOID" if score >= 4 else "CAUTION" if score >= 2 else "ACCEPTABLE" if score >= 0 else "ATTRACTIVE"

        return {
            "verdict": verdict,
            "score": score,
            "flags": flags,
            "current_pe": current_pe,
            "historical_avg_pe": historical_avg_pe,
        }

    def summarise(self, result: dict) -> str:
        return f"Valuation: {result['verdict']} | PE={result['current_pe']} | Flags: {'; '.join(result['flags']) or 'None'}"
