# Emerging Framework Detection Engine

## 1. Introduction

The **Emerging Framework Detection Engine** is designed to solve the "Backward-Looking Anchor" failure mode of the core Principle Extraction architecture. While Core Principles require multi-year historical persistence, the market constantly evolves, generating new macroeconomic and technological paradigms.

This engine's goal is to identify new mental models (e.g., AI Infrastructure, Defense Indigenization, Data Centers) *before* they have the historical track record to become Core Principles. It identifies high-velocity, structurally novel concepts and flags them for immediate utilization.

## 2. Emerging Framework Schema

To differentiate between a Core Principle and a nascent trend, we introduce the `emerging_framework_schema.json`.

```json
{
  "framework_id": "",
  "title": "",
  "description": "",
  "category": "EMERGING_THEME",
  "velocity_score": 0,
  "novelty_score": 0,
  "first_detected_date": "YYYY-MM-DD",
  "evidence_count_30d": 0,
  "evidence_count_90d": 0,
  "source_references": [],
  "conflicting_core_principles": [],
  "status": "CANDIDATE | EMERGING | PROMOTED | ABANDONED"
}
```
*Key Differences from Core Schema:* It tracks short-term temporal windows (`30d`, `90d`) instead of absolute frequency, explicitly scores `novelty`, and tracks conflicts with legacy principles (which often block new ideas).

## 3. Velocity Scoring Model

Velocity measures the *intensity* of a new idea's repetition over a short time frame, compensating for its lack of long-term persistence.

**Velocity Score = (E_30d * W_recent) + (E_90d * W_medium) + Cross_Format_Spike**

Where:
*   **E_30d / E_90d:** Count of unique evidence snippets containing the concept in the last 30 and 90 days.
*   **W_recent / W_medium:** Exponential decay weights prioritizing recent days.
*   **Cross_Format_Spike:** A binary multiplier (e.g., 1.5x) if the concept suddenly appears across different formats (e.g., mentioned in a YouTube video *and* a Paid Post in the same week).

*Threshold:* A concept crossing a defined Velocity Score threshold is immediately flagged as a "Candidate Framework."

## 4. Novelty Detection Model

A high-velocity topic might just be a news cycle (e.g., "Elections"). The Novelty Detection Model ensures the topic represents a *structural shift* in reasoning, not just market noise.

**Novelty Score = Semantic_Distance_from_Core + Structural_Keyword_Density**

1.  **Semantic Distance:** The engine measures the embedding distance between the Candidate Framework and all existing Core Principles.
    *   *If distance is low:* It's just a repetition of an old principle (Low Novelty).
    *   *If distance is high:* It is fundamentally new reasoning (High Novelty).
2.  **Structural Keyword Density:** The engine parses the evidence for words implying permanence or regime change (e.g., "structural", "capex cycle", "indigenization", "platform shift", "secular"). A high density of these words increases the Novelty Score.

*Rule:* To survive, a Framework must have BOTH High Velocity AND High Novelty.

## 5. Promotion Lifecycle

The lifecycle ensures ideas are tested, utilized, and eventually either canonized or discarded.

1.  **Candidate Framework:** Triggered automatically by high Velocity and Novelty scores. Resides in a temporary sandbox.
2.  **Emerging Framework:** Promoted by a human reviewer or if velocity sustains for > 6 months. It is now active and usable by the system.
3.  **Core Principle:** Promoted if the Framework survives and provides accurate predictive value over a 3-year multi-year cycle.
4.  **Abandoned:** If velocity drops to zero after 6 months and fundamental data (Opportunity Scanner) fails to validate the thesis, it is archived as a "Failed Narrative."

## 6. Integration with Principle Catalog

The Principle Catalog will be bifurcated:
*   `knowledge/principles/core_catalog.md` (High Confidence, High Persistence)
*   `knowledge/principles/emerging_catalog.md` (High Velocity, High Novelty)

When the system runs reasoning tasks, it queries the `core_catalog` for foundational rules (e.g., position sizing, valuation discipline) and queries the `emerging_catalog` for tactical thesis generation (e.g., "Where is the new Capex going?").

If an Emerging Framework directly conflicts with a Core Principle (e.g., "Defense Indigenization" vs. "Avoid State-Owned Enterprises"), the system explicitly flags this tension in the `docs/open-decisions.md` tracker for human resolution.

## 7. Integration with Opportunity Scanner

The Opportunity Scanner actively searches for fundamental financial data to validate narratives.

*   **Proactive Validation:** When a new Emerging Framework (e.g., "AI Infrastructure") is added, the Scanner immediately generates a targeted fundamental screen: "Show me companies with Capex > 20% YoY, semiconductor supply chain exposure, and zero consumer-facing revenue."
*   **Feedback Loop:** If the Scanner finds companies matching this screen that are expanding operating margins, the Emerging Framework's "Confidence Score" increases. If the Scanner finds zero margin expansion after 4 quarters, the Framework is penalized and risks being downgraded to "Abandoned."

## 8. Failure Modes

1.  **The "News Cycle" False Positive:** The engine misinterprets a temporary, high-velocity macro panic (e.g., a regional banking crisis) as a "Structural Novelty" because of the dense use of words like "regime change."
    *   *Mitigation:* The Opportunity Scanner feedback loop. A banking panic rarely results in positive, forward-looking Capex screens.
2.  **Semantic Drift:** As an Emerging Framework evolves (e.g., AI shifts from "chips" to "power/cooling"), the embedding distance might drift, causing the engine to log "AI Data Centers" and "AI Energy" as two separate frameworks rather than evolving the original thesis.
    *   *Mitigation:* Implementing a parent-child relationship check during the Candidate phase.
3.  **Valuation Ignorance:** High-velocity emerging trends (like AI in 2023) are often accompanied by massive valuation spikes. The engine might prioritize the narrative while ignoring the Core Principle of "Buy fair value," leading to capital destruction.
    *   *Mitigation:* Emerging Frameworks must *always* be subordinated to the risk-management Core Principles during the final portfolio construction phase.