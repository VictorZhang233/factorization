"""X2/T4: LP (tropical) certificates for the one-loop triangle: (H1),(H2) on the 2x2 cover, (H3), and the remainder norm.
Normalisation P = P' = 1/sqrt2 (Qt = 1); u = x/P = k^+/P, kap = kT^2; densities w.r.t. du dkap (rho~ = rho/sqrt2*sqrt2...):
  rG = v/((u m2 v + kap) * DG),  DG = (m2+u)(v(1+m2)+kap) + kap v,  v = 1-u          (0<u<1)
  rS = 1/((u m2 + kap)(m2+u))                                                           (u>0)
  rC1 = u m2/((u m2 v + kap)(u m2 + kap))  (0<u<1);   -1/(u (u m2 + kap))  (u>1)
  rC2 = -1/((m2+u+kap)(m2+u))                                                          (u>0)
  rH = -u/((u+kap)(u v + kap))  (0<u<1);   1/(u(u+kap))  (u>1)
Cover (s = lambda^theta, y = kap/(sqrt2 u) ~ kap/u):  U_S={u<=s, y<=s}, U_C1={s<u<=2, y<=s}, U_C2={u<=s, s<y<=1} u sliver,
U_H = rest.  Normalised logs: u=e^{L Xu}, kap=e^{L Xk}, v=e^{L Xv}, m2=e^{-L}, s=e^{-theta L/2}.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, numpy as np
from tropical import certify

u, v, kap, m2 = sp.symbols('u v kap m2', positive=True)
DG = (m2 + u)*(v*(1 + m2) + kap) + kap*v
F = {
 'G':  (v, [u*m2*v + kap, DG]),
 'S':  (sp.Integer(1), [u*m2 + kap, m2 + u]),
 'C1': (u*m2, [u*m2*v + kap, u*m2 + kap]),
 'C2': (sp.Integer(-1), [m2 + u + kap, m2 + u]),
 'H':  (-u, [u + kap, u*v + kap]),
}
Fbig = {
 'S':  (sp.Integer(1), [u*m2 + kap, m2 + u]),
 'C1': (sp.Integer(-1), [u, u*m2 + kap]),
 'C2': (sp.Integer(-1), [m2 + u + kap, m2 + u]),
 'H':  (sp.Integer(1), [u, u + kap]),
}

def combo(table, names_signs):
    """return (numerator polynomial N with v=1-u imposed, list of den factors (structural positive forms))"""
    dens = []
    for nm, sg in names_signs:
        for f in table[nm][1]:
            if not any(sp.simplify(f - g) == 0 for g in dens):
                dens.append(f)
    Dprod = sp.Mul(*dens)
    N = 0
    for nm, sg in names_signs:
        num, fl = table[nm]
        rest = sp.cancel(Dprod/sp.Mul(*fl))
        N += sg*num*rest
    N = sp.expand(N.subs(v, 1 - u))
    return N, dens

def run_item(label, table, names_signs, region, theta=1.0, eps=0.0):
    """region in {'I','II','III','IV'} sub-domains with extra cover constraints given as list of (coeffs dict, rhs)"""
    N, dens = combo(table, names_signs)
    return N, dens

def cert(label, N, dens, local, frozen, cons, eps=0.0):
    """local: list of local sympy vars (subset of u, v, kap); frozen: dict var->value substitution for O(1) vars
    (factor-level equivalence: bounded var replaced by 1); cons: list of (vector over local vars, rhs) for G X <= h."""
    # numerator in local variables: substitute u = 1 - v where u is frozen-to-1 region etc.
    Nl = N
    if v in local:            # region II: u = 1 - v
        Nl = sp.expand(N.subs(u, 1 - v))
    if u in local and v not in local:
        Nl = sp.expand(N)     # v already eliminated
    if kap not in local:
        raise ValueError
    # frozen vars in numerator: substitute value (they're O(1) there); keep monomial structure in local vars
    for var, val in frozen.items():
        Nl = Nl.subs(var, val)
    Nl = sp.expand(Nl)
    # den factors: replace frozen vars by 1 (equivalence within constants on the sub-domain)
    densl = []
    for f in dens:
        g = f
        for var in [u, v]:
            if var not in local:
                g = g.subs(var, 1)
        densl.append(sp.expand(g))
    n = len(local)
    w = [1]*n
    if eps:
        w[local.index(kap)] = 1 - eps
    G = [np.array(c, float) for c, _ in cons]; h = [float(r) for _, r in cons]
    return certify(Nl, local, m2, densl, G, h, wvec=w, label=label, verbose=True, top=3)

if __name__ == "__main__":
    th = 1.0   # s = lambda^theta
    t2 = th/2
    for eps in [0.0, 0.1]:
        print("="*100); print(f"eps = {eps}")
        res = {}
        # ---- remainder r ----
        N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
        # sub-domain I: 0<u<=1/2 : local (u,kap), Xu <= 0
        res['r_I'] = cert('r, 0<u<1/2', N, D, [u, kap], {}, [([1, 0], 0)], eps)
        res['r_II'] = cert('r, 1/2<u<1', N, D, [v, kap], {}, [([1, 0], 0)], eps)
        Nb, Db = combo(Fbig, [('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
        res['r_III'] = cert('r, u>1 (Xu>=0)', Nb, Db, [u, kap], {}, [([-1, 0], 0)], eps)
        # ---- (H1)_S : G - S on U_S = {Xu <= -t2, Xk - Xu <= -t2} ----
        N, D = combo(F, [('G', 1), ('S', -1)])
        res['H1_S'] = cert('(H1)_S: G-S on U_S', N, D, [u, kap], {}, [([1, 0], -t2), ([-1, 1], -t2)], eps)
        for nm in ['C1', 'C2', 'H']:
            N, D = combo(F, [(nm, 1)])
            res['H2_S_' + nm] = cert(f'(H2)_S: {nm} on U_S', N, D, [u, kap], {}, [([1, 0], -t2), ([-1, 1], -t2)], eps)
        # ---- (H1)_C1 : G - S - C1 on U_C1 : I-part {-t2 <= Xu <= 0, Xk - Xu <= -t2}, II-part {Xv<=0, Xk <= -t2}
        N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1)])
        res['H1_C1_I'] = cert('(H1)_C1 on U_C1, s<u<1/2', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)], eps)
        res['H1_C1_II'] = cert('(H1)_C1 on U_C1, 1/2<u<1', N, D, [v, kap], {}, [([1, 0], 0), ([0, 1], -t2)], eps)
        Nb, Db = combo(Fbig, [('S', -1), ('C1', -1)])
        res['H1_C1_III'] = cert('(H1)_C1 on U_C1, 1<u<2 (u frozen)', Nb, Db, [kap], {u: 1}, [([1], -t2)], eps)
        for nm in ['C2', 'H']:
            N, D = combo(F, [(nm, 1)])
            res['H2_C1_I_' + nm] = cert(f'(H2)_C1: {nm}, s<u<1/2', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([-1, 1], -t2)], eps)
            res['H2_C1_II_' + nm] = cert(f'(H2)_C1: {nm}, 1/2<u<1', N, D, [v, kap], {}, [([1, 0], 0), ([0, 1], -t2)], eps)
            Nb, Db = combo(Fbig, [(nm, 1)])
            res['H2_C1_III_' + nm] = cert(f'(H2)_C1: {nm}, 1<u<2', Nb, Db, [kap], {u: 1}, [([1], -t2)], eps)
        # ---- (H1)_C2 : G - S - C2 on U_C2 = {Xu <= -t2, -t2 <= Xk - Xu <= 0}
        N, D = combo(F, [('G', 1), ('S', -1), ('C2', -1)])
        res['H1_C2'] = cert('(H1)_C2 on U_C2 (u>0 part)', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)], eps)
        for nm in ['C1', 'H']:
            N, D = combo(F, [(nm, 1)])
            res['H2_C2_' + nm] = cert(f'(H2)_C2: {nm} on U_C2', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], t2), ([-1, 1], 0)], eps)
        # ---- (H1)_H : r on U_H = {Xu>=-t2, Xk-Xu>=-t2} u {Xu<=-t2, Xk-Xu>=0} u {u>2}; the u>1 part is r_III (whole).
        N, D = combo(F, [('G', 1), ('S', -1), ('C1', -1), ('C2', -1), ('H', -1)])
        res['H1_H_a'] = cert('(H1)_H: r on {s<u<1/2, y>s}', N, D, [u, kap], {}, [([1, 0], 0), ([-1, 0], t2), ([1, -1], t2)], eps)
        res['H1_H_b'] = cert('(H1)_H: r on {1/2<u<1, y>s}', N, D, [v, kap], {}, [([1, 0], 0), ([0, -1], t2)], eps)
        res['H1_H_c'] = cert('(H1)_H: r on {u<s, y>1}', N, D, [u, kap], {}, [([1, 0], -t2), ([1, -1], 0)], eps)
        print("\nSUMMARY eps=%g: item -> (exponent of lambda, power of L)" % eps)
        for k, (ph, d) in res.items():
            print(f"   {k:22s}: lambda^{-2*ph:.4f} L^{d}")
