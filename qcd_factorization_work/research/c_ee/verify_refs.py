"""
verify_refs.py -- look up the references used in c_ee that are NOT already in research/refs/refs.bib,
on INSPIRE-HEP (by journal reference / report number) and cross-check the DOI on Crossref.
Usage:  python3 -I verify_refs.py <download_dir>      (raw JSON is written to <download_dir>)
Prints one line per reference: key | authors | title | journal | DOI | crossref-title-match
"""
import sys, json, os, re, urllib.request, urllib.parse, time

REFS = [
    ('ChetyrkinKataevTkachov1979', 'j Phys.Lett.B,85,277'),
    ('DineSapirstein1979', 'j Phys.Rev.Lett.,43,668'),
    ('CelmasterGonsalves1980PRL', 'j Phys.Rev.Lett.,44,560'),
    ('CelmasterGonsalves1980PRD', 'j Phys.Rev.D,21,3112'),
    ('GorishnyKataevLarin1991', 'j Phys.Lett.B,259,144'),
    ('SurguladzeSamuel1991', 'j Phys.Rev.Lett.,66,560'),
    ('BaikovChetyrkinKuhn2008', 'j Phys.Rev.Lett.,101,012002'),
    ('Adler1974', 'j Phys.Rev.D,10,3714'),
    ('ChetyrkinTkachov1981', 'j Nucl.Phys.B,192,159'),
    ('Tkachov1981', 'j Phys.Lett.B,100,65'),
    ('tHooft1973', 'j Nucl.Phys.B,61,455'),
    ('KugoOjima1979', 'j Prog.Theor.Phys.Suppl.,66,1'),
    ('BreitenlohnerMaison1977', 'j Commun.Math.Phys.,52,11'),
    ('BreitenlohnerMaison1977a', 'j Commun.Math.Phys.,52,39'),
    ('BreitenlohnerMaison1977b', 'j Commun.Math.Phys.,52,55'),
    ('LowensteinSpeer1976', 'j Commun.Math.Phys.,47,43'),
    ('Lowenstein1976', 'j Commun.Math.Phys.,47,53'),
    ('EllisRossTerrano1981', 'j Nucl.Phys.B,178,421'),
    ('KataevStarshenko1995', 'j Mod.Phys.Lett.A,10,235'),
    ('KrasnikovPivovarov1982', 'j Phys.Lett.B,116,168'),
    ('tHooftVeltman1972comb', 'j Nucl.Phys.B,50,318'),
    ('ChetyrkinKuhnKwiatkowski1996', 'j Phys.Rept.,277,189'),
    ('Sterman1976', 'j Phys.Rev.D,14,2123'),
    ('StermanWeinberg1977', 'j Phys.Rev.Lett.,39,1436'),
    ('PoggioQuinn1976', 'j Phys.Rev.D,14,578'),
    ('Symanzik1973', 'j Commun.Math.Phys.,34,7'),
    ('Speer1974', 'j Commun.Math.Phys.,37,83'),
    ('KinoshitaUkawa1976', 'j Phys.Rev.D,13,1573'),
    ('Muta_book_check', 'find t "Foundations of quantum chromodynamics" and a Muta'),
    ('Diagrammar1973', 'find r CERN-73-09'),
    ('Radyushkin1982_repub', 'find eprint hep-ph/9907228'),
    ('Gonsalves1983', 'j Phys.Rev.D,28,1542'),
    ('MochVermaserenVogt2005FF', 'j JHEP,0508,049'),
    ('KramerLampe1987', 'j Z.Phys.C,34,497'),
    ('GorishnyKataevLarin1988', 'j Phys.Lett.B,212,238'),
    ('Sterman1979', 'j Phys.Rev.D,19,3135'),
    ('AltarelliEllisMartinelliPi1979', 'j Nucl.Phys.B,160,301'),
    ('FryeEtAl2019', 'j Phys.Rev.D,99,056015'),
    ('AppelquistGeorgi1973', 'j Phys.Rev.D,8,4000'),
    ('Zee1973', 'j Phys.Rev.D,8,4038'),
    ('Kinoshita1962', 'j J.Math.Phys.,3,650'),
    ('LeeNauenberg1964', 'j Phys.Rev.,133,B1549'),
    ('Cutkosky1960', 'j J.Math.Phys.,1,429'),
    ('Veltman1963', 'j Physica,29,186'),
    ('PoggioQuinnWeinberg1976', 'j Phys.Rev.D,13,1958'),
    ('LowensteinZimmermann1975', 'j Commun.Math.Phys.,44,73'),
    ('Sterman1978a', 'j Phys.Rev.D,17,2773'),
    ('Sterman1978b', 'j Phys.Rev.D,17,2789'),
    ('DoriaFrenkelTaylor1980', 'j Nucl.Phys.B,168,93'),
    ('ShifmanVainshteinZakharov1979a', 'j Nucl.Phys.B,147,385'),
]


def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()

API = 'https://inspirehep.net/api/literature?'


def get(url):
    req = urllib.request.Request(url, headers={'Accept': 'application/json', 'User-Agent': 'c_ee-refcheck/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    for key, q in REFS:
        url = API + urllib.parse.urlencode({'q': q, 'size': 3,
                                            'fields': 'titles,authors.full_name,publication_info,dois,texkeys,abstracts,arxiv_eprints,report_numbers'})
        try:
            data = get(url)
        except Exception as e:
            print(f'{key} | ERROR {e}')
            continue
        json.dump(data, open(os.path.join(outdir, key + '.json'), 'w'), indent=1)
        hits = data['hits']['hits']
        n = data['hits']['total']
        if not hits:
            print(f'{key} | NO HIT for {q}')
            continue
        for h in hits[:1]:
            md = h['metadata']
            title = clean(md.get('titles', [{}])[0].get('title', ''))
            au = [a['full_name'] for a in md.get('authors', [])][:5]
            pub = md.get('publication_info', [{}])
            pubs = '; '.join(f"{p.get('journal_title','')} {p.get('journal_volume','')} ({p.get('year','')}) {p.get('artid', p.get('page_start',''))}" for p in pub)
            doi = md.get('dois', [{}])[0].get('value', '') if md.get('dois') else ''
            tk = md.get('texkeys', [''])[0] if md.get('texkeys') else ''
            cr = ''
            if doi:
                try:
                    c = get('https://api.crossref.org/works/' + urllib.parse.quote(doi))
                    ct = clean(c['message'].get('title', [''])[0])
                    cp = c['message'].get('page', '')
                    cr = f'crossref: "{ct}" p.{cp}'
                except Exception as e:
                    cr = f'crossref ERROR {e}'
            print(f'{key} | hits={n} | {tk} | {"; ".join(au)} | {title} | {pubs} | doi:{doi} | {cr}')
        time.sleep(0.4)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/c_ee_refs')
