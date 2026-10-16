"""Spec v2.1 independent audit of refs_merged_v2.bib: distinct keys, no DOI/arXiv collisions, every entry of the four
source bibliographies resolves (directly or via key_aliases_v2.tsv), every alias points to an existing key.
Run: python3 -I bib_audit_v21.py WORKDIR  (log: bib_audit_v21.log)"""
import re, sys, collections
W = sys.argv[1]
def entries(fn):
    t = open(fn, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}', t, re.S):
        typ, key, body = m.group(1).lower(), m.group(2), m.group(3)
        if typ in ('comment', 'string', 'preamble'): continue
        f = {}
        for fm in re.finditer(r'(\w+)\s*=\s*', body):
            pass
        doi = re.search(r'\bdoi\s*=\s*[{"]+([^}"]+)', body, re.I)
        ep = re.search(r'\beprint\s*=\s*[{"]+([^}"]+)', body, re.I)
        hp = re.search(r'arXiv:\s*([0-9]{4}\.[0-9]{4,5}|[a-z\-]+/[0-9]{7})', body)
        out.append((key, typ, (doi.group(1).lower().strip() if doi else None),
                    (ep.group(1).strip() if ep else (hp.group(1) if hp else None)), body))
    return out
merged = entries(W + '/spec_v2/refs_merged_v2.bib')
keys = [e[0] for e in merged]
print('merged entries', len(merged), 'distinct keys', len(set(keys)))
dup = [k for k, c in collections.Counter(keys).items() if c > 1]
print('duplicate keys:', dup)
bydoi = collections.defaultdict(list); byep = collections.defaultdict(list)
for k, t, d, e, b in merged:
    if d: bydoi[d].append(k)
    if e: byep[re.sub(r'v\d+$', '', e)].append(k)
print('DOI collisions:', {d: v for d, v in bydoi.items() if len(v) > 1})
print('eprint collisions:', {d: v for d, v in byep.items() if len(v) > 1})
al = {}
for ln in open(W + '/spec_v2/key_aliases_v2.tsv', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) >= 2 and p[0] != 'alias': al.setdefault(p[0], p[1])
ks = set(keys)
for src in ['spec/refs_merged.bib', 'frontier/lamet/lamet.bib', 'frontier/yzliu/yzliu.bib', 'frontier/others/others.bib']:
    es = entries(W + '/' + src)
    lost = [e[0] for e in es if e[0] not in ks and al.get(e[0]) not in ks]
    print(src, 'entries', len(es), 'unresolved', lost[:10])
bad_alias = [(a, k) for a, k in al.items() if k not in ks]
print('aliases pointing to missing keys:', bad_alias[:10])
m = {e[0]: e[4] for e in merged}
for k in ['Ji:2020brr', 'Ji:2020ect', 'Ji:2019ewn', 'JiEtAl2021']:
    if k in m:
        a = re.search(r'author\s*=\s*[{"](.*?)[}"],?\n', m[k], re.S)
        print(k, '|', (a.group(1)[:200] if a else None))
