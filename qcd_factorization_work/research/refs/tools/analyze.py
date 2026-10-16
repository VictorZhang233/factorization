"""Cross-check INSPIRE vs expectations vs Crossref vs arXiv.
usage: python3 -I analyze.py SPEC_PY DL_DIR OUT_JSON [--verbose]"""
import sys, os, json, re, unicodedata, difflib
import xml.etree.ElementTree as ET

spec_path, dl, out_json = sys.argv[1], sys.argv[2], sys.argv[3]
verbose = '--verbose' in sys.argv
ns = {}
exec(open(spec_path, encoding='utf-8').read(), ns)
S = ns['S']

def safe(s):
    return re.sub(r'[^A-Za-z0-9._-]', '_', s)

def asc(s):
    s = unicodedata.normalize('NFKD', s or '')
    return ''.join(c for c in s if not unicodedata.combining(c))

def norm_title(t):
    t = asc(t or '').lower()
    t = re.sub(r'<[^>]+>', ' ', t)          # MathML/HTML tags from Crossref
    t = re.sub(r'\\[a-z]+', ' ', t)          # LaTeX commands
    t = re.sub(r'[^a-z0-9]+', ' ', t)
    return ' '.join(t.split())

def surname_key(s):
    s = asc(s).lower()
    s = s.replace("'t ", 't').replace('van ', 'van').replace('de ', 'de')
    return re.sub(r'[^a-z]', '', s)

def insp_surnames(m):
    out = []
    for a in m.get('authors', []) or []:
        fn = a['full_name']
        out.append(fn.split(',')[0].strip())
    return out

# arXiv
ARX = {}
ATOM = '{http://www.w3.org/2005/Atom}'
ARXNS = '{http://arxiv.org/schemas/atom}'
for fn in sorted(os.listdir(os.path.join(dl, 'arxiv'))):
    if not fn.endswith('.xml'):
        continue
    root = ET.parse(os.path.join(dl, 'arxiv', fn)).getroot()
    for ent in root.findall(ATOM + 'entry'):
        idurl = ent.findtext(ATOM + 'id') or ''
        m = re.search(r'abs/(.+?)(v\d+)?$', idurl)
        if not m:
            continue
        aid = m.group(1)
        ARX[aid] = dict(title=' '.join((ent.findtext(ATOM + 'title') or '').split()),
                        authors=[a.findtext(ATOM + 'name') for a in ent.findall(ATOM + 'author')],
                        published=ent.findtext(ATOM + 'published'),
                        journal_ref=ent.findtext(ARXNS + 'journal_ref'),
                        doi=ent.findtext(ARXNS + 'doi'),
                        primary=(ent.find(ARXNS + 'primary_category').attrib.get('term') if ent.find(ARXNS + 'primary_category') is not None else None))

def crossref(doi):
    p = os.path.join(dl, 'crossref', safe(doi.lower()) + '.json')
    if not os.path.exists(p):
        return None
    d = json.load(open(p, encoding='utf-8'))
    if d.get('status') != 'ok':
        return None
    m = d['message']
    def yr(k):
        v = m.get(k, {}).get('date-parts', [[None]])
        return v[0][0] if v and v[0] else None
    return dict(doi=m.get('DOI'), type=m.get('type'), title=(m.get('title') or [''])[0],
                subtitle=(m.get('subtitle') or [''])[0] if m.get('subtitle') else '',
                authors=[(a.get('given', ''), a.get('family', a.get('name', ''))) for a in m.get('author', [])],
                container=(m.get('container-title') or [''])[0], short=(m.get('short-container-title') or [''])[0],
                volume=m.get('volume'), issue=m.get('issue'), page=m.get('page'), artno=m.get('article-number'),
                issued=yr('issued'), pprint=yr('published-print'), ponline=yr('published-online'),
                publisher=m.get('publisher'), isbn=m.get('ISBN'), relation=m.get('relation'),
                update_to=m.get('update-to'))

def first_page(pg):
    if not pg:
        return None
    return re.split(r'[-–]', str(pg))[0].strip()

results = {}
nwarn = 0
for e in S:
    key = e['key']
    rep = dict(key=key, issues=[], notes=[])
    p = os.path.join(dl, 'inspire', key + '.json')
    if not os.path.exists(p):
        rep['issues'].append('NO INSPIRE FILE')
        results[key] = rep
        continue
    d = json.load(open(p, encoding='utf-8'))
    hits = d['hits']['hits']
    rep['nhits'] = len(hits)
    if len(hits) != 1:
        rep['issues'].append('INSPIRE hits=%d' % len(hits))
    if not hits:
        results[key] = rep
        continue
    m = hits[0]['metadata']
    rep['recid'] = m.get('control_number')
    rep['texkeys'] = m.get('texkeys')
    rep['doctype'] = m.get('document_type')
    rep['title'] = m['titles'][0]['title']
    rep['alt_titles'] = [t['title'] for t in m['titles'][1:]]
    rep['authors'] = [a['full_name'] for a in m.get('authors', []) or []]
    rep['nauthors'] = len(rep['authors'])
    rep['collaborations'] = [c['value'] for c in m.get('collaborations', []) or []]
    rep['pubinfo'] = m.get('publication_info', [])
    rep['dois'] = [x['value'] for x in m.get('dois', []) or []]
    rep['arxiv'] = [(x['value'], x.get('categories')) for x in m.get('arxiv_eprints', []) or []]
    rep['imprints'] = m.get('imprints')
    rep['isbns'] = m.get('isbns')
    rep['book_series'] = m.get('book_series')
    rep['report_numbers'] = [r['value'] for r in m.get('report_numbers', []) or []]
    rep['number_of_pages'] = m.get('number_of_pages')
    # --- expectations
    sn = [surname_key(s) for s in insp_surnames(m)]
    exp = [surname_key(s) for s in e['au']]
    if exp:
        if not sn:
            rep['issues'].append('no authors in INSPIRE')
        elif sn[0] != exp[0]:
            rep['issues'].append('first author mismatch: INSPIRE %s vs expected %s' % (sn[:3], exp[:3]))
        elif len(exp) > 1 and sn[:len(exp)] != exp:
            rep['issues'].append('author list mismatch: INSPIRE %s vs expected %s' % (sn, exp))
        if len(exp) > 1 and len(sn) != len(exp) and len(sn) < 12:
            rep['issues'].append('author count INSPIRE %d vs expected %d' % (len(sn), len(exp)))
    # main publication info
    main = None
    errata = []
    others = []
    for pi in rep['pubinfo']:
        if pi.get('material') == 'erratum':
            errata.append(pi)
        elif pi.get('journal_title') and main is None and pi.get('material') not in ('addendum', 'reprint', 'translation'):
            main = pi
        else:
            others.append(pi)
    rep['main'] = main
    rep['errata'] = errata
    rep['otherpub'] = others
    if e.get('j'):
        if not main:
            rep['issues'].append('no journal pubinfo in INSPIRE (expected %s %s %s)' % (e['j'], e['v'], e['p']))
        else:
            if main.get('journal_title') != e['j']:
                rep['issues'].append('journal %s vs expected %s' % (main.get('journal_title'), e['j']))
            if e.get('v') and str(main.get('journal_volume')) != str(e['v']):
                rep['issues'].append('volume %s vs expected %s' % (main.get('journal_volume'), e['v']))
            pg = main.get('page_start') or main.get('artid')
            if e.get('p') and str(pg) != str(e['p']):
                rep['issues'].append('page %s vs expected %s' % (pg, e['p']))
    yr = (main or {}).get('year')
    if e.get('y') and yr and int(yr) != int(e['y']):
        rep['issues'].append('year %s vs expected %s' % (yr, e['y']))
    if e.get('y') and not yr and rep['doctype'] not in (['book'],):
        rep['notes'].append('no journal year in INSPIRE')
    # --- Crossref cross-check
    cr = {}
    for doi in rep['dois']:
        c = crossref(doi)
        if c:
            cr[doi.lower()] = c
        else:
            rep['notes'].append('crossref unavailable for %s' % doi)
    rep['crossref'] = cr
    main_doi = None
    if main:
        for doi, c in cr.items():
            vol_ok = str(c.get('volume') or '').lstrip('0') == str(main.get('journal_volume') or '').lstrip('0')
            if main.get('journal_title') == 'JHEP':
                vol_ok = str(c.get('volume')) == str(main.get('year')) and (('(%s)' % main.get('year')) in doi or ('/%s/' % main.get('year')) in doi)
            fp = first_page(c.get('page')) or c.get('artno')
            pg_ok = str(fp or '').lstrip('0') == str(main.get('page_start') or main.get('artid') or '').lstrip('0')
            if vol_ok and pg_ok:
                main_doi = doi
        if cr and not main_doi:
            rep['issues'].append('no Crossref DOI matches main vol/page: ' + '; '.join('%s v%s p%s' % (k, c.get('volume'), c.get('page') or c.get('artno')) for k, c in cr.items()))
    elif len(cr) == 1:
        main_doi = list(cr)[0]
    rep['main_doi'] = main_doi
    rep['erratum_dois'] = [k for k in cr if k != main_doi]
    if main_doi:
        c = cr[main_doi]
        r = difflib.SequenceMatcher(None, norm_title(rep['title']), norm_title(c['title'] + (' ' + c['subtitle'] if c['subtitle'] else ''))).ratio()
        rep['title_ratio_crossref'] = round(r, 3)
        if r < 0.9:
            rep['issues'].append('TITLE differs (ratio %.2f): INSPIRE "%s" | Crossref "%s"' % (r, rep['title'], c['title']))
        cfam = [surname_key(a[1]) for a in c['authors']]
        if cfam and sn:
            if len(sn) <= 12 and set(cfam) != set(sn):
                rep['issues'].append('AUTHORS differ: INSPIRE %s | Crossref %s' % (sn, cfam))
        elif not cfam:
            rep['notes'].append('Crossref has no authors')
        cy = c.get('pprint') or c.get('issued')
        if yr and cy and int(cy) != int(yr):
            rep['issues'].append('YEAR INSPIRE %s vs Crossref print/issued %s (online %s)' % (yr, cy, c.get('ponline')))
        if c.get('page') and '-' in str(c['page']):
            rep['page_range_crossref'] = c['page']
    # --- arXiv cross-check
    for aid, cats in rep['arxiv'][:1]:
        a = ARX.get(aid)
        if not a:
            rep['issues'].append('arXiv record missing for %s' % aid)
            continue
        r = difflib.SequenceMatcher(None, norm_title(rep['title']), norm_title(a['title'])).ratio()
        rep['title_ratio_arxiv'] = round(r, 3)
        if r < 0.85:
            rep['notes'].append('arXiv title differs (ratio %.2f): "%s"' % (r, a['title']))
        asn = [surname_key(n.split()[-1]) for n in a['authors']]
        if sn and len(sn) <= 12 and set(asn) != set(sn):
            # surname extraction from 'First Last' is crude; only report clear mismatches
            miss = [s for s in sn if not any(s in x or x in s for x in asn)]
            if miss:
                rep['notes'].append('arXiv authors %s vs INSPIRE %s' % (a['authors'], sn))
        rep['arxiv_meta'] = a
    if rep['issues']:
        nwarn += 1
    results[key] = rep

json.dump(results, open(out_json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for key, rep in results.items():
    flag = 'WARN' if rep['issues'] else 'ok  '
    main = rep.get('main') or {}
    line = '%s %-32s %-8s %s %s %s (%s) doi=%s arx=%s tk=%s' % (flag, key, rep.get('recid'), main.get('journal_title'), main.get('journal_volume'),
                                                              main.get('page_start') or main.get('artid'), main.get('year'), rep.get('main_doi'),
                                                              rep['arxiv'][0][0] if rep.get('arxiv') else None, (rep.get('texkeys') or [None])[0])
    print(line)
    for i in rep['issues']:
        print('      ISSUE:', i)
    if verbose:
        for i in rep['notes']:
            print('      note:', i)
print('entries', len(results), 'with issues', nwarn)
