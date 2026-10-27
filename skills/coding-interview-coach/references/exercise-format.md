# Exercise and review file format

## Exercise file

Create `coding/sessions/YYYY-MM-DD/NNN-slug.py`. Use a module docstring for metadata and learner prompts, followed by editable Python sections.

Required fields in the docstring:

- session date and sequence;
- canonical problem ID/title and source URL;
- difficulty;
- timebox;
- whether this is new, reinforcement, variant, or review;
- explicit instruction not to inspect prior solutions.

Required learner sections:

```python
# 1. 题意复述与需要澄清的问题
# 2. 暴力解法
# 3. 优化思路与核心不变量
# 4. 时间/空间复杂度
# 5. 最终代码
# 6. 自测用例与 dry run
# 7. 用时、使用过的提示等级、仍不确定的地方
```

Do not include the answer, hidden pattern label, or copied full statement. A short original summary of constraints is acceptable when needed to disambiguate a variant.

## Review file

Write `NNN-slug.review.md` without modifying the exercise. Include:

- submission snapshot identifier (path and review time);
- concise result;
- evidence by review dimension;
- failing or adversarial cases;
- highest hint level;
- error taxonomy IDs;
- one allowed verdict;
- what the learner must do next;
- scheduled review dates;
- explanation only to the level already earned or requested.

When the learner resubmits, append a dated review section or create `-v2`; do not erase the prior evaluation.

## Daily plan

`plan.md` records the session objective, due review summary, selected problem and selection reason without exposing the solution pattern, expected time budget, and chronological outcomes.
