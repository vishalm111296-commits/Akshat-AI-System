# Stock Discovery Test Results

*This document analyzes the outputs of the 10 macro-event tests run against the extended MVP architecture featuring the new Stock Discovery layer.*

---

## 1. Semiconductor incentives
*   **Framework:** Convergence of Follow Government Subsidies & Avoid Capital-Intensive Execution Traps & Follow Geopolitical Supply-Chain Shifts
*   **Sectors:** Semiconductors, EMS Manufacturing, Industrial Automation, Specialty Chemicals
*   **Stocks Discovered:** Amber Enterprises, CG Power, Dixon Tech, Kaynes Technology, Moschip, Syrma SGS, Avalon Tech, Tata Electronics
*   **Failure Analysis:** SUCCESS. The specific sector strings matched exactly, pulling the hardcoded stocks into the report.

## 2. Defense indigenization
*   **Framework:** Convergence of Follow Government Subsidies & Follow Geopolitical Supply-Chain Shifts & Avoid State-Owned Enterprises (PSUs) & Follow Monopsony Buyers
*   **Sectors:** Private Defense Contractors, Aerospace Subsystems, Shipbuilding Components, Precision Engineering
*   **Stocks Discovered:** Azad Engineering, Data Patterns, Dynamatic Tech, Zen Tech, MTAR Tech, Solar Industries
*   **Failure Analysis:** SUCCESS. Exact mapping successful.

## 3. Nuclear incentives
*   **Framework:** Convergence of Follow Government Subsidies & Avoid Capital-Intensive Execution Traps & Avoid State-Owned Enterprises (PSUs)
*   **Sectors:** Private Power Generation, Nuclear Component Suppliers, Heavy Engineering, Uranium Mining
*   **Stocks Discovered:** Adani Power, BHEL, L&T, Tata Power, JSW Energy, Walchandnagar Industries
*   **Failure Analysis:** PARTIAL FAILURE (CIRCULAR LOGIC). The framework explicitly says "Avoid State-Owned Enterprises (PSUs)". However, because the sector mapping triggered "Nuclear Component Suppliers", and the stock map hardcoded "BHEL" under that sector, the system outputted a state-owned enterprise (BHEL) as a "Primary Stock." The stock layer completely ignored the constraints generated in the principle layer.

## 4. Logistics corridors
*   **Framework:** Terminal Value Trap: Avoid Capital-Intensive Execution Traps
*   **Sectors:** Risks (Heavy Manufacturing, Capital Goods, Traditional Infrastructure, Airlines)
*   **Stocks Discovered:** None Identified.
*   **Failure Analysis:** SUCCESSFUL DEGRADATION. As designed, the script only pulls stocks from "Primary" and "Secondary" sectors. Since Logistics only generated "Risk" sectors due to the mapping failure in the previous step, it correctly outputted zero buy candidates.

## 5. Hospital expansion
*   **Framework:** Convergence of Avoid Capital-Intensive Execution Traps & Follow Demographic Destiny
*   **Sectors:** Private Healthcare Chains, Diagnostics Labs, Health Insurance, Medical Devices
*   **Stocks Discovered:** Apollo Hospitals, Dr Lal PathLabs, Max Healthcare, Metropolis, Medanta, Vijaya Diagnostic, Fortis Healthcare
*   **Failure Analysis:** SUCCESS. Exact mapping successful.

## 6. Data center growth
*   **Framework:** Terminal Value Trap: Avoid Capital-Intensive Execution Traps
*   **Sectors:** Risks (Heavy Manufacturing, Capital Goods)
*   **Stocks Discovered:** None Identified.
*   **Failure Analysis:** EXPECTED FAILURE. Cascading failure from the framework generation layer.

## 7. Power grid upgrades
*   **Framework:** Convergence of Avoid Capital-Intensive Execution Traps & Follow Demographic Destiny & Avoid Sunset / ESG Restricted Industries
*   **Sectors:** Renewable Energy Generation, Smart Grid Infrastructure, EV Charging Networks, Energy Storage
*   **Stocks Discovered:** ABB India, Hitachi Energy, KPIL, Tata Power, Adani Green, Siemens India, Suzlon
*   **Failure Analysis:** SUCCESS. Exact mapping successful.

## 8. Water infrastructure
*   **Framework:** Terminal Value Trap: Avoid Capital-Intensive Execution Traps
*   **Sectors:** Risks (Heavy Manufacturing)
*   **Stocks Discovered:** None Identified.
*   **Failure Analysis:** EXPECTED FAILURE.

## 9. Robotics adoption
*   **Framework:** Terminal Value Trap: Avoid Capital-Intensive Execution Traps
*   **Sectors:** Risks (Heavy Manufacturing)
*   **Stocks Discovered:** None Identified.
*   **Failure Analysis:** EXPECTED FAILURE.

## 10. Unknown industry
*   **Framework:** Null Framework
*   **Sectors:** None Identified.
*   **Stocks Discovered:** None Identified.
*   **Failure Analysis:** SUCCESSFUL DEGRADATION.