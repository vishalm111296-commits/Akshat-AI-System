# 08 — Akshat Update Protocol

> The rulebook governing how new evidence travels from raw source to doctrine. This is the immune system of the knowledge base.

*Layer: L7 — Update Engine*

---

## 1. Classification Rules

Every new piece of content must be classified as exactly **ONE** of:

| Class | Definition | Destination |
|---|---|---|
| `New Idea` | Principle not present in any prior source | `04_Recent_Changes` (new entry) |
| `Repeated Idea` | Principle already in Frequency Table | `02_Frequency_Table` (increment count) |
| `Changed View` | Modifies a previously held tactical view | `04_Recent_Changes` (update entry) |
| `Contradiction` | Directly opposes a Doctrine-level principle | FLAG for human review |
| `Temporary Opinion` | Clearly cycle-specific or event-dependent | `04_Recent_Changes` (with expiry note) |

---

## 2. Frequency Counting Rules

1. Count each **independent source once**, regardless of internal repetitions
2. Sources that qualify: YouTube transcripts, community posts, paid posts, published interviews
3. Sources that NEVER qualify: AI-generated outputs, changelog entries, summary documents, this system's own outputs
4. A source must be **independently published** (not a reshare or duplicate)
5. Counts are **cumulative** — they never reset
6. If the same principle appears in 5 posts on the same day from the same platform — count as 1 (single publication event)

---

## 3. Promotion Hierarchy

```
RAW SOURCE (raw_sources/)
  ↓ [Extract principles]
  ↓ [Classify each principle]
  ↓
FREQUENCY TABLE (02_Akshat_Principle_Frequency_Table.md)
  ↓ [Count: 3+ independent sources over 6+ months]
  ↓
RECENT CHANGES (04_Akshat_Recent_Changes.md)
  ↓ [Count: 8+ independent sources over 2+ time periods]
  ↓ [Human nomination required]
  ↓
MASTER SYSTEM (01_Akshat_Master_System.md)
  ← [Human review + manual PR + evidence log only]
```

---

## 4. Promotion Thresholds

| Promotion | Minimum Sources | Minimum Time Spread | Human Required |
|---|---|---|---|
| Raw → Frequency Table | 1 (first appearance) | — | No |
| Frequency Table → Recent Changes (if new) | 3+ | 6+ months | No |
| Recent Changes → Master System nomination | 8+ | 2+ distinct periods | YES |
| Master System update | 8+ + human review | 2+ distinct periods | YES |

---

## 5. Demotion / Contradiction Rules

- If 2+ independent sources **contradict** a Doctrine principle → flag in `02_Frequency_Table` Contradiction Log + open GitHub Issue
- If a Tactical View has **no reinforcement for 12+ months** → archive from `04_Recent_Changes`
- If a principle was promoted based on **later-invalidated sources** → human review required before demotion
- **Doctrine is never auto-demoted.** Only a human can remove a principle from `01_Master_System`.

---

## 6. What Automation MAY Do

| Action | Allowed |
|---|---|
| Fetch new content from YouTube/RSS | ✅ |
| Store verbatim in `raw_sources/` | ✅ |
| Add entry to `03_Source_Database` | ✅ |
| Update `04_Recent_Changes` | ✅ |
| Increment counts in `02_Frequency_Table` | ✅ |
| Generate `CHANGELOG` entries | ✅ |
| Open GitHub Issues for promotion candidates | ✅ |
| Create draft PR for human review | ✅ |

---

## 7. What Automation MAY NEVER Do

| Action | Forbidden |
|---|---|
| Write to `01_Akshat_Master_System.md` | ❌ NEVER |
| Delete any file in `raw_sources/` | ❌ NEVER |
| Count AI-generated content as a source | ❌ NEVER |
| Promote a principle that appeared only once | ❌ NEVER |
| Auto-merge any PR touching `01_Master` | ❌ NEVER |
| Modify the Contradiction Log without flagging | ❌ NEVER |

---

## 8. Update Protocol Run Sequence

When `automation/run_update_protocol.py` is triggered:

```
1. Scan raw_sources/ for new files since last run
2. For each new file:
   a. Assign Source ID
   b. Add to 03_Source_Database.md
   c. Extract principles (keyword matching + LLM classification)
   d. Classify each principle (New / Repeated / Changed / Contradiction / Temporary)
   e. Update 02_Frequency_Table.md (increment counts)
   f. Update 04_Recent_Changes.md (add/update tactical views)
   g. Generate changelog entry
3. Check for promotion candidates (count ≥ 8, 2+ periods)
4. If candidates found: open GitHub Issue
5. Check for stale views (no reinforcement in 12+ months)
6. If stale views found: flag for archive review
7. Commit all changes
```
