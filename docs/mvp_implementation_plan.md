# MVP Implementation Plan: Akshat Reasoning System

## 1. Goal

The goal of Phase 2 is to build the smallest possible working version (MVP) of the Akshat Reasoning System. This MVP will execute the first complete reasoning loop: extracting principles from a test dataset, cataloging them, and activating them against a manually supplied macro event to synthesize a new framework and produce a reasoning report.

## 2. MVP Folder Structure

We will leverage the existing repository structure and build lightweight components to support the MVP.

```text
knowledge/
└── principles/
    ├── core_catalog.md              (Final accepted principles)
    ├── principle_schema.json        (Schema definition)
    ├── principle_evidence_map.json  (Links principles to source files)
    └── confidence_scores.json       (Stores calculated scores)

raw_sources/
└── mvp_test_data/
    ├── SOURCE-2021-01-DEFENSE.txt
    ├── SOURCE-2022-11-AI_CAPEX.txt
    └── SOURCE-2020-08-PLI_SCHEME.txt

scripts/
└── mvp/
    ├── 1_extract_principles.py      (Mock/Rule-based extractor for MVP)
    ├── 2_score_principles.py        (Applies MVP confidence math)
    ├── 3_macro_activator.py         (Takes manual macro input -> activates principles)
    └── 4_generate_report.py         (Outputs the final reasoning report)

tests/
└── mvp/
    └── test_reasoning_loop.py       (Validates the pipeline execution)

docs/
└── mvp_output/
    └── reasoning_report_YYYYMMDD.md (The final output)
```

## 3. Data Flow

The MVP reasoning loop operates in two distinct phases:

**Phase A: Catalog Generation (Offline/Batch)**
1.  **Ingestion:** `1_extract_principles.py` reads `mvp_test_data/`.
2.  **Extraction:** Extracts predefined concepts (using regex/heuristics to avoid heavy NLP for the MVP) and maps evidence.
3.  **Scoring:** `2_score_principles.py` calculates the Confidence Score based on F (Frequency) + T (Time persistence).
4.  **Storage:** Writes passing principles to `core_catalog.md` and updates `principle_evidence_map.json`.

**Phase B: Macro Activation (On-Demand)**
1.  **Macro Input:** User manually supplies a JSON macro event to `3_macro_activator.py` (e.g., `{"event": "MoD bans 100 import items", "tags": ["defense", "government_mandate"]}`).
2.  **Activation:** The script matches the macro `tags` against the metadata of the `core_catalog.md`.
3.  **Collision & Framework:** Combines activated principles to generate a synthetic thesis (e.g., "Monopsony Tailwind").
4.  **Reporting:** `4_generate_report.py` formats the output into a readable Markdown `reasoning_report`.

## 4. Required Files

*   `scripts/mvp/1_extract_principles.py`
*   `scripts/mvp/2_score_principles.py`
*   `scripts/mvp/3_macro_activator.py`
*   `scripts/mvp/4_generate_report.py`
*   `raw_sources/mvp_test_data/` (3-5 mock transcript text files)
*   `docs/mvp_output/` (Directory for generated reports)

## 5. Required Schemas

*   `knowledge/principles/principle_schema.json` (Already drafted; defines ID, title, description, category, score, evidence).
*   `scripts/mvp/macro_event_schema.json` (New for MVP to standardise manual input):
    ```json
    {
      "event_id": "MACRO-001",
      "description": "Government announces 30% increase in defense capital expenditure.",
      "trigger_tags": ["capex", "government_incentive", "defense"],
      "date": "2024-02-01"
    }
    ```

## 6. Test Dataset

We will create a highly constrained test dataset consisting of 3-5 synthetic "transcript" files placed in `raw_sources/mvp_test_data/`.

These files will be heavily seeded with specific, repeating phrases designed to easily trigger our rule-based MVP extractor.
*   *File 1 (2020):* Discusses avoiding state-owned enterprises due to capital misallocation.
*   *File 2 (2021):* Discusses following government subsidies and PLI schemes.
*   *File 3 (2022):* Discusses the importance of a predictable order book.

## 7. Validation Methodology

The system will be validated using `pytest` and manual inspection:

1.  **Extraction Validation:** Run Phase A. Ensure `core_catalog.md` correctly lists exactly three distinct principles derived from the test data, and that `confidence_scores.json` accurately reflects the frequency.
2.  **Activation Validation:** Run Phase B using the test event: *"MoD announces 100 item import embargo."*
3.  **Collision Validation:** The system must output a report that successfully activates the "Follow subsidies/mandates" principle AND the "Avoid state-owned enterprises" principle, noting the collision.

## 8. Success Criteria

The MVP is successful if, and only if, executing the pipeline generates a `docs/mvp_output/reasoning_report.md` that explicitly answers:
*   *"Given a major macro change, which Akshat principles become active and what framework emerges?"*

It must show the Evidence → Principle → Macro Event → Activated Framework pathway cleanly, without relying on vector DBs, external APIs, or full stock scanners.