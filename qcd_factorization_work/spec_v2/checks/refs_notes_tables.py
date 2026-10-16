"""Generate the per-key tables of REFS_NOTES_v2.md for all entries that are new in spec v2.

Usage: python3 -I refs_notes_tables.py WORKDIR OUTFILE
For every new key: bibliographic one-liner, source bibliography, the sections of the frontier report
that cite it, and the reading depth recorded by the frontier agent next to the citation
(read / abstract / title / recall / not marked).  The depth is extracted heuristically from the
markers the agents used: LAMET.md '*(read)*', '*(abstract)*', '*(title)*'; YZLIU.md '[txt ...]',
'[abs]', '[bib]' and its publication-map column; OTHERS.md section tables of Appendix A and the
list of papers read in full (Sec. 0.3, arXiv numbers).  Writers must still read the report passage
before attributing content (WRITER_SPEC_v2 Sec. 8).
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bibparse import parse_bib

W = sys.argv[1].rstrip('/') + '/'
OUT = sys.argv[2]
bib = {e['key']: e for e in parse_bib(open(W + 'spec_v2/refs_merged_v2.bib', encoding='utf-8').read(), 'v2')}
log = [l.rstrip('\n').split('\t') for l in open(W + 'spec_v2/checks/merge_log_v2.tsv', encoding='utf-8')][1:]
REP = {'lamet': W + 'frontier/lamet/LAMET.md', 'yzliu': W + 'frontier/yzliu/YZLIU.md', 'others': W + 'frontier/others/OTHERS.md'}
rep = {k: open(v, encoding='utf-8').read() for k, v in REP.items()}

def headings(text):
    hs = []
    for m in re.finditer(r'^(#{2,4}|\*\*§)\s*([^\n]*)', text, re.M):
        hs.append((m.start(), m.group(2).strip()))
    return hs

HS = {k: headings(v) for k, v in rep.items()}

def section_of(src, pos):
    best = ''
    for p, h in HS[src]:
        if p <= pos: best = h
        else: break
    m = re.match(r'([0-9A-F][0-9.]*|[A-F]\d+\.|Appendix [AB]\.?|§[0-9–\- ]+)', best)
    return (m.group(1).rstrip('.') if m else best[:28]).strip()

def depth_markers(src, text, pos):
    win = text[pos:pos + 160]
    d = set()
    if re.search(r'\(read[:)\s]|\[read|\[txt', win): d.add('read')
    if re.search(r'abstract|\[abs\]', win): d.add('abstract')
    if re.search(r'\(title\)', win): d.add('title')
    if re.search(r'\(recall\)', win): d.add('recall')
    if re.search(r'\[bib\]', win): d.add('bib')
    return d

# OTHERS: arXiv numbers read in full (Sec. 0.3)
m = re.search(r'### 0\.3 Sources read in full in this session(.*?)### 0\.4', rep['others'], re.S)
others_read = set(re.findall(r'(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})', m.group(1))) if m else set()
# YZLIU: publication map read column
yz_read = {}
for row in re.findall(r'^\| [IVX]+\.\d+ \| `([^`]+)` \|[^\n]*\| (full|main[^|]*|intro[^|]*|partial|abs|[^|]+) \| [^|]* \|$', rep['yzliu'], re.M):
    yz_read[row[0]] = row[1].strip()

def bibline(e):
    f = e['fields']
    au = f.get('author', '') or f.get('collaboration', '')
    names = [a.split(',')[0].strip(' {}') for a in au.split(' and ')]
    names = [re.sub(r'[{}\\"\']', '', n) for n in names if n]
    if 'others' in names or len(names) > 3:
        a = names[0] + ' et al.'
    else:
        a = '–'.join(names)
    j = f.get('journal', '')
    if j:
        s = '%s %s (%s) %s' % (j, f.get('volume', ''), f.get('year', ''), (f.get('pages', '') or '').split('-')[0])
    elif e['type'] == 'misc':
        s = 'preprint ' + f.get('howpublished', '').replace('arXiv:', 'arXiv:') + ' (%s)' % f.get('year', '')
    elif e['type'] in ('book', 'techreport', 'inbook', 'incollection'):
        s = '%s %s (%s)' % (e['type'], f.get('publisher', '') or f.get('institution', ''), f.get('year', ''))
    else:
        s = '%s (%s)' % (e['type'], f.get('year', ''))
    t = re.sub(r'[{}]', '', f.get('title', ''))
    t = re.sub(r'\s+', ' ', t)
    if len(t) > 90: t = t[:87] + '...'
    return a, s.strip(), t

rows = collections.OrderedDict((s, []) for s in ('yzliu', 'lamet', 'others', 'spec-v2 INSPIRE', 'spec-v2 manual'))
for key, src, status, mk, how, notes in log:
    s0 = src.split(':')[0]
    if status != 'new': continue
    e = bib[key]
    a, s, t = bibline(e)
    secs, deps = [], set()
    if s0 in rep:
        txt = rep[s0]
        for mm in re.finditer(re.escape(key) + r'(?![A-Za-z0-9])', txt):
            secs.append(section_of(s0, mm.start()))
            deps |= depth_markers(s0, txt, mm.start())
        if s0 == 'others':
            ep = e['fields'].get('eprint', '')
            if ep and ep in others_read: deps.add('read')
            elif ep or e['fields'].get('doi'): deps.add('abstract')
        if s0 == 'yzliu' and key in yz_read:
            v = yz_read[key]
            yzd = ('read (full)' if v == 'full' else 'read (main text)' if v.startswith('main') else
                   'read (intro/concl.)' if v.startswith('intro') else 'read (partial)' if v == 'partial' else
                   'abstract' if v.startswith('abs') else v)
            deps.add(yzd)
    secs = sorted(set(x for x in secs if x), key=lambda z: (len(z), z))
    yzs = [d for d in deps if d.startswith('read (')]
    dep = (yzs[0] if yzs else 'read' if 'read' in deps else 'abstract' if 'abstract' in deps else
           'title' if 'title' in deps else 'recall' if 'recall' in deps else 'bib' if 'bib' in deps else '—')
    pre = 'yes' if e['type'] == 'misc' and not e['fields'].get('journal') else ''
    rows[s0].append((key, a, s, t, ', '.join(secs[:6]), dep, pre))

names = {'yzliu': 'frontier/yzliu/yzliu.bib (report YZLIU.md)', 'lamet': 'frontier/lamet/lamet.bib (report LAMET.md)',
         'others': 'frontier/others/others.bib (report OTHERS.md)', 'spec-v2 INSPIRE': 'spec-v2 additions (INSPIRE-HEP)',
         'spec-v2 manual': 'spec-v2 manual entries (Crossref)'}
with open(OUT, 'w', encoding='utf-8') as fh:
    for s0, lst in rows.items():
        fh.write('\n### New keys from %s — %d entries\n\n' % (names[s0], len(lst)))
        fh.write('| key | authors | publication | title | cited in (report §) | depth | preprint |\n|---|---|---|---|---|---|---|\n')
        for r in sorted(lst, key=lambda z: z[0].lower()):
            fh.write('| `%s` | %s | %s | %s | %s | %s | %s |\n' % tuple(x.replace('|', '/') for x in r))
    # duplicates: frontier keys that map to an existing key
    fh.write('\n### Frontier keys that are duplicates of an existing entry (use the merged key)\n\n')
    fh.write('| frontier key | source | merged key | match |\n|---|---|---|---|\n')
    for key, src, status, mk, how, notes in log:
        if status == 'duplicate' and key != mk:
            fh.write('| `%s` | %s | `%s` | %s |\n' % (key, src, mk, how))
    fh.write('\nFrontier keys identical to an existing key (same INSPIRE texkey; nothing to replace): %s.\n' %
             ', '.join('`%s`' % k for k in sorted(set(k for k, src, st, mk, how, n in log if st == 'duplicate' and k == mk), key=str.lower)))
print('written', OUT)
for s0, lst in rows.items(): print(s0, len(lst))
