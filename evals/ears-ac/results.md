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

# Run 2 — skill change, 2026-10-25

**Change:** one rule added to `ears-ac` (plus a final-gate line): every point the Product Context flags as open, not defined or `proposed — confirm` that touches the story must appear in Open Questions, never only in Out of Scope or Related stories. Re-run: Sonnet on all 8 cases, Opus on the 2 cases it failed. Same cases, same blind judge.

| Case | Sonnet run 1 → 2 | Opus run 1 → 2 |
|---|---|---|
| 05 weekly series — open questions | 0.5 → **1.0** | 1.0 → 1.0 |
| 07 deactivate user — open questions | 0.5 → **1.0** | 0.5 → **1.0** |
| Sonnet, all 8 cases — overall | 0.97 → 0.91 | — |

## What it showed

- **The fix works on its target.** Both models now raise the open points the Product Context flags (series vs no-show, Workspace sync).
- **The eval caught new problems elsewhere.** On cases that scored 1.0 before, Sonnet asked a question the Product Context already answers (case 01) and added rejection criteria for states the user cannot reach (cases 02, 04). These are not what the rule asks for, so they may be run-to-run variance rather than the rule; one run per case cannot tell.
- **Next:** three runs per case to measure variance before the rule goes into the published skill.
