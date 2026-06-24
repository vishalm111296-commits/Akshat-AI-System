"""
Skills package for Akshat-AI-System.

IMPORTANT: Do not import all skills at startup.
Use skill_loader.load_skill(task_description) to load
only the skill relevant to the current task.

Token-efficient context loading: 2,000 lines of focused
context beats 10,000 lines of scattered context.
"""

from skills.skill_loader import load_skill, list_available_skills

__all__ = ["load_skill", "list_available_skills"]
