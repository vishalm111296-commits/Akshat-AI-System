"""
L1 — Earnings Skill
Analyses EPS growth, operating profit growth, and margin direction.
Based on Akshat Master System Section 3.3.
"""


class EarningsSkill:
    """
    Inputs: eps_growth_pct, op_margin_current, op_margin_prev,
            revenue_growth_pct, eps_vs_estimate_pct
    Output: earnings_verdict dict
    """

    def assess(self, eps_growth_pct: float, op_margin_current: float,
               op_margin_prev: float, revenue_growth_pct: float = None,
               eps_vs_estimate_pct: float = None) -> dict:

        flags = []
        thesis_status = "INTACT"

        # Rule 1: EPS growth direction
        if eps_growth_pct < 0:
            flags.append(f"EPS_DECLINING: {eps_growth_pct:.1f}%")
            thesis_status = "WEAKENED"
        elif eps_growth_pct < 5:
            flags.append(f"EPS_WEAK: {eps_growth_pct:.1f}%")
        else:
            flags.append(f"EPS_HEALTHY: {eps_growth_pct:.1f}%")

        # Rule 2: Operating margin direction
        margin_delta = op_margin_current - op_margin_prev
        if margin_delta < -2:
            flags.append(f"MARGIN_COMPRESSION: {margin_delta:.1f}pp")
            thesis_status = "WEAKENED" if thesis_status == "INTACT" else "THESIS_BROKEN"
        elif margin_delta > 0:
            flags.append(f"MARGIN_EXPANDING: +{margin_delta:.1f}pp")

        # Rule 3: Revenue without profit check
        if revenue_growth_pct and revenue_growth_pct > 20 and eps_growth_pct < 0:
            flags.append("REVENUE_WITHOUT_PROFIT: Growth narrative without earnings")
            thesis_status = "WEAKENED"

        # Rule 4: Earnings surprise
        if eps_vs_estimate_pct is not None:
            if eps_vs_estimate_pct < -10:
                flags.append(f"EARNINGS_MISS: {eps_vs_estimate_pct:.1f}% below estimate")
                thesis_status = "THESIS_BROKEN" if thesis_status == "THESIS_BROKEN" else "WEAKENED"
            elif eps_vs_estimate_pct > 5:
                flags.append(f"EARNINGS_BEAT: +{eps_vs_estimate_pct:.1f}%")

        return {
            "thesis_status": thesis_status,
            "eps_growth_pct": eps_growth_pct,
            "margin_delta": margin_delta,
            "flags": flags,
        }

    def action(self, result: dict) -> str:
        mapping = {
            "INTACT": "HOLD or ACCUMULATE on dips",
            "WEAKENED": "REDUCE position or WAIT for next quarter",
            "THESIS_BROKEN": "EXIT or materially reduce position",
        }
        return mapping.get(result["thesis_status"], "REVIEW")
