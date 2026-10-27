from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SKILL_ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


initializer = load_module("initializer", "initialize_workspace.py")
validator = load_module("validator", "validate_state.py")
scheduler = load_module("scheduler", "schedule_reviews.py")


class SkillScriptTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        coding = self.root / "coding"
        coding.mkdir()
        (coding / "sessions").mkdir()
        for name, content in {
            "profile.md": initializer.PROFILE,
            "curriculum.md": initializer.CURRICULUM,
            "mistakes.md": initializer.MISTAKES,
            "reviews.md": initializer.REVIEWS,
        }.items():
            (coding / name).write_text(content, encoding="utf-8")
        progress = {
            "schema_version": 1,
            "learner": {},
            "curriculum": {},
            "topics": {},
            "problems": {},
            "review_queue": [],
            "stats": {},
        }
        (coding / "progress.json").write_text(json.dumps(progress), encoding="utf-8")
        bank = {
            "schema_version": 1,
            "updated_at": "2026-10-27",
            "problems": [
                {
                    "id": "leetcode-1",
                    "title": "Two Sum",
                    "url": "https://leetcode.com/problems/two-sum/",
                    "difficulty": "easy",
                    "topics": ["array"],
                    "source_type": "curated-baseline",
                }
            ],
        }
        (coding / "question-bank.json").write_text(json.dumps(bank), encoding="utf-8")

    def tearDown(self):
        self.temporary.cleanup()

    def test_valid_seed_state(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_validator_reports_corruption(self):
        path = self.root / "coding" / "progress.json"
        progress = json.loads(path.read_text(encoding="utf-8"))
        del progress["learner"]
        path.write_text(json.dumps(progress), encoding="utf-8")
        self.assertIn("progress.json missing key: learner", validator.validate(self.root))

    def test_record_is_idempotent_and_due_is_deterministic(self):
        class Args:
            root = self.root
            problem_id = "leetcode-1"
            topic = "array-hash-string"
            outcome = "incorrect"
            on = "2026-10-27"

        scheduler.record(Args)
        scheduler.record(Args)
        progress = json.loads((self.root / "coding" / "progress.json").read_text(encoding="utf-8"))
        self.assertEqual(len(progress["review_queue"]), 5)
        self.assertEqual(progress["review_queue"][0]["due_date"], "2026-10-28")
        self.assertEqual(validator.validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
