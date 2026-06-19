"""
L1 — Geographic Filter Skill
Compares investment opportunities across geographies.
Based on Akshat Master System Section 3.4.
"""


class GeographicFilterSkill:
    """
    Akshat's default comparison: US vs India vs Global.
    US tech = structural compounder.
    India = rotation/trading market, valuation-sensitive.
    """

    GEOGRAPHY_PROFILES = {
        "US": {
            "type": "STRUCTURAL_COMPOUNDER",
            "currency": "USD",
            "profit_pool": "DEEP",
            "capital_market": "MATURE",
            "default_bias": "STRUCTURAL_BUY_ON_DIPS",
        },
        "INDIA": {
            "type": "ROTATION_TRADE_MARKET",
            "currency": "INR",
            "profit_pool": "SEGMENT_SPECIFIC",
            "capital_market": "DEVELOPING",
            "default_bias": "SELECTIVE_VALUATION_SENSITIVE",
        },
        "GLOBAL_EM": {
            "type": "TACTICAL_OPPORTUNITY",
            "currency": "MIXED",
            "profit_pool": "VARIABLE",
            "capital_market": "VARIABLE",
            "default_bias": "OPPORTUNISTIC",
        },
    }

    def compare(self, primary_geo: str, alternative_geo: str = "US") -> dict:
        primary = self.GEOGRAPHY_PROFILES.get(primary_geo.upper(), {})
        alternative = self.GEOGRAPHY_PROFILES.get(alternative_geo.upper(), {})

        return {
            "primary": {"geography": primary_geo, **primary},
            "alternative": {"geography": alternative_geo, **alternative},
            "recommendation": self._recommend(primary, alternative),
        }

    def _recommend(self, primary: dict, alternative: dict) -> str:
        if primary.get("type") == "STRUCTURAL_COMPOUNDER":
            return "PREFER_PRIMARY"
        elif alternative.get("type") == "STRUCTURAL_COMPOUNDER":
            return "COMPARE_CAREFULLY_AGAINST_ALTERNATIVE"
        return "EVALUATE_ON_VALUATION"

    def india_dollar_check(self, local_return_pct: float,
                           inr_depreciation_pct: float) -> dict:
        """Convert Indian returns to dollar terms."""
        dollar_return = local_return_pct - inr_depreciation_pct
        verdict = "ADEQUATE" if dollar_return > 8 else "WEAK" if dollar_return > 3 else "POOR"
        return {
            "local_return_pct": local_return_pct,
            "inr_depreciation_pct": inr_depreciation_pct,
            "dollar_adjusted_return_pct": dollar_return,
            "verdict": verdict,
        }
