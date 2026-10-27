# 12-week curriculum

The curriculum is a dependency-aware spine, not a deadline that forces advancement. Start with easy examples because the learner reports a low starting level. Interleave verified easy company-relevant problems as soon as prerequisites are ready.

## Weeks 1–2: foundations

- Big-O, arrays, strings, hash sets, hash maps, counting, sorting tradeoffs.
- Recognition cues: membership, frequency, complement, grouping, deduplication.
- Exit evidence: independently solve easy array/hash problems and explain why hashing changes the complexity.

## Weeks 3–4: linear scans and search

- Two pointers, fast/slow pointers, sliding window, prefix sums, binary search.
- Recognition cues: ordered input, paired movement, contiguous ranges, monotonic answer space.
- Emphasize pointer/window invariants and off-by-one boundaries.

## Weeks 5–6: linear structures and greedy choices

- Stack, queue, linked list, intervals, monotonic stack introduction, greedy reasoning.
- Require justification for local choices; do not accept “this is a greedy problem” as proof.

## Weeks 7–8: trees and priority

- Recursion, binary trees, BSTs, DFS, BFS, heaps, Top-K.
- Require a clear recursive contract, base case, traversal order, and space analysis including the call stack.

## Weeks 9–10: combinatorial and state problems

- Backtracking, graphs, topological ordering, union-find, one- and two-dimensional dynamic programming.
- Teach state definition and transition derivation before code. Use easy DP first.

## Week 11: recommendation-algorithm coding

- Numerically stable sigmoid/softmax and cross entropy.
- AUC computation, Top-K, sampling, simple recall/ranking utilities.
- LR forward/loss/gradient basics, negative sampling, metric edge cases.
- Prefer pure Python first; use NumPy only when the exercise explicitly permits it.

## Week 12: company-focused consolidation

- Mixed Meta/ByteDance sets, timed sessions, variants, and retention checks.
- Meta-style practice may use two concise problems in a 45-minute block only after single-problem fundamentals are stable.
- ByteDance-style practice may deepen one problem through optimization and constraint changes.

## Adaptation rules

- Extend a topic while prerequisite gaps or repeated error patterns remain.
- Compress a topic only when independent and transfer evidence exists.
- If two consecutive problems fail for the same conceptual reason, step down one difficulty level and teach a minimal example.
- If implementation, not recognition, is the blocker, use short code drills instead of more full problems.
- Never advance solely because a calendar week ended.
