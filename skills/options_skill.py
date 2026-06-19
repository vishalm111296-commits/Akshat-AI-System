"""
L1 — Options Skill
Enforces Akshat's options rules: only covered calls and cash-secured puts.
Based on Akshat Master System Section 3.5 and 4.5.
NAKED OPTIONS ARE BLOCKED.
"""


class OptionsSkill:

    ALLOWED_STRATEGIES = ["COVERED_CALL", "CASH_SECURED_PUT"]

    def evaluate(self, strategy: str, owns_underlying: bool = False,
                 has_cash: bool = False, strike_based_on_intent: bool = True,
                 happy_with_assignment: bool = True) -> dict:

        # Hard block on naked options
        if strategy.upper() not in self.ALLOWED_STRATEGIES:
            return {
                "blocked": True,
                "reason": f"NAKED_OPTIONS_BLOCKED: '{strategy}' is not permitted. "
                          f"Only COVERED_CALL or CASH_SECURED_PUT allowed.",
                "action": "DO_NOT_EXECUTE",
            }

        issues = []

        if strategy.upper() == "COVERED_CALL" and not owns_underlying:
            issues.append("MUST_OWN_SHARES_FIRST: Cannot sell covered call without holding underlying.")

        if strategy.upper() == "CASH_SECURED_PUT" and not has_cash:
            issues.append("MUST_HOLD_CASH_FIRST: Cannot sell CSP without cash secured.")

        if not strike_based_on_intent:
            issues.append("STRIKE_NOT_INTENT_BASED: Strike must reflect where you actually want to buy/sell, not premium greed.")

        if not happy_with_assignment:
            issues.append("ASSIGNMENT_RISK: Only trade options where assignment is acceptable.")

        return {
            "blocked": len(issues) > 0,
            "strategy": strategy,
            "issues": issues,
            "action": "DO_NOT_EXECUTE" if issues else "PERMITTED",
        }
