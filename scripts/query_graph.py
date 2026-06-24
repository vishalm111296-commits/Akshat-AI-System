import json
import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GRAPH_DB_PATH = REPO_ROOT / "knowledge_graph" / "master_graph.json"

def load_graph():
    if not GRAPH_DB_PATH.exists():
        print(f"Error: Graph database not found at {GRAPH_DB_PATH}")
        return None
    with open(GRAPH_DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def print_results(results):
    if not results:
        print("No matching relationships found.")
        return

    print(f"\nFound {len(results)} relationships:\n")
    for r in results:
        print(f"[{r['relationship'].upper()}] {r['source']} -> {r['target']}")
        print(f"  Confidence: {r['confidence']}")
        print(f"  Evidence File: {r['evidence_file']}")
        print(f"  Snippet: \"{r['evidence_snippet'][:100]}...\"")
        print(f"  Timestamp: {r['timestamp']}\n")

def get_entity_id_from_alias(graph_data, alias_query):
    alias_query_lower = alias_query.lower()
    for node in graph_data.get("nodes", []):
        node_id = node["id"]
        if node_id.lower() == alias_query_lower:
            return node_id
        for alias in node.get("aliases", []):
            if alias.lower() == alias_query_lower:
                return node_id
    # Fallback to uppercase if no alias matched
    return alias_query.upper().replace(" ", "_")

def query_structured(graph_data, entity=None, relationship=None):
    edges = graph_data.get("edges", [])
    results = []

    # Normalize inputs
    if entity:
        entity = get_entity_id_from_alias(graph_data, entity)
    if relationship:
        relationship = relationship.lower()

    for edge in edges:
        match = True

        if entity:
            if edge["source"] != entity and edge["target"] != entity:
                match = False

        if relationship:
            if edge["relationship"] != relationship:
                match = False

        if match:
            results.append(edge)

    return results

def query_natural_language(graph_data, query):
    """
    Rule-based natural language parser.
    Example queries:
    "Which principles support AI Supercycle?"
    "What sectors benefit from de-dollarization?"
    "What themes contradict gold accumulation?"
    """

    # 1. Load entities and aliases to detect them in the query
    nodes = graph_data.get("nodes", [])
    alias_map = {}
    node_types = {}

    for node in nodes:
        node_id = node["id"]
        node_types[node_id] = node.get("type", "Unknown")
        for alias in node.get("aliases", []):
            alias_map[alias.lower()] = node_id
        alias_map[node_id.lower()] = node_id

    query_lower = query.lower()

    # 2. Extract entities from query
    detected_entities = set()
    # Sort aliases by length descending to match longest first
    sorted_aliases = sorted(alias_map.keys(), key=len, reverse=True)

    for alias in sorted_aliases:
        if re.search(r'\b' + re.escape(alias) + r'\b', query_lower):
            detected_entities.add(alias_map[alias])

    # 3. Extract relationship keywords from query
    rel_keywords = {
        "supports": ["support", "supports", "reinforce", "reinforces", "backs"],
        "contradicts": ["contradict", "contradicts", "disagrees with"],
        "causes": ["cause", "causes", "leads to"],
        "influenced_by": ["influenced by", "affected by"],
        "belongs_to": ["belongs to", "part of"],
        "strengthens": ["strengthens", "boosts", "increases", "benefit from", "benefits from", "benefit"],
        "weakens": ["weakens", "reduces", "decreases"],
        "depends_on": ["depends on", "relies on"]
    }

    detected_relationship = None
    for rel, keywords in rel_keywords.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', query_lower):
                detected_relationship = rel
                break
        if detected_relationship:
            break

    # 4. Extract target node type if specified
    # e.g., "Which principles...", "What sectors...", "What themes..."
    type_keywords = {
        "Person": ["person", "people"],
        "Company": ["company", "companies"],
        "Sector": ["sector", "sectors"],
        "Theme": ["theme", "themes"],
        "Country": ["country", "countries"],
        "AssetClass": ["asset class", "asset classes", "assets"],
        "Risk": ["risk", "risks"],
        "InvestmentPrinciple": ["principle", "principles", "investment principle"],
        "MacroTrend": ["macro trend", "macro trends", "trend", "trends"],
        "EconomicIndicator": ["economic indicator", "indicator", "indicators"]
    }

    target_type = None
    for t_type, keywords in type_keywords.items():
        for kw in keywords:
            if re.search(r'\b' + re.escape(kw) + r'\b', query_lower):
                target_type = t_type
                break
        if target_type:
            break

    print(f"Parsed Query - Entities: {list(detected_entities)}, Relationship: {detected_relationship}, Target Type: {target_type}")

    # 5. Filter graph
    edges = graph_data.get("edges", [])
    results = []

    for edge in edges:
        match = True

        if detected_entities:
            if edge["source"] not in detected_entities and edge["target"] not in detected_entities:
                match = False

        # If the user asks for a specific relationship, or we map "benefit from" to "strengthens", but our graph only has "depends_on",
        # a strict match might return nothing. We'll do a strict match if a relationship was explicitly detected.
        if detected_relationship:
            # We also map "benefit" to "strengthens" etc., so we should check if the edge matches
            if edge["relationship"] != detected_relationship:
                match = False

        if target_type:
            # Check if either source or target has the desired type
            # And it should not be the entity we already filtered by
            src_type = node_types.get(edge["source"])
            tgt_type = node_types.get(edge["target"])

            if src_type != target_type and tgt_type != target_type:
                match = False

            # If we know the entity we're looking FOR (the target type), and the entity we are pivoting FROM
            if detected_entities:
                pivot_entity = list(detected_entities)[0]
                if edge["source"] == pivot_entity and tgt_type != target_type:
                    match = False
                if edge["target"] == pivot_entity and src_type != target_type:
                    match = False

        if match:
            results.append(edge)

    return results

def main():
    parser = argparse.ArgumentParser(description="Query the Akshat Investment Knowledge Graph")

    # Structured arguments
    parser.add_argument("--entity", type=str, help="Filter by entity ID (e.g., AI_SUPERCYCLE)")
    parser.add_argument("--relationship", type=str, help="Filter by relationship type (e.g., supports)")

    # Natural language argument
    parser.add_argument("--query", type=str, help="Natural language query (e.g., 'Which principles support AI Supercycle?')")

    args = parser.parse_args()

    graph_data = load_graph()
    if not graph_data:
        return

    if args.query:
        print(f"Running natural language query: '{args.query}'")
        results = query_natural_language(graph_data, args.query)
        print_results(results)
    elif args.entity or args.relationship:
        print(f"Running structured query - Entity: {args.entity}, Relationship: {args.relationship}")
        results = query_structured(graph_data, entity=args.entity, relationship=args.relationship)
        print_results(results)
    else:
        print("Please provide a --query or --entity/--relationship. Use -h for help.")

if __name__ == "__main__":
    main()
