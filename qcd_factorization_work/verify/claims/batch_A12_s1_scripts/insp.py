import sys, json, urllib.request, urllib.parse
# usage: insp.py "query" [size] [abs]
q = sys.argv[1]; size = sys.argv[2] if len(sys.argv) > 2 else '3'; showabs = len(sys.argv) > 3
url = "https://inspirehep.net/api/literature?" + urllib.parse.urlencode({'q': q, 'size': size, 'fields': 'titles,authors.full_name,publication_info,arxiv_eprints,texkeys,abstracts,dois,documents,urls,collaborations,citation_count'})
req = urllib.request.Request(url, headers={'Accept': 'application/json'})
d = json.load(urllib.request.urlopen(req, timeout=60))
print(f"### query: {q}  (total {d['hits']['total']})")
for h in d['hits']['hits']:
    m = h['metadata']
    au = [a['full_name'] for a in m.get('authors', [])]
    print('recid', h['id'], 'TEXKEY', m.get('texkeys'), 'cites', m.get('citation_count'))
    print('  title:', [t['title'] for t in m.get('titles', [])][:2])
    print('  authors:', au[:8], '...' if len(au) > 8 else '')
    print('  pub:', [(p.get('journal_title'), p.get('journal_volume'), p.get('page_start') or p.get('artid'), p.get('year'), p.get('material'), p.get('pubinfo_freetext')) for p in m.get('publication_info', [])])
    print('  arXiv:', [e['value'] for e in m.get('arxiv_eprints', [])], 'doi:', [x['value'] for x in m.get('dois', [])][:4])
    if showabs:
        for ab in m.get('abstracts', [])[:2]:
            print('  ABS(%s): %s' % (ab.get('source'), ab['value'][:3000]))
