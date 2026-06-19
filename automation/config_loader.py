#!/usr/bin/env python3
"""
config_loader.py — Centralized config reader.
All scripts should import get_config() from here instead of hardcoding paths.
This ensures a single source of truth: operating_system/config.yaml
"""
import os, yaml

_CONFIG = None

def get_config():
    global _CONFIG
    if _CONFIG is not None:
        return _CONFIG
    # Walk up from this file's location to find operating_system/config.yaml
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cfg_path = os.path.join(base, "operating_system", "config.yaml")
    if not os.path.exists(cfg_path):
        raise FileNotFoundError(f"config.yaml not found at expected path: {cfg_path}")
    with open(cfg_path, encoding="utf-8") as f:
        _CONFIG = yaml.safe_load(f)
    return _CONFIG

if __name__ == "__main__":
    import json
    cfg = get_config()
    print(json.dumps(cfg, indent=2))
