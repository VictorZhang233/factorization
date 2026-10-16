import json, urllib.parse, urllib.request, time
def get(q, size=50, fields='titles.title,authors.full_name,arxiv_eprints.value,earliest_date,control_number'):
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': q, 'size': size, 'sort': 'mostrecent', 'fields': fields})
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'x1-review-r3-2'}), timeout=60))
for ax in ['1510.08696', '0811.0246', '1601.04695']:
    rec = get('arxiv:' + ax, 1)['hits']['hits'][0]['metadata']['control_number']
    for extra in ['t glauber', 't spectator', 't "drell-yan" and t factorization']:
        q = f'refersto:recid:{rec} and {extra}'
        d = get(q)
        print('=' * 90); print(f'citers of arXiv:{ax} (recid {rec}) with [{extra}]: total {d["hits"]["total"]}')
        for h in d['hits']['hits'][:40]:
            m = h['metadata']; au = [a['full_name'] for a in m.get('authors', [])]
            axx = (m.get('arxiv_eprints') or [{}])[0].get('value', '-')
            print(' ', m.get('earliest_date'), axx, '|', '; '.join(au[:3]) + (' et al.' if len(au) > 3 else ''), '|', m['titles'][0]['title'][:110])
        time.sleep(0.5)
