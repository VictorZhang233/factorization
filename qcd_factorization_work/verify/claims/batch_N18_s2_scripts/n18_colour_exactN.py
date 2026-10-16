# N18 (stage-2 verifier): gluonic-pole strengths exactly in N, by a symbolic birdtrack (Fierz) engine.
# Method differs from stage 1 (explicit numerical SU(N) matrices for N=2..6): here the colour space of
# 2 upper (fundamental) and 2 lower (antifundamental) indices is spanned by the two pairings, the
# colour-charge operators act on pairings via the Fierz identity with N symbolic, and scalar products
# are N^{#cycles}.  Everything is exact rational functions of N.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

N = sp.symbols('N', positive=True)
CF = (N**2 - 1)/(2*N)
results = []
def check(name, cond, info=''):
    results.append(bool(cond))
    print(('PASS ' if cond else 'FAIL ') + name + (('   [' + info + ']') if info else ''))

# A colour tensor = dict {pairing: coeff}; a pairing = frozenset of (upper, lower) pairs.
# Legs: name -> ('u', idx) or ('l', idx).  Upper index = outgoing quark / incoming antiquark,
# lower index = incoming quark / outgoing antiquark (Catani-Seymour all-outgoing language).
def add(t, p, c):
    t[p] = sp.simplify(t.get(p, 0) + c)

def swap_upper(p, u1, u2):
    m = dict(p)  # upper -> lower
    m[u1], m[u2] = m[u2], m[u1]
    return frozenset(m.items())

def swap_lower(p, l1, l2):
    out = []
    for (u, l) in p:
        if l == l1: out.append((u, l2))
        elif l == l2: out.append((u, l1))
        else: out.append((u, l))
    return frozenset(out)

def contract_new(p, u, l):
    """sum over a common value of upper index u and lower index l of pairing p, then pair u-l (new deltas).
    Returns (factor, newpairing)."""
    m = dict(p)
    if m[u] == l:
        return N, p        # delta_{u l} contracted -> N, and the new delta_{u l} recreates the pairing
    # p contains (u, l_x) and (u_y, l); contraction gives delta_{u_y l_x}; new delta (u, l)
    lx = m[u]
    uy = [a for (a, b) in p if b == l][0]
    q = dict(m); q[uy] = lx; q[u] = l
    return 1, frozenset(q.items())

def TdotT(t, legs, i, j):
    """apply T_i . T_j (Catani-Seymour charges, upper: t, lower: -t^T) to colour tensor t."""
    (ki, ii), (kj, ij) = legs[i], legs[j]
    out = {}
    if i == j:                      # same leg: quadratic Casimir of the fundamental (or antifundamental)
        for p, c in t.items(): add(out, p, CF*c)
        return out
    for p, c in t.items():
        if ki == 'u' and kj == 'u':
            add(out, swap_upper(p, ii, ij), c/2); add(out, p, -c/(2*N))
        elif ki == 'l' and kj == 'l':
            add(out, swap_lower(p, ii, ij), c/2); add(out, p, -c/(2*N))
        else:
            u, l = (ii, ij) if ki == 'u' else (ij, ii)
            f, q = contract_new(p, u, l)
            add(out, q, -c*f/2); add(out, p, c/(2*N))
    return out

def cycles(p, q):
    # number of index loops in sum_{indices} delta(p) delta(q)  (both pair uppers with lowers)
    mp = dict(p); mq_inv = {l: u for (u, l) in q}
    seen = set(); n = 0
    for u in mp:
        if u in seen: continue
        n += 1; x = u
        while x not in seen:
            seen.add(x); x = mq_inv[mp[x]]
    return n

def inner(a, b):
    return sp.simplify(sum(ca*cb*N**cycles(pa, pb) for pa, ca in a.items() for pb, cb in b.items()))

def lin(*terms):
    t = {}
    for c, p in terms: add(t, p, c)
    return t

# ---------------- channels ----------------
# qq -> qq : a, b incoming quarks (lower), c, d outgoing quarks (upper)
legs_qq = {'a': ('l', 'a'), 'b': ('l', 'b'), 'c': ('u', 'c'), 'd': ('u', 'd')}
I_qq = frozenset({('c', 'a'), ('d', 'b')}); S_qq = frozenset({('c', 'b'), ('d', 'a')})
Mt_qq = lin((sp.Rational(1, 2), S_qq), (-1/(2*N), I_qq))     # t^x_{ca} t^x_{db}
Mu_qq = lin((sp.Rational(1, 2), I_qq), (-1/(2*N), S_qq))     # t^x_{da} t^x_{cb}
# q qbar -> q qbar : a incoming quark (lower), b incoming antiquark (upper), c outgoing quark (upper), d outgoing antiquark (lower)
legs_qa = {'a': ('l', 'a'), 'b': ('u', 'b'), 'c': ('u', 'c'), 'd': ('l', 'd')}
P1 = frozenset({('c', 'a'), ('b', 'd')}); P2 = frozenset({('c', 'd'), ('b', 'a')})
Mt_qa = lin((sp.Rational(1, 2), P2), (-1/(2*N), P1))          # t^x_{ca} t^x_{bd}
Ms_qa = lin((sp.Rational(1, 2), P1), (-1/(2*N), P2))          # t^x_{ba} t^x_{cd}

# colour conservation sum_k T_k |M> = 0, checked via <M'|T_k.(sum_j T_j)|M> = 0 for every k
def conserved(M, legs):
    ok = True
    for k in legs:
        tot = {}
        for j in legs:
            for p, c in TdotT(M, legs, k, j).items(): add(tot, p, c)
        for M2 in (M,):
            ok = ok and sp.simplify(inner(M2, tot)) == 0
        # stronger: all coefficients vanish
        ok = ok and all(sp.simplify(c) == 0 for c in tot.values())
    return ok
for name, M, legs in [('Mt_qq', Mt_qq, legs_qq), ('Mu_qq', Mu_qq, legs_qq), ('Mt_qa', Mt_qa, legs_qa), ('Ms_qa', Ms_qa, legs_qa)]:
    check('colour conservation sum_j T_k.T_j |%s> = 0 for every k (exact in N)' % name, conserved(M, legs))

# Casimir sanity: T_k.T_k = C_F on every leg
for k in legs_qq:
    tt = TdotT(Mt_qq, legs_qq, k, k)
    check('T_%s.T_%s = C_F on Mt_qq' % (k, k), all(sp.simplify(tt.get(p, 0) - CF*Mt_qq.get(p, 0)) == 0 for p in set(tt) | set(Mt_qq)))

# ---------------- pole rule and C_G ----------------
# P = sum_out T - sum_{in, != a} T ; per-attachment factor  C_X/C_u = <M|(-T_a).(sigma_X T_X)|M'> / (C_F <M|M'>)
def att(M, Mp, legs, X, sigma):
    return sp.simplify(sigma*(-1)*inner(M, TdotT(Mp, legs, 'a', X))/(CF*inner(M, Mp)))

def CG(M, Mp, legs, outs, ins):
    return sp.simplify(sum(att(M, Mp, legs, X, +1) for X in outs) + sum(att(M, Mp, legs, X, -1) for X in ins))

def TaTb(M, Mp, legs):
    return sp.simplify(inner(M, TdotT(Mp, legs, 'a', 'b'))/inner(M, Mp))

chan = {
  'qq tt*': (Mt_qq, Mt_qq, legs_qq), 'qq uu*': (Mu_qq, Mu_qq, legs_qq), 'qq tu*': (Mt_qq, Mu_qq, legs_qq),
  'qqbar tt*': (Mt_qa, Mt_qa, legs_qa), 'qqbar ss*': (Ms_qa, Ms_qa, legs_qa), 'qqbar st*': (Ms_qa, Mt_qa, legs_qa)}
bbmp = {'qq tt*': (N**2-5)/(N**2-1), 'qq uu*': (N**2-5)/(N**2-1), 'qq tu*': -(N**2+3)/(N**2-1),
        'qqbar tt*': -(N**2-3)/(N**2-1), 'qqbar ss*': (N**2+1)/(N**2-1), 'qqbar st*': (N**2+1)/(N**2-1)}
tatb_claim = {'qq tt*': -1/N, 'qq uu*': -1/N, 'qq tu*': -(N**2+1)/(2*N), 'qqbar tt*': -(N**2-2)/(2*N),
              'qqbar ss*': 1/(2*N), 'qqbar st*': 1/(2*N)}
for k, (M, Mp, legs) in chan.items():
    cg = CG(M, Mp, legs, ['c', 'd'], ['b'])
    tab = TaTb(M, Mp, legs)
    closed = sp.simplify(1 + 2*tab/CF)
    check('%-10s pole-rule C_G = %s = BBMP Table I value' % (k, sp.factor(cg)), sp.simplify(cg - bbmp[k]) == 0)
    check('%-10s <T_a.T_b> = %s (claimed %s); closed formula 1+2<TaTb>/C_F = pole rule' % (k, sp.factor(tab), tatb_claim[k]),
          sp.simplify(tab - tatb_claim[k]) == 0 and sp.simplify(closed - cg) == 0)
    print('      SU(3):', cg.subs(N, 3))

# SIDIS and DY limits
# SIDIS: only a (incoming quark, lower) and c (outgoing quark, upper): M = delta_{ca}; C_G = <(-T_a).T_c>/C_F
legs_sidis = {'a': ('l', 'a'), 'c': ('u', 'c'), 'x': ('u', 'x'), 'y': ('l', 'y')}   # x,y: spectator pair kept as a colour singlet
M_sidis = lin((1, frozenset({('c', 'a'), ('x', 'y')})))
cg_sidis = sp.simplify(-inner(M_sidis, TdotT(M_sidis, legs_sidis, 'a', 'c'))/(CF*inner(M_sidis, M_sidis)))
check('SIDIS: C_G = <(-T_a).T_c>/C_F = +1', sp.simplify(cg_sidis - 1) == 0)
# DY: a incoming quark (lower), b incoming antiquark (upper), colour singlet annihilation: M = delta_{ba}
legs_dy = {'a': ('l', 'a'), 'b': ('u', 'b'), 'x': ('u', 'x'), 'y': ('l', 'y')}
M_dy = lin((1, frozenset({('b', 'a'), ('x', 'y')})))
cg_dy = sp.simplify(+inner(M_dy, TdotT(M_dy, legs_dy, 'a', 'b'))/(CF*inner(M_dy, M_dy)))   # incoming b: sigma=-1 => <(-T_a).(-T_b)>
check('DY: C_G = <T_a.T_b>/C_F = -1 (Collins sign flip)', sp.simplify(cg_dy + 1) == 0)

# ---------------- QVY Table I, graph by graph (all 24 entries) ----------------
# QVY normalisation: C_u = <M|M'>/N^2 ; C_X = C_u * (per-attachment factor);  F1 = line of momentum P1, F2 = P2.
# Diagram (1) qq'->qq' t-channel: P1 = parton on the polarized quark's line (c), P2 = d.  (2) uu*: same jets, the
# u-channel connects a to d.  (3) tu*.  (4) q qbar' t-channel: P1 = outgoing quark c, P2 = outgoing antiquark d.
# (5) q qbar -> q' qbar' s-channel; (6) st* interference.  (P1 = quark jet c, P2 = antiquark jet d in 4-6.)
qvy = {
 1: dict(Cu=(N**2-1)/(4*N**2), CI=-1/(2*N**2), CF1=-1/(4*N**2), CF2=(N**2-2)/(4*N**2)),
 2: dict(Cu=(N**2-1)/(4*N**2), CI=-1/(2*N**2), CF1=(N**2-2)/(4*N**2), CF2=-1/(4*N**2)),
 3: dict(Cu=-(N**2-1)/(4*N**3), CI=(N**2+1)/(4*N**3), CF1=1/(4*N**3), CF2=1/(4*N**3)),
 4: dict(Cu=(N**2-1)/(4*N**2), CI=-(N**2-2)/(4*N**2), CF1=-1/(4*N**2), CF2=1/(2*N**2)),
 5: dict(Cu=(N**2-1)/(4*N**2), CI=1/(4*N**2), CF1=(N**2-2)/(4*N**2), CF2=1/(2*N**2)),
 6: dict(Cu=-(N**2-1)/(4*N**3), CI=-1/(4*N**3), CF1=1/(4*N**3), CF2=-(N**2+1)/(4*N**3)),
}
diag = {1: (Mt_qq, Mt_qq, legs_qq), 2: (Mu_qq, Mu_qq, legs_qq), 3: (Mt_qq, Mu_qq, legs_qq),
        4: (Mt_qa, Mt_qa, legs_qa), 5: (Ms_qa, Ms_qa, legs_qa), 6: (Ms_qa, Mt_qa, legs_qa)}
nmatch = 0
for d, (M, Mp, legs) in diag.items():
    Cu = sp.simplify(inner(M, Mp)/N**2)
    CI = sp.simplify(Cu*att(M, Mp, legs, 'b', -1))
    C1 = sp.simplify(Cu*att(M, Mp, legs, 'c', +1))
    C2 = sp.simplify(Cu*att(M, Mp, legs, 'd', +1))
    got = dict(Cu=Cu, CI=CI, CF1=C1, CF2=C2)
    for key in ('Cu', 'CI', 'CF1', 'CF2'):
        ok = sp.simplify(got[key] - qvy[d][key]) == 0
        nmatch += ok
        check('QVY Table I diagram (%d) %-3s = %s' % (d, key, sp.factor(got[key])), ok)
check('all 24 QVY Table I entries reproduced exactly in N', nmatch == 24)
# ratios for diagram (1)
r = [sp.factor(sp.simplify(qvy[1][k]/qvy[1]['Cu'])) for k in ('CI', 'CF1', 'CF2')]
check('QVY diagram (1) ratios C_I/C_u, C_F1/C_u, C_F2/C_u = -2/(N^2-1), -1/(N^2-1), (N^2-2)/(N^2-1)',
      sp.simplify(r[0] + 2/(N**2-1)) == 0 and sp.simplify(r[1] + 1/(N**2-1)) == 0 and sp.simplify(r[2] - (N**2-2)/(N**2-1)) == 0,
      'got %s; SU(3): %s' % (r, [x.subs(N, 3) for x in r]))
# QVY eq. (28): sum = (N^2-5)/(4N^2)
check('QVY eq.(28): C_I+C_F1+C_F2 (diagram 1) = (N^2-5)/(4N^2)', sp.simplify(sum(qvy[1][k] for k in ('CI', 'CF1', 'CF2')) - (N**2-5)/(4*N**2)) == 0)
# the sum over graphs/C_u equals BBMP for every diagram
for d, k in zip(range(1, 7), ['qq tt*', 'qq uu*', 'qq tu*', 'qqbar tt*', 'qqbar ss*', 'qqbar st*']):
    s = sp.simplify((qvy[d]['CI'] + qvy[d]['CF1'] + qvy[d]['CF2'])/qvy[d]['Cu'])
    check('QVY diagram (%d): (C_I+C_F1+C_F2)/C_u = BBMP C_G[%s]' % (d, k), sp.simplify(s - bbmp[k]) == 0)

# QVY eqs (25)-(27) recomputed literally as colour traces (independent of the pole rule):
# (1/N) Tr(T^b T^c T^a)(T^b T^c)_{ij} = C_I T^a_ij etc.  Check with explicit SU(3) and SU(4) matrices numerically.
import numpy as np
def gellmann(n):
    gens = []
    for i in range(n):
        for j in range(i+1, n):
            m = np.zeros((n, n), complex); m[i, j] = m[j, i] = 1; gens.append(m/2)
            m = np.zeros((n, n), complex); m[i, j] = -1j; m[j, i] = 1j; gens.append(m/2)
    for k in range(1, n):
        m = np.zeros((n, n), complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        gens.append(m/np.sqrt(2*k*(k+1)))
    return gens
for n in (3, 4):
    T = gellmann(n)
    def coef(fun):
        # fun(a) -> matrix ; extract c with fun(a) = c T^a
        cs = []
        for a in range(len(T)):
            M = fun(a); cs.append(np.trace(M @ T[a]).real/0.5)
        return np.mean(cs), np.std(cs)
    cI = coef(lambda a: sum(np.trace(T[b] @ T[c] @ T[a]) * (T[b] @ T[c]) for b in range(len(T)) for c in range(len(T)))/n)
    c1 = coef(lambda a: sum(np.trace(T[b] @ T[c]) * (T[b] @ T[a] @ T[c]) for b in range(len(T)) for c in range(len(T)))/n)
    c2 = coef(lambda a: sum(np.trace(T[b] @ T[a] @ T[c]) * (T[b] @ T[c]) for b in range(len(T)) for c in range(len(T)))/n)
    check('QVY eqs (25)-(27) literal traces, SU(%d): C_I=%.6f C_F1=%.6f C_F2=%.6f' % (n, cI[0], c1[0], c2[0]),
          abs(cI[0] + 1/(2*n**2)) < 1e-12 and abs(c1[0] + 1/(4*n**2)) < 1e-12 and abs(c2[0] - (n**2-2)/(4*n**2)) < 1e-12)

# BBMP's own link algebra: C_G of combinations with C_G[U+]=1, C_G[U-]=-1, C_G[U box U+]=3, C_G[Tr(U box)U+/N]=1
links = {
 'qq tt*': ((N**2+1)*1 - 2*3)/(N**2-1),
 'qq tu*': N/(N**2-1)*(2*N*1 - (N**2+1)/N*3),
 'qqbar ss*': (N**2*1 - (-1))/(N**2-1),
 'qqbar tt*': (1 + (N**2-2)*(-1))/(N**2-1),
 'qqbar st*': N/(N**2-1)*(N*1 - (1/N)*(-1)),
}
for k, v in links.items():
    check('BBMP gauge-link combination (eqs. QuarkQuark/QuarkAntiquark + Table I upper) gives C_G[%s]' % k, sp.simplify(v - bbmp[k]) == 0)
# normalisation of BBMP links (all reduce to 1 at zero field)
norms = [((N**2+1) - 2)/(N**2-1), N/(N**2-1)*(2*N - (N**2+1)/N), (N**2 - 1)/(N**2-1), (1 + N**2-2)/(N**2-1), N/(N**2-1)*(N - 1/N)]
check('BBMP links normalised to 1 at zero field', all(sp.simplify(x - 1) == 0 for x in norms))

# large N
for k in bbmp:
    print('   large-N limit of C_G[%s] = %s' % (k, sp.limit(bbmp[k], N, sp.oo)))

print('\nSUMMARY: %d/%d checks passed' % (sum(results), len(results)))
