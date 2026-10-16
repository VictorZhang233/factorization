import sys, os, re, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))

BIB = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec/refs_merged.bib"
REF = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/refdoc/work_R4/bib.txt"

txt = open(BIB, encoding='utf-8').read()
entries = []
for m in re.finditer(r'@(\w+)\{([^,]+),(.*?)\n\}', txt, re.S):
    typ, key, body = m.group(1), m.group(2), m.group(3)
    f = {}
    for fm in re.finditer(r'(\w+)\s*=\s*(\{(.*?)\}|"(.*?)")\s*,?\s*\n', body + '\n', re.S):
        val = fm.group(3) if fm.group(3) is not None else fm.group(4)
        f[fm.group(1).lower()] = re.sub(r'\s+', ' ', val).replace('{', '').replace('}', '')
    f['key'] = key
    f['type'] = typ
    entries.append(f)

# parse reference list
lines = open(REF, encoding='utf-8').read().split('\n')
refs = {}
cur = None
for ln in lines:
    if re.match(r'^\S*参考文献\s+\d+\s*$', ln.strip()) or ln.strip().startswith('参考文献'):
        continue
    m = re.match(r'^\s*\[(\d+)\]\s*(.*)$', ln)
    if m:
        cur = int(m.group(1))
        refs[cur] = m.group(2).strip()
    elif cur is not None and ln.strip():
        refs[cur] += ' ' + ln.strip()

def first_page(p):
    return re.split(r'[-–]', p)[0].strip() if p else ''

out = []
for n in sorted(refs):
    r = refs[n]
    # find volume/page/year patterns like "B 261 (1985) 104" or "57 (1998) 3051"
    vps = re.findall(r'(\d+)\s*\((\d{4})\)\s*([A-Za-z]?\d+)', r)
    cands = []
    for vol, yr, pg in vps:
        for e in entries:
            if e.get('volume', '').strip() == vol and first_page(e.get('pages', '')) == pg:
                cands.append(e)
    # title match fallback
    tm = re.search(r'“(.*?)”', r)
    title = tm.group(1) if tm else ''
    if not cands and title:
        tw = set(w.lower() for w in re.findall(r'[A-Za-z]{4,}', title))
        best = None; bs = 0
        for e in entries:
            ew = set(w.lower() for w in re.findall(r'[A-Za-z]{4,}', e.get('title', '')))
            if not ew: continue
            s = len(tw & ew) / max(1, len(tw | ew))
            if s > bs:
                bs, best = s, e
        if best is not None and bs > 0.5:
            cands.append(best)
    out.append((n, r, cands))

for n, r, cands in out:
    print('=' * 100)
    print(f'[{n}] {r}')
    if not cands:
        print('   --> NO MATCH in refs_merged.bib')
    seen = set()
    for e in cands:
        if e['key'] in seen: continue
        seen.add(e['key'])
        print(f"   --> {e['key']}: {e.get('author','')} | {e.get('title','')} | {e.get('journal','')} {e.get('volume','')} ({e.get('year','')}) {e.get('pages','')} | {e.get('eprint','')} | note={e.get('note','')}")
