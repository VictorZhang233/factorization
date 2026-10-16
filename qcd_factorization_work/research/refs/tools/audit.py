import sys, re, json, os, difflib, unicodedata
bib, dl = sys.argv[1], sys.argv[2]
txt = open(bib, encoding='utf-8').read()
def asc(s):
    s = unicodedata.normalize('NFKD', s); return ''.join(c for c in s if not unicodedata.combining(c))
def norm(t):
    t = asc(t).lower(); t = re.sub(r'<[^>]+>', ' ', t); t = re.sub(r'\\[a-z]+', ' ', t)
    t = re.sub(r'[^a-z0-9]+', ' ', t); return ' '.join(t.split())
ents = re.findall(r'@(\w+)\{([^,]+),\n(.*?)\n\}', txt, flags=re.S)
n = 0; bad = 0
for typ, key, body in ents:
    f = dict(re.findall(r'^\s*(\w+)\s*=\s*\{(.*)\},?\s*$', body, flags=re.M))
    d = f.get('doi')
    if not d: continue
    p = os.path.join(dl, 'crossref', re.sub(r'[^A-Za-z0-9._-]', '_', d.lower()) + '.json')
    if not os.path.exists(p):
        print('NO CROSSREF FILE', key, d); continue
    j = json.load(open(p, encoding='utf-8'))
    if j.get('status') != 'ok': print('CR not ok', key); continue
    m = j['message']; n += 1
    probs = []
    if typ == 'article':
        cv = str(m.get('volume') or ''); bv = f.get('volume', '')
        jn = f.get('journal', '')
        cy = (m.get('published-print') or m.get('issued'))['date-parts'][0][0]
        if jn == 'JHEP':
            if cv != f.get('year'): probs.append('JHEP vol/year %s vs %s' % (cv, f.get('year')))
        elif cv.lstrip('0') != bv.lstrip('0'): probs.append('volume %s vs CR %s' % (bv, cv))
        cp = (m.get('page') or m.get('article-number') or '').split('-')[0]
        bp = f.get('pages', '').split('--')[0]
        if cp.lstrip('0') != bp.lstrip('0'): probs.append('page %s vs CR %s' % (bp, cp))
        cr_last = (m.get('page') or '').split('-')[1] if '-' in (m.get('page') or '') else None
        if '--' in f.get('pages', '') and cr_last and f['pages'].split('--')[1] != cr_last: probs.append('last page %s vs CR %s' % (f['pages'], m.get('page')))
        if abs(int(f.get('year', 0)) - int(cy)) > 0: probs.append('year %s vs CR %s' % (f.get('year'), cy))
    ct = (m.get('title') or [''])[0]
    r = difflib.SequenceMatcher(None, norm(f.get('title', '')), norm(ct)).ratio()
    if r < 0.8: probs.append('title ratio %.2f: bib "%s" | CR "%s"' % (r, f.get('title'), ct[:120]))
    fa = re.split(r'\s+and\s+', f.get('author', ''))[0].split(',')[0].strip('{} ')
    ca = [a.get('family', '') for a in m.get('author', [])]
    if ca and norm(fa).replace(' ', '') not in norm(' '.join(ca)).replace(' ', ''): probs.append('first author %s not in CR %s' % (fa, ca[:4]))
    if probs:
        bad += 1; print(key, '|', '; '.join(probs))
print('audited', n, 'entries with DOI; flagged', bad)
