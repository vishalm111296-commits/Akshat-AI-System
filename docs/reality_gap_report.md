# Reality Gap Report

## Overview
This document compares the grandiose claims of the Akshat Reasoning System Architecture against the physical reality of the MVP implementation.

---

## Gap 1: Discovery vs. Dictionary
* **Claim:** "Emerging Framework Detection Engine identifies new mental models via velocity and novelty scoring before they gain multi-year persistence."
* **Reality:** The MVP relies on `ontology_map.json`, a hardcoded dictionary. It cannot detect anything that is not explicitly pre-programmed by a human. There is no velocity scoring. There is no novelty detection.

## Gap 2: Generative Reasoning vs. Tag Collision
* **Claim:** "The Macro-to-Principle Collision Engine shifts the architecture from reactive to generative by combining hard macro data with Core Principles."
* **Reality:** The system splits a string, looks up matching array keys, and prints the corresponding JSON `name` property. It generates absolutely zero new text, insights, or combinations. It is a filter, not a generator.

## Gap 3: Principle Extraction vs. Manual Data Entry
* **Claim:** "Utilizes a Hybrid pipeline for concept extraction, theme detection, and principle scoring."
* **Reality:** The MVP specifically bans the extraction pipeline. `core_catalog.json` had to be manually typed out by the developer. The system currently cannot read, extract, or score YouTube transcripts.

## Gap 4: Hierarchical Taxonomy vs. Flat Output
* **Claim:** "The Principle Catalog must enforce a strict Principle Taxonomy hierarchy (Parent -> Child -> Tactic/Constraint) to prevent flat hierarchies."
* **Reality:** The MVP JSON contains `parent_id` fields, but `collide.py` completely ignores them when generating the report. It prints Parents and Children side-by-side as a flat list.

## Gap 5: Conflict Resolution vs. Blind Suppression
* **Claim:** "The system integrates a Doubt Engine to challenge theses and resolve conflicting principles."
* **Reality:** `collide.py` resolves conflicts using a brute-force loop: if a Tactic shares *any* tag with a Constraint, the Tactic is deleted. It does not understand *why* they conflict or if the constraint is actually relevant to the specific domain.

## Gap 6: Alpha Generation vs. Mad Libs
* **Claim:** "Convert trends into sectors → Convert sectors into stocks."
* **Reality:** The system outputs: `"We are entering a [capex_cycle] driving [margin_expansion] in [tech_hardware]. Action: Identify profit-expanding companies..."` It does not identify a single sector or stock. It just regurgitates the input tags back to the user in a template.
