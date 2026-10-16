# Round-3 reviewer 2: verify bibliographic data (and abstracts) of references used by the X1 report (fix round 2).
import json, sys, urllib.parse, urllib.request, time
def q(query, size=3, abstract=False):
    fields = 'titles.title,authors.full_name,arxiv_eprints.value,earliest_date,publication_info,citation_count'
    if abstract: fields += ',abstracts.value'
    url = 'https://inspirehep.net/api/literature?' + urllib.parse.urlencode({'q': query, 'size': size, 'fields': fields})
    req = urllib.request.Request(url, headers={'User-Agent': 'x1-review-r3-2'})
    for attempt in range(3):
        try:
            return json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:
            err = e; time.sleep(2)
    return {'error': str(err)}
def show(label, query, abstract=False, size=2):
    d = q(query, size, abstract)
    print('=' * 100); print(label, '| QUERY:', query)
    if 'error' in d: print('  ERROR', d['error']); return
    print('  total hits:', d['hits']['total'])
    for h in d['hits']['hits']:
        m = h['metadata']
        au = [a['full_name'] for a in m.get('authors', [])]
        pis = m.get('publication_info', [])
        pub = '; '.join(' '.join(str(p.get(k, '')) for k in ('journal_title', 'journal_volume', 'year', 'artid', 'page_start')).strip() for p in pis)
        ax = (m.get('arxiv_eprints') or [{}])[0].get('value', '-')
        print('  -', m.get('earliest_date'), '| arXiv', ax, '| cit', m.get('citation_count'), '|', '; '.join(au[:6]), '|', m['titles'][0]['title'], '|', pub)
        if abstract:
            for a in m.get('abstracts', [])[:1]:
                print('    ABSTRACT:', a['value'][:1500])
refs = [
 ('Lindsay 1984 NPB 231 397', 'j Nucl.Phys.B,231,397', True),
 ('Brandt-Frenkel-Taylor 1989 NPB 312 589', 'j Nucl.Phys.B,312,589', True),
 ('LRS PLB 117 105', 'j Phys.Lett.B,117,105', True),
 ('LRS NPB 214 61', 'j Nucl.Phys.B,214,61', True),
 ('LRS NPB 222 189', 'j Nucl.Phys.B,222,189', True),
 ('Doria-Frenkel-Taylor NPB 168 93', 'j Nucl.Phys.B,168,93', False),
 ('Di Lieto et al NPB 183 223', 'j Nucl.Phys.B,183,223', False),
 ('Andrasi et al NPB 182 104', 'j Nucl.Phys.B,182,104', False),
 ('Landshoff-Stirling ZPC 14 251', 'j Z.Phys.C,14,251', True),
 ('Nelson NPB 223 366', 'j Nucl.Phys.B,223,366', False),
 ('Brandt ZPC 45 287', 'j Z.Phys.C,45,287', False),
 ('Zhou-Yan-Zhang-Li CTP 74 115202', 'j Commun.Theor.Phys.,74,115202', True),
 ('arXiv:1708.01743', 'arxiv:1708.01743', False),
 ('Forshaw-Kyrieleis-Seymour JHEP 0608 059', 'arxiv:hep-ph/0604094', False),
 ('Forshaw-Seymour-Siodmok 1206.6363', 'arxiv:1206.6363', False),
 ('Catani-de Florian-Rodrigo 1112.4405', 'arxiv:1112.4405', False),
 ('Becher et al 2408.10308', 'arxiv:2408.10308', True),
 ('Boer et al 1709.04935', 'arxiv:1709.04935', True),
 ('Buffing-Mulders 1309.4681', 'arxiv:1309.4681', False),
 ('Chang-Li 1305.4694', 'arxiv:1305.4694', True),
 ('Li 2201.10901', 'arxiv:2201.10901', True),
 ('Aybat-Sterman 0811.0246', 'arxiv:0811.0246', True),
 ('Collins 2002 hep-ph/0204004', 'arxiv:hep-ph/0204004', False),
 ('Collins-Metz hep-ph/0408249', 'arxiv:hep-ph/0408249', False),
 ('Collins-Qiu 0705.2141', 'arxiv:0705.2141', True),
 ('Collins 0708.4410', 'arxiv:0708.4410', False),
 ('DGOPS 1510.08696', 'arxiv:1510.08696', False),
 ('Schwartz-Yan-Zhu 1801.01138?', 'j Phys.Rev.D,97,096017', False),
 ('Rothstein-Stewart 1601.04695', 'arxiv:1601.04695', False),
 ('Sterman-Erdogan EPJ ST 235 1493', 't Glauber and a Erdogan and a Sterman', False),
 ('Sterman-Erdogan alt', 'a Sterman and a Erdogan and date > 2024', False),
 ('Liu-Ma 0802.2973', 'arxiv:0802.2973', False),
 ('Gaunt 2014 1405.2080', 'arxiv:1405.2080', False),
 ('Angeles-Martinez-Forshaw-Seymour 1510.07998', 'arxiv:1510.07998', False),
 ('Del Duca hep-ph/9503226', 'arxiv:hep-ph/9503226', False),
 ('Bodwin PRD 31 2616', 'j Phys.Rev.D,31,2616', False),
 ('BBL PRL 47 1799', 'j Phys.Rev.Lett.,47,1799', False),
]
for lab, qq, ab in refs:
    show(lab, qq, ab)
    time.sleep(0.4)
