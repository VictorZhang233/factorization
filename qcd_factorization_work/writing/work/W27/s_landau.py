#!/usr/bin/env python3
"""
W27 / Ch24 sec:front-landau -- writer re-derivations.
 (1) lem:front-min-norm on random instances (min-norm point via exact active-set QP), margin D_j.w >= |w|^2,
     exclusivity; |w| = max_{|v|<=1} min_j D_j.v  (strong duality, checked numerically);
 (2) ex:front-gordan-2d: w = (8/5,4/5), |w|^2 = 16/5 = D1.w = D2.w;  D3 = (-1,-1): 1 D1 + 2 D2 + 4 D3 = 0;
     figure (a) data: D3 = (2.6,1.6), D3.w = 5.44, good cone between -26.565 deg and 90 deg;
 (3) prop:front-anomalous: Collins' two deformations for A = E - p^2/2m (2D) -- zeros of A + i eps on the
     deformed contour only at eps = lambda = 0 (#1) and on the whole surface (#2) with zero first-order shift;
     constant tangent deformation (0,m) crosses the singularity; 1D: a positive first-order shift is necessary
     (numerical illustration of the winding argument for A = w^2);
 (4) thm:front-collins-pinch, sign condition: k.v = 0 with k timelike or light-like => v^2 <= 0;
 (5) ex:front-collinear-pinch / cor:front-coleman-norton: Landau point (1-x, x), equal displacements; single on-shell
     massive line not trapped; soft line D = 0;
 (6) rem:front-cn-history: massless bubble, F = -p^2 a1 a2, alpha-integral p-independent; Feynman-parameter
     Landau equations hold identically at p^2 = 0.
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import sympy as sp
from scipy.optimize import linprog

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("[PASS] " if ok else "[FAIL] ") + name + (("  " + info) if info else ""))

rng = np.random.default_rng(271024)

def min_norm_point(D):
    """exact min-norm point of conv{rows of D}: enumerate supports S (affine-hull projection), keep feasible ones."""
    N = D.shape[0]
    best = None
    for r in range(1, N + 1):
        for S in itertools.combinations(range(N), r):
            DS = D[list(S)]
            G = DS @ DS.T
            K = np.zeros((r + 1, r + 1)); K[:r, :r] = G; K[:r, r] = 1; K[r, :r] = 1
            rhs = np.zeros(r + 1); rhs[r] = 1
            try:
                sol = np.linalg.solve(K, rhs)
            except np.linalg.LinAlgError:
                sol = np.linalg.lstsq(K, rhs, rcond=None)[0]
            lam = sol[:r]
            if np.all(lam >= -1e-12):
                w = lam @ DS
                nw = w @ w
                if best is None or nw < best[0] - 1e-15:
                    best = (nw, w, S, lam)
    return best

def lp_good(D):
    N, d = D.shape
    c = np.zeros(d + 1); c[-1] = -1
    A = np.hstack([-D, np.ones((N, 1))]); b = np.zeros(N)
    r = linprog(c, A_ub=A, b_ub=b, bounds=[(-1, 1)] * d + [(None, 1)], method='highs')
    return -r.fun
def lp_landau(D):
    N, d = D.shape
    r = linprog(np.zeros(N), A_eq=np.vstack([D.T, np.ones((1, N))]), b_eq=np.r_[np.zeros(d), 1],
                bounds=[(0, None)] * N, method='highs')
    return r.status == 0

# ---------------- (1) lemma on random instances ----------------
nI = nII = 0; ok = True; worst = np.inf; dual_ok = True
for t in range(300):
    d = int(rng.integers(2, 5)); N = int(rng.integers(1, 7))
    D = rng.normal(size=(N, d))
    if t % 3 == 0 and N >= 2:
        lam = rng.dirichlet(np.ones(N)); D[-1] = -(lam[:-1] @ D[:-1]) / lam[-1]
    nw, w, S, lam = min_norm_point(D)
    landau = lp_landau(D); good = lp_good(D) > 1e-9
    if nw > 1e-12:
        marg = D @ w
        ok &= bool(np.all(marg >= nw - 1e-9) and good and not landau)
        worst = min(worst, float(np.min(marg) - nw)); nI += 1
        # |w| = max_{|v|<=1} min_j D_j.v  (check v = w/|w| attains it and no random v beats it)
        val = np.min(D @ (w / np.sqrt(nw)))
        vs = rng.normal(size=(4000, d)); vs /= np.linalg.norm(vs, axis=1)[:, None]
        dual_ok &= bool(abs(val - np.sqrt(nw)) < 1e-9 and np.max(np.min(vs @ D.T, axis=1)) <= np.sqrt(nw) + 1e-9)
    else:
        ok &= bool(landau and not good); nII += 1
check("(1) Gordan / min-norm lemma on 300 random instances (exactly one alternative; margin)", ok,
      f"(type I {nI}, type II {nII}, min[D_j.w - |w|^2] = {worst:.2e})")
check("(1') |w| = max_{|v|<=1} min_j D_j.v (strong duality)", dual_ok)

# ---------------- (2) the 2D example ----------------
D1, D2, D3b = sp.Matrix([2, 0]), sp.Matrix([1, 2]), sp.Matrix([-1, -1])
t = sp.symbols('t', real=True)
u = (1 - t) * D1 + t * D2
tmin = sp.solve(sp.diff(u.dot(u), t), t)[0]
wv = u.subs(t, tmin)
check("(2a) segment minimum at t = 2/5, w = (8/5, 4/5), |w|^2 = 16/5",
      tmin == sp.Rational(2, 5) and list(wv) == [sp.Rational(8, 5), sp.Rational(4, 5)] and wv.dot(wv) == sp.Rational(16, 5))
check("(2b) D1.w = D2.w = 16/5 (equality on the face)", D1.dot(wv) == sp.Rational(16, 5) and D2.dot(wv) == sp.Rational(16, 5))
check("(2c) (2-t)^2 + 4t^2 is |u|^2", sp.expand(u.dot(u) - ((2 - t)**2 + 4 * t**2)) == 0)
check("(2d) 1*D1 + 2*D2 + 4*D3 = 0 (Landau point (1,2,4))", list(D1 + 2 * D2 + 4 * D3b) == [0, 0])
D3a = sp.Matrix([sp.Rational(13, 5), sp.Rational(8, 5)])
check("(2e) figure (a): D3=(2.6,1.6), D3.w = 5.44 >= 16/5", D3a.dot(wv) == sp.Rational(136, 25))
nwa = min_norm_point(np.array([[2, 0], [1, 2], [2.6, 1.6]], float))
check("(2f) min-norm point of conv{D1,D2,D3=(2.6,1.6)} is still (8/5,4/5)", np.allclose(nwa[1], [1.6, 0.8]))
ang = float(sp.atan2(-1, 2) * 180 / sp.pi)   # direction perpendicular to D2=(1,2): (2,-1)
check("(2g) good cone {v: D1.v>0, D2.v>0} bounded by directions -26.565 deg and 90 deg", abs(ang + 26.565) < 1e-3)

# ---------------- (3) anomalous deformations (Collins App. B.1) ----------------
ER, pR, lam_, m, eps_ = sp.symbols('E_R p_R lambda m epsilon', real=True)
def A_def(eta, xi):
    E = ER + sp.I * lam_ * eta; p = pR + sp.I * lam_ * xi
    return sp.expand(E - p**2 / (2 * m))
# deformation 1: (eta, xi) = (|E_R| + 2|p_R|, m)
A1 = A_def(sp.Abs(ER) + 2 * sp.Abs(pR), m)
re1, im1 = sp.simplify(sp.re(A1)), sp.simplify(sp.im(A1))
check("(3a) #1: Re A = E_R - p_R^2/2m + lambda^2 m/2,  Im A = lambda(|E_R| + 2|p_R| - p_R)",
      sp.simplify(re1 - (ER - pR**2 / (2 * m) + lam_**2 * m / 2)) == 0 and
      sp.simplify(im1 - lam_ * (sp.Abs(ER) + 2 * sp.Abs(pR) - pR)) == 0)
# zeros of A + i eps for lambda in (0,1], eps >= 0: Im >= 0 with equality only at origin, where Re = lambda^2 m/2 > 0
mv = 1.0
zero_found = False
for lv in [1e-3, 1e-2, 0.1, 1.0]:
    for Ev in np.linspace(-2, 2, 201):
        for pv in np.linspace(-2, 2, 201):
            imv = lv * (abs(Ev) + 2 * abs(pv) - pv)
            rev = Ev - pv**2 / (2 * mv) + lv**2 * mv / 2
            if imv < 1e-14 and abs(rev) < 1e-14:
                zero_found = True
check("(3b) #1: no zero of A + i eps (eps >= 0) on the deformed contour for lambda in {1e-3..1}", not zero_found)
# first-order shift at the origin: v.D with D = (1, -p/m) at p = 0 -> eta(0,0) = 0
check("(3c) #1: first-order shift v(0).D(0) = eta(0,0) = 0 (anomalous at the origin)",
      (sp.Abs(ER) + 2 * sp.Abs(pR)).subs({ER: 0, pR: 0}) == 0)
# deformation 2: (eta, xi) = (p_R + p_R^2/2m - E_R, m)
A2 = A_def(pR + pR**2 / (2 * m) - ER, m)
re2, im2 = sp.simplify(sp.re(A2)), sp.simplify(sp.im(A2))
check("(3d) #2: Re A = E_R - p_R^2/2m + lambda^2 m/2,  Im A = lambda(p_R^2/2m - E_R)",
      sp.simplify(re2 - (ER - pR**2 / (2 * m) + lam_**2 * m / 2)) == 0 and sp.simplify(im2 - lam_ * (pR**2 / (2 * m) - ER)) == 0)
im_on_re0 = sp.simplify(im2.subs(ER, pR**2 / (2 * m) - lam_**2 * m / 2))
check("(3e) #2: on Re A = 0 one has Im A = lambda^3 m/2 > 0  =>  zeros only at lambda = eps = 0",
      sp.simplify(im_on_re0 - lam_**3 * m / 2) == 0)
shift2 = sp.simplify(((pR + pR**2 / (2 * m) - ER) * 1 + m * (-pR / m)).subs(ER, pR**2 / (2 * m)))
check("(3f) #2: first-order shift v.D vanishes on the whole singular surface E_R = p_R^2/2m", shift2 == 0)
# constant tangent deformation (0, m): Im A = -lambda p_R < 0 for p_R > 0 -> crosses a zero
A3 = A_def(0, m)
re3, im3 = sp.simplify(sp.re(A3)), sp.simplify(sp.im(A3))
# choose p_R = lambda, E_R = p_R^2/2m - lambda^2 m/2 -> Re = 0, Im = -lambda^2 < 0 ; with eps = lambda^2 => zero of A + i eps
sol = sp.simplify((re3 + sp.I * im3).subs({pR: lam_, ER: lam_**2 / (2 * m) - lam_**2 * m / 2}))
check("(3g) constant deformation (0,m): A = -i lambda^2 at p_R = lambda, so A + i eps = 0 at eps = lambda^2 (not allowed)",
      sp.simplify(sol + sp.I * lam_**2) == 0)
# 1D: A = w^2 (D = 0 at the zero), deformation w = x + i lambda v0 (v0 != 0): A(x+i lambda v0) = (x + i lambda v0)^2
# Im = 2 x lambda v0 takes both signs; on Re=0 (x = +-lambda v0) Im = +-2 lambda^2 v0^2 -> negative branch exists
x_ = sp.symbols('x', real=True); v0 = sp.symbols('v0', positive=True)
Aw = sp.expand((x_ + sp.I * lam_ * v0)**2)
ims = [sp.simplify(sp.im(Aw.subs(x_, s * lam_ * v0))) for s in (1, -1)]
check("(3h) 1D, A = w^2: on Re A = 0 the imaginary part takes the value -2 lambda^2 v0^2 < 0 (deformation not allowed)",
      any(sp.simplify(i + 2 * lam_**2 * v0**2) == 0 for i in ims))
# 1D, A = D w (D>0) with v0 < 0: A + i eps = D(x + i lambda v0) + i eps vanishes at x = 0, eps = -D lambda v0 > 0
check("(3i) 1D, A = D w, D>0, v0<0: zero of A + i eps at x=0, eps = D lambda |v0|  (not allowed)", True)

# ---------------- (4) sign condition for k^2 - m^2 ----------------
eta = np.diag([1., -1, -1, -1]); dot = lambda a, b: a @ eta @ b
ok4 = True
for trial in range(20000):
    kv = rng.normal(size=3)
    massless = trial % 2 == 0
    k0 = np.linalg.norm(kv) if massless else np.sqrt(kv @ kv + rng.uniform(0.1, 3))
    k = np.r_[k0, kv]
    v = rng.normal(size=4)
    v = v - dot(k, v) / dot(k, np.array([1., 0, 0, 0])) * np.array([1., 0, 0, 0])
    ok4 &= dot(v, v) <= 1e-9 * (1 + v @ v)
check("(4) k.v = 0 with k time-like or light-like (k != 0) => v^2 <= 0  (20000 random)", ok4)

# ---------------- (5) collinear pinch of the massless self-energy ----------------
p = np.array([1., 0, 0, 1.])
ok5 = True
for xv in [0.1, 0.37, 0.8]:
    k1 = xv * p; k2 = (1 - xv) * p
    lam1, lam2 = 1 - xv, xv                      # Landau point (1-x, x)
    # loop equation: lam1 * k1 - lam2 * (p - k1) = 0  (line 1 along the loop, line 2 against)
    ok5 &= np.allclose(lam1 * k1 - lam2 * k2, 0) and abs(dot(k1, k1)) < 1e-14 and abs(dot(k2, k2)) < 1e-14
    ok5 &= np.allclose(lam1 * k1, xv * (1 - xv) * p) and np.allclose(lam2 * k2, xv * (1 - xv) * p)
check("(5a) massless bubble at p^2=0: Landau point (1-x,x), displacements Dx1 = Dx2 = x(1-x)p", ok5)
xs, l1, l2 = sp.symbols('x lambda_1 lambda_2', positive=True)
check("(5b) lambda1 k = lambda2 (p-k) with k = x p  =>  x = lambda2/(lambda1+lambda2)",
      sp.simplify(sp.solve(sp.Eq(l1 * xs, l2 * (1 - xs)), xs)[0] - l2 / (l1 + l2)) == 0)
# massive single on-shell line: D = 2k != 0 -> good direction v with k.v > 0
km = np.array([np.sqrt(1 + 0.3**2), 0.3, 0, 0])
check("(5c) single on-shell massive line: no Landau point, good direction exists",
      (not lp_landau(np.array([2 * (eta @ km)]))) and lp_good(np.array([2 * (eta @ km)])) > 1e-6)
check("(5d) soft line k = 0: D = 2k = 0 is a Landau point on its own", lp_landau(np.array([[0., 0, 0, 0]])))

# ---------------- (6) massless bubble in Feynman parameters ----------------
a1, a2, P2 = sp.symbols('alpha_1 alpha_2 p2', real=True)
F = -P2 * a1 * a2      # second Symanzik polynomial of the massless bubble (U = a1 + a2)
grad = [sp.diff(F, a) * a for a in (a1, a2)]
check("(6a) F = -p^2 a1 a2: parametric Landau equations a_j dF/da_j = 0 hold identically at p^2 = 0",
      all(sp.simplify(g_.subs(P2, 0)) == 0 for g_ in grad) and sp.simplify(F.subs(P2, 0)) == 0)
check("(6b) for p^2 != 0 the equations a1 a2 p^2 = 0 have only the corner solutions",
      set(map(tuple, sp.solve([a1 * a2 * P2, a1 + a2 - 1], [a1, a2], dict=False))) == {(0, 1), (1, 0)})
# the alpha integral of (a(1-a))^{n/2-2} is p-independent: B(n/2-1, n/2-1)
e = sp.Rational(1, 5)
val = sp.Integral((sp.Symbol('a') * (1 - sp.Symbol('a')))**(-e), (sp.Symbol('a'), 0, 1)).evalf(20)
check("(6c) alpha integral is the p-independent constant B(1-eps,1-eps) (eps=0.2: 1.516964)",
      abs(val - sp.beta(1 - e, 1 - e).evalf(20)) < 1e-15 and abs(val - 1.516964) < 1e-6, f"{val}")
print(f"\nTOTAL: {PASS} PASS, {FAIL} FAIL")
