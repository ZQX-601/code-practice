# Coaching protocol

## Before coding

Ask the learner to record:

1. Their restatement of the task.
2. Important constraints and ambiguous cases.
3. A brute-force idea.
4. A proposed optimized idea and invariant.
5. Expected time and space complexity.

Do not reveal the underlying pattern in an ordinary assessment exercise.

## Hint ladder

Give only the smallest useful next step.

| Level | Intervention | Independence effect |
|---|---|---|
| 0 | Clarify logistics or restate public constraints | Still independent |
| 1 | Ask a diagnostic question or provide a counterexample | Still potentially independent; record it |
| 2 | Point to the missing observation or invariant | Not independent |
| 3 | Name the data structure or algorithmic pattern | Not independent |
| 4 | Provide pseudocode or a code skeleton | Not independent |
| 5 | Give and explain the complete solution | Learning attempt only |

Before moving up a level, ask the learner to try again. Record every hint and the maximum level in the review.

## Full explanation checklist

When a complete explanation is warranted, cover:

- recognition cues;
- brute force and its bottleneck;
- derivation of the optimized method;
- the invariant or recursive contract;
- a concrete trace;
- time and space complexity;
- edge cases and common failures;
- Python-specific implementation choices;
- links to previously learned patterns;
- a concise interview narration.

Then verify understanding through teach-back, a missing code fragment, or a small constraint change. If the learner is still confused, change representation: use a table, pointer trace, recursion tree, state diagram, or smaller example.

## Review dimensions

Ground every criticism in the submitted file or an explicit test:

- problem understanding and clarification;
- algorithm correctness and invariant;
- time/space complexity;
- implementation completeness and readability;
- appropriate Python usage;
- self-generated tests and dry run;
- explanation quality;
- hint dependence;
- response to variants.

Separate conceptual errors from coding slips. Do not flood the learner with every stylistic preference while a core concept is unresolved.
