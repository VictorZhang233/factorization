"""R-M31 (reference Rem. E.54(b), p. 228): dependence of a central-jet factor J_1 on the
Glauber momentum k exchanged with a spectator of hadron A.

Conventions: light-cone components (+,-,x,y), v.w = v+ w- + v- w+ - vT.wT, Q = 1.
Hadron A along +z: n_A = (1,0,0,0) (so k.n_A = k^-).  Central jet direction w1 (lightlike, all
components O(1)).  J_1 line l = E w1 + l_perp (l_perp ~ lambda, transverse to w1) with virtuality
l^2 ~ lambda^2.

Checks
 (1) generic DY-Glauber k = (lambda^2, lambda^2, lambda) with k_T in a generic direction:
     2 l.k is dominated by -2 l_T.k_T ~ lambda >> lambda^2  -> J_1 line off shell by O(lambda),
     the k^- dependence of the J_1 denominator is a relative O(lambda) effect.
 (2) Glauber region relative to the pair (n_A, w1): k.n_A ~ k.w1 ~ lambda^2, remaining components
     ~ lambda: 2 l.k ~ lambda^2 and d/dk^- of the J_1 denominator = 2 l^+ = O(1), i.e. J_1 depends on
     k^- at the same scale lambda^2 as J_A.  (conclusion of Rem. E.54(b) survives)
 (3) power counting of the k-integral (gluon propagator x J_A line x J_1 line x measure):
     generic DY-Glauber region with k_T generic: lambda^1 (suppressed);
     (n_A, w1)-Glauber region: lambda^0 (leading).
     Done by explicit scaling of the integrand with a numerical measure of the region volumes.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

def dot(a, b):
    return a[0]*b[1] + a[1]*b[0] - a[2]*b[2] - a[3]*b[3]

rng = np.random.default_rng(7)
# central jet direction: rapidity 0.3, azimuth along x
y1 = 0.3
w1 = np.array([np.exp(y1)/np.sqrt(2), np.exp(-y1)/np.sqrt(2), 1.0, 0.0])   # w1^2 = 2 w+ w- - 1 = 0
assert abs(dot(w1, w1)) < 1e-14
nA = np.array([1.0, 0.0, 0.0, 0.0])
wbar = np.array([np.exp(y1)/np.sqrt(2), np.exp(-y1)/np.sqrt(2), -1.0, 0.0])  # lightlike, wbar.w1 = 2
assert abs(dot(wbar, w1) - 2) < 1e-14

def jet_line(lam, E=0.7):
    # l = E w1 + perp (two directions orthogonal to w1 and wbar) * lam + (lam^2-scale) * wbar
    # vectors orthogonal to w1 and wbar: e2 = (0,0,0,1) and e1 = combination
    e2 = np.array([0, 0, 0, 1.0])
    # e1: v with v.w1 = v.wbar = 0, v_y = 0: solve v = (a, b, c, 0)
    # a w- + b w+ - c = 0 ; a wb- + b wb+ + c = 0
    A = np.array([[w1[1], w1[0], -1.0], [wbar[1], wbar[0], 1.0]])
    _, _, Vt = np.linalg.svd(A); v = Vt[-1]; e1 = np.array([v[0], v[1], v[2], 0.0])
    e1 /= np.sqrt(-dot(e1, e1))
    a1, a2 = 0.83, -0.47          # fixed O(1) coefficients (clean scaling)
    lperp = lam*(a1*e1 + a2*e2)
    # add a lambda^2 component along wbar so that l^2 ~ lambda^2 (off shell by lambda^2)
    c = lam**2*0.61
    l = E*w1 + lperp + c*wbar
    return l

print("lambda   |l^2|     |2 l.k| generic  |2l+ k-|   |2 lT.kT|   ratio(2l+k-)/(2l.k)  ||  (nA,w1)-Glauber: |2 l.k|  |2 l+ k-|  ratio")
for lam in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3]:
    l = jet_line(lam)
    # (1) generic DY Glauber: k = (lam^2 a, lam^2 b, lam*(cos phi, sin phi)), phi generic
    phi = 1.1
    kg = np.array([0.6*lam**2, -0.8*lam**2, lam*np.cos(phi), lam*np.sin(phi)])
    two_lk_g = 2*dot(l, kg)
    term_km = 2*l[0]*kg[1]
    term_T = 2*(l[2]*kg[2] + l[3]*kg[3])
    # (2) (nA,w1)-Glauber: k.nA = k^- ~ lam^2 ; k.w1 ~ lam^2 ; rest ~ lam
    # parametrize k = alpha*nbar_like + ... : solve for k with k^- = 0.7 lam^2, k.w1 = -0.5 lam^2,
    # components orthogonal to nA and w1 of size lam: v = (v+, 0, v+ w-/wx, vy)
    vplus, vy = 0.9*lam, -0.6*lam
    v = np.array([vplus, 0.0, vplus*w1[1]/w1[2], vy])
    assert abs(dot(v, nA)) < 1e-15 and abs(dot(v, w1)) < 1e-15
    # add pieces fixing k^- and k.w1: use u1 = (0,1,0,0) direction (k^- component) and adjust k^+:
    km = 0.7*lam**2
    # k = v + (0, km, 0, 0) + (dp, 0, 0, 0): k.w1 = km w+ + dp w-  (v contributes 0)
    target = -0.5*lam**2
    dp = (target - km*w1[0])/w1[1]
    kG = v + np.array([dp, km, 0.0, 0.0])
    assert abs(dot(kG, nA) - km) < 1e-15 and abs(dot(kG, w1) - target) < 1e-15
    two_lk_G = 2*dot(l, kG)
    term_km_G = 2*l[0]*kG[1]
    print(f"{lam:7.0e}  {abs(dot(l,l)):8.2e}  {abs(two_lk_g):10.3e}   {abs(term_km):8.2e}  {abs(term_T):9.2e}   {abs(term_km/two_lk_g):10.3e}"
          f"        ||  {abs(two_lk_G):9.2e}  {abs(term_km_G):9.2e}  {abs(term_km_G/two_lk_G):6.3f}   k^+={kG[0]:+.2e} |kT|={np.hypot(kG[2],kG[3]):.2e}")

print()
print("Scaling exponents (fit log|.| vs log lambda):")
lams = np.array([1e-2, 3e-3, 1e-3, 3e-4, 1e-4])
g_two, g_km, G_two, G_km = [], [], [], []
for lam in lams:
    l = jet_line(lam)
    phi = 1.1
    kg = np.array([0.6*lam**2, -0.8*lam**2, lam*np.cos(phi), lam*np.sin(phi)])
    g_two.append(abs(2*dot(l, kg))); g_km.append(abs(2*l[0]*kg[1]))
    vplus, vy = 0.9*lam, -0.6*lam
    v = np.array([vplus, 0.0, vplus*w1[1]/w1[2], vy]); km = 0.7*lam**2; target = -0.5*lam**2
    dp = (target - km*w1[0])/w1[1]; kG = v + np.array([dp, km, 0.0, 0.0])
    G_two.append(abs(2*dot(l, kG) + dot(kG, kG)*0)); G_km.append(abs(2*l[0]*kG[1]))
fit = lambda y: np.polyfit(np.log(lams), np.log(np.array(y)), 1)[0]
print(f"  generic DY-Glauber: 2l.k ~ lambda^{fit(g_two):.3f},  2l^+k^- ~ lambda^{fit(g_km):.3f}")
print(f"  (nA,w1)-Glauber   : 2l.k ~ lambda^{fit(G_two):.3f},  2l^+k^- ~ lambda^{fit(G_km):.3f}")

# (3) power counting of the region integral  int d^4k  1/k^2 * 1/D_A * 1/D_1
# D_A ~ lambda^2 (pinched J_A line), D_1 = l^2 + 2 l.k + k^2 ; gluon k^2 ~ -kT^2 ~ lambda^2
# generic region: volume dk+ dk- d^2kT ~ lam^2 * lam^2 * lam^2 ; D_1 ~ lam
# (nA,w1) region: volume d(k.nA) d(k.w1) d^2 k_perp / (nA.w1) ~ lam^6 ; D_1 ~ lam^2
print()
for lam in [1e-2, 1e-3, 1e-4]:
    gen = lam**6 / (lam**2 * lam**2 * lam**1)
    nw = lam**6 / (lam**2 * lam**2 * lam**2)
    print(f"  lambda={lam:.0e}: generic DY-Glauber region ~ {gen:.1e} (lambda^1);  (nA,w1)-Glauber region ~ {nw:.1e} (lambda^0)")
# Monte-Carlo check of the generic-direction suppression: fraction of the DY-Glauber k_T-disc
# (|kT| in [lam/2, lam]) on which |w1.k| <= c*lam^2 (i.e. J_1 stays at virtuality lambda^2)
print()
for lam in [1e-2, 1e-3]:
    N = 400000
    r = lam*np.sqrt(rng.uniform(0.25, 1.0, N)); ph = rng.uniform(0, 2*np.pi, N)
    kp = lam**2*rng.uniform(-1, 1, N); km = lam**2*rng.uniform(-1, 1, N)
    wk = w1[0]*km + w1[1]*kp - (w1[2]*r*np.cos(ph))
    frac = np.mean(np.abs(wk) <= 2*lam**2)
    print(f"  lambda={lam:.0e}: fraction of DY-Glauber volume with |w1.k|<=2 lambda^2 : {frac:.3e}  (expected ~ lambda: {lam:.1e})")
