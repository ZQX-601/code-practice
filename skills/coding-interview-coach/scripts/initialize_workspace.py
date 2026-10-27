#!/usr/bin/env python3
"""Initialize an additive coding-coach workspace without overwriting user data."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


PROFILE = """# 学习者档案

- 目标公司：Meta、字节跳动
- 目标岗位：推荐算法工程师（社招 3–5 年）
- 答题语言：Python
- 教学语言：中文
- 每日预算：90 分钟
- 训练周期：12 周
- 当前水平：基础阶段，从简单题开始
- 启动方式：由学习者主动说“开始今天的训练”
"""

CURRICULUM = """# 12 周训练进度

当前阶段：第 1 周 / 数组、哈希、字符串与复杂度

| 周次 | 主题 | 状态 |
|---|---|---|
| 1–2 | 数组、哈希、字符串、复杂度 | 进行中 |
| 3–4 | 双指针、滑动窗口、前缀和、二分 | 未开始 |
| 5–6 | 栈、队列、链表、区间、贪心 | 未开始 |
| 7–8 | 树、递归、DFS、BFS、堆 | 未开始 |
| 9–10 | 回溯、图、并查集、动态规划 | 未开始 |
| 11 | 推荐算法手写 | 未开始 |
| 12 | 公司高频混合训练与模拟 | 未开始 |

日历周不强制推进；只有掌握证据充分时才进入下一主题。
"""

MISTAKES = """# 错误模式记录

按概念错误聚合，不按题目数量堆积。每条记录应包含日期、题目、证据、错误类型、修正方法和复测结果。
"""

REVIEWS = """# 间隔复习队列

机器可读队列位于 `progress.json`。这里记录面向学习者的复习原因、结果和下一次安排。
"""

SEED_PROBLEMS = [
    ("leetcode-1", "Two Sum", "https://leetcode.com/problems/two-sum/", "easy", ["array", "hash-map"]),
    ("leetcode-217", "Contains Duplicate", "https://leetcode.com/problems/contains-duplicate/", "easy", ["array", "hash-set"]),
    ("leetcode-242", "Valid Anagram", "https://leetcode.com/problems/valid-anagram/", "easy", ["string", "counting"]),
    ("leetcode-125", "Valid Palindrome", "https://leetcode.com/problems/valid-palindrome/", "easy", ["string", "two-pointers"]),
    ("leetcode-283", "Move Zeroes", "https://leetcode.com/problems/move-zeroes/", "easy", ["array", "two-pointers"]),
    ("leetcode-704", "Binary Search", "https://leetcode.com/problems/binary-search/", "easy", ["binary-search"]),
    ("leetcode-20", "Valid Parentheses", "https://leetcode.com/problems/valid-parentheses/", "easy", ["stack", "string"]),
    ("leetcode-206", "Reverse Linked List", "https://leetcode.com/problems/reverse-linked-list/", "easy", ["linked-list"]),
    ("leetcode-104", "Maximum Depth of Binary Tree", "https://leetcode.com/problems/maximum-depth-of-binary-tree/", "easy", ["tree", "dfs", "bfs"]),
    ("leetcode-3", "Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/", "medium", ["sliding-window", "hash-map"]),
]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--start-date", default=date.today().isoformat())
    args = parser.parse_args()

    coding = args.root.resolve() / "coding"
    coding.mkdir(parents=True, exist_ok=True)
    (coding / "sessions").mkdir(exist_ok=True)

    created = []
    for name, content in {
        "profile.md": PROFILE,
        "curriculum.md": CURRICULUM,
        "mistakes.md": MISTAKES,
        "reviews.md": REVIEWS,
    }.items():
        if write_if_missing(coding / name, content):
            created.append(name)

    progress = {
        "schema_version": 1,
        "learner": {
            "language": "Python",
            "timezone": "Asia/Shanghai",
            "daily_minutes": 90,
            "target_companies": ["Meta", "ByteDance"],
            "target_role": "Recommendation Algorithm Engineer, 3-5 YOE",
        },
        "curriculum": {"start_date": args.start_date, "current_week": 1, "current_topic": "array-hash-string"},
        "topics": {},
        "problems": {},
        "review_queue": [],
        "stats": {"independent": 0, "hinted": 0, "failed": 0, "retained": 0},
    }
    if write_if_missing(coding / "progress.json", json.dumps(progress, ensure_ascii=False, indent=2) + "\n"):
        created.append("progress.json")

    bank = {
        "schema_version": 1,
        "updated_at": args.start_date,
        "problems": [
            {
                "id": problem_id,
                "title": title,
                "url": url,
                "difficulty": difficulty,
                "topics": topics,
                "source_type": "curated-baseline",
                "company_signals": [],
                "ranking": {"frequency": 0.0, "recency": 0.0, "role_relevance": 0.5, "source_diversity": 0.0},
            }
            for problem_id, title, url, difficulty, topics in SEED_PROBLEMS
        ],
    }
    if write_if_missing(coding / "question-bank.json", json.dumps(bank, ensure_ascii=False, indent=2) + "\n"):
        created.append("question-bank.json")

    print(json.dumps({"coding_dir": str(coding), "created": created, "preserved_existing": len(created) < 6}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
