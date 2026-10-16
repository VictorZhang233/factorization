#!/usr/bin/env python3
"""E19 (stage 2), complementary scan.

(a) Lines mentioning 'Collins' together with a book-style equation/figure/section number
    (e.g. (14.30), eq. 11.6, Fig. 7.10, §14.4, 第 14 章) and an error word on the SAME line or +-1 line.
(b) Any mention of the specific Collins-book errata items that concern signs
    ((14.30), (14.22), (14.23), (14.27), Fig. 7.10, (11.4)-(11.6), (13.116), (11.18), (12.71), (12.72)),
    with or without an error word, so that every place that touches them can be inspected.
Third-party paper sources (frontier/*/papers/) and the verification reports (verify/) are listed
separately, because they are not monograph material.
Run: python3 -I e19_scan2.py <workdir>
"""
import os, re, sys

root = sys.argv[1]
EXT = {'.md', '.tex', '.py', '.tsv', '.json', '.txt', '.bib', '.log', '.csv'}
booknum = re.compile(r"\((?:1[0-4]|[1-9])\.\d{1,3}[a-z]?\)|(?:eq|Eq|eqs|Eqs|Fig|fig|§|Sec|sec|式|图)\.?\s*~?\(?(?:1[0-4]|[1-9])\.\d{1,3}|第\s*~?\d{1,2}\s*~?章")
err = re.compile(r"misprint|typo|errat|sign error|wrong|incorrect|should read|mistake|erroneous|"
                 r"勘误|笔误|印刷|错误|有误|符号错|误印|更正|订正", re.I)
items = re.compile(r"14\.30|14\.22|14\.23|14\.27|7\.10|11\.4\)|11\.5\)|11\.6\)|13\.116|11\.18|12\.71|12\.72")

A, B = [], []
for dp, dns, fns in os.walk(root):
    dns[:] = [d for d in dns if d not in {'.git', 'batch_E19_s2_scripts'}]
    for fn in fns:
        if os.path.splitext(fn)[1].lower() not in EXT:
            continue
        p = os.path.join(dp, fn)
        rel = os.path.relpath(p, root)
        with open(p, encoding='utf-8', errors='replace') as f:
            lines = f.read().split('\n')
        for i, L in enumerate(lines):
            if 'Collins' in L or 'collins' in L.lower():
                win = '\n'.join(lines[max(0, i - 1):i + 2])
                if booknum.search(L) and err.search(win):
                    A.append((rel, i + 1, L.strip()[:400]))
                if items.search(L):
                    B.append((rel, i + 1, L.strip()[:400]))

def show(title, rows):
    print('=' * 100)
    print(title, len(rows))
    for grp in ('monograph material', 'verify/ reports', 'third-party paper sources'):
        sel = [r for r in rows if (grp == 'verify/ reports') == r[0].startswith('verify/')
               and (grp == 'third-party paper sources') == ('/papers/' in r[0])]
        print(f'--- {grp}: {len(sel)}')
        for rel, ln, L in sel:
            print(f'{rel}:{ln}: {L}')

show('(a) Collins + book number + error word (same line or +-1):', A)
show('(b) Collins + specific errata-item numbers:', B)
