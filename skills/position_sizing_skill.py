"""
L1 — Position Sizing Skill
Enforces Akshat's portfolio weight rules.
Based on Akshat Master System Section 5.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operating_system.constants import (
    MAX_SINGLE_STOCK_WEIGHT, MAX_HIGH_RISK_WEIGHT,
    MIN_LIQUID_RATIO, MAX_ILLIQUID_RATIO, MIN_DRY_POWDER
)


class PositionSizingSkill:

    def check_position(self, proposed_weight: float,
                       is_high_risk: bool = False) -> dict:
        max_allowed = MAX_HIGH_RISK_WEIGHT if is_high_risk else MAX_SINGLE_STOCK_WEIGHT
        flag = "OVER_WEIGHT" if proposed_weight > max_allowed else "OK"
        return {
            "proposed_weight": proposed_weight,
            "max_allowed": max_allowed,
            "flag": flag,
            "recommended": min(proposed_weight, max_allowed),
        }

    def check_portfolio_balance(self, liquid_ratio: float,
                                illiquid_ratio: float,
                                dry_powder_ratio: float) -> dict:
        issues = []
        if liquid_ratio < MIN_LIQUID_RATIO:
            issues.append(f"INSUFFICIENT_LIQUID: {liquid_ratio:.0%} < {MIN_LIQUID_RATIO:.0%} target")
        if illiquid_ratio > MAX_ILLIQUID_RATIO:
            issues.append(f"TOO_MUCH_ILLIQUID: {illiquid_ratio:.0%} > {MAX_ILLIQUID_RATIO:.0%} max")
        if dry_powder_ratio < MIN_DRY_POWDER:
            issues.append(f"LOW_DRY_POWDER: {dry_powder_ratio:.0%} < {MIN_DRY_POWDER:.0%} min")

        return {
            "liquid_ratio": liquid_ratio,
            "illiquid_ratio": illiquid_ratio,
            "dry_powder_ratio": dry_powder_ratio,
            "issues": issues,
            "status": "REBALANCE_NEEDED" if issues else "BALANCED",
        }
