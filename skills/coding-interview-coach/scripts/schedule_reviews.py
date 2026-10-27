#!/usr/bin/env python3
"""Query and update the deterministic spaced-review queue."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from datetime import date, timedelta
from pathlib import Path

INTERVALS = {
    "incorrect": [1, 3, 7, 14, 30],
    "hinted": [1, 3, 7, 14, 30],
    "independent": [3, 7, 14, 30],
    "variant": [7, 14, 30],
    "retained": [30, 60],
}


def load_progress(root: Path) -> tuple[Path, dict]:
    path = root / "coding" / "progress.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def atomic_write(path: Path, data: dict) -> None:
    fd, temporary = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def due(args: argparse.Namespace) -> int:
    _, progress = load_progress(args.root.resolve())
    on = date.fromisoformat(args.on)
    items = [
        item
        for item in progress.get("review_queue", [])
        if item.get("status") == "pending" and date.fromisoformat(item["due_date"]) <= on
    ]
    items.sort(key=lambda item: (item["due_date"], item["stage"], item["id"]))
    print(json.dumps({"on": args.on, "due": items}, ensure_ascii=False, indent=2))
    return 0


def record(args: argparse.Namespace) -> int:
    path, progress = load_progress(args.root.resolve())
    base = date.fromisoformat(args.on)
    intervals = INTERVALS[args.outcome]
    queue = progress.setdefault("review_queue", [])
    existing_ids = {item.get("id") for item in queue}
    created = []
    for stage, days in enumerate(intervals, start=1):
        review_id = f"{args.problem_id}:{args.on}:{args.outcome}:{stage}"
        if review_id in existing_ids:
            continue
        item = {
            "id": review_id,
            "problem_id": args.problem_id,
            "topic": args.topic,
            "due_date": (base + timedelta(days=days)).isoformat(),
            "stage": stage,
            "status": "pending",
            "reason": args.outcome,
        }
        queue.append(item)
        created.append(item)
    atomic_write(path, progress)
    print(json.dumps({"created": created, "progress": str(path)}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    subparsers = parser.add_subparsers(dest="command", required=True)

    due_parser = subparsers.add_parser("due")
    due_parser.add_argument("--on", default=date.today().isoformat())
    due_parser.set_defaults(func=due)

    record_parser = subparsers.add_parser("record")
    record_parser.add_argument("--problem-id", required=True)
    record_parser.add_argument("--topic", required=True)
    record_parser.add_argument("--outcome", choices=sorted(INTERVALS), required=True)
    record_parser.add_argument("--on", default=date.today().isoformat())
    record_parser.set_defaults(func=record)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
