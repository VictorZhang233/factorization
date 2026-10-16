"""X2/T8: two-loop planar off-shell Sudakov vertex (scalar, d=4): regions, per-line approximators, (Com),(Abs),
meet closure, Hasse diagram, and the pattern expansion of r = prod_R (1-T_R) Gamma.
Lines: g1=k1, g2=k2, a1=p1-k2, a2=p1-k1-k2, b1=p2+k2, b2=p2+k1+k2.  Modes S<A,B<H (A=C1, B=C2).
Approximators = coordinate zeroing (REPORT Def. C.6, 'soft-first' convention):
coordinates k1+,k1-,k1T,k2+,k2-,k2T and M (= {m2, p1^-, p2^+}, the IR regulator)."""
import itertools, json, sys, os

REG = ['HH', 'HC1', 'HC2', 'C1C1', 'C2C2', 'HS', 'C1S', 'C2S', 'SS']
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
mode_of = {'H': 'H', 'C1': 'A', 'C2': 'B', 'S': 'S'}
def split(R):
    for a in ['H', 'C1', 'C2', 'S']:
        if R.startswith(a):
            return a, R[len(a):]
LM = {  # line modes per region
 'HH':   dict(g1='H', g2='H', a1='H', a2='H', b1='H', b2='H'),
 'HC1':  dict(g1='H', g2='A', a1='A', a2='H', b1='H', b2='H'),
 'HC2':  dict(g1='H', g2='B', a1='H', a2='H', b1='B', b2='H'),
 'C1C1': dict(g1='A', g2='A', a1='A', a2='A', b1='H', b2='H'),
 'C2C2': dict(g1='B', g2='B', a1='H', a2='H', b1='B', b2='B'),
 'HS':   dict(g1='H', g2='S', a1='A', a2='H', b1='B', b2='H'),
 'C1S':  dict(g1='A', g2='S', a1='A', a2='A', b1='B', b2='H'),
 'C2S':  dict(g1='B', g2='S', a1='A', a2='H', b1='B', b2='B'),
 'SS':   dict(g1='S', g2='S', a1='A', a2='A', b1='B', b2='B'),
}
M = 'M'
Z = {
 'HH':   dict(g1=set(), g2=set(), a1={M}, a2={M}, b1={M}, b2={M}),
 'HC1':  dict(g1=set(), g2=set(), a1=set(), a2={'k2-', 'k2T', M}, b1={'k2-', 'k2T', M}, b2={'k2-', 'k2T', M}),
 'HC2':  dict(g1=set(), g2=set(), a1={'k2+', 'k2T', M}, a2={'k2+', 'k2T', M}, b1=set(), b2={'k2+', 'k2T', M}),
 'C1C1': dict(g1=set(), g2=set(), a1=set(), a2=set(), b1={'k2-', 'k2T', M}, b2={'k1-', 'k1T', 'k2-', 'k2T', M}),
 'C2C2': dict(g1=set(), g2=set(), a1={'k2+', 'k2T', M}, a2={'k1+', 'k1T', 'k2+', 'k2T', M}, b1=set(), b2=set()),
 'HS':   dict(g1=set(), g2=set(), a1={'k2+', 'k2T'}, a2={'k2+', 'k2-', 'k2T', M}, b1={'k2-', 'k2T'}, b2={'k2+', 'k2-', 'k2T', M}),
 'C1S':  dict(g1=set(), g2=set(), a1={'k2+', 'k2T'}, a2={'k2+', 'k2T'}, b1={'k2-', 'k2T'}, b2={'k1-', 'k1T', 'k2+', 'k2-', 'k2T', M}),
 'C2S':  dict(g1=set(), g2=set(), a1={'k2+', 'k2T'}, a2={'k1+', 'k1T', 'k2+', 'k2-', 'k2T', M}, b1={'k2-', 'k2T'}, b2={'k2-', 'k2T'}),
 'SS':   dict(g1=set(), g2=set(), a1={'k2+', 'k2T'}, a2={'k1+', 'k1T', 'k2+', 'k2T'}, b1={'k2-', 'k2T'}, b2={'k1-', 'k1T', 'k2-', 'k2T'}),
}
order = {('S', 'A'), ('S', 'B'), ('S', 'H'), ('A', 'H'), ('B', 'H')}
def le_mode(a, b): return a == b or (a, b) in order
def le(R1, R2): return all(le_mode(LM[R1][l], LM[R2][l]) for l in LINES)
def meet_mode(a, b):
    if le_mode(a, b): return a
    if le_mode(b, a): return b
    return 'S'   # A ^ B = S
def meet(R1, R2):
    m = {l: meet_mode(LM[R1][l], LM[R2][l]) for l in LINES}
    for R in REG:
        if LM[R] == m: return R
    return None

ok = True
# poset & Hasse diagram
less = [(a, b) for a in REG for b in REG if a != b and le(a, b)]
cover = [(a, b) for (a, b) in less if not any((a, c) in less and (c, b) in less for c in REG)]
print("covering relations (Hasse edges):", len(cover))
for a, b in sorted(cover): print("   ", a, "<", b)
# meet closure for pairs with a common lower bound (all pinch sets contain the origin -> all pairs)
for a, b in itertools.combinations(REG, 2):
    m = meet(a, b)
    if m is None:
        print("   meet not in set:", a, b); ok = False
# (Abs): Z_{R^R'}(f) subset Z_R(f) U Z_R'(f) for incomparable R,R'
nabs = 0
for a, b in itertools.combinations(REG, 2):
    if le(a, b) or le(b, a): continue
    m = meet(a, b)
    for l in LINES:
        if not Z[m][l] <= (Z[a][l] | Z[b][l]):
            print(f"   (Abs) FAILS for {a},{b} (meet {m}) on line {l}: {Z[m][l]} not in {Z[a][l] | Z[b][l]}"); ok = False
    nabs += 1
print("incomparable pairs checked for (Abs):", nabs)
# idempotence/commutation automatic for coordinate zeroing. Also check the Abs consequence T_R T_R' = T_R T_meet T_R'.
# pattern expansion of r = prod_R (1 - T_R) Gamma: sum over subsets S of (-1)^|S| T_S Gamma, T_S = union of Z
patterns = {}
for k in range(len(REG) + 1):
    for S in itertools.combinations(REG, k):
        pat = tuple(tuple(sorted(set().union(*[Z[R][l] for R in S]) if S else set())) for l in LINES)
        patterns[pat] = patterns.get(pat, 0) + (-1)**k
nz = {p: c for p, c in patterns.items() if c != 0}
print(f"distinct zeroing patterns: {len(patterns)}; with nonzero coefficient in r: {len(nz)}")
# chain-expansion check of C_R via recursion vs product formula, on the level of patterns (exact)
def T_apply(R, expr):   # expr: dict pattern->coeff ; T_R unions Z_R into each line set
    out = {}
    for pat, c in expr.items():
        newp = tuple(tuple(sorted(set(pat[i]) | Z[R][LINES[i]])) for i in range(len(LINES)))
        out[newp] = out.get(newp, 0) + c
    return out
def add(e1, e2, s=1):
    out = dict(e1)
    for p, c in e2.items(): out[p] = out.get(p, 0) + s*c
    return {p: c for p, c in out.items() if c != 0}
Gamma = {tuple(() for _ in LINES): 1}
# topological order (smaller first)
topo = sorted(REG, key=lambda R: sum(1 for x in REG if le(x, R)))
C = {}
for R in topo:
    X = dict(Gamma)
    for R2 in REG:
        if R2 != R and le(R2, R): X = add(X, C[R2], -1)
    C[R] = T_apply(R, X)
rem = dict(Gamma)
for R in REG: rem = add(rem, C[R], -1)
print("recursion remainder == product-formula remainder:", rem == nz)
ok &= (rem == nz)
json.dump({'Z': {R: {l: sorted(Z[R][l]) for l in LINES} for R in REG},
           'C': {R: [[list(map(list, p)), c] for p, c in C[R].items()] for R in REG},
           'r': [[list(map(list, p)), c] for p, c in nz.items()]},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'twoloop_patterns.json'), 'w'))
print("ALL PASS" if ok else "SOME FAIL")
