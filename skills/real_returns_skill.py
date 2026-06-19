"""
L1 — Real Returns Skill
Calculates post-tax, post-inflation, post-INR depreciation returns.
Based on Akshat Master System: 'Always measure returns in real terms.'
"""


class RealReturnsSkill:

    def calculate(self, nominal_return_pct: float,
                  inflation_pct: float = 6.0,
                  tax_rate_pct: float = 12.5,
                  inr_depreciation_pct: float = 0.0,
                  geography: str = "INDIA") -> dict:

        # Post-tax return
        post_tax = nominal_return_pct * (1 - tax_rate_pct / 100)

        # Post-inflation
        post_inflation = post_tax - inflation_pct

        # Post-INR (only relevant for India-denominated assets)
        post_inr = post_inflation - inr_depreciation_pct if geography == "INDIA" else post_inflation

        verdict = "STRONG" if post_inr > 8 else "ADEQUATE" if post_inr > 3 else "WEAK" if post_inr > 0 else "NEGATIVE"

        return {
            "nominal_return_pct": nominal_return_pct,
            "post_tax_pct": round(post_tax, 2),
            "post_inflation_pct": round(post_inflation, 2),
            "post_inr_real_pct": round(post_inr, 2),
            "verdict": verdict,
            "geography": geography,
        }
