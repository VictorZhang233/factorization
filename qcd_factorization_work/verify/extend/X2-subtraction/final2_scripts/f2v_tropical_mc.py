"""X2 final2 -- f2v_tropical_mc.py: INDEPENDENT numerical evaluation of parametric integrals by tropical Monte Carlo
(exact sampling from the tropical approximation on the normal fan; cf. Borinsky, AIHPD 10 (2023) 635), used to check
  (A) the full planar two-loop vertex at eps = 0 (projective form, J = int F^{-2}) against Usyukina-Davydychev,
      m2 = 0.04 and 0.01 (Qt2 = 1): exact 82.282..., 223.863... (closed form of Thm E.3(v));
  (B) the closed forms of the singles SS, HS, C1S (Gamma products) and the two-dimensional representations of HC1, C1C1
      (Prop E.4(d)) at points (eps, delta) of the Lee-Pomeransky convergence domain, Qt2 = 1, m2 = 1/3:
         I_R = Gamma(t) / (Gamma(3t - |a|) prod_l Gamma(a_l)) * int_{R_+^6} x^{a-1} (U+F)^{-t} dx,   t = 2 - eps.
Method: for G = U + F (or the pair U, F in projective form) with positive coefficients, the tropical integrand
exp(<a,X> - t h_G(X)) is a pure exponential on every cone of the normal fan; the cones (normal cones of the vertices of
the Newton polytope, rays = outer facet normals) are triangulated (Delaunay on a cross-section; the triangulation is
checked to tile the cross-section by volume), integrated exactly, and sampled exactly; the weight f/f_tr is bounded.
Facets: exact (from f2v_conv_intervals.hull_facets_exact).  Polynomials: f2v_UF_polytopes (independent code).
Run: python3 -I f2v_tropical_mc.py  (log: ../final2_logs/f2v_tropical_mc.log)"""
import sys, os, json, itertools, math
from fractions import Fraction as Fr
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.spatial import Delaunay, ConvexHull
import sympy as sp
import mpmath as mp
import functools
print = functools.partial(print, flush=True)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import f2v_UF_polytopes as V
    import f2v_conv_intervals as CI
LOGDIR = os.path.join(os.path.dirname(HERE), 'final2_logs')
ALL_OK = True
def report(name, ok):
    global ALL_OK
    ALL_OK &= bool(ok)
    print(f"   [{'PASS' if ok else 'FAIL'}] {name}")

def numeric_poly(E, qt2, mm):
    """support (n x 6 int array) and coefficients of the polynomial E(y) at Qt2 = qt2, m2 = mm (P' = Qt2/(2P))"""
    E2 = sp.expand(E.subs(V.Pp, V.Qt2/(2*V.P)))
    pol = sp.Poly(E2, *V.XS)
    S = np.array(pol.monoms(), dtype=float)
    c = np.array([float(sp.cancel(cc).subs({V.Qt2: qt2, V.m2: mm, V.P: 1/math.sqrt(2)})) for cc in pol.coeffs()])
    assert np.all(c > 0)
    return S, c

def log_poly_minus_trop(S, c, X):
    """log(sum_v c_v e^{<v,X>}) - max_v <v,X>, for X of shape (N, n)"""
    E = X @ S.T                       # (N, nterms)
    mx = E.max(axis=1)
    return np.log(np.sum(c[None, :]*np.exp(E - mx[:, None]), axis=1)), mx

class TropicalIntegral:
    """integral over R^n (projective=False) or R^n / R(1,...,1) (projective=True, X_n = 0) of
       exp(<a,X>) * prod_j P_j(e^X)^{-t_j}  for positive polynomials P_j"""
    def __init__(self, polys_int_supports, a, ts, projective):
        self.a = np.array(a, float); self.ts = list(ts); self.proj = projective
        supps = [sorted(set(tuple(int(v) for v in row) for row in S)) for S in polys_int_supports]
        self.supps = supps
        Msum = sorted(set(tuple(sum(z) for z in zip(*combo)) for combo in itertools.product(*supps)))
        fl, n, cols = CI.hull_facets_exact(Msum)
        self.dim = n
        amb = len(Msum[0])
        # outer normals (in ambient coords); for the projective case reduce mod (1,...,1): last coordinate 0
        rays = []
        for mu, nu, on in fl:
            r = np.array([-m for m in mu], float)
            if projective: r = r - r[-1]
            rays.append((r, on))
        self.Msum = Msum; self.rays = rays
        # vertices of Msum: points lying on >= dim facets with spanning normals
        pts = np.array(Msum, float); bary = pts.mean(axis=0)
        cones = []
        for vi, p in enumerate(Msum):
            inc = [r for r, on in rays if vi in on]
            if len(inc) < n: continue
            R = np.array(inc)
            Rr = R[:, :-1] if projective else R
            if np.linalg.matrix_rank(Rr) < n: continue
            # exponent vector on this cone: w = a - sum_j t_j v_j, v_j = argmax over supp_j at an interior direction
            interior = Rr.sum(axis=0)
            xdir = np.concatenate([interior, [0.0]]) if projective else interior
            w = self.a.copy()
            for S, t in zip(supps, ts):
                Sa = np.array(S, float); vals = Sa @ xdir
                j = int(np.argmax(vals)); assert np.sum(np.abs(vals - vals[j]) < 1e-9) == 1
                w -= t*Sa[j]
            wr = w[:-1] if projective else w
            # triangulate the cone over a cross-section <c, y> = 1, c = (vertex - barycentre)
            cvec = (np.array(p, float) - bary); cr = cvec[:-1] if projective else cvec
            if projective:
                # in the quotient, use c reduced consistently: the functional <c, r> is invariant since sum(c) = 0
                pass
            dots = Rr @ cr
            assert np.all(dots > 1e-12), "cross-section functional not positive on the cone"
            Y = Rr/dots[:, None]
            if len(inc) == n:
                simplices = [list(range(n))]
            else:
                # coordinates on the hyperplane: orthonormal basis of cr^perp
                Q, _ = np.linalg.qr(np.column_stack([cr] + [np.eye(n)[:, k] for k in range(n)]))
                B = Q[:, 1:n]
                Yc = Y @ B
                tri = Delaunay(Yc, qhull_options='QJ Qbb Qc')
                simplices = [list(s) for s in tri.simplices]
                vol_tri = sum(abs(np.linalg.det(np.column_stack([Yc[s[k]] - Yc[s[0]] for k in range(1, n)])))/math.factorial(n - 1)
                              for s in simplices)
                vol_hull = ConvexHull(Yc).volume
                assert abs(vol_tri/vol_hull - 1) < 1e-9, f"triangulation does not tile: {vol_tri} vs {vol_hull}"
            for s in simplices:
                Rs = Rr[s]
                det = abs(np.linalg.det(Rs))
                if det < 1e-12: continue
                lam = -(Rs @ wr)
                if np.any(lam <= 0): raise ValueError("not in the convergence domain")
                cones.append((Rs, lam, det*np.prod(1.0/lam), w))
        self.cones = cones
        self.Itrop = sum(c[2] for c in cones)
    def sample(self, polys_numeric, N, rng):
        probs = np.array([c[2] for c in self.cones])/self.Itrop
        idx = rng.choice(len(self.cones), size=N, p=probs)
        tot = np.zeros(N)
        Xall = np.zeros((N, len(self.a)))
        for ci, (Rs, lam, I, w) in enumerate(self.cones):
            sel = np.where(idx == ci)[0]
            if len(sel) == 0: continue
            s = rng.exponential(1.0/lam[None, :], size=(len(sel), len(lam)))
            Xr = s @ Rs
            Xall[sel, :Xr.shape[1]] = Xr      # projective: last coordinate stays 0
        logw = np.zeros(N)
        for (S, c), t in zip(polys_numeric, self.ts):
            lr, _ = log_poly_minus_trop(S, c, Xall)
            logw -= t*lr
        wts = np.exp(logw)
        return self.Itrop*wts.mean(), self.Itrop*wts.std()/math.sqrt(N)

def run(Ti, polys_numeric, N, seed, reps=16):
    rng = np.random.default_rng(seed); vals = []
    for _ in range(reps):
        m, e = Ti.sample(polys_numeric, N, rng); vals.append(m)
    vals = np.array(vals)
    return vals.mean(), vals.std(ddof=1)/math.sqrt(len(vals)), vals

mp.mp.dps = 30
# ------------------------------------------------------------------------------------------------ (A) full planar
print("(A) full planar two-loop vertex at eps = 0: J = int_simplex F^{-2} (projective) vs Usyukina-Davydychev")
U, F = V.FULL['planar']['U'], V.FULL['planar']['F']
def UD(mm):
    L = mp.log(1/mm)
    return (1 + mm)*(12*mp.polylog(4, -mm) + L**4/4 + mp.pi**2*L**2/2 + 7*mp.pi**4/60)/((1 - mm)*(1 + mm)**4)
for mm in [0.04, 0.01]:
    SF_, cF = numeric_poly(F, 1.0, mm)
    Ti = TropicalIntegral([SF_], [1]*6, [2.0], projective=True)
    m_, e_, vals = run(Ti, [(SF_, cF)], 200000, 11)
    ex = float(UD(mp.mpf(mm)))
    report(f"m2 = {mm}: tropical MC J = {m_:.5f} +- {e_:.5f} (16 x 2e5 samples; {len(Ti.cones)} simplicial cones) vs "
           f"UD {ex:.5f}  (pull {(m_ - ex)/e_:+.2f})", abs(m_ - ex) < 4*e_ + 1e-3*ex)

# ------------------------------------------------------------------------------------------------ (B) singles
print("\n(B) singles at points of the Lee-Pomeransky convergence domain (Qt2 = 1, m2 = 1/3, P = P' = 1/sqrt2)")
Gm = mp.gamma
def Bf(x, y): return Gm(x)*Gm(y)/Gm(x + y)
def closed(R, ev, d, mm):
    t = 2 - ev; a = {l: 1 + d[l] for l in V.LINES}
    if R == 'SS':
        Aa = a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*t; Bb = a['b1'] + a['b2'] + a['g1'] + a['g2'] - 2*t
        num = (Gm(t - a['g1'])*Gm(t - a['g2'])*Gm(Aa)*Gm(Bb)*mm**(-Aa - Bb)*Bf(a['a1'], a['a2'] + a['g1'] - t)
               *Bf(a['b1'], a['b2'] + a['g1'] - t))
        return num/mp.fprod([Gm(a[l]) for l in V.LINES])
    if R == 'HS':
        N1 = a['g1'] + a['a2'] + a['b2']
        T0 = Gm(N1 - t)*Gm(t - a['g1'] - a['b2'])*Gm(t - a['g1'] - a['a2'])/(Gm(a['a2'])*Gm(a['b2'])*Gm(2*t - N1))
        S2 = (Gm(t - a['g2'])*Gm(a['a1'] + a['g2'] - t)*Gm(a['b1'] + a['g2'] - t)/(Gm(a['g2'])*Gm(a['a1'])*Gm(a['b1']))
              *mm**(2*t - 2*a['g2'] - a['a1'] - a['b1']))
        return T0*S2
    if R == 'C1S':
        c = a['a2'] + a['g1'] - t
        num = (Gm(a['b2'])*Gm(t - a['g2'])*Gm(a['b1'] + a['g2'] - t)*Bf(c, a['a1'])
               *Gm(a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*t)*Bf(t - a['g1'] - a['b2'], t - a['a2'])
               *mm**(-(a['b1'] + a['g2'] - t) - (a['a1'] + a['a2'] + a['g1'] + a['g2'] - 2*t)))
        return num/mp.fprod([Gm(a[l]) for l in V.LINES])
    if R == 'HC1':
        N1 = a['g1'] + a['a2'] + a['b2']
        pref = (Gm(a['a1'] + a['g2'] - t)*Gm(N1 - t)*Bf(t - a['b2'], t - a['g1'] - a['a2'])
                /(Gm(a['g2'])*Gm(a['a1'])*Gm(a['g1'])*Gm(a['a2'])*Gm(a['b2']))*mm**(t - a['a1'] - a['g2']))
        f = lambda z, w: (z**(t - a['b1'] - a['g2'] - 1)*(1 - z)**(t - a['a1'] - 1)*w**(a['a2'] - 1)*(1 - w)**(a['g1'] - 1)
                          *(w + z - z*w)**(t - N1))
        return pref*quad2(f)
    if R == 'C1C1':
        bpp = a['a1'] + a['g1'] + a['a2'] - t
        pref = (Gm(a['g1'] + a['a2'] - t)*Gm(a['g2'] + bpp - t)/(Gm(a['g1'])*Gm(a['a2'])*Gm(a['g2'])*Gm(bpp))
                *mm**(t - a['g2'] - bpp))
        f = lambda y, z: (y**(t - a['g1'] - 1)*(1 - y)**(t - a['a2'] - 1)*z**(t - a['g2'] - a['b1'] - 1)*(1 - z)**(t - bpp - 1)
                          *(z + y - y*z)**(-a['b2']))
        return pref*quad2(f)
def quad2(f):
    # endpoint-softening substitutions u = s^4 on both variables (all endpoint singularities are integrable)
    g = lambda s1, s2: 16*s1**3*s2**3*f(s1**4, s2**4)
    h1 = lambda s1: mp.quad(lambda s2: g(s1, s2), [0, mp.mpf(1)/2, 1])
    return mp.quad(h1, [0, mp.mpf(1)/2, 1])

POINTS = json.load(open(os.path.join(LOGDIR, 'f2_E4_points.json')))
extra = {'SS': {'eps': '-1/5', 'g1': '3/10', 'g2': '3/10', 'a1': '1/10', 'a2': '0', 'b1': '0', 'b2': '1/5'},
         'HS': {'eps': '-1/4', 'g1': '-1/10', 'g2': '7/10', 'a1': '1/10', 'a2': '0', 'b1': '0', 'b2': '0'},
         'C1S': {'eps': '-3/10', 'g1': '1/10', 'g2': '7/10', 'a1': '0', 'a2': '1/2', 'b1': '0', 'b2': '-1/5'},
         'HC1': {'eps': '-1/4', 'g1': '-1/10', 'g2': '1/10', 'a1': '7/10', 'a2': '0', 'b1': '-2/5', 'b2': '1/10'},
         'C1C1': {'eps': '-2/5', 'g1': '1/2', 'g2': '1/10', 'a1': '0', 'a2': '7/10', 'b1': '-2/5', 'b2': '0'}}
mm = mp.mpf(1)/3
for R in ['SS', 'HS', 'C1S', 'HC1', 'C1C1']:
    U, F = V.SDATA[R]['U'], V.SDATA[R]['F']
    G = sp.expand(U + F)
    SG, cG = numeric_poly(G, 1.0, float(mm))
    for tag, pt in [('max-margin', POINTS['max_margin'][R]), ('extra', extra[R])]:
        ev = Fr(pt['eps']); d = {l: Fr(pt[l]) for l in V.LINES}
        t = 2 - ev; a = [1 + d[l] for l in V.LINES]; asum = sum(a)
        try:
            Ti = TropicalIntegral([SG], [float(x) for x in a], [float(t)], projective=False)
        except ValueError as exc:
            print(f"   [SKIP] {R} {tag} point {pt}: not inside the LP convergence domain"); continue
        m_, e_, vals = run(Ti, [(SG, cG)], 200000, 7)
        pref = math.gamma(float(t))/(math.gamma(float(3*t - asum))*math.prod(math.gamma(float(x)) for x in a))
        mc = pref*m_; mce = pref*e_
        cf = closed(R, mp.mpf(ev.numerator)/ev.denominator, {l: mp.mpf(d[l].numerator)/d[l].denominator for l in V.LINES}, mm)
        report(f"{R} {tag} (eps={pt['eps']}, delta={ {l: str(d[l]) for l in V.LINES if d[l] != 0} }): tropical MC "
               f"{mc:.6g} +- {mce:.2g}  vs closed form / 2D representation {float(cf):.6g}  (pull {(mc - float(cf))/mce:+.2f}, "
               f"rel dev {abs(mc/float(cf) - 1):.1e})", abs(mc - float(cf)) < 4*mce + 2e-3*abs(float(cf)))
print("\nALL CHECKS PASS (f2v_tropical_mc)" if ALL_OK else "\nSOME CHECK FAILED (f2v_tropical_mc)")
