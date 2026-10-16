"""Fetch INSPIRE, Crossref and arXiv metadata for every spec entry.
usage: python3 -I fetch.py SPEC_PY DL_DIR [--only key1,key2] [--refresh]
Raw responses are saved under DL_DIR/{inspire,crossref,arxiv}; nothing is executed from DL_DIR."""
import sys, os, json, time, re, urllib.request, urllib.parse, urllib.error

spec_path, dl = sys.argv[1], sys.argv[2]
only = None
refresh = '--refresh' in sys.argv
if '--only' in sys.argv:
    only = set(sys.argv[sys.argv.index('--only') + 1].split(','))
ns = {}
exec(open(spec_path, encoding='utf-8').read(), ns)
S = ns['S']
for sub in ('inspire', 'crossref', 'arxiv'):
    os.makedirs(os.path.join(dl, sub), exist_ok=True)

UA = 'qcd-monograph-bibliography-check/1.0 (python urllib)'
FIELDS = ','.join(['titles', 'authors.full_name', 'collaborations', 'corporate_author', 'publication_info', 'dois',
                   'arxiv_eprints', 'texkeys', 'document_type', 'control_number', 'imprints', 'isbns',
                   'book_series', 'report_numbers', 'number_of_pages', 'editions'])

def get(url, tries=4, pause=2.0):
    last = None
    for t in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as ex:
            last = ex
            if ex.code == 404:
                return None
            time.sleep(pause * (t + 1))
        except Exception as ex:  # network hiccup
            last = ex
            time.sleep(pause * (t + 1))
    print('  FAILED', url, last, file=sys.stderr)
    return None

def safe(s):
    return re.sub(r'[^A-Za-z0-9._-]', '_', s)

# 1. INSPIRE
n = 0
for e in S:
    if only and e['key'] not in only:
        continue
    out = os.path.join(dl, 'inspire', e['key'] + '.json')
    if os.path.exists(out) and not refresh:
        continue
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': e['q'], 'size': 5, 'fields': FIELDS})
    b = get(url)
    if b is None:
        print('INSPIRE fail', e['key'])
        continue
    with open(out, 'wb') as f:
        f.write(b)
    n += 1
    time.sleep(0.45)
print('inspire fetched', n)

# 2. Crossref for every DOI in the INSPIRE hits
dois = set()
for e in S:
    if only and e['key'] not in only:
        continue
    p = os.path.join(dl, 'inspire', e['key'] + '.json')
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding='utf-8'))
    for h in d['hits']['hits'][:3]:
        for x in h['metadata'].get('dois', []) or []:
            dois.add(x['value'].lower())
for x in ns.get('EXTRA_DOIS', []):
    dois.add(x.lower())
n = 0
for doi in sorted(dois):
    out = os.path.join(dl, 'crossref', safe(doi) + '.json')
    if os.path.exists(out) and not refresh:
        continue
    b = get('https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/()._-;'))
    if b is None:
        print('Crossref fail', doi)
        with open(out, 'w') as f:
            f.write('{"status":"notfound"}')
        continue
    with open(out, 'wb') as f:
        f.write(b)
    n += 1
    time.sleep(0.25)
print('crossref fetched', n, 'of', len(dois))

# 3. arXiv metadata (batch)
ids = set()
for e in S:
    if only and e['key'] not in only:
        continue
    p = os.path.join(dl, 'inspire', e['key'] + '.json')
    if not os.path.exists(p):
        continue
    d = json.load(open(p, encoding='utf-8'))
    for h in d['hits']['hits'][:1]:
        for x in h['metadata'].get('arxiv_eprints', []) or []:
            ids.add(x['value'])
ids = sorted(ids)
have = set()
for fn in os.listdir(os.path.join(dl, 'arxiv')):
    if fn.endswith('.ids'):
        have |= set(open(os.path.join(dl, 'arxiv', fn)).read().split())
need = [i for i in ids if i not in have] if not refresh else ids
k = len([fn for fn in os.listdir(os.path.join(dl, 'arxiv')) if fn.endswith('.xml')])
for i in range(0, len(need), 40):
    chunk = need[i:i + 40]
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': ','.join(chunk), 'max_results': len(chunk) + 5})
    b = get(url, pause=5.0)
    if b is None:
        print('arXiv fail chunk', i)
        continue
    with open(os.path.join(dl, 'arxiv', 'batch%03d.xml' % k), 'wb') as f:
        f.write(b)
    with open(os.path.join(dl, 'arxiv', 'batch%03d.ids' % k), 'w') as f:
        f.write('\n'.join(chunk))
    k += 1
    time.sleep(3.5)
print('arxiv ids', len(ids), 'newly fetched', len(need))
