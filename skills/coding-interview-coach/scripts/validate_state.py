#!/usr/bin/env python3
"""Validate coding-coach JSON state without modifying it."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

STATES = {"unseen", "learning", "practicing", "independent", "transferable", "retained"}
REVIEW_STATUSES = {"pending", "completed", "cancelled"}


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path}: {exc}")
    return None


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    coding = root / "coding"
    for name in ("profile.md", "curriculum.md", "mistakes.md", "reviews.md"):
        if not (coding / name).is_file():
            errors.append(f"missing file: {coding / name}")

    progress = load_json(coding / "progress.json", errors)
    bank = load_json(coding / "question-bank.json", errors)
    if progress is not None:
        if progress.get("schema_version") != 1:
            errors.append("progress.json schema_version must be 1")
        for key in ("learner", "curriculum", "topics", "problems", "review_queue", "stats"):
            if key not in progress:
                errors.append(f"progress.json missing key: {key}")
        if not isinstance(progress.get("review_queue", []), list):
            errors.append("progress.json review_queue must be a list")
        seen_review_ids: set[str] = set()
        for index, item in enumerate(progress.get("review_queue", [])):
            prefix = f"review_queue[{index}]"
            for key in ("id", "problem_id", "topic", "due_date", "stage", "status", "reason"):
                if key not in item:
                    errors.append(f"{prefix} missing key: {key}")
            review_id = item.get("id")
            if review_id in seen_review_ids:
                errors.append(f"duplicate review id: {review_id}")
            seen_review_ids.add(review_id)
            try:
                date.fromisoformat(item.get("due_date", ""))
            except ValueError:
                errors.append(f"{prefix} has invalid due_date")
            if item.get("status") not in REVIEW_STATUSES:
                errors.append(f"{prefix} has invalid status")
        for topic, item in progress.get("topics", {}).items():
            if not isinstance(item, dict) or item.get("state") not in STATES:
                errors.append(f"topic {topic!r} has invalid state")

    if bank is not None:
        if bank.get("schema_version") != 1:
            errors.append("question-bank.json schema_version must be 1")
        problems = bank.get("problems")
        if not isinstance(problems, list):
            errors.append("question-bank.json problems must be a list")
        else:
            seen_problem_ids: set[str] = set()
            for index, item in enumerate(problems):
                for key in ("id", "title", "url", "difficulty", "topics", "source_type"):
                    if key not in item:
                        errors.append(f"question-bank problems[{index}] missing key: {key}")
                problem_id = item.get("id")
                if problem_id in seen_problem_ids:
                    errors.append(f"duplicate problem id: {problem_id}")
                seen_problem_ids.add(problem_id)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    errors = validate(args.root.resolve())
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"valid": True, "root": str(args.root.resolve())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
