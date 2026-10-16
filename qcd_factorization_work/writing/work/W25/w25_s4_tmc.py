#!/usr/bin/env python3
"""W25 / Ch22 -- s4: exact target-mass corrections (prop:lamet-tmc, ex:lamet-tmc-moments).

Conventions (book): z^mu = z e_z^mu, P = (P^0,0,0,P^z), lambda = P.z = -P^z z, c = M^2/(4 P_z^2),
h_Gamma = <O_Gamma>/(2 P^Gamma) with P^{gamma^0} = P^0, P^{gamma^z} = P^z; <P|O^{mu1..muN}|P> = 2 a_N (P..P - traces).

M1  T_N(z) = z_{mu1}..z_{muN}(P^{mu1}..P^{muN} - traces) = sum_i binom(N-i,i)(-P^2 z^2/4)^i (P.z)^{N-2i}:
    harmonic (box_z T_N = 0) and unique among homogeneous polynomials with leading term (P.z)^N (d = 4); recursion
    beta_k/beta_{k-1} = -(N-2k+2)(N-2k+1)/(4k(N-k+1)).
M2  Taylor expansion convention: W[0,-z] psi(-z) = sum_k (i^k/k!) (z.iD)^k psi(0)  =>  <P|O_{gamma^alpha}(z)|P> = 2P^alpha sum_n (i lambda)^n/n! a_{n+1}
    (tree-level plane-wave check).
M3  gamma^z: (1/N) dT_N/dz_alpha (alpha=3) / (P^z (P.z)^{N-1}) = K_N = sum_i binom(N-i,i) c^i ;
    gamma^0: (1/N) dT_N/dz_alpha (alpha=0) / (P^0 (P.z)^{N-1}) = Kperp_N = sum_i binom(N-i,i) (N-2i)/N c^i = K_N - (2c/N) K_N';
    the extra twist-2 structure (z^alpha/z^2) T_N for gamma^z also gives K_N.
M4  explicit values N <= 4 and K_N = (r_+^{N+1}-r_-^{N+1})/(r_+-r_-), r_pm = (1 pm sqrt(1+4c))/2, recursion K_N = K_{N-1} + c K_{N-2}.
M5  x space (numerics, quark + antiquark test function, breakpoints at 0 and at the support edges):
    Chen et al. gamma^z closed form has moments K_N a_N; gamma^0 formula q_z - 2c int_0^1 dy/y d_c q_z(x/y) has moments Kperp_N a_N;
    inverse series reproduces q.
M6  O(c): q - c(xq'+q) [gamma^z], q - c(xq'+3q) + 2c int_{|x|}^1 dy/y q(x/y) [gamma^0]  (moments, symbolic in N; numerics).
M7  order of TMC and matching: C (x)_{P^z} D_s q = D_s (C (x)_{s P^z} q) for D_s q(x) = s q(x/s) (exact dilatation identity),
    hence C (x) q_M differs from TMC[C (x) q] at O(alpha_s c).
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

z0, z1, z2, z3, P0, P3, c = sp.symbols('z0 z1 z2 z3 P0 P3 c', real=True)
Z = [z0, z1, z2, z3]; eta = [1, -1, -1, -1]
Pv = [P0, 0, 0, P3]
Pz = sum(eta[m] * Pv[m] * Z[m] for m in range(4))            # P.z
z2s = sum(eta[m] * Z[m]**2 for m in range(4))                 # z^2
P2 = P0**2 - P3**2
def box(f): return sum(eta[m] * sp.diff(f, Z[m], 2) for m in range(4))
def TN(N): return sum(sp.binomial(N - i, i) * (-P2 * z2s / 4)**i * Pz**(N - 2 * i) for i in range(N // 2 + 1))

# ---------------- M1 ----------------
check("M1 T_N harmonic (box_z T_N = 0) for N=1..8", all(sp.expand(box(TN(N))) == 0 for N in range(1, 9)))
ok = True
for N in range(2, 8):
    betas = sp.symbols('b1:%d' % (N // 2 + 1))
    cand = Pz**N + sum(betas[k - 1] * (P2 * z2s)**k * Pz**(N - 2 * k) for k in range(1, N // 2 + 1))
    sol = sp.solve(sp.Poly(sp.expand(box(cand)), *Z).coeffs(), betas, dict=True)
    ok &= len(sol) == 1 and all(sp.simplify(sol[0][betas[k - 1]] - sp.binomial(N - k, k) * (-sp.Rational(1, 4))**k) == 0
                                for k in range(1, N // 2 + 1))
check("M1 uniqueness: harmonic ansatz fixes beta_k = binom(N-k,k)(-1/4)^k, N=2..7", ok)
Nn, kk = sp.symbols('N k', positive=True, integer=True)
ratio = sp.combsimp(sp.binomial(Nn - kk, kk) / sp.binomial(Nn - kk + 1, kk - 1) * (-sp.Rational(1, 4)))
check("M1 recursion beta_k/beta_{k-1} = -(N-2k+2)(N-2k+1)/(4k(N-k+1))",
      sp.simplify(ratio + (Nn - 2 * kk + 2) * (Nn - 2 * kk + 1) / (4 * kk * (Nn - kk + 1))) == 0)
# the recursion as derived from box acting on (z^2)^k (P.z)^{N-2k} in d=4 (coefficients 4k(N-k+1) and (N-2k+2)(N-2k+1))
ok = True
for N in range(2, 8):
    for k in range(1, N // 2 + 1):
        term_k = (P2 * z2s)**k * Pz**(N - 2 * k)
        term_km1 = (P2 * z2s)**(k - 1) * Pz**(N - 2 * k + 2)
        target = P2**k * z2s**(k - 1) * Pz**(N - 2 * k)
        # coefficient of target in box(term_k) and box(term_km1): compare by evaluating at a random point after removing other structure
        bk = sp.expand(box(term_k)); bkm1 = sp.expand(box(term_km1))
        pt = {z0: sp.Rational(3, 7), z1: sp.Rational(2, 5), z2: -sp.Rational(1, 3), z3: sp.Rational(5, 4), P0: sp.Rational(7, 3), P3: sp.Rational(1, 2)}
        # predicted: box(term_k) = P2^k[4k(N-k+1) z2^{k-1} Pz^{N-2k} + (N-2k)(N-2k-1) P2 z2^k Pz^{N-2k-2}]
        pred_k = P2**k * (4 * k * (N - k + 1) * z2s**(k - 1) * Pz**(N - 2 * k) + (N - 2 * k) * (N - 2 * k - 1) * P2 * z2s**k * Pz**(N - 2 * k - 2 if N - 2 * k - 2 >= 0 else 0) * (1 if N - 2 * k - 2 >= 0 else 0))
        ok &= sp.simplify((bk - pred_k).subs(pt)) == 0
check("M1 box[(P^2 z^2)^k (P.z)^{N-2k}] = P^{2k}[4k(N-k+1) z^{2(k-1)}(P.z)^{N-2k} + (N-2k)(N-2k-1)P^2 z^{2k}(P.z)^{N-2k-2}] (d=4)", ok)

# ---------------- M2 ----------------
# plane-wave check: psi ~ u e^{-i p.x}; (z.iD)^k psi(0) -> (p.z)^k psi; sum_k i^k (p.z)^k/k! = e^{i p.z}; psibar(z) psi(0) ~ e^{+ip.z}
pz_s = sp.Symbol('pz', real=True)
ser = sum((sp.I * pz_s)**k / sp.factorial(k) for k in range(12))
check("M2 sum_k i^k (p.z)^k/k! reproduces e^{i p.z} (tree-level <p|psibar(z) G psi(0)|p> = ubar G u e^{i p.z})",
      sp.simplify(sp.series(sp.exp(sp.I * pz_s), pz_s, 0, 12).removeO() - ser) == 0)
check("M2 p.z = -p^z z for z^mu = z e_z^mu, so e^{i p.z} = e^{-i p^z z} = e^{i lambda}", True)

# ---------------- M3 ----------------
Mm = sp.Symbol('M', positive=True); Pzv = sp.Symbol('P_z', positive=True); zs = sp.Symbol('zs', real=True)
sub = {z0: 0, z1: 0, z2: 0, z3: zs, P0: sp.sqrt(Mm**2 + Pzv**2), P3: Pzv}
def KN(N): return sum(sp.binomial(N - i, i) * c**i for i in range(N // 2 + 1))
def KperpN(N): return sum(sp.binomial(N - i, i) * sp.Rational(N - 2 * i, N) * c**i for i in range(N // 2 + 1))
cval = Mm**2 / (4 * Pzv**2)
okz = okt = okzz = True
for N in range(1, 9):
    T = TN(N)
    # T^{alpha mu..} z_mu.. = (1/N) dT/dz_alpha (lower index) = (1/N) eta[a] dT/dZ[a]  (Z contravariant)
    contr_z = eta[3] * sp.diff(T, z3) / N
    hz = sp.simplify((contr_z / P3).subs(sub) / (Pz.subs(sub))**(N - 1))
    okz &= sp.simplify(hz - KN(N).subs(c, cval)) == 0
    contr_t = eta[0] * sp.diff(T, z0) / N
    ht = sp.simplify((contr_t / P0).subs(sub) / (Pz.subs(sub))**(N - 1))
    okt &= sp.simplify(ht - KperpN(N).subs(c, cval)) == 0
    # second twist-2 structure for gamma^z: (z^alpha/z^2) T_N(z), alpha = 3 (z^3 = zs)
    hzz = sp.simplify(((Z[3] / z2s) * T / P3).subs(sub) / (Pz.subs(sub))**(N - 1))
    okzz &= sp.simplify(hzz - KN(N).subs(c, cval)) == 0
check("M3 gamma^z: (1/N) dT_N/dz_3 /(P^z lambda^{N-1}) = K_N (incl. trace terms), N=1..8", okz)
check("M3 gamma^0: (1/N) dT_N/dz_0 /(P^0 lambda^{N-1}) = Kperp_N, N=1..8", okt)
check("M3 gamma^z: the structure (z^alpha/z^2) T_N(z) also gives K_N (same moment factor)", okzz)
check("M3 -P^2 z^2/(4 (P.z)^2) = c = M^2/(4P_z^2) at z = z e_z (z-independent)",
      sp.simplify((-P2 * z2s / (4 * Pz**2)).subs(sub) - cval) == 0)
check("M3 identity Kperp_N = K_N - (2c/N) dK_N/dc, N=1..40",
      all(sp.simplify(KperpN(N) - (KN(N) - 2 * c / N * sp.diff(KN(N), c))) == 0 for N in range(1, 41)))

# ---------------- M4 ----------------
vals = [(sp.expand(KN(N)), sp.expand(KperpN(N))) for N in range(1, 7)]
print("   K_N, Kperp_N (N=1..6):", vals)
check("M4 K_1..4 = 1, 1+c, 1+2c, 1+3c+c^2 ; Kperp_1..4 = 1, 1, 1+2c/3, 1+3c/2",
      [v[0] for v in vals[:4]] == [1, 1 + c, 1 + 2 * c, 1 + 3 * c + c**2]
      and [v[1] for v in vals[:4]] == [1, 1, 1 + 2 * c / 3, 1 + sp.Rational(3, 2) * c])
rp = (1 + sp.sqrt(1 + 4 * c)) / 2; rm = (1 - sp.sqrt(1 + 4 * c)) / 2
check("M4 K_N = (r+^{N+1} - r-^{N+1})/(r+ - r-), r_pm = (1 pm sqrt(1+4c))/2, N=0..12",
      all(sp.simplify(sp.expand((rp**(N + 1) - rm**(N + 1)) / (rp - rm)) - (KN(N) if N > 0 else 1)) == 0 for N in range(0, 13)))
check("M4 recursion K_N = K_{N-1} + c K_{N-2}", all(sp.expand(KN(N) - KN(N - 1) - c * KN(N - 2)) == 0 for N in range(3, 20)))
check("M4 f_+/2 = r_+ and -f_-/2 = r_- with f_pm = sqrt(1+4c) pm 1",
      sp.simplify((sp.sqrt(1 + 4 * c) + 1) / 2 - rp) == 0 and sp.simplify(-(sp.sqrt(1 + 4 * c) - 1) / 2 - rm) == 0)

# ---------------- M5 (numerics) ----------------
cv = 0.15
def qf(x):                       # q(x) for x>0 and -qbar(-x) for x<0, support [-1,1]
    if 0.0 < x < 1.0: return x**0.6 * (1 - x)**3
    if -1.0 < x < 0.0: return -0.4 * (-x)**0.6 * (1 + x)**5
    return 0.0
def fpm(cc): s = np.sqrt(1 + 4 * cc); return s + 1.0, s - 1.0
def qz(x, cc=cv):
    fp, fm = fpm(cc)
    return (fp / 2 * qf(2 * x / fp) - fm / 2 * qf(-2 * x / fm)) / np.sqrt(1 + 4 * cc)
fp, fm = fpm(cv); lo, hi = -fp / 2, fp / 2      # q has quark AND antiquark parts: support of q_z is [-f_+/2, f_+/2]
lo_q, hi_q = -fm / 2, fp / 2                     # support for a pure quark distribution (q supported in [0,1])
def moment(f, n, a, b, pts):
    tot = 0.0
    grid = [a] + sorted(p for p in pts if a < p < b) + [b]
    for u, v in zip(grid[:-1], grid[1:]):
        val, err = integrate.quad(lambda x: x**n * f(x), u, v, limit=400, epsabs=1e-14, epsrel=1e-12)
        tot += val
    return tot
aN = {N: moment(qf, N - 1, -1, 1, [0.0]) for N in range(1, 7)}
okm = True; worst = 0
for N in range(1, 7):
    m = moment(qz, N - 1, lo, hi, [0.0, -fm / 2, fm / 2])
    target = float(KN(N).subs(c, cv)) * aN[N]
    worst = max(worst, abs(m - target)); okm &= abs(m - target) < 1e-10
check("M5 gamma^z closed form (Chen et al.) has moments K_N a_N, N=1..6 (c=0.15)", okm, "max dev %.1e" % worst)
def dqz_dc(x, h=1e-5): return (qz(x, cv + h) - qz(x, cv - h)) / (2 * h)
def Aop(g, x):
    # A[g](x) = int_0^1 dy/y g(x/y); g supported in [lo,hi] => only y >= |x|/edge contributes
    if x == 0.0: return 0.0
    edge = hi if x > 0 else -lo
    ymin = abs(x) / edge
    if ymin >= 1.0: return 0.0
    val, err = integrate.quad(lambda y: g(x / y) / y, ymin, 1.0, limit=300, epsabs=1e-12, epsrel=1e-10,
                              points=[min(1.0, abs(x))] if ymin < abs(x) < 1.0 else None)
    return val
def qt(x): return qz(x) - 2 * cv * Aop(dqz_dc, x)
okt = True; worst = 0
for N in range(1, 6):
    m = moment(qt, N - 1, lo, hi, [0.0, -fm / 2, fm / 2, -0.6, 0.3, 0.7])
    target = float(KperpN(N).subs(c, cv)) * aN[N]
    worst = max(worst, abs(m - target)); okt &= abs(m - target) < 2e-6
check("M5 gamma^0 formula q_z - 2c int_0^1 dy/y d_c q_z(x/y) has moments Kperp_N a_N, N=1..5", okt, "max dev %.1e" % worst)
def qinv(x, nmax=60):
    s = 0.0
    for n in range(nmax):
        arg = fp**(n + 1) * x / (2 * fm**n)
        if abs(arg) > hi + 1: break
        s += fm**n / fp**(n + 1) * ((1 + (-1)**n) * qz(arg) + (1 - (-1)**n) * qz(-arg))
    return np.sqrt(1 + 4 * cv) * s
ok = all(abs(qinv(x) - qf(x)) < 1e-12 for x in (0.1, 0.37, 0.8, -0.2, -0.65))
check("M5 inverse series q(x) = sqrt(1+4c) sum_n f_-^n/f_+^{n+1}[...] reproduces q (5 points)", ok)
def qpure(x): return x**0.6 * (1 - x)**3 if 0.0 < x < 1.0 else 0.0
def qz_pure(x, cc=cv):
    fp_, fm_ = fpm(cc)
    return (fp_ / 2 * qpure(2 * x / fp_) - fm_ / 2 * qpure(-2 * x / fm_)) / np.sqrt(1 + 4 * cc)
xs = np.linspace(-1.3, 1.3, 26001)
nz = [x for x in xs if abs(qz_pure(x)) > 0]
check("M5 support of q_z for a pure quark q (supp in [0,1]): [-f_-/2, f_+/2] = [%.4f, %.4f] ~ [-c, 1+c] (c=%.2f); found [%.4f, %.4f]" % (lo_q, hi_q, cv, min(nz), max(nz)),
      abs(min(nz) - lo_q) < 2e-4 and abs(max(nz) - hi_q) < 2e-4 and abs(lo_q + cv) < 0.03 and abs(hi_q - 1 - cv) < 0.03)
nz2 = [x for x in xs if abs(qz(x)) > 0]
check("M5 with antiquarks (q(y<0) = -qbar(-y) nonzero) the support is [-f_+/2, f_+/2]: found [%.4f, %.4f]" % (min(nz2), max(nz2)),
      abs(min(nz2) + fp / 2) < 2e-4 and abs(max(nz2) - fp / 2) < 2e-4)
okq = True
for N in range(1, 6):
    m = moment(qz_pure, N - 1, lo_q, hi_q, [0.0])
    aq = moment(qpure, N - 1, 0, 1, [])
    okq &= abs(m - float(KN(N).subs(c, cv)) * aq) < 1e-10
check("M5 pure-quark case: moments K_N a_N on [-f_-/2, f_+/2], N=1..5", okq)

# ---------------- M6 ----------------
check("M6 gamma^z O(c): moments of -c(xq'+q) = c(N-1) a_N = O(c) part of K_N",
      all(sp.series(KN(N), c, 0, 2).removeO() == 1 + (N - 1) * c for N in range(1, 12)))
check("M6 gamma^0 O(c): moments of -c(xq'+3q) + 2c A[q] = c(N-3+2/N) a_N = c(N-1)(N-2)/N a_N = O(c) part of Kperp_N",
      sp.simplify(-(3 - Nn) + 2 / Nn - (Nn - 1) * (Nn - 2) / Nn) == 0 and
      all(sp.simplify(sp.series(KperpN(N), c, 0, 2).removeO() - (1 + c * sp.Rational((N - 1) * (N - 2), N))) == 0 for N in range(1, 12)))
# numerics of the O(c) gamma^0 form (with q smooth enough to differentiate: use q = x^2 (1-x)^3, antiquark -0.4 x^2(1-x)^5)
def q2(x):
    if 0 < x < 1: return x**2 * (1 - x)**3
    if -1 < x < 0: return -0.4 * x**2 * (1 + x)**5
    return 0.0
def q2p(x, h=1e-6): return (q2(x + h) - q2(x - h)) / (2 * h)
cs = 1e-3
def qt_oc(x):
    integ = 0.0
    if 0 < abs(x) < 1:
        integ, _ = integrate.quad(lambda y: q2(x / y) / y, abs(x), 1.0, limit=200)
    return q2(x) - cs * (x * q2p(x) + 3 * q2(x)) + 2 * cs * integ
a2 = {N: moment(q2, N - 1, -1, 1, [0.0]) for N in range(1, 6)}
ok = True
for N in range(1, 6):
    m = moment(qt_oc, N - 1, -1, 1, [0.0])
    ok &= abs(m - (1 + cs * (N - 1) * (N - 2) / N) * a2[N]) < 1e-9
check("M6 numerics: O(c) gamma^0 form reproduces 1 + c(N-1)(N-2)/N, N=1..5", ok)

# ---------------- M7 ----------------
def Ctoy(xi_, ell):              # smooth toy kernel with explicit dependence on the parton momentum through ell
    return np.exp(-(xi_ - 1)**2) * (1 + 0.3 * ell)
def conv(f, x, P, mu=1.0):
    val = 0.0
    for u, v in ((-1.5, -1), (-1, -0.5), (-0.5, 0), (0, 0.5), (0.5, 1), (1, 1.5)):   # dilated PDFs reach |y| = s > 1
        r, _ = integrate.quad(lambda y: Ctoy(x / y, np.log(mu / (abs(y) * P))) / abs(y) * f(y), u, v, limit=200)
        val += r
    return val
def q3(y):                       # smooth test pdf vanishing at y=0 so that the toy convolution converges
    if 0 < y < 1: return y**2 * (1 - y)**3
    if -1 < y < 0: return -0.4 * y**2 * (1 + y)**5
    return 0.0
s_ = 1.13
Ds = lambda f: (lambda x: s_ * f(x / s_))
x0 = 0.42
lhs = conv(Ds(q3), x0, 2.0)
rhs = Ds(lambda x: conv(q3, x, s_ * 2.0))(x0)
check("M7 C (x)_{P^z} D_s q = D_s (C (x)_{s P^z} q): matching at P^z of the dilated PDF = dilation of matching at s P^z",
      abs(lhs - rhs) < 1e-9, "%.12f vs %.12f" % (lhs, rhs))
wrong = Ds(lambda x: conv(q3, x, 2.0))(x0)
check("M7 ... while D_s (C (x)_{P^z} q) differs (order matters through the ln P^z dependence)", abs(wrong - lhs) > 1e-4,
      "%.3e" % (wrong - lhs))
# analytic: for the one-loop MSbar kernel, P^z d/dP^z acts as -2 d/d ell_p; dilation by s = 1 + c + O(c^2) changes ell_p by -2 ln s
check("M7 s_+ = f_+/2 = 1 + c + O(c^2): ln s = c + O(c^2), so TMC[C (x) q] - C (x) TMC[q] = O(alpha_s c)",
      sp.simplify(sp.series(sp.log((sp.sqrt(1 + 4 * c) + 1) / 2), c, 0, 2).removeO() - c) == 0)

print("\nSUMMARY w25_s4_tmc: %d PASS, %d FAIL" % (NP, NF))
