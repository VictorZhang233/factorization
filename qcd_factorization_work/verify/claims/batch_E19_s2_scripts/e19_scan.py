#!/usr/bin/env python3
"""E19 (stage 2): proximity scan of the whole work directory.

For every text-like file, find lines that refer to Collins' 2011 book
(Collins 2011, Foundations, Collins:2011zzd, Collins2011, 'the book', Collins (2011) ...)
and report every such reference that has an error-type word within +-W lines.
Different from a plain keyword grep: the window couples the two conditions, and
the set of error words is wide (English + Chinese).  Output: one record per hit,
deduplicated by (file, line).  Run: python3 -I e19_scan.py <workdir> [W]
"""
import os, re, sys

root = sys.argv[1]
W = int(sys.argv[2]) if len(sys.argv) > 2 else 3
SKIP_DIRS = {'.git', 'batch_E19_s2_scripts'}
EXT = {'.md', '.tex', '.py', '.tsv', '.json', '.txt', '.bib', '.log', '.csv', '.out', '.sty', '.cls', '.yaml', '.yml'}

collins = re.compile(r"Collins\s*\(?\s*2011|Collins:2011zzd|Collins2011|Collins'?s? book|Foundations of [Pp]erturbative|"
                     r"Collins,?\s*\*?Foundations|Collins\s+(?:eq|Eq|Fig|fig|Sec|sec|ch|Ch)\.?\s*\(?\d|Collins\s*\[?2011|"
                     r"Collins\s+book|柯林斯|Collins\s*（2011|Collins\s*2023|9781009401845")
err = re.compile(r"misprint|typo|errat|sign error|wrong sign|wrong|incorrect|should read|should be|mistake|erroneous|"
                 r"correct(?:ed|ion)|withdraw|勘误|笔误|印刷|错误|有误|符号错|误印|更正|订正|修正", re.I)

hits = []
nfiles = 0
for dp, dns, fns in os.walk(root):
    dns[:] = [d for d in dns if d not in SKIP_DIRS]
    for fn in fns:
        if os.path.splitext(fn)[1].lower() not in EXT:
            continue
        p = os.path.join(dp, fn)
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                lines = f.read().split('\n')
        except Exception as e:
            print('READ-FAIL', p, e)
            continue
        nfiles += 1
        for i, L in enumerate(lines):
            if not collins.search(L):
                continue
            lo, hi = max(0, i - W), min(len(lines), i + W + 1)
            window = '\n'.join(lines[lo:hi])
            m = err.findall(window)
            if m:
                hits.append((os.path.relpath(p, root), i + 1, sorted(set(x.lower() for x in m)), L.strip()[:300]))

print(f'files scanned: {nfiles}; Collins-2011 references with an error word within +-{W} lines: {len(hits)}')
for rel, ln, words, text in hits:
    print(f'--- {rel}:{ln}  words={words}\n    {text}')
