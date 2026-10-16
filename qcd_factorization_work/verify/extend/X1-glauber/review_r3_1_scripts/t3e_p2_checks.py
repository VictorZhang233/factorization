# X1 review round 3, reviewer 1 -- independent checks of
#  (A) T3(e)(3) and (e'): the regulated A-side weight v_K = w_K^[12] - 1/2 with the even Lorentzian k^- regulator
#      chi_K = K^2/(k^2+K^2) on both lines, on the rotated contour k^+ = e^{i pi/4} kappa; claims
#      |v_K| <= (|x1|+|x2|)/4 for |x_e| <= 1/4, |v_K| <= 1/2 everywhere, v_K = (x1-x2)/4 + O(x^2), c_U = 1.65,
#      derived here from scratch (L1': partial fractions + race weights), symbolic in x_e = iK/z_e.
#  (B) P2(b),(c): w^A_12 = 1/2 + i delta_A for rational line-dependent regulators, example 97/105, by residues;
#      sharp-window formula; p_opp identity incl. the sign convention of delta_B.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

out = []
def log(s):
    print(s, flush=True); out.append(s)

# ---------------- (A) ----------------
x1, x2 = sp.symbols('x1 x2')
K = sp.Integer(1)
def poles(x, init_gluon):
    """pole list (value, group, weight) for one line; z = iK/x; group of the gluon pole given by init_gluon"""
    z = sp.I*K/x
    return [(z, 'B' if init_gluon else 'F', x**2/(x**2 - 1)),
            (sp.I*K, 'B', 1/(2*(1 - x))),
            (-sp.I*K, 'F', 1/(2*(1 + x)))]
def race12(p1, t1, p2, t2):
    if t1 == 'F' and t2 == 'F':
        return p1/(p1 + p2)
    if t1 == 'B' and t2 == 'B':
        return p2/(p1 + p2)
    if t1 == 'B' and t2 == 'F':
        return sp.Integer(1)
    return sp.Integer(0)
def wK(init1, init2):
    tot = 0
    for (p1, t1, u1) in poles(x1, init1):
        for (p2, t2, u2) in poles(x2, init2):
            tot += u1*u2*race12(p1, t1, p2, t2)
    return sp.simplify(tot)

# sanity: sum of pole weights
for init in (True, False):
    sw = sum(w for (_, _, w) in poles(x1, init))
    assert sp.simplify(sw - 1) == 0
quad = {(1, 1): (False, False), (-1, -1): (True, True), (-1, 1): (True, False), (1, -1): (False, True)}
# kappa_e > 0: z_e at angle -pi/4 (final), x_e = (2K kappa_e/a_e) e^{3 i pi/4};  kappa_e < 0: z_e initial, x_e on e^{-i pi/4}
W = {q: wK(*quad[q]) for q in quad}
lead_ok = True
for q in quad:
    v = W[q] - sp.Rational(1, 2)
    t = sp.symbols('t')
    ser = sp.series(v.subs({x1: t*x1, x2: t*x2}), t, 0, 2).removeO()
    lin = sp.simplify(ser.subs(t, 1))
    log(f"(A) quadrant {q}: v_K = w_K^[12]-1/2, linear term = {lin}   (claim (x1-x2)/4)")
    lead_ok &= sp.simplify(lin - (x1 - x2)/4) == 0
    # K -> 0 limit (x -> infinity) reproduces the race weights of L2 (in terms of z, i.e. kappa)
f = {q: sp.lambdify((x1, x2), W[q] - sp.Rational(1, 2), 'numpy') for q in quad}
cv = 0.0; cinf = 0.0; lead_err = 0.0
ts = np.exp(np.linspace(np.log(1e-7), np.log(0.25), 300))
tb = np.exp(np.linspace(np.log(1e-7), np.log(1e7), 500))
for q in quad:
    ang = [3*np.pi/4 if q[e] > 0 else -np.pi/4 for e in range(2)]
    T1, T2 = np.meshgrid(ts, ts, indexing='ij')
    X1 = T1*np.exp(1j*ang[0]); X2 = T2*np.exp(1j*ang[1])
    V = f[q](X1, X2)
    cv = max(cv, np.max(np.abs(V)/(T1 + T2)))
    lead_err = max(lead_err, np.max(np.abs(V - (X1 - X2)/4)/(T1 + T2)**2))
    B1, B2 = np.meshgrid(tb, tb, indexing='ij')
    Vb = f[q](B1*np.exp(1j*ang[0]), B2*np.exp(1j*ang[1]))
    cinf = max(cinf, np.nanmax(np.abs(Vb)))
log(f"(A) sup_{{|x|<=1/4}} |v_K|/(|x1|+|x2|) = {cv:.5f} (claim 1/4);  sup |v_K| = {cinf:.5f} (claim 1/2);  "
    f"sup |v_K-(x1-x2)/4|/(|x1|+|x2|)^2 = {lead_err:.4f} (claim 0.044);  linear term = (x1-x2)/4 in all quadrants: {lead_ok}")
# c_U on the pi/4 rays
tt = np.exp(np.linspace(np.log(1e-8), np.log(1e8), 200001))
cU = 0.0
for ang in (3*np.pi/4, -np.pi/4):
    X = tt*np.exp(1j*ang)
    s = np.abs(X**2/(X**2 - 1)) + np.abs(1/(2*(1 - X))) + np.abs(1/(2*(1 + X)))
    cU = max(cU, s.max())
    # closed-quadrant property: final group {z (Im<0), -iK}, initial {z (Im>0), +iK}
log(f"(A) c_U = sup_rays sum_p |u_e(p)| = {cU:.5f} (claim 1.65)")
# check the closed-quadrant statement: on the pi/4 contour, z_e for kappa_e>0 is at angle -pi/4 (with -iK at -pi/2) and for
# kappa_e<0 at 3pi/4 (with +iK at pi/2): pairwise angles pi/4 <= pi/2 -> closed quadrant.  At theta = pi/2 they would be
# at -pi/2 and pi/2: collision with -+iK possible (|z| = K) -> L1' pole terms singular; the theta = pi/4 choice avoids it.

# ---------------- (B) P2 ----------------
k = sp.symbols('k')
def rat(K1, K2):
    return K1*K2/((K1 + sp.I*k)*(K2 - sp.I*k))
def w12_residue(K1a, K2a, K1b, K2b):
    """w^A_12 = (1/2pi) int chi_1(k) chi_2(-k) i/(k + i0) dk (normalized; chi(0) = 1): close in the UHP
    (the i0 pole is in the LHP); integrand decays like 1/k^5"""
    g = rat(K1a, K2a)*rat(K1b, K2b).subs(k, -k)*sp.I/k
    # poles in UHP: chi_1: k = i K1a ; chi_2(-k): (K1b - i k) = 0 -> k = -i K1b (LHP); (K2b + i k)=0 -> k = i K2b
    # chi_1: (K2a - i k) = 0 -> k = -i K2a (LHP)
    res = sp.residue(g, k, sp.I*K1a) + sp.residue(g, k, sp.I*K2b)
    return sp.nsimplify(sp.simplify(sp.I*res))   # (1/2pi) 2 pi i sum Res
for args in ((1, 3, 1, 3), (1, 3, 4, sp.Rational(1, 2)), (2, 1, sp.Rational(1, 2), 6)):
    w = w12_residue(*args)
    log(f"(B) rational regulators (K1,K2;K1',K2') = {args}: w^A_12 by residues = {w} = {float(sp.re(w)):.12f}{float(sp.im(w)):+.3e}i")
# sharp windows: delta = (1/2pi) PV int over [-min(K1,K2'), min(K2,K1')] dk/k
def sharp_delta(K1, K2, K1p, K2p):
    return np.log(min(K2, K1p)/min(K1, K2p))/(2*np.pi)
log(f"(B) sharp windows [-1,3],[-3,1]: delta = {sharp_delta(1, 3, 3, 1):.10f} (fix_r2 log 0.1748495763)")
# identity and the B-side convention: the identity p = 1/2 + 2 dA dB holds iff w^B_12 = 1/2 + i dB with the SAME
# orientation as on A; with w^B_12 = 1/2 - i dB (opposite orientation) one gets 1/2 - 2 dA dB.
dA, dB = sp.symbols('dA dB')
p_same = sp.expand((sp.Rational(1, 2) + sp.I*dA)*(sp.Rational(1, 2) - sp.I*dB) + (sp.Rational(1, 2) - sp.I*dA)*(sp.Rational(1, 2) + sp.I*dB))
p_opp_conv = sp.expand((sp.Rational(1, 2) + sp.I*dA)*(sp.Rational(1, 2) + sp.I*dB) + (sp.Rational(1, 2) - sp.I*dA)*(sp.Rational(1, 2) - sp.I*dB))
log(f"(B) p_opp = W(12,21)+W(21,12) = {p_same} if w^B_12 = 1/2 + i dB;  = {p_opp_conv} if w^B_12 = 1/2 - i dB  (sign of the dA dB term is convention dependent)")

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_r3_1_logs', 't3e_p2_checks.log'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
