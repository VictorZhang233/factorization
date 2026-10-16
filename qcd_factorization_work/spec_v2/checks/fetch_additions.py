"""Fetch bibliography additions for spec v2 from INSPIRE-HEP (one record per query).
Usage: python3 -I fetch_additions.py OUTDIR
Each query is a journal reference / eprint / texkey; the script stores the INSPIRE BibTeX
verbatim in OUTDIR/<tag>.bib and the metadata used for verification in OUTDIR/<tag>.json.
"""
import sys, json, urllib.request, urllib.parse, time, os
OUT = sys.argv[1]
Q = [
 # tag, INSPIRE query, purpose
 ('YangMills1954', 'j Phys.Rev.,96,191', 'Ch2 qcd: Yang-Mills gauge theory'),
 ('FaddeevPopov1967', 'j Phys.Lett.B,25,29', 'Ch2 qcd: gauge fixing, ghosts'),
 ('FritzschGellMannLeutwyler1973', 'j Phys.Lett.B,47,365', 'Ch2 qcd: colour octet gluon picture'),
 ('GellMann1964', 'j Phys.Lett.,8,214', 'Ch2 qcd: quark model'),
 ('Zweig1964', 'texkey Zweig:1964jf', 'Ch2 qcd: quark (aces) model'),
 ('HanNambu1965', 'j Phys.Rev.,139,B1006', 'Ch2 qcd: colour'),
 ('Greenberg1964', 'j Phys.Rev.Lett.,13,598', 'Ch2 qcd: parastatistics / colour'),
 ('TarasovVladimirovZharkov1980', 'j Phys.Lett.B,93,429', 'Ch2 qcd: three-loop beta function'),
 ('LarinVermaseren1993', 'j Phys.Lett.B,303,334', 'Ch2 qcd: three-loop beta function (check)'),
 ('vanRitbergenVermaserenLarin1997', 'j Phys.Lett.B,400,379', 'Ch2 qcd: four-loop beta function'),
 ('Czakon2005', 'j Nucl.Phys.B,710,485', 'Ch2 qcd: four-loop beta function (check)'),
 ('BaikovChetyrkinKuhn2017', 'j Phys.Rev.Lett.,118,082002', 'Ch2 qcd: five-loop beta function'),
 ('HerzogEtAl2017', 'j JHEP,1702,090', 'Ch2 qcd: five-loop beta function, general gauge group'),
 ('PDG2024', 'j Phys.Rev.D,110,030001', 'Ch2 qcd: alpha_s(M_Z) world average'),
 ('GellMannLow1954', 'j Phys.Rev.,95,1300', 'Ch2 qcd: renormalization group'),
 ('Callan1970', 'j Phys.Rev.D,2,1541', 'Ch2 qcd: Callan-Symanzik equation'),
 ('Symanzik1970', 'j Commun.Math.Phys.,18,227', 'Ch2 qcd: Callan-Symanzik equation'),
 ('Nielsen1981', 'j Am.J.Phys.,49,1171', 'Ch2 qcd: asymptotic freedom as a spin effect (pedagogical)'),
 ('ItzyksonZuber1980', 'texkey Itzykson:1980rh', 'Ch2 qcd: textbook'),
 ('Wilson1974', 'j Phys.Rev.D,10,2445', 'Ch2/Ch22: lattice gauge theory'),
 ('ChengWu1969', 'j Phys.Rev.Lett.,22,666', 'S60/App O: eikonal high-energy scattering in QED'),
 ('KorchemskayaKorchemsky1995', 'j Nucl.Phys.B,437,127', 'S60/App O: Wilson-loop cross singularities, Regge'),
 ('Korchemsky1994', 'j Phys.Lett.B,325,459', 'S60/App O: near-forward high-energy scattering'),
 ('HambergVanNeerven1992', 'j Nucl.Phys.B,379,143', 'S60/App M: gluon operator renormalization in covariant gauge'),
 ('Bostelmann2005', 'j J.Math.Phys.,46,082304', 'S60/App M: OPE from phase-space properties (AQFT)'),
 ('KogutSoper1970', 'j Phys.Rev.D,1,2901', 'S60/App O: light-front QED'),
 ('ChangYan1973', 'j Phys.Rev.D,7,1147', 'S60/App O: Feynman rules at infinite momentum'),
 ('LigterinkBakker1995', 'j Phys.Rev.D,52,5954', 'S60/App O: equivalence of light-front and covariant PT'),
 ('BrodskyPauliPinsky1998', 'j Phys.Rept.,301,299', 'S60/App O: light-cone quantization review'),
 ('Collins2018LF', 'eprint 1801.03960', 'S60/App O: light-front vacuum'),
 ('AndrasiEtAl1981', 'j Nucl.Phys.B,182,104', 'S60/Ch12: two-loop soft-gluon effects in DY'),
 ('CollinsGambergEtAl2016', 'j Phys.Rev.D,94,034014', 'S60/Ch14: W+Y matching'),
 ('ChayKim2004', 'j Nucl.Phys.B,680,302', 'S60/Ch20: B->pi pi in SCET'),
 ('BenekeBraunKivel1998', 'j Phys.Lett.B,443,308', 'S60/Ch21: O(N) sigma model renormalons'),
 ('David1982', 'j Nucl.Phys.B,209,433', 'S60/Ch21: sigma-model IR renormalons'),
 ('NovikovEtAl1984', 'j Phys.Rept.,116,103', 'S60/Ch21: two-dimensional sigma models'),
 ('FeldmanEtAl1986', 'j Commun.Math.Phys.,103,67', 'S60/Ch21: massive Gross-Neveu model constructed'),
 ('GawedzkiKupiainen1985', 'j Commun.Math.Phys.,102,1', 'S60/Ch21: Gross-Neveu model constructed'),
 ('ChetyrkinGorishnyTkachov1982', 'j Phys.Lett.B,119,407', 'S19/App M: OPE in minimal subtraction'),
 ('Haag1958', 'j Phys.Rev.,112,669', 'App M: Haag-Ruelle scattering'),
 ('Ruelle1962', 'j Helv.Phys.Acta,35,147', 'App M: Haag-Ruelle scattering'),
 ('Jost1965', 't general theory of quantized fields and a Jost', 'App M: axiomatic QFT textbook'),
 ('Epstein1960', 'j J.Math.Phys.,1,524', 'App M: edge-of-the-wedge theorem'),
]
def get(url):
    for k in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return r.read().decode('utf-8')
        except Exception as e:
            time.sleep(2+2*k)
    raise RuntimeError('failed ' + url)
log = []
for tag, q, why in Q:
    base = 'https://inspirehep.net/api/literature?q=' + urllib.parse.quote(q) + '&size=5'
    meta = json.loads(get(base + '&fields=texkeys,titles,authors.full_name,publication_info,arxiv_eprints,dois,document_type'))
    hits = meta['hits']['hits']; n = meta['hits']['total']
    rec = {'tag': tag, 'query': q, 'purpose': why, 'total': n}
    if n >= 1:
        h = hits[0]['metadata']
        rec['texkey'] = (h.get('texkeys') or [''])[0]
        rec['title'] = (h.get('titles') or [{}])[0].get('title')
        rec['first_author'] = (h.get('authors') or [{}])[0].get('full_name')
        rec['pubinfo'] = h.get('publication_info')
        rec['dois'] = h.get('dois')
        rec['eprints'] = h.get('arxiv_eprints')
        bib = get(base + '&format=bibtex')
        rec['nbib'] = bib.count('@')
        open(os.path.join(OUT, tag + '.bib'), 'w', encoding='utf-8').write(bib)
    json.dump(rec, open(os.path.join(OUT, tag + '.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    log.append(rec)
    print(tag, '| hits', n, '|', rec.get('texkey'), '|', (rec.get('first_author') or ''), '|', (rec.get('title') or '')[:70], '|', [(p.get('journal_title'), p.get('journal_volume'), p.get('page_start') or p.get('artid'), p.get('year')) for p in (rec.get('pubinfo') or [])][:2])
    time.sleep(0.4)
