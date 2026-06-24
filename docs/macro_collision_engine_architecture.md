# Macro-to-Principle Collision Engine

## 1. Goal & Vision

The overarching system currently operates as a **Parsing Architecture**: it waits for human commentary (`raw_sources`) and backward-engineers the reasoning. The **Macro-to-Principle Collision Engine** transforms the system into a **Generative Reasoning Architecture**.

It shifts the paradigm from:
*Content → Principle → Framework*
To:
*Macro Change + Core Principle Collision → Synthetic Framework Generation → Opportunity Discovery*

By independently combining hard macro data with established mental models, the system can front-run the human analyst and proactively detect the next major market narrative.

---

## 2. Inputs

The engine ingests structured, real-world data (independent of Akshat's commentary) across five core vectors:

1.  **Policy Changes:** Central bank rate decisions, fiscal deficit targets, import/export embargo lists, subsidy (PLI) announcements.
2.  **Capex Changes:** S&P 500 top 10 trailing/forward capital expenditure guidance, global supply chain FDI routing.
3.  **Demographic Changes:** Median age curves, urbanization rates, labor force participation rates.
4.  **Technological Changes:** S-curve adoption rates of new platforms, semiconductor fab utilization, compute cost curves.
5.  **Regulatory Changes:** Sector-specific price caps, antitrust rulings, carbon tax implementations.

---

## 3. Principle Activation Logic

When new Macro data enters the system, the engine must decide which of the hundreds of Core Principles in the `principle_catalog.md` should "wake up."

**Activation is triggered by Semantic Tagging and Threshold Breaches:**

*   *Step 1: Metric Mapping.* Every Core Principle is tagged with mathematical proxy metrics. (e.g., The Principle "Follow Government Incentives" is mapped to the `Subsidy_YoY_Growth` and `Import_Tariff_Index` metrics).
*   *Step 2: The Breach.* When an incoming Macro Input breaches a predefined historical standard deviation (e.g., US Hyperscaler Capex jumps 30% YoY), the engine queries the catalog.
*   *Step 3: Activation.* The Principle "Follow secular Capex cycles" is mathematically Activated. Similarly, if interest rates spike, the Principle "Avoid capital-intensive, long-gestation assets" is Activated.

---

## 4. Collision Logic

A single activated Principle is not a framework; it is just an observation. A framework is born when multiple, often conflicting, Principles collide around a specific macro event.

**The Collision Matrix:**
The engine plots Activated Principles against the specific Macro Entity (e.g., a sector or country) to generate a synthetic thesis.

*Example Collision:*
*   *Macro Input:* India announces an import ban on 100 defense items.
*   *Activated Principle 1 (Tailwind):* "Follow Government Incentives / Monopsony Buyers"
*   *Activated Principle 2 (Constraint):* "Avoid State-Owned Enterprises (PSUs) due to poor capital allocation"

*   **Synthesis (The Collision):** The engine mathematically resolves the tension. If the Monopsony Tailwind is strong enough to override the historical PSU inefficiency drag, it synthesizes a new framework: *"State-Sponsored Capital Efficiency Pivot."*

---

## 5. Framework Generation Lifecycle

1.  **Signal:** A macro standard deviation breach is detected.
2.  **Candidate Framework:** The Collision Engine combines Activated Principles into a hypothetical thesis (e.g., "AI Hardware will capture 80% of Capex value before Software monetizes"). It exists purely as logic.
3.  **Emerging Framework:** The hypothesis is routed to the Opportunity Scanner. If the Scanner finds early fundamental validation (e.g., forward guidance matching the thesis), it is promoted to Emerging.
4.  **Validated Framework:** The thesis sustains for 2-4 quarters. The stock discovery metrics (ROCE, margins) are actively expanding. It is now treated as a high-conviction narrative.
5.  **Core Framework:** The macro thesis completes its multi-year cycle, proving the system's synthetic reasoning was correct. It is archived as a permanent Core Principle.

---

## 6. Failure Modes

1.  **The "Data Hallucination" (False Causality):** The engine detects a massive spike in Government Capex and activates "Follow Government Incentives," synthesizing a massive bull framework for a sector. It fails to realize the Capex is purely election-year spending with zero structural terminal value.
    *   *Fix:* Implement a "Political Cycle Mask" to discount macro inputs heavily during election years.
2.  **The Over-Constrained Null Output:** When a macro event occurs, the engine activates too many conflicting principles (e.g., "Buy Tech Growth" collides with "Avoid High P/E" and "Avoid Concentrated Supply Chains"). The collision math resolves to exactly zero, paralyzing the system and preventing any framework generation.
    *   *Fix:* Introduce a "Dominant Variable Hierarchy" where secular growth principles mathematically override valuation principles in the first 12 months of a new S-curve.
3.  **Premature Extrapolation:** A single quarter of elevated data (e.g., a one-off inventory restock) triggers an entire "Manufacturing Supercycle" framework.
    *   *Fix:* Macro Inputs must require a TTM (Trailing Twelve Month) confirmation or forward-guidance confirmation, not just a single quarterly print.

---

## 7. Historical Validation (How it would have worked)

### AI Infrastructure (2022)
*   *Macro Input:* Q4 2022 earnings transcripts show a massive, anomalous upward revision in Capex by MSFT, GOOG, and META, specifically directed at compute, while laying off headcount.
*   *Activated Principles:* "Follow secular Capex," "Prefer Picks & Shovels," "Seek supply chain bottlenecks."
*   *Collision:* The engine collides "Exploding Cloud Capex" with "Concentrated Semiconductor Foundry (TSMC)" and generates the synthetic thesis: *"The compute layer will absorb all immediate value."*
*   *Detection:* It generates this framework in **November 2022**, months before Akshat or the broad market synthesizes the hardware-first narrative.

### Defense Indigenization (2021)
*   *Macro Input:* 2020/2021 release of positive indigenization lists (embargoes) by the MoD.
*   *Activated Principles:* "Follow Import Substitution," "Follow Government Mandates."
*   *Collision:* Collides the government mandate with the "Predictable Order Book" principle. The Opportunity Scanner confirms that Order-Book-to-Bill ratios are extending past 3 years.
*   *Detection:* It synthesizes the *"Monopsony Tailwind"* framework in **Mid 2021**, before the margin expansion becomes visible in trailing PE ratios.

### India Manufacturing (2020)
*   *Macro Input:* Global FDI flow data shows capital actively routing away from China; India announces initial $26B PLI outlay.
*   *Activated Principles:* "China+1 Geopolitics," "Follow Subsidies."
*   *Collision:* The engine collides geopolitical derisking with sovereign financial backing.
*   *Detection:* Synthesizes the *"State-Sponsored Catch-Up"* framework in **Late 2020**.

---

## 8. Future Integration

The Collision Engine acts as the autonomous brain of the overarching system:

*   **Principle Catalog:** The Collision Engine reads the catalog as its core "laws of physics." It cannot synthesize a framework using logic that violates the core catalog without explicit Doubt Engine resolution.
*   **Emerging Framework Engine:** Synthesized frameworks are injected directly into the Emerging Framework Engine at the "Candidate" level, bypassing the need for Akshat to ever say a word.
*   **Opportunity Scanner:** The generated framework immediately triggers the Opportunity Scanner to build custom fundamental screens (e.g., generating a screen for "Defense Order Books > 3x Market Cap").
*   **Doubt Engine:** Before a synthetic framework is promoted to "Emerging," the Doubt Engine acts as a red team, deliberately searching for macro inputs that contradict the thesis (e.g., checking if the government is running out of fiscal space to fund the PLI).