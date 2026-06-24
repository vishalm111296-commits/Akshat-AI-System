import json
import pytest
from scripts.mvp.collide import extract_tags, fetch_active_principles, resolve_conflicts

@pytest.fixture
def sample_ontology():
    return {
        "rate cut": ["liquidity_up", "risk_on"],
        "naked options": ["naked_calls", "naked_puts"]
    }

@pytest.fixture
def sample_catalog():
    return [
        {
            "id": "T-01",
            "name": "Buy Tech",
            "type": "tactic",
            "activation_tags": ["liquidity_up"],
            "activation_condition": "ANY"
        },
        {
            "id": "C-01",
            "name": "Never Naked",
            "type": "constraint",
            "activation_tags": ["naked_calls"],
            "activation_condition": "ANY"
        }
    ]

def test_extract_tags(sample_ontology):
    text = "The Fed announces a massive rate cut today."
    tags = extract_tags(text, sample_ontology)
    assert "liquidity_up" in tags
    assert "risk_on" in tags

def test_extract_tags_empty(sample_ontology):
    text = "Nothing happens today."
    tags = extract_tags(text, sample_ontology)
    assert len(tags) == 0

def test_fetch_active_principles(sample_catalog):
    tags = ["liquidity_up"]
    active = fetch_active_principles(tags, sample_catalog)
    assert len(active) == 1
    assert active[0]["principle_id"] == "T-01"

def test_resolve_conflicts():
    # Setup a scenario where constraint and tactic share a triggered tag (e.g. from the same keyword match)
    active = [
        {
            "principle_id": "T-01",
            "type": "tactic",
            "matched_tags": ["danger_tag"],
            "status": "active"
        },
        {
            "principle_id": "C-01",
            "type": "constraint",
            "matched_tags": ["danger_tag"],
            "status": "active"
        }
    ]
    resolved = resolve_conflicts(active)
    # Tactic should be suppressed
    tactic = next(p for p in resolved if p["type"] == "tactic")
    assert tactic["status"] == "suppressed_by_constraint"
    assert tactic["suppressing_constraint_id"] == "C-01"
