# DDD Decision Log

> **APPEND-ONLY.** Following Doubt-Driven Development (DDD).

---

## 2026-06-24 — Add DDD guard comments to automation/ and pre-flight check

- **CLAIM:** This change introduces system-level invariants and function-level doubt gates to prevent overconfident or unauthorized automated writes to the knowledge base.
- **CYCLES:** 1
- **CONTRACT:** All automation write operations must pass the pre-flight check, and all critical write/decision functions must be preceded by a DDD review process.
- **FINDINGS:** Initial automation lacked explicit checks for system state (like missing master file) or execution context (like running in PR). Function-level logic lacked formal "doubt" gates, increasing the risk of overconfident automated updates.
- **DECISION:** Implement a centralized `pre_flight_check()` in the orchestrator and add `# ⚠️ DDD GATE` comments to all direct-write and decision-making functions in the automation suite.

---
