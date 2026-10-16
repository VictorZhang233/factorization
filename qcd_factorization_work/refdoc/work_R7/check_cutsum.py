"""Checks of Lemma E.24 (cut-position identity, eq. E.24), Example E.23 (eqs. E.19, E.20),
eq. (E.10) and Lemma E.16(i) (E.15) of the reference document."""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np
import sympy as sp
mp.mp.dps = 40
I = mp.mpc(0, 1)

def int_poles(zs, coef=1):
    """int_R dE/(2pi) coef * prod_k 1/(E - z_k); requires >=2 factors, distinct z_k, none real."""
    assert len(zs) >= 2
    tot = mp.mpc(0)
    for k, zk in enumerate(zs):
        if mp.im(zk) > 0:
            r = mp.mpc(1)
            for m, zm in enumerate(zs):
                if m != k:
                    r /= (zk - zm)
            tot += r
    return coef * I * tot

def T_j(j, E, alpha, beta, eta):
    n = len(E) - 1
    W = mp.mpc(1)
    for i in range(1, n + 1):
        W *= alpha[i] if i <= j else beta[i]
    if W == 0:
        return mp.mpc(0)
    # 2 pi delta_reg(E-E_j) = i[(E-E_j+i eta)^-1 - (E-E_j-i eta)^-1]
    base = [E[i] - I * eta for i in range(0, j)] + [E[i] + I * eta for i in range(j + 1, n + 1)]
    if len(base) == 0:   # n = 0: int dE/2pi 2 eta/(E^2+eta^2) = 1
        return W * 1
    t1 = int_poles(base + [E[j] - I * eta], coef=I)
    t2 = int_poles(base + [E[j] + I * eta], coef=-I)
    return W * (t1 + t2)

def rhs(E, alpha, beta, eta):
    n = len(E) - 1
    if n == 0:
        return mp.mpc(1)
    tot = mp.mpc(0)
    for m in range(1, n + 1):
        pre = (alpha[m] - beta[m])
        for i in range(1, m): pre *= alpha[i]
        for i in range(m + 1, n + 1): pre *= beta[i]
        if pre == 0: continue
        zs = [E[i] - I * eta for i in range(0, m)] + [E[i] + I * eta for i in range(m, n + 1)]
        tot += pre * int_poles(zs)
    return -I * tot

rng = np.random.default_rng(11)
ok_all = True
print("Lemma E.24, generic complex weights:")
for n in range(0, 7):
    for trial in range(3):
        E = [mp.mpf(float(x)) for x in rng.uniform(-2, 2, n + 1)]
        alpha = [None] + [mp.mpc(float(a), float(b)) for a, b in rng.normal(size=(n, 2))]
        beta = [None] + [mp.mpc(float(a), float(b)) for a, b in rng.normal(size=(n, 2))]
        eta = mp.mpf('0.23')
        lhs = sum(T_j(j, E, alpha, beta, eta) for j in range(0, n + 1))
        r = rhs(E, alpha, beta, eta)
        d = abs(lhs - r)
        ok = d < mp.mpf('1e-25') * max(1, abs(r))
        ok_all &= ok
        if trial == 0:
            print(f"  n={n}: sum_j T_j={mp.nstr(lhs,10)}  RHS={mp.nstr(r,10)}  |diff|={mp.nstr(d,3)}  {'PASS' if ok else 'FAIL'}")
print("Lemma E.24(a): all internal vertices (alpha=beta) -> sum_j T_j = delta_{n0}:")
for n in range(0, 7):
    E = [mp.mpf(float(x)) for x in rng.uniform(-2, 2, n + 1)]
    a = [None] + [mp.mpc(float(x), float(y)) for x, y in rng.normal(size=(n, 2))]
    lhs = sum(T_j(j, E, a, a, mp.mpf('0.1')) for j in range(0, n + 1))
    target = 1 if n == 0 else 0
    ok = abs(lhs - target) < 1e-25
    ok_all &= ok
    print(f"  n={n}: {mp.nstr(lhs, 6)}  {'PASS' if ok else 'FAIL'}")
print("Lemma E.24(b): insertion patterns (amp insertion beta=0, conj insertion alpha=0):")
# pattern strings: 'I' internal, 'A' amplitude insertion, 'C' conjugate insertion
for pat in ['IAI', 'AIC', 'ICA', 'AAI', 'IAICI', 'CIA', 'AICIA']:
    n = len(pat)
    E = [mp.mpf(float(x)) for x in rng.uniform(-2, 2, n + 1)]
    alpha, beta = [None], [None]
    for ch in pat:
        v = mp.mpc(float(rng.normal()), float(rng.normal()))
        if ch == 'I': alpha.append(v); beta.append(v)
        elif ch == 'A': alpha.append(v); beta.append(mp.mpc(0))
        else: alpha.append(mp.mpc(0)); beta.append(v)
    eta = mp.mpf('0.17')
    lhs = sum(T_j(j, E, alpha, beta, eta) for j in range(0, n + 1))
    r = rhs(E, alpha, beta, eta)
    # count non-zero terms on the RHS
    nz = []
    for m in range(1, n + 1):
        pre = (alpha[m] - beta[m])
        for i in range(1, m): pre *= alpha[i]
        for i in range(m + 1, n + 1): pre *= beta[i]
        if pre != 0: nz.append(m)
    ok = abs(lhs - r) < 1e-25 * max(1, abs(r))
    ok_all &= ok
    print(f"  pattern {pat:6s}: sum T_j={mp.nstr(lhs,8)}  nonzero RHS terms at m={nz}  {'PASS' if ok else 'FAIL'}")

print("\nExample E.23 (sympy):")
k, al, be = sp.symbols('k alpha beta')
D1 = be - al
lhs = sp.I / D1 * (sp.I / (k - al) + sp.I / (be - k))
rhs_ = 1 / ((k - al) * (k - be))
print("  (E.19):  (i/D1)[i/(k-a)+i/(b-k)] - 1/((k-a)(k-b)) =", sp.simplify(lhs - rhs_), "-> PASS" if sp.simplify(lhs - rhs_) == 0 else "FAIL")
# product of Feynman propagators: i/(2a^+(a^- - E_a)) * i/(2s1^+(s1^- - E_s1)), a^- - E_a = k - alpha, s1^- - E_s1 = beta - k
ap, sp1 = sp.symbols('a_p s_p', positive=True)
prop = sp.I / (2 * ap * (k - al)) * sp.I / (2 * sp1 * (be - k))
print("  propagator product vs (E.19)/(2a^+ 2s1^+):", sp.simplify(prop - rhs_ / (4 * ap * sp1)), "-> PASS" if sp.simplify(prop - rhs_ / (4 * ap * sp1)) == 0 else "FAIL")
# (E.20): int dk/2pi 1/((k-a+i0)(k-b-i0)) = i/(b-a+i0): numeric with finite eps
def e20(a, b, eps):
    f = lambda x: 1 / ((x - a + 1j * eps) * (x - b - 1j * eps)) / (2 * mp.pi)
    return mp.quad(f, [-mp.inf, min(a, b) - 1, a, b, max(a, b) + 1, mp.inf])
for (a, b) in [(0.3, 1.1), (-0.7, 0.2), (1.3, -0.4)]:
    val = e20(a, b, 1e-6)
    pred = 1j / (b - a + 2e-6j)
    print(f"  (E.20) a={a}, b={b}: numeric={mp.nstr(val,8)}  i/(b-a)={mp.nstr(pred,8)}  {'PASS' if abs(val-pred)<1e-5 else 'FAIL'}")
# the two orderings separately: conditionally convergent; symmetric cutoff
Kc = mp.mpf(10)**4
a_, b_ = mp.mpf('0.3'), mp.mpf('1.1'); eps = mp.mpf('1e-8')
I1 = mp.quad(lambda x: (1j/(b_-a_))*(1j/(x-a_+1j*eps))/(2*mp.pi), [-Kc, a_, Kc])
I2 = mp.quad(lambda x: (1j/(b_-a_))*(1j/(b_-x+1j*eps))/(2*mp.pi), [-Kc, b_, Kc])
print(f"  ordering (I) alone, symmetric cutoff: {mp.nstr(I1,6)};  ordering (II): {mp.nstr(I2,6)};  sum: {mp.nstr(I1+I2,6)};  i/D1={mp.nstr(1j/(b_-a_),6)}")
print("   -> each ordering gets weight 1/2 of i/D1 under symmetric truncation (Note E.29(2)):",
      'PASS' if abs(I1 - 0.5j/(b_-a_)) < 1e-3 and abs(I2 - 0.5j/(b_-a_)) < 1e-3 else 'FAIL')

print("\n(E.10): int dl/2pi e^{-i l tau} i/(2l+(l-E)) = [th(l+)th(tau)+th(-l+)th(-tau)] e^{-iE tau}/(2|l+|):")
for lp in [0.7, -0.7]:
    for tau in [1.3, -1.3]:
        eta = 0.4
        Ev = (0.9 - 1j * eta) / (2 * lp)
        f = lambda x: mp.exp(-1j * x * tau) * 1j / (2 * lp * (x - Ev)) / (2 * mp.pi)
        val = mp.quadosc(f, [-mp.inf, mp.inf], omega=abs(tau)) if False else None
        # do it by residues instead (exact): close LHP for tau>0, UHP for tau<0
        if tau > 0:
            val = (-1j) * (mp.exp(-1j * Ev * tau) * 1j / (2 * lp)) if mp.im(Ev) < 0 else 0
        else:
            val = (1j) * (mp.exp(-1j * Ev * tau) * 1j / (2 * lp)) if mp.im(Ev) > 0 else 0
        pred = ((lp > 0 and tau > 0) or (lp < 0 and tau < 0)) * mp.exp(-1j * Ev * tau) / (2 * abs(lp))
        print(f"  l+={lp:+.1f}, tau={tau:+.1f}: residue={mp.nstr(val,8)}  formula={mp.nstr(pred,8)}  {'PASS' if abs(val-pred)<1e-20 else 'FAIL'}")

print("\nLemma E.16(i): l-slash = g+ l- + g- l+ - gT.lT and (E.15):")
g0 = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
s1 = sp.Matrix([[0,1],[1,0]]); s2 = sp.Matrix([[0,-sp.I],[sp.I,0]]); s3 = sp.Matrix([[1,0],[0,-1]])
def gam(s):
    Z = sp.zeros(2)
    return sp.Matrix(sp.BlockMatrix([[Z, s], [-s, Z]]))
g1, g2, g3 = gam(s1), gam(s2), gam(s3)
gp = (g0 + g3) / sp.sqrt(2); gm = (g0 - g3) / sp.sqrt(2)
lp_, lm_, l1, l2, m = sp.symbols('lp lm l1 l2 m', real=True)
l0 = (lp_ + lm_) / sp.sqrt(2); l3 = (lp_ - lm_) / sp.sqrt(2)
lslash = g0 * l0 - g1 * l1 - g2 * l2 - g3 * l3
lslash_lc = gp * lm_ + gm * lp_ - g1 * l1 - g2 * l2
print("  l-slash decomposition:", sp.simplify(lslash - lslash_lc) == sp.zeros(4), )
Eon = (l1**2 + l2**2 + m**2) / (2 * lp_)
lon = gp * Eon + gm * lp_ - g1 * l1 - g2 * l2
l2m2 = 2 * lp_ * lm_ - l1**2 - l2**2 - m**2
lhs = sp.I * (lslash_lc + m * sp.eye(4)) / l2m2
rhsE = sp.I * (lon + m * sp.eye(4)) / (2 * lp_ * (lm_ - Eon)) + sp.I * gp / (2 * lp_)
print("  (E.15) identity:", sp.simplify(lhs - rhsE) == sp.zeros(4))
print("  gamma+ gamma+ = 0 (Note E.17):", sp.simplify(gp * gp) == sp.zeros(4))
print('\nALL E.24 CHECKS PASS' if ok_all else '\nSOME E.24 CHECKS FAIL')
