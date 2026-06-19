"""
L1 — Macro Skill
Tracks global liquidity, interest rates, INR trend, FII flows.
Based on Akshat Master System Section 3.8.
"""


class MacroSkill:
    """
    Inputs: liquidity_trend, rate_direction, inr_1y_depreciation_pct,
            fii_flows_90d, panic_type
    Output: macro_dashboard dict
    """

    LIQUIDITY_OPTIONS = ["EXPANDING", "NEUTRAL", "CONTRACTING"]
    RATE_OPTIONS = ["CUTTING", "NEUTRAL", "HIKING"]
    PANIC_OPTIONS = ["V_SHAPED", "W_SHAPED", "STRUCTURAL", "NONE"]

    def assess(self, liquidity_trend: str, rate_direction: str,
               inr_1y_depreciation_pct: float, fii_flows_90d: str,
               panic_type: str = "NONE") -> dict:

        signals = {}
        flags = []

        # Global liquidity signal
        signals["liquidity"] = {
            "EXPANDING": "BULLISH",
            "NEUTRAL": "NEUTRAL",
            "CONTRACTING": "BEARISH"
        }.get(liquidity_trend, "UNKNOWN")

        # Rate direction signal
        signals["rates"] = {
            "CUTTING": "BULLISH_FOR_EQUITIES",
            "NEUTRAL": "NEUTRAL",
            "HIKING": "BEARISH_FOR_GROWTH_STOCKS"
        }.get(rate_direction, "UNKNOWN")

        # INR depreciation risk
        if inr_1y_depreciation_pct > 5:
            flags.append(f"INR_HIGH_DEPRECIATION: {inr_1y_depreciation_pct:.1f}% in 12m")
            signals["inr"] = "BEARISH_FOR_INDIA"
        elif inr_1y_depreciation_pct > 2:
            signals["inr"] = "CAUTION"
        else:
            signals["inr"] = "STABLE"

        # FII flows
        signals["fii"] = fii_flows_90d  # e.g. "OUTFLOW", "INFLOW", "NEUTRAL"

        # Panic classification
        if panic_type == "V_SHAPED":
            flags.append("BUYING_OPPORTUNITY: V-shaped panic, likely temporary")
        elif panic_type == "STRUCTURAL":
            flags.append("CAUTION: Structural deterioration, not a simple dip")

        # Overall macro stance
        bullish_count = sum(1 for v in signals.values() if "BULLISH" in str(v))
        bearish_count = sum(1 for v in signals.values() if "BEARISH" in str(v))

        if bearish_count > bullish_count:
            overall = "RISK_OFF"
        elif bullish_count > bearish_count:
            overall = "RISK_ON"
        else:
            overall = "NEUTRAL"

        return {
            "overall": overall,
            "signals": signals,
            "flags": flags,
            "panic_type": panic_type,
        }
