import os
import json
import re
import networkx as nx
import time
from pathlib import Path

# Directories to scan
DIRECTORIES_TO_SCAN = ["knowledge", "raw_sources", "skills"]
REPO_ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE_GRAPH_DIR = REPO_ROOT / "knowledge_graph"
ENTITIES_SCHEMA_PATH = KNOWLEDGE_GRAPH_DIR / "entities.json"
ENTITY_DICTIONARY_PATH = KNOWLEDGE_GRAPH_DIR / "entity_dictionary.json"
OUTPUT_JSON_PATH = KNOWLEDGE_GRAPH_DIR / "master_graph.json"
OUTPUT_MD_PATH = KNOWLEDGE_GRAPH_DIR / "master_graph.md"

def load_json(filepath):
    if not filepath.exists():
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def build_alias_map(entity_dictionary):
    alias_map = {}
    for entity_id, data in entity_dictionary.items():
        for alias in data.get("aliases", []):
            alias_map[alias.lower()] = entity_id
        alias_map[entity_id.lower()] = entity_id
    return alias_map

def build_regex_pattern(alias_map):
    # Sort by length descending to match longest alias first
    sorted_aliases = sorted(alias_map.keys(), key=len, reverse=True)
    # Escape aliases for regex
    escaped_aliases = [re.escape(alias) for alias in sorted_aliases]
    # Join into a single regex (with word boundaries)
    pattern = r'\b(' + '|'.join(escaped_aliases) + r')\b'
    return re.compile(pattern, re.IGNORECASE)

def scan_files():
    markdown_files = []
    for d in DIRECTORIES_TO_SCAN:
        dir_path = REPO_ROOT / d
        if dir_path.exists():
            markdown_files.extend(list(dir_path.rglob("*.md")))
            markdown_files.extend(list(dir_path.rglob("*.txt"))) # Include txt files from raw_sources
    return markdown_files

def extract_entities_and_relationships(text, filename, alias_map, regex_pattern, entities_schema):
    """
    Finds entities in the text and creates simple co-occurrence/proximity based relationships,
    or matches explicit relationship keywords between entities.
    """
    edges = []

    # Simple relationship keywords map
    rel_keywords = {
        "supports": ["supports", "agrees with", "reinforces", "backs"],
        "contradicts": ["contradicts", "disagrees with", "goes against"],
        "causes": ["causes", "leads to", "results in"],
        "influenced_by": ["influenced by", "affected by", "driven by"],
        "belongs_to": ["belongs to", "part of", "included in"],
        "strengthens": ["strengthens", "boosts", "increases"],
        "weakens": ["weakens", "reduces", "decreases"],
        "depends_on": ["depends on", "relies on"]
    }

    # We will process paragraph by paragraph or sentence by sentence
    paragraphs = text.split('\n\n')

    for para in paragraphs:
        if not para.strip():
            continue

        # Find all entity matches in the paragraph
        matches = list(regex_pattern.finditer(para))
        if len(matches) >= 2:
            # Check for relationships between adjacent matches
            for i in range(len(matches) - 1):
                match1 = matches[i]
                match2 = matches[i+1]

                entity1_alias = match1.group(0).lower()
                entity2_alias = match2.group(0).lower()

                entity1_id = alias_map.get(entity1_alias)
                entity2_id = alias_map.get(entity2_alias)

                if entity1_id == entity2_id:
                    continue # Same entity

                # Look at the text between the two entities to find relationship keywords
                text_between = para[match1.end():match2.start()].lower()

                found_rel = False
                for rel_type, keywords in rel_keywords.items():
                    if rel_type not in entities_schema.get("relationship_types", []):
                        continue

                    for kw in keywords:
                        if kw in text_between:
                            # We found a relationship
                            edges.append({
                                "source": entity1_id,
                                "target": entity2_id,
                                "relationship": rel_type,
                                "confidence": 0.8, # Based on keyword match
                                "evidence_file": filename,
                                "evidence_snippet": para.strip()[:500], # Store up to 500 chars of context
                                "timestamp": time.strftime('%Y-%m-%d')
                            })
                            found_rel = True
                            break
                    if found_rel:
                        break

                if not found_rel:
                    # Default relationship if they appear close to each other (co-occurrence)
                    # We might not add this if we only want explicit relationships. Let's add "belongs_to" or "influences" with low confidence
                    # Actually, the instructions give specific relationships. Let's just stick to explicit matches for high precision,
                    # or default to "supports" with low confidence if we assume general discussion.
                    # Given the examples, maybe let's just log co-occurrences as "depends_on" or "influenced_by" with 0.5 confidence.
                    # Or better yet, we can skip it to avoid noise, but let's add "depends_on" with 0.5 confidence.
                    edges.append({
                                "source": entity1_id,
                                "target": entity2_id,
                                "relationship": "depends_on",
                                "confidence": 0.5,
                                "evidence_file": filename,
                                "evidence_snippet": para.strip()[:500],
                                "timestamp": time.strftime('%Y-%m-%d')
                            })

    return edges

def build_graph():
    entities_schema = load_json(ENTITIES_SCHEMA_PATH)
    entity_dictionary = load_json(ENTITY_DICTIONARY_PATH)

    if not entities_schema or not entity_dictionary:
        print("Missing schema or dictionary. Exiting.")
        return

    alias_map = build_alias_map(entity_dictionary)
    regex_pattern = build_regex_pattern(alias_map)

    files_to_scan = scan_files()

    # Initialize NetworkX graph (MultiDiGraph allows multiple edges between same nodes)
    G = nx.MultiDiGraph()

    # Add all entities as nodes
    for entity_id, data in entity_dictionary.items():
        G.add_node(entity_id, type=data.get("type", "Unknown"), aliases=data.get("aliases", []))

    all_edges = []

    for filepath in files_to_scan:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Failed to read {filepath}: {e}")
            continue

        filename = filepath.name

        edges = extract_entities_and_relationships(content, filename, alias_map, regex_pattern, entities_schema)

        for edge in edges:
            G.add_edge(edge["source"], edge["target"],
                       relationship=edge["relationship"],
                       confidence=edge["confidence"],
                       evidence_file=edge["evidence_file"],
                       evidence_snippet=edge["evidence_snippet"],
                       timestamp=edge["timestamp"])
            all_edges.append(edge)

    # Save to JSON
    graph_data = {
        "nodes": [{"id": node, **data} for node, data in G.nodes(data=True)],
        "edges": all_edges
    }

    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2)

    # Generate Markdown Summary
    generate_markdown_summary(G, graph_data)

def generate_markdown_summary(G, graph_data):
    nodes = graph_data["nodes"]
    edges = graph_data["edges"]

    md_content = ["# Knowledge Graph Summary\n"]
    md_content.append("## Entity Counts\n")
    md_content.append(f"Total Entities: {len(nodes)}\n")

    type_counts = {}
    for node in nodes:
        t = node.get("type", "Unknown")
        type_counts[t] = type_counts.get(t, 0) + 1

    for t, count in type_counts.items():
        md_content.append(f"- **{t}**: {count}")

    md_content.append("\n## Relationship Counts\n")
    md_content.append(f"Total Relationships: {len(edges)}\n")

    rel_counts = {}
    for edge in edges:
        r = edge.get("relationship", "Unknown")
        rel_counts[r] = rel_counts.get(r, 0) + 1

    for r, count in rel_counts.items():
        md_content.append(f"- **{r}**: {count}")

    md_content.append("\n## Top Connected Entities\n")
    degree_dict = dict(G.degree())
    sorted_nodes = sorted(degree_dict.items(), key=lambda item: item[1], reverse=True)

    for node_id, degree in sorted_nodes[:10]:
        md_content.append(f"- **{node_id}**: {degree} connections")

    md_content.append("\n## Entity Details\n")

    # Process edges to list under entities
    entity_relations = {}
    for edge in edges:
        src = edge["source"]
        tgt = edge["target"]
        rel = edge["relationship"]

        if src not in entity_relations:
            entity_relations[src] = []
        entity_relations[src].append(f"{rel} {tgt}")

    for node in nodes:
        node_id = node["id"]
        node_type = node.get("type", "Unknown")

        md_content.append(f"### {node_id}\n")
        md_content.append(f"Type: {node_type}\n")

        if node_id in entity_relations:
            md_content.append("Relationships:\n")
            # Remove duplicates for the summary display
            unique_rels = set(entity_relations[node_id])
            for rel_str in unique_rels:
                md_content.append(f"- {rel_str}")
        else:
            md_content.append("Relationships: None extracted\n")
        md_content.append("\n")

    with open(OUTPUT_MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

if __name__ == "__main__":
    build_graph()
