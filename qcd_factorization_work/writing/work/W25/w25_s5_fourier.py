#!/usr/bin/env python3
"""W25 / Ch22 -- s5: the Fourier step (lem:lamet-fourier, cor:lamet-endpoint, lem:lamet-strip, prop:lamet-truncation,
prop:lamet-slepian, ex:lamet-fourier-numbers) and the harmonic majorant used in the proof of thm:lamet-exp-decay.

F1  Fourier lemma: int dlam/(2pi) e^{-i x lam} [z^2 Lam^2 r(lam)] = +(Lam^2/P_z^2) rho''(x),  z^2 = -lam^2/P_z^2
    numerically for rho(alpha) = (1-alpha^2)^6 (r(lambda) closed form via quadrature), x = 0, 0.35, 0.7
F2  endpoint ratios rho''/rho -> a(a-1)/x^2, b(b-1)/(1-x)^2 ; corollary: rho4 = q (1-x)^delta, q ~ (1-x)^b
    -> rho4''/q ~ (b+delta)(b+delta-1)(1-x)^(delta-2)
F3  analyticity strip: Lorentzian prototype e^{-m|lam|/P^z} -> (1/pi) d/(d^2+x^2), poles at x = +-i m/P^z
F4  truncation bound: |int_{|lam|>lamL} dlam/(2pi) e^{-ix lam} h| <= A P^z/(pi m) e^{-m z_L}; numbers for m = 0.5 GeV,
    z_L = 1 fm, 1.5 fm; lamL = z_L P^z for P^z = 2 GeV
F5  time-frequency limiting operator on [-1,1]: trace 2 lamL/pi, number of eigenvalues > 1/2 for lamL = 5,10,15,25 and
    lamL = 10.14; Landau-Widom count
F6  harmonic majorant for the exponential-decay proof: v(w) = Re sqrt(R^2 - w^2) on C \ ((-inf,-R] u [R,inf)):
    harmonic, = 0 on the cuts, = R at w = 0, Re sqrt(R^2-w^2) - |Im w| -> 0 at infinity, Re sqrt >= |Im w|
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
import numpy as np

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

mp.mp.dps = 25
# ---------------------------------------------------------------- F1
al, x, lam = sp.symbols('alpha x lambda', real=True)
rho = (1 - al**2)**6
# r(lambda) = int_{-1}^1 (1-a^2)^6 e^{i a lambda} da = sqrt(pi) Gamma(7) (2/lambda)^{6.5} J_{6.5}(lambda)  (numerically stable)
def rf(l):
    l = mp.mpf(l)
    if abs(l) < mp.mpf('1e-8'):
        return mp.quad(lambda a: (1 - a**2)**6, [-1, 1])
    return mp.sqrt(mp.pi) * mp.gamma(7) * (2 / l)**mp.mpf(6.5) * mp.besselj(mp.mpf(6.5), l)
check("F1 Bessel representation of r(lambda) agrees with direct quadrature at lambda=3.7",
      abs(rf(3.7) - mp.quad(lambda a: (1 - a**2)**6 * mp.cos(a * mp.mpf(3.7)), [-1, 1])) < 1e-18)
rho2 = sp.lambdify(al, sp.diff(rho, al, 2), 'mpmath')
for xv in (0.0, 0.35, 0.7):
    # int dlam/(2pi) e^{-i x lam} (-lam^2) r(lam) = rho''(x)   (Lam^2/P_z^2 factored out); r even -> cosine transform
    f1 = lambda l: -l**2 * rf(l) * mp.cos(xv * l)
    val = (mp.quad(f1, mp.linspace(0, 60, 61)) + mp.quadosc(f1, [60, mp.inf], omega=1 + xv)) / mp.pi
    check("F1 Fourier lemma: FT[-lambda^2 r](x=%.2f) = rho''(x)" % xv, abs(val - rho2(xv)) < 1e-6,
          "%s vs %s" % (mp.nstr(val, 10), mp.nstr(rho2(xv), 10)))
check("F1 sign: z^2 Lam^2 r = -(Lam^2/P_z^2) lambda^2 r and lambda^2 e^{-ix lambda} = -d_x^2 e^{-ix lambda}",
      sp.simplify(lam**2 * sp.exp(-sp.I * x * lam) + sp.diff(sp.exp(-sp.I * x * lam), x, 2)) == 0)

# ---------------------------------------------------------------- F2
a_, b_, d_ = sp.symbols('a b delta', positive=True)
okA = okB = True
for av, bv in ((0.7, 3.2), (1.5, 2.0), (0.3, 4.5)):
    fnum = x**sp.nsimplify(av) * (1 - x)**sp.nsimplify(bv)
    rA = sp.simplify(sp.diff(fnum, x, 2) / fnum)
    okA &= abs(float(sp.N((rA * x**2).subs(x, sp.Rational(1, 10**6)))) - av * (av - 1)) < 1e-4
    okB &= abs(float(sp.N((rA * (1 - x)**2).subs(x, 1 - sp.Rational(1, 10**6)))) - bv * (bv - 1)) < 1e-4
check("F2 rho''/rho -> a(a-1)/x^2 at x->0 (three (a,b) pairs)", okA)
check("F2 rho''/rho -> b(b-1)/(1-x)^2 at x->1 (three (a,b) pairs)", okB)
q = (1 - x)**b_ * (1 + x)          # generic q ~ (1-x)^b
rho4 = q * (1 - x)**d_
ratio = sp.simplify(sp.diff(rho4, x, 2) / q * (1 - x)**(2 - d_))
check("F2 corollary: rho4''/q * (1-x)^(2-delta) -> (b+delta)(b+delta-1)",
      sp.simplify(sp.limit(ratio, x, 1) - (b_ + d_) * (b_ + d_ - 1)) == 0)
for dv in (0, 1):
    print("   delta=%d: relative correction ~ Lam^2/P_z^2 * (1-x)^(%d)" % (dv, dv - 2))

# ---------------------------------------------------------------- F3
m, Pz = sp.symbols('m P_z', positive=True)
dd = m / Pz
lor = sp.integrate(sp.exp(-dd * lam) * sp.cos(x * lam), (lam, 0, sp.oo), conds='none') / sp.pi
check("F3 FT of e^{-m|lam|/P^z} = (1/pi) d/(d^2+x^2), d = m/P^z (poles at x = +-i m/P^z)",
      sp.simplify(lor - dd / (sp.pi * (dd**2 + x**2))) == 0)

# ---------------------------------------------------------------- F4
hbarc = mp.mpf('0.1973')            # GeV fm
mm = mp.mpf('0.5')
for zL in (mp.mpf(1), mp.mpf('1.5')):
    print("   z_L = %s fm: m z_L = %s, e^{-m z_L} = %s" % (zL, mp.nstr(mm * zL / hbarc, 5), mp.nstr(mp.e**(-mm * zL / hbarc), 4)))
check("F4 e^{-m z_L} = 0.079 (z_L = 1 fm), 0.022 (z_L = 1.5 fm) for m = 0.5 GeV",
      abs(mp.e**(-mm / hbarc) - mp.mpf('0.0794')) < 5e-4 and abs(mp.e**(-mm * 1.5 / hbarc) - mp.mpf('0.0224')) < 5e-4)
lamL = 1 / hbarc * 2
check("F4 lambda_L = z_L P^z = 10.14 for z_L = 1 fm, P^z = 2 GeV", abs(lamL - mp.mpf('10.137')) < 1e-2, mp.nstr(lamL, 5))
# bound: 2 * int_{lamL}^inf A e^{-m lam/P^z} dlam/(2pi) = A P^z/(pi m) e^{-m lamL/P^z}
Pzv = mp.mpf(2); A = mp.mpf(1)
tail = 2 * mp.quad(lambda l: A * mp.e**(-mm * l / Pzv), [lamL, mp.inf]) / (2 * mp.pi)
check("F4 tail integral = A P^z/(pi m) e^{-m z_L}", abs(tail - A * Pzv / (mp.pi * mm) * mp.e**(-mm * lamL / Pzv)) < 1e-20)
print("   bound A P^z/(pi m) e^{-m z_L} for P^z = 2 GeV, z_L = 1 fm: %s A" % mp.nstr(A * Pzv / (mp.pi * mm) * mp.e**(-mm / hbarc), 4))

# ---------------------------------------------------------------- F5 Slepian / Landau-Widom
def eig_count(L, n=1600):
    # Gauss-Legendre discretisation of (Kf)(x) = int_{-1}^1 sin(L(x-y))/(pi(x-y)) f(y) dy  (symmetrised)
    xg, wg = np.polynomial.legendre.leggauss(n)
    X, Y = np.meshgrid(xg, xg, indexing='ij')
    D = X - Y
    K = np.where(np.abs(D) < 1e-14, L / np.pi, np.sin(L * D) / (np.pi * np.where(np.abs(D) < 1e-14, 1, D)))
    sw = np.sqrt(wg)
    Ks = sw[:, None] * K * sw[None, :]
    ev = np.linalg.eigvalsh(Ks)
    return ev
res = {}
for L in (5, 10, 15, 25, 10.137):
    ev = eig_count(L)
    res[L] = (int(np.sum(ev > 0.5)), float(np.sum(ev)), 2 * L / np.pi, int(np.sum(ev > 0.99)), int(np.sum(ev > 0.01)))
    print("   lambda_L=%6.3f: #(eig>1/2)=%d, trace=%.4f (2L/pi=%.4f), #(eig>0.99)=%d, #(eig>0.01)=%d" % ((L,) + res[L]))
check("F5 #eigenvalues > 1/2 = 3, 6, 10, 16 for lambda_L = 5, 10, 15, 25",
      [res[L][0] for L in (5, 10, 15, 25)] == [3, 6, 10, 16])
check("F5 trace = 2 lambda_L/pi", all(abs(res[L][1] - res[L][2]) < 1e-6 for L in (5, 10, 15, 25)))
check("F5 lambda_L = 10.14 (P^z = 2 GeV, z_L = 1 fm): about six modes", res[10.137][0] == 6)
# Landau-Widom: N(eps) = 2L/pi + (1/pi^2) ln((1-eps)/eps) ln L + o(ln L)
for L in (25,):
    ev = eig_count(L)
    for eps in (0.1, 0.01):
        Nn = int(np.sum(ev > eps)); pred = 2 * L / np.pi + np.log((1 - eps) / eps) * np.log(L) / np.pi**2
        print("   Landau-Widom check L=%d eps=%.2f: N=%d, formula %.2f" % (L, eps, Nn, pred))
        check("F5 Landau-Widom count at L=%d, eps=%.2f within 2 of the asymptotic formula (o(ln L) corrections)" % (L, eps), abs(Nn - pred) < 2)

# ---------------------------------------------------------------- F6 harmonic majorant
R = 1.3
def g(w):                           # branch of sqrt(R^2 - w^2) analytic on C minus the cuts, positive on (-R, R)
    w = complex(w)
    s = np.sqrt(complex(R**2 - w**2))
    # choose the branch with Re >= 0 (principal sqrt has Re >= 0 automatically)
    return s
# harmonic: Laplacian of Re g by finite differences at a few points
ok = True
for w in (0.3 + 0.7j, -2.0 + 0.4j, 1.7 - 1.1j, 0.2 - 3.0j):
    h = 1e-3
    lap = (g(w + h).real + g(w - h).real + g(w + 1j * h).real + g(w - 1j * h).real - 4 * g(w).real) / h**2
    ok &= abs(lap) < 1e-4
check("F6 Re sqrt(R^2-w^2) harmonic off the cuts (finite-difference Laplacian ~ 0)", ok)
check("F6 = 0 on the cuts (|t| > R, approached from either side) and = R at w = 0",
      abs(g(2.0 + 1e-12j).real) < 1e-9 and abs(g(-3.0 - 1e-12j).real) < 1e-9 and abs(g(0).real - R) < 1e-12)
ok = all(g(w).real >= abs(w.imag) - 1e-12 for w in (0.1 + 0.2j, 5 + 0.1j, -7 - 3j, 0.5 - 20j, 30 + 30j))
check("F6 Re sqrt(R^2 - w^2) >= |Im w| (so the half-plane bound alone does not give the decay at w=0)", ok)
ok = all(abs(g(w).real - abs(w.imag)) < 2 * R**2 / abs(w) for w in (100 + 3j, -80 - 50j, 1j * 200, 300 - 1j))
check("F6 Re sqrt(R^2 - w^2) - |Im w| = O(R^2/|w|) at infinity", ok)
# continuity of Re g across the real axis inside (-R,R) and its sign
check("F6 no cut on (-R,R): g(t+i0) = g(t-i0) > 0", abs(g(0.5 + 1e-12j) - g(0.5 - 1e-12j)) < 1e-9 and g(0.5).real > 0)

print("\nSUMMARY w25_s5_fourier: %d PASS, %d FAIL" % (NP, NF))
