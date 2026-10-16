"""W03 / Ch3 sec:prelim-distributions and App A sec:appA-plus, sec:appA-mellin.
Conventions: <[g]_+, h> = int_0^1 g (h - h(1)); D_k = [ln^k(1-z)/(1-z)]_+; product convention
g D_k = g(1) D_k + (g - g(1)) ln^k(1-z)/(1-z)  (= the distributional product <g D_k, h> := <D_k, g h>).
  P1  VF-CONV-7 identities on test functions
  P2  product convention = distributional product
  P3  (1+z^2) D_1 = [(1+z^2) ln(1-z)/(1-z)]_+ + 7/4 delta(1-z)  (VF-DY-12); -int (1+z) ln(1-z) = 7/4
  P4  expansion lemma (1-z)^{-1-a e} = -delta/(a e) + sum_k (-a e)^k/k! D_k  for test functions in T_eta, -eta < a e < 0
  P5  ex:prelim-plus: int (1-z)^{-1-2e} z^{-e} h = -h(1)/(2e) + <D_0,h> - e[int h ln z/(1-z) + 2<D_1,h>] + O(e^2);
      h = z^{N-1}: closed form B(N-e,-2e), coefficients -S_1(N-1) and -[S_1^2 + 2 S_2 - zeta_2](N-1)
  M1  <D_0, z^{N-1}> = -S_1(N-1), <D_1, z^{N-1}> = (S_1^2+S_2)(N-1)/2 for N = 1..10 (exact) and complex N (numerical)
  M2  large N: -ln Nbar, (ln^2 Nbar + zeta_2)/2 (VF-CONV-8, VF-THR-2)
  M3  P_qq moment C_F[3/2 + 1/(N(N+1)) - 2 S_1(N)] (VF-PDF-8) from (1+z^2) D_0 = 2 D_0 - (1+z)
  M4  C_2^q, C_2^g moments (VF-DIS-8) from the x-space forms (VF-DIS-7), N = 1..8 table
  M5  convolution theorem for (i) two functions, (ii) D_0 (x) function, numerically via <f(x)g, h> = int int f(x)g(y) h(xy)
  M6  harmonic sums: S_1(N) = psi(N+1)+gamma_E, S_2(N) = zeta_2 - psi'(N+1); int (z^{N-1}-1)/(1-z) = -S_1(N-1) for Re N > 0
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp

PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('PASS  ' if ok else 'FAIL  ') + name + ('   ' + info if info else ''))
mp.mp.dps = 30
def Dk(k, h):
    return mp.quad(lambda z: mp.log(1 - z)**k / (1 - z) * (h(z) - h(1)), [0, 0.5, 1])
def plus(gfun, h):
    return mp.quad(lambda z: gfun(z) * (h(z) - h(1)), [0, 0.5, 1])
tests = [lambda z: mp.e**z, lambda z: mp.cos(3 * z) + z**2, lambda z: mp.sqrt(z) * (1 + z)**2]
# P1
ok = True
for h in tests:
    l1 = plus(lambda z: (1 + z**2) / (1 - z), h)
    r1 = mp.quad(lambda z: ((1 + z**2) * h(z) - 2 * h(1)) / (1 - z), [0, 0.5, 1]) + mp.mpf(3) / 2 * h(1)
    l2 = plus(lambda z: 2 * z / (1 - z), h)
    r2 = mp.quad(lambda z: (2 * z * h(z) - 2 * h(1)) / (1 - z), [0, 0.5, 1]) + 2 * h(1)
    l3 = plus(lambda z: z / (1 - z), h)
    r3 = mp.quad(lambda z: (z * h(z) - h(1)) / (1 - z), [0, 0.5, 1]) + h(1)
    ok &= abs(l1 - r1) < 1e-20 and abs(l2 - r2) < 1e-20 and abs(l3 - r3) < 1e-20
check('P1 [(1+z^2)/(1-z)]_+ = (1+z^2)D_0 + 3/2 delta; [2z/(1-z)]_+ = 2z D_0 + 2 delta; [z/(1-z)]_+ = z D_0 + delta', ok)
# P2 product convention
ok = True
for gk in (lambda z: 1 + z**2, lambda z: mp.e**(2 * z)):
    for h in tests:
        for k in (0, 1, 2):
            lhs = mp.quad(lambda z: mp.log(1 - z)**k / (1 - z) * (gk(z) * h(z) - gk(1) * h(1)), [0, 0.5, 1])   # <D_k, g h>
            rhs = gk(1) * Dk(k, h) + mp.quad(lambda z: (gk(z) - gk(1)) * mp.log(1 - z)**k / (1 - z) * h(z), [0, 0.5, 1])
            ok &= abs(lhs - rhs) < 1e-20
check('P2 <D_k, g h> = g(1)<D_k,h> + int (g-g(1)) ln^k(1-z)/(1-z) h  (product convention), k = 0,1,2', ok)
# P3
z = sp.Symbol('z', positive=True)
I74 = sp.integrate((1 + z) * sp.log(1 - z), (z, 0, 1))
ok = sp.simplify(I74 + sp.Rational(7, 4)) == 0
for h in tests:
    lhs = mp.quad(lambda zz: mp.log(1 - zz) / (1 - zz) * ((1 + zz**2) * h(zz) - 2 * h(1)), [0, 0.5, 1])
    rhs = plus(lambda zz: (1 + zz**2) * mp.log(1 - zz) / (1 - zz), h) + mp.mpf(7) / 4 * h(1)
    ok &= abs(lhs - rhs) < 1e-20
check('P3 (1+z^2)D_1 = [(1+z^2)ln(1-z)/(1-z)]_+ + 7/4 delta;  int_0^1 (1+z)ln(1-z) dz = -7/4', ok, 'int = %s' % I74)
# P4 expansion lemma.  <D_k,h> = int_0^1 ln^k(1-z)/(1-z) (h(z)-h(1)) dz = int_0^inf (-s)^k (h(1-e^{-s}) - h(1)) ds
# (substitution 1-z = e^{-s}); this form is numerically stable for large k.  LHS: int_0^1 (1-z)^{-1+t} h(z) dz with
# t = -a eps > 0, written as h(1)/t + int_0^inf e^{-t s}(h(1-e^{-s}) - h(1)) ds.  Exact polynomial check: h = z^{N-1},
# LHS = B(N,t) = Gamma(N)Gamma(t)/Gamma(N+t), and B(N,t) - 1/t is analytic for |t| < 1 (radius = eta = 1).
def Dk_stable(k, h):
    return mp.quad(lambda s_: (-s_)**k * (h(1 - mp.e**(-s_)) - h(1)), [0, 1, 5, 20, 60, mp.inf])
ok = True
info = []
mp.mp.dps = 20
Dcache = {}
for ih, h in enumerate(tests[:2]):
    Dcache[ih] = [Dk_stable(k, h) for k in range(0, 60)]      # <D_k,h> do not depend on a, eps
for a in (1, 2):
    for ae in (-0.1, -0.3, -0.6):
        t = -ae
        for ih, h in enumerate(tests[:2]):
            lhs = h(1) / t + mp.quad(lambda s_: mp.e**(-t * s_) * (h(1 - mp.e**(-s_)) - h(1)), [0, 1, 5, 20, 60, mp.inf])
            ser = h(1) / t
            for k in range(0, 60):
                ser += t**k / mp.factorial(k) * Dcache[ih][k]
            ok &= abs(lhs - ser) < 1e-10
            info.append(float(abs(lhs - ser)))
# independent direct quadrature of the left-hand side for one case (no substitution)
# (the substitution u = (1-z)^t removes the integrable endpoint singularity: (1-z)^{-1+t} dz = -du/t)
lhs_direct = (1 / mp.mpf('0.3')) * mp.quad(lambda uu: tests[0](1 - uu**(1 / mp.mpf('0.3'))), [0, 0.5, 1])
lhs_sub = tests[0](1) / mp.mpf('0.3') + mp.quad(lambda s_: mp.e**(-mp.mpf('0.3') * s_) * (tests[0](1 - mp.e**(-s_)) - tests[0](1)), [0, 1, 5, 20, 60, mp.inf])
ok &= abs(lhs_direct - lhs_sub) < 1e-8
check('P4 (1-z)^{-1-a e} = -delta/(a e) + sum_k (-a e)^k/k! D_k (a=1,2; a e = -0.1,-0.3,-0.6; smooth test fns, eta=1)', ok,
      'max err %.1e' % max(info))
# exact: Taylor coefficients of B(N,t) - 1/t at t=0 equal <D_k, z^{N-1}>/k!  (N = 3), radius of convergence 1
tt = sp.Symbol('t')
okx = True
for Nv in (2, 3, 4):
    Bm = sp.gamma(Nv) * sp.gamma(tt) / sp.gamma(Nv + tt) - 1 / tt
    serB = sp.series(Bm, tt, 0, 4).removeO()
    for kk_ in range(0, 4):
        z_ = sp.Symbol('z', positive=True)
        # <D_k, z^{N-1}> = int_0^1 ln^k(1-z)/(1-z) (z^{N-1}-1) dz  = -sum_{j=0}^{N-2} int_0^1 z^j ln^k(1-z) dz
        u_ = sp.Symbol('u', positive=True)   # u = 1 - z avoids the sympy branch issue of log(1-z)
        dk = -sum(sp.integrate(sp.expand((1 - u_)**j) * sp.log(u_)**kk_, (u_, 0, 1)) for j in range(0, Nv - 1))
        okx &= sp.simplify(serB.coeff(tt, kk_) - dk / sp.factorial(kk_)) == 0
    # poles of B(N,t) - 1/t: t = -1, ..., -(N-1): nearest singularity at t = -1
    okx &= sp.simplify(sp.limit(Bm * (tt + 1), tt, -1)) != 0
check('P4 exact (h = z^{N-1}, N=2,3,4): Taylor coefficients of B(N,t)-1/t are <D_k,z^{N-1}>/k!; nearest pole t=-1 (radius 1)', okx)
# remainder estimate |<D_k,h>| <= C k!/eta^{k+1} for h in T_eta: test h(z) = (1-z)^eta, eta = 1/2: <D_k,h> = int (-s)^k (e^{-s eta}-1)
eta_ = mp.mpf('0.5')
hh = lambda zz: (1 - zz)**eta_
okb = True
mp.mp.dps = 30
for k in range(0, 8):
    # breakpoints adapted to the peak of s^k e^{-eta s} at s = k/eta (the [60, inf) tail is not negligible for k = 7)
    val = mp.quad(lambda s_: (-s_)**k * (hh(1 - mp.e**(-s_)) - hh(1)), [0, 1, 5, 10, 20, 40, 80, 160, 320, mp.inf])
    exact = (-1)**k * (mp.factorial(k) / eta_**(k + 1))   # int_0^inf (-s)^k e^{-eta s} ds, the -1 part is the h(1)=0 term
    okb &= abs(val - exact) < 1e-8 * abs(exact)
check('P4 bound: for h=(1-z)^eta, <D_k,h> = (-1)^k k!/eta^{k+1} exactly (series radius = eta)', okb)
# P5 ex:prelim-plus
N, e = sp.symbols('N e')
B = sp.gamma(N - e) * sp.gamma(-2 * e) / sp.gamma(N - 3 * e)
ok = True
for Nv in (1, 2, 3, 5, 8):
    ser = sp.series(B.subs(N, Nv), e, 0, 2).removeO()
    S1 = sp.harmonic(Nv - 1); S2 = sp.harmonic(Nv - 1, 2)
    targ = -1 / (2 * e) - S1 - e * (S1**2 + 2 * S2 - sp.zeta(2))
    ok &= sp.simplify(sp.expand(ser - targ)) == 0
check('P5 h = z^{N-1}: B(N-e,-2e) = -1/(2e) - S_1(N-1) - e[S_1^2 + 2S_2 - zeta_2](N-1) + O(e^2), N = 1,2,3,5,8', ok)
ok = True
rinfo = []
for h in tests:
    a0 = Dk_stable(0, h)
    a1 = -(mp.quad(lambda zz: h(zz) * mp.log(zz) / (1 - zz), [0, 0.5, 1]) + 2 * Dk_stable(1, h))
    rems = []
    for ev in (mp.mpf('-0.004'), mp.mpf('-0.002'), mp.mpf('-0.001')):
        t = -2 * ev
        # int_0^1 (1-z)^{-1+t} z^{-ev} h(z) dz = H(1)/t + int_0^inf e^{-t s} (H(1-e^{-s}) - H(1)) ds,  H = z^{-ev} h
        H = lambda zz, ev=ev: zz**(-ev) * h(zz)
        lhs = H(1) / t + mp.quad(lambda s_: mp.e**(-t * s_) * (H(1 - mp.e**(-s_)) - H(1)), [0, 1, 5, 20, 60, mp.inf])
        pred = -h(1) / (2 * ev) + a0 + ev * a1
        rems.append((lhs - pred) / ev**2)
    # the remainder divided by e^2 must approach a constant: successive differences shrink linearly
    d1 = abs(rems[0] - rems[1]); d2 = abs(rems[1] - rems[2])
    ok &= d2 < 0.6 * d1 + 1e-12 and abs(rems[2]) < 1e3
    rinfo.append(mp.nstr(rems[2], 6))
check('P5 generic test functions: (lhs - expansion through O(e))/e^2 tends to a constant (e = -0.004,-0.002,-0.001)', ok,
      'limits: %s' % rinfo)
# M1 Mellin table: <D_0,z^{N-1}> = -S_1(N-1) (polynomial division, exact); <D_1,z^{N-1}> = sum_{m<N} S_1(m)/m
#    = (S_1^2+S_2)(N-1)/2 (exact rational identity), cross-checked by direct quadrature of the defining integrals
ok = True
mp.mp.dps = 25
for Nv in range(1, 11):
    S1 = sp.harmonic(Nv - 1); S2 = sp.harmonic(Nv - 1, 2)
    d0 = -sum(sp.Rational(1, j_ + 1) for j_ in range(0, Nv - 1))
    d1 = sum(sp.harmonic(m) / m for m in range(1, Nv))
    ok &= sp.simplify(d0 + S1) == 0 and sp.simplify(d1 - (S1**2 + S2) / 2) == 0
    q0 = mp.quad(lambda zz: (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    q1 = mp.quad(lambda zz: mp.log(1 - zz) * (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    ok &= abs(q0 - mp.mpf(sp.Rational(d0).p) / sp.Rational(d0).q) < 1e-15 and abs(q1 - mp.mpf(sp.Rational(d1).p) / sp.Rational(d1).q) < 1e-15
check('M1 <D_0,z^{N-1}> = -S_1(N-1), <D_1,z^{N-1}> = (S_1^2+S_2)(N-1)/2, N = 1..10 (exact + quadrature)', ok)
ok = True
for Nc in (mp.mpc(2.3, 1.1), mp.mpc(0.7, -0.4), mp.mpf(5.5)):
    d0 = mp.quad(lambda zz: (zz**(Nc - 1) - 1) / (1 - zz), [0, 0.5, 1])
    d1 = mp.quad(lambda zz: mp.log(1 - zz) * (zz**(Nc - 1) - 1) / (1 - zz), [0, 0.5, 1])
    S1 = mp.digamma(Nc) + mp.euler; S2 = mp.zeta(2) - mp.psi(1, Nc)
    ok &= abs(d0 + S1) < 1e-15 and abs(d1 - (S1**2 + S2) / 2) < 1e-15
check('M1 continuation: S_1(N-1) = psi(N)+gamma_E, S_2(N-1) = zeta_2 - psi\'(N), complex N (numerical)', ok)
# M2 large N
ok = True
for Nv in (mp.mpf(10)**4, mp.mpf(10)**6):
    S1 = mp.digamma(Nv) + mp.euler; S2 = mp.zeta(2) - mp.psi(1, Nv)
    lnNb = mp.log(Nv) + mp.euler
    ok &= abs(-S1 + lnNb) < 2 / Nv and abs((S1**2 + S2) / 2 - (lnNb**2 + mp.zeta(2)) / 2) < 50 * mp.log(Nv) / Nv
check('M2 large N: <D_0> -> -ln Nbar, <D_1> -> (ln^2 Nbar + zeta_2)/2, corrections O(ln N/N)', ok)
# M3 P_qq moment
CF = sp.Symbol('C_F')
ok = True
for Nv in range(1, 9):
    mom = CF * (2 * (-sp.harmonic(Nv - 1)) - sp.integrate(z**(Nv - 1) * (1 + z), (z, 0, 1)) + sp.Rational(3, 2))
    ok &= sp.simplify(mom - CF * (sp.Rational(3, 2) + sp.Rational(1, Nv * (Nv + 1)) - 2 * sp.harmonic(Nv))) == 0
check('M3 P_qq: (1+z^2)D_0 = 2D_0 - (1+z) gives C_F[3/2 + 1/(N(N+1)) - 2S_1(N)], N = 1..8', ok)
# M4 C_2 moments from x space (VF-DIS-7) by quadrature, vs the VF-DIS-8 table and closed forms (N = 1..8)
table_q = [0, sp.Rational(1, 6), sp.Rational(29, 24), sp.Rational(91, 40), sp.Rational(589, 180), sp.Rational(5281, 1260),
           sp.Rational(50791, 10080), sp.Rational(58703, 10080)]
table_g = [sp.Rational(1, 3), -sp.Rational(1, 4), -sp.Rational(7, 20), -sp.Rational(133, 360), -sp.Rational(23, 63),
           -sp.Rational(1777, 5040), -sp.Rational(27, 80), -sp.Rational(16231, 50400)]
TF = sp.Symbol('T_F')
okq = okg = okf = True
mp.mp.dps = 25
fr = lambda r: mp.mpf(sp.Rational(r).p) / sp.Rational(r).q
for Nv in range(1, 9):
    D0 = mp.quad(lambda zz: (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    D1 = mp.quad(lambda zz: mp.log(1 - zz) * (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    reg = mp.quad(lambda zz: zz**(Nv - 1) * (-(1 + zz) * mp.log(1 - zz) - (1 + zz**2) / (1 - zz) * mp.log(zz) + 3 + 2 * zz), [0, 0.5, 1])
    cq = 2 * D1 - mp.mpf(3) / 2 * D0 + reg - (mp.mpf(9) / 2 + mp.pi**2 / 3)
    okq &= abs(cq - fr(table_q[Nv - 1])) < 1e-15
    cg = mp.quad(lambda zz: zz**(Nv - 1) * ((zz**2 + (1 - zz)**2) * mp.log((1 - zz) / zz) - 8 * zz**2 + 8 * zz - 1), [0, 0.5, 1])
    okg &= abs(cg - fr(table_g[Nv - 1])) < 1e-15
    S1N = sp.harmonic(Nv); S2N = sp.harmonic(Nv, 2)
    fq = S1N**2 - S2N + sp.Rational(3, 2) * S1N - S1N / (Nv * (Nv + 1)) + sp.Rational(3, 2 * Nv) + sp.Rational(2, Nv + 1) + sp.Rational(1, Nv**2) - sp.Rational(9, 2)
    fg = -sp.Rational(Nv**2 + Nv + 2, Nv * (Nv + 1) * (Nv + 2)) * S1N + sp.Rational(1, Nv**2) - sp.Rational(1, Nv) + sp.Rational(6, (Nv + 1) * (Nv + 2))
    okf &= sp.simplify(fq - table_q[Nv - 1]) == 0 and sp.simplify(fg - table_g[Nv - 1]) == 0
check('M4 C_2^q moments from the x-space form (quadrature) = VF-DIS-8 table, N = 1..8', okq)
check('M4 C_2^g moments from the x-space form (quadrature) = VF-DIS-8 table, N = 1..8', okg)
check('M4 closed forms of C^q_{2,N}, C^g_{2,N} (VF-DIS-8) reproduce the table', okf)
# M5 convolution theorem
mp.mp.dps = 20
f1 = lambda x: x**0.5 * (1 - x)**2
g1 = lambda x: (1 - x)**1.5 * (1 + x)
def conv_moment(fm, gm, Nn):
    # <f (x) g, x^{N-1}> = int int f(x) g(y) (x y)^{N-1}
    return mp.quad(lambda xx, yy: fm(xx) * gm(yy) * (xx * yy)**(Nn - 1), [0, 1], [0, 1])
def mel(fm, Nn): return mp.quad(lambda xx: fm(xx) * xx**(Nn - 1), [0, 1])
ok = all(abs(conv_moment(f1, g1, Nn) - mel(f1, Nn) * mel(g1, Nn)) < 1e-12 for Nn in (1.0, 2.5, 4.0))
# check that int int f(x) g(y) h(xy) = int dx h(x) (f(x)g)(x) with (f(x)g)(x) = int_x^1 dxi/xi f(xi) g(x/xi)
hfun = lambda x: mp.cos(2 * x)
lhs = mp.quad(lambda xx, yy: f1(xx) * g1(yy) * hfun(xx * yy), [0, 1], [0, 1])
convx = lambda x: mp.quad(lambda xi: f1(xi) * g1(x / xi) / xi, [x, 1])
rhs = mp.quad(lambda x: hfun(x) * convx(x), [0, 0.5, 1])
ok &= abs(lhs - rhs) < 1e-10
# distribution D_0 convolved with a function: Mellin product
Dmel = lambda Nn: -(mp.digamma(Nn) + mp.euler)
dist_conv = lambda Nn: mp.quad(lambda yy: g1(yy) * yy**(Nn - 1) * 1, [0, 1]) * Dmel(Nn)
direct = lambda Nn: mp.quad(lambda xx: (xx**(Nn - 1) - 1) / (1 - xx), [0, 0.5, 1]) * mel(g1, Nn)
ok &= all(abs(dist_conv(Nn) - direct(Nn)) < 1e-12 for Nn in (2.0, 3.7))
check('M5 convolution theorem: Mellin(f(x)g) = f~ g~ (functions; <f(x)g,h> = int int f g h(xy); D_0 (x) g)', ok)
# M6
ok = True
for Nn in (1, 2, 5, 9):
    ok &= abs(mp.harmonic(Nn) - (mp.digamma(Nn + 1) + mp.euler)) < 1e-15
    ok &= abs(sum(mp.mpf(1) / j**2 for j in range(1, Nn + 1)) - (mp.zeta(2) - mp.psi(1, Nn + 1))) < 1e-15
check('M6 S_1(N) = psi(N+1)+gamma_E, S_2(N) = zeta_2 - psi\'(N+1)', ok)

# M7 Mellin moments of all four LO kernels (VF-PDF-8) from the x-space kernels (VF-PDF-7, product convention),
#    plus the quark-number and momentum sum rules, N = 1..8 (exact)
CA, nf = sp.symbols('C_A n_f')
beta0 = sp.Rational(11, 3) * CA - sp.Rational(4, 3) * TF * nf
zz_ = sp.Symbol('z', positive=True)
def mel_fun(f, Nv):
    return sp.integrate(zz_**(Nv - 1) * f, (zz_, 0, 1))
def mel_D0(g, Nv):
    # <g D_0, z^{N-1}> = <D_0, g z^{N-1}> = int (g(z) z^{N-1} - g(1))/(1-z) ; g polynomial -> exact by division
    num = sp.expand(g * zz_**(Nv - 1) - g.subs(zz_, 1))
    q, r = sp.div(sp.Poly(num, zz_), sp.Poly(1 - zz_, zz_))
    assert r.is_zero
    return sp.integrate(q.as_expr(), (zz_, 0, 1))
okm = True
for Nv in range(1, 9):
    S1N = sp.harmonic(Nv)
    gqq = CF * (mel_D0(1 + zz_**2, Nv) + sp.Rational(3, 2))
    okm &= sp.simplify(gqq - CF * (sp.Rational(3, 2) + sp.Rational(1, Nv * (Nv + 1)) - 2 * S1N)) == 0
    gqg = TF * mel_fun(zz_**2 + (1 - zz_)**2, Nv)
    okm &= sp.simplify(gqg - TF * sp.Rational(Nv**2 + Nv + 2, Nv * (Nv + 1) * (Nv + 2))) == 0
    if Nv >= 2:
        ggq = CF * mel_fun((1 + (1 - zz_)**2) / zz_, Nv)
        okm &= sp.simplify(ggq - CF * sp.Rational(Nv**2 + Nv + 2, (Nv - 1) * Nv * (Nv + 1))) == 0
        ggg = 2 * CA * (mel_D0(zz_, Nv) + mel_fun((1 - zz_) / zz_ + zz_ * (1 - zz_), Nv)) + beta0 / 2
        okm &= sp.simplify(ggg - (2 * CA * (sp.Rational(1, Nv * (Nv - 1)) + sp.Rational(1, (Nv + 1) * (Nv + 2)) - S1N) + beta0 / 2)) == 0
    if Nv == 1:
        okm &= sp.simplify(gqq) == 0                       # quark number
    if Nv == 2:
        okm &= sp.simplify(gqq + ggq) == 0                  # momentum, quark column
        okm &= sp.simplify(2 * nf * gqg + ggg) == 0         # momentum, gluon column
check('M7 gamma_qq, gamma_qg, gamma_gq, gamma_gg (VF-PDF-8) from the x-space kernels; quark-number and momentum sum rules', okm)
# A1 weak convergence without a rate: nu_Q = sin(Q^2 x) dx has all moments O(1/Q^2), but sup_{|phi|<=1} |int phi d nu_Q|
#    = int |sin(Q^2 x)| dx -> 2/pi (no uniform rate, not even convergence in total variation)
okw = True
for Qv in (5.0, 10.0, 20.0):
    q2v = Qv**2
    moms = [abs(q2v * mp.quad(lambda x: x**n * mp.sin(q2v * x), mp.linspace(0, 1, 40))) for n in (0, 2, 4, 6)]
    tv = mp.quad(lambda x: abs(mp.sin(q2v * x)), mp.linspace(0, 1, 400))
    okw &= max(moms) < 3.0 and abs(tv - 2 / mp.pi) < 0.02
check('A1 sin(Q^2 x): Q^2 * (moments) bounded, total variation -> 2/pi (weak convergence has no uniform rate)', okw)
# A2 Weierstrass in t = x^2: polynomial in x^2 approximating phi(x) = |x - 1/2| uniformly (Bernstein in t), error -> 0
def bern(f, n, t):
    return sum(f(mp.mpf(j) / n) * mp.binomial(n, j) * t**j * (1 - t)**(n - j) for j in range(n + 1))
phi = lambda x: abs(x - mp.mpf(1) / 2)
psi = lambda t: phi(mp.sqrt(t))
errs = []
for n in (10, 40, 160):
    errs.append(max(abs(bern(psi, n, x * x) - phi(x)) for x in mp.linspace(0, 1, 201)))
check('A2 polynomials in x^2 are dense in C([0,1]) (Bernstein approximation of psi(t)=phi(sqrt t)): sup errors decrease',
      errs[0] > errs[1] > errs[2] and errs[2] < 0.06, 'errors %s' % [mp.nstr(e_, 3) for e_ in errs])
# A3 product convention vs whole-term plus: g D_k = [g ln^k/(1-z)]_+ + c_k[g] delta, c_k[g] = int (g-g(1)) ln^k(1-z)/(1-z)
c1 = mp.quad(lambda zz: (zz**2 - 1) * mp.log(1 - zz) / (1 - zz), [0, 0.5, 1])
c0 = mp.quad(lambda zz: (zz**2 - 1) / (1 - zz), [0, 0.5, 1])
uu = sp.Symbol('u', positive=True)
c1x = sp.integrate(-(2 - uu) * sp.log(uu), (uu, 0, 1))       # u = 1 - z: (z^2-1)/(1-z) = -(1+z) = -(2-u)
check('A3 c_1[1+z^2] = 7/4 (VF-DY-12), c_0[1+z^2] = -3/2 (so (1+z^2)D_0 = [(1+z^2)/(1-z)]_+ - 3/2 delta)',
      abs(c1 - mp.mpf(7) / 4) < 1e-15 and abs(c0 + mp.mpf(3) / 2) < 1e-15 and sp.simplify(c1x - sp.Rational(7, 4)) == 0,
      'c1=%s (exact %s), c0=%s' % (mp.nstr(c1, 12), c1x, mp.nstr(c0, 12)))
# A4 example numbers for ex:prelim-plus: N = 2: B(2-e,-2e) = -1/(2e) - 1 - e(3 - zeta_2) + O(e^2)
Bv = sp.gamma(2 - e) * sp.gamma(-2 * e) / sp.gamma(2 - 3 * e)
ser2 = sp.series(Bv, e, 0, 2).removeO()
check('A4 N=2: B(2-e,-2e) = -1/(2e) - 1 - (3 - zeta_2) e + O(e^2)',
      sp.simplify(sp.expand(ser2 - (-1 / (2 * e) - 1 - (3 - sp.zeta(2)) * e))) == 0, str(sp.expand(ser2)))

print('\nSUMMARY s5: %d/%d PASS' % (sum(PASS), len(PASS)))
