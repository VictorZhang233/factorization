# A02: compare INSPIRE BAI search (a Y.Liu.90) with quoted name search (a "Liu, Yizhuang").
# Usage: python3 -I a02_inspire_counts.py bai.json name.json
import json, sys
bai = json.load(open(sys.argv[1]))['hits']
nam = json.load(open(sys.argv[2]))['hits']
print('BAI total =', bai['total'], ' name total =', nam['total'])
def key(h):
    m = h['metadata']
    return m.get('texkeys', ['?'])[0]
def liu_entry(h):
    out = []
    for a in h['metadata'].get('authors', []):
        if a['full_name'].startswith('Liu, Y'):
            ids = [i['value'] for i in a.get('ids', []) if i.get('schema') == 'INSPIRE BAI']
            out.append((a['full_name'], ids, [x.get('value') for x in a.get('affiliations', [])]))
    return out
B = {key(h): h for h in bai['hits']}
N = {key(h): h for h in nam['hits']}
print('in BAI not in name:', sorted(set(B) - set(N)))
for k in sorted(set(B) - set(N)):
    print('   ', k, B[k]['metadata']['titles'][0]['title'], liu_entry(B[k]))
print('in name not in BAI:', sorted(set(N) - set(B)))
for k in sorted(set(N) - set(B)):
    print('   ', k, N[k]['metadata']['titles'][0]['title'], liu_entry(N[k]))
dates = sorted(h['metadata'].get('earliest_date', '?') for h in bai['hits'])
print('BAI earliest/latest date:', dates[0], dates[-1])
# affiliation history of Y.Liu.90 by year (from BAI records with affiliations)
from collections import defaultdict
aff = defaultdict(set)
for h in bai['hits']:
    d = h['metadata'].get('earliest_date', '????')[:4]
    for a in h['metadata'].get('authors', []):
        ids = [i['value'] for i in a.get('ids', []) if i.get('schema') == 'INSPIRE BAI']
        if 'Y.Liu.90' in ids:
            for x in a.get('affiliations', []):
                aff[d].add(x.get('value'))
for y in sorted(aff):
    print(y, sorted(aff[y]))
