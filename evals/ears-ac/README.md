# Eval: ears-ac

A small, repeatable test for the `ears-ac` skill. It answers two questions: does the skill still work after I change it, and which model should run it.

## What is in the set

8 stories on the example Product Context (`examples/project-knowledge/product_context.md`): move, cancel own, Office Manager cancel, check-in, weekly series, manual no-show, deactivate a user, remove the Office Manager role.

Each case in `cases.json` lists:

- **must_cover** — rules from the Product Context the AC must state;
- **must_not** — traps: superseded decisions, Future Phase features, unreachable states;
- **expected_questions** — places where the Product Context is silent or flags an open point, so a good output raises an open question instead of inventing an answer (for example, a 12-week series against a 30-day booking horizon).

## How a run is scored

1. **Format checks** (`check.py`, no model): must not shall, continuous numbering, `TBD` as a code chip, every `TBD` / `proposed — confirm` has an open question, no inline story references, no source citations, no vague verbs.
2. **Blind judge** (`rubric.md`): a model judge scores coverage, respected traps, inventions, open questions and reachability. Runs are renamed with random ids (`blind.py`), so the judge does not know which model wrote what.

## How to run it

1. Run the skill on every story in `cases.json`, one fresh session per story, with only the skill and the Product Context as input. Save each block to `runs/<model>/<case-id>.md`.
2. `python3 check.py runs/<model>`
3. `python3 blind.py`, then give the judge `rubric.md`, `cases.json`, the Product Context and `blind/` (never `_key.json`); it writes `blind/scores.json`.
4. `python3 blind.py --unblind` → `results.json`. Summarise in `results.md`.

Re-run after every change to the skill. A drop in any measure is a regression.

Results: [results.md](results.md) (run 1: model comparison; run 2: a skill change and what it caught).
