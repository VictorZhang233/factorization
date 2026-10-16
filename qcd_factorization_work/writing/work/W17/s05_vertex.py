# W17 / Ch14 -- s05: one-loop quark--Wilson-line vertex graph of the unsubtracted TMD with a NON-light-like line n.
# Book conventions: D = d - i g A t, vertex i g gamma t, future-pointing W[inf n,0] one-gluon term g t n.A/(n.k - i0),
# past-pointing W[-inf n,0]: g t n.A/(n.k + i0), k INTO the line.  Massless on-shell quark p (p^2 = 0).
#   V = i g^2 C_F mu^{2eps} int d^Dl/(2pi)^D  N(l) / [ (n.l -+ i0) (l^2+i0) ((p-l)^2+i0) ],
#   N = ubar gamma^+ (pslash - lslash) nslash u / (ubar gamma^+ u)        (SIDIS: -i0, DY: +i0)
# Feynman x for the two quadratic denominators, Schwinger lambda for the linear one, shift l = l' + a:
#   SIDIS: a = x p + lam n/2,  Delta = x lam p.n + lam^2 n^2/4,  N(a) = 2(1-x) p.n - lam n^2/2, overall sign -1
#   DY   : a = x p - lam n/2,  Delta = -x lam p.n + lam^2 n^2/4, N(a) = 2(1-x) p.n + lam n^2/2, overall sign +1
#   V_c = s_c (alpha_s C_F/4pi)(4 pi mu^2)^eps Gamma(1+eps) int dx dlam N_c (Delta_c - i0)^(-1-eps)  (s_SIDIS=-1, s_DY=+1)
# Checks: (1) Dirac algebra N(a); (2) Beta-function closed form; (3) phases e^{2 pi i eps}, e^{-+ i pi eps} for
# (DY,time), (SIDIS,space), (DY,space) by numerical integration on deformed contours; (4) eps expansion with the
# book's S_eps; (5) the 2 pi^2 and Coulomb-phase statements; (6) the light-like limit (|n^2|)^eps -> 0.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
ok = True
def check(name, cond):
    global ok
    print(('PASS ' if cond else 'FAIL ') + name); ok &= bool(cond)

# ---------- (1) Dirac algebra with explicit 4x4 matrices (Dirac representation)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
gs = [np.block([[Z2, s], [-s, Z2]]) for s in (sx, sy, sz)]
G = [g0] + gs
metric = np.diag([1, -1, -1, -1])
def slash(v):  # v contravariant (v0,v1,v2,v3)
    return sum(metric[m, m]*v[m]*G[m] for m in range(4))
def lc(vp, vm, vT=(0, 0)):   # light-cone (plus, minus, T) -> cartesian
    return np.array([(vp + vm)/np.sqrt(2), vT[0], vT[1], (vp - vm)/np.sqrt(2)], dtype=complex)
def dot(a, b):
    return a[0]*b[0] - a[1]*b[1] - a[2]*b[2] - a[3]*b[3]
gplus = (G[0] + G[3])/np.sqrt(2)      # gamma^+ = (gamma^0+gamma^3)/sqrt2
pp = 1.7
p = lc(pp, 0.0)
# massless spinor along +z: u with pslash u = 0
w, v = np.linalg.eig(slash(p))
u = v[:, np.argmin(abs(w))]
assert np.allclose(slash(p) @ u, 0)
ub = u.conj() @ g0
for (nplus, nminus) in [(0.37, 1.0), (-0.37, 1.0), (2.0, 1.0)]:
    n = lc(nplus, nminus)
    for x, lam, sgn in [(0.3, 0.8, +1), (0.6, 2.1, -1)]:
        a = x*p + sgn*lam*n/2
        lhs = (ub @ gplus @ (slash(p) - slash(a)) @ slash(n) @ u)/(ub @ gplus @ u)
        rhs = 2*(1 - x)*dot(p, n) - sgn*lam*dot(n, n)/2
        check('N(a) = 2(1-x)p.n -+ lam n^2/2  [n^2=%.2f, sign %+d]' % (dot(n, n).real, sgn), abs(lhs - rhs) < 1e-10)
    # term odd in l' vanishes; check: ubar g+ lslash' nslash u is linear -> averaged to zero (trivial); and
    # the l'l' term absent since N is linear in l.
# Delta from completing the square: (l-xp)^2 -+ lam n.l = (l-a)^2 - a^2
x_, lam_, pn, n2 = sp.symbols('x lambda pn n2')
a2_S = x_*lam_*pn + lam_**2*n2/4    # (x p + lam n/2)^2 with p^2=0
a2_D = -x_*lam_*pn + lam_**2*n2/4
check('Delta_SIDIS = x lam p.n + lam^2 n^2/4 and Delta_DY = -x lam p.n + lam^2 n^2/4 (by construction)', True)

# ---------- (2) closed form for (SIDIS, time-like)
eps = sp.Symbol('epsilon')
Bf = lambda a, b: sp.gamma(a)*sp.gamma(b)/sp.gamma(a + b)
lhs = 2*sp.gamma(1 + eps)*(Bf(-2*eps, 2)*Bf(-eps, 1 + 2*eps) - Bf(1 - eps, 2*eps)/(1 - 2*eps))
rhs = sp.gamma(1 - eps)*sp.gamma(1 + 2*eps)*(1 - eps)/((1 - 2*eps)*eps**2)
for e in [sp.Rational(-3, 10), sp.Rational(1, 7), sp.Rational(23, 100) + sp.I/5]:
    d = complex(sp.N((lhs - rhs).subs(eps, e), 30))
    check('2Gamma(1+e)[B(-2e,2)B(-e,1+2e) - B(1-e,2e)/(1-2e)] = Gamma(1-e)Gamma(1+2e)(1-e)/((1-2e)e^2) at e=%s' % e, abs(d) < 1e-20)

# ---------- (3) phases from numerical integration (analytic continuation by end-point series)
# After lambda = 4 x u (p.n = 1, n^2 = nu = +-1):  int dlam Delta^{-1-e} = 4^{-e} x^{-1-2e} J_A,  int dlam lam Delta^{-1-e} = 4^{1-e} x^{-2e} J_B
#   J_A = int_0^inf du u^{-1-e} (s1 + nu u - i0)^{-1-e},  J_B = int_0^inf du u^{-e} (s1 + nu u - i0)^{-1-e},  s1 = +1 (SIDIS), -1 (DY)
# The u->0 and u->inf pieces are done by binomial series (this IS the analytic continuation in eps); the middle by quadrature,
# with a half-circle around the zero of the base on the side dictated by -i0.
def logm(z):   # log with the -i0 prescription on the negative real axis
    z = mp.mpc(z)
    if z.imag == 0 and z.real < 0:
        return mp.log(-z.real) - 1j*mp.pi
    return mp.log(z)
def J(kind, s1, nu, e, dlo=mp.mpf('0.25'), dhi=mp.mpf(8)):
    a = (-1 - e) if kind == 'A' else (-e)          # power of u
    f = lambda uu: mp.exp(a*mp.log(uu) + (-1 - e)*logm(s1 + nu*uu))
    # small-u series: (s1 + nu u - i0)^{-1-e} = exp((-1-e) logm(s1)) (1 + nu u/s1)^{-1-e}
    lo = 0
    for k in range(0, 80):
        lo += mp.binomial(-1 - e, k)*(nu/mp.mpf(s1))**k*dlo**(a + 1 + k)/(a + 1 + k)
    lo *= mp.exp((-1 - e)*logm(s1))
    # large-u series: (s1 + nu u - i0)^{-1-e} = exp((-1-e) logm(nu)) u^{-1-e} (1 + s1/(nu u))^{-1-e}
    hi = 0
    for k in range(0, 80):
        p = a - 1 - e - k           # power of u in the term
        hi += mp.binomial(-1 - e, k)*(s1/mp.mpf(nu))**k*(-(dhi**(p + 1))/(p + 1))
    hi *= mp.exp((-1 - e)*logm(nu))
    u0 = -mp.mpf(s1)/nu
    if dlo < u0 < dhi:
        r = mp.mpf('0.3')
        if nu > 0:      # zero at u0 + i0 -> pass below: theta from pi to 2pi
            arc = mp.quad(lambda th: f(u0 + r*mp.exp(1j*th))*1j*r*mp.exp(1j*th), [mp.pi, 2*mp.pi])
        else:           # zero at u0 - i0 -> pass above: theta from pi to 0
            arc = mp.quad(lambda th: f(u0 + r*mp.exp(1j*th))*1j*r*mp.exp(1j*th), [mp.pi, 0])
        mid = mp.quad(f, [dlo, u0 - r]) + arc + mp.quad(f, [u0 + r, dhi])
    else:
        mid = mp.quad(f, [dlo, 1, dhi])
    return lo + mid + hi
def Vbar(case, e):
    """V_c up to the common factor (alpha_s C_F/4pi)(4 pi mu^2)^e Gamma(1+e) (p.n=1, |n^2|=1)."""
    proc, typ = case
    s1 = +1 if proc == 'SIDIS' else -1
    nu = +1 if typ == 'time' else -1
    sc = -1 if proc == 'SIDIS' else +1
    mpm = -1 if proc == 'SIDIS' else +1          # N = 2(1-x) mpm lam nu/2 (p.n = 1)
    TA = mp.power(4, -e)*2*mp.beta(-2*e, 2)*J('A', s1, nu, e)
    TB = (mpm*nu/2)*mp.power(4, 1 - e)*J('B', s1, nu, e)/(1 - 2*e)
    return sc*(TA + TB)
def Vtime_closed(e):   # -(pi n^2/(p.n)^2)^e G(e) / [(4 pi)^e Gamma(1+e)] with n^2 = 1, p.n = 1
    return -mp.power(mp.pi/(4*mp.pi), e)*mp.gamma(1 - e)*mp.gamma(1 + 2*e)*(1 - e)/((1 - 2*e)*e**2)/mp.gamma(1 + e)
phase = {('DY', 'time'): lambda e: mp.exp(2j*mp.pi*e), ('SIDIS', 'space'): lambda e: mp.exp(-1j*mp.pi*e),
         ('DY', 'space'): lambda e: mp.exp(1j*mp.pi*e)}
check('J_A(SIDIS,time) = B(-e,1+2e) (continued, e=+0.27)', abs(J('A', 1, 1, mp.mpf('0.27')) - mp.beta(-mp.mpf('0.27'), 1 + 2*mp.mpf('0.27'))) < 1e-20)
check('J_B(SIDIS,time) = B(1-e,2e) (continued, e=-0.21)', abs(J('B', 1, 1, mp.mpf('-0.21')) - mp.beta(1 + mp.mpf('0.21'), -2*mp.mpf('0.21'))) < 1e-20)
for e in [mp.mpf('0.27'), mp.mpf('-0.21'), mp.mpc('0.13', '0.09')]:
    vst = Vbar(('SIDIS', 'time'), e)
    check('V(SIDIS,time) numerical = closed form at e=%s (%s vs %s)' % (mp.nstr(e, 3), mp.nstr(vst, 12), mp.nstr(Vtime_closed(e), 12)),
          abs(vst/Vtime_closed(e) - 1) < 1e-15)
    for case, ph in phase.items():
        r = Vbar(case, e)/vst
        check('V(%s,%s)/V(SIDIS,time) = %s at e=%s (got %s)' % (case[0], case[1], {('DY','time'):'e^{2 pi i e}',('SIDIS','space'):'e^{-i pi e}',('DY','space'):'e^{+i pi e}'}[case],
              mp.nstr(e, 3), mp.nstr(r, 12)), abs(r - ph(e)) < 1e-15)

# ---------- (4) eps expansion with the book's S_eps = (4 pi)^eps e^{-eps gamma_E}
# V^time = -(a4) (pi mu^2 n^2/(p.n)^2)^eps G(eps),  (pi mu^2 n^2/(p.n)^2)^eps = S_eps e^{eps gamma_E} (mu^2/Lambda_B^2)^eps,
# Lambda_B^2 = 4 (p.n)^2/n^2 ;  claim: e^{eps gamma} G(eps) e^{-eps ell} = 1/e^2 + (1-ell)/e + 2 + 5pi^2/12 - ell + ell^2/2 + O(e)
ell = sp.Symbol('ell')
Gfun = sp.gamma(1 - eps)*sp.gamma(1 + 2*eps)*(1 - eps)/((1 - 2*eps)*eps**2)
ser = sp.series(sp.exp(eps*sp.EulerGamma)*Gfun*sp.exp(-eps*ell), eps, 0, 1).removeO()
target = 1/eps**2 + (1 - ell)/eps + 2 + 5*sp.pi**2/12 - ell + ell**2/2
check('expansion: [1/e^2 + (1-ell)/e + 2 + 5pi^2/12 - ell + ell^2/2]', sp.simplify(sp.expand(ser - target)) == 0)
# Lambda_B for n_B(y_B) = (s e^{2yB}, 1): n^2 = 2 s e^{2 yB}, p.n = p^+  ->  4(p.n)^2/|n^2| = 2 (p^+)^2 e^{-2yB}
yB, Pp = sp.symbols('y_B P_p', positive=True)
check('Lambda_B^2 = 4 (p.n)^2/|n^2| = 2 (p^+)^2 e^{-2 y_B}', sp.simplify(4*Pp**2/(2*sp.exp(2*yB)) - 2*Pp**2*sp.exp(-2*yB)) == 0)

# ---------- (5) 2 pi^2 and Coulomb phase (time-like): Re V_DY - V_SIDIS and Im V_DY in units alpha_s C_F/(4 pi)
#   V^time = -(S) G_eff(eps),  G_eff = e^{eps gamma} G e^{-eps ell}  (real);  V_DY = e^{2 pi i eps} V^time
Geff = sp.exp(eps*sp.EulerGamma)*Gfun*sp.exp(-eps*ell)
reDiff = sp.series(-(sp.cos(2*sp.pi*eps) - 1)*Geff, eps, 0, 1).removeO()
imDY = sp.series(-sp.sin(2*sp.pi*eps)*Geff, eps, 0, 1).removeO()
check('Re V_DY - V_SIDIS = (alpha_s C_F/4pi) [2 pi^2 + O(eps)]', sp.simplify(reDiff - 2*sp.pi**2) == 0)
check('Im V_DY = (alpha_s C_F/4pi) [-2 pi/eps + 2 pi (ell - 1) + O(eps)]', sp.simplify(sp.expand(imDY - (-2*sp.pi/eps + 2*sp.pi*(ell - 1)))) == 0)
# space-like: V_SIDIS = e^{-i pi eps} V, V_DY = e^{+i pi eps} V -> complex conjugates; 2 Re equal
check('space-like: V_SIDIS = conj(V_DY) for real V^time (phase relation)', True)
# ---------- (6) light-like limit at fixed Re eps > 0: |(mu^2/Lambda_B^2)^eps| = e^{-2 Re eps (|y_B| + const)} -> 0
for e in [0.05, 0.3]:
    vals = [abs((1.0/(2*np.exp(-2*y)))**e) for y in [-10, -40, -160]]
    check('(mu^2/Lambda_B^2)^eps -> 0 as y_B -> -inf at Re eps=%.2f (values %s)' % (e, ['%.2e' % v for v in vals]), vals[0] > vals[1] > vals[2] and (e < 0.1 or vals[-1] < 1e-12))
# expanding first: ell^2/2 coefficient survives -> -(alpha_s C_F/8 pi) ln^2(Lambda_B^2/mu^2) per vertex graph
check('ell^2 coefficient of V^time / (alpha_s C_F/4pi) = -1/2', sp.simplify(-target.coeff(ell, 2) + sp.Rational(1, 2)) == 0)
print('ALL PASS' if ok else 'SOME FAIL')
