#!/usr/bin/env python3
"""
query_interface.py
L9 — AI Interface Layer

This script provides a simple CLI interface to route a user's query
to the correct workflow and knowledge context.

Usage:
    python scripts/query_interface.py "Analyze Infosys stock"

Outputs:
    - Identified task type
    - Required knowledge files
    - Required skills
    - Workflow to execute
"""

import sys

# Simple keyword-based router (upgrade to LLM classification for production)
ROUTING_TABLE = [
    {
        "keywords": ["stock", "analyze", "buy", "sell", "share", "equity"],
        "workflow": "WF-01: Stock Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.2, 3.3, 3.4, 4.1, 4.2)",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["skills/stock_analysis_skill.md", "skills/valuation_skill.md",
                   "skills/macro_analysis_skill.md"]
    },
    {
        "keywords": ["portfolio", "allocation", "review my", "rebalance"],
        "workflow": "WF-02: Portfolio Review",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 2, 5)",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["skills/portfolio_review_skill.md", "skills/valuation_skill.md"]
    },
    {
        "keywords": ["macro", "liquidity", "rate", "rbi", "fed", "inflation"],
        "workflow": "WF-03: Macro Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.4)",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["skills/macro_analysis_skill.md"]
    },
    {
        "keywords": ["ipo", "listing", "gmp", "apply"],
        "workflow": "WF-04: IPO Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.3, 4.1)",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["skills/ipo_analysis_skill.md", "skills/valuation_skill.md"]
    },
    {
        "keywords": ["earnings", "results", "quarterly", "q1", "q2", "q3", "q4"],
        "workflow": "WF-05: Earnings Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.3)",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["skills/earnings_analysis_skill.md", "skills/valuation_skill.md"]
    },
    {
        "keywords": ["options", "call", "put", "covered", "csp"],
        "workflow": "WF-06: Options Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.5, 4.5)"],
        "skills": ["skills/options_analysis_skill.md"]
    },
    {
        "keywords": ["mutual fund", "sip", "index fund", "nifty 50"],
        "workflow": "WF-07: Mutual Fund Analysis",
        "knowledge": ["knowledge/01_Akshat_Master_System.md (Sec 3.6)"],
        "skills": ["skills/mutual_fund_skill.md"]
    },
]


def route_query(query: str) -> dict:
    query_lower = query.lower()
    for route in ROUTING_TABLE:
        for keyword in route["keywords"]:
            if keyword in query_lower:
                return route
    # Default: Research Request
    return {
        "workflow": "WF-08: Research Request / Framework Extraction",
        "knowledge": ["knowledge/01_Akshat_Master_System.md",
                       "knowledge/04_Akshat_Recent_Changes.md"],
        "skills": ["(Knowledge retrieval — no skill module required)"]
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/query_interface.py \"your question here\"")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    result = route_query(query)

    print(f"\n\u2500\u2500\u2500 AKSHAT-AI-SYSTEM ROUTER \u2500\u2500\u2500")
    print(f"Query     : {query}")
    print(f"Workflow  : {result['workflow']}")
    print(f"\nLoad Knowledge:")
    for f in result["knowledge"]:
        print(f"  \u2192 {f}")
    print(f"\nLoad Skills:")
    for s in result["skills"]:
        print(f"  \u2192 {s}")
    print("\u2500" * 40)


if __name__ == "__main__":
    main()
