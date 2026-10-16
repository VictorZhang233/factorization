# Independent check of the A-side quadrant formulas (Lemma L3 of the report):
# k2^- integral by residues in the UPPER half plane (sympy, exact), then k1^- integral by mpmath quadrature on R.
# (The formula was derived closing contours in the opposite way / by sectors; agreement checks the i0 bookkeeping.)
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp, sympy as sp
from twoexch_model import jet_params, F_A_terms, I
mp.mp.dps = 25
lam = 1.0
sc = lambda v: (lam*v[0], lam*v[1])
k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
pa = jet_params(lam, 0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
eta = sp.Rational(1, int(sys.argv[1]) if len(sys.argv) > 1 else 20)
k1, k2 = sp.symbols('k1 k2')
P = {k: sp.nsimplify(round(float(v), 12)) for k, v in pa.items()}
A1 = sp.nsimplify(round(a1, 12)); A2 = sp.nsimplify(round(a2, 12))
def JA(col):
    den3 = (P['al1'] - k2 + sp.I*eta) if col == '12' else (P['al2'] - k1 + sp.I*eta)
    return sp.I**3 / ((k1 + k2 - P['beta'] + sp.I*eta) * (P['al0'] - k1 - k2 + sp.I*eta) * den3)
def check(y, x, col):
    y = sp.nsimplify(y); x = sp.nsimplify(x)
    f = JA(col) / ((2*y*k1 - A1 + sp.I*eta) * (2*x*k2 - A2 + sp.I*eta))
    num, den = sp.fraction(sp.together(f))
    # poles in k2 for generic real k1: roots of den in k2 (linear factors)
    facs = sp.factor_list(sp.expand(den), k2)[1]
    g = 0
    for (fac, mult) in facs:
        if sp.degree(fac, k2) == 1:
            root = sp.solve(fac, k2)[0]
            # pole is in UHP iff Im(root) > 0 for real k1: imaginary part independent of k1
            imr = sp.im(root.subs(k1, 0))
            if imr > 0:
                g += sp.residue(f, k2, root)
    g = 2*sp.pi*sp.I*g
    gl = sp.lambdify(k1, g, 'mpmath')
    # breakpoints: real parts of k1-poles of g
    num1, den1 = sp.fraction(sp.together(g))
    rts = [complex(r) for r in sp.Poly(sp.expand(den1), k1).nroots()]
    bps = sorted(set([mp.mpf(r.real) for r in rts]))
    pts = [-mp.inf] + [b + d for b in bps for d in (-0.2, -0.05, 0, 0.05, 0.2)] + [mp.inf]
    pts = sorted(set(pts))
    val = mp.quad(gl, pts) / (2*mp.pi)**2
    terms = F_A_terms(mp.mpf(float(y)), pa, a1, a2, mp.mpf(float(eta)), col)
    sx = 1 if x > 0 else -1
    fo = mp.mpc(0)
    for (C, m, fcs) in terms[sx]:
        v = C * mp.mpf(float(x))**m
        for (gg, h) in fcs: v = v/(gg*float(x) - h)
        fo += v
    print(f"y={float(y):5}, x={float(x):5}, col={col}: residue+quad={mp.nstr(val,12)}  formula={mp.nstr(fo,12)}  abs.diff={mp.nstr(abs(val-fo),3)}", flush=True)
for (y, x) in [(0.7, 1.3), (0.7, -0.9), (-0.6, 1.1), (-0.8, -1.4), (2.5, 0.3), (-0.2, -3.0)]:
    for col in ('12', '21'):
        check(y, x, col)
