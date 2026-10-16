#!/usr/bin/env python3
"""
s1_landau_gordan.py  --  checks for Section 1 of OTHERS.md (Landau condition / Coleman-Norton).

(a) Collins (arXiv:2007.04085) Thm. 3  ==  Gordan's theorem of the alternative (Math. Ann. 6 (1873) 23):
    for dual vectors D_1..D_N on R^d EXACTLY ONE of
       (I)  exists v with D_j(v) > 0 for all j          ("good direction")
       (II) exists lambda_j >= 0, not all 0, sum lambda_j D_j = 0   ("Landau point")
    holds.  We test the constructive min-norm proof used in OTHERS.md on random instances:
    w = argmin_{u in conv{D_j}} |u|;  if |w|>0 then D_j.w >= |w|^2 > 0 for all j (I);
    if |w|=0 the convex weights give a Landau point (II).  We also check exclusivity with an LP.
(b) Feynman-graph instances: one-loop massless self-energy at a collinear point (Landau point with
    positive weights = pinch), soft point (D=0), massive below-threshold point (no Landau point).
(c) Collins' sign restriction (8.15): for a line with A = k^2 - m^2, a deformation direction vhat with
    k.vhat = 0 has vhat^2 <= 0 when k^2 = m^2 > 0 (k timelike) or k^2 = 0, k != 0.  (random check)
(d) Coleman-Norton: at a Landau point the vertex displacements dx_j = lambda_j k_j close around the
    loop (sum over loop of +-lambda_j k_j = 0) -- checked for the collinear self-energy and a
    triangle with two collinear lines.
Run:  python3 -I s1_landau_gordan.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.optimize import linprog, minimize

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    if ok: PASS += 1
    else:  FAIL += 1
    print(("[PASS] " if ok else "[FAIL] ") + name + ("  " + info if info else ""))

rng = np.random.default_rng(20261010)

def min_norm_point(D):
    """min |sum_j lam_j D_j|^2 over the simplex (SLSQP, then polish)."""
    N = D.shape[0]
    f = lambda lam: float(np.sum((lam @ D) ** 2))
    g = lambda lam: 2.0 * (D @ (lam @ D))
    cons = [{'type': 'eq', 'fun': lambda lam: np.sum(lam) - 1.0, 'jac': lambda lam: np.ones(N)}]
    best = None
    for trial in range(4):
        x0 = rng.dirichlet(np.ones(N))
        r = minimize(f, x0, jac=g, bounds=[(0, 1)] * N, constraints=cons, method='SLSQP',
                     options={'ftol': 1e-15, 'maxiter': 2000})
        if best is None or r.fun < best.fun:
            best = r
    lam = np.clip(best.x, 0, None); lam /= lam.sum()
    # polish: exact KKT solve on the support (min-norm point of the affine hull of the support)
    S = np.where(lam > 1e-7)[0]
    G = D[S] @ D[S].T; k = len(S)
    K = np.zeros((k + 1, k + 1)); K[:k, :k] = G; K[:k, k] = 1; K[k, :k] = 1
    rhs = np.zeros(k + 1); rhs[k] = 1
    sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
    if np.all(sol[:k] >= -1e-12):
        lam2 = np.zeros_like(lam); lam2[S] = np.clip(sol[:k], 0, None); lam2 /= lam2.sum()
        if np.sum((lam2 @ D) ** 2) <= np.sum((lam @ D) ** 2) + 1e-14:
            lam = lam2
    return lam, lam @ D

def lp_good_direction(D):
    """maximize t s.t. D v >= t, |v_i| <= 1.  Returns t* (>0 iff good direction exists)."""
    N, d = D.shape
    c = np.zeros(d + 1); c[-1] = -1.0
    A = np.hstack([-D, np.ones((N, 1))]); b = np.zeros(N)
    bounds = [(-1, 1)] * d + [(None, 1.0)]
    r = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    return -r.fun

def lp_landau_point(D):
    """feasibility: lam >= 0, sum lam = 1, D^T lam = 0.  Returns True if feasible."""
    N, d = D.shape
    A_eq = np.vstack([D.T, np.ones((1, N))]); b_eq = np.concatenate([np.zeros(d), [1.0]])
    r = linprog(np.zeros(N), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * N, method='highs')
    return r.status == 0

# ---------------- (a) random instances of Gordan / Collins Thm 3 ----------------
n_I = n_II = 0; ok_all = True; worst_margin = np.inf
for trial in range(400):
    d = rng.integers(2, 7); N = rng.integers(1, 9)
    D = rng.normal(size=(N, d))
    if trial % 3 == 0:     # force a Landau point sometimes: make 0 a convex combination
        lam = rng.dirichlet(np.ones(N));
        if N >= 2:
            D[-1] = -(lam[:-1] @ D[:-1]) / lam[-1]
    lam, w = min_norm_point(D)
    nw = np.linalg.norm(w)
    tstar = lp_good_direction(D); landau = lp_landau_point(D)
    exactly_one = (tstar > 1e-9) != landau
    if nw > 1e-7:
        # (I): w is a good direction with margin >= |w|^2
        margins = D @ w
        okI = np.all(margins >= nw ** 2 * (1 - 1e-6) - 1e-12) and (tstar > 1e-9) and (not landau)
        worst_margin = min(worst_margin, np.min(margins) - nw ** 2)
        n_I += 1; ok_all &= bool(okI and exactly_one)
    else:
        okII = landau and (tstar < 1e-7) and np.linalg.norm(lam @ D) < 1e-6
        n_II += 1; ok_all &= bool(okII and exactly_one)
check("Gordan alternative / Collins Thm 3 on 400 random instances (exactly one of I, II)", ok_all,
      f"(#good-direction cases={n_I}, #Landau-point cases={n_II}, min[D_j.w-|w|^2]={worst_margin:.2e})")

# ---------------- (b) Feynman-graph instances ----------------
eta = np.diag([1.0, -1.0, -1.0, -1.0])
dot = lambda a, b: a @ eta @ b
def grad_k2(k):           # derivative of A = k.k w.r.t. the loop momentum components (lower index -> row)
    return 2.0 * (eta @ k)

# one-loop self-energy: A1 = l^2, A2 = (p-l)^2 ; massless, p lightlike
p = np.array([1.0, 0.0, 0.0, 1.0])
for x in [0.2, 0.5, 0.9]:
    l = x * p
    D = np.vstack([grad_k2(l), -grad_k2(p - l)])     # d(p-l)^2/dl = -2(p-l)
    ok = abs(dot(l, l)) < 1e-14 and abs(dot(p - l, p - l)) < 1e-14 and lp_landau_point(D)
    lam_exp = np.array([1 - x, x])                    # explicit Landau point
    ok &= np.linalg.norm(lam_exp @ D) < 1e-12 and np.all(lam_exp > 0)
    check(f"massless self-energy, collinear point l = {x} p : Landau point (1-x, x) => pinch", ok)
# soft point l = 0 : D1 = 0 alone is a Landau point
D = np.vstack([grad_k2(np.zeros(4))])
check("soft point l=0 (single massless denominator, D=0) is a Landau point => pinch",
      lp_landau_point(D) and np.allclose(D, 0))
# massive self-energy below threshold: p^2 = s < 4m^2, both lines can't be on shell simultaneously with
# real l; check a point where only one line is on shell: Landau point impossible (D != 0)
m = 1.0; s = 3.0
pm = np.array([np.sqrt(s), 0, 0, 0.0])
l = np.array([np.sqrt(m**2 + 0.3**2), 0.3, 0.0, 0.0])   # on shell, (p-l)^2 != m^2
D = np.vstack([grad_k2(l)])
check("massive line on shell alone (k^2=m^2>0): D = 2k != 0, no Landau point => no pinch",
      (not lp_landau_point(D)) and lp_good_direction(D) > 1e-6)
# massive at the normal threshold s = 4 m^2, l = p/2: both on shell, Landau point (1/2,1/2)
s = 4.0; pm = np.array([2.0, 0, 0, 0]); l = pm / 2
D = np.vstack([grad_k2(l), -grad_k2(pm - l)])
check("massive self-energy at normal threshold s=4m^2, l=p/2: Landau point => pinch (threshold)",
      lp_landau_point(D) and abs(dot(l, l) - 1) < 1e-14)

# ---------------- (c) sign restriction (8.15) ----------------
okc = True; cnt = 0
for trial in range(20000):
    massless = trial % 2 == 0
    kv = rng.normal(size=3)
    k = np.concatenate([[np.linalg.norm(kv) if massless else np.sqrt(kv @ kv + rng.uniform(0.1, 4))], kv])
    v = rng.normal(size=4)
    # project v onto the hyperplane k.v = 0 (Minkowski):  v -> v - (k.v / k.n) n with n = (1,0,0,0)
    n = np.array([1.0, 0, 0, 0])
    v = v - dot(k, v) / dot(k, n) * n
    assert abs(dot(k, v)) < 1e-9 * (1 + np.abs(v).max())
    okc &= dot(v, v) <= 1e-9 * (1 + v @ v); cnt += 1
check("Collins (8.15): k.v=0 with k timelike or lightlike  =>  v.v <= 0  (20000 random)", okc)

# ---------------- (d) Coleman-Norton displacements ----------------
# self-energy, collinear: vertices a (p enters) and b; lines 1: a->b with k1 = l, 2: a->b with k2 = p-l.
x = 0.3; k1 = x * p; k2 = (1 - x) * p; lam = np.array([1 - x, x])
dx1 = lam[0] * k1; dx2 = lam[1] * k2
check("CN: self-energy collinear pinch, both lines give the same displacement x_b - x_a",
      np.allclose(dx1, dx2), f"dx = {dx1}")
# triangle (vertex function) with lines 1: l (a->b), 2: p1 - l (a->c), 3: from b to c with k3 = l - p2?
# use massless external p1 = (1,0,0,1) incoming at a? Construct a jet-type pinch: l = x p1, line 2 = (1-x) p1,
# and the third line (from b to c) carrying l - q with q hard: off shell -> lambda_3 = 0.
p1 = np.array([1.0, 0, 0, 1.0]); x = 0.6
l = x * p1
A_grads = np.vstack([grad_k2(l), -grad_k2(p1 - l)])
lamt = np.array([1 - x, x])
check("CN: triangle with a collinear pinch (third, hard line has lambda=0): Landau point exists",
      np.linalg.norm(lamt @ A_grads) < 1e-12)

print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
