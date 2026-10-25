# Results — first run, 2026-10-25

`ears-ac` as published in this repository · 8 cases · one run per case per model · blind judge (Opus).

| Measure | Sonnet | Opus |
|---|---|---|
| **Overall** | **0.97** | **0.97** |
| Coverage of must-cover rules | 0.99 | 0.96 |
| Traps respected (must_not) | 1.00 | 1.00 |
| Inventions (stated as decided without a source) | 0 | 2 |
| Expected open questions raised | 0.88 | 0.94 |
| Reachability | 1.00 | 1.00 |
| Format checks passed | 100% | 100% |
| Average criteria / open questions per story | 7.8 / 4.4 | 11.4 / 6.2 |

## What it showed

- **Both models follow the skill well.** No trap was hit and every format check passed on all 16 runs.
- **Sonnet matches Opus on this skill.** Same overall score, fuller coverage, no inventions, about a third shorter. Opus raises more open questions but twice stated a detail as decided (daylight-saving handling, ending sessions on deactivation).
- **The common weakness is the skill, not the model.** Both models parked an open point that the Product Context explicitly flags (Workspace sync on deactivation, no-show inside a series) in Out of Scope or Related stories instead of raising it as an open question. Candidate fix for the skill: every point the Product Context marks as open must appear in Open Questions.
- **The eval needed calibration too.** The first judge pass penalised AC that did not restate "only an Admin can…", although the skill forbids standalone role criteria. Three expectations were corrected and those runs re-scored.

## Limits

8 cases, one run each (no variance measured), one judge model from the same family as one of the candidates, a fictional Product Context. Enough to catch regressions and compare models on this skill; not a benchmark.
