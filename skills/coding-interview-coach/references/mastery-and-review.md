# Mastery and review

## States

Use only these ordered topic/problem states:

`unseen -> learning -> practicing -> independent -> transferable -> retained`

- `unseen`: no evidence.
- `learning`: concept has been introduced or a full solution was shown.
- `practicing`: can progress with substantive hints.
- `independent`: independently completes a standard problem.
- `transferable`: independently completes an unseen structural variant.
- `retained`: later spaced retrieval confirms the skill.

Regression is allowed when later evidence contradicts the current state.

## Theme mastery gate

A theme is mastered only after all of the following are documented:

1. An easy foundational problem completed without a key hint.
2. A more demanding standard problem completed without a key hint.
3. An unseen variant completed without a key hint.
4. A later spaced review completed independently.
5. A correct explanation of invariant, complexity, and applicability boundaries.

Hint levels 2–5 prevent that attempt from satisfying an independent gate.

## Allowed verdicts

Use exactly one Chinese verdict in each review:

- `需要重新学习`
- `需要相似题强化`
- `标准题可独立完成`
- `可以进入陌生变体`
- `已通过短期掌握验证`
- `已通过长期记忆验证`

## Error taxonomy

Use stable identifiers in `progress.json`:

- `pattern_not_recognized`
- `concept_not_understood`
- `implementation_gap`
- `boundary_or_initialization`
- `python_usage`
- `complexity_not_acceptable`
- `variant_transfer_failure`
- `time_pressure`

## Review intervals

For a failed or materially hinted attempt, schedule retrieval at 1, 3, 7, 14, and 30 days. Successful independent or variant work may begin at a later interval, but must still include delayed retrieval. After a successful 30-day retrieval, normally schedule 60 days; shorten the interval after failure.

During review, hide old code and explanation until the new attempt is complete. Prefer an equivalent or light variant at 7 and 30 days so recognition of the filename is not mistaken for recall.

## Progress schema invariants

`coding/progress.json` must contain:

- `schema_version`: currently `1`.
- `learner`: language, timezone, daily minutes, target companies and role.
- `curriculum`: current week/topic and start date.
- `topics`: mapping to valid mastery states plus evidence arrays.
- `problems`: mapping to attempt summaries.
- `review_queue`: items with unique ID, problem/topic, due date, stage, status, and reason.
- `stats`: independent, hinted, failed, and retained attempt counters.

Never delete attempt evidence when changing mastery. Append a new attempt or review record.
