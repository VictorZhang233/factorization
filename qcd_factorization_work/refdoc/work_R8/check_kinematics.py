"""R8 checks: analytic statements of refdoc App. E.4.5-E.5 (pp. 199-216).

 K1  (E.19)/(E.37) sign: (i/D1)[i/(k-a+i0) + i/(b-k+i0)] = +1/((k-a+i0)(k-b-i0))  (the printed (E.19) has a minus sign)
 K2  (E.20)/Ex. E.37: int dk/2pi J_A = i/D1 ; J_- = J_+ = i/D1
 K3  Ex. E.37 with the exact connecting propagator R(k) = 1/(2k^+ k - kT^2 + i0):
       int dk/2pi J_A R = R(0) i/D1 (1 + O(lambda_J/Lambda)); ordering weights c = theta(k^+)
 K4  AS-type: J_A = J^in only, int J^in R = theta(-k^+) R(0) J_-  (+ small);  symmetric window -> 1/2
 K5  Lemma E.48(d): int_{-K}^{K} dk/2pi i/(+-2pk + i eta) -> 1/(4p) each (equal weights 1/2)
 K6  Prop. E.46 step 2: iQa/(k+i0) + iQs[1/(k+i0) - 1/(k-i0)] = iQa/(k-i0) for Qs = -Qa  (test function)
 K7  carrier phi(x) = 2 sqrt(pi) exp(-x^2): int dx/2pi phi = 1; max_{|y|<=1/2}|phi(x+iy)| = 2 sqrt(pi) e^{1/4}
 K8  (E.39)/(E.42): e_G = nbar - n, e_G^2=-2, n.e_G=1, nbar.e_G=-1, (l+i t s f e_G)^2 - m^2 formula;
     n_A(y).e_G = 1+e^{-2y}, n_B(y).e_G = -(1+e^{2y})
 K9  Lemma E.41(b): Re k_t^2 <= -kT^2/4 for kappa<=1/2, delta<=1/8, AA and SA lines (random scan)
 K10 Prop. E.43(i): |k^+||k^-| >= min(kappa^2, delta/2) kT^2 on the deformed contour (random scan)
 K11 Prop. E.45(b),(c): |D - Dt| <= (f/kappa)(4|p^-|+2|pT|) + 9 f^2/kappa^2 ; (E.46); eps3 bound (random scan)
"""
import sys, os, math, cmath
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp

ok_all = True
def report(name, ok, extra=''):
    global ok_all
    ok_all &= bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'} {extra}")

# ---------- K1 ----------
k, a, b, eta = sp.symbols('k a b eta', real=True)
D1 = b - a
lhs = (sp.I / D1) * (sp.I / (k - a + sp.I * eta) + sp.I / (b - k + sp.I * eta))
rhs_plus = 1 / ((k - a + sp.I * eta) * (k - b - sp.I * eta))
diff = sp.simplify(sp.together(lhs - rhs_plus))
# lhs - rhs vanishes only up to O(eta) (the sum identity uses beta-alpha = D1 exactly when eta->0)
num = sp.lambdify((k, a, b, eta), lhs - rhs_plus, 'numpy')
num2 = sp.lambdify((k, a, b, eta), lhs + rhs_plus, 'numpy')
kk = np.linspace(-3, 3, 7) + 0.123
v1 = np.max(np.abs(num(kk, 0.3, 1.1, 1e-9)))
v2 = np.max(np.abs(num2(kk, 0.3, 1.1, 1e-9)))
report('K1 (E.19) sign: lhs = +1/((k-a)(k-b))', v1 < 1e-6 and v2 > 1e-2, f'|lhs-(+)|={v1:.1e}, |lhs+(+)|={v2:.2e}')

# ---------- K2 ----------
al, be = 0.3, 1.1
D1n = be - al
etan = 1e-3
def JA(kv, e=etan):
    return (1j / D1n) * (1j / (kv - al + 1j * e) + 1j / (be - kv + 1j * e))
# integrate on a large symmetric interval with fine grid (integrand ~ 1/k^2 at large k)
L = 4000.0
xs = np.concatenate([np.linspace(-L, -5, 400001), np.linspace(-5, 5, 2000001), np.linspace(5, L, 400001)])
val = np.trapz(JA(xs), xs) / (2 * np.pi)
report('K2 int dk/2pi J_A = i/D1', abs(val - 1j / D1n) < 2e-3 * abs(1j / D1n), f'val={val:.5f}, i/D1={1j/D1n:.5f}')

# ---------- K3, K4 ----------
def integrate(f, L=60.0, n=3_000_001):
    x = np.linspace(-L, L, n)
    return np.trapz(f(x), x) / (2 * np.pi)
kT = 1.0
for kp in (+0.02, -0.02):
    Lam = kT ** 2 / (4 * abs(kp))
    R = lambda kv, kp=kp: 1.0 / (2 * kp * kv - kT ** 2 + 1j * 1e-3 * np.sign(1))
    R0 = -1 / kT ** 2
    full = integrate(lambda x: JA(x, 1e-3) * R(x), L=200.0, n=8_000_001)
    target = R0 * 1j / D1n
    rel = abs(full / target - 1)
    Jin = lambda x: (1j / D1n) * (1j / (x - al + 1j * 1e-3))
    Jfi = lambda x: (1j / D1n) * (1j / (be - x + 1j * 1e-3))
    win = integrate(lambda x: Jin(x) * R(x), L=200.0, n=8_000_001)
    wfi = integrate(lambda x: Jfi(x) * R(x), L=200.0, n=8_000_001)
    lamJ = max(al, be)
    report(f'K3 k^+={kp:+.2f}: int J_A R = R(0) i/D1 (1+O(lamJ/Lam))', rel < 5 * lamJ / Lam,
           f'rel.err={rel:.3e}, lamJ/Lam={lamJ/Lam:.3e}; weights in={abs(win/target):.3f}, fi={abs(wfi/target):.3f}')
    # AS-type: J^in only, J_+ = 0, J_- = i/D1 ... expect theta(-k^+) R(0) J_-
    expect = (1.0 if kp < 0 else 0.0)
    report(f'K4 k^+={kp:+.2f}: AS-type int J^in R = theta(-k^+) R(0) J_-', abs(win / target - expect) < 0.1,
           f'ratio={win/target:.3f}, expected {expect}')
# symmetric window for the AS-type: weight 1/2
Kw = 0.5  # window |k| <= K with lamJ << K << Lambda
x = np.linspace(-Kw, Kw, 2_000_001)
eps_ = 1e-5
Jin_t = lambda x: (1j / D1n) * (1j / (x - 0.002 + 1j * eps_))
sym = np.trapz(Jin_t(x), x) / (2 * np.pi)
report('K4b AS-type, symmetric window (R=const): weight 1/2 (+O(lamJ/K))', abs(sym / (1j / D1n) - 0.5) < 0.02, f'ratio={sym/(1j/D1n):.4f}')

# ---------- K5 ----------
p = 0.7
x = np.linspace(-1.0, 1.0, 4_000_001)
for sgn in (+1, -1):
    e = 1e-5
    w = np.trapz(1j / (sgn * 2 * p * x + 1j * e), x) / (2 * np.pi)
    report(f'K5 ordering sign {sgn:+d}: int dk/2pi i/(+-2pk+i0) = 1/(4p)', abs(w - 1 / (4 * p)) < 1e-3, f'w={w:.5f}, 1/(4p)={1/(4*p):.5f}')

# ---------- K6 ----------
g = lambda x: np.exp(-(x - 0.3) ** 2) * (1 + 0.5 * x)
Qa = 0.8; Qs = -Qa
x = np.linspace(-30, 30, 6_000_001)
e = 1e-4
lhs = np.trapz(g(x) * (1j * Qa / (x + 1j * e) + 1j * Qs * (1 / (x + 1j * e) - 1 / (x - 1j * e))), x)
rhs = np.trapz(g(x) * (1j * Qa / (x - 1j * e)), x)
past = np.trapz(g(x) * (1j * Qa / (x + 1j * e)), x)
report('K6 sum of attachments in a single cut graph = future-pointing term', abs(lhs - rhs) < 1e-3,
       f'lhs={lhs:.5f}, iQa/(k-i0)={rhs:.5f}, past iQa/(k+i0)={past:.5f}, diff to past = 2 pi Qs g(0) = {2*np.pi*Qs*g(0):.5f} vs {lhs-past:.5f}')

# ---------- K7 ----------
phi = lambda z: 2 * np.sqrt(np.pi) * np.exp(-z ** 2)
x = np.linspace(-12, 12, 2_000_001)
norm = np.trapz(phi(x), x) / (2 * np.pi)
X, Y = np.meshgrid(np.linspace(-3, 3, 1201), np.linspace(-0.5, 0.5, 201))
mx = np.max(np.abs(phi(X + 1j * Y)))
report('K7 phi normalisation and bound', abs(norm - 1) < 1e-9 and abs(mx - 2 * np.sqrt(np.pi) * np.exp(0.25)) < 1e-6,
       f'norm={norm:.12f}, max={mx:.6f}, 2 sqrt(pi) e^(1/4)={2*np.sqrt(np.pi)*np.exp(0.25):.6f}')

# ---------- K8 ----------
lp, lm, l1, l2, m, t, s, f, y = sp.symbols('lp lm l1 l2 m t s f y', real=True)
def dot(u, v):  # (+,-,T1,T2)
    return u[0] * v[1] + u[1] * v[0] - u[2] * v[2] - u[3] * v[3]
n_ = (1, 0, 0, 0); nb = (0, 1, 0, 0)
eG = tuple(nb[i] - n_[i] for i in range(4))
l = (lp, lm, l1, l2)
c8 = [sp.simplify(dot(eG, eG) + 2) == 0, sp.simplify(dot(n_, eG) - 1) == 0, sp.simplify(dot(nb, eG) + 1) == 0]
lt = tuple(l[i] + sp.I * t * s * f * eG[i] for i in range(4))
expr = sp.expand(dot(lt, lt) - m ** 2 - (dot(l, l) - m ** 2 + 2 * t ** 2 * s ** 2 * f ** 2 + 2 * sp.I * t * s * f * (lp - lm)))
# s = sigma = +-1 so s^2 = 1 in (E.42)
c8.append(sp.simplify(expr.subs(s, 1)) == 0 and sp.simplify(expr.subs(s, -1)) == 0)
nA = (1, -sp.exp(-2 * y), 0, 0); nB = (-sp.exp(2 * y), 1, 0, 0)
c8.append(sp.simplify(dot(nA, eG) - (1 + sp.exp(-2 * y))) == 0)
c8.append(sp.simplify(dot(nB, eG) + (1 + sp.exp(2 * y))) == 0)
c8.append(sp.simplify(dot(nA, nA) + 2 * sp.exp(-2 * y)) == 0)
report('K8 Glauber direction algebra, (E.42), n_A(y), n_B(y)', all(c8), str(c8))

# ---------- K9 ----------
rng = np.random.default_rng(3)
worst = -1e9
for _ in range(200000):
    delta = rng.uniform(1e-3, 1 / 8); kappa = rng.uniform(1e-3, 0.5)
    kT2 = rng.uniform(0.1, 2.0)
    prod = rng.uniform(-delta, delta) * kT2  # k^+ k^- in the window W_delta
    k2 = 2 * prod - kT2
    lamaG = rng.uniform(1e-4, 1.0)
    Th = rng.uniform(0, 1); psi = rng.uniform(0, 1); tt = rng.uniform(0, 1)
    typ = rng.integers(0, 2)
    if typ == 0:   # AA
        psiA = psiB = psi; sA = sB = 1.0
    else:          # SA
        psiA = psi * Th; sA = lamaG; psiB = psi; sB = 1 + (1 / lamaG - 1) * Th
    re = k2 + 2 * tt ** 2 * kappa ** 2 * psiA * psiB * sA * sB * kT2
    worst = max(worst, re / kT2)
report('K9 Lemma E.41(b): max Re(k_t^2)/kT^2 <= -1/4', worst <= -0.25 + 1e-12, f'max = {worst:.4f}')

# ---------- K10 ----------
worst = 1e9
for _ in range(200000):
    delta = rng.uniform(1e-3, 1 / 8); kappa = rng.uniform(1e-3, 0.5)
    kT = rng.uniform(0.1, 2.0); lamaG = rng.uniform(1e-4, 1.0)
    # choose real k^+, k^- anywhere with |k^+ k^-| up to 3 delta kT^2
    kpm = rng.uniform(-3 * delta, 3 * delta) * kT ** 2
    kp = rng.choice([-1, 1]) * 10 ** rng.uniform(-3, 1)
    km = kpm / kp
    x = abs(kpm) / (delta * kT ** 2)
    # smooth theta: 1 on (-inf,1/2], 0 on [1,inf); use linear interpolation as a stand-in (only psi=1 on core matters)
    psi = 1.0 if x <= 0.5 else (0.0 if x >= 1 else 2 * (1 - x))
    typ = rng.integers(0, 2)
    if typ == 0:
        dm = kappa * psi * kT; dp = kappa * psi * kT
    else:
        dm = kappa * psi * lamaG * kT; dp = kappa * psi * kT / lamaG
    val = abs(complex(kp, -dp)) * abs(complex(km, dm)) / kT ** 2
    worst = min(worst, val / min(kappa ** 2, delta / 2))
report('K10 Prop. E.43(i): |k^+||k^-| >= min(kappa^2, delta/2) kT^2', worst >= 1 - 1e-12, f'min ratio = {worst:.4f}')

# ---------- K11 ----------
worst46 = 0.0; worst_raw = 0.0; worst_eps = 0.0; okDt = True
for _ in range(100000):
    kappa = rng.uniform(0.01, 0.5)
    nleg = rng.integers(1, 5)
    qT = rng.normal(size=(nleg, 2)) * rng.uniform(0.01, 1.0)
    qTn = np.linalg.norm(qT, axis=1)
    fa = qTn * kappa * (1 + rng.uniform(0, 3, size=nleg))   # f_a >= kappa |q_Ta|
    rep = rng.uniform(-1, 1, size=nleg) * qTn                # |Re q^+| <= |q_T|
    rem = rng.uniform(-1, 1, size=nleg) * qTn
    kp = np.sum(rep) - 1j * np.sum(fa)    # Im q^+ = -f_a (sigma=+1)
    km = np.sum(rem) + 1j * np.sum(fa)    # Im q^- = +f_a
    kTv = np.sum(qT, axis=0)
    fI = np.sum(fa)
    pplus = rng.uniform(0.5, 2.0); pminus = rng.uniform(-0.5, 0.5); pT = rng.normal(size=2) * rng.uniform(0, 0.5)
    m2 = rng.uniform(0, 0.3)
    p2 = 2 * pplus * pminus - pT @ pT
    Dt = p2 - m2 + 2 * pplus * km
    D = p2 - m2 + 2 * pplus * km + 2 * pminus * kp - 2 * (pT @ kTv) + 2 * kp * km - kTv @ kTv
    okDt &= abs(Dt) >= 2 * pplus * fI * (1 - 1e-12)
    bound_raw = (fI / kappa) * (4 * abs(pminus) + 2 * np.linalg.norm(pT)) + 9 * fI ** 2 / kappa ** 2
    worst_raw = max(worst_raw, abs(D - Dt) / bound_raw)
    NCs = fI / kappa  # the bound uses f_I <= kappa N_C s, i.e. N_C s >= f_I/kappa; take equality
    b46 = (1 / (kappa * pplus)) * (2 * abs(pminus) + np.linalg.norm(pT) + 4.5 * NCs)
    worst46 = max(worst46, (abs(D - Dt) / abs(Dt)) / b46)
    eps3 = (abs(kp) * abs(pminus) + np.linalg.norm(kTv) * np.linalg.norm(pT)) / (abs(km) * pplus)
    eps3b = (2 * abs(pminus) + np.linalg.norm(pT)) / (kappa * pplus)
    worst_eps = max(worst_eps, eps3 / eps3b)
report('K11 Prop. E.45: |Dt| >= 2p^+ f_I', okDt)
report('K11 Prop. E.45: |D-Dt| <= (f/k)(4|p^-|+2|pT|)+9f^2/k^2', worst_raw <= 1 + 1e-12, f'max ratio={worst_raw:.4f}')
report('K11 (E.46)', worst46 <= 1 + 1e-12, f'max ratio={worst46:.4f}')
report('K11 eps3 <= (2|p^-|+|pT|)/(kappa p^+)', worst_eps <= 1 + 1e-12, f'max ratio={worst_eps:.4f}')

print('ALL PASS' if ok_all else 'SOME FAIL')
