"""Spec v2.1 supplement to fetch_additions.py: three more INSPIRE-HEP records (one record per query).
Usage: python3 -I fetch_additions_v21.py OUTDIR      (OUTDIR = spec_v2/checks/inspire_additions)

Why these: verify/CLAIMS.md E34(iv) and frontier/others/OTHERS.md Sec. 9.5 report that the small-x helicity
results of Borden-Kovchegov (Borden:2023ugd, Borden:2025ehe; both already in the bib) disagree with
Bartels-Ermolaev-Ryskin from four loops on and slightly with Bluemlein-Vogt.  CLAIMS E34 says the BER reference
is 'to be added and verified'.  The identity of the papers was fixed from the INSPIRE reference list of
Borden:2025ehe (PRD 113 (2026) 034002), which cites exactly: BER Z.Phys.C 70 (1996) 273, BER Z.Phys.C 72 (1996)
627, Bluemlein-Vogt Phys.Lett.B 386 (1996) 350 and Phys.Lett.B 370 (1996) 149.  The singlet papers carry the
quoted intercepts; the non-singlet BER paper is added because BER is cited as a pair.  Bluemlein-Vogt PLB 370
(non-singlet) is not added (not needed for any statement in our material).
Same storage format as fetch_additions.py: OUTDIR/<tag>.bib (INSPIRE BibTeX verbatim) and OUTDIR/<tag>.json.
"""
import sys, json, urllib.request, urllib.parse, time, os
OUT = sys.argv[1]
Q = [
 ('BartelsErmolaevRyskin1996a', 'j Z.Phys.C,70,273', 'Ch24 front (small-x helicity, CLAIMS E34(iv)): BER non-singlet g1 at small x'),
 ('BartelsErmolaevRyskin1996b', 'j Z.Phys.C,72,627', 'Ch24 front (small-x helicity, CLAIMS E34(iv)): BER singlet g1 at small x; intercept quoted in OTHERS 9.5'),
 ('BlumleinVogt1996', 'j Phys.Lett.B,386,350', 'Ch24 front (small-x helicity): Bluemlein-Vogt singlet g1 at small x (cited by Borden:2025ehe)'),
]
def get(url):
    for k in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return r.read().decode('utf-8')
        except Exception as e:
            time.sleep(2 + 2 * k)
    raise RuntimeError('failed ' + url)
for tag, q, why in Q:
    base = 'https://inspirehep.net/api/literature?q=' + urllib.parse.quote(q) + '&size=5'
    meta = json.loads(get(base + '&fields=texkeys,titles,authors.full_name,publication_info,arxiv_eprints,dois,document_type'))
    hits = meta['hits']['hits']; n = meta['hits']['total']
    rec = {'tag': tag, 'query': q, 'purpose': why, 'total': n}
    if n == 1:
        h = hits[0]['metadata']
        rec['texkey'] = (h.get('texkeys') or [''])[0]
        rec['title'] = (h.get('titles') or [{}])[0].get('title')
        rec['first_author'] = (h.get('authors') or [{}])[0].get('full_name')
        rec['authors'] = [a.get('full_name') for a in (h.get('authors') or [])]
        rec['pubinfo'] = h.get('publication_info')
        rec['dois'] = h.get('dois')
        rec['eprints'] = h.get('arxiv_eprints')
        bib = get(base + '&format=bibtex')
        rec['nbib'] = bib.count('@')
        open(os.path.join(OUT, tag + '.bib'), 'w', encoding='utf-8').write(bib)
    json.dump(rec, open(os.path.join(OUT, tag + '.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(tag, '| hits', n, '|', rec.get('texkey'), '|', rec.get('authors'), '|', (rec.get('title') or '')[:80], '|',
          [(p.get('journal_title'), p.get('journal_volume'), p.get('page_start') or p.get('artid'), p.get('year'))
           for p in (rec.get('pubinfo') or [])][:2], '|', rec.get('eprints'), '|', rec.get('dois'))
    time.sleep(0.5)
