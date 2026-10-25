# Judge rubric — ears-ac

The judge sees one AC block per run, the case expectations from `cases.json`, and the example Product Context. It does not know which model wrote the block (runs are labelled with random ids).

Score every run on four measures:

| Measure | How it is scored |
|---|---|
| **Coverage** | For each `must_cover` item: 1 if a criterion (or a Related story, where the item says it may be one) states it correctly, 0.5 if partly, 0 if missing or wrong. Coverage = sum / number of items. |
| **No invention** | For each `must_not` item: 1 if the block does **not** do it. Also list any other statement presented as decided that the Product Context does not support (extra rules, values, notifications, roles). Each such statement is an invention. |
| **Open questions** | For each `expected_questions` item: 1 if the block raises it as an open question, or writes the criterion as `(proposed — confirm)` / `TBD` with a matching question. Cases with no expected questions score 1 unless the block asks about something the Product Context already decides (then 0.5). |
| **Reachability** | 1 if every criterion describes a state the user can reach in this flow, 0 if any criterion describes an unreachable state (for example check-in after no-show). |

Output per run: the four scores, the list of inventions, and one sentence on the biggest problem.

Overall run score = mean of Coverage, No invention (share of `must_not` respected, minus 0.1 per extra invention, floor 0), Open questions and Reachability.
