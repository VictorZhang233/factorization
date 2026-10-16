"""X2 final2 -- f2v_UF_polytopes.py: INDEPENDENT re-implementation (imports no other f2_* script) of the polynomial and
polytope data behind Prop E.4 and Prop E.5 of X2-subtraction_final2.md.

What is recomputed, and how (different code path from f2_twoloop_polytopes.py / f2_E4_singles.py):
 (1) line factors of the nine singles from the REGION SCALING (leading monomials of -V^2 under the mode weights
     H=(0,0,0), C1=(0,2,1), C2=(2,0,1), S=(2,2,2) for (+,-,T), with weight 2 for m^2), compared with the coordinate
     zeroing of twoloop_patterns.json (Thm E.3(ii): zeroed line factor = leading part);
 (2) U, F of all 49 non-trivial patterns by completing the square in light-cone variables:
       S = sum_l x_l D_l = -2 k+^T M k- + b+.k+ + b-.k- + kT^T A kT + C,
       U = det M,  F = C det M + (1/2) b-^T adj(M) b+,
     with the checks: no (k+)^2, (k-)^2, linear kT or x-y mixed terms; det M == det A (single power U^{-d/2});
 (3) positivity: every coefficient (polynomial in the x_l) is, after P' = Qt2/(2P), a P-independent polynomial in
     (Qt2, m2) with positive coefficients;
 (4) Newton polytope of G = U + F: affine dimension; for the composites the dimension of the lineality space
     (quasi-homogeneities) is compared with dim K of Thm E.3(i) (counts 18, 15, 6, 1 for dim K = 1, 2, 3, 4);
 (5) singles: all facets of Newt(G) by exact enumeration (every facet contains 6 affinely independent support points),
     primitive inward normals mu, nu = min <mu, .>; the nu = 0 facets; the discrete set Z_R near eps = 0;
 (6) singles at delta = 0, Feynman (projective) form J = int x^{a-1} U^{|a|-3t} F^{2t-|a|}, t = 2 - eps:
     the divergence certificates (rays r with B(r) = 0, A(r) >= 0) of the seven singles, recomputed exactly from
     the supports; the SS relative-interior certificate on (0, 1);
 (7) the full planar and crossed vertex: U, F, positivity, exact relative-interior certificate for (1/2)(1,...,1) in
     Newt(F) with lambda_min, and the coordinate-difference graph (Prop E.5).
Run: python3 -I f2v_UF_polytopes.py  (log: ../final2_logs/f2v_UF_polytopes.log; json: ../final2_logs/f2v_UF_polytopes.json)
"""
import sys, os, json, itertools
from fractions import Fraction as Fr
from math import gcd
from functools import reduce
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import functools
print = functools.partial(print, flush=True)

HERE = os.path.dirname(os.path.abspath(__file__))
PAT = json.load(open(os.path.join(os.path.dirname(HERE), 'scripts', 'twoloop_patterns.json')))
LOGDIR = os.path.join(os.path.dirname(HERE), 'final2_logs')

P, Pp, m2, Qt2 = sp.symbols('P Pp m2 Qt2', positive=True)
kp = sp.symbols('kp1 kp2', real=True); km = sp.symbols('km1 km2', real=True)
kx = sp.symbols('kx1 kx2', real=True); ky = sp.symbols('ky1 ky2', real=True)
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
XS = sp.symbols('y_g1 y_g2 y_a1 y_a2 y_b1 y_b2', positive=True)
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

# momenta as dicts of light-cone components; p1 = (P, -m2/2P, 0), p2 = (m2/2P', -P', 0)
def mom(plus, minus, x, y): return {'+': sp.sympify(plus), '-': sp.sympify(minus), 'x': sp.sympify(x), 'y': sp.sympify(y)}
def lin(*terms):
    out = mom(0, 0, 0, 0)
    for c, v in terms:
        for key in out: out[key] += c*v[key]
    return out
def sq(v): return sp.expand(2*v['+']*v['-'] - v['x']**2 - v['y']**2)
K = [mom(kp[i], km[i], kx[i], ky[i]) for i in range(2)]
def p1(mm): return mom(P, -mm/(2*P), 0, 0)
def p2(mm): return mom(mm/(2*Pp), -Pp, 0, 0)

def line_mom(name, k1, k2, mm):
    return {'g1': k1, 'g2': k2, 'a1': lin((1, p1(mm)), (-1, k2)), 'a2': lin((1, p1(mm)), (-1, k1), (-1, k2)),
            'b1': lin((1, p2(mm)), (1, k2)), 'b2': lin((1, p2(mm)), (1, k1), (1, k2))}[name]

def zeroed_factor(name, zset):
    mm = 0 if 'M' in zset else m2
    def zk(i):
        tag = f'k{i+1}'
        return mom(0 if tag + '+' in zset else kp[i], 0 if tag + '-' in zset else km[i],
                   0 if tag + 'T' in zset else kx[i], 0 if tag + 'T' in zset else ky[i])
    return sp.expand(-sq(line_mom(name, zk(0), zk(1), mm)))

MODE_W = {'H': (0, 0, 0), 'C1': (0, 2, 1), 'C2': (2, 0, 1), 'S': (2, 2, 2)}
def leading_factor(name, R):
    """leading part of -V^2 under the region scaling of R = (mode k1, mode k2); m2 has weight 2"""
    modes = {'HH': ('H', 'H'), 'HC1': ('H', 'C1'), 'HC2': ('H', 'C2'), 'C1C1': ('C1', 'C1'), 'C2C2': ('C2', 'C2'),
             'HS': ('H', 'S'), 'C1S': ('C1', 'S'), 'C2S': ('C2', 'S'), 'SS': ('S', 'S')}[R]
    lam = sp.Symbol('lam', positive=True)
    sub = {}
    for i in range(2):
        w = MODE_W[modes[i]]
        sub[kp[i]] = lam**w[0]*kp[i]; sub[km[i]] = lam**w[1]*km[i]
        sub[kx[i]] = lam**w[2]*kx[i]; sub[ky[i]] = lam**w[2]*ky[i]
    sub[m2] = lam**2*m2
    full = sp.expand(-sq(line_mom(name, K[0], K[1], m2)))
    scaled = sp.expand(full.xreplace(sub))
    pol = sp.Poly(scaled, lam)
    low = min(m[0] for m in pol.monoms())
    return sp.expand(pol.coeff_monomial(lam**low))

def UF(factors):
    S = sp.expand(sum(x*f for x, f in zip(XS, factors)))
    allk = list(kp) + list(km) + list(kx) + list(ky)
    pol = sp.Poly(S, *allk)
    # structural checks
    bad = []
    for mon, c in zip(pol.monoms(), pol.coeffs()):
        e = dict(zip(allk, mon)); deg = sum(mon)
        npl = e[kp[0]] + e[kp[1]]; nmi = e[km[0]] + e[km[1]]; nx = e[kx[0]] + e[kx[1]]; ny = e[ky[0]] + e[ky[1]]
        if deg == 2 and not ((npl == 1 and nmi == 1) or nx == 2 or ny == 2): bad.append(mon)
        if deg == 1 and (nx or ny): bad.append(mon)
        if deg > 2: bad.append(mon)
    M = sp.Matrix(2, 2, lambda i, j: -sp.Rational(1, 2)*pol.coeff_monomial(kp[i]*km[j]))
    A = sp.Matrix(2, 2, lambda i, j: (pol.coeff_monomial(kx[i]**2) if i == j else pol.coeff_monomial(kx[0]*kx[1])/2))
    Ay = sp.Matrix(2, 2, lambda i, j: (pol.coeff_monomial(ky[i]**2) if i == j else pol.coeff_monomial(ky[0]*ky[1])/2))
    bp = sp.Matrix([pol.coeff_monomial(kp[i]) for i in range(2)])
    bm = sp.Matrix([pol.coeff_monomial(km[i]) for i in range(2)])
    C = pol.coeff_monomial(1)
    U = sp.expand(M.det())
    F = sp.expand(C*U + (bm.T*M.adjugate()*bp)[0, 0]/2)
    struct_ok = (not bad) and sp.expand(A - Ay) == sp.zeros(2, 2)
    return U, F, sp.expand(A.det()), struct_ok

def coeff_positive(E):
    """every coefficient in the y's is, after Pp = Qt2/(2P), a P-free polynomial in (Qt2, m2) with positive coeffs"""
    E2 = sp.expand(E.subs(Pp, Qt2/(2*P)))
    for c in sp.Poly(E2, *XS).coeffs():
        c = sp.cancel(sp.together(c))
        if c.has(P): return False
        num, den = sp.fraction(c)
        pd = sp.Poly(den, Qt2, m2)
        if len(pd.coeffs()) != 1 or pd.coeffs()[0] <= 0: return False      # positive monomial denominator
        if not all(t > 0 for t in sp.Poly(sp.expand(num), Qt2, m2).coeffs()): return False
    return True

def supp(E): return sorted(set(sp.Poly(E, *XS).monoms()))

def rank_q(rows):
    M = [[Fr(v) for v in r] for r in rows]; rk = 0
    ncol = len(M[0]) if M else 0
    for col in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]/M[rk][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        rk += 1
    return rk
def affdim(pts): return 0 if len(pts) < 2 else rank_q([[a - b for a, b in zip(p, pts[0])] for p in pts[1:]])

def kernel_q(rows, n):
    """basis of {y : rows.y = 0} over Q"""
    M = [[Fr(v) for v in r] for r in rows]; piv = []; rk = 0
    for col in range(n):
        p_ = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if p_ is None: continue
        M[rk], M[p_] = M[p_], M[rk]; pv = M[rk][col]; M[rk] = [a/pv for a in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col]; M[i] = [a - f*b for a, b in zip(M[i], M[rk])]
        piv.append(col); rk += 1
    free = [c for c in range(n) if c not in piv]; basis = []
    for fc in free:
        y = [Fr(0)]*n; y[fc] = Fr(1)
        for r, pc in enumerate(piv): y[pc] = -M[r][fc]
        basis.append(y)
    return basis

def primitive(v):
    den = reduce(lambda a, b: a*b//gcd(a, b), [x.denominator for x in v], 1)
    iv = [int(x*den) for x in v]; g = reduce(gcd, [abs(x) for x in iv if x != 0], 0) or 1
    return tuple(x//g for x in iv)

def facets_exact(pts):
    """all facets of conv(pts) (full-dimensional in R^n): {mu (primitive, inward): nu}"""
    n = len(pts[0]); out = {}
    for sub in itertools.combinations(range(len(pts)), n):
        Q = [pts[i] for i in sub]
        if affdim(Q) != n - 1: continue
        ker = kernel_q([[a - b for a, b in zip(q, Q[0])] for q in Q[1:]], n)
        if len(ker) != 1: continue
        mu = primitive(ker[0])
        vals = [sum(a*b for a, b in zip(mu, p)) for p in pts]
        nu0 = sum(a*b for a, b in zip(mu, Q[0]))
        if all(v >= nu0 for v in vals): out[mu] = nu0
        elif all(v <= nu0 for v in vals): out[tuple(-a for a in mu)] = -nu0
    return out

def h(S, r): return max(sum(a*b for a, b in zip(v, r)) for v in S)

# ------------------------------------------------------------------------------------------------ (1) line factors
print("(1) line factors of the nine singles: region-scaling leading part vs coordinate zeroing")
Z = PAT['Z']; SINGLES = ['HH', 'HC1', 'HC2', 'C1C1', 'C2C2', 'HS', 'C1S', 'C2S', 'SS']
lf_ok = True
for R in SINGLES:
    for ln in LINES:
        a_ = zeroed_factor(ln, Z[R][ln]); b_ = leading_factor(ln, R)
        if sp.expand(a_ - b_) != 0:
            lf_ok = False; print(f"      mismatch {R} {ln}: zeroed {a_}  leading {b_}")
report("for all 9 singles x 6 lines, the zeroed line factor equals the leading part under the region scaling", lf_ok)

# ------------------------------------------------------------------------------------------------ (2)-(4) all patterns
print("\n(2)-(4) U, F of the 49 non-trivial patterns (light-cone completion of the square)")
def key(pz): return tuple(tuple(sorted(z)) for z in pz)
single_key = {key([Z[R][ln] for ln in LINES]): R for R in SINGLES}
pats = [pz for pz, c in PAT['r'] if any(len(z) for z in pz)]
report(f"number of non-trivial patterns = {len(pats)} (expected 49), of which singles {sum(key(p) in single_key for p in pats)} (expected 9)",
       len(pats) == 49 and sum(key(p) in single_key for p in pats) == 9)
DATA = {}; comp_stats = {}
struct_all = pos_all = True
for pz in pats:
    fac = [zeroed_factor(ln, z) for ln, z in zip(LINES, pz)]
    U, F, detA, sok = UF(fac)
    single = single_key.get(key(pz))
    struct_all &= sok and U != 0 and sp.expand(U - detA) == 0
    pos = coeff_positive(U) and coeff_positive(F)
    pos_all &= pos
    G = sp.expand(U + F); SG = supp(G); dm = affdim(SG)
    lineality = 6 - dm
    if single is None:
        comp_stats[lineality] = comp_stats.get(lineality, 0) + 1
    DATA[str(key(pz))] = dict(single=single, U=str(U), F=str(F), dimG=dm)
report("structure: only k+k-, kx^2, ky^2 quadratic terms, x/y transverse blocks equal, det M = det A_T != 0 (all 49)", struct_all)
report("positivity: all coefficients of U and F are P-free polynomials in (Qt2, m2) with positive coefficients (all 49)", pos_all)
report(f"composites: dimension of the lineality space of Newt(U+F) -> counts {dict(sorted(comp_stats.items()))} "
       f"(Thm E.3(i): dim K = 1, 2, 3, 4 for 18, 15, 6, 1)", comp_stats == {1: 18, 2: 15, 3: 6, 4: 1})

# ------------------------------------------------------------------------------------------------ (5) singles: facets
print("\n(5) singles: facets of Newt(U+F) (exact enumeration), nu = 0 facets, Z_R near eps = 0")
SDATA = {}
for R in SINGLES:
    fac = [zeroed_factor(ln, Z[R][ln]) for ln in LINES]
    U, F, detA, sok = UF(fac)
    G = sp.expand(U + F); SG = supp(G)
    fcts = facets_exact(SG)
    nu0 = sorted(mu for mu, nu in fcts.items() if nu == 0)
    crit = all(sum(mu) >= 1 for mu in nu0)
    unit = all(sorted(mu) == [0, 0, 0, 0, 0, 1] for mu in nu0)
    Zset = set()
    for mu, nu in fcts.items():
        if nu == 0: continue
        s1 = sum(mu)
        for nn in range(0, 60):
            e = Fr(-nn - s1 + 2*nu, nu)
            if abs(e) <= 1: Zset.add(e)
    zs = sorted(Zset)
    near = [z for z in zs if abs(z) < Fr(1, 3)]
    # LP-form convergence interval at delta = 0 (BFP Thm 2.2, sufficient): <mu,1> > nu (2 - eps) for all facets
    lo, hi = Fr(-10**9), Fr(10**9)
    for mu, nu in fcts.items():
        s1 = sum(mu)
        if nu > 0: lo = max(lo, Fr(2*nu - s1, nu))
        elif nu < 0: hi = min(hi, Fr(2*nu - s1, nu))
        elif s1 <= 0: lo, hi = Fr(1), Fr(0)
    SDATA[R] = dict(U=U, F=F, SU=supp(U), SF=supp(F), facets=fcts)
    report(f"{R}: |supp G| = {len(SG)}, dim = {affdim(SG)}, facets = {len(fcts)}, nu=0 facets = {len(nu0)} "
           f"(all unit vectors: {unit}); <mu,1> >= 1 on nu=0 facets: {crit}; Z_R in [-1,1] = {[str(z) for z in zs]}; "
           f"Z_R in (-1/3,1/3) = {[str(z) for z in near]}; LP-form interval at delta=0: "
           f"{'(' + str(lo) + ', ' + str(hi) + ')' if lo < hi else 'empty'}",
           affdim(SG) == 6 and crit and set(near) <= {Fr(0)})

# ------------------------------------------------------------------------------------------------ (6) pure-DR divergence
print("\n(6) delta = 0, projective form: psi_eps(r) = A(r) + eps B(r), A = <1,r> - 2 h_F(r), B = 3 h_U(r) - 2 h_F(r)")
CERT = {'HC1': (1, -1, -1, 1, 0, 0), 'C1C1': (0, 0, -1, -1, 1, 1), 'HS': (1, -1, 0, 1, -1, 0),
        'C1S': (1, -1, 0, 0, -1, 1), 'HC2': (1, -1, 0, 0, -1, 1), 'C2C2': (0, 0, 1, 1, -1, -1),
        'C2S': (1, -1, -1, 1, 0, 0)}
# NB: the coordinate order of the archived rays is (g1, g2, a1, a2, b1, b2), the same as here
for R, r in CERT.items():
    SU, SF = SDATA[R]['SU'], SDATA[R]['SF']
    A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
    # also the sharper statement: the integrand is asymptotically CONSTANT along r (A = B = 0) or growing (A > 0)
    report(f"{R}: ray {r}: A = {A}, B = {B}  ->  psi_eps(r) = {A} for every eps: divergent for all eps", B == 0 and A >= 0)
# search for an independent certificate for each of the seven (smallest-norm ray with B = 0, A >= 0)
for R in CERT:
    SU, SF = SDATA[R]['SU'], SDATA[R]['SF']
    found = []
    for r in itertools.product([-1, 0, 1], repeat=6):
        if len(set(r)) == 1: continue
        A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
        if B == 0 and A >= 0: found.append((r, A))
    print(f"      {R}: rays in {{-1,0,1}}^6 with B = 0, A >= 0: {len(found)}; e.g. {found[:3]}")
# SS: relative-interior certificate for eps in (0,1)
SU, SF = SDATA['SS']['SU'], SDATA['SS']['SF']
report(f"SS: U is the monomial y_g1 y_g2: {SU == [(1, 1, 0, 0, 0, 0)]}", SU == [(1, 1, 0, 0, 0, 0)])
def in_hull_lp(p, S, strict):
    """exact certificate that p lies in conv(S) (strict=True: with all weights > 0, i.e. in the relative interior when
    S affinely spans its hull); scipy LP for a candidate, then an exact rational repair; returns weights or None"""
    import numpy as np
    from scipy.optimize import linprog
    n_ = len(S); d_ = len(S[0])
    Aeq = np.array([[s[i] for s in S] for i in range(d_)] + [[1]*n_], float)
    beq = np.array([float(x) for x in p] + [1.0])
    if strict:
        c = np.zeros(n_ + 1); c[-1] = -1
        Aub = np.hstack([-np.eye(n_), np.ones((n_, 1))]); bub = np.zeros(n_)
        res = linprog(c, A_ub=Aub, b_ub=bub, A_eq=np.hstack([Aeq, np.zeros((d_ + 1, 1))]), b_eq=beq,
                      bounds=[(0, None)]*n_ + [(None, 1)], method='highs')
        if not res.success or res.x[-1] <= 1e-9: return None
        lamf = res.x[:n_]
    else:
        res = linprog(np.zeros(n_), A_eq=Aeq, b_eq=beq, bounds=[(0, None)]*n_, method='highs')
        if not res.success: return None
        lamf = np.maximum(res.x, 0.0)
    act = [i for i in range(n_) if lamf[i] > 1e-10] if not strict else list(range(n_))
    order = sorted(act, key=lambda i: -lamf[i]); basis = []
    for i in order:
        if affdim([S[j] for j in basis + [i]]) == len(basis): basis.append(i)
    for den in (10**3, 10**5, 10**8):
        lam = {i: Fr(0) for i in range(n_)}
        for i in act:
            if i not in basis: lam[i] = Fr(float(lamf[i])).limit_denominator(den)
        rhs = [Fr(x) for x in p] + [Fr(1)]
        for i in act:
            if i in basis: continue
            for k in range(d_): rhs[k] -= lam[i]*S[i][k]
            rhs[d_] -= lam[i]
        Mx = sp.Matrix([[S[b][k] for b in basis] for k in range(d_)] + [[1]*len(basis)])
        try:
            sol, params = Mx.gauss_jordan_solve(sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in rhs]))
        except ValueError:
            continue
        if params.shape[0]: sol = sol.subs({t: 0 for t in params})
        for j, b in enumerate(basis):
            q = sp.Rational(sol[j]); lam[b] = Fr(int(q.p), int(q.q))
        exact = (sum(lam.values()) == 1 and all(sum(lam[i]*S[i][k] for i in range(n_)) == Fr(p[k]) for k in range(d_)))
        sign = all(v > 0 for v in lam.values()) if strict else all(v >= 0 for v in lam.values())
        if exact and sign: return lam
    return None
def a_SS(e):   # (1 + 3 e (e_g1 + e_g2)) / (2 + 2 e) in the coordinate order (g1, g2, a1, a2, b1, b2)
    return [Fr(1 + 3*e, 1)/(2 + 2*e) if i < 2 else Fr(1)/(2 + 2*e) for i in range(6)]
lam_mid = in_hull_lp(a_SS(Fr(1, 3)), SF, True); lam0 = in_hull_lp(a_SS(Fr(0)), SF, False); lam1 = in_hull_lp(a_SS(Fr(1)), SF, False)
report(f"SS: a(1/3) in relint Newt(F) (min weight {min(lam_mid.values()) if lam_mid else None}); a(0), a(1) in Newt(F): "
       f"{lam0 is not None}, {lam1 is not None}  =>  J_SS converges absolutely for 0 < eps < 1", lam_mid and lam0 and lam1)
# SS: divergence outside (0,1): rays
for r in [(-1, 0, -1, -1, -1, -1), (-1, -1, -1, -1, 0, 0)]:
    A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
    print(f"      SS: ray {r}: A = {A}, B = {B}: psi >= 0 for eps {'>= ' + str(Fr(-A, B)) if B > 0 else '<= ' + str(Fr(-A, B))}")
SU, SF = SDATA['HH']['SU'], SDATA['HH']['SF']
for r in [(-1, 0, -1, -1, 0, -1), (-1, 0, 0, -1, 0, -1)]:
    A = sum(r) - 2*h(SF, r); B = 3*h(SU, r) - 2*h(SF, r)
    print(f"      HH: ray {r}: A = {A}, B = {B}: psi >= 0 for eps {'>= ' + str(Fr(-A, B)) if B > 0 else '<= ' + str(Fr(-A, B))}")

# ------------------------------------------------------------------------------------------------ (7) full vertices
print("\n(7) full planar and crossed two-loop vertex: U, F, positivity, relint certificate, coordinate graph")
FULL = {}
for kind in ['planar', 'crossed']:
    k1, k2 = K
    if kind == 'planar':
        V = [k1, k2, lin((1, p1(m2)), (-1, k2)), lin((1, p1(m2)), (-1, k1), (-1, k2)), lin((1, p2(m2)), (1, k2)),
             lin((1, p2(m2)), (1, k1), (1, k2))]
    else:
        V = [k1, k2, lin((1, p1(m2)), (-1, k1)), lin((1, p1(m2)), (-1, k1), (-1, k2)), lin((1, p2(m2)), (1, k2)),
             lin((1, p2(m2)), (1, k1), (1, k2))]
    fac = [sp.expand(-sq(v)) for v in V]
    U, F, detA, sok = UF(fac)
    pos = coeff_positive(U) and coeff_positive(F)
    SU, SF = supp(U), supp(F)
    FULL[kind] = dict(U=U, F=F, SU=SU, SF=SF)
    lam = in_hull_lp([Fr(1, 2)]*6, SF, True)
    lmin = min(lam.values()) if lam else None
    edges = set()
    for f_, g_ in itertools.permutations(SF, 2):
        dlt = [a - b for a, b in zip(f_, g_)]
        if sorted(dlt) == [-1, 0, 0, 0, 0, 1]: edges.add(frozenset((dlt.index(1), dlt.index(-1))))
    complete = len(edges) == 15
    report(f"{kind}: structure {sok}, det M = det A_T: {sp.expand(U - detA) == 0}, positivity {pos}, |supp U| = {len(SU)}, "
           f"|supp F| = {len(SF)}, affdim supp F = {affdim(SF)}; (1/2)1 in relint Newt(F) with exact weights, "
           f"lambda_min = {lmin}; coordinate graph complete (diameter 1): {complete}",
           sok and pos and lam is not None and complete and affdim(SF) == 5)
    if lam:
        # the bound of Prop E.5: eps_0 = lambda_min / (6 D), D = 1
        print(f"      => eps_0 = lambda_min/6 = {lmin/6}  (exact weights: {sorted(set(lam.values()))})")
json.dump({R: dict(U=str(d['U']), F=str(d['F']), facets={str(k): v for k, v in d['facets'].items()}) for R, d in SDATA.items()},
          open(os.path.join(LOGDIR, 'f2v_UF_polytopes.json'), 'w'), indent=1)
print("\nALL CHECKS PASS" if ALL_OK else "\nSOME CHECK FAILED")
