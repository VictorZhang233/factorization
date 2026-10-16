"""Check that every bibliography key mentioned in the spec_v2 markdown files exists in refs_merged_v2.bib.

Run: python3 -I keys_check.py WORKDIR   (writes keys_check.log next to this script)
A key is collected from \\cite{...} and from back-quoted INSPIRE-style (Name:2019abc) or readable (Name2019, NameEtAl2019)
tokens. Status: OK = merged key; ALIAS = not a merged key but listed in key_aliases_v2.tsv (allowed only where the text
names it as an alias, e.g. the duplicates table of REFS_NOTES_v2 Sec. 4.6 -- writers must cite the merged key);
UNKNOWN = neither (an error). The script exits with status 1 if any UNKNOWN key is found.
"""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bibparse import parse_bib
W = sys.argv[1].rstrip('/') + '/'
keys = {e['key'] for e in parse_bib(open(W + 'spec_v2/refs_merged_v2.bib', encoding='utf-8').read())}
alias = {}
for l in open(W + 'spec_v2/key_aliases_v2.tsv', encoding='utf-8').read().split('\n')[1:]:
    if l.strip():
        a, k = l.split('\t')[:2]
        alias.setdefault(a, k)
log = []
nunk = 0
for fn in ('WRITER_SPEC_v2.md', 'FIGURES_INDEX_v2.md', 'VERIFIED_FORMULAS_v2.md', 'REFS_NOTES_v2.md', 'FINAL_OUTLINE_v2.md', 'ASSUMPTIONS.md'):  # v2.2: + FINAL_OUTLINE_v2, ASSUMPTIONS
    p = W + 'spec_v2/' + fn
    if not os.path.exists(p):
        log.append('%s: missing file' % fn)
        continue
    t = open(p, encoding='utf-8').read()
    found = set()
    for c in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}', t):
        found.update(k.strip() for k in c.split(','))
    found.update(re.findall(r'`([A-Za-z][A-Za-z\-]*(?::\d{4}[a-z]{2,3}|\d{4}[a-z]?|:[0-9]{4}))`', t))
    ok = sorted(k for k in found if k in keys)
    al = sorted(k for k in found if k not in keys and k in alias)
    unk = sorted(k for k in found if k not in keys and k not in alias)
    nunk += len(unk)
    log.append('%s: %d keys; %d merged keys, %d alias mentions, %d UNKNOWN' % (fn, len(found), len(ok), len(al), len(unk)))
    for k in al:
        log.append('   ALIAS   %s -> %s' % (k, alias[k]))
    for k in unk:
        log.append('   UNKNOWN %s' % k)
log.append('RESULT: %s' % ('PASS (no unknown keys)' if nunk == 0 else 'FAIL (%d unknown keys)' % nunk))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'keys_check.log'), 'w', encoding='utf-8').write('\n'.join(log) + '\n')
print('\n'.join(l for l in log if not l.startswith('   ALIAS')))
sys.exit(1 if nunk else 0)
