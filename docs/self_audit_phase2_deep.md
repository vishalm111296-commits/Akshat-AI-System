# Self-Audit Phase 2 (Deep)

## Objective
Attempt to destroy my own conclusions from previous audits and documentation.

---

### Top 20 Mistakes Made So Far
1. Writing an MVP script (`2_collide.py`) that explicitly ignores the `parent_id` JSON schema I designed.
2. Relying on "Deprecated Batch IDs" to justify proceeding past Phase 1.
3. Pretending that string interpolation in a Markdown f-string constitutes "Framework Generation."
4. Designing a Stock Selection Constraint matrix without actually building a data pipeline to feed it.
5. Assuming a "Red Team Audit" makes the codebase better, when in reality, writing audits without fixing the code just creates bloat.
6. Permitting the "No LLM" constraint to force the system into a 1990s-era deterministic keyword router.
7. Creating `sector_map.json` which maps tags to sectors in an M:N relationship, guaranteeing false positives.
8. Writing `P-EarningsGravity` into the MVP catalog when it does not exist in the source Frequency Table.
9. Writing `P-AsymmetryLoss` into the MVP catalog when it does not exist in the source Frequency Table.
10. Validating the "Barbell" portfolio concept in docs without writing a single line of code that checks portfolio weightings.
11. Letting the system output "Tata Motors" for "Hospital Expansion" and calling it an acceptable failure rather than a fatal design flaw.
12. Believing `ontology_map.json` could ever scale without semantic embeddings.
13. Designing a contradiction checker that suppresses tactics based on blind tag overlaps.
14. Ignoring negative sentiment parsing (`deactivation_tags`) entirely in the codebase.
15. Focusing on edge-cases (Python 2.7 tests, broken json schemas) while ignoring the core fact that the system couldn't reason.
16. Treating Akshat's YouTube videos as "Doctrine" when financial markets change daily.
17. Building `run_tests.py` to assert against its own hardcoded output rather than a ground-truth dataset.
18. Mapping "rate cut" to "risk_on" automatically, ignoring environments where rate cuts signal a recession (risk_off).
19. Assuming a 0-10 scoring system in Markdown audits held empirical weight.
20. Recommending a "One-Week Improvement Plan" that polishes a broken system rather than demanding a rewrite.

### Top 20 False Assumptions
1. Assuming "Evidence-Driven" meant the evidence was actually verifiable.
2. Assuming `extract_tags()` was extracting meaning, not just substrings.
3. Assuming Phase 1 was "Complete" just because `02_Akshat_Principle_Frequency_Table.md` existed.
4. Assuming the 8-source threshold discovered trends "early."
5. Assuming a Constraint can safely suppress a Tactic just because they share a domain tag.
6. Assuming the system can "generate" a framework without an LLM.
7. Assuming `yfinance` is stable enough for a production stock screener.
8. Assuming the user knows what "K-shaped" means when the system outputs it.
9. Assuming "Sovereign Survival Capex" applies equally to all countries.
10. Assuming `margin_expansion` is always good (ignoring cyclical peaks).
11. Assuming an automated PR system makes a knowledge base immune to human bias.
12. Assuming 50 attack scenarios in a Markdown file makes the Python code resilient.
13. Assuming `parent_id` inheritance solves conflicting logic.
14. Assuming `ANY/ALL` boolean logic handles linguistic nuance.
15. Assuming the MVP needed to be built before the core data was cleansed.
16. Assuming "Phase 2" was a coding phase rather than a data-cleaning phase.
17. Assuming the term "AI" always maps to "Infrastructure."
18. Assuming "Hospital" always maps to "K-shaped."
19. Assuming "Defense" always maps to "Capex."
20. Assuming I could build a Reasoning System without the ability to Reason.

### Top 20 Documentation Artifacts That Should Be Deleted
1. `docs/ai_query_interface.md`
2. `docs/how_to_add_source.md`
3. `docs/mvp_attack_scenarios.md` (It tests a broken system).
4. `docs/edge_case_library.md` (Tests basic python errors, not financial logic).
5. `docs/mvp_test_suite_design.md`
6. `docs/sector_red_team_audit.md` (Bloat, the conclusion is already in the RCA).
7. `docs/dynamic_stock_selection_implementation_plan.md` (Irrelevant until Phase 1 is fixed).
8. `docs/dynamic_stock_selection_mvp_design.md` (Irrelevant).
9. `docs/one_week_improvement_plan.md` (Recommends fixing a dead-end architecture).
10. `docs/principle_taxonomy_review.md` (Abstract theory not tied to the MVP).
11. `docs/repository_cleanup_plan.md` (I am replacing it with this list).
12. `docs/project_readiness_report.md` (It was wrong, the project wasn't ready).
13. `docs/project_red_team_audit.md`
14. `docs/historical_validation_lab.md`
15. `docs/implementation_blockers.md`
16. `docs/implementation_go_no_go_report.md`
17. `docs/end_to_end_execution_walkthrough.md`
18. `docs/mvp_build_blueprint.md`
19. `docs/schema_validation_manual.md`
20. `skills/__init__.py` (And the entire fragmented skills folder).

### Top 20 Documents That Must Survive
*(There aren't 20 worth saving. Here are the 5 that actually matter).*
1. `knowledge/01_Akshat_Master_System.md` (The actual human doctrine).
2. `operating_system/source_naming_rules.md` (The data ingestion rules).
3. `update_engine/08_Akshat_Update_Protocol.md` (The human-in-the-loop logic).
4. `docs/root_cause_analysis.md` (The definitive proof that deterministic routing fails).
5. `docs/goal_drift_analysis.md` (The reminder of what the system is actually supposed to do).
