"""X2 fix round 2 / r2_twoloop_regulator.py -- scaling structure of the 50 zeroing patterns of the two-loop planar
remainder r = prod_R (1 - T_R) Gamma (soft-first; twoloop_patterns.json), with and without analytic line regulators
(review r2_2 F1; corrects X2-Thm4.3(i)).

Coordinates: weights d = (d1p, d1m, d1T, d2p, d2m, d2T) of (k1+, k1-, |k1T|, k2+, k2-, |k2T|); m2 has weight mu.
A pattern is homogeneous along (d, mu) iff every line factor -V^2 = -2 V+ V- + |V_T|^2 (with the zeroed components
removed) has all its monomials of equal weight w_l(d, mu).  K = {d : mu = 0} (m2-independent scalings) is a linear
space; the full family is an affine space over K (when mu = 1 is solvable).
Weights of integrand x measure (d = 4 - 2 eps, line powers nu_l = 1 + delta_l):
    W(d) = d1p + d1m + d2p + d2m + (2 - 2 eps)(d1T + d2T) - sum_l nu_l w_l(d).
D0 := W at eps = 0, delta = 0.  For d in K:  W(d) = D0(d) - 2 eps (d1T + d2T) - sum_l delta_l w_l(d).
Checks: (1) D0 = 0 on the whole family; (2) dim K per pattern; (3) the subspace K0 = {d in K : eps-weight 0}
(exact, eps-independent invariances: not regulated by DR); (4) with generic analytic regulators the weight map
Phi: K -> R^7, d -> (-2(d1T+d2T), -w_g1(d), ..., -w_b2(d)) is injective (every exact invariance acquires a non-zero
weight), so every composite is exactly scaleless with non-zero weight in DR + generic analytic regularization;
(5) singles: K = 0 (unique scaling), m2 exponent -k_R eps (and -k_R eps - l_R(delta) with regulators)."""
import sys, os, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
pats = json.load(open(os.path.join(HERE, 'twoloop_patterns.json')))
LINES = ['g1', 'g2', 'a1', 'a2', 'b1', 'b2']
CONT = {'g1': (None, 1, 0), 'g2': (None, 0, 1), 'a1': ('p1', 0, -1), 'a2': ('p1', -1, -1),
        'b1': ('p2', 0, 1), 'b2': ('p2', 1, 1)}
D = sp.symbols('d1p d1m d1T d2p d2m d2T')
mu = sp.Symbol('mu')
eps = sp.Symbol('epsilon')
dl = {l: sp.Symbol('delta_' + l) for l in LINES}

def line_monomials(line, Z):
    ext, c1, c2 = CONT[line]
    d1p, d1m, d1T, d2p, d2m, d2T = D
    Vp, Vm, VT = [], [], []
    if ext == 'p1':
        Vp.append(sp.Integer(0))                 # p1+ = P (weight 0)
        if 'M' not in Z: Vm.append(mu)           # p1- = -m2/2P
    if ext == 'p2':
        if 'M' not in Z: Vp.append(mu)           # p2+ = m2/2P'
        Vm.append(sp.Integer(0))                 # p2- = -P'
    if c1:
        if 'k1+' not in Z: Vp.append(d1p)
        if 'k1-' not in Z: Vm.append(d1m)
        if 'k1T' not in Z: VT.append(d1T)
    if c2:
        if 'k2+' not in Z: Vp.append(d2p)
        if 'k2-' not in Z: Vm.append(d2m)
        if 'k2T' not in Z: VT.append(d2T)
    return [xp + xm for xp in Vp for xm in Vm] + [t1 + t2 for t1 in VT for t2 in VT]

def analyse(p):
    Z = {LINES[i]: set(p[i]) for i in range(6)}
    mons = {l: line_monomials(l, Z[l]) for l in LINES}
    eqs = []
    for l in LINES:
        for mm in mons[l][1:]:
            eqs.append(sp.expand(mm - mons[l][0]))
    rows = [[sp.expand(e).coeff(v) for v in D] + [sp.expand(e).coeff(mu)] for e in eqs]
    M = sp.Matrix(rows) if rows else sp.zeros(0, 7)
    # homogeneous with mu = 1 ?  solve M[:, :6] d = -M[:, 6]
    A, b = M[:, :6], -M[:, 6]
    try:
        sol, par = A.gauss_jordan_solve(b)
        homog = True
    except ValueError:
        homog = False
    if not homog:
        return dict(homog=False)
    Kb = A.nullspace()
    wl = lambda vec, muv: {l: (mons[l][0].subs(dict(zip(D, vec))).subs(mu, muv) if mons[l] else 0) for l in LINES}
    def W(vec, muv, with_reg):
        w = wl(vec, muv)
        meas = vec[0] + vec[1] + vec[3] + vec[4] + (2 - 2*eps)*(vec[2] + vec[5])
        tot = meas - sum((1 + (dl[l] if with_reg else 0))*w[l] for l in LINES)
        return sp.expand(tot)
    s0 = list(sol.subs({q: 0 for q in par})) if par.shape[0] else list(sol)
    D0_part = W(s0, 1, False).subs(eps, 0)
    D0_K = [W(list(kv), 0, False).subs(eps, 0) for kv in Kb]
    epsw_part = sp.expand(W(s0, 1, False)).coeff(eps)
    # weight map Phi on K
    Phi = []
    for kv in Kb:
        Wr = W(list(kv), 0, True)
        Phi.append([Wr.coeff(eps)] + [Wr.coeff(dl[l]) for l in LINES])
    PhiM = sp.Matrix(Phi) if Phi else sp.zeros(0, 7)
    rank_phi = PhiM.rank() if Phi else 0
    eps_row = sp.Matrix([[r[0]] for r in Phi]) if Phi else sp.zeros(0, 1)
    rank_eps = eps_row.rank() if Phi else 0
    # explicit zero-eps-weight directions (basis of K0)
    K0 = []
    if Phi:
        coeffs = sp.Matrix([[r[0] for r in Phi]])           # eps-weights of the basis vectors, 1 x dimK
        for nvec in coeffs.nullspace():
            K0.append([sp.simplify(sum(nvec[i]*Kb[i][j] for i in range(len(Kb)))) for j in range(6)])
    return dict(homog=True, dimK=len(Kb), D0_part=sp.simplify(D0_part), D0_K=[sp.simplify(z) for z in D0_K],
                epsw_part=sp.simplify(epsw_part), rank_phi=rank_phi, dimK0=len(Kb) - rank_eps, K0=K0,
                Phi=Phi, regw_part=sp.expand(W(s0, 1, True) - W(s0, 1, False)))

res = []
for p, c in pats['r']:
    res.append((p, c, analyse(p)))
nonh = [r for r in res if not r[2]['homog']]
hom = [r for r in res if r[2]['homog']]
singles = [r for r in hom if r[2]['dimK'] == 0]
comps = [r for r in hom if r[2]['dimK'] > 0]
print(f"patterns: {len(res)}; not homogeneous: {len(nonh)} (Gamma itself: {all(all(len(z) == 0 for z in r[0]) for r in nonh)})")
print(f"D0 = 0 on every family (particular solution and all kernel directions): "
      f"{all(r[2]['D0_part'] == 0 and all(z == 0 for z in r[2]['D0_K']) for r in hom)}")
print(f"singles (dim K = 0, unique scaling): {len(singles)};  composites (dim K >= 1): {len(comps)}")
print("   singles: coefficient, m2-exponent coefficient of eps (= -k_R), extra m2-exponent with line regulators:")
for p, c, a in singles:
    print(f"      coeff {c:+d}  eps-weight {a['epsw_part']}   regulator part {a['regw_part']}   pattern {p}")
print("   distribution of dim K over the composites:", dict(sorted(Counter(a['dimK'] for _, _, a in comps).items())))
print("   distribution of dim K0 (exact eps-INDEPENDENT invariances):", dict(sorted(Counter(a['dimK0'] for _, _, a in comps).items())))
n_unreg = sum(1 for _, _, a in comps if a['dimK0'] > 0)
print(f"   composites with an exact eps-independent invariance (dim K0 >= 1): {n_unreg}")
print(f"   composites with a direction of non-zero eps-weight (DR-scaleless): {sum(1 for _, _, a in comps if a['dimK0'] < a['dimK'])}")
inj = all(a['rank_phi'] == a['dimK'] for _, _, a in comps)
print(f"   weight map Phi: K -> (eps, delta_g1..delta_b2) injective for every composite: {inj}")
print("   => with generic independent analytic powers 1+delta_l on the six lines, no composite retains an exact invariance of")
print("      zero weight; each is exactly homogeneous under a scaling of non-zero weight, hence 0 in DR + analytic reg.")
print("\nexamples of exact eps-independent invariances (basis of K0) and their weight with line regulators:")
shown = 0
for p, c, a in comps:
    if a['dimK0'] > 0 and shown < 6:
        for vec in a['K0'][:1]:
            # regulator weight of this direction
            Wr = None
            Z = {LINES[i]: set(p[i]) for i in range(6)}
            mons = {l: line_monomials(l, Z[l]) for l in LINES}
            w = {l: (mons[l][0].subs(dict(zip(D, vec))).subs(mu, 0) if mons[l] else 0) for l in LINES}
            regw = -sum(dl[l]*w[l] for l in LINES)
            print(f"   coeff {c:+d}, dim K = {a['dimK']}, dim K0 = {a['dimK0']}: direction (d1p,d1m,d1T,d2p,d2m,d2T) = {vec};"
                  f" weight with regulators {sp.simplify(regw)}")
            print(f"        zeroing: {dict(zip(LINES, p))}")
        shown += 1
json.dump([dict(pattern=p, coeff=c, homog=a['homog'], dimK=a.get('dimK'), dimK0=a.get('dimK0'),
                rank_phi=a.get('rank_phi'), epsw=str(a.get('epsw_part'))) for p, c, a in res],
          open(os.path.join(os.path.dirname(HERE), 'logs', 'r2_twoloop_regulator.json'), 'w'), indent=1)
