#!/usr/bin/env python3
"""
collide.py - MVP Macro-to-Principle Collision Engine
Reads an event, maps via ontology, fetches principles, applies constraints, outputs markdown.
"""
import json
import sys
import os
import argparse

def load_json(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Missing required file: {filepath}")
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
        condition = p.get("activation_condition", "ANY")

        matches = False
        if condition == "ANY" and tags_set.intersection(p_tags):
            matches = True
        elif condition == "ALL" and p_tags and p_tags.issubset(tags_set):
            matches = True

        if matches:
            active.append({
                "principle_id": p["id"],
                "name": p["name"],
                "type": p["type"],
                "matched_tags": list(tags_set.intersection(p_tags)),
                "status": "active",
                "suppressing_constraint_id": None
            })
    return active

def resolve_conflicts(active_principles):
    """
    Very basic MVP conflict resolution:
    If a constraint is active, it flags. In a deeper engine, we'd map constraint domain to tactic domain.
    For this blueprint, constraints suppress ALL tactics that share ANY matched_tag.
    """
    constraints = [p for p in active_principles if p["type"] == "constraint"]
    tactics = [p for p in active_principles if p["type"] == "tactic"]

    for t in tactics:
        t_tags = set(t["matched_tags"])
        for c in constraints:
            c_tags = set(c["matched_tags"])
            # If they triggered on the exact same underlying ontology tag, constraint blocks tactic
            if t_tags.intersection(c_tags):
                t["status"] = "suppressed_by_constraint"
                t["suppressing_constraint_id"] = c["principle_id"]
                break

    return active_principles

def generate_markdown(event, extracted_tags, active_principles, out_dir):
    event_id = event.get("event_id", "UNKNOWN-EVENT")
    date = event.get("date", "YYYY-MM-DD")
    raw_text = event.get("raw_text", "")

    constraints = [p for p in active_principles if p["type"] == "constraint" and p["status"] == "active"]
    tactics = [p for p in active_principles if p["type"] == "tactic" and p["status"] == "active"]
    suppressed = [p for p in active_principles if p["status"] == "suppressed_by_constraint"]
    themes = [p for p in active_principles if p["type"] in ("parent", "child")]

    md = f"# Reasoning Report: {event_id}\n"
    md += f"**Date:** {date}\n\n"
    md += f"## 1. Summary of Macro Event\n{raw_text}\n\n"
    md += f"**Extracted Tags:** {', '.join(extracted_tags) if extracted_tags else 'None'}\n\n"

    md += "## 2. Activated Constraints (Hard Boundaries)\n"
    if constraints:
        for c in constraints:
            md += f"- **{c['principle_id']}**: {c['name']} (Triggered by: {', '.join(c['matched_tags'])})\n"
    else:
        md += "- None triggered.\n"
    md += "\n"

    md += "## 3. Activated Tactics (Offensive Actions)\n"
    if tactics:
        for t in tactics:
            md += f"- **{t['principle_id']}**: {t['name']}\n"
    else:
        md += "- None active.\n"
    md += "\n"

    if suppressed:
        md += "## Suppressed Tactics\n"
        for s in suppressed:
            md += f"- ~{s['principle_id']}: {s['name']}~ (Blocked by {s['suppressing_constraint_id']})\n"
        md += "\n"

    md += "## 4. Structural Themes\n"
    for t in themes:
        md += f"- **{t['principle_id']}**: {t['name']}\n"

    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, f"{event_id}.md")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md)
    return out_file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", default="tests/mvp/macro_input.json", help="Path to macro event JSON")
    parser.add_argument("--catalog", default="knowledge/principles/core_catalog.json", help="Path to core catalog JSON")
    parser.add_argument("--ontology", default="scripts/mvp/ontology_map.json", help="Path to ontology map JSON")
    parser.add_argument("--outdir", default="docs/mvp_output/generated_frameworks", help="Output directory")
    args = parser.parse_args()

    try:
        event = load_json(args.event)
        catalog = load_json(args.catalog)
        ontology = load_json(args.ontology)

        tags = extract_tags(event.get("raw_text", ""), ontology)
        if not tags:
            print("No tags extracted. Exiting cleanly.")
            # Still generate a report
            generate_markdown(event, [], [], args.outdir)
            sys.exit(0)

        active = fetch_active_principles(tags, catalog)
        resolved = resolve_conflicts(active)

        out_path = generate_markdown(event, tags, resolved, args.outdir)
        print(f"Success. Report generated at: {out_path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
