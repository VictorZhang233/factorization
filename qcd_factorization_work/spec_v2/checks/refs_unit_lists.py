"""Generate the per-unit citation lists of REFS_NOTES_v2.md Sec. 3 for the new v2 units.

Usage: python3 -I refs_unit_lists.py WORKDIR OUTFILE
Keys are taken from the frontier reports section by section (LAMET.md, YZLIU.md: keys cited in the section;
OTHERS.md: the section tables of its Appendix A) and from hand lists for Ch2 and App M/N/O/P/Q; every key is
mapped through key_aliases_v2.tsv to the merged key and checked against refs_merged_v2.bib.
"""
import re, sys, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bibparse import parse_bib
W = sys.argv[1].rstrip('/') + '/'
OUT = sys.argv[2]
bib = {e['key']: e for e in parse_bib(open(W + 'spec_v2/refs_merged_v2.bib', encoding='utf-8').read())}
alias = {}
for l in open(W + 'spec_v2/key_aliases_v2.tsv', encoding='utf-8').read().split('\n')[1:]:
    if l.strip():
        a, k = l.split('\t')[:2]
        alias.setdefault(a, k)
def m(k):
    k = k.strip()
    if k in bib: return k
    if k in alias and alias[k] in bib: return alias[k]
    return None
missing = []
def mm(keys):
    out = []
    for k in keys:
        r = m(k)
        if r is None: missing.append(k)
        elif r not in out: out.append(r)
    return out

def sections(text, level_re):
    """Return list of (heading, body) for headings matching level_re."""
    hs = [(mt.start(), mt.group(1)) for mt in re.finditer(level_re, text, re.M)]
    res = []
    for i, (p, h) in enumerate(hs):
        q = hs[i + 1][0] if i + 1 < len(hs) else len(text)
        res.append((h.strip(), text[p:q]))
    return res
keypat = re.compile(r'\b([A-Z][A-Za-z\-]+:\d{4}[a-z]{2,3})\b')

# ---- LAMET: top-level sections '## N. title'
lam = open(W + 'frontier/lamet/LAMET.md', encoding='utf-8').read()
lam_secs = sections(lam, r'^## (\d+\. [^\n]+)')
# ---- YZLIU: '### 3.A ...' blocks and '### 3.E', '### 3.F'
yz = open(W + 'frontier/yzliu/YZLIU.md', encoding='utf-8').read()
yz_secs = sections(yz, r'^### (3\.[A-F] [^\n]+)')
# ---- OTHERS appendix tables
ot = open(W + 'frontier/others/OTHERS.md', encoding='utf-8').read()
app = ot[ot.index('## Appendix A.'):ot.index('## Appendix B.')]
ot_secs = sections(app, r'^\*\*(§[^*]+)\*\*')

out = []
def block(title, keys, note=''):
    ks = mm(keys)
    out.append('**%s** (%d keys)%s\n\n%s\n' % (title, len(ks), (' — ' + note) if note else '', ', '.join('`%s`' % k for k in ks)))

out.append('### 3.1 Ch2 `qcd` (pedagogical QCD; v1 Ch2 keys plus the spec-v2 additions)\n')
block('gauge theory, colour, quarks', ['Yang:1954ek', 'Gell-Mann:1964ewy', 'Zweig:1964jf', 'Greenberg:1964pe', 'Han:1965pf', 'Fritzsch:1973pi'])
block('quantization, ghosts, BRST, unitarity', ['Faddeev:1967fc', 'BecchiRouetStora1975', 'BecchiRouetStora1976', 'Tyutin1975', 'KugoOjima1979', 'tHooft1971', 'Taylor1971', 'Slavnov1972', 'tHooftVeltman1972b'])
block('regularization, renormalization, RG', ['tHooftVeltman1972', 'tHooft1973', 'BardeenEtAl1978', 'Gell-Mann:1954yli', 'Callan:1970yg', 'Symanzik:1970rt', 'Collins1984', 'Joglekar:1975nu', 'Joglekar:1976eb', 'Joglekar:1976pe', 'Kluberg-Stern:1974iel', 'Henneaux:1993jn', 'DixonTaylor1974', 'Collins:1994ee', 'Hamberg:1991qt', 'Breitenlohner:1975hg', 'Breitenlohner:1976te'])
block('beta function, asymptotic freedom, alpha_s', ['GrossWilczek1973a', 'Politzer1973', 'Coleman:1973sx', 'Caswell1974', 'Jones1974', 'Tarasov:1980au', 'Larin:1993tp', 'vanRitbergen:1997va', 'Czakon:2004bu', 'Baikov:2016tgj', 'Herzog:2017ohr', 'Nielsen:1980sx', 'ParticleDataGroup:2024cfk'])
block('IR divergences and IR safety (introductory)', ['BlochNordsieck1937', 'Kinoshita1962', 'LeeNauenberg1964', 'StermanWeinberg1977', 'EllisRossTerrano1981'])
block('textbooks', ['PeskinSchroeder1995', 'Itzykson:1980rh', 'Weinberg1996', 'Muta2010', 'EllisStirlingWebber1996', 'Sterman1993', 'Collins2011', 'Wilson:1974sk'])

out.append('\n### 3.2 Ch22 `lamet` (keys cited in LAMET.md §1–§9; TMD sections go to Ch23)\n')
for h, body in lam_secs:
    n = int(h.split('.')[0])
    if 1 <= n <= 9:
        block('LAMET §' + h, sorted(set(keypat.findall(body)), key=str.lower))
out.append('\n### 3.3 Ch23 `yzliu` (YZLIU.md §3.A–§3.E and LAMET.md §10–§11)\n')
for h, body in yz_secs:
    if h.startswith('3.F'):
        continue
    block('YZLIU §' + h, sorted(set(keypat.findall(body)) | set(re.findall(r'`\[?([A-Z][A-Za-z\-]+:\d{4}[a-z]{2,3})\]?`', body)), key=str.lower),
          'E1–E2 (exponential decay, renormalization) are owned by Ch22' if h.startswith('3.E') else '')
for h, body in lam_secs:
    n = int(h.split('.')[0])
    if n in (10, 11):
        block('LAMET §' + h, sorted(set(keypat.findall(body)), key=str.lower))
for h, body in yz_secs:
    if h.startswith('3.F'):
        block('YZLIU §' + h + ' (owner Ch19 `excl`)', sorted(set(keypat.findall(body)) | set(re.findall(r'`\[?([A-Z][A-Za-z\-]+:\d{4}[a-z]{2,3})\]?`', body)), key=str.lower))

out.append('\n### 3.4 Ch24 `front` (OTHERS.md Appendix A sections; in brackets the v2 units that use the same keys)\n')
handoff = {'§0–1': 'Ch4, App D', '§2': 'App M, Ch21', '§3': 'Ch4, Ch15', '§4': 'Ch12, Ch16, Ch18', '§5': 'Ch21, Ch20', '§6': 'Ch14',
           '§7': 'Ch8', '§8': 'Ch2, Ch8, App J', '§9': 'Ch17', '§10': 'Ch18', '§11': 'Ch16', '§12': 'Ch20', '§13': 'Ch11'}
for h, body in ot_secs:
    keys = re.findall(r'^\| `([^`]+)` \|', body, re.M)
    tag = h.split()[0]
    if tag == '§0–1': keys = ['Gordan:1873'] + keys
    block('OTHERS ' + h + ' [' + handoff.get(tag, '') + ']', keys)

out.append('\n### 3.5 App M, App N, App O (refdoc S46–S48, S60)\n')
block('App M (OPE)', ['Zimmermann1969', 'Zimmermann1970', 'Zimmermann1973', 'LowensteinZimmermann1975', 'Lowenstein:1974qt', 'WilsonZimmermann1972', 'Wilson1969',
      'Anikin:1978tj', 'Zavyalov:1990kv', 'Smirnov:1990rz', 'Smirnov2002', 'Chetyrkin:1982zq', 'Joglekar:1975nu', 'Joglekar:1976eb', 'Joglekar:1976pe',
      'Hollands:2007zg', 'Hollands:2011gf', 'Frob:2016mzv', 'Collins:1994ee', 'Hamberg:1991qt', 'Falcioni:2022fdm', 'Gehrmann:2023ksf', 'Breitenlohner:1975hg',
      'Breitenlohner:1976te', 'Bostelmann:2005rr', 'Streater:1989vi', 'Jost:1965yxu', 'Haag:1958vt', 'Epstein1960', 'Markoff1916', 'Fredenhagen:1984bz'])
block('App N (subtraction)', ['Collins2011', 'CollinsSoperSterman1989', 'UsyukinaDavydychev1993a', 'Ma2020', 'Jantzen2011', 'Gardi:2024axt', 'Zimmermann1969', 'Breitenlohner:1975hg'])
block('App O (LCOPT, Glauber)', ['AybatSterman2009', 'Diehl:2015bca', 'RothsteinStewart2016', 'Bodwin1985', 'CollinsSoperSterman1985a', 'Kogut:1969xa', 'Chang:1973qi',
      'Ligterink:1994tm', 'Brodsky:1997de', 'Collins:2018aqt', 'Cheng:1969eh', 'Korchemskaya:1994qp', 'Korchemsky:1993hr', 'Caron-Huot:2013fea',
      'DoriaFrenkelTaylor1980', 'Andrasi:1980qw', 'DiLietoEtAl1981', 'Basu:1984ba', 'Schwartz:2018obd', 'Gaunt2014', 'Zeng:2015iba'])
block('App Q (errata candidates; sources only)', ['Ji:2020brr', 'JiEtAl2021', 'Su:2022fiu', 'Braun:2018brg', 'Ji:2019ewn', 'Liu:2022nnk', 'Ji:2021znw', 'Ji:2023pba',
      'Guo:2021ibg', 'Guo:2023pqw', 'BecherSchwartz2008', 'AybatRogers2011'])

with open(OUT, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
print('written', OUT)
print('keys not found (not printed):', sorted(set(missing)))
