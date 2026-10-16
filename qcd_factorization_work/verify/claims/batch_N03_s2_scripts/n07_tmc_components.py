#!/usr/bin/env python3
"""
N07 (stage-2 verifier): exact target-mass correction for Gamma = gamma^0.

Independent method: build the symmetric traceless tensor T^{mu1..muN} = P^{mu1}..P^{muN} - traces explicitly in
components (4-D Minkowski, exact rational arithmetic with sympy), as sum_k beta_k Sym[g^{(x)k} (x) P^{(x)(N-2k)}] with
beta_k fixed by imposing the trace condition on the full tensor (no harmonic-polynomial / Gegenbauer formula used),
then contract:
   gamma^z :  T^{3 3 ... 3} z^N ...            -> K_N      = T(z,..,z)/(P.z)^N
   gamma^0 :  T^{0 3 ... 3} with z_mu's        -> Kperp_N  = T(u,z,..,z)/(P^0 (P.z)^{N-1}),  u = e_t
Compare with the claimed closed forms, check the identity Kperp = K - (2c/N) dK/dc, the x-space representation,
the O(c) expansion vs BVZ eqs. (target-parallel)/(target-perp) (as printed, read from arXiv:1810.00048),
and the pointwise equality with Chen et al. 2016's helicity x-space formula (App. B, as printed).
Also: the "commutes with matching" wording -- dilatation covariance of the momentum-space kernel.
Run: python3 -I n07_tmc_components.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy import integrate

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

g = sp.diag(1, -1, -1, -1)

def sym_tensor_from_pairs(N, k, P):
    """Sym[ g^{(x)k} (x) P^{(x)(N-2k)} ] as dict index-tuple -> value (contravariant indices, g^{mu nu} = g)."""
    T = {}
    for idx in itertools.product(range(4), repeat=N):
        T[idx] = 0
    # average over all permutations of slots
    slots = list(range(N))
    perms = list(itertools.permutations(slots))
    for idx in itertools.product(range(4), repeat=N):
        acc = 0
        for pm in perms:
            val = 1
            j = [idx[pm[s]] for s in range(N)]
            for t in range(k):
                val *= g[j[2 * t], j[2 * t + 1]]
                if val == 0:
                    break
            if val == 0:
                continue
            for t in range(2 * k, N):
                val *= P[j[t]]
            acc += val
        T[idx] = sp.Rational(1, 1) * acc / len(perms)
    return T

def traceless_tensor(N, P):
    ks = list(range(N // 2 + 1))
    beta = sp.symbols('b0:%d' % len(ks))
    parts = [sym_tensor_from_pairs(N, k, P) for k in ks]
    T = {idx: sum(beta[k] * parts[k][idx] for k in ks) for idx in parts[0]}
    eqs = [sp.Eq(beta[0], 1)]
    if N >= 2:
        # trace over first two indices with g_{mu nu} (lowered) for all remaining index values
        for rest in itertools.product(range(4), repeat=N - 2):
            tr = sum(g[m, m] * T[(m, m) + rest] for m in range(4))
            tr = sp.expand(tr)
            if tr != 0:
                eqs.append(sp.Eq(tr, 0))
    sol = sp.solve(eqs, beta, dict=True)
    assert len(sol) == 1, sol
    return {idx: sp.simplify(v.subs(sol[0])) for idx, v in T.items()}, sol[0]

def contract(T, vecs):
    """T^{mu1..muN} a_{mu1} b_{mu2} ...  with covariant vectors given as contravariant components (lowered here)."""
    low = [[g[m, m] * v[m] for m in range(4)] for v in vecs]
    s = 0
    for idx, val in T.items():
        if val == 0:
            continue
        prod = val
        for t, m in enumerate(idx):
            prod *= low[t][m]
            if prod == 0:
                break
        s += prod
    return sp.simplify(s)

M, Pz = sp.symbols('M P_z', positive=True)
c = sp.symbols('c', positive=True)
P0 = sp.sqrt(Pz**2 + M**2)
P = [P0, 0, 0, Pz]
zvec = [0, 0, 0, 1]          # z^mu (unit, z>0); P.z = -Pz
uvec = [1, 0, 0, 0]          # u^mu = e_t ; u.z = 0
def Kclaim(N):  return sum(sp.binomial(N - i, i) * c**i for i in range(N // 2 + 1))
def Kpclaim(N): return sum(sp.binomial(N - i, i) * sp.Rational(N - 2 * i, N) * c**i for i in range(N // 2 + 1))
csub = {M: 2 * Pz * sp.sqrt(c)}
for N in range(1, 7):
    T, sol = traceless_tensor(N, P)
    Pz_dot = -Pz
    KN = sp.simplify((contract(T, [zvec] * N) / Pz_dot**N).subs(csub))
    KpN = sp.simplify((contract(T, [uvec] + [zvec] * (N - 1)) / (P0 * Pz_dot**(N - 1))).subs(csub))
    okK = sp.simplify(KN - Kclaim(N)) == 0
    okKp = sp.simplify(KpN - Kpclaim(N)) == 0
    check(f"N={N}: component tensor gives K_N = {sp.expand(KN)}, Kperp_N = {sp.expand(KpN)}", okK and okKp)
    okId = sp.simplify(Kpclaim(N) - (Kclaim(N) - 2 * c / N * sp.diff(Kclaim(N), c))) == 0
    check(f"N={N}: Kperp = K - (2c/N) dK/dc", okId)
check("explicit values: Kperp_1 = Kperp_2 = 1, Kperp_3 = 1+2c/3, Kperp_4 = 1+3c/2",
      sp.simplify(Kpclaim(1) - 1) == 0 and sp.simplify(Kpclaim(2) - 1) == 0 and
      sp.simplify(Kpclaim(3) - (1 + 2 * c / 3)) == 0 and sp.simplify(Kpclaim(4) - (1 + sp.Rational(3, 2) * c)) == 0)
# identity for larger N (symbolic)
okall = all(sp.simplify(Kpclaim(N) - (Kclaim(N) - 2 * c / N * sp.diff(Kclaim(N), c))) == 0 for N in range(1, 41))
check("identity Kperp = K - (2c/N)K' for N = 1..40", okall)
# Chen et al. helicity ratio  Kbar_n = sum_i ((n-i)/n) C(n-i-1, i) c^i  (polPDFs.tex eq. Knbar, as printed)
def Kbar(n): return sum(sp.Rational(n - i, n) * sp.binomial(n - i - 1, i) * c**i for i in range(n // 2 + 1))
check("Kperp_N == Chen et al. helicity Kbar_N for N = 1..40", all(sp.simplify(Kpclaim(n) - Kbar(n)) == 0 for n in range(1, 41)))

# ---------------- x-space ----------------
cv = 0.15
fp, fm = np.sqrt(1 + 4 * cv) + 1, np.sqrt(1 + 4 * cv) - 1
def qtest(x):            # quark (x>0) and antiquark (x<0) parts, compact support [-1,1]
    if 0 < x < 1:  return 3.1 * x**0.6 * (1 - x)**3.2
    if -1 < x < 0: return -0.9 * (-x)**0.8 * (1 + x)**5.0
    return 0.0
def qz(x, cc):           # Chen et al. gamma^z: (1/sqrt(1+4c))[(f+/2) q(2x/f+) - (f-/2) q(-2x/f-)]
    a = np.sqrt(1 + 4 * cc); p, m = a + 1, a - 1
    return (p / 2 * qtest(2 * x / p) - (m / 2 * qtest(-2 * x / m) if m > 0 else 0.0)) / a
def dqz_dc(x, cc, h=1e-6):
    return (qz(x, cc + h) - qz(x, cc - h)) / (2 * h)
def A_op(fun, x):        # int_0^1 dy/y fun(x/y)  = int_x^{+-inf} dt/|t| fun(t); support of qtilde_z is [-f+/2, f+/2]
    S = fp / 2 + 1e-9
    if x > 0:
        return integrate.quad(lambda t: fun(t) / t, x, S, limit=400)[0] if x < S else 0.0
    else:
        return integrate.quad(lambda t: fun(t) / abs(t), -S, x, limit=400)[0] if x > -S else 0.0
def q0(x):               # our gamma^0 formula
    return qz(x, cv) - 2 * cv * A_op(lambda t: dqz_dc(t, cv), x)
def q0_chen(x):          # Chen et al. helicity formula with Delta q -> q (App. B, as printed)
    a = 1 + 4 * cv
    first = (fp / 2 * qtest(2 * x / fp) + fm / 2 * qtest(-2 * x / fm)) / a
    integrand = lambda y: (qtest(2 * y / fp) + qtest(-2 * y / fm)) / y
    S = fp / 2 + 1e-9
    if x > 0:
        I = -integrate.quad(integrand, x, S, limit=400)[0] if x < S else 0.0   # int_{+inf}^x
    else:
        I = integrate.quad(integrand, -S, x, limit=400)[0] if x > -S else 0.0  # int_{-inf}^x
    return first - 2 * cv / a**1.5 * I
for xv in [0.07, 0.3, 0.55, 0.9, 1.05, -0.02, -0.06]:
    a1, a2 = q0(xv), q0_chen(xv)
    check(f"x={xv}: our gamma^0 x-space formula = Chen et al. helicity formula (Dq->q): {a1:.10f} vs {a2:.10f}",
          abs(a1 - a2) < 2e-7 * max(1, abs(a1)))
# moments of q0 reproduce Kperp_n a_n
def mom(f, n, lo=-fp / 2 - 1e-9, hi=fp / 2 + 1e-9):
    pts = [p for p in [-fm / 2, 0.0, fm / 2, 1.0] if lo < p < hi]
    return integrate.quad(lambda x: x**(n - 1) * f(x), lo, hi, limit=400, points=pts)[0]
for n in range(1, 6):
    an = mom(qtest, n, -1, 1)
    r = mom(q0, n) / an
    check(f"moment n={n} of gamma^0 TMC distribution / a_n = {r:.9f} vs Kperp_n(c) = {float(Kpclaim(n).subs(c, cv)):.9f}",
          abs(r - float(Kpclaim(n).subs(c, cv))) < 5e-6)

# ---------------- O(c) vs BVZ (as printed) ----------------
# BVZ (target-parallel): Q = q + (1/4)(m^2 v^2/(pv)^2)[x q' + q];  (target-perp): Q = q + (1/4)(..)[x q' + 3q] - (1/2)(..) int_{|x|}^1 dy/y q(x/y)
# with v^2 = -1, (pv)^2 = Pz^2:  (1/4) m^2 v^2/(pv)^2 = -c.
xs, cs = sp.symbols('x c_s', positive=True)
qf = sp.Function('q')
# moments: int x^{n-1} [x q'] = -n a_n ; int x^{n-1} int_{x}^1 dy/y q(x/y) = a_n/n
nn = sp.symbols('n', positive=True, integer=True)
bvz_par = 1 - cs * (-nn + 1)
bvz_perp = 1 - cs * (-nn + 3) + 2 * cs / nn
Kz1 = sp.expand(sp.series(sum(sp.binomial(nn - i, i) * cs**i for i in range(2)), cs, 0, 2).removeO())
check("O(c) gamma^z: 1 + c(n-1) from K_n  == BVZ (target-parallel) moments", sp.simplify(bvz_par - (1 + cs * (nn - 1))) == 0)
check("O(c) gamma^0: 1 + c(n-1)(n-2)/n from Kperp_n == BVZ (target-perp) moments",
      sp.simplify(bvz_perp - (1 + cs * (nn - 1) * (nn - 2) / nn)) == 0)
check("Kperp_n at O(c) for n=3..8 equals 1 + c(n-1)(n-2)/n",
      all(sp.simplify(sp.series(Kpclaim(n), c, 0, 2).removeO() - (1 + c * sp.Rational((n - 1) * (n - 2), n))) == 0 for n in range(3, 9)))

# ---------------- "commutes with matching": dilatation covariance ----------------
# For D_s q(x) = (1/s) q(x/s) and (C (x)_{P} q)(x) = int dy/|y| C(x/y, mu/(|y|P)) q(y):
#   C (x)_P D_s q = D_s (C (x)_{sP} q)   (exact).  The MS-bar kernel depends on ln(mu^2/(4 y^2 P^2)), so
#   C (x)_P TMC[q] != TMC[C (x)_P q] at O(alpha_s c): check numerically with the P-dependent part of the one-loop kernel.
def conv_logpart(f, x, P, mu=1.0, ysup=1.0):
    # P-dependent one-loop piece (units a), 0<xi<1:  [(1+xi^2)/(1-xi)]_+ (-l(y)) + (3/2) l(y) delta(1-xi),  l(y) = ln(mu^2/(4 y^2 P^2)),
    # (C (x) f)(x) = int_0^1 dxi/xi C(xi, y=x/xi) f(x/xi); plus prescription acts on h(xi) = (-l(x/xi)) f(x/xi)/xi (f=0 off support)
    lx = np.log(mu**2 / (4 * x**2 * P**2))
    def h(xi):
        y = x / xi
        if not (0 < y < ysup):
            return 0.0
        return (-np.log(mu**2 / (4 * y**2 * P**2))) * f(y) / xi
    xib = x / ysup
    g_xi = lambda xi: (1 + xi**2) / (1 - xi) * (h(xi) - (-lx) * f(x))
    I = integrate.quad(g_xi, 0, xib, limit=400)[0] + integrate.quad(g_xi, xib, 1, limit=400)[0]
    I += 1.5 * lx * f(x)
    return I
f_s = lambda y: 30 * y**2 * (1 - y)**2 if 0 < y < 1 else 0.0
s_ = 1.08; P_ = 2.0; xv = 0.4
Ds = lambda f: (lambda x: f(x / s_) / s_)
lhs = conv_logpart(Ds(f_s), xv, P_, ysup=s_)
rhs_cov = conv_logpart(f_s, xv / s_, s_ * P_) / s_          # D_s (C (x)_{sP} q)(x)
rhs_naive = conv_logpart(f_s, xv / s_, P_) / s_             # D_s (C (x)_{P} q)(x)
check(f"dilatation covariance C(x)_P D_s q = D_s(C(x)_(sP) q): {lhs:.10f} vs {rhs_cov:.10f}", abs(lhs - rhs_cov) < 1e-7)
check(f"literal commutation fails: C(x)_P D_s q - D_s(C(x)_P q) = {lhs - rhs_naive:.6f} (nonzero, O(a ln s))", abs(lhs - rhs_naive) > 1e-3)

print(f"\nSUMMARY n07: {PASS} PASS, {FAIL} FAIL")
