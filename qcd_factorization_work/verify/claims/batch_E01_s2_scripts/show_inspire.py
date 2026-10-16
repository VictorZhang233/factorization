import json, sys, glob, os
d = sys.argv[1]
for f in sorted(glob.glob(os.path.join(d, '*.json'))):
    j = json.load(open(f))
    for h in j['hits']['hits']:
        m = h['metadata']
        t = m.get('titles', [{}])[0].get('title')
        ax = [e.get('value') for e in m.get('arxiv_eprints', [])]
        pi = [(p.get('journal_title'), p.get('journal_volume'), p.get('artid') or p.get('page_start'), p.get('year'), p.get('material')) for p in m.get('publication_info', [])]
        doi = [x.get('value') for x in m.get('dois', [])]
        au = [a['full_name'] for a in m.get('authors', [])][:8]
        print(os.path.basename(f), '|', m.get('control_number'), '|', t)
        print('   arXiv', ax, 'pub', pi, 'doi', doi)
        print('   authors', au)
