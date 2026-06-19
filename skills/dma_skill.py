"""
L1 — DMA Skill
50/150/200 Day Moving Average zone analysis.
Based on Akshat Recent Changes: DMA-Based Accumulation Framework.
"""


class DMASkill:

    def assess_dma_position(self, current_price: float, dma_50: float,
                             dma_150: float = None, dma_200: float = None) -> dict:

        zones = []
        buy_signal = False

        if dma_200 and current_price <= dma_200 * 1.02:
            zones.append("AT_OR_NEAR_200DMA")
            buy_signal = True
        if dma_150 and current_price <= dma_150 * 1.02:
            zones.append("AT_OR_NEAR_150DMA")
            buy_signal = True
        if current_price <= dma_50 * 1.02:
            zones.append("AT_OR_NEAR_50DMA")

        if current_price > (dma_200 or dma_50) * 1.20:
            zones.append("EXTENDED_ABOVE_DMA")
            buy_signal = False

        return {
            "current_price": current_price,
            "dma_50": dma_50,
            "dma_150": dma_150,
            "dma_200": dma_200,
            "zones": zones,
            "accumulation_signal": buy_signal,
            "verdict": "ACCUMULATE" if buy_signal else "WAIT_FOR_DMA" if not zones else "MONITOR",
        }
