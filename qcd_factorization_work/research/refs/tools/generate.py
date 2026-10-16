"""Generate refs.bib, refs_bibitems.tex and NOTES.md from spec + verified analysis.
usage: python3 -I generate.py SPEC_PY ANALYSIS_JSON OUTDIR"""
import sys, os, json, re, unicodedata, datetime

spec_path, ana_path, outdir = sys.argv[1:4]
ns = {}
exec(open(spec_path, encoding='utf-8').read(), ns)
S = ns['S']
R = json.load(open(ana_path, encoding='utf-8'))
NOTE = {e['key']: e['note'] for e in S}
GRP = {e['key']: e['grp'] for e in S}

# ------------------------------------------------------------------ journals
JOURNAL = {  # INSPIRE abbreviation -> (bib form, house-style bibitem form)
    'Phys.Rev.D': ('Phys. Rev. D', 'Phys. Rev.~D'), 'Phys.Rev.Lett.': ('Phys. Rev. Lett.', 'Phys. Rev. Lett.'),
    'Phys.Rev.': ('Phys. Rev.', 'Phys. Rev.'), 'Nucl.Phys.B': ('Nucl. Phys. B', 'Nucl. Phys.~B'),
    'Nucl.Phys.': ('Nucl. Phys.', 'Nucl. Phys.'), 'Phys.Lett.B': ('Phys. Lett. B', 'Phys. Lett.~B'),
    'Z.Phys.C': ('Z. Phys. C', 'Z. Phys.~C'), 'Annals Phys.': ('Ann. Phys. (N.Y.)', 'Ann. Phys. (N.Y.)'),
    'Nuovo Cim.': ('Nuovo Cimento', 'Nuovo Cimento'), 'J.Math.Phys.': ('J. Math. Phys.', 'J. Math. Phys.'),
    'Commun.Math.Phys.': ('Commun. Math. Phys.', 'Commun. Math. Phys.'), 'Physica': ('Physica', 'Physica'),
    'Theor.Math.Phys.': ('Theor. Math. Phys.', 'Theor. Math. Phys.'), 'Teor.Mat.Fiz.': ('Teor. Mat. Fiz.', 'Teor. Mat. Fiz.'),
    'Sov.J.Nucl.Phys.': ('Sov. J. Nucl. Phys.', 'Sov. J. Nucl. Phys.'), 'Yad.Fiz.': ('Yad. Fiz.', 'Yad. Fiz.'),
    'Sov.Phys.JETP': ('Sov. Phys. JETP', 'Sov. Phys. JETP'), 'Zh.Eksp.Teor.Fiz.': ('Zh. Eksp. Teor. Fiz.', 'Zh. Eksp. Teor. Fiz.'),
    'Phys.Rept.': ('Phys. Rep.', 'Phys. Rep.'), 'Rev.Mod.Phys.': ('Rev. Mod. Phys.', 'Rev. Mod. Phys.'),
    'JHEP': ('JHEP', 'JHEP'), 'Eur.Phys.J.C': ('Eur. Phys. J. C', 'Eur. Phys. J.~C'),
    'Fortsch.Phys.': ('Fortschr. Phys.', 'Fortschr. Phys.'), 'Acta Phys.Polon.B': ('Acta Phys. Pol. B', 'Acta Phys. Pol.~B'),
    'Ann.Rev.Nucl.Part.Sci.': ('Annu. Rev. Nucl. Part. Sci.', 'Annu. Rev. Nucl. Part. Sci.'),
    'Acta Math.': ('Acta Math.', 'Acta Math.'),
}

# ------------------------------------------------------------------ author names
CANON = {  # INSPIRE full_name -> canonical "Last, Given" (same person written differently across records)
    'Ji, Xiang-Dong': 'Ji, Xiangdong', 'Ji, Xiang-dong': 'Ji, Xiangdong', 'Ji, X.': 'Ji, Xiangdong',
    'Ma, Jian-ping': 'Ma, Jian-Ping', 'Qiu, Jian-wei': 'Qiu, Jian-Wei', 'Chiu, Jui-yu': 'Chiu, Jui-Yu',
    'Collins, John': 'Collins, John C.', 'Beneke, M.': 'Beneke, Martin', 'Neubert, M.': 'Neubert, Matthias',
    'Diehl, M.': 'Diehl, Markus', 'Catani, S.': 'Catani, Stefano', 'Gross, D.J.': 'Gross, David J.',
    'Lepage, G.P.': 'Lepage, G. Peter', 'Poggio, E.C.': 'Poggio, Enrico C.', 'Seymour, M.H.': 'Seymour, Michael H.',
    'Yuan, F.': 'Yuan, Feng', 'Zimmermann, W.': 'Zimmermann, Wolfhart', 'Belitsky, A.V.': 'Belitsky, Andrei V.',
    # diacritics stripped by INSPIRE but present in the publisher's byline (Crossref)
    'Schafer, Andreas': 'Schäfer, Andreas', 'Siodmok, Andrzej': 'Siódmok, Andrzej',
    'Echevarria, Miguel G.': 'Echevarría, Miguel G.',
}
TEXACC = [('ä', '{\\"a}'), ('ö', '{\\"o}'), ('ü', '{\\"u}'), ('Ü', '{\\"U}'), ('é', "{\\'e}"), ('á', "{\\'a}"),
          ('í', "{\\'\\i}"), ('ó', "{\\'o}"), ('ř', '{\\v{r}}'), ('š', '{\\v{s}}'), ('ç', '{\\c{c}}'), ('ñ', '{\\~n}')]

def to_tex(s):
    for a, b in TEXACC:
        s = s.replace(a, b)
    return s

def fix_given(g):
    g = re.sub(r'\.(?=[A-Za-z])', '. ', g.strip())
    return g

def canon(full):
    full = CANON.get(full, full)
    if ',' not in full:
        return full, ''
    last, given = full.split(',', 1)
    return last.strip(), fix_given(given)

SPECIAL_BIB = {"'t Hooft": "{'t Hooft}", "Di'Lieto": "{Di'Lieto}", 'Llewellyn Smith': '{Llewellyn Smith}'}

def bib_name(full):
    if full == 'Grammer, G., Jr.':
        return 'Grammer, Jr., G.'
    last, given = canon(full)
    last = SPECIAL_BIB.get(last, last)
    return to_tex(last) + (', ' + to_tex(given) if given else '')

def initials(given):
    out = []
    for tok in given.split():
        if tok in ('Jr.', 'Jr'):
            continue
        parts = tok.split('-')
        ini = []
        for p in parts:
            if not p:
                continue
            p = p.rstrip('.')
            ini.append(p[0] + '.')
        out.append('-'.join(ini))
    return '~'.join(out)

def item_name(full):
    if full == 'Grammer, G., Jr.':
        return 'G.~Grammer, Jr.'
    last, given = canon(full)
    last = last.replace("'t Hooft", "'t~Hooft")
    ini = initials(given)
    return (ini + '~' if ini else '') + last

def join_items(names):
    if len(names) == 1:
        return names[0]
    return ', '.join(names[:-1]) + ' and ' + names[-1]

# ------------------------------------------------------------------ titles (LaTeX) where the publisher title needs markup/correction
TITLE = {
    'BjorkenPaschos1969': r'Inelastic Electron-Proton and $\gamma$-Proton Scattering and the Structure of the Nucleon',
    'BogoliubovParasiuk1957': r'{\"U}ber die Multiplikation der Kausalfunktionen in der Quantentheorie der Felder',
    'AppelquistGeorgi1973': r'$e^+e^-$ Annihilation in Gauge Theories of Strong Interactions',
    'CataniEtAl1993': r'Resummation of large logarithms in $e^+e^-$ event shape distributions',
    'HambergVanNeervenMatsuura1991': r'A complete calculation of the order $\alpha_s^2$ correction to the Drell--Yan $K$-factor',
    'CandidoForteHekhorn2020': r'Can $\overline{\mathrm{MS}}$ parton distributions be negative?',
    'Collins2002': r'Leading-twist single-transverse-spin asymmetries: Drell--Yan and deep-inelastic scattering',
    'BecherNeubert2011': r'Drell--Yan production at small $q_T$, transverse parton distributions and the collinear anomaly',
    'CollinsQiu2007': r'$k_T$ factorization is violated in production of high-transverse-momentum particles in hadron-hadron collisions',
    'AffolderEtAl2000': r'Diffractive Dijets with a Leading Antiproton in $\bar{p}p$ Collisions at $\sqrt{s}=1800\,\mathrm{GeV}$',
    'Kovchegov1999': r'Small-$x$ $F_2$ structure function of a nucleus including multiple Pomeron exchanges',
    'IsgurLlewellynSmith1984': r'Asymptotic $Q^2$ for Exclusive Processes in Quantum Chromodynamics',
    'BauerFlemingLuke2000': r'Summing Sudakov logarithms in $B\to X_s\gamma$ in effective field theory',
    'BauerPirjolStewart2001': r'Proof of Factorization for $B\to D\pi$',
    'BecherSchwartz2008': r'A precise determination of $\alpha_s$ from LEP thrust data using effective field theory',
    'BenekeEtAl1999': r'QCD Factorization for $B\to\pi\pi$ Decays: Strong Phases and $CP$ Violation in the Heavy Quark Limit',
    'BenekeEtAl2000': r'QCD factorization for exclusive non-leptonic $B$-meson decays: general arguments and the case of heavy--light final states',
    'BenekeEtAl2001': r'QCD factorization in $B\to\pi K,\pi\pi$ decays and extraction of Wolfenstein parameters',
    'BenekeNeubert2003': r'QCD factorization for $B\to PP$ and $B\to PV$ decays',
    'MaQiu2018': r'Exploring Partonic Structure of Hadrons Using \emph{ab initio} Lattice QCD Calculations',
    'CurciFurmanskiPetronzio1980': r'Evolution of parton densities beyond leading order: The non-singlet case',
    'CollinsSoper1982b': r'Back-to-back jets: Fourier transform from $b$ to $k_T$',
    'EchevarriaIdilbiScimemi2012': r'Factorization theorem for Drell--Yan at low $q_T$ and transverse-momentum distributions on-the-light-cone',
    'QiuSterman1991a': r'Power corrections in hadronic scattering (I). Leading $1/Q^2$ corrections to the Drell--Yan cross section',
    'CataniCiafaloniHautmann1991': r'High energy factorization and small-$x$ heavy flavour production',
    'ShifmanVainshteinZakharov1979a': r'QCD and resonance physics. Theoretical foundations',
    'ShifmanVainshteinZakharov1979b': r'QCD and resonance physics. Applications',
    'CaswellLepage1986': r'Effective Lagrangians for bound state problems in QED, QCD, and other field theories',
    'StermanEtAl1995': r'Handbook of perturbative QCD',
    'Landau1959': r'On analytic properties of vertex parts in quantum field theory',
    'GribovLipatov1972a': r'Deep inelastic $e p$ scattering in perturbation theory',
    'GribovLipatov1972b': r'$e^+e^-$ pair annihilation and deep inelastic $e p$ scattering in perturbation theory',
    'Dokshitzer1977': r'Calculation of structure functions of deep-inelastic scattering and $e^+e^-$ annihilation by perturbation theory in quantum chromodynamics',
    'KuraevLipatovFadin1977': r'The Pomeranchuk singularity in nonabelian gauge theories',
    'BalitskyLipatov1978': r'The Pomeranchuk singularity in quantum chromodynamics',
    'Sudakov1956': r'Vertex Parts at Very High Energies in Quantum Electrodynamics',
    'Collins2003': r'What exactly is a parton density?',
    'DrellYan1970': r'Massive Lepton-Pair Production in Hadron-Hadron Collisions at High Energies',
    'Farhi1977': r'Quantum Chromodynamics Test for Jets',
    'Sen1983': r'Asymptotic behavior of the fixed-angle on-shell quark scattering amplitudes in non-Abelian gauge theories',
}
TITLE_SRC = {  # where a title was taken from, if not the Crossref (publisher) record
    'CurciFurmanskiPetronzio1980': 'title incl. subtitle per INSPIRE + Semantic Scholar (Crossref truncates the subtitle)',
    'Dokshitzer1977': 'title per JETP archive (jetp.ras.ru) English-edition index',
    'KuraevLipatovFadin1977': 'title per JETP archive + INSPIRE', 'Sudakov1956': 'title per JETP archive + INSPIRE',
    'GribovLipatov1972a': 'title per INSPIRE', 'GribovLipatov1972b': 'title per INSPIRE', 'BalitskyLipatov1978': 'title per INSPIRE',
    'Collins2003': 'title per INSPIRE + arXiv',
}

def clean_cr_title(t):
    t = ' '.join(t.split())
    t = t.replace('–', '--').replace('—', '---').replace('’', "'").replace('“', '``').replace('”', "''")
    return t

def title_for(key, r):
    if key in TITLE:
        return TITLE[key]
    md = r.get('main_doi')
    c = (r.get('crossref') or {}).get(md) if md else None
    if c and c['title'] and '<' not in c['title'] and c['title'].upper() != c['title']:
        t = clean_cr_title(c['title'])
        t = t.replace('Drell-Yan', 'Drell--Yan').replace('Yang-Mills', 'Yang--Mills').replace('Bloch-Nordsieck', 'Bloch--Nordsieck').replace('Bogoliubov-Parasiuk', 'Bogoliubov--Parasiuk')
        return t
    t = r['title']
    return t

def bib_escape_title(t):
    # protect & % # outside math (none expected) ; keep LaTeX
    t = re.sub(r'(?<!\\)&', r'\\&', t)
    t = re.sub(r'(?<!\\)%', r'\\%', t)
    return t

# ------------------------------------------------------------------ manual corrections of publication data
# fields: main=(jtitle, vol, first, last, year); doi; extra notes (errata/translations) as list of (kind, jtitle, vol, first, last, year, doi)
PUB_OVERRIDE = {
    'Landau1959': dict(main=('Nucl.Phys.', '13', '181', '192', 1959), doi='10.1016/0029-5582(59)90154-3',
                       extra=[('see also', 'Sov.Phys.JETP', '10', '45', None, 1960, None)]),
    'Sudakov1956': dict(main=('Sov.Phys.JETP', '3', '65', None, 1956), doi=None,
                        extra=[('orig', 'Zh.Eksp.Teor.Fiz.', '30', '87', None, 1956, None)]),
    'Slavnov1972': dict(main=('Theor.Math.Phys.', '10', '99', '104', 1972), doi='10.1007/BF01090719',
                        extra=[('orig', 'Teor.Mat.Fiz.', '10', '153', None, 1972, None)]),
    'Balitsky1996': dict(main=('Nucl.Phys.B', '463', '99', '157', 1996), doi='10.1016/0550-3213(95)00638-9', extra=[]),
    'GribovLipatov1972a': dict(main=('Sov.J.Nucl.Phys.', '15', '438', None, 1972), doi=None, extra=[('orig', 'Yad.Fiz.', '15', '781', None, 1972, None)]),
    'GribovLipatov1972b': dict(main=('Sov.J.Nucl.Phys.', '15', '675', None, 1972), doi=None, extra=[('orig', 'Yad.Fiz.', '15', '1218', None, 1972, None)]),
    'Dokshitzer1977': dict(main=('Sov.Phys.JETP', '46', '641', None, 1977), doi=None, extra=[('orig', 'Zh.Eksp.Teor.Fiz.', '73', '1216', None, 1977, None)]),
    'KuraevLipatovFadin1977': dict(main=('Sov.Phys.JETP', '45', '199', None, 1977), doi=None, extra=[('orig', 'Zh.Eksp.Teor.Fiz.', '72', '377', None, 1977, None)]),
    'BalitskyLipatov1978': dict(main=('Sov.J.Nucl.Phys.', '28', '822', None, 1978), doi=None, extra=[('orig', 'Yad.Fiz.', '28', '1597', None, 1978, None)]),
}
# errata (all confirmed against Crossref; first/last page from Crossref)
ERRATA = {
    'DrellYan1970': [('Phys.Rev.Lett.', '25', '902', None, 1970, '10.1103/PhysRevLett.25.902.2')],
    'FloratosRossSachrajda1977': [('Nucl.Phys.B', '139', '545', '546', 1978, '10.1016/0550-3213(78)90367-X')],
    'Bodwin1985': [('Phys.Rev.D', '34', '3932', None, 1986, '10.1103/PhysRevD.34.3932')],
    'HambergVanNeervenMatsuura1991': [('Nucl.Phys.B', '644', '403', '404', 2002, '10.1016/S0550-3213(02)00814-3')],
    'CollinsSoper1981': [('Nucl.Phys.B', '213', '545', None, 1983, '10.1016/0550-3213(83)90235-3')],
    'Collins1998a': [('Phys.Rev.D', '61', '019902', None, 2000, '10.1103/PhysRevD.61.019902')],
    'DiehlOstermeierSchafer2012': [('JHEP', '03', '001', None, 2016, '10.1007/JHEP03(2016)001')],
    'BodwinBraatenLepage1995': [('Phys.Rev.D', '55', '5853', '5854', 1997, '10.1103/PhysRevD.55.5853')],
}
FIRSTPAGE_ONLY = {'AngelesMartinezEtAl2015', 'Collins2003', 'Sudakov1956', 'GribovLipatov1972a', 'GribovLipatov1972b',
                  'Dokshitzer1977', 'KuraevLipatovFadin1977', 'BalitskyLipatov1978'}
AUTHOR_OVERRIDE = {  # publisher author order (Crossref) where INSPIRE's differs
    'StermanEtAl1995': ['Sterman, George F.'],  # + others (17 authors; CTEQ); Crossref byline starts with Sterman
}
COLLAB = {'StermanEtAl1995': 'CTEQ', 'AffolderEtAl2000': 'CDF', 'BrambillaEtAl2005': 'Quarkonium Working Group'}
MAXAUTH = 10

# ------------------------------------------------------------------ hand-built entries (books, chapters, reports, preprints)
MANUAL = {
 'Collins2011': dict(type='book', author=['Collins, John C.'], title='Foundations of Perturbative QCD',
    series='Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology', number='32',
    publisher='Cambridge University Press', address='Cambridge', year='2011', isbn='978-0-521-85533-4', doi='10.1017/CBO9780511975592',
    verify='Crossref 10.1017/CBO9780511975592 (CUP, 2011; ISBNs 9780521855334/9781107645257); CUP Core page (Series Number 32; pp. i-624); INSPIRE 922696; Open Library (xii+624 p.)'),
 'Collins2023': dict(type='book', author=['Collins, John C.'], title='Foundations of Perturbative QCD',
    series='Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology',
    publisher='Cambridge University Press', address='Cambridge', year='2023', isbn='978-1-009-40183-8', doi='10.1017/9781009401845',
    note='Open Access reissue of the 2011 edition',
    verify='Crossref 10.1017/9781009401845 (online 2023-07-13; print 2023-07-27; edition-number 1); CUP Core page: "First published in 2011, this title has been reissued as an Open Access publication" (CC-BY-NC-ND 4.0, 638 pp.). NOT a second edition; pagination vs 2011 not compared'),
 'Sterman1993': dict(type='book', author=['Sterman, George F.'], title='An Introduction to Quantum Field Theory',
    publisher='Cambridge University Press', address='Cambridge', year='1993', isbn='978-0-521-31132-8', doi='10.1017/CBO9780511622618',
    verify='Crossref 10.1017/CBO9780511622618 (CUP, 1993-08-26; ISBNs 9780521311328/9780521322584); INSPIRE 375196; Open Library (xvii+572 p.)'),
 'EllisStirlingWebber1996': dict(type='book', author=['Ellis, R.Keith', 'Stirling, W.James', 'Webber, B.R.'], title='QCD and Collider Physics',
    series='Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology', number='8',
    publisher='Cambridge University Press', address='Cambridge', year='1996', isbn='978-0-521-58189-9', doi='10.1017/CBO9780511628788',
    verify='Crossref 10.1017/CBO9780511628788 (CUP, 1996-10-24); INSPIRE 328604 (series vol. 8, 435 p.); Open Library (series 8; xiv+435 p.)'),
 'Muta2010': dict(type='book', author=['Muta, Taizo'], title='Foundations of Quantum Chromodynamics: An Introduction to Perturbative Methods in Gauge Theories',
    edition='3rd', series='World Scientific Lecture Notes in Physics', number='78',
    publisher='World Scientific', address='Singapore', year='2010', isbn='978-981-279-353-9', doi='10.1142/6766',
    verify='Crossref 10.1142/6766 (edition 3; series WS Lecture Notes in Physics; print date 2009-09); INSPIRE 1330235 (2010, vol. 78); Open Library (3rd ed., 2010, v. 78, xvi+409 p.). Year: catalogues give 2010, Crossref print date Sept 2009'),
 'Field1989': dict(type='book', author=['Field, R.D.'], title='Applications of Perturbative QCD', series='Frontiers in Physics', number='77',
    publisher='Addison-Wesley', address='Redwood City, CA', year='1989', isbn='0-201-14295-3',
    verify='INSPIRE 287536 (Front. Phys. 77, 366 p.); Open Library ISBN 0201142953 (Addison-Wesley Advanced Book Program, Redwood City, 1989, xviii+366 p., Frontiers in Physics v. 77). No DOI'),
 'PeskinSchroeder1995': dict(type='book', author=['Peskin, Michael E.', 'Schroeder, Daniel V.'], title='An Introduction to Quantum Field Theory',
    publisher='Addison-Wesley', address='Reading, MA', year='1995', isbn='0-201-50397-2',
    verify='INSPIRE 407703 (Addison-Wesley, Reading 1995; ISBN 9780201503975); Open Library (xxii+842 p.). Later CRC reprint DOI 10.1201/9780429503559 (2018) not cited'),
 'Weinberg1996': dict(type='book', author=['Weinberg, Steven'], title='The Quantum Theory of Fields. Vol.~II: Modern Applications',
    publisher='Cambridge University Press', address='Cambridge', year='1996', isbn='978-0-521-55002-4', doi='10.1017/CBO9781139644174',
    verify='Crossref 10.1017/CBO9781139644174 (CUP, 1996-08-13; ISBN 9780521550024); INSPIRE 430948 (Vol. 2: Modern applications); Open Library (3 v.)'),
 'Smirnov2002': dict(type='book', author=['Smirnov, Vladimir A.'], title='Applied Asymptotic Expansions in Momenta and Masses',
    series='Springer Tracts in Modern Physics', number='177', publisher='Springer', address='Berlin, Heidelberg', year='2002',
    isbn='978-3-540-42334-8', doi='10.1007/3-540-44574-9',
    verify='Crossref 10.1007/3-540-44574-9 (Springer Tracts in Modern Physics; print 2002, online 2001-06-11); INSPIRE 582124 (vol. 177, 262 p.)'),
 'BecherBroggioFerroglia2015': dict(type='book', author=['Becher, Thomas', 'Broggio, Alessandro', 'Ferroglia, Andrea'], title='Introduction to Soft-Collinear Effective Theory',
    series='Lecture Notes in Physics', number='896', publisher='Springer', address='Cham', year='2015', isbn='978-3-319-14847-2',
    doi='10.1007/978-3-319-14848-9', eprint='1410.1892', primaryClass='hep-ph',
    verify='Crossref 10.1007/978-3-319-14848-9 (Springer, Cham, 2015, Lecture Notes in Physics); INSPIRE 1320996 (Lect. Notes Phys. 896); arXiv:1410.1892'),
 'KovchegovLevin2012': dict(type='book', author=['Kovchegov, Yuri V.', 'Levin, Eugene'], title='Quantum Chromodynamics at High Energy',
    series='Cambridge Monographs on Particle Physics, Nuclear Physics and Cosmology', number='33',
    publisher='Cambridge University Press', address='Cambridge', year='2012', isbn='978-0-521-11257-4', doi='10.1017/CBO9781139022187',
    verify='Crossref 10.1017/CBO9781139022187 (CUP, 2012-08-30); INSPIRE 1217905 (series vol. 33); Open Library (series 33). (A 2022 CUP reissue has DOI 10.1017/9781009291446)'),
 'Collins1984': dict(type='book', author=['Collins, John C.'], title='Renormalization: An Introduction to Renormalization, the Renormalization Group and the Operator-Product Expansion',
    series='Cambridge Monographs on Mathematical Physics', publisher='Cambridge University Press', address='Cambridge', year='1984',
    isbn='978-0-521-24261-5', doi='10.1017/CBO9780511622656',
    verify='Crossref 10.1017/CBO9780511622656 (CUP, 1984-11-15; subtitle as given); CUP Core page (series name; OA reissue 2023 DOI 10.1017/9781009401807); INSPIRE 209810. Series number (26 in INSPIRE only) omitted'),
 'EdenEtAl1966': dict(type='book', author=['Eden, R.J.', 'Landshoff, P.V.', 'Olive, D.I.', 'Polkinghorne, J.C.'], title='The Analytic S-Matrix',
    publisher='Cambridge University Press', address='Cambridge', year='1966',
    verify='INSPIRE 1517084 (CUP, Cambridge 1966); Open Library (CUP 1966, 295 p.); 1967 reviews in Am. J. Phys./Science (Crossref). No DOI'),
 'Zimmermann1970': dict(type='incollection', author=['Zimmermann, Wolfhart'], title='Local operator products and renormalization in quantum field theory',
    booktitle='Lectures on Elementary Particles and Quantum Field Theory (1970 Brandeis University Summer Institute in Theoretical Physics), Vol.~1',
    editor=['Deser, Stanley', 'Grisaru, Marc', 'Pendleton, Hugh'], publisher='MIT Press', address='Cambridge, MA', year='1970',
    verify='INSPIRE proceedings record 1375392 (eds. Deser, Grisaru, Pendleton; MIT, Cambridge MA 1970); Open Library ISBN 026204031X (M.I.T. Press 1970, 2 v.); web search of catalogue contents (Vol. 1: Zimmermann, "Local Operator Products and Renormalization in Quantum Field Theory"). No INSPIRE record for the lecture itself; PAGE RANGE NOT VERIFIED and therefore omitted'),
 'tHooft1979': dict(type='incollection', author=["'t Hooft, Gerard"], title="Can We Make Sense Out of ``Quantum Chromodynamics''?",
    booktitle='The Whys of Subnuclear Physics (Erice, 1977)', editor=['Zichichi, Antonino'], series='Subnuclear Series', number='15',
    publisher='Springer US', address='Boston, MA', year='1979', pages=('943', '982'), doi='10.1007/978-1-4684-0991-8_17',
    verify="Crossref 10.1007/978-1-4684-0991-8_17 (pp. 943-982 in 'The Whys of Subnuclear Physics', ed. Zichichi, Springer US, Boston MA, 1979); INSPIRE 5753 (Subnucl. Ser. 15 (1979) 943; Erice 1977)"),
 'CollinsSoperSterman1989': dict(type='incollection', author=['Collins, John C.', 'Soper, Davison E.', 'Sterman, George F.'], title='Factorization of Hard Processes in QCD',
    booktitle='Perturbative QCD', editor=['Mueller, A.H.'], series='Adv. Ser. Direct. High Energy Phys.', number='5',
    publisher='World Scientific', address='Singapore', year='1989', pages=('1', '91'), doi='10.1142/9789814503266_0001', eprint='hep-ph/0409313',
    verify='Crossref 10.1142/9789814503266_0001 (pp. 1-91, in "Perturbative QCD", Adv. Ser. Direct. High Energy Phys., 1989-07); INSPIRE 25808 (vol. 5, pp. 1-91) and 286221 (volume: ed. A. H. Mueller, WSP Singapore 1989); arXiv:hep-ph/0409313'),
 'BrambillaEtAl2005': dict(type='techreport', author=['Brambilla, N.'], others=True, collaboration='Quarkonium Working Group', title='Heavy Quarkonium Physics',
    institution='CERN', reporttype='CERN Yellow Report', number='CERN-2005-005', address='Geneva', year='2005', doi='10.5170/CERN-2005-005', eprint='hep-ph/0412158',
    verify='DataCite 10.5170/CERN-2005-005 (CERN 2005; 85 creators) -> CDS 872545; INSPIRE 666911 (CERN-2005-005, 487 p.); arXiv:hep-ph/0412158'),
 'BoerEtAl2011': dict(type='misc', author=['Boer, Daniel'], others=True, title='Gluons and the quark sea at high energies: distributions, polarization, tomography',
    year='2011', eprint='1108.1713', primaryClass='nucl-th', note='INT-PUB-11-034',
    verify='INSPIRE 922440 (report nos. SLAC-R-995, INT-PUB-11-034, BNL-96164-2011, JLAB-THY-11-1373; 218 authors; no journal publication); arXiv:1108.1713'),
 'BoussarieEtAl2023': dict(type='misc', author=['Boussarie, Renaud'], others=True, title='TMD Handbook', year='2023', eprint='2304.03302', primaryClass='hep-ph',
    verify='INSPIRE 2650019 (29 authors; no journal publication recorded); arXiv:2304.03302'),
 'Collins2007': dict(type='misc', author=['Collins, John C.'], title='2-soft-gluon exchange and factorization breaking', year='2007', eprint='0708.4410', primaryClass='hep-ph',
    verify='INSPIRE 759565 (no journal publication); arXiv:0708.4410 (comment: 8 pages; no journal-ref)'),
}

# ------------------------------------------------------------------ build entries
def arxiv_of(r):
    if r.get('arxiv'):
        aid, cats = r['arxiv'][0]
        return aid, (cats[0] if cats else None)
    return None, None

def pages_str(first, last, sep='--'):
    if first and last and str(last) != str(first):
        return '%s%s%s' % (first, sep, last)
    return str(first) if first else ''

entries = []
order_keys = [e['key'] for e in S]
if 'Zimmermann1970' not in order_keys:
    i = order_keys.index('Zimmermann1973')
    order_keys.insert(i, 'Zimmermann1970')
    NOTE['Zimmermann1970'] = "Brandeis lectures: normal products and the all-orders perturbative proof of the short-distance (Wilson) expansion (Ch. 5)."
    GRP['Zimmermann1970'] = 'ope'

for key in order_keys:
    r = R.get(key, {})
    E = dict(key=key, grp=GRP[key], content=NOTE[key], texkeys=r.get('texkeys') or [], recid=r.get('recid'))
    if key in MANUAL:
        E.update(MANUAL[key])
        E['author_full'] = E['author']
        entries.append(E)
        continue
    E['type'] = 'article'
    # authors
    au = AUTHOR_OVERRIDE.get(key, r['authors'])
    others = (key in AUTHOR_OVERRIDE) or len(au) > MAXAUTH
    if len(au) > MAXAUTH:
        au = au[:1]
    E['author_full'] = au
    E['others'] = others
    E['collaboration'] = COLLAB.get(key) or (r.get('collaborations') or [None])[0]
    E['title'] = title_for(key, r)
    # publication
    if key in PUB_OVERRIDE:
        o = PUB_OVERRIDE[key]
        j, v, p1, p2, y = o['main']
        E['doi'] = o['doi']
        E['extra'] = o['extra']
    else:
        m = r['main']
        j, v, y = m['journal_title'], m['journal_volume'], m['year']
        p1 = m.get('page_start') or m.get('artid')
        p2 = None
        md = r.get('main_doi')
        c = (r.get('crossref') or {}).get(md) if md else None
        if c and c.get('page') and '-' in c['page']:
            a, b = c['page'].split('-', 1)
            if a.strip().lstrip('0') == str(p1).lstrip('0') and b.strip() != a.strip():
                p2 = b.strip()
        if key in FIRSTPAGE_ONLY:
            p2 = None
        E['doi'] = None
        if md:
            cands = [d for d in (r.get('dois') or []) if d.lower() == md.lower()]
            E['doi'] = cands[0] if cands else md
        E['extra'] = []
    E['journal'], E['volume'], E['p1'], E['p2'], E['year'] = j, v, p1, p2, str(y)
    E['errata'] = ERRATA.get(key, [])
    aid, cat = arxiv_of(r)
    E['eprint'], E['primaryClass'] = aid, cat
    entries.append(E)

# restore canonical DOI capitalisation (DOIs are case-insensitive; print in publisher's usual form)
def doi_case(d):
    if not d:
        return d
    d2 = d
    for pfx in ('10.1103/', '10.1016/', '10.1007/', '10.1088/', '10.1140/', '10.1146/', '10.1142/', '10.1002/', '10.5506/', '10.1017/', '10.1063/'):
        if d.lower().startswith(pfx):
            rest = d[len(pfx):]
            if pfx in ('10.1103/',):
                rest = re.sub(r'^physrev', 'PhysRev', rest, flags=re.I)
                rest = re.sub(r'^PhysRev(lett|d|)', lambda m: 'PhysRev' + {'lett': 'Lett', 'd': 'D', '': ''}[m.group(1).lower()], rest)
                rest = re.sub(r'^revmodphys', 'RevModPhys', rest, flags=re.I)
            elif pfx == '10.1007/':
                rest = re.sub(r'^jhep', 'JHEP', rest, flags=re.I).replace('bf', 'BF', 1) if rest.lower().startswith(('jhep', 'bf')) else rest
                rest = re.sub(r'^s', 'S', rest) if re.match(r'^s\d', rest) else rest
            elif pfx == '10.1016/':
                rest = rest.upper() if re.match(r'^[0-9]', rest) else rest.replace('j.', 'j.')
                rest = re.sub(r'^S', 'S', rest)
                if rest.lower().startswith('s0'):
                    rest = 'S' + rest[1:].upper()
            elif pfx == '10.1017/':
                rest = rest.replace('cbo', 'CBO')
            elif pfx == '10.1088/':
                rest = rest
            elif pfx == '10.1140/':
                rest = rest
            elif pfx == '10.5506/':
                rest = rest.replace('aphyspolb', 'APhysPolB')
            d2 = pfx + rest
    return d2

# (DOIs are taken in INSPIRE's original capitalisation; DOIs are case-insensitive)

# ------------------------------------------------------------------ writers
def bibfield(k, v):
    return '  %-13s = {%s},\n' % (k, v)

def write_bib(E):
    t = E['type']
    s = '@%s{%s,\n' % (t, E['key'])
    names = [bib_name(a) for a in E['author_full']]
    if E.get('others'):
        names.append('others')
    s += bibfield('author', ' and '.join(names))
    if E.get('collaboration'):
        s += bibfield('collaboration', E['collaboration'])
    s += bibfield('title', '{' + bib_escape_title(E['title']) + '}')
    if t == 'article':
        s += bibfield('journal', JOURNAL[E['journal']][0])
        s += bibfield('volume', E['volume'])
        s += bibfield('pages', pages_str(E['p1'], E['p2']))
        s += bibfield('year', E['year'])
        notes = []
        for (kind, j, v, p1, p2, y, d) in E.get('extra', []):
            if kind == 'orig':
                notes.append('[%s %s, %s (%s)]' % (JOURNAL[j][0], v, pages_str(p1, p2), y))
            else:
                notes.append('[See also %s %s, %s (%s)]' % (JOURNAL[j][0], v, pages_str(p1, p2), y))
        for (j, v, p1, p2, y, d) in E.get('errata', []):
            notes.append('[Erratum: %s %s, %s (%s)]' % (JOURNAL[j][0], v, pages_str(p1, p2), y))
        if notes:
            s += bibfield('note', ' '.join(notes))
    elif t == 'book':
        if E.get('edition'):
            s += bibfield('edition', E['edition'])
        if E.get('series'):
            s += bibfield('series', E['series'])
        if E.get('number'):
            s += bibfield('volume', E['number'])
        s += bibfield('publisher', E['publisher'])
        s += bibfield('address', E['address'])
        s += bibfield('year', E['year'])
        if E.get('isbn'):
            s += bibfield('isbn', E['isbn'])
        if E.get('note'):
            s += bibfield('note', E['note'])
    elif t == 'incollection':
        s += bibfield('booktitle', '{' + E['booktitle'] + '}')
        s += bibfield('editor', ' and '.join(bib_name(a) for a in E['editor']))
        if E.get('series'):
            s += bibfield('series', E['series'])
        if E.get('number'):
            s += bibfield('volume', E['number'])
        s += bibfield('publisher', E['publisher'])
        s += bibfield('address', E['address'])
        s += bibfield('year', E['year'])
        if E.get('pages'):
            s += bibfield('pages', pages_str(*E['pages']))
    elif t == 'techreport':
        s += bibfield('institution', E['institution'])
        s += bibfield('type', E['reporttype'])
        s += bibfield('number', E['number'])
        s += bibfield('address', E['address'])
        s += bibfield('year', E['year'])
    elif t == 'misc':
        s += bibfield('year', E['year'])
        if E.get('note'):
            s += bibfield('note', E['note'])
    if E.get('doi'):
        s += bibfield('doi', E['doi'])
    if E.get('eprint'):
        s += bibfield('eprint', E['eprint'])
        s += bibfield('archivePrefix', 'arXiv')
        if '/' not in E['eprint'] and E.get('primaryClass'):
            s += bibfield('primaryClass', E['primaryClass'])
    for (j, v, p1, p2, y, d) in E.get('errata', []):
        s += bibfield('erratumdoi', d)
    if E.get('texkeys'):
        s += bibfield('inspire', E['texkeys'][0])
    s = s.rstrip(',\n') + '\n}\n'
    return s

def item_title(t):
    return t

def write_item(E):
    names = [item_name(a) for a in E['author_full']]
    if E.get('others'):
        au = names[0] + ' \\emph{et al.}'
    else:
        au = join_items(names)
    if E.get('collaboration'):
        au += ' (%s%s)' % (E['collaboration'], '' if 'Group' in E['collaboration'] else ' Collaboration')
    t = E['type']
    s = '\\bibitem{%s}\n%s, \\emph{%s}' % (E['key'], au, item_title(E['title']))
    if t == 'article':
        s += ', %s~\\textbf{%s} (%s) \\mbox{%s}' % (JOURNAL[E['journal']][1], E['volume'], E['year'], pages_str(E['p1'], E['p2']))
        for (kind, j, v, p1, p2, y, d) in E.get('extra', []):
            if kind == 'orig':
                s += ' [%s \\textbf{%s} (%s) \\mbox{%s}]' % (JOURNAL[j][1], v, y, pages_str(p1, p2))
            else:
                s += '; see also %s~\\textbf{%s} (%s) \\mbox{%s}' % (JOURNAL[j][1], v, y, pages_str(p1, p2))
        for (j, v, p1, p2, y, d) in E.get('errata', []):
            s += ' [Erratum: %s~\\textbf{%s} (%s) \\mbox{%s}]' % (JOURNAL[j][1], v, y, pages_str(p1, p2))
    elif t == 'book':
        if E.get('edition'):
            s += ', %s ed.' % E['edition']
        if E.get('series'):
            s += ', %s%s' % (E['series'], (' \\textbf{%s}' % E['number']) if E.get('number') else '')
        s += ', %s, %s (%s)' % (E['publisher'], E['address'], E['year'])
        if E.get('note'):
            s += ' [%s]' % E['note']
    elif t == 'incollection':
        eds = join_items([item_name(a) for a in E['editor']])
        s += ', in \\emph{%s}, %s %s' % (E['booktitle'], 'eds.' if len(E['editor']) > 1 else 'ed.', eds)
        if E.get('series'):
            s += ', %s~\\textbf{%s}' % (E['series'], E['number'])
        s += ', %s, %s (%s)' % (E['publisher'], E['address'], E['year'])
        if E.get('pages'):
            s += ', pp.~\\mbox{%s}' % pages_str(*E['pages'])
    elif t == 'techreport':
        s += ', %s %s, %s, %s (%s)' % (E['reporttype'], E['number'], E['institution'], E['address'], E['year'])
    elif t == 'misc':
        if E.get('note'):
            s += ', %s' % E['note']
        s += ' (%s)' % E['year']
    if E.get('eprint'):
        s += ', \\href{https://arxiv.org/abs/%s}{arXiv:%s}' % (E['eprint'], E['eprint'])
    s += '.\n'
    return s

GROUP_TITLE = [
    ('book', 'Textbooks and monographs'), ('review', 'Reviews'),
    ('ope', 'Parton model, OPE, asymptotic freedom, evolution'),
    ('ren', 'Renormalization, gauge-theory identities, unitarity, Wilson lines'),
    ('ir', 'Infrared structure, Landau equations, power counting, regions'),
    ('ee', 'e+e- annihilation, duality, event shapes, cut vertices'),
    ('fact', 'Collinear factorization proofs (DIS, DY), PDFs'),
    ('hq', 'Heavy quarks in factorization'),
    ('tmd', 'TMD factorization'),
    ('break', 'Factorization breaking and non-rigorous cases'),
    ('smallx', 'Small-x, BFKL, saturation'),
    ('excl', 'Hard exclusive processes, DAs, GPDs'),
    ('scet', 'Soft-collinear effective theory'),
    ('bphys', 'B-meson decays (QCD factorization)'),
    ('onium', 'Heavy quarkonium'),
    ('power', 'Power corrections, higher twist, renormalons, threshold resummation'),
    ('lattice', 'Lattice approaches to parton physics'),
]

def verification_line(E):
    k = E['key']
    if E['type'] != 'article':
        return E['verify']
    r = R[k]
    parts = ['INSPIRE %s (%s)' % (r.get('recid'), ', '.join(r.get('texkeys') or []))]
    if E.get('doi'):
        md = r.get('main_doi')
        if k in PUB_OVERRIDE and PUB_OVERRIDE[k].get('doi'):
            parts.append('Crossref %s' % E['doi'])
        elif md:
            c = r['crossref'][md]
            parts.append('Crossref %s (vol %s, p. %s, %s)' % (E['doi'], c.get('volume'), c.get('page') or c.get('artno'), c.get('pprint') or c.get('issued')))
    else:
        parts.append('no DOI')
    if E.get('eprint'):
        parts.append('arXiv:%s' % E['eprint'])
    for (j, v, p1, p2, y, d) in E.get('errata', []):
        parts.append('erratum Crossref %s' % d)
    extra = {
        'Dokshitzer1977': 'JETP archive: JETP 46(4) 641, Oct 1977 [ZhETF 73(4) 1216]; end pages INSPIRE-only -> first page cited; printed spelling "Dokshitser"',
        'KuraevLipatovFadin1977': 'JETP archive: JETP 45(2) 199, Feb 1977 [ZhETF 72(2) 377]; first page cited',
        'Sudakov1956': 'JETP archive: JETP 3(1) 65, Jul 1956 [ZhETF 30(1) 87]; first page cited',
        'Landau1959': 'INSPIRE mislabels Nucl. Phys. 13 as "reprint"; Crossref confirms Nucl. Phys. 13 (1959) 181-192; JETP archive confirms JETP 10(1) 45 (Jan 1960) version',
        'Slavnov1972': 'English pages 99-104 per Crossref/OpenAlex/Semantic Scholar (INSPIRE says 99-107: wrong); Russian original TMF 10, 153 per INSPIRE only',
        'Balitsky1996': 'pages 99-157 per Crossref/OpenAlex/Semantic Scholar (INSPIRE says 99-160: wrong)',
        'GribovLipatov1972a': 'Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited',
        'GribovLipatov1972b': 'Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited',
        'BalitskyLipatov1978': 'Sov. J. Nucl. Phys. and Yad. Fiz. data INSPIRE-only (no DOI); first pages cited',
        'StermanEtAl1995': 'author order per publisher (Crossref: Sterman, Smith, Collins, Whitmore, Brock, ...; 17 authors); INSPIRE lists alphabetically from Brock; title per publisher (INSPIRE adds "Version 1.0")',
        'CurciFurmanskiPetronzio1980': TITLE_SRC['CurciFurmanskiPetronzio1980'],
        'Sen1983': 'publisher title says "fixed-angle" (INSPIRE: "wide angle")',
        'IsgurLlewellynSmith1984': 'publisher title "Asymptotic Q^2 for ..." (INSPIRE carries preprint title "Asymptopia in high q**2 ...")',
        'Farhi1977': 'publisher title "Quantum Chromodynamics Test for Jets" (INSPIRE: "A QCD Test for Jets")',
        'PoggioQuinnWeinberg1976': 'publisher title "Smearing method in the quark model" (INSPIRE: "Smearing the Quark Model")',
        'DoriaFrenkelTaylor1980': 'publisher title "...conjecture" (INSPIRE: "...Theorem")',
        'RogersMulders2010': 'publisher title differs from arXiv/INSPIRE wording; publisher version used',
        'Bodwin1985': 'NB: INSPIRE BibTeX export puts the ERRATUM DOI in the doi field; main DOI 10.1103/PhysRevD.31.2616 used here',
        'DokshitzerDiakonovTroian1978': 'names as in INSPIRE; printed byline: D. I. D\'yakonov, S. I. Troyan',
        'BogoliubovParasiuk1957': 'German original title per publisher; printed author spelling "Bogoliubow"; INSPIRE gives English translation of title',
        'Collins2003': 'journal data INSPIRE + arXiv journal-ref (no DOI); first page cited',
        'AngelesMartinezEtAl2015': 'Crossref gives first page only; page range INSPIRE-only -> first page cited',
        'QiuSterman1992': 'content is direct-photon production (not pion production)',
        'BauerFlemingLuke2000': 'year 2000 (Crossref issued 2000; issue dated Jan 2001)',
        'Collins1998a': 'erratum PRD 61 019902: Crossref online 1999, volume year 2000 (INSPIRE 2000)',
        'AybatSterman2009': 'arXiv 2008, journal 2009',
        'HambergVanNeervenMatsuura1991': 'INSPIRE title has typo "alpha-s"; publisher title used',
        'EchevarriaIdilbiScimemi2012': 'author diacritics per publisher byline (Echevarría)',
        'DiehlOstermeierSchafer2012': 'author diacritics per publisher byline (Schäfer)',
        'ForshawSeymourSiodmok2012': 'author diacritics per publisher byline (Siódmok)',
    }.get(k)
    if extra:
        parts.append(extra)
    if E.get('title') and k not in TITLE and r.get('main_doi'):
        pass
    return '; '.join(parts)

# ---- write files
os.makedirs(outdir, exist_ok=True)
today = '2026-10-09'
hdr = ('% refs.bib -- verified bibliography for the QCD factorization monograph\n'
       '% Generated ' + today + '. Every entry checked against INSPIRE-HEP and (where a DOI exists) Crossref; arXiv IDs checked via the arXiv API.\n'
       '% Key scheme: <Surname1><Surname2><Surname3><Year>[a|b|c] for <=3 authors, <FirstSurname>EtAl<Year>[a|b] for >=4 authors.\n'
       '% Non-standard fields (ignored by standard styles): inspire = INSPIRE texkey, erratumdoi = DOI of the erratum.\n'
       '% See NOTES.md for one line per entry (content + verification source).\n\n')
out_bib = hdr
out_items = ('%% refs_bibitems.tex -- the same verified entries as refs.bib, in the house style of furry_qcd.tex\n'
             '%% (\\bibitem{Key} Authors, \\emph{Title}, Journal~\\textbf{vol} (year) \\mbox{pages}, arXiv link).\n'
             '%% Grouped by topic; reorder by first citation when assembling the monograph. Requires hyperref (\\href).\n'
             '\\begin{thebibliography}{999}\n\n')
notes = []
count = 0
by_grp = {}
for E in entries:
    by_grp.setdefault(E['grp'], []).append(E)
for g, gt in GROUP_TITLE:
    lst = by_grp.get(g, [])
    if not lst:
        continue
    out_bib += '%% ==================== %s ====================\n\n' % gt
    out_items += '%% ---------------- %s ----------------\n' % gt
    notes.append('\n## %s (%d)\n' % (gt, len(lst)))
    for E in lst:
        out_bib += write_bib(E) + '\n'
        out_items += write_item(E) + '\n'
        count += 1
        notes.append('- `%s` — %s — **Verified:** %s' % (E['key'], E['content'], verification_line(E)))
out_items += '\\end{thebibliography}\n'
open(os.path.join(outdir, 'refs.bib'), 'w', encoding='utf-8').write(out_bib)
open(os.path.join(outdir, 'refs_bibitems.tex'), 'w', encoding='utf-8').write(out_items)
open(os.path.join(outdir, 'NOTES_entries.md.part'), 'w', encoding='utf-8').write('\n'.join(notes) + '\n')
json.dump(entries, open(os.path.join(outdir, 'entries_debug.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print('entries written:', count)
