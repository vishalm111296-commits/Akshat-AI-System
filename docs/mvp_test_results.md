# MVP Test Results

## Execution Summary
The Phase 2 MVP was successfully built and executed. The test suite (`pytest tests/mvp/test_collide.py`) passed 4/4 cases. The execution of `collide.py` correctly parsed `macro_input.json`, mapped tags via `ontology_map.json`, retrieved principles from `core_catalog.json`, and wrote a markdown file to `docs/mvp_output/generated_frameworks/EVT-2026-100.md`.

## What Worked
- **Data Flow:** The JSON structures successfully flowed from input to output. The `load_json` logic cleanly read the blueprints.
- **Ontology Extraction:** The naive substring match correctly extracted `["margin_expansion", "tech_hardware", "ai_infrastructure", "capex_cycle"]` from the raw text.
- **Principle Activation:** The boolean `ANY` matching logic successfully triggered the corresponding rules (GF-05, SS-03, P-EarningsGravity, RM-02).
- **Markdown Generation:** The output report successfully formatted the themes, constraints, and tactics into a readable Barbell-like structure.

## What Failed
- **Granular Constraint Resolution:** In the implementation, I had to define conflict resolution as: "Constraints suppress ALL tactics that share ANY matched_tag." In practice, `RM-02` (Avoid concentration risk) triggers on `tech_hardware`. `GF-05` (Buy K-shaped segments) triggered on `capex_cycle`. Because they didn't share the exact same tag, the Tactic was NOT suppressed by the Constraint. The logic works exactly as designed, but the *design fails real-world reasoning*.
- **The Expected Assertion:** The Blueprint required `macro_input.json` to have an `expected_principles` array. The implementation does not natively test this array within `collide.py` during runtime (it's meant for PyTest wrappers). If the goal is end-to-end user validation, `collide.py` ignores its own accuracy check.

## Unexpected Behavior
- **Dumb Inheritance:** The output correctly lists "P-EarningsGravity" and "SS-03" (its child). However, it lists them as equal peers under "Structural Themes". The system currently has no way to visually nest or subordinate them in the markdown.

## Architectural Assumptions That Proved Wrong
- **Assumption:** "JSON taxonomy solves conflicting principles."
  **Reality:** A tactic and a constraint can activate from the same text via two *different* matched tags. Because they have different matched tags, the engine assumes they don't conflict, allowing a risky tactic to pass through unsuppressed. A true resolution engine requires domain mapping, not just tag intersection.
- **Assumption:** "Substring ontology mapping is sufficient for MVP."
  **Reality:** The ontology map relies heavily on explicit string exactness. Plurals or typos (e.g. "manufacturing incentive" instead of "manufacturing incentives") instantly fail the entire reasoning loop.
