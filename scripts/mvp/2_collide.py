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

def generate_report(event, activated, framework_title, reasoning, output_file=None):
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
    default_macro_path = os.path.join(repo_root, "scripts", "mvp", "sample_macro_event.json")

    catalog = load_json(catalog_path)
    ontology = load_json(ontology_path)

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

    output_path = args.output
    if not output_path and not args.macro:
        output_path = os.path.join(repo_root, "docs", "mvp_output", f"generated_framework_report.md")

    report = generate_report(event, activated_principles, framework_title, reasoning_text, output_path)

    # Also print to stdout for easy reading during tests
    if args.macro:
        print(report)

if __name__ == "__main__":
    main()