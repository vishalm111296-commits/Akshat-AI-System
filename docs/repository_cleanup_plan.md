# Repository Cleanup Plan

*This plan consolidates the sprawling architectural documents generated during Phase 1 and 2 into a clean, maintainable structure, removing dead concepts and redundancies.*

## 1. KEEP (Immutable System Files)
*These files represent the final, agreed-upon architecture and must not be touched.*
*   `knowledge/01_Akshat_Master_System.md` (The human-gated doctrine)
*   `knowledge/principles/core_catalog.json` (The active MVP principle base)
*   `operating_system/system_rules.md` (Repo constitution)
*   `scripts/mvp/2_collide.py` (The MVP engine)
*   `scripts/mvp/ontology_map.json` (The semantic router)

## 2. MERGE (Consolidate Architecture Docs)
*The system currently has too many overlapping design documents. They must be merged into a single `System_Architecture_v2.md` manual.*
*   Merge `docs/principle_extraction_architecture.md`
*   Merge `docs/emerging_framework_detection_engine.md`
*   Merge `docs/macro_collision_engine_architecture.md`
    *   *Action:* Combine these into `docs/ARCHITECTURE_MANUAL.md`.

*Consolidate the testing and audit documents into a QA directory.*
*   Merge `docs/architecture_validation_simulation.md`
*   Merge `docs/emerging_framework_stress_test.md`
*   Merge `docs/project_red_team_audit.md`
*   Merge `docs/mvp_attack_scenarios.md`
*   Merge `docs/historical_validation_lab.md`
    *   *Action:* Combine these into `docs/qa/SYSTEM_TEST_PLAN.md`.

## 3. DELETE (Dead Architecture & Redundancies)
*These files represent deprecated ideas, overly complex non-MVP phases, or redundant placeholders.*
*   `knowledge/principles/principle_catalog.md` (Redundant; replaced by `core_catalog.json` for MVP)
*   `knowledge/principles/principle_evidence_map.md` (Too complex for MVP; tracking is deferred)
*   `knowledge/principles/principle_confidence_scores.json` (Math is suspended for MVP)
*   `scripts/extract_principles.py` (The Phase 1 placeholder is dead; MVP uses `scripts/mvp/1_extract.py` conceptually, but really relies on manual JSON creation for the freeze).
*   `docs/principle_extraction_adversarial_review.md` (Lessons absorbed into the Red Team Audit; delete to reduce clutter).
*   `docs/mvp_implementation_plan.md` (Superseded completely by `mvp_ruthless_audit_specification.md` and `mvp_implementation_freeze.md`).