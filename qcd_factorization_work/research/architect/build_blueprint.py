"""Assemble BLUEPRINT.md from parts/ and generate the label registry.

Run:  python3 -I build_blueprint.py   (from any directory; paths are relative to this file)
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "parts")
ORDER = [
    "00_header.md", "00b_depgraph.md",
    "01_ch01.md", "02_ch02.md", "03_ch03.md", "04_ch04.md", "05_ch05.md",
    "06_ch06.md", "07_ch07.md", "08_ch08.md", "09_ch09.md", "10_ch10.md",
    "11_ch11.md", "12_ch12.md", "13_ch13.md", "14_ch14.md", "15_ch15_16.md",
    "17_ch17_app.md", "16_supplements.md", "18_discrepancies.md",
]

# statement headers look like:  **T4.8 `thm:R-finite`** ... [R] ...
HEAD = re.compile(r"\*\*(?:(?:D|L|P|T|C|Cj|E|R|H)\d+\.\d+[′']?\s*/\s*)?((?:D|L|P|T|C|Cj|E|R|H)\d+\.\d+[′']?)\s+`([^`]+)`")
TAG = re.compile(r"\[(R|A|P|C|V)\]")
KIND = {"D": "definition", "L": "lemma", "P": "proposition", "T": "theorem", "C": "corollary",
        "Cj": "conjecture", "E": "example", "R": "remark", "H": "heuristic"}


def registry(texts):
    rows = []
    for name, txt in texts:
        for line in txt.splitlines():
            for m in HEAD.finditer(line):
                num, label = m.group(1), m.group(2)
                rest = line[m.end():]
                t = TAG.search(rest)
                tag = "[" + t.group(1) + "]" if t else "—"
                kind = KIND.get(re.match(r"[A-Za-z]+", num).group(0), "?")
                rows.append((num, label, kind, tag))
    out = ["", "---", "", "## 19. Label registry (auto-generated from the statements above)", "",
           "First rigor tag appearing on the statement line is listed; see the statement for qualifications "
           "(e.g. \"[R] in (PT)\", hypotheses).", "",
           "| No. | `\\label` | kind | tag |", "|---|---|---|---|"]
    seen = set()
    for num, label, kind, tag in rows:
        if label in seen:
            continue
        seen.add(label)
        out.append(f"| {num} | `{label}` | {kind} | {tag} |")
    out.append("")
    out.append(f"Total labelled statements: {len(seen)}.")
    return "\n".join(out) + "\n"


def main():
    texts = []
    for fn in ORDER:
        with open(os.path.join(PARTS, fn), encoding="utf-8") as f:
            texts.append((fn, f.read()))
    toc = [
        "",
        "**Contents of this blueprint:** §0 global architecture (tracks, changes to OUTLINE v0, named hypotheses, "
        "additional binding conventions, meaning of 'proof', page budget, dependency graph) · Chapters 1–17 · "
        "Appendices A–H · §S proof supplements (S1–S9) · §18 discrepancies, corrections and verification tasks · §19 label registry.",
        "",
    ]
    body = []
    for i, (fn, txt) in enumerate(texts):
        body.append(txt.rstrip() + "\n")
        if fn == "00_header.md":
            pass
    head, rest = body[0], body[1:]
    # insert the contents line after the first paragraph block of the header
    lines = head.split("\n")
    insert_at = next((i + 1 for i, l in enumerate(lines) if l.startswith("**Output:**")), 4)
    head = "\n".join(lines[:insert_at] + toc + lines[insert_at:])
    full = head + "\n" + "\n".join(rest) + registry(texts)
    out = os.path.join(HERE, "BLUEPRINT.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(full)
    words = len(re.findall(r"\S+", full))
    print(f"wrote {out}: {len(full)} chars, ~{words} words, {full.count(chr(10))} lines")


if __name__ == "__main__":
    main()
