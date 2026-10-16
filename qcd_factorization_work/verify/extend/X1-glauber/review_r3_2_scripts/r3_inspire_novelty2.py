import json, urllib.parse, urllib.request, time
def search(q, size=15):
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': q, 'size': size, 'sort': 'mostrecent',
          'fields': 'titles.title,authors.full_name,arxiv_eprints.value,earliest_date'})
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'x1-review-r3-2'}), timeout=60))
    print('=' * 90); print('QUERY:', q, '| total', d['hits']['total'])
    for h in d['hits']['hits']:
        m = h['metadata']; au = [a['full_name'] for a in m.get('authors', [])]
        ax = (m.get('arxiv_eprints') or [{}])[0].get('value', '-')
        print(' ', m.get('earliest_date'), ax, '|', '; '.join(au[:3]) + (' et al.' if len(au) > 3 else ''), '|', m['titles'][0]['title'][:120])
for q in ['title glauber and title drell-yan', 'title glauber and title factorization and date > 2016',
          'title glauber and title spectator', 'title "spectator interactions"', 'title glauber and title unitarity',
          'title "glauber phase" or title "glauber phases"', 'title glauber and title "two-loop"',
          'refersto:arxiv:1510.08696 and title glauber', 'refersto:arxiv:0811.0246 and date > 2015']:
    search(q); time.sleep(0.5)
