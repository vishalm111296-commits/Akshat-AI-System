"""
Token-efficient skill loader.
Loads ONLY the skill relevant to the task based on trigger keywords.
Never loads all skills at once — focused context beats large context.
"""

import os
import re
from pathlib import Path
from typing import Optional

SKILLS_DIR = Path(__file__).parent

def parse_frontmatter(filepath: Path) -> dict:
    """Extract YAML frontmatter from a .md skill file."""
    content = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
        elif line.startswith("  - "):
            last_key = list(fm.keys())[-1]
            if not isinstance(fm[last_key], list):
                fm[last_key] = []
            fm[last_key].append(line.strip("  - ").strip())
    return fm

def load_skill(task_description: str) -> Optional[str]:
    """
    Given a task description, find and return the content of the
    most relevant skill .md file. Returns None if no match found.

    Usage:
        context = load_skill("analyze earnings for RELIANCE")
        # Returns content of earnings_analysis_skill.md
    """
    task_lower = task_description.lower()
    best_match = None
    best_score = 0

    for md_file in SKILLS_DIR.glob("*_skill.md"):
        fm = parse_frontmatter(md_file)
        triggers = fm.get("triggers", [])
        if isinstance(triggers, str):
            triggers = [triggers]

        score = sum(1 for t in triggers if t.lower() in task_lower)
        if score > best_score:
            best_score = score
            best_match = md_file

    if best_match and best_score > 0:
        return best_match.read_text(encoding="utf-8")
    return None

def list_available_skills() -> list[dict]:
    """Return a summary list of all available skills with their triggers."""
    skills = []
    for md_file in sorted(SKILLS_DIR.glob("*_skill.md")):
        fm = parse_frontmatter(md_file)
        skills.append({
            "name": fm.get("name", md_file.stem),
            "description": fm.get("description", ""),
            "triggers": fm.get("triggers", []),
            "file": md_file.name,
        })
    return skills
