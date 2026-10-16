"""Spec v2.1: every key-like reference in verify/CLAIMS.md must resolve to a merged key of refs_merged_v2.bib
(directly or via key_aliases_v2.tsv).  Run: python3 -I claims_keys_check.py WORKDIR  (log: claims_keys_check.log)"""
import re, sys
W = sys.argv[1]
bib = open(W + '/spec_v2/refs_merged_v2.bib', encoding='utf-8').read()
keys = set(re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib))
al = {}
for ln in open(W + '/spec_v2/key_aliases_v2.tsv', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) >= 2 and p[0] != 'alias':
        al.setdefault(p[0], p[1])
txt = open(W + '/verify/CLAIMS.md', encoding='utf-8').read()
# texkeys Name:YYYYabc and readable CamelCaseYYYY keys
cands = set(re.findall(r'\b([A-Z][A-Za-z\-\']+:\d{4}[a-z]{2,3})\b', txt))
cands |= set(re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)*(?:EtAl)?\d{4}[a-z]?)\b', txt))
missing = []
for c in sorted(cands):
    if c in keys: continue
    if c in al and al[c] in keys: continue
    missing.append(c)
print('candidates:', len(cands), 'missing:', len(missing))
for m in missing: print('  MISSING', m)
