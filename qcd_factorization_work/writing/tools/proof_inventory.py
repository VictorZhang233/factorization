#!/usr/bin/env python3
"""Inventory of everything the outline does NOT prove completely (for the proof-completion phase).
For each unit: the 'Box' lines; every statement tagged [A]/[P]/[C]/[V]; every [R] statement whose proof plan
is a sketch; with the status/gap text. Output: proofs/INVENTORY.json and proofs/INVENTORY.md."""
import os, re, json
W = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
t = open(os.path.join(W, 'spec_v2', 'FINAL_OUTLINE_v2.md')).read().split('\n')
heads = [i for i, l in enumerate(t) if l.startswith('## ')]
def unit_of(l):
    if l.startswith('## Front matter'): return 'front'
    m = re.match(r'## Chapter (\d+) —', l)
    if m: return 'Ch%02d' % int(m.group(1))
    m = re.match(r'## Appendix ([A-Q]) —', l)
    if m: return 'App' + m.group(1)
    return None
STMT = re.compile(r'^\s*[\*\-] \*\*(定义|假设|定理|引理|命题|推论|猜想|注|例)\s*`([^`]+)`\s*—\s*(.*?)\*\*\s*(.*)$')
units = []
for k, i in enumerate(heads):
    u = unit_of(t[i])
    if not u: continue
    j = heads[k + 1] if k + 1 < len(heads) else len(t)
    sec = t[i:j]
    box = []
    for a, l in enumerate(sec):
        if l.startswith('**Box'):
            b = a + 1
            while b < len(sec) and (sec[b].startswith('- ') or sec[b].strip() == '' and b == a + 1):
                if sec[b].startswith('- '): box.append(sec[b][2:].strip())
                b += 1
            break
    items = []
    a = 0
    while a < len(sec):
        m = STMT.match(sec[a])
        if not m: a += 1; continue
        typ, lab, title, rest = m.groups()
        tagm = re.match(r'\s*\[([^\]]+)\]', rest) or re.search(r'\[(R[^\]]*|A|P|C|V|\\tag[APCRV])\]', rest)
        tag = tagm.group(1) if tagm else 'none'
        # gather the entry body (sub-items or same line for App M-Q format)
        body = [sec[a]]
        b = a + 1
        while b < len(sec) and not STMT.match(sec[b]) and not sec[b].startswith('## ') and not sec[b].startswith('### '):
            body.append(sec[b]); b += 1
        txt = '\n'.join(body)
        status = ''
        ms = re.search(r'(地位与缺口[^\n]*\n?(?:[^\n]*\n){0,6})', txt)
        if ms: status = ms.group(1)
        sketch = bool(re.search(r'(Proof[^\n]{0,40}sketch|sketch\b|proofsketch|概要)', txt, re.I))
        full = bool(re.search(r'(Proof[^\n]{0,20}full|\bfull\b proof|证明.{0,6}完整)', txt, re.I))
        t0 = tag.replace('\\tag', '')
        cls = None
        if t0.startswith(('A', 'P', 'C', 'V')): cls = t0[0]
        elif t0.startswith('R') and sketch and not full: cls = 'R-sketch'
        if cls and typ not in ('注', '例') or (cls in ('A', 'P', 'C', 'V') and typ in ('注', '例')):
            items.append(dict(label=lab, type=typ, title=title.strip(), tag=tag, cls=cls, status=status.strip()[:1500], entry=txt[:2500]))
        a = b
    units.append(dict(unit=u, head=t[i][3:], box=box, items=items))
json.dump(units, open(os.path.join(W, 'proofs', 'INVENTORY.json'), 'w'), ensure_ascii=False, indent=1)
out = ['# Proof-completion inventory (generated from FINAL_OUTLINE_v2 by writing/tools/proof_inventory.py)\n']
tot = {}
for U in units:
    out.append(f"\n## {U['unit']} — {U['head']}\n")
    if U['box']:
        out.append('Box:\n' + '\n'.join('- ' + x for x in U['box']) + '\n')
    for it in U['items']:
        tot[it['cls']] = tot.get(it['cls'], 0) + 1
        out.append(f"- [{it['cls']}] `{it['label']}` ({it['type']}, tag {it['tag']}) — {it['title']}")
open(os.path.join(W, 'proofs', 'INVENTORY.md'), 'w').write('\n'.join(out) + '\n')
print('items by class:', tot, '; units:', len(units))
