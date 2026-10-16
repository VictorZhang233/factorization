"""X2 fix round 1 / r1_abs_naive.py -- (Abs) for the two-loop planar vertex under the soft-first convention (t8) and under
the literal convention of the reference (App. D, Def. D.18: the hard factor sees pi_+/pi_- of the EXACT jet momentum
entering H; Def. D.19: soft momenta are approximated only inside jet factors).  Supersedes the unscripted claim of
X2-Prop4.2 (review r1_2, F11).

Literal convention: the zeroing sets differ from soft-first exactly on four (region, line) entries (derivation):
  HS , a2 = pi_+(p1 - k2) - k1        = (P - k2+ - k1+, -k1-, -k1T)  -> zero {k2-, k2T, M}       (soft-first: + k2+)
  HS , b2 = pi_-(p2 + k2) + k1        = (k1+, -P' + k2-, k1T)        -> zero {k2+, k2T, M}       (soft-first: + k2-)
  C1S, b2 = pi_-(p2 + k2) + pi_+(k1)  = (k1+, -P' + k2-, 0)          -> zero {k1-, k1T, k2+, k2T, M} (soft-first: + k2-)
  C2S, a2 = pi_+(p1 - k2) - pi_-(k1)  = (P - k2+, -k1-, 0)           -> zero {k1+, k1T, k2-, k2T, M} (soft-first: + k2+)
(Abs): for incomparable R, R' with meet R^R':  Z_{R^R'}(f) subset Z_R(f) U Z_R'(f) for every line f."""
import os, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
Zsf = {R: {l: set(s) for l, s in d.items()} for R, d in json.load(open(os.path.join(HERE, 'twoloop_patterns.json')))['Z'].items()}
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
LM = {'HH': dict(g1='H', g2='H', a1='H', a2='H', b1='H', b2='H'), 'HC1': dict(g1='H', g2='A', a1='A', a2='H', b1='H', b2='H'),
      'HC2': dict(g1='H', g2='B', a1='H', a2='H', b1='B', b2='H'), 'C1C1': dict(g1='A', g2='A', a1='A', a2='A', b1='H', b2='H'),
      'C2C2': dict(g1='B', g2='B', a1='H', a2='H', b1='B', b2='B'), 'HS': dict(g1='H', g2='S', a1='A', a2='H', b1='B', b2='H'),
      'C1S': dict(g1='A', g2='S', a1='A', a2='A', b1='B', b2='H'), 'C2S': dict(g1='B', g2='S', a1='A', a2='H', b1='B', b2='B'),
      'SS': dict(g1='S', g2='S', a1='A', a2='A', b1='B', b2='B')}
order = {('S', 'A'), ('S', 'B'), ('S', 'H'), ('A', 'H'), ('B', 'H')}
lem = lambda a, b: a == b or (a, b) in order
le = lambda R1, R2: all(lem(LM[R1][l], LM[R2][l]) for l in LINES)
def meet(R1, R2):
    mm = lambda a, b: a if lem(a, b) else (b if lem(b, a) else 'S')
    m = {l: mm(LM[R1][l], LM[R2][l]) for l in LINES}
    return next(R for R in LM if LM[R] == m)
Zlit = {R: {l: set(s) for l, s in d.items()} for R, d in Zsf.items()}
Zlit['HS']['a2'] = {'k2-', 'k2T', 'M'}; Zlit['HS']['b2'] = {'k2+', 'k2T', 'M'}
Zlit['C1S']['b2'] = {'k1-', 'k1T', 'k2+', 'k2T', 'M'}; Zlit['C2S']['a2'] = {'k1+', 'k1T', 'k2-', 'k2T', 'M'}
for name, Z in [('soft-first (t8)', Zsf), ('literal App. D', Zlit)]:
    fails = []; npairs = 0
    for a, b in itertools.combinations(LM, 2):
        if le(a, b) or le(b, a): continue
        npairs += 1; m = meet(a, b)
        for l in LINES:
            extra = Z[m][l] - (Z[a][l] | Z[b][l])
            if extra: fails.append((a, b, m, l, sorted(extra)))
    print(f"{name}: incomparable pairs {npairs}, (Abs) failures {len(fails)}")
    for f in fails: print("    pair", f[:2], "meet", f[2], "line", f[3], "coordinate(s) zeroed by the meet but by neither region:", f[4])
