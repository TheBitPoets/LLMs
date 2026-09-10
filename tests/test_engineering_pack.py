"""Verify the actual student export can run without repository-only files."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class StudentExportChecks(unittest.TestCase):
    def test_capstone_export_runs_mcp_and_training_without_teacher_assets(self):
        activity_dir = ROOT / "activities/llm/llm-activity-m19-pollicino"
        activity = json.loads((activity_dir / "activity.json").read_text())
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            for asset in activity["assets"]:
                if asset["visibility"] != "student":
                    continue
                destination = target / asset["target_path"]
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(activity_dir / asset["path"], destination)
            self.assertFalse(list(target.rglob("SOLUTION.md")))
            env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
            for module, args in [("run", ["mcp-check"]),
                                 ("train", ["--steps", "2", "--adapter-steps", "2"])]:
                result = subprocess.run([sys.executable, "-m", "labs.engineering."+module, *args],
                                        cwd=target, env=env, capture_output=True, text=True, timeout=30)
                self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads((target / "output/engineering/training-report.json").read_text())
            self.assertTrue(report["frozen_base_unchanged"])

    def test_teacher_material_is_not_an_indexed_source(self):
        pack = json.loads((ROOT / "content/llm/content-pack.json").read_text())
        engineering = next(s for s in pack["sources"] if s["id"] == "llm-source-engineering")
        self.assertNotIn("TEACHER.md", engineering["files"])
        self.assertEqual(len([f for f in engineering["files"] if f.startswith("E0")]), 8)
