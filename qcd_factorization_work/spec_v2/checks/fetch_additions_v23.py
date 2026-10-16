"""Spec v2.3 (verify patch) supplement: INSPIRE-HEP records for the bibliography additions of the verify patch.
Usage: python3 -I fetch_additions_v23.py OUTDIR      (OUTDIR = spec_v2/checks/inspire_additions)

Why these: (1) the 14 items named by the spec patch task (S60 leftovers cited as 「文献待补」 in FINAL_OUTLINE_v2 /
ASSUMPTIONS, the E01 first correction Chou-Chen, the BHNS 2026 Glauber paper, Joglekar 1977, Nakanishi-Ojima);
(2) sources cited by the final App M/N/O/Q text of the patch (verify/extend_reports/X1-X3 final reports and
verify/CLAIM_VERDICTS.md: N01, N04, A06, S63-7).  One INSPIRE record per query is required (total == 1); items with
0 or >1 hits are reported and resolved by hand (Crossref, see crossref_additions_v23.py) or dropped.
Same storage format as fetch_additions.py: OUTDIR/<tag>.bib (INSPIRE BibTeX verbatim) and OUTDIR/<tag>.json.
"""
import sys, json, urllib.request, urllib.parse, time, os
OUT = sys.argv[1]
Q = [
 # --- task list (f)
 ('Gribov1978', 'j Nucl.Phys.B,139,1', 'Ch2 qcd: Gribov copies'),
 ('LeeZinnJustin1972a', 'j Phys.Rev.D,5,3121', 'Ch2 qcd: renormalizability, Lee-Zinn-Justin I'),
 ('LeeZinnJustin1972b', 'j Phys.Rev.D,5,3137', 'Ch2 qcd: renormalizability, Lee-Zinn-Justin II'),
 ('LeeZinnJustin1972c', 'j Phys.Rev.D,5,3155', 'Ch2 qcd: renormalizability, Lee-Zinn-Justin III'),
 ('ZinnJustin1975', 'j Lect.Notes Phys.,37,1', 'Ch2 qcd: Zinn-Justin equation'),
 ('AppelquistCarazzone1975', 'j Phys.Rev.D,11,2856', 'Ch2 qcd: decoupling'),
 ('Vladimirov1979', 't "generalized functions in mathematical physics" and a Vladimirov', 'App M: Laplace transforms in tubes'),
 ('Hormander', 't "analysis of linear partial differential operators"', 'App M, Ch22: Paley-Wiener-Schwartz, almost-analytic extensions'),
 ('BergereDeCalanMalbouisson1978', 'j Commun.Math.Phys.,62,137', 'App M, App N: asymptotic expansion of Feynman amplitudes'),
 ('Balaban1987', 'j Commun.Math.Phys.,109,249', 'App M: UV stability of lattice YM (RG approach I)'),
 ('Balaban1988', 'j Commun.Math.Phys.,116,1', 'App M: UV stability of lattice YM (RG approach II) -- 0 hits on INSPIRE (2026-10-11), not added'),
 ('Balaban1989', 'j Commun.Math.Phys.,122,355', 'App M: UV stability of lattice YM (large field renormalization II)'),
 ('MagnenRivasseauSeneor1993', 'j Commun.Math.Phys.,155,325', 'App M: YM4 with an infrared cutoff'),
 ('SchoonderwoerdBakker1998a', 'j Phys.Rev.D,57,4965', 'App O / ASSUMPTIONS asm:appO-lcopt: covariant vs light-front PT I'),
 ('SchoonderwoerdBakker1998b', 'j Phys.Rev.D,58,025013', 'App O / ASSUMPTIONS asm:appO-lcopt: covariant vs light-front PT II'),
 ('ChouChen2022', 'j Phys.Rev.D,106,014507', 'App Q E01: first published correction of the hybrid kernel'),
 ('BecherHagerNeubertSchwienbacher2026', 'eprint 2603.12383', 'Ch18 front: qg->q coherence violation confirmed in SCET'),
 ('NakanishiOjima1990', 't "covariant operator formalism of gauge theories"', 'Ch24 front: BRST classification as cited by Collins 2011 11.3.2 (6 hits; resolved by the next query)'),
 ('NakanishiOjima1990b', 'j World Sci.Lect.Notes Phys.,27', 'Ch24 front: Nakanishi-Ojima, World Sci. Lect. Notes Phys. 27 (1990)'),
 ('Joglekar1977a', 'j Annals Phys.,108,233', 'Joglekar 1977 I: confirm that the bib key Joglekar:1976eb is this record (no addition)'),
 ('Joglekar1977b', 'j Annals Phys.,109,210', 'Joglekar 1977 II: confirm that the bib key Joglekar:1976pe is this record (no addition)'),
 # --- cited by the final App M/N/O text and the claim sweep
 ('Meggiolaro1997', 'eprint hep-th/9602104', 'N01 / App O: eikonal amplitudes at O(g^4)'),
 ('GiordanoMeggiolaro2006', 'eprint hep-ph/0602143', 'N01 / App O: eikonal amplitudes, colour structure'),
 ('ChengEtAl2025', 'eprint 2410.05141', 'A06: N3LO quasi-PDF matching kernel'),
 ('JLSZ2025', 'j JHEP,2503,045', 'A06: Ji-Liu-Su-Zhang JHEP 03 (2025) 045 (check against Ji:2024hit)'),
 ('Radyushkin2019', 'j Phys.Lett.B,788,380', 'A06: reply to Rossi-Testa'),
 ('Lindsay1984', 'j Nucl.Phys.B,231,397', 'App O: two-loop spectator calculation'),
 ('BelitskySmirnov2026', 'eprint 2505.22595', 'App N: off-shell form factor, factorization violated'),
 ('BelitskyBorkSmirnov2025', 'eprint 2409.05945', 'App N: Pinching Sudakov'),
 ('JackiwTempleton1981', 'j Phys.Rev.D,23,2291', 'App N: IR of super-renormalizable theories (phi^3_6 regulator remark)'),
 ('Borinsky2023', 'eprint 2008.12310', 'App M/N: tropical Monte Carlo, Newton polytopes'),
 ('Schultka2018', 'eprint 1806.01086', 'App M: Newton polytopes of Feynman integrals'),
 ('LNvRV1997', 'j Nucl.Phys.B,492,338', 'App M: forward expansion check'),
 ('BMMS2019', 'eprint 1901.06172', 'N04: light-ray operators as generating functions (prior art)'),
 ('Barcaro2026', 'eprint 2607.14259', 'App O: Glauber literature comparison'),
 ('ZhouEtAl2022', 'eprint 1708.01743', 'App O: all-order argument literature'),
 ('LiuMa2008', 'eprint 0802.2973', 'App O: all-order argument literature'),
 ('ScimemiVladimirov2017', 'eprint 1609.06047', 'S63-7: small-b power corrections b^2'),
 ('MoosVladimirov2020', 'eprint 2008.01744', 'S63-7: small-b power corrections b^2'),
 ('ArkaniHamedHillmanMizera2022', 'eprint 2202.12296', 'App N: tropical geometry of divergences'),
 ('FeichtnerSturmfels2005', 'eprint math/0411260', 'App M: matroid polytopes / nested sets (NE lemma check)'),
 ('NilssonPassare2013', 'eprint 1010.5060', 'App M open problem O12: Mellin transforms of rational functions'),
 ('Henneaux1996', 'j Phys.Lett.B,367,163', 'App M lem:appM-lbc-formal: local BRST cohomology (X3 K6, checked)'),
 ('BHHS2000', 'j Phys.Lett.B,492,376', 'App M lem:appM-lbc-formal: local BRST cohomology (X3 K6, checked)'),
 ('HerrlichNierste1995', 'j Nucl.Phys.B,455,39', 'App M lem:appM-ne(iii): evanescent operators (X3 K12, abstract)'),
 ('ChangLi2013', 'eprint 1305.4694', 'App O rem:appO-literature-comparison: dissenting Glauber-phase proposal (X1 sec. 11)'),
 ('Li2022', 'eprint 2201.10901', 'App O rem:appO-literature-comparison: dissenting Glauber-phase proposal (X1 sec. 11)'),
 ('LRS1983', 'j Nucl.Phys.B,222,189', 'App O lem:appO-halfcoinc-colour: colour-singlet-target mechanism (Lindsay-Ross-Sachrajda)'),
 ('BoerEtAl2017', 'eprint 1709.04935', 'App O rem:appO-literature-comparison: double Boer-Mulders model check (X1 sec. 11)'),
 ('AybatCollinsQiuRogers2012', 'j Phys.Rev.D,85,034043', 'App Q E17: the factor-free zeta normalization used by the same authors (claim E17 literature check)'),
 ('BhattacharyaCocuzzaMetz2020', 'eprint 1903.05721', 'Ch22 prop:lamet-tmc: P^z-independence of the first two gamma^0 moments (claim N07 literature check)'),
 ('MonahanNeumann2026', 'eprint 2609.40205', 'Ch22 lem:lamet-strip, prop:lamet-slepian: classical results applied to quasi-PDFs (claim N10 literature check)'),
 ('BuffingMulders2011', 'eprint 1105.4804', 'Ch18 prop:break-colour: attachment rule in Wilson-line form (claim N18 literature check)'),
 ('BalitskyChirilli2009', 'eprint 0903.5326', 'Ch24 prop:front-nlo-bk: the zeta(3) mismatch withdrawn by its authors (claim E34(iii) literature check)'),
]
def get(url):
    for k in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return r.read().decode('utf-8')
        except Exception as e:
            time.sleep(2 + 2 * k)
    raise RuntimeError('failed ' + url)
only = sys.argv[2:]
for tag, q, why in Q:
    if only and tag not in only:
        continue
    base = 'https://inspirehep.net/api/literature?q=' + urllib.parse.quote(q) + '&size=5'
    meta = json.loads(get(base + '&fields=texkeys,titles,authors.full_name,publication_info,arxiv_eprints,dois,document_type,imprints,isbns'))
    hits = meta['hits']['hits']; n = meta['hits']['total']
    rec = {'tag': tag, 'query': q, 'purpose': why, 'total': n}
    if n >= 1:
        rec['candidates'] = []
        for hh in hits:
            h = hh['metadata']
            rec['candidates'].append({'texkey': (h.get('texkeys') or [''])[0], 'title': (h.get('titles') or [{}])[0].get('title'),
                                      'authors': [a.get('full_name') for a in (h.get('authors') or [])][:6],
                                      'pubinfo': h.get('publication_info'), 'doc': h.get('document_type'), 'imprints': h.get('imprints'),
                                      'isbns': h.get('isbns'), 'dois': h.get('dois'), 'eprints': h.get('arxiv_eprints')})
    if n == 1:
        h = hits[0]['metadata']
        rec['texkey'] = (h.get('texkeys') or [''])[0]
        rec['title'] = (h.get('titles') or [{}])[0].get('title')
        rec['authors'] = [a.get('full_name') for a in (h.get('authors') or [])]
        rec['pubinfo'] = h.get('publication_info')
        rec['dois'] = h.get('dois')
        rec['eprints'] = h.get('arxiv_eprints')
        bib = get(base + '&format=bibtex')
        rec['nbib'] = bib.count('@')
        open(os.path.join(OUT, tag + '.bib'), 'w', encoding='utf-8').write(bib)
    json.dump(rec, open(os.path.join(OUT, tag + '.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(tag, '| hits', n, '|', rec.get('texkey'), '|', (rec.get('authors') or [])[:5], '|', (rec.get('title') or '')[:90], '|',
          [(p.get('journal_title'), p.get('journal_volume'), p.get('page_start') or p.get('artid'), p.get('year'))
           for p in (rec.get('pubinfo') or [])][:2], '|', rec.get('eprints'), '|', [d.get('value') for d in (rec.get('dois') or [])][:2])
    if n > 1:
        for c in rec['candidates']:
            print('     cand:', c['texkey'], '|', c['authors'][:3], '|', (c['title'] or '')[:80], '|', c['doc'], '|', c['imprints'], '|', [(p.get('journal_title'), p.get('journal_volume'), p.get('year')) for p in (c['pubinfo'] or [])][:2])
    time.sleep(0.4)
