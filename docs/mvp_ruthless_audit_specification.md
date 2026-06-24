# MVP Ruthless Audit & Specification

*This document defines the absolute minimum viable product (MVP) required to prove the generative reasoning architecture. All non-essential systems (Doubt Engine, Opportunity Scanner, complex NLP, databases) have been aggressively stripped away.*

---

## 1. Exact Folder Structure

```text
knowledge/
└── principles/
    ├── core_catalog.json           (Replaces Markdown for MVP script parsing)

raw_sources/
└── mvp_test_data/
    └── mock_transcripts.json       (Single file test corpus)

scripts/
└── mvp/
    ├── 1_extract.py                (Rules-based extraction)
    ├── 2_collide.py                (Macro input -> Framework generation)
    └── ontology_map.json           (Maps macro words to abstract tags)

docs/
└── mvp_output/
    └── generated_frameworks/
```

## 2. Exact Files Required

Only two Python scripts and a helper mapping file are required.
*   `scripts/mvp/1_extract.py`
*   `scripts/mvp/2_collide.py`
*   `scripts/mvp/ontology_map.json`

Everything else is JSON data or output text. The Emerging Framework Engine, Doubt Engine, and Opportunity Scanner are **omitted** from the MVP code entirely.

## 3. Exact Schemas Required

**A. Principle Schema (`core_catalog.json`)**
```json
{
  "id": "PRIN-001",
  "title": "Follow Government Subsidies",
  "activation_tags": ["incentive", "government", "subsidy"],
  "polarity": "positive",
  "evidence_count": 5
}
```
*Note: Stripped down. No 'Time Persistence' or 'Novelty' scoring for the MVP. Crucially, specific sector nouns (like "semiconductor") are strictly forbidden in Core Principles.*

**B. Macro Input Schema (Passed into `2_collide.py`)**
```json
{
  "event_id": "MACRO-TEST-01",
  "description": "Government launches large semiconductor manufacturing incentives.",
  "trigger_tags": ["semiconductor", "incentive"]
}
```

## 4. Exact Scripts Required

1.  **`1_extract.py`:** Reads `mock_transcripts.json`. Uses a hardcoded Python dictionary of abstract keywords to scan the text. If abstract concepts match, it increments `evidence_count` and saves to `core_catalog.json`. *(Mocking the Principle Extraction Engine).*
2.  **`2_collide.py`:** Reads the user-supplied Macro Input JSON. Before matching tags, it uses `ontology_map.json` to translate specific input nouns (e.g., "semiconductors") into abstract systemic tags (e.g., "geopolitics", "capex"). It then compares these abstract tags against `core_catalog.json`. Finds overlapping principles. Synthesizes a hardcoded text output based on the colliding polarities. *(Mocking the Collision Engine).*

## 5. Input Format

The user runs the MVP via the terminal, passing a JSON string:
`python scripts/mvp/2_collide.py --macro '{"description": "Government launches large semiconductor manufacturing incentives", "trigger_tags": ["semiconductor", "incentive", "capex"]}'`

## 6. Output Format

A single Markdown file saved to `docs/mvp_output/generated_frameworks/MACRO-TEST-01.md` containing the final Reasoning Report.

## 7. Test Dataset Size

**Exactly 3 mock paragraphs** saved in `raw_sources/mvp_test_data/mock_transcripts.json`.
1. Paragraph mentioning subsidies = good.
2. Paragraph mentioning capital-heavy execution in India = historically bad.
3. Paragraph mentioning geopolitics = macro tailwind.

## 8. Manual Validation Process

1. Delete `core_catalog.json`.
2. Run `python scripts/mvp/1_extract.py`. Verify the catalog is populated with 3 principles.
3. Run `python scripts/mvp/2_collide.py` with the semiconductor JSON.
4. Read the output Markdown file. Verify it explicitly lists the colliding principles.

## 9. Success Criteria

The code successfully connects the chain: *Macro Input → Tag Matching → Principle Activation → Framework Synthesis Report*, running end-to-end locally in under 2 seconds without external API calls.

---

## MVP WALKTHROUGH 1: The Basic Test

**Macro Event Input:**
`"Government launches broad manufacturing subsidies"` (Tags: `manufacturing`, `incentive`, `capex`, `government`)

### Step 1: Which principles activate?

`2_collide.py` scans `core_catalog.json` for tag overlaps and mathematically activates:
1.  **PRIN-001:** "Follow Government Subsidies" *(Activation Tags: incentive, government. Polarity: Positive)*
2.  **PRIN-002:** "Avoid Capital-Intensive Execution Traps" *(Activation Tags: capex, manufacturing. Polarity: Negative)*

### Step 2: Which framework emerges?

The script detects a "Collision" between one Positive Tailwind (Subsidies) and one Negative Constraint (Capital Execution Risk).

It generates the basic framework: **"State-Sponsored Catch-Up Narrative with Execution Risk."**

---

## MVP WALKTHROUGH 2: The Abstract Collision Test (Testing Generative Synthesis)

*To prove the system is not merely matching exact keywords, we test an input containing specific sector nouns that DO NOT EXIST in the Principle Catalog.*

**Macro Event Input:**
`"Government launches large semiconductor incentives"`
*(Input words: "government", "semiconductor", "incentive")*

**The Constraint:**
The word "semiconductor" does NOT exist in the `core_catalog.json`.

### Step 1: Ontology Abstraction
Instead of failing to match, `2_collide.py` passes "semiconductor" through the MVP `ontology_map.json`. The dictionary maps `semiconductor -> ["capex", "geopolitics", "supply_chain"]`.

### Step 2: Which principles activate?

The script now scans the catalog using the *abstracted* tags rather than the raw text. It activates:
1.  **PRIN-001:** "Follow Government Subsidies" *(Triggered by "government", "incentive" tags. Polarity: Positive)*
2.  **PRIN-002:** "Follow Geopolitical Supply-Chain Shifts" *(Triggered by abstracted "geopolitics", "supply_chain" tags. Polarity: Positive)*
3.  **PRIN-003:** "Avoid Capital-Intensive Execution Traps" *(Triggered by abstracted "capex" tag. Polarity: Negative)*

### Step 3: Which framework emerges?

The collision logic recognizes that a specific noun ("semiconductor") has triggered multiple structural themes simultaneously: State Funding + Geopolitics + Capital Intensity.

Because multiple structural tailwinds collide to override the execution constraint, the MVP logic conditionally synthesizes a specialized framework: **"Domestic Strategic Manufacturing"** (or "State-Sponsored Semiconductor Manufacturing" by prepending the input noun to the base structural framework).

### Step 4: What reasoning report is generated?

*(Output written to `docs/mvp_output/generated_frameworks/MACRO-TEST-02.md`)*

> # Reasoning Report: MACRO-TEST-02
>
> **Event:** Government launches large semiconductor incentives.
>
> **Activated Principles:**
> - [x] Follow Government Subsidies (Tailwind)
> - [x] Follow Geopolitical Supply-Chain Shifts (Tailwind)
> - [!] Avoid Capital-Intensive Execution Traps (Constraint)
>
> **Synthesized Framework:** *Domestic Strategic Manufacturing*
>
> **Reasoning:** The event ("semiconductor") maps structurally to high capex, vulnerable supply chains, and deep geopolitical tension. The presence of government incentives provides a catalyst to offset the traditional capital-intensive execution trap. The collision of these principles generates a "Domestic Strategic Manufacturing" framework. The system synthesized this structural thesis without requiring a pre-existing rule explicitly about "semiconductors."

---

## CRITICAL QUESTION

**What is the MINIMUM amount of code required to prove the architecture works?**

**Answer:** Less than 200 lines of Python.

We only need to prove the *routing logic* (Tag → Principle → Collision), not the intelligence of the NLP.
Therefore, we completely remove embeddings, LLMs, API calls, dynamic web scraping, Confidence Math, and the Opportunity Scanner. The minimum code is simply a tag-matching algorithm and a basic conditional collision logic script that prints a formatted string.