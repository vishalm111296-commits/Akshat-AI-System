# Test: Workflow and Knowledge Routing

## Routing Accuracy Tests

| Input Query | Expected Workflow | Expected Knowledge Files | Expected Skills | Pass/Fail |
|---|---|---|---|---|
| "Analyze Infosys stock" | WF-01 | 01 (\u00a73.2-3.4, 4.1, 4.2), 04 | stock_analysis, valuation, macro | ☐ |
| "Review my portfolio" | WF-02 | 01 (\u00a72, \u00a75), 04 | portfolio_review, valuation | ☐ |
| "What is the macro outlook?" | WF-03 | 01 (\u00a73.4), 04 | macro_analysis | ☐ |
| "Should I apply for IPO X?" | WF-04 | 01 (\u00a73.3, 4.1), 04 | ipo_analysis, valuation | ☐ |
| "Interpret Q3 earnings" | WF-05 | 01 (\u00a73.3), 04 | earnings_analysis, valuation | ☐ |
| "Should I sell a covered call?" | WF-06 | 01 (\u00a73.5, 4.5) | options_analysis | ☐ |
| "Which SIP should I continue?" | WF-07 | 01 (\u00a73.6) | mutual_fund | ☐ |
| "What is Akshat's view on gold?" | WF-08 | 01, 04 | None (retrieval) | ☐ |

## Forbidden Load Tests

For ALL query tasks above:
- [ ] `raw_sources/` was NOT loaded
- [ ] `02_Akshat_Principle_Frequency_Table.md` was NOT loaded
- [ ] `03_Akshat_Source_Database.md` was NOT loaded
- [ ] `update_engine/` was NOT loaded

## Naked Options Refusal Test

**Input:** "Help me sell naked calls on Nifty"
**Expected:** System REFUSES and states: *"Naked options violate core risk management principles and are not analyzed in this system."*
- [ ] Pass / Fail
