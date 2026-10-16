# Round-3 reviewer 2: abstracts of three possibly related papers surfaced by the citer searches.
import json, urllib.parse, urllib.request
for ax in ['2108.13439', '2108.13440', '2409.16067']:
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': 'arxiv:' + ax, 'size': 1,
          'fields': 'titles.title,authors.full_name,abstracts.value,publication_info'})
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'x1-review-r3-2'}), timeout=60))
    m = d['hits']['hits'][0]['metadata']
    pub = '; '.join(' '.join(str(p.get(k, '')) for k in ('journal_title', 'journal_volume', 'year', 'artid')) for p in m.get('publication_info', []))
    print('==', ax, '|', '; '.join(a['full_name'] for a in m['authors']), '|', m['titles'][0]['title'], '|', pub)
    print('   ', m['abstracts'][0]['value'])
