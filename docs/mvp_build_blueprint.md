# MVP Build Blueprint

*This document translates the frozen MVP architecture into explicit implementation instructions. A developer should be able to build the system entirely from this blueprint without referencing any other documentation.*

---

## 1. `knowledge/principles/core_catalog.json`

*   **Responsibility:** Acts as the static database of predefined "laws" (principles) that govern the reasoning system.
*   **Input:** Manual creation by the developer.
*   **Output:** Read into memory by `2_collide.py` during runtime.
*   **Functions:** N/A (Data file).
*   **Dependencies:** None.
*   **Estimated Line Count:** ~40 lines.
*   **Implementation Details (Data Shape):**
    Must be a JSON array of objects. Each object represents a Principle:
    *   `id` (string): e.g., "PRIN-001"
    *   `title` (string): e.g., "Follow Government Subsidies"
    *   `activation_tags` (array of strings): Core abstract tags that trigger this principle (e.g., `["incentive", "government", "subsidy"]`).
    *   `polarity` (string): Either `"positive"` (tailwind) or `"negative"` (constraint).
    *   `evidence_count` (integer): Hardcoded integer (e.g., `5`).

---

## 2. `scripts/mvp/ontology_map.json`

*   **Responsibility:** Solves the "exact keyword" problem by mapping specific, real-world sector nouns to abstract, structural tags.
*   **Input:** Manual creation by the developer.
*   **Output:** Read into memory by `2_collide.py` during runtime.
*   **Functions:** N/A (Data file).
*   **Dependencies:** None.
*   **Estimated Line Count:** ~20 lines.
*   **Implementation Details (Data Shape):**
    Must be a simple Key-Value JSON dictionary mapping a noun string to an array of tag strings:
    *   `"semiconductor"`: `["capex", "geopolitics", "supply_chain"]`
    *   `"defense"`: `["monopsony", "government", "psu"]`

---

## 3. `scripts/mvp/macro_input.json`

*   **Responsibility:** Provides the simulated external macro event that triggers the reasoning loop.
*   **Input:** Manual creation by the developer.
*   **Output:** Read into memory by `2_collide.py` during runtime.
*   **Functions:** N/A (Data file).
*   **Dependencies:** None.
*   **Estimated Line Count:** ~15 lines.
*   **Implementation Details (Data Shape):**
    Must be a single JSON object containing:
    *   `event_id` (string): e.g., "MACRO-TEST-02"
    *   `description` (string): A human-readable sentence.
    *   `trigger_tags` (array of strings): Specific nouns or tags (e.g., `["semiconductor", "incentive"]`).

---

## 4. `scripts/mvp/2_collide.py`

*   **Responsibility:** The core reasoning engine. It performs the sequence: load input → abstract tags via ontology → match principles → synthesize framework → output report.
*   **Input:** Reads `macro_input.json`, `ontology_map.json`, and `core_catalog.json` from disk.
*   **Output:** Writes a markdown file to `docs/mvp_output/generated_frameworks/[event_id].md`.
*   **Dependencies:** Only standard Python libraries (`json`, `os`, `argparse`).
*   **Estimated Line Count:** ~100 lines.
*   **Functions Required:**

    1.  `load_json(filepath: str) -> dict/list`
        *   Standard helper to load the three JSON files.

    2.  `abstract_tags(input_tags: list, ontology: dict) -> set`
        *   Iterates through `input_tags`. If a tag exists as a key in `ontology`, it adds the mapped abstract tags to a set. If it doesn't exist, it adds the original tag itself to the set. Returns a deduplicated set of abstract tags.

    3.  `find_activated_principles(abstracted_tags: set, catalog: list) -> list`
        *   Iterates through the `catalog`. If any tag in a Principle's `activation_tags` intersects with the `abstracted_tags` set, that Principle is appended to the active list. Returns the list of activated principle objects.

    4.  `synthesize_framework(activated_principles: list) -> tuple(str, str)`
        *   *MVP Conditional Logic:* Calculates the total number of "positive" vs "negative" polarities in the activated list.
        *   If `positive > 0` and `negative > 0`: Return Framework: `"State-Sponsored Catch-Up Narrative with Execution Risk"`.
        *   If `positive > 0` and `negative == 0`: Return Framework: `"Pure Structural Tailwind"`.
        *   If `positive == 0` and `negative > 0`: Return Framework: `"Terminal Value Trap"`.
        *   Returns a tuple containing `(Framework_Title, Reasoning_Paragraph)`.

    5.  `generate_report(event: dict, activated: list, framework: str, reasoning: str)`
        *   Formats the data into a Markdown string matching the required MVP output format (including checkboxes `[x]` for positive and `[!]` for negative principles).
        *   Writes the string to the correct output path using `event["event_id"]` as the filename.

    6.  `main()`
        *   Uses `argparse` to accept an optional `--macro` flag (passing a JSON string directly). If not provided, it defaults to reading `macro_input.json`.
        *   Executes functions 1 through 5 sequentially.

---

## 5. `docs/mvp_output/generated_frameworks/[event_id].md`

*   **Responsibility:** The final artifact proving the collision engine successfully synthesized a thesis.
*   **Input:** Text strings passed from `2_collide.py`.
*   **Output:** Final file written to disk.
*   **Functions:** N/A (Generated file).
*   **Dependencies:** `2_collide.py`
*   **Estimated Line Count:** ~25 lines.
*   **Implementation Details (Formatting Shape):**
    The markdown output MUST strictly follow this structure:
    ```markdown
    # Reasoning Report: {event_id}

    **Event:** {description}

    **Activated Principles:**
    - [x] {title} (Tailwind)
    - [!] {title} (Constraint)

    **Synthesized Framework:** *{framework_title}*

    **Reasoning:** {reasoning_paragraph}
    ```