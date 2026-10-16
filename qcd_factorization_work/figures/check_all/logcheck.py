#!/usr/bin/env python3
r"""Summarise check_all.log: errors, overfull/underfull boxes, missing characters, multiply defined
labels, undefined references; per-figure picture widths (CHKPIC lines); map figure ordinal -> label
using the order of \label{fig:...} inside the figure environments of the sources.

    python3 -I logcheck.py check_all.log src/figures1.tex ... src/figset_F.tex
"""
import re
import sys

log = open(sys.argv[1], encoding='utf-8', errors='replace').read()
srcs = sys.argv[2:]

# figure ordinal -> (file, label, first line)
figs = []
for f in srcs:
    lines = open(f, encoding='utf-8').read().splitlines()
    depth, cur = 0, None
    for i, line in enumerate(lines, 1):
        s = re.sub(r'(?<!\\)%.*', '', line)
        if re.search(r'\\begin\{figure\*?\}', s):
            depth += 1
            if depth == 1:
                cur = {'file': f.split('/')[-1], 'line': i, 'labels': []}
        for m in re.finditer(r'\\label\{(fig:[^}]*)\}', s):
            if cur is not None:
                cur['labels'].append(m.group(1))
        if re.search(r'\\end\{figure\*?\}', s):
            depth -= 1
            if depth == 0 and cur is not None:
                figs.append(cur)
                cur = None
print('figure environments in sources:', len(figs))

# errors
errs = [l for l in log.splitlines() if l.startswith('!') or 'LaTeX Error' in l or 'Emergency stop' in l]
print('ERRORS:', len(errs))
for e in errs[:30]:
    print('   ', e)

# file attribution for box warnings: walk the log tracking (./src/xxx.tex
stack = []
cur_file = 'check_all.tex'
box = []
for line in log.splitlines():
    for m in re.finditer(r'\((\./[^\s()]+\.tex)', line):
        cur_file = m.group(1)
    mm = re.match(r'^(Overfull|Underfull) \\([hv])box \(([^)]*)\) (.*)', line)
    if mm:
        box.append((mm.group(1), mm.group(2), mm.group(3), mm.group(4), cur_file))
print('BOX WARNINGS:', len(box))
for b in box:
    print('   ', b)

miss = sorted(set(re.findall(r'Missing character: There is no (.*?) in font (.*?)!', log)))
print('MISSING CHARACTERS:', len(miss))
for m in miss[:40]:
    print('   ', m)

mult = sorted(set(re.findall(r"Label `([^']*)' multiply defined", log)))
print('MULTIPLY DEFINED:', mult if mult else 'none')
undef = sorted(set(re.findall(r"Reference `([^']*)' on page \d+ undefined", log)))
print('UNDEFINED REFERENCES:', undef if undef else 'none')
cites = sorted(set(re.findall(r"Citation `([^']*)' on page \d+ undefined", log)))
print('UNDEFINED CITATIONS (expected: no bib in the test):', cites)
other = [l for l in log.splitlines() if re.search(r'(Package|LaTeX|Class) \S* ?Warning', l)
         and 'Citation' not in l and 'Reference' not in l and 'There were undefined' not in l]
print('OTHER WARNINGS:', len(other))
for o in sorted(set(other))[:40]:
    print('   ', o)

# picture widths
TEXTW = 455.24411  # 16 cm in pt (A4, 2.5 cm margins: 21-5 = 16 cm = 455.244 pt)
pics = {}
for m in re.finditer(r'CHKPIC (\d+) w=([\d.]+)pt h=([\d.]+)pt', log):
    pics.setdefault(int(m.group(1)), []).append((float(m.group(2)), float(m.group(3))))
print('PICTURE WIDTHS > 0.98 textwidth (single picture):')
for k in sorted(pics):
    wmax = max(w for w, h in pics[k])
    lab = figs[k - 1]['labels'] if k - 1 < len(figs) else '?'
    if wmax > 0.98 * TEXTW:
        print('    fig #%d %s  max pic width %.1f pt = %.2f cm' % (k, lab, wmax, wmax / 28.4528))
with open('figwidths.tsv', 'w') as fo:
    for k in sorted(pics):
        lab = figs[k - 1]['labels'] if k - 1 < len(figs) else ['?']
        fo.write('%d\t%s\t%s\t%s\n' % (k, figs[k - 1]['file'] if k - 1 < len(figs) else '?', ','.join(lab),
                                      ' '.join('%.1fx%.1fcm' % (w / 28.4528, h / 28.4528) for w, h in pics[k])))
