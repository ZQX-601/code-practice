# Source discovery and ranking

## Collection boundaries

- Store titles, canonical IDs, public URLs, dates, tags, original short summaries, and aggregate signals.
- Do not copy full copyrighted statements, editorials, paid company-tag tables, or candidate solutions.
- Do not bypass login, paywalls, robots restrictions, or anti-automation controls.
- Never request or persist passwords, cookies, tokens, or browser profiles.
- An authenticated local browser may be inspected only after explicit user authorization in that interaction.

## Normalization

Map each report to a canonical LeetCode ID when the evidence is strong. Otherwise use an `unmapped-*` ID and preserve the approximate description. Record aliases and variant relationships separately; do not turn a vague similarity into an exact match.

Deduplicate by canonical ID plus material constraint changes. Multiple sources should increase source count rather than create duplicate problems.

## Evidence fields

Each sourced signal should include:

- `url`
- `publisher`
- `published_at` or `observed_at`
- `company`
- `role` and `level` when known
- `round` when known
- `mapping_confidence`: `high`, `medium`, or `low`
- `notes`: a short original summary

Treat interview reports as noisy observations, not promises.

## Ranking

Rank candidates using transparent components on a 0–1 scale:

- 35% verified source frequency, capped to avoid one site dominating;
- 25% recency with gradual decay;
- 20% relevance to recommendation-algorithm/SWE coding roles;
- 10% source diversity;
- 10% curriculum fit for the learner's current prerequisites.

Keep the component values in the index so the choice can be explained. A high company score cannot override missing prerequisites; choose an easier analogue first.

Generated variants have `source_type: generated` and no company-frequency credit.
