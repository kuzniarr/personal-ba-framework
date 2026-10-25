"""Deterministic format checks for ears-ac outputs.

Usage: python3 check.py runs/<model>/   -> prints a table and writes checks.json there
Each run file is <case-id>.md with one AC block produced by the skill.
"""
import json, re, sys
from pathlib import Path

SECTION = re.compile(r"^\*\*(.+?)\*\*\s*$")
NUM = re.compile(r"^\s*(\d+)\.\s+(.*)")


def sections(text):
    """Split the block into {header: [lines]} by bold header lines."""
    out, cur = {}, "_preamble"
    for line in text.splitlines():
        m = SECTION.match(line.strip())
        if m:
            cur = m.group(1).strip()
            out.setdefault(cur, [])
        else:
            out.setdefault(cur, []).append(line)
    return out


def check(text):
    sec = sections(text)
    names = list(sec)
    res = {}
    # criteria = numbered lines between "Acceptance Criteria" and the first closing block
    closing = {"Data Dictionary", "Related stories", "Out of Scope", "Open Questions"}
    crit, in_ac = [], False
    for name in names:
        if name == "Acceptance Criteria":
            in_ac = True
        elif name in closing:
            in_ac = False
        if in_ac:
            crit += [NUM.match(l) for l in sec[name] if NUM.match(l)]
    nums = [int(m.group(1)) for m in crit]
    oq = [l for l in sec.get("Open Questions", []) if NUM.match(l)]
    crit_text = "\n".join(m.group(2) for m in crit)

    res["has_story_line"] = text.lstrip().startswith("**Story:**")
    res["has_ac_header"] = "Acceptance Criteria" in sec
    res["uses_must_not_shall"] = "shall" not in text.lower() and " must " in text
    res["numbering_continuous"] = bool(nums) and nums == list(range(1, len(nums) + 1))
    tbd = len(re.findall(r"`TBD`", text))
    bare_tbd = len(re.findall(r"(?<!`)\bTBD\b(?!`)", text))
    proposed = len(re.findall(r"proposed\s*[—-]\s*confirm", crit_text, re.I))
    res["tbd_as_code_chip"] = bare_tbd == 0
    res["tbd_and_proposed_have_questions"] = (tbd + proposed == 0) or len(oq) > 0
    res["no_inline_story_refs"] = not re.search(r"\bsee (the )?['\"“]?[A-Z]", crit_text)
    res["no_source_citations"] = not re.search(r"§\s?\d|\bS\d\b|\bR\d{1,3}\b|WBS R", crit_text)
    res["no_vague_verbs"] = not re.search(r"\b(handle[sd]?|manage[sd]?|restrict(s|ed)?)\b", crit_text, re.I)
    res["criteria_count"] = len(nums)
    res["open_questions_count"] = len(oq)
    bools = [v for v in res.values() if isinstance(v, bool)]
    res["pass_rate"] = round(sum(bools) / len(bools), 2)
    return res


if __name__ == "__main__":
    d = Path(sys.argv[1])
    allres = {}
    for f in sorted(d.glob("*.md")):
        allres[f.stem] = check(f.read_text())
    (d / "checks.json").write_text(json.dumps(allres, indent=2))
    keys = [k for k in next(iter(allres.values())) if k not in ("pass_rate",)]
    for case, r in allres.items():
        fails = [k for k in keys if r[k] is False]
        print(f"{case:24} pass {r['pass_rate']:.2f}  AC {r['criteria_count']:2}  OQ {r['open_questions_count']:2}  fails: {', '.join(fails) or '-'}")
