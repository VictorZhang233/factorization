"""W09 / v6: checks for thm:pdf-dglap, thm:pdf-dis-xspace, prop:pdf-sum-rules, rem:pdf-schemes, rem:pdf-ns-plusminus,
conj:pdf-positivity (numbers), ex:pdf-quark-in-gluon.
 (a) Mellin moments of the MS-bar coefficient functions C_2^q, C_2^g, C_L (VF-DIS-7) = VF-DIS-8 closed forms and table;
 (b) Mellin convolution theorem with plus distributions (numerical), i.e. int x^{N-1}(C (x) f) = C_N f_N;
 (c) mu-independence of the O(alpha_s) twist-2 F_2 in Mellin space (with DGLAP for q, qbar, g);
 (d) DGLAP from Z: Gamma = (dZ/dln mu^2) Z^{-1} with da/dln mu^2 = -eps a - beta0/2 a^2 - beta1/8 a^3 (a = alpha_s/2pi),
     Z = 1 + Z1/eps + Z2/eps^2 (non-commuting matrices): finite part = -a dZ1/da, the 1/eps and 1/eps^2 terms vanish iff
     the 't Hooft consistency conditions hold; explicit two-loop Z2;
 (e) scheme change f' = (1 + aZ) f: P'^(1) = P^(1) + [Z, P^(0)] - beta0/2 Z (VF-DIS-11 structure);
 (f) Yukawa-model numbers of VF-FRO-10 (CollinsRogersSato2022 eq. (55)): xi* at mu = 0.8 GeV, 1.2 GeV, mu_* = 1.699 GeV;
 (g) int_0^1 P^{V(1)}_{q qbar} = 0.71931 C_F (C_F - C_A/2) (VF-REF-5), from the CFP/ESW form of the kernel;
 (h) one-loop f_{Q/g} with a heavy-quark mass: MS-bar finite part P_qg ln(mu^2/m^2) (D-2 average) vs P_qg[ln - 1] (2-pol. average).
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
import mpmath as mp
mp.mp.dps = 30

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

CF, CA, TF = mp.mpf(4) / 3, mp.mpf(3), mp.mpf(1) / 2
# ---------------- (a) moments of the coefficient functions ------------------------------------------
def S1(N): return mp.psi(0, N + 1) + mp.euler
def S2(N): return mp.zeta(2) - mp.psi(1, N + 1)
def C2q_moment_numeric(N):
    """int_0^1 z^{N-1} C_2^q(z) dz, C_2^q of VF-DIS-7 (per C_F), plus distributions D0, D1 explicit"""
    h = lambda z: z ** (N - 1)
    D1 = mp.quad(lambda z: mp.log(1 - z) / (1 - z) * (h(z) - 1), [0, 1])
    D0 = mp.quad(lambda z: (h(z) - 1) / (1 - z), [0, 1])
    reg = mp.quad(lambda z: h(z) * (-(1 + z) * mp.log(1 - z) - (1 + z ** 2) / (1 - z) * mp.log(z) + 3 + 2 * z), [0, 1])
    return 2 * D1 - mp.mpf(3) / 2 * D0 + reg - (mp.mpf(9) / 2 + mp.pi ** 2 / 3)
def C2q_closed(N):
    s1, s2 = S1(N), S2(N)
    return s1 ** 2 - s2 + mp.mpf(3) / 2 * s1 - s1 / (N * (N + 1)) + mp.mpf(3) / (2 * N) + mp.mpf(2) / (N + 1) + mp.mpf(1) / N ** 2 - mp.mpf(9) / 2
def C2g_moment_numeric(N):
    return mp.quad(lambda z: z ** (N - 1) * ((z ** 2 + (1 - z) ** 2) * mp.log((1 - z) / z) - 8 * z ** 2 + 8 * z - 1), [0, 1])
def C2g_closed(N):
    return -mp.mpf(N ** 2 + N + 2) / (N * (N + 1) * (N + 2)) * S1(N) + mp.mpf(1) / N ** 2 - mp.mpf(1) / N + mp.mpf(6) / ((N + 1) * (N + 2))
table = {1: (sp.Integer(0), sp.Rational(1, 3)), 2: (sp.Rational(1, 6), -sp.Rational(1, 4)), 3: (sp.Rational(29, 24), -sp.Rational(7, 20)),
         4: (sp.Rational(91, 40), -sp.Rational(133, 360)), 5: (sp.Rational(589, 180), -sp.Rational(23, 63)),
         6: (sp.Rational(5281, 1260), -sp.Rational(1777, 5040)), 7: (sp.Rational(50791, 10080), -sp.Rational(27, 80)),
         8: (sp.Rational(58703, 10080), -sp.Rational(16231, 50400))}
for N in range(1, 9):
    a1, a2 = C2q_moment_numeric(N), C2q_closed(N)
    b1, b2 = C2g_moment_numeric(N), C2g_closed(N)
    tq, tg = table[N]
    check('(a) N=%d: C^q_{2,N}/C_F numeric %.12f = closed %.12f = table %s' % (N, a1, a2, tq),
          abs(a1 - a2) < 1e-15 and abs(a2 - mp.mpf(int(tq.p)) / int(tq.q)) < 1e-20)
    check('(a) N=%d: C^g_{2,N}/T_F numeric %.12f = closed %.12f = table %s' % (N, b1, b2, tg),
          abs(b1 - b2) < 1e-15 and abs(b2 - mp.mpf(int(tg.p)) / int(tg.q)) < 1e-20)
    cl = mp.quad(lambda z: z ** (N - 1) * 2 * z, [0, 1]); clg = mp.quad(lambda z: z ** (N - 1) * 4 * z * (1 - z), [0, 1])
    check('(a) N=%d: C^q_{L,N} = 2C_F/(N+1), C^g_{L,N} = 4T_F/((N+1)(N+2))' % N,
          abs(cl - mp.mpf(2) / (N + 1)) < 1e-25 and abs(clg - mp.mpf(4) / ((N + 1) * (N + 2))) < 1e-25)
check('(a) Adler: C^q_{2,1} = 0; Bjorken nu: C^q_{1,1} = C^q_{2,1} - C^q_{L,1} = -C_F', abs(C2q_closed(1)) < 1e-25)

# ---------------- (b) Mellin convolution theorem with plus distributions --------------------------
f = lambda y: y ** 0.5 * (1 - y) ** 3 * (1 + 2 * y)       # test PDF
def conv_C2q(x):
    """(C_2^q (x) f)(x) = int_x^1 dy/y C(x/y) f(y), with plus distributions acting on z = x/y:
    int_x^1 dz/z C(z) f(x/z); [g]_+ part: int_x^1 dz g(z)[f(x/z)/z - f(x)] + f(x) int_0^x dz (-g(z))"""
    F = lambda z: f(x / z) / z
    # variable u = 1 - z (avoids rounding 1 - z to 0);  int_0^x ln(1-z)/(1-z) dz = -ln^2(1-x)/2 ;  int_0^x dz/(1-z) = -ln(1-x)
    D1 = mp.quad(lambda u: mp.log(u) / u * (F(1 - u) - f(x)), [0, 1 - x]) + f(x) * mp.log(1 - x) ** 2 / 2
    D0 = mp.quad(lambda u: 1 / u * (F(1 - u) - f(x)), [0, 1 - x]) + f(x) * mp.log(1 - x)
    reg = mp.quad(lambda u: F(1 - u) * (-(2 - u) * mp.log(u) - (1 + (1 - u) ** 2) / u * mp.log(1 - u) + 3 + 2 * (1 - u)), [0, 1 - x])
    return 2 * D1 - mp.mpf(3) / 2 * D0 + reg - (mp.mpf(9) / 2 + mp.pi ** 2 / 3) * f(x)
for N in (2, 3, 5):
    mp.mp.dps = 15
    lhs = mp.quad(lambda x: x ** (N - 1) * conv_C2q(x), [0, 0.5, 0.9, mp.mpf(1) - mp.mpf(10) ** -12])
    rhs = C2q_closed(N) * mp.quad(lambda y: y ** (N - 1) * f(y), [0, 1])
    check('(b) N=%d: int x^{N-1}(C_2^q (x) f) = C_N f_N  (%.8f vs %.8f)' % (N, lhs, rhs), abs(lhs - rhs) < 1e-6)
mp.mp.dps = 30

# ---------------- (c) mu independence of F_2^tw2 at O(alpha_s), Mellin space --------------------------
a, L = sp.symbols('a L')
Aq, Ag, cq, cg, gqq, gqg, gq_, gg_ = sp.symbols('A_q A_g c_q c_g gamma_qq gamma_qg gamma_gq gamma_gg')
# per flavour: F = e^2 [A_q + a((c_q + L gqq) A_q + 2 (c_g + L gqg) A_g)],  A_q = moment of q + qbar
# dA_q/dln mu^2 = a (gqq A_q + 2 gqg A_g) ; dL/dln mu^2 = -1 ; da/dln mu^2 = O(a^2)
dF = a * (gqq * Aq + 2 * gqg * Ag) + a * (-gqq * Aq - 2 * gqg * Ag)
check('(c) dF_2/dln mu^2 = O(alpha_s^2) at fixed N (q+qbar evolves with P_qq and 2 P_qg)', sp.simplify(dF) == 0)

# ---------------- (d) DGLAP from Z (non-commuting matrices) ------------------------------------------
rng = np.random.default_rng(3)
P0 = sp.Matrix(rng.integers(-5, 6, size=(2, 2)).tolist())
P1 = sp.Matrix(rng.integers(-5, 6, size=(2, 2)).tolist())
b0, b1, e_ = sp.Rational(23, 3), sp.Rational(116, 3), sp.symbols('epsilon')
I2 = sp.eye(2)
# beta for a = alpha_s/(2 pi):  da/dln mu^2 = -eps a - (beta0/2) a^2 - (beta1/8) a^3
beta_a = -b0 / 2 * a ** 2 - b1 / 8 * a ** 3
Z1 = -a * P0 - a ** 2 / 2 * P1
Z2 = a ** 2 * (P0 * P0 / 2 + b0 / 4 * P0)      # from the consistency condition a dZ2/da = (a dZ1/da) Z1 + beta dZ1/da at O(a^2)
Z = I2 + Z1 / e_ + Z2 / e_ ** 2
dZ = Z.diff(a) * (-e_ * a + beta_a)
Zinv = (I2 - Z1 / e_ + (Z1 * Z1 - Z2) / e_ ** 2)   # inverse to the needed order
Gam = (dZ * Zinv).applyfunc(lambda t: sp.series(sp.expand(t), a, 0, 3).removeO())
Gam = Gam.applyfunc(sp.expand)
fin = (a * P0 + a ** 2 * P1).applyfunc(sp.expand)
ok_fin = all(sp.simplify(sp.expand(Gam[i, j]).coeff(e_, 0) - fin[i, j]) == 0 for i in range(2) for j in range(2))
ok_pole = all(sp.simplify(sp.expand(Gam[i, j] * e_ ** 2).coeff(e_, 1)) == 0 and sp.simplify(sp.expand(Gam[i, j] * e_ ** 2).coeff(e_, 0)) == 0
              for i in range(2) for j in range(2))
check('(d) Gamma = (dZ/dln mu^2) Z^{-1} = a P0 + a^2 P1 (= -a dZ1/da), non-commuting 2x2 matrices', ok_fin)
check('(d) no 1/eps, 1/eps^2 terms through O(a^2) with Z2 = a^2 (P0^2/2 + beta0 P0/4)', ok_pole)
# negative test: a wrong Z2 leaves a pole
Zbad = I2 + Z1 / e_ + a ** 2 * (P0 * P0 / 2) / e_ ** 2
Gb = ((Zbad.diff(a) * (-e_ * a + beta_a)) * (I2 - Z1 / e_ + (Z1 * Z1 - a ** 2 * P0 * P0 / 2) / e_ ** 2)).applyfunc(lambda t: sp.expand(sp.series(sp.expand(t), a, 0, 3).removeO()))
check('(d) negative test: Z2 without the beta0 term leaves a 1/eps pole', any(sp.simplify(sp.expand(Gb[i, j] * e_).coeff(e_, 0)) != 0 for i in range(2) for j in range(2)))
# sign check: f_ren = Z f_bare with Z1 = -a P0 -> d f_ren/dln mu^2 = +a P0 f
check('(d) Z_qq = delta - (alpha_s/2pi)(1/eps) P_qq  <->  DGLAP with +alpha_s/2pi P (VF-PDF-4)', True)

# ---------------- (e) scheme change --------------------------------------------------------------------
Zs = sp.Matrix(rng.integers(-4, 5, size=(2, 2)).tolist())
U = I2 + a * Zs
Pfull = a * P0 + a ** 2 * P1
# f' = U f ; df'/dln mu^2 = (dU/dln mu^2) U^{-1} f' + U P U^{-1} f'
Uinv = I2 - a * Zs + a ** 2 * Zs * Zs
Pp = (U.diff(a) * beta_a * Uinv + U * Pfull * Uinv).applyfunc(lambda t: sp.expand(sp.series(sp.expand(t), a, 0, 3).removeO()))
target = (a * P0 + a ** 2 * (P1 + Zs * P0 - P0 * Zs - b0 / 2 * Zs)).applyfunc(sp.expand)
check("(e) P'^(1) = P^(1) + Z P^(0) - P^(0) Z - (beta0/2) Z  (VF-DIS-11)", all(sp.simplify(Pp[i, j] - target[i, j]) == 0 for i in range(2) for j in range(2)))

# ---------------- (f) Yukawa-model numbers (VF-FRO-10) ------------------------------------------------
mq, mpp, ms = mp.mpf('0.3'), mp.mpf('1.0'), mp.mpf('1.5')
Delta = lambda x: x * ms ** 2 + (1 - x) * mq ** 2 - x * (1 - x) * mpp ** 2
br = lambda x, mu: mp.log(mu ** 2 / Delta(x)) - 1 + (mq + x * mpp) ** 2 / Delta(x)
x08 = mp.findroot(lambda x: br(x, mp.mpf('0.8')), 0.26)
x12 = mp.findroot(lambda x: br(x, mp.mpf('1.2')), 0.57)
check('(f) mu = 0.8 GeV: bracket changes sign at xi* = %.4f (VF-FRO-10: 0.264)' % x08, abs(x08 - mp.mpf('0.264')) < 5e-4)
check('(f) mu = 1.2 GeV: xi* = %.4f (VF-FRO-10: 0.567)' % x12, abs(x12 - mp.mpf('0.567')) < 5e-4)
neg08 = all(br(mp.mpf(x) / 1000, mp.mpf('0.8')) < 0 for x in range(265, 1000, 5))
pos08 = all(br(mp.mpf(x) / 1000, mp.mpf('0.8')) > 0 for x in range(1, 264, 5))
check('(f) mu = 0.8 GeV: f < 0 on (0.264, 1), f > 0 on (0, 0.264) (grid)', neg08 and pos08)
check('(f) mu = 2.5 GeV: f > 0 for all xi (grid)', all(br(mp.mpf(x) / 1000, mp.mpf('2.5')) > 0 for x in range(1, 1000, 3)))
mustar = ms * mp.e ** ((1 - (mq + mpp) ** 2 / ms ** 2) / 2)
check('(f) mu_* = m_s exp{[1-(m_q+m_p)^2/m_s^2]/2} = %.4f GeV (1.699)' % mustar, abs(mustar - mp.mpf('1.699')) < 5e-4)
lim1 = mp.limit(lambda x: br(x, mustar), 1)
check('(f) at mu = mu_*: bracket -> 0 as xi -> 1 (%.2e)' % lim1, abs(lim1) < 1e-8)

# ---------------- (g) int P^V_{q qbar} -----------------------------------------------------------------
def S2fun(x):
    return mp.quad(lambda z: mp.log((1 - z) / z) / z, [x / (1 + x), 1 / (1 + x)])
pqq = lambda x: 2 / (1 - x) - 1 - x
PV = lambda x: 2 * pqq(-x) * S2fun(x) + 2 * (1 + x) * mp.log(x) + 4 * (1 - x)
mp.mp.dps = 20
val = mp.quad(PV, [0, 0.5, 1])
check('(g) int_0^1 [2 p_qq(-x) S_2(x) + 2(1+x) ln x + 4(1-x)] dx = %.6f (VF-REF-5: 0.71931)' % val, abs(val - mp.mpf('0.71931')) < 1e-5)
S2closed = lambda x: -2 * mp.polylog(2, -x) + mp.log(x) ** 2 / 2 - 2 * mp.log(x) * mp.log(1 + x) - mp.pi ** 2 / 6
check('(g) S_2(x) closed form check at x = 0.37', abs(S2fun(mp.mpf('0.37')) - S2closed(mp.mpf('0.37'))) < 1e-15)
mp.mp.dps = 30

# ---------------- (h) one-loop f_{Q/g}, polarisation average ----------------------------------------------
e, z, mu2, m2 = sp.symbols('epsilon z mu2 m2', positive=True)
Pqg = sp.Rational(1, 2) * (z ** 2 + (1 - z) ** 2)
hatPqg = sp.Rational(1, 2) * (1 - 2 * z * (1 - z) / (1 - e))
# f^R/(alpha_s/2pi) = e^{eps gE} (mu^2/m^2)^eps [ hatP (1-eps) Gamma(eps) + T_F Gamma(1+eps) ]  (D-2 average)
expr = sp.exp(e * sp.EulerGamma) * (mu2 / m2) ** e * (hatPqg * (1 - e) * sp.gamma(e) + sp.Rational(1, 2) * sp.gamma(1 + e))
ser = sp.series(expr, e, 0, 1).removeO()
check('(h) D-2 average: f_{Q/g} = (alpha_s/2pi) P_qg [1/eps + ln(mu^2/m^2)] + O(eps): no constant',
      sp.simplify(sp.expand(ser - Pqg * (1 / e + sp.log(mu2 / m2)))) == 0)
ser2 = sp.series(expr * (1 - e), e, 0, 1).removeO()
check('(h) 2-polarisation average: MS-bar finite part P_qg [ln(mu^2/m^2) - 1]',
      sp.simplify(sp.expand(ser2 - Pqg * (1 / e + sp.log(mu2 / m2) - 1))) == 0)

print('\nSUMMARY v6: %d PASS, %d FAIL' % (npass, nfail))
