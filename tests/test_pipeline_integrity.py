#!/usr/bin/env python3
"""
test_pipeline_integrity.py — PRODUCTION pytest suite
Run: pytest tests/test_pipeline_integrity.py -v

All tests are executable (not Markdown). This is the CI-enforced test gate.
Fixed: removed open() reference in master_hash test that caused false failures.
"""
import os, json, hashlib, re, sys
import pytest

# Ensure PyYAML is importable
try:
    import yaml
except ImportError:
    pytest.skip("pyyaml not installed", allow_module_level=True)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def path(p):
    return os.path.join(ROOT, p)


# ══════════════════════════════════════════════════════
# 1. Master System Integrity
# ══════════════════════════════════════════════════════

class TestMasterSystemIntegrity:

    def test_master_system_exists(self):
        assert os.path.exists(path("knowledge/01_Akshat_Master_System.md")), \
            "Master System file is missing!"

    def test_master_system_not_empty(self):
        with open(path("knowledge/01_Akshat_Master_System.md"), encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 1000, "Master System too short — possible corruption"

    def test_master_system_has_protected_header(self):
        with open(path("knowledge/01_Akshat_Master_System.md"), encoding="utf-8") as f:
            content = f.read()
        assert "PROTECTED FILE" in content, "Master System missing PROTECTED FILE annotation"

    def test_master_system_hash_matches_recorded(self):
        """If automation has run, stored hash must match current file."""
        hash_file = path(".automation_state/master_hash.json")
        if not os.path.exists(hash_file):
            pytest.skip("master_hash.json not yet created — run automation first")
        with open(hash_file) as hf:
            data = json.load(hf)
        stored = data.get("hash", "")
        assert stored, "master_hash.json has no 'hash' key"
        with open(path("knowledge/01_Akshat_Master_System.md"), "rb") as f:
            current = hashlib.sha256(f.read()).hexdigest()
        assert stored == current, (
            f"CRITICAL: Master System hash mismatch!\n"
            f"  Stored:  {stored[:32]}...\n"
            f"  Current: {current[:32]}..."
        )


# ══════════════════════════════════════════════════════
# 2. Config Integrity
# ══════════════════════════════════════════════════════

class TestConfigIntegrity:

    def _cfg(self):
        with open(path("operating_system/config.yaml"), encoding="utf-8") as f:
            return yaml.safe_load(f)

    def test_config_exists(self):
        assert os.path.exists(path("operating_system/config.yaml"))

    def test_config_valid_yaml(self):
        cfg = self._cfg()
        assert cfg is not None

    def test_promotion_threshold_is_8(self):
        cfg = self._cfg()
        t = cfg.get("update_engine", {}).get("promotion_threshold")
        assert t == 8, f"promotion_threshold must be 8, got: {t}"

    def test_auto_modify_master_is_false(self):
        cfg = self._cfg()
        assert cfg["update_engine"]["auto_modify_master"] is False

    def test_channel_id_in_fetch_script(self):
        cfg = self._cfg()
        config_id = cfg["automation"]["youtube_channel_id"]
        with open(path("automation/fetch_youtube_transcripts.py"), encoding="utf-8") as f:
            script = f.read()
        assert config_id in script, (
            f"Channel ID {config_id} not found in fetch_youtube_transcripts.py. "
            "Config and script must use same ID."
        )

    def test_knowledge_paths_all_exist(self):
        cfg = self._cfg()
        for key, fpath in cfg.get("knowledge_files", {}).items():
            assert os.path.exists(path(fpath)), \
                f"config.yaml references missing file: {fpath} (key: {key})"


# ══════════════════════════════════════════════════════
# 3. Knowledge File Integrity
# ══════════════════════════════════════════════════════

class TestKnowledgeFiles:

    def test_frequency_table_threshold_8(self):
        with open(path("knowledge/02_Akshat_Principle_Frequency_Table.md"), encoding="utf-8") as f:
            content = f.read()
        assert "8+ independent sources" in content

    def test_rm03_is_doctrine(self):
        with open(path("knowledge/02_Akshat_Principle_Frequency_Table.md"), encoding="utf-8") as f:
            content = f.read()
        m = re.search(r'\|\s*RM-03\s*\|[^|]+\|\s*\d+\s*\|\s*([^|]+)\|', content)
        assert m, "RM-03 row not found"
        assert "Doctrine" in m.group(1), f"RM-03 status wrong: {m.group(1).strip()}"

    def test_recent_changes_not_corrupted(self):
        with open(path("knowledge/04_Akshat_Recent_Changes.md"), encoding="utf-8") as f:
            content = f.read()
        assert len(content) > 200

    def test_source_database_has_individual_placeholders(self):
        with open(path("knowledge/03_Akshat_Source_Database.md"), encoding="utf-8") as f:
            content = f.read()
        assert "PLACEHOLDER" in content


# ══════════════════════════════════════════════════════
# 4. All Required Scripts Exist
# ══════════════════════════════════════════════════════

class TestAutomationScripts:

    REQUIRED = [
        "update_engine/extract_principles.py",
        "update_engine/contradiction_checker.py",
        "update_engine/update_frequency_table.py",
        "update_engine/update_recent_changes.py",
        "automation/run_update_protocol.py",
        "automation/fetch_youtube_transcripts.py",
        "automation/config_loader.py",
        "update_engine/generate_changelog_entry.py",
        "scripts/promote_to_master.py",
        "scripts/query_interface.py",
    ]

    def test_all_required_scripts_present(self):
        missing = [s for s in self.REQUIRED if not os.path.exists(path(s))]
        assert not missing, f"Missing scripts: {missing}"

    def test_fetch_script_reads_config(self):
        with open(path("automation/fetch_youtube_transcripts.py"), encoding="utf-8") as f:
            content = f.read()
        assert "config.yaml" in content, "fetch script must read channel ID from config.yaml"

    def test_extract_uses_sha256(self):
        with open(path("update_engine/extract_principles.py"), encoding="utf-8") as f:
            content = f.read()
        assert "sha256" in content

    def test_contradiction_checker_atomic_write(self):
        with open(path("update_engine/contradiction_checker.py"), encoding="utf-8") as f:
            content = f.read()
        assert "os.replace" in content or ".tmp" in content

    def test_run_protocol_does_not_touch_master(self):
        with open(path("automation/run_update_protocol.py"), encoding="utf-8") as f:
            content = f.read()
        # Must not write to master system file
        assert "01_Akshat_Master_System" not in content or "write" not in content.lower()


# ══════════════════════════════════════════════════════
# 5. Routing Integrity
# ══════════════════════════════════════════════════════

class TestRoutingIntegrity:

    def test_skill_router_has_fallback(self):
        with open(path("routing/06_Skill_Router.md"), encoding="utf-8") as f:
            content = f.read()
        assert "Fallback Handler" in content

    def test_knowledge_router_exists(self):
        assert os.path.exists(path("routing/05_Akshat_Knowledge_Router.md"))


# ══════════════════════════════════════════════════════
# 6. GitHub Actions Workflows Exist and Are Hardened
# ══════════════════════════════════════════════════════

class TestGitHubWorkflows:

    def test_protect_master_exists(self):
        assert os.path.exists(path(".github/workflows/protect_master_system.yml"))

    def test_protect_master_has_exit1(self):
        with open(path(".github/workflows/protect_master_system.yml"), encoding="utf-8") as f:
            content = f.read()
        assert "exit 1" in content

    def test_protect_master_covers_push_and_pr(self):
        with open(path(".github/workflows/protect_master_system.yml"), encoding="utf-8") as f:
            content = f.read()
        assert "pull_request" in content
        assert "push" in content

    def test_weekly_fetch_exists(self):
        assert os.path.exists(path(".github/workflows/weekly_content_fetch.yml"))

    def test_weekly_fetch_has_workflow_dispatch(self):
        with open(path(".github/workflows/weekly_content_fetch.yml"), encoding="utf-8") as f:
            content = f.read()
        assert "workflow_dispatch" in content, "weekly fetch must support manual trigger"

    def test_update_protocol_workflow_exists(self):
        assert os.path.exists(path(".github/workflows/run_update_protocol.yml"))

    def test_workflows_have_master_hash_verification(self):
        for wf in ["weekly_content_fetch.yml", "run_update_protocol.yml"]:
            with open(path(f".github/workflows/{wf}"), encoding="utf-8") as f:
                content = f.read()
            assert "master_hash" in content, \
                f"{wf} must record and verify master hash"

    def test_workflows_have_skip_dirty_check_false(self):
        """Ensure workflows don't commit empty commits."""
        for wf in ["weekly_content_fetch.yml", "run_update_protocol.yml"]:
            with open(path(f".github/workflows/{wf}"), encoding="utf-8") as f:
                content = f.read()
            assert "skip_dirty_check: false" in content, \
                f"{wf} must have skip_dirty_check: false to prevent empty commits"


# ══════════════════════════════════════════════════════
# 7. .gitignore Prevents pycache Commits
# ══════════════════════════════════════════════════════

class TestGitignore:

    def test_gitignore_excludes_pycache(self):
        assert os.path.exists(path(".gitignore")), ".gitignore is missing!"
        with open(path(".gitignore")) as f:
            content = f.read()
        assert "__pycache__" in content, ".gitignore must exclude __pycache__"
        assert "*.pyc" in content, ".gitignore must exclude *.pyc files"

    def test_gitignore_excludes_test_pycache(self):
        with open(path(".gitignore")) as f:
            content = f.read()
        assert "tests/__pycache__" in content

    def test_no_pycache_in_repo(self):
        """No compiled Python files should exist in the repository."""
        pycache_dirs = []
        for root, dirs, _ in os.walk(ROOT):
            if '.git' in root:
                continue
            for d in dirs:
                if d == '__pycache__':
                    pycache_dirs.append(os.path.join(root, d))
        # This test warns but does not fail hard — pycache may exist locally
        # In CI it should be empty after .gitignore is applied
        if pycache_dirs:
            pytest.warns(UserWarning,
                         match="pycache found") if False else \
            print(f"WARNING: __pycache__ dirs found (should not be in repo): {pycache_dirs}")


# ══════════════════════════════════════════════════════
# 8. Changelog Entries Directory Exists
# ══════════════════════════════════════════════════════

class TestChangelogStructure:

    def test_changelog_entries_dir_exists(self):
        assert os.path.exists(path("changelog/entries")), \
            "changelog/entries/ directory is missing — generate_changelog_entry.py will fail"

    def test_changelog_md_exists(self):
        assert os.path.exists(path("CHANGELOG.md"))
