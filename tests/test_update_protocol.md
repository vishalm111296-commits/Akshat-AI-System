# Test: Update Protocol (08_Akshat_Update_Protocol)

## Test Case 1 — New Source Ingested

**Action:** Add new file to `raw_sources/youtube_transcripts/`

**Expected Behaviour:**
- [ ] Source assigned unique ID in `03_Akshat_Source_Database.md`
- [ ] File stored verbatim (not modified)
- [ ] Principles classified (New / Repeated / Changed / Contradiction / Temporary)
- [ ] `02_Frequency_Table.md` updated (count incremented by 1 per relevant principle)
- [ ] `01_Akshat_Master_System.md` NOT modified
- [ ] `CHANGELOG.md` entry generated
- [ ] `.automation_state/processed_sources.json` updated

---

## Test Case 2 — Repeated Principle

**Action:** New source reinforces "Buy near 200DMA" principle

**Expected Behaviour:**
- [ ] Count for SS-04 incremented by exactly 1
- [ ] New source ID added to sources list for SS-04
- [ ] NOT counted twice if same source referenced in multiple runs

---

## Test Case 3 — AI Output Protection

**Action:** Attempt to add AI-generated summary to `raw_sources/`

**Expected Behaviour:**
- [ ] System must not count this as an independent source
- [ ] File naming: if filename contains `generated`, `summary`, or `analysis` → flag

---

## Test Case 4 — Promotion Candidate Detection

**Action:** Principle reaches count = 8 across 2 time periods

**Expected Behaviour:**
- [ ] GitHub Issue opened (if `check_promotion_candidates()` is implemented)
- [ ] `01_Akshat_Master_System.md` NOT auto-modified
- [ ] Human review required before any change

---

## Test Case 5 — Stale Tactical View

**Action:** A view in `04_Recent_Changes.md` has no reinforcement for 12+ months

**Expected Behaviour:**
- [ ] View flagged for archive review
- [ ] NOT automatically deleted
- [ ] Human confirmation required before archiving
