"""Copy runs into a blind folder with random ids, so the judge cannot tell which model wrote what.

Usage: python3 blind.py            -> writes blind/<id>.md and _key.json (keep the key away from the judge)
       python3 blind.py --unblind  -> joins blind/scores.json with the key into results.json
"""
import json, random, shutil, sys
from pathlib import Path

HERE = Path(__file__).parent
RUNS, BLIND, KEY = HERE / "runs", HERE / "blind", HERE / "_key.json"

if "--unblind" in sys.argv:
    key = json.loads(KEY.read_text())
    scores = json.loads((BLIND / "scores.json").read_text())
    out = {}
    for bid, s in scores.items():
        model, case = key[bid]
        out.setdefault(model, {})[case] = s
    (HERE / "results.json").write_text(json.dumps(out, indent=2))
    print("results.json written")
else:
    BLIND.mkdir(exist_ok=True)
    files = sorted(RUNS.glob("*/*.md"))
    ids = random.sample(range(100, 1000), len(files))
    key = {}
    for f, i in zip(files, ids):
        bid = f"run-{i}"
        case = f.stem
        shutil.copy(f, BLIND / f"{bid}__{case}.md")
        key[f"{bid}__{case}"] = [f.parent.name, case]
    KEY.write_text(json.dumps(key, indent=2))
    print(f"{len(files)} runs blinded")
