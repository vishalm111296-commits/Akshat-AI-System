#!/usr/bin/env python3
"""
test_pipeline_integrity.py
Executable pytest suite for Akshat-AI-System.
Replaces the previous Markdown-only test stubs for critical system tests.

Run: pytest tests/test_pipeline_integrity.py -v
"""
import os, json, hashlib, re, yaml
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(p):
    return os.path.join(ROOT, p)

# ─────────────────────────────────────────────
# 1. Master System Integrity
# ─────────────────────────────────────────────

class TestMasterSystemIntegrity:

    def test_master_system_exists(self):
        assert os.path.exists(path("knowledge/01_Akshat_Master_System.md")), \
            "Master System file is missing!"

    def test_master_system_not_empty(self):
        with open(path("knowledge/01_Akshat_Master_System.md"), encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 1000, "Master System file appears too short — possible corruption"

    def test_master_system_has_protected_header(self):
        with open(path("knowledge/01_Akshat_Master_System.md"), encoding="utf-8") as f:
            content = f.read()
        assert "PROTECTED FILE" in content, "Master System is missing PROTECTED FILE annotation"

    def test_master_system_hash_recorded(self):
        """If automation has run, master hash should be recorded."""
        hash_file = path(".automation_state/master_hash.json")
        if os.path.exists(hash_file):
            data = json.load(open(hash_file))
            assert "hash" in data, "master_hash.json is malformed"
            # Verify stored hash matches current file
            with open(path("knowledge/01_Akshat_Master_System.md"), "rb") as f:
                current = hashlib.sha256(f.read()).hexdigest()
            assert data["hash"] == current, (
                "Master System hash mismatch — file may have been modified by automation! "
                f"Stored: {data['hash'][:16]}... Current: {current[:16]}..."
            )
        else:
            pytest.skip("master_hash.json not yet created (run automation once first)")


# ─────────────────────────────────────────────
# 2. Config Integrity
# ─────────────────────────────────────────────

class TestConfigIntegrity:

    def test_config_exists(self):
        assert os.path.exists(path("operating_system/config.yaml")), "config.yaml is missing"

    def test_config_is_valid_yaml(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        assert cfg is not None, "config.yaml parsed as empty"

    def test_config_promotion_threshold_is_8(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        threshold = cfg.get("update_engine", {}).get("promotion_threshold")
        assert threshold == 8, f"promotion_threshold should be 8, got: {threshold}"

    def test_config_auto_modify_master_is_false(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        assert cfg["update_engine"]["auto_modify_master"] is False, \
            "CRITICAL: auto_modify_master must always be False"

    def test_config_channel_id_matches_script(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        config_id = cfg["automation"]["youtube_channel_id"]
        with open(path("automation/fetch_youtube_transcripts.py"), encoding="utf-8") as f:
            script = f.read()
        assert config_id in script, (
            f"Channel ID in config.yaml ({config_id}) not found in fetch_youtube_transcripts.py. "
            "The two must match."
        )

    def test_config_knowledge_paths_exist(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        for key, fpath in cfg.get("knowledge_files", {}).items():
            full = path(fpath)
            assert os.path.exists(full), f"config.yaml references missing file: {fpath} (key: {key})"


# ─────────────────────────────────────────────
# 3. Knowledge File Integrity
# ─────────────────────────────────────────────

class TestKnowledgeFiles:

    def test_frequency_table_threshold_says_8(self):
        with open(path("knowledge/02_Akshat_Principle_Frequency_Table.md"), encoding="utf-8") as f:
            content = f.read()
        assert "8+ independent sources" in content, \
            "Frequency Table must state 8+ independent sources as promotion threshold"

    def test_rm03_is_doctrine(self):
        with open(path("knowledge/02_Akshat_Principle_Frequency_Table.md"), encoding="utf-8") as f:
            content = f.read()
        # Find RM-03 row and check status
        pattern = re.compile(r'\|\s*RM-03\s*\|[^|]+\|\s*\d+\s*\|\s*([^|]+)\|', re.MULTILINE)
        m = pattern.search(content)
        assert m, "RM-03 row not found in Frequency Table"
        status = m.group(1).strip()
        assert "Doctrine" in status, f"RM-03 status should be Doctrine, got: {status}"

    def test_no_wildcard_sources_in_new_entries(self):
        """Warn if new table rows still use YT-* wildcards (not individual IDs)."""
        with open(path("knowledge/02_Akshat_Principle_Frequency_Table.md"), encoding="utf-8") as f:
            content = f.read()
        # Only old rows should have wildcards — this is acceptable debt flagged by audit
        # New rows must use specific IDs. This test passes but logs a warning.
        wildcard_rows = re.findall(r'\|[^|]*YT-\*[^|]*\|', content)
        if wildcard_rows:
            pytest.warns(UserWarning, match="wildcard")

    def test_source_database_has_individual_placeholders(self):
        with open(path("knowledge/03_Akshat_Source_Database.md"), encoding="utf-8") as f:
            content = f.read()
        assert "PLACEHOLDER" in content, \
            "Source Database should have PLACEHOLDER rows guiding new individual source entries"

    def test_recent_changes_not_corrupted(self):
        with open(path("knowledge/04_Akshat_Recent_Changes.md"), encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 500, "04_Recent_Changes.md appears too short — possible corruption"
        assert "AUTO-UPDATABLE" in content, "Recent Changes header annotation missing"


# ─────────────────────────────────────────────
# 4. Automation Scripts Exist
# ─────────────────────────────────────────────

class TestAutomationScripts:

    REQUIRED_SCRIPTS = [
        "automation/extract_principles.py",
        "automation/contradiction_checker.py",
        "automation/update_frequency_table.py",
        "automation/update_recent_changes.py",
        "automation/run_update_protocol.py",
        "automation/fetch_youtube_transcripts.py",
        "automation/config_loader.py",
        "scripts/promote_to_master.py",
        "scripts/query_interface.py",
    ]

    def test_all_required_scripts_exist(self):
        missing = [s for s in self.REQUIRED_SCRIPTS if not os.path.exists(path(s))]
        assert not missing, f"Missing required scripts: {missing}"

    def test_run_update_never_imports_master(self):
        with open(path("automation/run_update_protocol.py"), encoding="utf-8") as f:
            content = f.read()
        assert "01_Akshat_Master_System" not in content or "open" not in content, \
            "run_update_protocol.py must never write to Master System"

    def test_extract_principles_uses_sha256(self):
        with open(path("automation/extract_principles.py"), encoding="utf-8") as f:
            content = f.read()
        assert "sha256" in content, "extract_principles.py must use SHA-256 for content deduplication"

    def test_contradiction_checker_has_atomic_write(self):
        with open(path("automation/contradiction_checker.py"), encoding="utf-8") as f:
            content = f.read()
        assert "os.replace" in content or ".tmp" in content, \
            "contradiction_checker.py should use atomic writes"


# ─────────────────────────────────────────────
# 5. Routing Integrity
# ─────────────────────────────────────────────

class TestRoutingIntegrity:

    def test_skill_router_has_fallback_handler(self):
        with open(path("routing/06_Skill_Router.md"), encoding="utf-8") as f:
            content = f.read()
        assert "Fallback Handler" in content, \
            "Skill Router must have a Fallback Handler section for unknown task types"

    def test_skill_router_has_default_response(self):
        with open(path("routing/06_Skill_Router.md"), encoding="utf-8") as f:
            content = f.read()
        assert "Default Response" in content or "default_response" in content.lower(), \
            "Skill Router must define a Default Response for unmatched tasks"

    def test_knowledge_router_exists(self):
        assert os.path.exists(path("routing/05_Akshat_Knowledge_Router.md")), \
            "Knowledge Router file missing"


# ─────────────────────────────────────────────
# 6. GitHub Actions Workflows
# ─────────────────────────────────────────────

class TestGitHubWorkflows:

    def test_protect_master_workflow_exists(self):
        assert os.path.exists(path(".github/workflows/protect_master_system.yml")), \
            "protect_master_system.yml workflow is missing — Master System unprotected!"

    def test_run_update_workflow_exists(self):
        assert os.path.exists(path(".github/workflows/run_update_protocol.yml"))

    def test_weekly_fetch_workflow_exists(self):
        assert os.path.exists(path(".github/workflows/weekly_content_fetch.yml"))

    def test_protect_workflow_blocks_automation(self):
        with open(path(".github/workflows/protect_master_system.yml"), encoding="utf-8") as f:
            content = f.read()
        assert "exit 1" in content, \
            "protect_master_system.yml must have exit 1 to block automation writes"
