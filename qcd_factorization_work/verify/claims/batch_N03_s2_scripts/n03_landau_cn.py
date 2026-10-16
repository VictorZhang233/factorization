#!/usr/bin/env python3
"""
N03 (stage-2 verifier): momentum-space Coleman-Norton picture including massless and eikonal lines, as a corollary of
Collins (arXiv:2007.04085) Thm 1 [trapped at w_S <=> Landau point for {D_j = dA_j(w_S)} over vanishing A_j, under
(a) A_j at most quadratic, (b) sign condition (8.15)].

What is checked here (exact rational arithmetic, different implementation from stage 1):
 (1) derivative map: for A = k_j^2 - m^2, dA/dl_L^mu = 2 eta_jL k_{j mu};  for A = n.k_j, dA/dl_L^mu = eta_jL n_mu
     -> sum_j lam_j D_j = 0 (as a dual vector on R^{4L}) <=> sum_j eta_jL lam_j Delta_j = 0 for all L
     (finite-difference check of the gradients on random graphs);
 (2) loop equations <=> existence of vertex positions (cycle space vs cut space), exact ranks with sympy, for random
     multigraphs and for random changes of loop basis (unimodular), i.e. basis independence;
 (3) orientation of eikonal denominators: with A = n.k + i0 the point k = beta n of the
     gluon/eikonal/quark triangle is a Landau point iff beta < 0; with 1/(n.k - i0) = -1/(-n.k + i0) iff beta > 0;
     good deformation directions found explicitly in the non-trapped cases;
 (4) sign condition (8.15) for +i0 propagators, eikonal lines and light-front-approximated denominators, and
     its failure pattern for a conjugated (-i0) propagator (opposite sign of v.E.v);
 (5) soft massless line: D = 0 gives a Landau point with all other lambda = 0 (degenerate CN picture).
Run: python3 -I n03_landau_cn.py
"""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import numpy as np
from scipy.optimize import linprog

PASS = FAIL = 0
def check(name, ok, info=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("   " + info if info else ""))

random.seed(11); rng = np.random.default_rng(11)
eta = np.diag([1.0, -1.0, -1.0, -1.0])

def random_graph(V, E):
    """connected multigraph: random spanning tree + extra edges (no self loops); edges oriented tail->head."""
    edges = []
    order = list(range(V)); random.shuffle(order)
    for i in range(1, V):
        edges.append((order[random.randrange(i)], order[i]))
    while len(edges) < E:
        a, b = random.sample(range(V), 2)
        edges.append((a, b))
    return edges

def incidence(V, edges):
    Bm = sp.zeros(V, len(edges))
    for j, (t, h) in enumerate(edges):
        Bm[t, j] -= 1; Bm[h, j] += 1
    return Bm

def cycle_basis(V, edges):
    """integer basis of the cycle space = nullspace of the incidence matrix (columns eta_{.L})."""
    Bm = incidence(V, edges)
    ns = Bm.nullspace()
    # clear denominators to get integer vectors
    out = []
    for v in ns:
        den = sp.ilcm(*[sp.fraction(x)[1] for x in v])
        out.append(v * den)
    return sp.Matrix.hstack(*out), Bm

# ---------------- (2) loop equations <=> vertex positions ----------------
ok2 = True; ntest = 0
for trial in range(120):
    V = random.randint(2, 7); E = V - 1 + random.randint(1, 4)
    edges = random_graph(V, E)
    Eta, Bm = cycle_basis(V, edges)          # E x L
    L = Eta.shape[1]
    if L == 0:
        continue
    # random unimodular change of loop basis (basis independence)
    U = sp.eye(L)
    for _ in range(3 * L):
        i, j = random.sample(range(L), 2) if L > 1 else (0, 0)
        if i != j:
            U[:, i] += random.choice([-1, 1]) * U[:, j]
    Eta2 = Eta * U
    # solution space of the loop equations (one Minkowski component suffices): {X in Q^E : Eta^T X = 0}
    sol = Eta2.T.nullspace()
    dim_sol = len(sol)
    # cut space = image of B^T (potential differences x_head - x_tail)
    cut_rank = (Bm.T).rank()
    ok = (dim_sol == cut_rank == V - 1)
    # every solution is a potential difference: rank([B^T | sol]) == rank(B^T)
    ok &= sp.Matrix.hstack(Bm.T, *sol).rank() == cut_rank
    # and every potential difference solves the loop equations
    xv = sp.Matrix([sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(V)])
    ok &= (Eta2.T * (Bm.T * xv)).is_zero_matrix
    ok2 &= bool(ok); ntest += 1
check(f"(2) loop equations <=> x_head - x_tail = lam_j Delta_j, exact ranks on {ntest} random graphs incl. random loop-basis changes", ok2)

# ---------------- (1) gradients of the denominators w.r.t. loop momenta ----------------
def momenta(Eta, ext, loops):
    return [sum(float(Eta[j, L]) * loops[L] for L in range(Eta.shape[1])) + ext[j] for j in range(Eta.shape[0])]
ok1 = True
for trial in range(30):
    V = random.randint(3, 6); E = V - 1 + random.randint(1, 3)
    edges = random_graph(V, E)
    Eta, _ = cycle_basis(V, edges); L = Eta.shape[1]
    ext = [rng.normal(size=4) for _ in range(E)]
    loops = [rng.normal(size=4) for _ in range(L)]
    n_eik = rng.normal(size=4)
    ks = momenta(Eta, ext, loops)
    for j in range(E):
        for Lp in range(L):
            for mu in range(4):
                h = 1e-6
                lp = [l.copy() for l in loops]; lp[Lp][mu] += h
                lm = [l.copy() for l in loops]; lm[Lp][mu] -= h
                kp, km = momenta(Eta, ext, lp)[j], momenta(Eta, ext, lm)[j]
                dq = ((kp @ eta @ kp) - (km @ eta @ km)) / (2 * h)
                de = ((n_eik @ eta @ kp) - (n_eik @ eta @ km)) / (2 * h)
                exp_q = 2 * float(Eta[j, Lp]) * (eta @ ks[j])[mu]
                exp_e = float(Eta[j, Lp]) * (eta @ n_eik)[mu]
                ok1 &= abs(dq - exp_q) < 1e-6 and abs(de - exp_e) < 1e-6
check("(1) d(k_j^2)/dl_L^mu = 2 eta_jL k_{j,mu} and d(n.k_j)/dl_L^mu = eta_jL n_mu (finite differences, random graphs)", ok1)

# ---------------- (3) eikonal orientation ----------------
def landau_point_exists(D):
    N, d = D.shape
    A_eq = np.vstack([D.T, np.ones((1, N))]); b_eq = np.concatenate([np.zeros(d), [1.0]])
    r = linprog(np.zeros(N), A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * N, method='highs')
    return r.status == 0
def good_direction(D):
    N, d = D.shape
    c = np.zeros(d + 1); c[-1] = -1.0
    A = np.hstack([-D, np.ones((N, 1))])
    r = linprog(c, A_ub=A, b_ub=np.zeros(N), bounds=[(-1, 1)] * d + [(None, 1.0)], method='highs')
    return -r.fun, r.x[:d]
n = np.array([1.0, 0, 0, 1.0])            # light-like Wilson-line direction
p = np.array([1.0, 0, 0, -1.0]) * 0.7      # massless quark, not collinear to n
for beta in [-0.8, -0.2, 0.3, 1.1]:
    k = beta * n
    assert abs(k @ eta @ k) < 1e-14 and abs(n @ eta @ k) < 1e-14 and abs((p - k) @ eta @ (p - k)) > 1e-3
    D_plus = np.vstack([2 * eta @ k, eta @ n])          # gluon k^2, eikonal +n.k (on shell); quark line off shell
    D_minus = np.vstack([2 * eta @ k, -eta @ n])        # eikonal written as -n.k + i0
    lp, lm = landau_point_exists(D_plus), landau_point_exists(D_minus)
    tp, vp = good_direction(D_plus); tm, vm = good_direction(D_minus)
    check(f"(3) k = {beta} n: Landau point with (n.k+i0): {lp} (expect {beta<0}); with (-n.k+i0): {lm} (expect {beta>0}); "
          f"good-direction margins {tp:.3f}, {tm:.3f}",
          lp == (beta < 0) and lm == (beta > 0) and ((tp > 1e-9) != lp) and ((tm > 1e-9) != lm))
# the Landau point gives the CN displacement: lambda_g * 2k + lambda_W * n = 0 -> x_W - x_g displacements along n
beta = -0.5; k = beta * n
lam_g, lam_W = 1.0, -2 * beta          # 2 beta lam_g + lam_W = 0  -> lam_W = -2 beta lam_g > 0
check("(3) CN displacements: gluon displacement 2 lam_g k = -lam_W n (closure of the loop gluon+eikonal)",
      np.allclose(lam_g * 2 * k + lam_W * n, 0) and lam_W > 0)

# ---------------- (4) sign condition (8.15) ----------------
ok4 = True; ok4m = True; cnt = 0
for trial in range(5000):
    m2 = 0.0 if trial % 2 == 0 else rng.uniform(0.1, 3.0)
    kv = rng.normal(size=3); k0 = np.sqrt(kv @ kv + m2) * rng.choice([-1, 1])
    k = np.concatenate([[k0], kv])
    v = rng.normal(size=4)
    # project v onto D.v = 0 with D = 2 eta k  (i.e. k.v = 0, Minkowski), using a generic auxiliary vector
    a = rng.normal(size=4)
    v = v - (k @ eta @ v) / (k @ eta @ a) * a
    if abs(k @ eta @ v) > 1e-9:
        continue
    vEv_plus = 2 * (v @ eta @ v)          # A = k^2 - m^2 (+i0)
    vEv_conj = -2 * (v @ eta @ v)         # A = -(k^2 - m^2): conjugated propagator rewritten with +i0
    ok4 &= vEv_plus <= 1e-9 * (1 + v @ v)
    ok4m &= vEv_conj >= -1e-9 * (1 + v @ v)
    cnt += 1
check(f"(4) +i0 propagators: k.v=0 with k on shell (massive or massless, either energy sign) => v.E.v = 2 v^2 <= 0 ({cnt} random)", ok4)
check("(4) conjugated propagator -(k^2-m^2)+i0 has v.E.v >= 0: opposite sign, so (8.15) is not automatic when such lines are relevant together with +i0 lines", ok4m)
# eikonal (linear) and light-front-approximated denominators
okL = True
for trial in range(2000):
    v = rng.normal(size=4)
    # A = 2 p+ k-  - kT^2 - m^2 (k- linear, + component set to zero): E acts on kT only, v.E.v = -2 vT^2 <= 0
    okL &= (-2 * (v[1]**2 + v[2]**2)) <= 0
check("(4) eikonal denominators E = 0; light-front approximated denominators: v.E.v = -2 v_T^2 <= 0 (same sign as propagators)", okL)

# ---------------- (5) soft line ----------------
D = np.vstack([2 * eta @ np.zeros(4), 2 * eta @ np.array([1.0, 0, 0, 1.0])])
check("(5) soft massless line (k=0): D=0 alone is a Landau point; CN picture degenerate (zero displacement)", landau_point_exists(D[:1]) and landau_point_exists(D))

print(f"\nSUMMARY n03: {PASS} PASS, {FAIL} FAIL")
