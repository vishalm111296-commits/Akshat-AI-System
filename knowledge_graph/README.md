# Knowledge Graph Layer

This directory contains the schemas and outputs for the Akshat Investment Knowledge Graph.
The system parses deterministic relationships from markdown text across `knowledge/`, `raw_sources/`, and `skills/` to build a queryable, machine-readable graph.

## Schema definitions

- `entities.json`: Defines the allowed Entity types (e.g. `MacroTrend`, `Company`) and Relationship types (e.g. `supports`, `contradicts`, `depends_on`).
- `entity_dictionary.json`: Maps standard entity IDs (e.g. `AI_SUPERCYCLE`) to their real-world string aliases found in text (e.g. `Artificial Intelligence`, `AI boom`).

## Building the Graph

To extract the graph from text, run:

```bash
python scripts/build_knowledge_graph.py
```

This scans all tracked markdown files using strict keyword and regex matching (no LLMs are used) to guarantee determinism. The graph output is saved to:
- `master_graph.json`: The raw system database.
- `master_graph.md`: A human-readable markdown summary.

## Querying the Graph

To query the knowledge graph, use `scripts/query_graph.py`.

**Structured Query:**
```bash
python scripts/query_graph.py --entity "AI_SUPERCYCLE" --relationship "depends_on"
```

**Natural Language Query (Rule-based):**
```bash
python scripts/query_graph.py --query "What companies depend on AI Supercycle?"
```

Each relationship output includes the underlying evidence, source file, confidence score, and timestamp.