# Principle Taxonomy Review

## 1. Current State of the Repository
The current taxonomy is largely defined in `knowledge/02_Akshat_Principle_Frequency_Table.md`. It is segmented into the following categories:
- 1. Core Philosophy Principles (CP-xx)
- 2. Portfolio Construction Principles (PC-xx)
- 3. Geographic Framework Principles (GF-xx)
- 4. Stock Selection Principles (SS-xx)
- 5. Macro Framework Principles (MF-xx)
- 6. Risk Management Principles (RM-xx)
- 7. Options Principles (OP-xx)

### Identified Problems with Current State
- **Flat Hierarchy:** Categories act merely as buckets. A Core Philosophy principle (like CP-04: "Earnings matter more than narratives") operates at the exact same level in the data structure as a Stock Selection principle (like SS-04: "Buy near 200DMA").
- **Duplicate Principles / Synonym Fragmentation:**
  - CP-01 ("Diversify across countries, currencies, and asset classes") overlaps heavily with RM-02 ("Avoid concentration risk") and PC-01 ("Use a barbell portfolio").
  - CP-06 ("Avoid narrative-driven investing") is effectively the inverse of CP-04 ("Earnings matter more than narratives") and GF-04 ("GDP growth is not an investment thesis").
  - SS-04 ("Buy near 200DMA") and CP-07 ("Use corrections as buying opportunity") are fundamentally the same concept expressed at different altitudes.
- **Lack of Constraints vs Tactics:** Currently, defensive rules (Constraints) and offensive actions (Tactics) are mixed within the same categories. "NEVER sell naked options" is a hard constraint, while "Use cash-secured puts" is a tactic. They should not sit side-by-side without relationship markers.

---

## 2. Recommended Ideal Taxonomy Architecture

To solve these issues, the taxonomy must move from a "List of Categories" to a "Parent-Child Hierarchy with Properties." Every principle must be typed as a **Mental Model**, a **Tactic**, or a **Constraint**.

### The New Structure
- **Tier 1: Parent Principles (Mental Models)** - Universal truths. They do not tell you *what* to buy, only *how the world works*.
- **Tier 2: Child Principles (Frameworks)** - How to apply the Parent Principle to a specific asset class or geography.
- **Tier 3: Tactics (Actionable Execution)** - Specific, timed actions based on Frameworks.
- **Tier 4: Constraints (Hard Rules)** - Absolute boundaries that negate Tactics regardless of the setup.

### Final Recommended Taxonomy

#### 1. DOMAIN: Capital Preservation (Defense)
- **Parent Principle: The Asymmetry of Loss** (Capital protection matters more than yield).
  - **Constraint:** Never use naked leverage.
  - **Constraint:** Maximum 25% of net worth in illiquid assets.
  - **Constraint:** Maximum 10% exposure to any single equity.
- **Parent Principle: The Barbell Structure**
  - **Child Principle:** Separate growth assets completely from hedge assets.
  - **Tactic:** Keep 60-80% of net worth highly liquid.
  - **Tactic:** Hold physical gold as a systemic non-correlated hedge.

#### 2. DOMAIN: Macro & Geography (Context)
- **Parent Principle: Global Opportunity Cost** (Every investment competes globally for capital).
  - **Child Principle:** Evaluate emerging markets (India) in USD real return terms.
  - **Constraint:** Do not invest in a country based solely on GDP growth narratives.
- **Parent Principle: Liquidity Drives Asset Prices**
  - **Child Principle:** Distinguish between liquidity-driven V-shaped panics and structural W-shaped damage.
  - **Tactic:** Track Central Bank balance sheets and Fed Funds probability as the primary signal for risk-on timing.

#### 3. DOMAIN: Equity Valuation & Quality (Offense)
- **Parent Principle: Earnings Gravity** (Price eventually converges with operating earnings).
  - **Child Principle:** K-shaped economics dictate margin expansion.
  - **Constraint:** Do not pay >100x PE for consumer mass-market stories.
- **Parent Principle: The Mean Reversion of Hype**
  - **Constraint:** Avoid parabolic price structures.
  - **Tactic:** Buy structural compounders (moats) when they correct to the 200DMA.

#### 4. DOMAIN: Options & Yield (Overlay)
- **Parent Principle: Options as Supplemental Yield, Not Gambling**
  - **Constraint:** NEVER sell naked options.
  - **Tactic:** Sell covered calls only on stocks already owned and near planned trim zones.
  - **Tactic:** Sell cash-secured puts only when capital is deployed and you desire assignment.

### Implementation Requirements
- Merge CP-04, CP-06, and GF-04 under the new **"Earnings Gravity"** Parent Principle.
- Merge CP-07 and SS-04 under the **"Mean Reversion of Hype"** Parent Principle.
- Transition `02_Akshat_Principle_Frequency_Table.md` to map to this nested JSON-style ontology. If a source supports a Tactic, it automatically increments the count for the Parent Principle.