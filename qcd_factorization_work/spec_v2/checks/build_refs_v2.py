"""Build spec_v2/refs_merged_v2.bib, spec_v2/key_aliases_v2.tsv and checks/merge_log_v2.tsv.

Usage (from anywhere):  python3 -I build_refs_v2.py WORKDIR
WORKDIR = the project directory qcd_factorization_work (path may contain spaces).

Inputs (read-only):
  spec/refs_merged.bib, spec/key_aliases.tsv                 (spec v1, 646 entries)
  frontier/yzliu/yzliu.bib, frontier/lamet/lamet.bib, frontier/others/others.bib
  spec_v2/checks/inspire_additions/*.bib                     (fetched by fetch_additions.py and, for spec v2.1,
                                                             fetch_additions_v21.py)
  verify/**/*.bib                                            (none existed on 2026-10-10)
Merge order (earlier wins): v1 > yzliu > lamet > others > spec-v2 INSPIRE additions > manual entries.
Duplicates are detected by DOI, arXiv number or INSPIRE texkey (entry key or `inspire` field).
"""
import os, re, sys, glob, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bibparse import parse_bib, norm_doi, norm_arxiv

W = sys.argv[1].rstrip('/') + '/'
OUTBIB = W + 'spec_v2/refs_merged_v2.bib'
OUTALIAS = W + 'spec_v2/key_aliases_v2.tsv'
OUTLOG = W + 'spec_v2/checks/merge_log_v2.tsv'

SOURCES = [
    ('v1', W + 'spec/refs_merged.bib'),
    ('yzliu', W + 'frontier/yzliu/yzliu.bib'),
    ('lamet', W + 'frontier/lamet/lamet.bib'),
    ('others', W + 'frontier/others/others.bib'),
]
verify_bibs = sorted(glob.glob(W + 'verify/**/*.bib', recursive=True))
for vb in verify_bibs:
    SOURCES.append(('verify:' + os.path.relpath(vb, W), vb))

# ---------------------------------------------------------------- manual entries (Crossref-verified)
MANUAL = r"""
@article{Epstein1960,
  author        = {Epstein, H.},
  title         = {{Generalization of the ``Edge-of-the-Wedge'' Theorem}},
  journal       = {J. Math. Phys.},
  volume        = {1},
  number        = {6},
  pages         = {524--531},
  year          = {1960},
  doi           = {10.1063/1.1703688}
}

@article{Markoff1916,
  author        = {Markoff, Wladimir},
  title         = {{\"Uber Polynome, die in einem gegebenen Intervalle m\"oglichst wenig von Null abweichen}},
  journal       = {Math. Ann.},
  volume        = {77},
  number        = {2},
  pages         = {213--258},
  year          = {1916},
  doi           = {10.1007/BF01456902}
}

@article{SlepianPollak1961,
  author        = {Slepian, D. and Pollak, H. O.},
  title         = {{Prolate spheroidal wave functions, Fourier analysis and uncertainty -- I}},
  journal       = {Bell Syst. Tech. J.},
  volume        = {40},
  number        = {1},
  pages         = {43--63},
  year          = {1961},
  doi           = {10.1002/j.1538-7305.1961.tb03976.x},
}

@article{LandauWidom1980,
  author        = {Landau, H. J. and Widom, H.},
  title         = {{Eigenvalue distribution of time and frequency limiting}},
  journal       = {J. Math. Anal. Appl.},
  volume        = {77},
  number        = {2},
  pages         = {469--481},
  year          = {1980},
  doi           = {10.1016/0022-247X(80)90241-3},
}

@techreport{Zweig:1964jf,
  author        = {Zweig, G.},
  title         = {{An SU(3) model for strong interaction symmetry and its breaking. Version 2}},
  institution   = {CERN},
  number        = {CERN-TH-412},
  year          = {1964},
  doi           = {10.17181/CERN-TH-412},
  note          = {Reprinted in D. B. Lichtenberg and S. P. Rosen (eds.), \emph{Developments in the Quark Theory of Hadrons}, Vol.~1, pp.~22--101},
  inspire       = {Zweig:1964jf}
}
"""
# spec v2.1: the printed note of Markoff1916 ('German version; Crossref also lists J. Grossmann') was an internal
# remark and is removed; Crossref lists J. Grossmann as a second 'author' (presumably the translator; not verified).
# spec v2.1: SlepianPollak1961 and LandauWidom1980 (Crossref metadata checked 2026-10-10) are cited for the
# Fourier step of Ch22 (VF-LAM-17; frontier/lamet/LAMET.md Sec. 7.2 names them but they are not in INSPIRE).
# spec v2.1: printed-note fixes in two v1 entries (the v1 text is otherwise copied verbatim).  BibTeX `unsrt` prints
# the note field, so internal provenance remarks must not be there; the provenance is kept in REFS_NOTES_v2 Sec. 1.2.
V1_NOTE_PATCHES = [
    ('    note = "Added by the spec audit (2026-10-10) from frontier/others/others.bib (INSPIRE- and Crossref-verified there)",\n', ''),
    ('    note = "Talk at the 8th International Symposium on Heavy Flavor Physics (1999); book reference corrected by the spec audit from INSPIRE (parent record Shifman:2001ck)",',
     '    note = "Talk at the 8th International Symposium on Heavy Flavor Physics (1999)",'),
]
# spec v2.1: legacy all-caps INSPIRE titles of eight v1 entries replaced by the published titles (Crossref, by DOI,
# checked 2026-10-10).  Frenkel:1983di and Catani:1985xt also differ in wording from the INSPIRE (preprint) titles.
V1_TITLE_PATCHES = [
    ('    title = "{NONCANCELLING INFRARED DIVERGENCES IN QCD COHERENT STATE}",',
     '    title = "{Non-cancelling infrared divergences in QCD coherent states}",'),
    ('    title = "{IS QUARK - ANTI-QUARK ANNIHILATION INFRARED SAFE AT HIGH-ENERGY?}",',
     '    title = "{Quark-antiquark annihilation is infrared safe at high energy to all orders}",'),
    ('    title = "{DOUBLE SCATTERING IN NUCLEI AT HIGH-ENERGY}",',
     '    title = "{Double scattering in nuclei at high energy}",'),
    ('    title = "{AN OPERATOR APPROACH TO WEIGHTED CROSS-SECTIONS}",',
     '    title = "{An operator approach to weighted cross sections}",'),
    ('    title = "{THE INFLUENCE OF THE ANALYTICAL CONTINUATION EFFECTS ON THE VALUE OF THE QCD SCALE PARAMETER LAMBDA EXTRACTED FROM THE DATA ON CHARMONIUM AND UPSILON HADRON DECAYS}",',
     '    title = "{The influence of the analytical continuation effects on the value of the QCD scale parameter $\\Lambda$ extracted from the data on charmonium and upsilon hadron decays}",'),
    ('    title = "{DIMENSIONALLY REGULARIZED TWO LOOP ON-SHELL QUARK FORM-FACTOR}",',
     '    title = "{Dimensionally regularized two-loop on-shell quark form factor}",'),
    ('    title = "{NONABELIAN EIKONAL EXPONENTIATION}",',
     '    title = "{Non-abelian eikonal exponentiation}",'),
    ('    title = "{FINITE CORRECTIONS TO QUARK FRAGMENTATION FUNCTIONS IN PERTURBATIVE QCD}",',
     '    title = "{Finite corrections to quark fragmentation functions in perturbative QCD}",'),
]
# INSPIRE additions replaced by a manual version (bibtex type problems)
REPLACED_BY_MANUAL = {'Zweig:1964jf'}
# field patches for new entries (verified via Crossref 2026-10-10); applied to the raw text
PATCHES = {
    'Piguet:1995er': ('    volume = "28",',
                      '    volume = "28",\n    series = "Lecture Notes in Physics Monographs",\n    publisher = "Springer",\n    address = "Berlin, Heidelberg",'),
    # spec v2.1: legacy all-caps titles replaced by the published titles (Crossref, by DOI)
    'Chetyrkin:1982zq': ('    title = "{OPERATOR PRODUCT EXPANSION IN THE MINIMAL SUBTRACTION SCHEME}",',
                         '    title = "{Operator product expansion in the minimal subtraction scheme}",'),
    'Gawedzki:1985ez': ('    title = "{GROSS-NEVEU MODEL THROUGH CONVERGENT PERTURBATION EXPANSIONS}",',
                        '    title = "{Gross-Neveu model through convergent perturbation expansions}",'),
    'Nielsen:1980sx': ('    title = "{ASYMPTOTIC FREEDOM AS A SPIN EFFECT}",',
                       '    title = "{Asymptotic freedom as a spin effect}",'),
    # spec v2.1: INSPIRE exports the ADS DOI 10.1007/BF02909194, which does not resolve in Crossref; the Crossref
    # record of Z. Phys. C 72 (1996) 627 (Bartels-Ermolaev-Ryskin) is 10.1007/s002880050285 (checked 2026-10-10).
    # spec v2.1: the yzliu entry carries an internal provenance note (printed by unsrt); removed, provenance kept in
    # REFS_NOTES_v2 Sec. 1.2.
    'LatticeParton:2020uhz': ('    year = "2020",\n    note = "INSPIRE record 1798505 merges this PRL with PoS LATTICE2021 (2022) 477 (doi:10.22323/1.396.0477); DOI and author list here checked against Crossref"',
                              '    year = "2020"'),
    'Bartels:1996wc': [('    doi = "10.1007/BF02909194",', '    doi = "10.1007/s002880050285",'),
                       ('    title = "{Flavor singlet contribution to the structure function G(1) at small x}",',
                        '    title = "{Flavor singlet contribution to the structure function $g_1$ at small $x$}",')],
    # spec v2.1: typographic title fixes (Crossref titles: 'g1', 'g1(x,Q2)')
    'Bartels:1995iu': ('    title = "{Nonsinglet contributions to the structure function g1 at small x}",',
                       '    title = "{Nonsinglet contributions to the structure function $g_1$ at small $x$}",'),
    # spec v2.1: INSPIRE exports 'Blumlein' without the umlaut; Crossref (DOI 10.1016/0370-2693(96)00958-6): Bluemlein.
    'Blumlein:1996hb': [('    author = "Blumlein, J. and Vogt, A.",', '    author = "Bl{\\"u}mlein, J. and Vogt, A.",'),
                        ('    title = "{The Singlet contribution to the structure function g1 (x, Q**2) at small x}",',
                         '    title = "{The singlet contribution to the structure function $g_1(x,Q^2)$ at small $x$}",')],
}

def ids(e):
    f = e['fields']; out = []
    d = norm_doi(f.get('doi'))
    if d: out.append(('doi', d))
    a = norm_arxiv(f.get('eprint'))
    if a: out.append(('arxiv', a))
    tk = f.get('inspire')
    if tk: out.append(('tk', tk.strip()))
    if ':' in e['key']: out.append(('tk', e['key']))
    return out

UNI = {'ξ': r'\xi', '→': r'\to ', '–': '--', '—': '---', '’': "'", '‘': '`', '“': '``', '”': "''",
       'ö': r'{\"o}', 'ü': r'{\"u}', 'ä': r'{\"a}', 'é': r"{\'e}", 'è': r'{\`e}', 'ł': r'{\l}', 'ń': r"{\'n}",
       'ç': r'{\c c}', 'á': r"{\'a}", 'í': r"{\'i}", 'ó': r"{\'o}", 'ú': r"{\'u}", 'ñ': r'{\~n}', 'Ö': r'{\"O}',
       'Ü': r'{\"U}', 'ß': r'{\ss}', 'ę': r'{\k e}', 'ą': r'{\k a}', 'ś': r"{\'s}", 'ć': r"{\'c}", 'ż': r'{\.z}',
       'ź': r"{\'z}", 'Ş': r'{\c S}', 'ş': r'{\c s}', 'ğ': r'{\u g}', 'ı': r'{\i}', 'Č': r'{\v C}', 'č': r'{\v c}',
       'š': r'{\v s}', 'ž': r'{\v z}', 'ř': r'{\v r}', 'ě': r'{\v e}', 'å': r'{\aa}', 'ø': r'{\o}', 'æ': r'{\ae}'}

def asciify(raw, key, log):
    out = []
    for c in raw:
        if ord(c) > 127:
            rep = UNI.get(c)
            if rep is None:
                raise SystemExit('unmapped non-ASCII %r in %s' % (c, key))
            log.append('%s: replaced %r by %r' % (key, c, rep))
            out.append(rep)
        else:
            out.append(c)
    return ''.join(out)

def to_misc(e):
    """arXiv-only @article (no journal) -> @misc with howpublished, as in spec v1."""
    f = e['fields']
    eprint = f.get('eprint', '').strip()
    pc = f.get('primaryclass', '').strip()
    hp = 'arXiv:%s' % eprint + (' [%s]' % pc if pc else '')
    lines = ['@misc{%s,' % e['key'], '    howpublished = "%s",' % hp]
    for name in e['order']:
        if name in ('journal',):
            continue
        val = f[name]
        lines.append('    %s = "%s",' % ({'archiveprefix': 'archivePrefix', 'primaryclass': 'primaryClass',
                                         'reportnumber': 'reportNumber'}.get(name, name), val))
    lines[-1] = lines[-1].rstrip(',')
    lines.append('}')
    return '\n'.join(lines)

def main():
    log_uni = []
    ents = {}
    for tag, fn in SOURCES:
        ents[tag] = parse_bib(open(fn, encoding='utf-8').read(), tag)
    add = []
    for fn in sorted(glob.glob(W + 'spec_v2/checks/inspire_additions/*.bib')):
        es = parse_bib(open(fn, encoding='utf-8').read(), 'spec-v2 INSPIRE:' + os.path.basename(fn)[:-4])
        assert len(es) == 1, fn
        if es[0]['key'] in REPLACED_BY_MANUAL:
            continue
        add.extend(es)
    man = parse_bib(MANUAL, 'spec-v2 manual')
    order = [t for t, _ in SOURCES] + ['add', 'manual']
    ents['add'] = add; ents['manual'] = man

    merged = []
    idx = collections.defaultdict(list)
    keys = {}
    aliases = []      # (alias, merged, origin)
    logrows = []      # key, source, status, target, how, notes
    newblocks = collections.OrderedDict((t, []) for t in order if t != 'v1')
    for e in ents['v1']:
        merged.append(e); keys[e['key']] = e
        for i in ids(e): idx[i].append(e)
    for tag in order[1:]:
        for e in ents[tag]:
            cands = [(i, c) for i in ids(e) for c in idx.get(i, [])]
            if cands:
                doim = [c for i, c in cands if i[0] == 'doi']
                target = doim[0] if doim else cands[0][1]
                how = sorted(set(i[0] for i, c in cands if c is target))
                other = sorted(set(c['key'] for i, c in cands if c is not target))
                src = e['source']
                if e['key'] != target['key']:
                    aliases.append((e['key'], target['key'], '%s duplicate of %s entry (match: %s)' % (src, target['source'], '+'.join(how))))
                logrows.append((e['key'], src, 'duplicate', target['key'], '+'.join(how),
                                ('also matches ' + ','.join(other)) if other else ''))
                continue
            if e['key'] in keys:
                raise SystemExit('key collision without identifier match: %s (%s vs %s)' % (e['key'], e['source'], keys[e['key']]['source']))
            raw = e['raw']
            note = []
            if e['type'] == 'article' and not e['fields'].get('journal') and e['fields'].get('eprint'):
                raw = to_misc(e); note.append('arXiv-only @article converted to @misc')
            if e['key'] in PATCHES:
                pl = PATCHES[e['key']]
                for old, new in ([pl] if isinstance(pl, tuple) else pl):
                    assert old in raw, (e['key'], old)
                    raw = raw.replace(old, new, 1)
                note.append('patched (Crossref): ' + e['key'])
            raw2 = asciify(raw, e['key'], log_uni)
            if raw2 != raw: note.append('non-ASCII replaced')
            e['raw_out'] = raw2
            merged.append(e); keys[e['key']] = e
            for i in ids(e): idx[i].append(e)
            newblocks[tag].append(e)
            aliases.append((e['key'], e['key'], '%s new entry' % e['source']))
            logrows.append((e['key'], e['source'], 'new', e['key'], '', '; '.join(note)))
    # readable aliases for the spec-v2 INSPIRE additions (tag -> texkey)
    for fn in sorted(glob.glob(W + 'spec_v2/checks/inspire_additions/*.bib')):
        tag = os.path.basename(fn)[:-4]
        es = parse_bib(open(fn, encoding='utf-8').read(), '')
        k = es[0]['key']
        if tag != k:
            aliases.append((tag, k, 'readable alias of a spec-v2 INSPIRE addition'))

    # ----------------------------------------------------------- write bib
    v1text = open(SOURCES[0][1], encoding='utf-8').read()
    for old, new in V1_NOTE_PATCHES + V1_TITLE_PATCHES:
        assert v1text.count(old) == 1, old
        v1text = v1text.replace(old, new, 1)
    hdr = []
    hdr.append('% refs_merged_v2.bib -- the single bibliography of the QCD factorization monograph, spec v2')
    hdr.append('% Built 2026-10-10 by spec_v2/checks/build_refs_v2.py (spec-v2 bibliography drafter); spec v2.1 rebuild')
    hdr.append('%   (same day) adds 3 INSPIRE records (checks/fetch_additions_v21.py) and 2 Crossref manual entries.')
    hdr.append('% Content: PARTS 1-4 = spec v1 refs_merged.bib verbatim (646 entries, all keys unchanged; spec v2.1 removed')
    hdr.append('%   two internal provenance remarks from printed note fields, see REFS_NOTES_v2 Sec. 1.2; numeric month')
    hdr.append('%   fields of all parts are written as BibTeX month macros, e.g. month = jul; eight legacy all-caps')
    hdr.append('%   INSPIRE titles of v1 entries replaced by the published titles from Crossref);')
    hdr.append('%   PART 5 = new entries of frontier/yzliu/yzliu.bib; PART 6 = frontier/lamet/lamet.bib;')
    hdr.append('%   PART 7 = frontier/others/others.bib; PART 8 = spec-v2 additions fetched from INSPIRE-HEP')
    hdr.append('%   (spec_v2/checks/inspire_additions, one hit per journal-reference query); PART 9 = manual entries')
    hdr.append('%   verified via Crossref.  Duplicates (DOI / arXiv / INSPIRE texkey) are NOT repeated: their keys')
    hdr.append('%   are mapped in spec_v2/key_aliases_v2.tsv.  arXiv-only article records were converted to misc entries')
    hdr.append('%   (howpublished = arXiv number), as in spec v1.  Non-ASCII characters were replaced by LaTeX macros.')
    hdr.append('% Content notes and binding warnings: spec_v2/REFS_NOTES_v2.md.')
    hdr.append('% verify/ bibliographies merged: ' + (', '.join(os.path.relpath(v, W) for v in verify_bibs) or 'none (verify/ did not exist at build time)'))
    out = ['\n'.join(hdr), '', '% ' + '=' * 70, '% PARTS 1-4: spec v1 (spec/refs_merged.bib), verbatim except the v2.1 format fixes (2 notes, 8 titles, 5 months)', '% ' + '=' * 70, '', v1text.rstrip(), '']
    titles = {'yzliu': 'PART 5: frontier/yzliu/yzliu.bib -- new entries (INSPIRE + Crossref verified by the yzliu agent)',
              'lamet': 'PART 6: frontier/lamet/lamet.bib -- new entries (INSPIRE texkeys, resolved by build_bib.py)',
              'others': 'PART 7: frontier/others/others.bib -- new entries (INSPIRE verbatim; Gordan:1873 via Crossref)',
              'add': 'PART 8: spec-v2 additions (INSPIRE-HEP, fetched 2026-10-10 by spec_v2/checks/fetch_additions.py and fetch_additions_v21.py)',
              'manual': 'PART 9: spec-v2 manual entries (Crossref-verified 2026-10-10)'}
    for tag, lst in newblocks.items():
        if not lst: continue
        out += ['', '% ' + '=' * 70, '% ' + titles.get(tag, 'PART: ' + tag), '% ' + '=' * 70, '']
        for e in lst:
            out.append(e['raw_out'].strip()); out.append('')
    final = '\n'.join(out) + '\n'
    # spec v2.1: numeric month fields (INSPIRE exports month = "7" for preprints) print as "7 2020" with unsrt; convert
    # them to the standard BibTeX month macros (printed "July 2020").  Format normalization only.
    MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    final, nmonth = re.subn(r'(\n[ \t]*month[ \t]*=[ \t]*)["{](\d{1,2})["}]',
                            lambda m: m.group(1) + MONTHS[int(m.group(2)) - 1], final)
    print('numeric month fields converted to macros:', nmonth)
    open(OUTBIB, 'w', encoding='utf-8').write(final)

    # ----------------------------------------------------------- aliases
    v1al = open(W + 'spec/key_aliases.tsv', encoding='utf-8').read().rstrip('\n').split('\n')
    lines = v1al[:]  # header + v1 rows verbatim
    seen = set(tuple(l.split('\t')[:2]) for l in v1al[1:])
    for a, k, o in aliases:
        if (a, k) in seen: continue
        seen.add((a, k)); lines.append('%s\t%s\t%s' % (a, k, o))
    open(OUTALIAS, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')

    # ----------------------------------------------------------- log
    with open(OUTLOG, 'w', encoding='utf-8') as fh:
        fh.write('key\tsource\tstatus\tmerged_key\tmatch\tnotes\n')
        for r in logrows: fh.write('\t'.join(r) + '\n')
    cnt = collections.Counter((r[1].split(':')[0], r[2]) for r in logrows)
    print('v1 entries:', len(ents['v1']))
    for k in sorted(cnt): print(k, cnt[k])
    print('merged total:', len(merged))
    print('alias rows:', len(lines) - 1)
    for l in log_uni: print('UNI', l)

if __name__ == '__main__':
    main()
