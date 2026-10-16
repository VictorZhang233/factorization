# Generic INSPIRE literature search helper.
# Usage: python3 -I inspire_search.py "<query>" [size] [sort]
import json, sys, urllib.parse, urllib.request
q = sys.argv[1]
size = sys.argv[2] if len(sys.argv) > 2 else '25'
sort = sys.argv[3] if len(sys.argv) > 3 else 'mostcited'
url = ('https://inspirehep.net/api/literature?' + urllib.parse.urlencode({
    'q': q, 'size': size, 'sort': sort,
    'fields': 'titles.title,authors.full_name,arxiv_eprints.value,texkeys,earliest_date,citation_count,publication_info.pubinfo_freetext,publication_info.journal_title,publication_info.journal_volume,publication_info.year,publication_info.artid,publication_info.page_start'}))
req = urllib.request.Request(url, headers={'User-Agent': 'verification-script'})
d = json.load(urllib.request.urlopen(req, timeout=60))
print('QUERY:', q, '| total =', d['hits']['total'])
for h in d['hits']['hits']:
    m = h['metadata']
    au = [a['full_name'] for a in m.get('authors', [])]
    aus = '; '.join(au[:4]) + (' et al.' if len(au) > 4 else '')
    ax = m.get('arxiv_eprints', [{}])[0].get('value', '-')
    pi = m.get('publication_info', [{}])
    pub = ''
    if pi:
        p = pi[0]
        pub = p.get('pubinfo_freetext') or ' '.join(str(p.get(k, '')) for k in ['journal_title', 'journal_volume', 'year', 'artid', 'page_start'])
    print(f"{m.get('earliest_date','?')} | {ax} | {m.get('texkeys',['?'])[0]} | cit {m.get('citation_count',0)} | {aus} | {m['titles'][0]['title'][:140]} | {pub}")
