# Principle Deduplication Audit

## Objective
Identify redundant, overlapping, and poorly structured principles within `knowledge/02_Akshat_Principle_Frequency_Table.md`.

---

## 1. Direct Duplicates

*   **RM-03 ("Avoid naked leverage / naked options") vs OP-03 ("NEVER sell naked options")**
    *   *Issue:* These are exactly the same principle. RM-03 is listed under Risk Management with a count of 7. OP-03 is listed under Options Principles with a count of 12.
    *   *Impact:* Artificial fragmentation of evidence counts. The system tracking is broken.

---

## 2. Near Duplicates & Synonym Fragmentation

*   **CP-04 ("Earnings and valuation matter more than narratives") vs CP-06 ("Avoid narrative-driven investing")**
    *   *Issue:* These are the inverse of each other. Avoiding narratives implies focusing on earnings/valuation. Keeping both splits the frequency counts and confuses extraction algorithms.
*   **CP-07 ("Use corrections as buying opportunity") vs SS-04 ("Buy near 200DMA / after 20-40% correction")**
    *   *Issue:* CP-07 is the conceptual version. SS-04 is the mathematical execution of that exact concept. These should not be separate, peer-level principles.

---

## 3. Parent-Child Relationship Conflicts

*   **PC-01 ("Use a barbell portfolio") vs PC-02 ("Separate growth assets and hedge assets")**
    *   *Issue:* Separating growth and hedge *is the definition* of a barbell portfolio. PC-02 is a child component of PC-01, not a peer principle.
*   **GF-04 ("GDP growth is not an investment thesis") vs GF-05 ("K-shaped economy: buy profit-expansion segments only")**
    *   *Issue:* The reason GDP growth is not a thesis (GF-04) is *because* the economy is K-shaped (GF-05). They belong in the same logical inheritance tree, not as separate items.

---

## 4. Taxonomy Conflicts

*   **CP-01 ("Diversify across countries, currencies, and asset classes") vs RM-02 ("Avoid concentration risk")**
    *   *Issue:* CP-01 is listed under "Core Philosophy." RM-02 is listed under "Risk Management." However, they describe the exact same action: preventing single-point failure. The taxonomy allows the same concept to be categorized differently depending on the context of the speech, leading to duplicate tracking.

## Conclusion
The Frequency Table is bloated with approximately 30-40% redundancy. The extraction engine has been allowed to create new principle IDs for synonyms rather than rolling counts up to established parent nodes.