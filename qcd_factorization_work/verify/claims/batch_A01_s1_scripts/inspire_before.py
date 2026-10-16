# INSPIRE search with local cutoff on earliest_date (YYYY-MM-DD); prints all hits before the cutoff.
# Usage: python3 -I inspire_before.py "<query>" <cutoff> [maxhits]
import json, sys, urllib.parse, urllib.request
q, cutoff = sys.argv[1], sys.argv[2]
maxhits = int(sys.argv[3]) if len(sys.argv) > 3 else 500
out, page, total = [], 1, None
while True:
    url = ('https://inspirehep.net/api/literature?' + urllib.parse.urlencode({
        'q': q, 'size': 250, 'page': page, 'sort': 'mostrecent',
        'fields': 'titles.title,authors.full_name,arxiv_eprints.value,texkeys,earliest_date,citation_count,publication_info.pubinfo_freetext,publication_info.journal_title,publication_info.journal_volume,publication_info.year'}))
    req = urllib.request.Request(url, headers={'User-Agent': 'verification-script'})
    d = json.load(urllib.request.urlopen(req, timeout=90))
    total = d['hits']['total']
    hits = d['hits']['hits']
    out += hits
    if len(hits) < 250 or len(out) >= maxhits or len(out) >= total:
        break
    page += 1
sel = [h for h in out if h['metadata'].get('earliest_date', '9999') < cutoff]
print(f'QUERY: {q} | total = {total} | fetched {len(out)} | before {cutoff}: {len(sel)}')
for h in sorted(sel, key=lambda h: h['metadata'].get('earliest_date', '')):
    m = h['metadata']
    au = [a['full_name'] for a in m.get('authors', [])]
    aus = '; '.join(au[:3]) + (' et al.' if len(au) > 3 else '')
    ax = m.get('arxiv_eprints', [{}])[0].get('value', '-')
    pi = m.get('publication_info', [{}])
    p = pi[0] if pi else {}
    pub = p.get('pubinfo_freetext') or ' '.join(str(p.get(k, '')) for k in ['journal_title', 'journal_volume', 'year'])
    print(f"{m.get('earliest_date','?')} | {ax} | {m.get('texkeys',['?'])[0]} | cit {m.get('citation_count',0)} | {aus} | {m['titles'][0]['title'][:150]} | {pub}")
