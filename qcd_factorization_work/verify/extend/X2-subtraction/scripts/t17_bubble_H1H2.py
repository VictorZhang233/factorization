"""X2/T17: bubble-chain class, (H1)/(H2) items on the 2x2 cover of T4 (s = lambda), for Gamma^(j) = l^j/(Dg D1 D2).
Shell forms (0<u<1, P=P'=1/sqrt2, densities w.r.t. du dkap):
  Gamma^(j) = lD^j rG ;  C_S^(j) = le^j rS ;  C_C1^(j) = lD^j a1 - le^j a2,  a1 = 1/(u(u m2 v+kap)), a2 = 1/(u(u m2+kap));
  C_C2^(j) = lh^j rC2 ;  C_H^(j) = -lt^j b1 + lh^j b2,  b1 = 1/(u(uv+kap)), b2 = 1/(u(u+kap)).
Each item is rewritten as  l_ref^j * (rational item of T4)  +  sum (l_a^j - l_b^j) * (rational),  and
|l_a^j - l_b^j| <= j (C L(1+|X|))^{j-1} min(ratio_ab, C L(1+|X|)).  Every piece is LP-certified (exponent >= 1 needed)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import monomials_of, positive_form, lp_max_psi

u, v, kap, m2 = sp.symbols('u v kap m2', positive=True)
DG = (m2 + u)*(v*(1 + m2) + kap) + kap*v
R_ = {  # rational pieces as (num, [positive den factors])
 'rG': (v, [u*m2*v + kap, DG]), 'rS': (sp.Integer(1), [u*m2 + kap, m2 + u]),
 'a1': (sp.Integer(1), [u, u*m2*v + kap]), 'a2': (sp.Integer(1), [u, u*m2 + kap]),
 'rC2': (sp.Integer(-1), [m2 + u + kap, m2 + u]),
 'b1': (sp.Integer(1), [u, u*v + kap]), 'b2': (sp.Integer(1), [u, u + kap]),
}
# log-difference ratio weights  |l_a - l_b| <= w_ab  (rational upper bounds), plus the alternative 1 (x L)
W = {('D', 'e'): (u, [v]), ('t', 'h'): (u, [v]), ('D', 'h'): (u*(m2*v + kap), [v, kap]), ('e', 'h'): (u*m2, [kap]),
     ('D', 't'): (u*m2*v, [kap])}

def combine(items):
    dens = []
    for _, (n, ds) in items:
        for f in ds:
            if not any(sp.expand(f - g) == 0 for g in dens): dens.append(f)
    D = sp.Mul(*dens); N = 0
    for s, (n, ds) in items: N += s*n*sp.cancel(D/sp.Mul(*ds))
    return sp.expand(N), dens

def expo(num, dens, region, cons):
    if region == 'I':
        N = sp.expand(num.subs(v, 1 - u)); loc = [u, kap]; dl = [sp.expand(f.subs(v, 1)) for f in dens]
    else:
        N = sp.expand(num.subs(u, 1 - v)); loc = [v, kap]; dl = [sp.expand(f.subs(u, 1)) for f in dens]
    if N == 0: return np.inf
    mons = monomials_of(N, loc, m2); forms = [positive_form(g, loc, m2) for g in dl]
    G = [np.array(c, float) for c, _ in cons]; h = [float(r) for _, r in cons]
    best = -np.inf
    for c, a in mons:
        val, X, res = lp_max_psi(a, forms, [1, 1], G, h, 2)
        best = max(best, val)
    return -2*best

def piece(items, region, cons, weight=None):
    """exponent of |sum items| possibly times a log-difference weight (best of ratio and L alternatives)."""
    num, dens = combine(items)
    e_L = expo(num, dens, region, cons)
    if weight is None: return e_L
    wn, wd = W[weight]
    e_r = expo(sp.expand(wn*num), list(wd) + list(dens), region, cons)
    return max(e_L, e_r)

# items: list of (main rational items, [(log pair, rational items), ...])
ITEMS = {
 '(H1)_S  G-S':        ([(1, R_['rG']), (-1, R_['rS'])], [(('D', 'e'), [(1, R_['rG'])])]),
 '(H2)_S  C_C1':       ([(1, R_['a1']), (-1, R_['a2'])], [(('D', 'e'), [(1, R_['a1'])])]),
 '(H2)_S  C_C2':       ([(1, R_['rC2'])], []),
 '(H2)_S  C_H':        ([(-1, R_['b1']), (1, R_['b2'])], [(('t', 'h'), [(1, R_['b1'])])]),
 '(H1)_C1 G-S-C1':     ([(1, R_['rG']), (-1, R_['rS']), (-1, R_['a1']), (1, R_['a2'])],
                        [(('D', 'e'), [(1, R_['rG']), (-1, R_['a1'])])]),
 '(H1)_C2 G-S-C2':     ([(1, R_['rG']), (-1, R_['rS']), (-1, R_['rC2'])],
                        [(('D', 'h'), [(1, R_['rG'])]), (('e', 'h'), [(1, R_['rS'])])]),
 # alternative: reference l_e:  l_e^j (G-S-C2) + (l_e^j - l_h^j) C2 + (l_D^j - l_e^j) G
 '(H1)_C2 alt':        ([(1, R_['rG']), (-1, R_['rS']), (-1, R_['rC2'])],
                        [(('e', 'h'), [(1, R_['rC2'])]), (('D', 'e'), [(1, R_['rG'])])]),
}
TH = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
t2 = TH/2
REGIONS = {   # cover sets in normalised logs (Xu or Xv, Y=Xk-Xu): list of (region, constraints); s = lambda^TH
 'U_S':  [('I', [([1, 0], -t2), ([-1, 1], -t2)])],
 'U_C1': [('I', [([1, 0], 0.0), ([-1, 0], t2), ([-1, 1], -t2)]), ('II', [([1, 0], 0.0), ([0, 1], -t2)])],
 'U_C2': [('I', [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0.0)])],
}
CHECK = {'U_S': ['(H1)_S  G-S', '(H2)_S  C_C1', '(H2)_S  C_C2', '(H2)_S  C_H'],
         'U_C1': ['(H1)_C1 G-S-C1', '(H2)_S  C_C2', '(H2)_S  C_H'],
         'U_C2': ['(H1)_C2 G-S-C2', '(H1)_C2 alt', '(H2)_S  C_C1', '(H2)_S  C_H']}

if __name__ == "__main__":
    worst = np.inf
    for U, names in CHECK.items():
        for nm in names:
            main, corr = ITEMS[nm]
            for (region, cons) in REGIONS[U]:
                es = [piece(main, region, cons)]
                for (pair, its) in corr:
                    es.append(piece(its, region, cons, weight=pair))
                e = min(es); worst = min(worst, e)
                print(f"{U:5s} {nm:18s} region {region}: piece exponents {['%.2f' % x for x in es]} -> lambda^{e:.2f}", flush=True)
    print(f"minimal certified exponent over all (H1)/(H2) items (log-insertion class, any j): {worst:.3f}")
