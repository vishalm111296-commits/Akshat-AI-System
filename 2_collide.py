import json
import sys
import os
import argparse

def load_json(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_tags(text, ontology):
    text_lower = text.lower()
    tags = set()
    for keyword, matched_tags in ontology.items():
        if keyword.lower() in text_lower:
            tags.update(matched_tags)
    return list(tags)

def fetch_active_principles(tags, catalog):
    active = []
    tags_set = set(tags)
    for p in catalog:
        p_tags = set(p.get("activation_tags", []))
        if tags_set.intersection(p_tags):
            active.append({
                "id": p["id"],
                "name": p["name"],
                "type": p["type"]
            })
    return active

def fetch_sectors(tags, sector_map):
    aggregated_sectors = {
        "Primary": set(),
        "Secondary": set(),
        "Beneficiary": set(),
        "Risk": set()
    }

    for tag in tags:
        if tag in sector_map:
            mapping = sector_map[tag]
            for category in aggregated_sectors.keys():
                if category in mapping:
                    aggregated_sectors[category].update(mapping[category])

    # Convert sets back to sorted lists
    for key in aggregated_sectors:
        aggregated_sectors[key] = sorted(list(aggregated_sectors[key]))

    return aggregated_sectors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default="sample_macro_event.json")
    parser.add_argument("--catalog", default="core_catalog.json")
    parser.add_argument("--ontology", default="ontology_map.json")
    parser.add_argument("--sectormap", default="sector_map.json")
    parser.add_argument("--output", default="generated_framework_report.md")
    args = parser.parse_args()

    event = load_json(args.event)
    catalog = load_json(args.catalog)
    ontology = load_json(args.ontology)
    sector_map = load_json(args.sectormap)

    raw_text = event.get("raw_text", "")
    tags = extract_tags(raw_text, ontology)

    active = fetch_active_principles(tags, catalog)
    sectors = fetch_sectors(tags, sector_map)

    constraints = [p for p in active if p["type"] == "constraint"]
    tactics = [p for p in active if p["type"] == "tactic"]

    md = f"# Generated Framework Report\n\n"
    md += f"**Input Event:** {raw_text}\n"
    md += f"**Extracted Tags:** {', '.join(tags) if tags else 'None'}\n\n"

    md += "## Activated Principles\n"
    if active:
        for p in active:
            md += f"- [{p['type'].upper()}] {p['id']}: {p['name']}\n"
    else:
        md += "None.\n"
    md += "\n"

    md += "## Generated Framework\n"
    if not active:
        md += "No actionable principles found for this macro event.\n"
    else:
        md += "Based on the macro input, the following framework is proposed:\n\n"
        if constraints:
            md += "**CRITICAL CONSTRAINTS:**\n"
            for c in constraints:
                md += f"- Must adhere to: {c['name']}\n"
            md += "\n"
        if tactics:
            md += "**TACTICAL ACTIONS:**\n"
            for t in tactics:
                md += f"- Execute strategy: {t['name']}\n"
            md += "\n"

    md += "## Affected Sectors\n"
    has_sectors = any(sectors.values())
    if not has_sectors:
        md += "No sectors identified.\n"
    else:
        for category, items in sectors.items():
            if items:
                md += f"**{category}:**\n"
                for item in items:
                    md += f"- {item}\n"
                md += "\n"

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(md)

if __name__ == "__main__":
    main()
