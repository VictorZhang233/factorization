"""Spec v2.3 (verify patch): build PART 10 of refs_merged_v2.bib from the INSPIRE records fetched by
fetch_additions_v23.py (checks/inspire_additions/<tag>.bib) plus three Crossref-verified manual entries.
Usage: python3 -I add_refs_v23.py INSPIRE_DIR OUTFILE
Normalizations as in build_refs_v2.py: arXiv-only @article -> @misc with howpublished = "arXiv:<eprint> [<class>]";
numeric month -> BibTeX month macro; non-ASCII -> LaTeX macros (only in Boer:2017hqr; mapped by TEXMAP, then asserted ASCII).
Not added (verification failed on INSPIRE and Crossref, 2026-10-11): Balaban CMP 116 (1988) 1 (0 INSPIRE hits; the
two other Balaban papers are added instead); Vladimirov, Generalized Functions in Mathematical Physics (Mir 1979)
(0 hits on INSPIRE, not on Crossref -> the Crossref-verified Vladimirov monograph of 2002 is cited instead);
Feichtner-Sturmfels, Port. Math. 62 (2005) 437 [math/0411260] (0 hits on INSPIRE and Crossref -> not cited).
"""
import sys, os, re
IND, OUT = sys.argv[1], sys.argv[2]
TAGS = ['Gribov1978', 'LeeZinnJustin1972a', 'LeeZinnJustin1972b', 'LeeZinnJustin1972c', 'ZinnJustin1975',
        'AppelquistCarazzone1975', 'BergereDeCalanMalbouisson1978', 'Balaban1987', 'Balaban1989',
        'MagnenRivasseauSeneor1993', 'SchoonderwoerdBakker1998a', 'SchoonderwoerdBakker1998b', 'ChouChen2022',
        'BecherHagerNeubertSchwienbacher2026', 'NakanishiOjima1990b', 'Meggiolaro1997', 'GiordanoMeggiolaro2006',
        'ChengEtAl2025', 'Radyushkin2019', 'Lindsay1984', 'BelitskySmirnov2026', 'BelitskyBorkSmirnov2025',
        'JackiwTempleton1981', 'Borinsky2023', 'Schultka2018', 'LNvRV1997', 'BMMS2019', 'Barcaro2026',
        'ZhouEtAl2022', 'LiuMa2008', 'ScimemiVladimirov2017', 'MoosVladimirov2020', 'ArkaniHamedHillmanMizera2022',
        'Henneaux1996', 'BHHS2000', 'HerrlichNierste1995', 'ChangLi2013', 'Li2022', 'BoerEtAl2017', 'LRS1983',
        'AybatCollinsQiuRogers2012', 'BhattacharyaCocuzzaMetz2020', 'MonahanNeumann2026', 'BuffingMulders2011',
        'BalitskyChirilli2009']
TEXMAP = {'\u00eb': '{\\"e}', '\u00e9': "{\\'e}", '\u00f6': '{\\"o}', '\u00fc': '{\\"u}', '\u00e4': '{\\"a}'}
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
out = []
out.append('% ======================================================================')
out.append('% PART 10: spec v2.3 verify-patch additions (INSPIRE-HEP, fetched 2026-10-11 by')
out.append('%   spec_v2/checks/fetch_additions_v23.py; built by add_refs_v23.py) and three Crossref-verified manual entries')
out.append('% ======================================================================')
out.append('')
keys = []
for t in TAGS:
    b = open(os.path.join(IND, t + '.bib'), encoding='utf-8').read().strip()
    assert b.count('@') == 1, t
    for ch, tex in TEXMAP.items():
        b = b.replace(ch, tex)
    assert all(ord(c) < 128 for c in b), ('non-ASCII in', t)
    m = re.match(r'@(\w+)\{([^,]+),', b)
    typ, key = m.group(1), m.group(2)
    keys.append(key)
    b = re.sub(r'month = "(\d+)"', lambda mm: 'month = ' + MONTHS[int(mm.group(1)) - 1], b)
    if typ == 'article' and 'journal =' not in b:
        ep = re.search(r'eprint = "([^"]+)"', b).group(1)
        pc = re.search(r'primaryClass = "([^"]+)"', b)
        hp = 'arXiv:%s [%s]' % (ep, pc.group(1)) if pc else 'arXiv:%s' % ep
        b = b.replace('@article{%s,' % key, '@misc{%s,\n    howpublished = "%s",' % (key, hp), 1)
    if key == 'Nakanishi:1990qm':
        # INSPIRE gives only the series volume; publisher/series from the INSPIRE journal field "World Sci.Lect.Notes Phys. 27"
        b = b.replace('    volume = "27",', '    series = "World Scientific Lecture Notes in Physics",\n    volume = "27",\n    publisher = "World Scientific",\n    address = "Singapore",')
    out.append(b)
    out.append('')
MANUAL = r'''@book{Hormander2003,
  author        = {H{\"o}rmander, Lars},
  title         = {{The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis}},
  series        = {Classics in Mathematics},
  publisher     = {Springer},
  address       = {Berlin, Heidelberg},
  year          = {2003},
  note          = {Reprint of the second (1990) edition},
  isbn          = {978-3-540-00662-6},
  doi           = {10.1007/978-3-642-61497-2}
}

@book{Vladimirov2002,
  author        = {Vladimirov, V. S.},
  title         = {{Methods of the Theory of Generalized Functions}},
  publisher     = {CRC Press},
  address       = {London},
  year          = {2002},
  doi           = {10.1201/9781482288162}
}

@article{NilssonPassare2013,
  author        = {Nilsson, Lisa and Passare, Mikael},
  title         = {{Mellin Transforms of Multivariate Rational Functions}},
  journal       = {J. Geom. Anal.},
  volume        = {23},
  number        = {1},
  pages         = {24--46},
  year          = {2013},
  doi           = {10.1007/s12220-011-9235-7}
}
'''
out.append(MANUAL)
open(OUT, 'w', encoding='utf-8').write('\n'.join(out))
print(len(keys) + 3, 'entries:', ', '.join(keys + ['Hormander2003', 'Vladimirov2002', 'NilssonPassare2013']))
