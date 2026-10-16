# Round-3 reviewer 2: targeted INSPIRE novelty searches for the X1 report's claimed new results.
import json, urllib.parse, urllib.request, time
def search(q, size=12):
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': q, 'size': size, 'sort': 'mostrecent',
          'fields': 'titles.title,authors.full_name,arxiv_eprints.value,earliest_date,citation_count'})
    req = urllib.request.Request(url, headers={'User-Agent': 'x1-review-r3-2'})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=60))
    except Exception as e:
        print('ERROR', q, e); return
    print('=' * 90); print('QUERY:', q, '| total', d['hits']['total'])
    for h in d['hits']['hits']:
        m = h['metadata']; au = [a['full_name'] for a in m.get('authors', [])]
        ax = (m.get('arxiv_eprints') or [{}])[0].get('value', '-')
        print(' ', m.get('earliest_date'), ax, '|', '; '.join(au[:3]) + (' et al.' if len(au) > 3 else ''), '|', m['titles'][0]['title'][:120])
qs = [
 't glauber and t spectator and t drell-yan',
 't glauber and t "time ordering"',
 't glauber and t ordering and t non-abelian and date > 2005',
 't "crossed box" and t glauber',
 't glauber and t "light-cone ordered"',
 't glauber and t unitarity and t spectator',
 't "spectator-spectator"',
 't glauber and t cancellation and date > 2016',
 'fulltext:"ordering weights" and t glauber',
 'fulltext:"spectator-spectator" and fulltext:"crossed box" and date > 2010',
 't "colour entanglement" or t "color entanglement"',
 't "rapidity regulator" and t glauber and date > 2016',
]
for q in qs:
    search(q); time.sleep(0.5)
