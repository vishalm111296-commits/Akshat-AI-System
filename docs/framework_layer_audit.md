# Framework Layer Audit

## Overview
This document audits the quality and authenticity of the Framework Generation layer, analyzing whether the system produces actionable insights or merely plausible-sounding lists.

---

## TASK 1 & 2: Plausibility vs. Correctness & The Routing Problem

*Reviewing the 10 Macro Tests from `test_results.md`.*

**Test 1: Semiconductor Incentives**
* *Framework Generated:* "Prefer margin expansion. Monitor AI cycle monetization. Avoid concentration risk."
* *Verdict:* **Merely Plausible.** It is not "correct" because it assumes all semiconductor incentives lead to AI monetization and margin expansion.
* *Why it's routing:* The word "semiconductor" routed directly to "AI monetization" via static map. It did not reason whether the incentives were for legacy auto chips (no AI relevance) or leading-edge GPUs.

**Test 2: Defense Indigenization**
* *Framework Generated:* "Sovereign Survival Capex."
* *Verdict:* **Merely Plausible.**
* *Why it's routing:* "Defense indigenization" triggered `defense_capex`. It routed a synonym. It didn't reason whether the budget allocation was actually large enough to constitute a structural shift.

**Test 3 & 4 & 8: Nuclear / Logistics / Water**
* *Framework Generated:* "No actionable principles found."
* *Verdict:* **Incorrect.**
* *Why it's routing:* The router hit a `KeyError` on the dictionary lookup. A reasoning engine would have deduced these were all forms of infrastructure capex.

**Test 5: Hospital Expansion**
* *Framework Generated:* "K-shaped economy: buy profit-expansion segments."
* *Verdict:* **Merely Plausible.**
* *Why it's routing:* "Hospital expansion" statically mapped to "K-shaped economy". The system did not reason whether the expansion was high-end corporate hospitals (K-shaped beneficiary) or government-subsidized rural clinics (low margin, anti-K-shape).

**Test 6 & 7: Data Center Growth / Power Grid Upgrades**
* *Framework Generated:* "Monitor AI cycle. The Base-Load Bottleneck."
* *Verdict:* **Merely Plausible.**
* *Why it's routing:* "Power grid" mapped to "Base-Load Bottleneck". The system didn't reason that power grid upgrades take 5-10 years to permit and build, meaning the "AI cycle" might end before the grid upgrade generates profit.

**Test 9: Robotics Adoption**
* *Framework Generated:* "Prefer margin expansion."
* *Verdict:* **Merely Plausible.**
* *Why it's routing:* Robotics mapped to margin expansion. It ignored whether the robotics were being bought (capex cost) or sold (revenue generation).

**Test 10: Unknown Industry**
* *Framework Generated:* "No actionable principles found."
* *Verdict:* **Incorrect.** (A Dyson sphere is the ultimate energy capex cycle).
* *Why it's routing:* Dictionary lookup failed.

---

## TASK 3: Missing Information Modifying Outcomes

For each generated framework, missing structural data would have drastically changed the output:

1. **Semiconductor Incentives:** Missing **Competitive Intensity**. If China is subsidizing simultaneously, margins compress, completely invalidating the "Prefer margin expansion" rule.
2. **Defense Indigenization:** Missing **Policy Timeline**. Defense cycles take years. If the indigenization is a 10-year goal, buying immediately traps capital in dead money.
3. **Hospital Expansion:** Missing **Demographics**. If expanding into a region with a declining birth rate and zero insurance penetration, the K-shape logic fails.
4. **Data Centers / Power Grid:** Missing **Market Structure**. If the power grid is state-owned and heavily regulated, it cannot monetize the base-load bottleneck.
5. **Robotics Adoption:** Missing **Capex Cycle Phase**. Is the industry at the beginning of the spend (buy the robotics manufacturers) or at the end of the spend (buy the factory owners who now have higher margins)?

---

## TASK 4: Can the current layer discover historical trends early?

**Answer:** NO.

**Evidence:**
To discover "Hospitals (2019)" or "Defense (2020)" before consensus, a system must observe a weak, unmapped signal (e.g., "Insurance penetration rises by 2%") and extrapolate a second-order effect ("Therefore, high-end hospitals will gain pricing power").

The current framework layer is mathematically barred from doing this because it requires the exact term "hospital expansion" to be pre-mapped to the exact tag `k_shaped_economy`. If a human has already mapped the relationship in the JSON dictionary, then *by definition*, the trend is already consensus in the human's mind. The system can only "discover" what the human has already figured out and hardcoded.

---

## TASK 5: Smallest Improvement for Framework Quality

**Constraint:** No LLMs, Embeddings, or New Engines.

**The Improvement:** **Contextual Conditionals (The 'IF/THEN' Checklist Layer).**
Instead of a principle merely being a string (`"Prefer margin expansion"`), the principle object in `core_catalog.json` must be expanded to include an array of required real-world conditions that the user must manually verify before the framework is considered valid.

*Example implementation:*
When `SS-03` triggers, the output isn't just the title. It outputs:
```text
TACTIC: Prefer margin expansion
VALIDATION REQUIRED:
- Is competitive intensity low? [Yes/No]
- Is the capex phase mature? [Yes/No]
(If No, discard this framework).
```
*Impact:* This forces the human user to provide the missing reasoning that the router cannot generate. It shifts the system from a "dumb oracle" to an "expert interview checklist."

---

## FINAL VERDICT

"The project's biggest bottleneck is **the assumption that language is deterministic.**"

**Defense:**
Every failure in the Akshat Reasoning System—from the missed macro events, to the false-positive sectors, to the doomed stock selections, to the merely "plausible" frameworks—stems from a single architectural sin: The belief that complex economic language can be mapped via static, hardcoded JSON dictionaries.

A "hospital" is not a "K-shaped economy" if it is a public clinic. An "incentive" does not mean "margin expansion" if it sparks a price war. Language is context-dependent, reflexive, and probabilistic. Because the MVP attempts to treat language as a deterministic, immutable key-value pair, it instantly strips away all context the moment it ingests a sentence.

You cannot build a dynamic reasoning engine on top of a data pipe that destroys context at Step 1. Until the semantic bottleneck is removed, the system will only ever be a fragile router.