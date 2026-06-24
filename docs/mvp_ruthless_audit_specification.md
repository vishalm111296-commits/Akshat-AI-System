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

docs/
└── mvp_output/
    └── generated_frameworks/
```

## 2. Exact Files Required

Only two Python scripts are required.
*   `scripts/mvp/1_extract.py`
*   `scripts/mvp/2_collide.py`

Everything else is JSON data or output text. The Emerging Framework Engine, Doubt Engine, and Opportunity Scanner are **omitted** from the MVP code entirely.

## 3. Exact Schemas Required

**A. Principle Schema (`core_catalog.json`)**
```json
{
  "id": "PRIN-001",
  "title": "Follow Government Subsidies",
  "activation_tags": ["capex", "incentive", "pli", "manufacturing", "semiconductor"],
  "polarity": "positive",
  "evidence_count": 5
}
```
*Note: Stripped down. No 'Time Persistence' or 'Novelty' scoring for the MVP.*

**B. Macro Input Schema (Passed into `2_collide.py`)**
```json
{
  "event_id": "MACRO-TEST-01",
  "description": "Government launches large semiconductor manufacturing incentives.",
  "trigger_tags": ["semiconductor", "incentive"]
}
```

## 4. Exact Scripts Required

1.  **`1_extract.py`:** Reads `mock_transcripts.json`. Uses a hardcoded Python dictionary of keywords to scan the text. If keywords match, it increments `evidence_count` and saves to `core_catalog.json`. *(Mocking the Principle Extraction Engine).*
2.  **`2_collide.py`:** Reads the user-supplied Macro Input JSON. Compares the `trigger_tags` against the `activation_tags` in `core_catalog.json`. Finds overlapping principles. Synthesizes a hardcoded text output based on the colliding polarities. *(Mocking the Collision Engine).*

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

## MVP WALKTHROUGH

**Macro Event Input:**
`"Government launches large semiconductor manufacturing incentives"` (Tags: `semiconductor`, `incentive`, `capex`, `government`)

### Step 1: Which principles activate?

`2_collide.py` scans `core_catalog.json` for tag overlaps and mathematically activates:
1.  **PRIN-001:** "Follow Government Subsidies" *(Activation Tags: incentive, government. Polarity: Positive)*
2.  **PRIN-002:** "Avoid Capital-Intensive Execution Traps" *(Activation Tags: capex, manufacturing. Polarity: Negative)*
3.  **PRIN-003:** "Follow Geopolitical De-risking" *(Activation Tags: semiconductor. Polarity: Positive)*

### Step 2: Which framework emerges?

The script detects a "Collision" between two Positive Tailwinds (Subsidies + Geopolitics) and one Negative Constraint (Capital Execution Risk).

Because the Geopolitics/Subsidy tags outweigh the Execution tag in this specific hardcoded MVP logic, it generates the framework: **"State-Sponsored Catch-Up Narrative with Execution Risk."**

### Step 3: What reasoning report is generated?

*(Output written to `docs/mvp_output/generated_frameworks/MACRO-TEST-01.md`)*

> # Reasoning Report: MACRO-TEST-01
>
> **Event:** Government launches large semiconductor manufacturing incentives.
>
> **Activated Principles:**
> - [x] Follow Government Subsidies (Tailwind)
> - [x] Follow Geopolitical De-risking (Tailwind)
> - [!] Avoid Capital-Intensive Execution Traps (Constraint)
>
> **Synthesized Framework:** *State-Sponsored Catch-Up Narrative with Execution Risk*
>
> **Reasoning:** The macro event acts as a massive double-tailwind (Geopolitics + Subsidies). However, semiconductor manufacturing is highly capital intensive, activating the historical execution constraint. Therefore, the framework suggests buying the narrative early but actively monitoring for execution delays that historically plague capital-heavy Indian sectors.

---

## CRITICAL QUESTION

**What is the MINIMUM amount of code required to prove the architecture works?**

**Answer:** Less than 200 lines of Python.

We only need to prove the *routing logic* (Tag → Principle → Collision), not the intelligence of the NLP.
Therefore, we completely remove embeddings, LLMs, API calls, dynamic web scraping, Confidence Math, and the Opportunity Scanner. The minimum code is simply a tag-matching algorithm and a basic conditional collision logic script that prints a formatted string.