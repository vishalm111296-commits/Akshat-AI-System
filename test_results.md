# MVP 10 Macro-Event Tests

### Test 1: Semiconductor incentives
**Input:** Government launches major semiconductor manufacturing incentives.

**Activated principles:**
- [TACTIC] SS-03: Prefer margin expansion
- [TACTIC] MF-03: Monitor AI cycle monetization
- [CONSTRAINT] RM-02: Avoid concentration risk

**Generated framework:**
Based on the macro input, the following framework is proposed:

**CRITICAL CONSTRAINTS:**
- Must adhere to: Avoid concentration risk

**TACTICAL ACTIONS:**
- Execute strategy: Prefer margin expansion
- Execute strategy: Monitor AI cycle monetization

**Failure analysis:** Success.

---

### Test 2: Defense indigenization
**Input:** New policy pushes rapid defense indigenization.

**Activated principles:**
- [TACTIC] PC-04: Sovereign Survival Capex

**Generated framework:**
Based on the macro input, the following framework is proposed:

**TACTICAL ACTIONS:**
- Execute strategy: Sovereign Survival Capex

**Failure analysis:** Success.

---

### Test 3: Nuclear incentives
**Input:** Govt subsidizes nuclear energy capex.

**Activated principles:**
None.

**Generated framework:**
No actionable principles found for this macro event.

**Failure analysis:** Failed due to lack of 'nuclear' or generic 'capex' synonym in ontology map.

---

### Test 4: Logistics corridors
**Input:** Massive funding approved for new logistics corridors.

**Activated principles:**
None.

**Generated framework:**
No actionable principles found for this macro event.

**Failure analysis:** Failed due to missing 'logistics' key in the ontology map.

---

### Test 5: Hospital expansion
**Input:** Private hospital expansion into tier 2 cities surges.

**Activated principles:**
- [TACTIC] GF-05: K-shaped economy: buy profit-expansion segments

**Generated framework:**
Based on the macro input, the following framework is proposed:

**TACTICAL ACTIONS:**
- Execute strategy: K-shaped economy: buy profit-expansion segments

**Failure analysis:** Success.

---

### Test 6: Data center growth
**Input:** Hyperscaler data center growth consumes the power grid.

**Activated principles:**
- [TACTIC] MF-03: Monitor AI cycle monetization
- [CONSTRAINT] RM-02: Avoid concentration risk
- [TACTIC] SS-04: The Base-Load Bottleneck

**Generated framework:**
Based on the macro input, the following framework is proposed:

**CRITICAL CONSTRAINTS:**
- Must adhere to: Avoid concentration risk

**TACTICAL ACTIONS:**
- Execute strategy: Monitor AI cycle monetization
- Execute strategy: The Base-Load Bottleneck

**Failure analysis:** Success.

---

### Test 7: Power grid upgrades
**Input:** Federal mandate requires total power grid upgrades.

**Activated principles:**
- [TACTIC] SS-04: The Base-Load Bottleneck

**Generated framework:**
Based on the macro input, the following framework is proposed:

**TACTICAL ACTIONS:**
- Execute strategy: The Base-Load Bottleneck

**Failure analysis:** Success.

---

### Test 8: Water infrastructure
**Input:** Billions allocated for water infrastructure repair.

**Activated principles:**
None.

**Generated framework:**
No actionable principles found for this macro event.

**Failure analysis:** Failed due to missing 'water infrastructure' key.

---

### Test 9: Robotics adoption
**Input:** Rapid robotics adoption drives factory efficiency.

**Activated principles:**
- [TACTIC] SS-03: Prefer margin expansion

**Generated framework:**
Based on the macro input, the following framework is proposed:

**TACTICAL ACTIONS:**
- Execute strategy: Prefer margin expansion

**Failure analysis:** Success.

---

### Test 10: Unknown industry
**Input:** Breakthrough in dyson sphere construction technology.

**Activated principles:**
None.

**Generated framework:**
No actionable principles found for this macro event.

**Failure analysis:** Graceful failure on genuinely unknown industry.

---

## FINAL SECTION

**Answer:**
Is this system producing reasoning? Or merely routing?

**Verdict:** Merely routing.

**Evidence:**
1. In the `Nuclear incentives` test, the text "Govt subsidizes nuclear energy capex." generated exactly zero principles because the word "nuclear" was not explicitly hardcoded into the `ontology_map.json`, even though the word "capex" is a fundamental concept in the system. The system could not *reason* that nuclear capex is still capex.
2. In the `Data center growth` test ("Hyperscaler data center growth consumes the power grid."), the system extracted predefined principles (MF-03, RM-02, SS-04) solely because "data center" and "power grid" were explicitly defined in the JSON map. It did not synthesize the relationship between AI infrastructure and baseload power constraints; it merely copy-pasted string arrays.
3. The "Generated framework" output is literally just a hardcoded markdown string (`f"- Execute strategy: {t['name']}"`) looping over whatever dictionary keys happened to match substrings in the text. There is no generative synthesis, no contextual weighing, and no actual reasoning occurring. It is a deterministic key-value router.
