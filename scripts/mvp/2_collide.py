import json
import argparse
import sys
import os

def load_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filepath}")
        sys.exit(1)

def abstract_tags(input_tags, ontology):
    abstracted = set()
    for tag in input_tags:
        tag_lower = tag.lower()
        if tag_lower in ontology:
            for abstract_tag in ontology[tag_lower]:
                abstracted.add(abstract_tag.lower())
        else:
            abstracted.add(tag_lower)
    return abstracted

def find_activated_principles(abstracted_tags, catalog):
    activated = []
    for principle in catalog:
        principle_tags = set([t.lower() for t in principle.get("activation_tags", [])])
        if abstracted_tags.intersection(principle_tags):
            activated.append(principle)
    return activated

def synthesize_framework(activated_principles):
    if not activated_principles:
        return "Null Framework", "No activated principles. Cannot synthesize framework."

    pos_count = sum(1 for p in activated_principles if p.get("polarity", "").lower() == "positive")
    neg_count = sum(1 for p in activated_principles if p.get("polarity", "").lower() == "negative")

    titles = [p.get("title", "") for p in activated_principles]

    if pos_count > 0 and neg_count > 0:
        framework_title = f"Convergence of {' & '.join(titles)}"
    elif pos_count > 0 and neg_count == 0:
        framework_title = f"Pure Structural Tailwind: {' & '.join(titles)}"
    elif pos_count == 0 and neg_count > 0:
        framework_title = f"Terminal Value Trap: {' & '.join(titles)}"
    else:
        framework_title = "Undefined Framework"

    reasoning_parts = []
    for p in activated_principles:
        prefix = "TAILWIND:" if p.get("polarity", "").lower() == "positive" else "CONSTRAINT:"
        reasoning_parts.append(f"{prefix} {p.get('description', '')}")

    reasoning_text = " ".join(reasoning_parts)
    return framework_title, reasoning_text

def discover_sectors(framework_title, sector_map):
    # Retrieve the sector mapping for the exact framework title.
    # If not found, return empty structures.
    return sector_map.get(framework_title, {
        "primary": [],
        "secondary": [],
        "beneficiaries": [],
        "risks": []
    })

def discover_stocks(sectors, stock_map):
    # Collects stocks for all primary and secondary sectors.
    # In a real system, we wouldn't map stocks to "risk" sectors as buys.
    all_primary_stocks = set()
    all_secondary_stocks = set()
    all_watchlist_stocks = set()

    # We only pull candidate stocks from Primary and Secondary sectors identified by the framework.
    candidate_sectors = sectors.get("primary", []) + sectors.get("secondary", [])

    for sector in candidate_sectors:
        mapped = stock_map.get(sector, {})
        all_primary_stocks.update(mapped.get("primary", []))
        all_secondary_stocks.update(mapped.get("secondary", []))
        all_watchlist_stocks.update(mapped.get("watchlist", []))

    return {
        "primary": sorted(list(all_primary_stocks)),
        "secondary": sorted(list(all_secondary_stocks)),
        "watchlist": sorted(list(all_watchlist_stocks))
    }

def generate_report(event, activated, framework_title, reasoning, sectors, stocks, output_file=None):
    lines = []
    event_id = event.get("event_id", "UNKNOWN-EVENT")

    lines.append(f"# Reasoning Report: {event_id}\n")
    lines.append(f"**Event:** {event.get('description', '')}\n")
    lines.append("**Activated Principles:**")

    if not activated:
        lines.append("- None")
    else:
        for p in activated:
            mark = "x" if p.get("polarity", "").lower() == "positive" else "!"
            polarity_label = "Tailwind" if p.get("polarity", "").lower() == "positive" else "Constraint"
            lines.append(f"- [{mark}] {p.get('title', '')} ({polarity_label})")

    lines.append(f"\n**Synthesized Framework:** *{framework_title}*\n")
    lines.append(f"**Reasoning:** {reasoning}\n")

    lines.append("**Affected Sectors:**")
    if not sectors.get("primary"):
        lines.append("- Primary: None Identified")
    else:
        lines.append(f"- Primary: {', '.join(sectors['primary'])}")

    if not sectors.get("secondary"):
        lines.append("- Secondary: None Identified")
    else:
        lines.append(f"- Secondary: {', '.join(sectors['secondary'])}")

    if not sectors.get("beneficiaries"):
        lines.append("- Beneficiaries: None Identified")
    else:
        lines.append(f"- Beneficiaries: {', '.join(sectors['beneficiaries'])}")

    if not sectors.get("risks"):
        lines.append("- Risks: None Identified\n")
    else:
        lines.append(f"- Risks: {', '.join(sectors['risks'])}\n")

    lines.append("**Candidate Stocks:**")
    if not stocks.get("primary"):
        lines.append("- Primary Stocks: None Identified")
    else:
        lines.append(f"- Primary Stocks: {', '.join(stocks['primary'])}")

    if not stocks.get("secondary"):
        lines.append("- Secondary Stocks: None Identified")
    else:
        lines.append(f"- Secondary Stocks: {', '.join(stocks['secondary'])}")

    if not stocks.get("watchlist"):
        lines.append("- Watchlist: None Identified")
    else:
        lines.append(f"- Watchlist: {', '.join(stocks['watchlist'])}\n")

    report_content = "\n".join(lines)

    if output_file:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as f:
            f.write(report_content)
        print(f"Report generated: {output_file}")

    return report_content

def main():
    parser = argparse.ArgumentParser(description="Macro Collision MVP")
    parser.add_argument("--macro", type=str, help="JSON string of macro event")
    parser.add_argument("--output", type=str, help="Path to write markdown output")
    args = parser.parse_args()

    # Define paths relative to repo root
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    catalog_path = os.path.join(repo_root, "knowledge", "principles", "core_catalog.json")
    ontology_path = os.path.join(repo_root, "scripts", "mvp", "ontology_map.json")
    sector_map_path = os.path.join(repo_root, "scripts", "mvp", "sector_map.json")
    stock_map_path = os.path.join(repo_root, "scripts", "mvp", "stock_map.json")
    default_macro_path = os.path.join(repo_root, "scripts", "mvp", "sample_macro_event.json")

    catalog = load_json(catalog_path)
    ontology = load_json(ontology_path)
    sector_map = load_json(sector_map_path)
    stock_map = load_json(stock_map_path)

    if args.macro:
        try:
            event = json.loads(args.macro)
        except json.JSONDecodeError:
            print("Error: Invalid JSON passed to --macro")
            sys.exit(1)
    else:
        event = load_json(default_macro_path)

    trigger_tags = event.get("trigger_tags", [])
    abstracted_tags = abstract_tags(trigger_tags, ontology)

    activated_principles = find_activated_principles(abstracted_tags, catalog)

    framework_title, reasoning_text = synthesize_framework(activated_principles)
    sectors = discover_sectors(framework_title, sector_map)
    stocks = discover_stocks(sectors, stock_map)

    output_path = args.output
    if not output_path and not args.macro:
        output_path = os.path.join(repo_root, "docs", "mvp_output", f"generated_framework_report.md")

    report = generate_report(event, activated_principles, framework_title, reasoning_text, sectors, stocks, output_path)

    # Also print to stdout for easy reading during tests
    if args.macro:
        print(report)

if __name__ == "__main__":
    main()