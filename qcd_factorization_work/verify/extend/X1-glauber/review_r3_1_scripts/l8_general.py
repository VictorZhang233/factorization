# X1 review round 3, reviewer 1 -- Lemma L8 tested on GENERAL (Sp')-class jets (genjet.py): several hexagon orbits,
# winding cycles, two-chains with multi-state shared gaps, isolated multi-multi terms.  The fix-round-2 check
# (l8_bounds.py) used only factorized jets (gap functions depending on the set of performed operations).
# Tested (theta = pi/2, constants as stated; theta = pi/4, constants x8 as stated in L8(h)):
#   (b) |J^(sigma)| <= Mflat/(<y1><y2>)   [theta=pi/4: 4 Mflat/(<y1><y2>)]
#   (c) off-strip R >= 4 lam, r_P >= R/4:  |f_pi| <= 400 Mflat lam/(R^2 <min(r1,r2)>)
#   (d) strip R >= 4 lam, r_P < R/4:  |f_12 - g/(i p2)|, |f_21 + g/(i p2)| <= 16 Mflat lam/(R^2 <r_P>);  g^[12] = g^[21]
#   (e) |g(-iU)| <= min(2 Mflat/<U>, 4 M lam/U^2) (second only for |U| >= lam);  int g(-iU) dU/(2pi) = -i Jcal
#   (f) int S d^2kappa/(2pi)^2 = -Jcal
# plus the structural (Sp') check and the counter-test: the same bounds for a jet that violates (Sp').
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from genjet import random_general_jet, check_spprime, SECTORS, GAPMOM, Jet

rng = np.random.default_rng(20261011)
br = lambda y, mu: np.sqrt(mu**2 + y**2)


def gaps(s, k1, k2):
    kP = k1 + k2
    m = dict(p1=k1, p2=k2, P=kP)
    a, b = GAPMOM[s]
    return m[a], m[b]


def pointwise(jet, theta, fac, npts=600):
    lam, mu = jet.lam_mu(); M, Mf = jet.norms()
    ph = np.exp(1j*theta)
    worst = dict(b=0.0, c=0.0, d=0.0, e=0.0, gsym=0.0)
    for pt in range(npts):
        R = 10**rng.uniform(np.log10(4*lam), 4)
        region = rng.integers(0, 6)
        s = rng.choice([-1, 1], size=2)
        if region == 0:
            k1 = s[0]*R; k2 = s[1]*R*rng.uniform(0.25, 1)
        elif region == 1:
            k2 = s[1]*R; k1 = s[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
        elif region == 2:
            k1 = s[0]*R; k2 = s[1]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
        elif region == 3:   # strip interior
            k2 = s[1]*R*rng.uniform(0.75, 1.0); kP = s[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4.2)); k1 = kP - k2
        elif region == 4:   # strip boundary r_P ~ R/4 (both sides)
            k2 = s[1]*R; kP = s[0]*R/4*rng.uniform(0.9, 1.1); k1 = kP - k2
        else:               # axis-band boundary r_1 ~ R/4
            k2 = s[1]*R; k1 = s[0]*R/4*rng.uniform(0.9, 1.1)
        Rr = max(abs(k1), abs(k2))
        if Rr < 4*lam:
            continue
        kP = k1 + k2
        p1 = -ph*k1; p2 = -ph*k2
        for sct in SECTORS:
            y1, y2 = gaps(sct, k1, k2)
            bnd = (Mf if theta == np.pi/2 else 4*Mf)/(br(y1, mu)*br(y2, mu))
            worst['b'] = max(worst['b'], abs(jet.sector(sct, p1, p2))/bnd)
        f12 = jet.colour('12', p1, p2); f21 = jet.colour('21', p1, p2)
        if abs(kP) >= Rr/4:
            bnd = fac*400*Mf*lam/(Rr**2*br(min(abs(k1), abs(k2)), mu))
            worst['c'] = max(worst['c'], abs(f12)/bnd, abs(f21)/bnd)
        else:
            P = p1 + p2
            g = jet.g(P); g2 = jet.g21(P)
            worst['gsym'] = max(worst['gsym'], abs(g - g2)/max(abs(g), 1e-300))
            E12 = f12 - g/(1j*p2); E21 = f21 + g/(1j*p2)
            bnd = fac*16*Mf*lam/(Rr**2*br(kP, mu))
            worst['d'] = max(worst['d'], abs(E12)/bnd, abs(E21)/bnd)
    for U in 10**rng.uniform(np.log10(mu) - 2, 4, size=300)*rng.choice([-1, 1], size=300):
        gv = jet.g(-ph*U)
        b1 = fac*2*Mf/br(U, mu); b2 = (fac*4*M*lam/U**2) if abs(U) >= lam else np.inf
        worst['e'] = max(worst['e'], abs(gv)/min(b1, b2))
    return worst


def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w


def integrals(jet):
    lam, mu = jet.lam_mu()
    Jc = jet.Jcal('BB')
    # int g(-iU) dU/(2 pi)
    t, w = gl(6000, np.log(mu) - 14, np.log(1e10))
    U = np.exp(t)
    val_g = (np.sum(w*U*jet.g(-1j*U)) + np.sum(w*U*jet.g(1j*U)))/(2*np.pi)
    # int S d^2kappa/(2pi)^2 at theta = pi/2; diagonal quadrants: log-log grid; off-diagonal: (v, U = k1 + k2) grid
    S = lambda k1, k2: jet.colour('12', -1j*k1, -1j*k2) + jet.colour('21', -1j*k1, -1j*k2)
    tot = 0.0
    td, wd = gl(500, np.log(mu) - 10, np.log(1e6))
    T1, T2 = np.meshgrid(td, td, indexing='ij'); W2 = np.outer(wd, wd)
    for q in ((1, 1), (-1, -1)):
        tot += np.sum(W2*np.exp(T1 + T2)*S(q[0]*np.exp(T1), q[1]*np.exp(T2)))
    tv, wv = gl(500, np.log(mu) - 10, np.log(1e6))
    sg, wsg = gl(500, 0.0, np.log(1e6) - np.log(mu) + 18)
    tU, wU = gl(500, np.log(mu) - 18, np.log(1e6))
    for q in ((-1, 1), (1, -1)):
        TV, SG = np.meshgrid(tv, sg, indexing='ij'); v = np.exp(TV); Uu = v*np.exp(-SG); Wp = np.outer(wv, wsg)*v*Uu
        TV2, TAU = np.meshgrid(tv, tU, indexing='ij'); v2 = np.exp(TV2); U2 = -np.exp(TAU); Wm = np.outer(wv, wU)*v2*np.exp(TAU)
        for (vv, UU, WW) in ((v, Uu, Wp), (v2, U2, Wm)):
            if q == (-1, 1):
                k2 = vv; k1 = UU - vv
            else:
                k1 = vv; k2 = UU - vv
            tot += np.sum(WW*S(k1, k2))
    val_S = tot/(2*np.pi)**2
    return val_g/(-1j*Jc), val_S/(-Jc)


out = []
def log(s):
    print(s); out.append(s)

allok = True
for theta, fac in ((np.pi/2, 1.0), (np.pi/4, 8.0)):
    W = dict(b=0.0, c=0.0, d=0.0, e=0.0, gsym=0.0)
    nsp = 0
    for trial in range(120):
        mu = 10**rng.uniform(-3, -0.3)
        jet = random_general_jet(rng, mu, n_orbit=int(rng.integers(1, 4)), n_wind=int(rng.integers(0, 3)),
                                 n_chain=int(rng.integers(0, 7)), n_iso=int(rng.integers(0, 4)))
        if abs(jet.Jcal('BB')) < 0.05:
            continue
        assert check_spprime(jet)
        Jc = [jet.Jcal(s) for s in SECTORS]
        assert max(abs(np.array(Jc) - Jc[0])) < 1e-12
        nsp += 1
        w = pointwise(jet, theta, fac, npts=300)
        for k in W:
            W[k] = max(W[k], w[k])
    ok = all(W[k] <= 1 for k in ('b', 'c', 'd', 'e')) and W['gsym'] < 1e-10
    allok &= ok
    log(f"theta/pi={theta/np.pi:.2f} (constants x{fac:g}), {nsp} general (Sp') jets: max ratios (b) {W['b']:.3f}  "
        f"(c) {W['c']:.4f}  (d) {W['d']:.4f}  (e) {W['e']:.3f};  max |g12-g21|/|g| = {W['gsym']:.1e};  ok={ok}")

for trial in range(4):
    mu = 10**rng.uniform(-2, -0.7)
    jet = random_general_jet(rng, mu, n_orbit=2, n_wind=1, n_chain=4, n_iso=2)
    if abs(jet.Jcal('BB')) < 0.1:
        continue
    rg, rS = integrals(jet)
    ok = abs(rg - 1) < 1e-5 and abs(rS - 1) < 3e-3
    allok &= ok
    log(f"integrals, general jet {trial} (mu={mu:.3g}): int g(-iU)dU/2pi / (-i Jcal) = {rg:.8f};  int S d^2k/(2pi)^2 / (-Jcal) = {rS:.6f};  ok={ok}")

# Counter-test: break (Sp') (perturb the BF partner of one chain/orbit) and show that the strip structure fails,
# i.e. (Sp') is really needed for (d) as stated (g^[12] != g^[21] or E not small).
mu = 0.05
jet = random_general_jet(rng, mu, n_orbit=2, n_wind=0, n_chain=0, n_iso=0)
bad = Jet(); bad.terms = {s: list(v) for s, v in jet.terms.items()}
c, g1, g2 = bad.terms['FF'][0]
bad.terms['FF'][0] = (c, [g1[0]*0.5], g2)      # change the first-gap energy of one FF term only (breaks the FF<->FFp pairing)
print("counter-test jet satisfies (Sp')?", check_spprime(bad))
lam, mu_ = bad.lam_mu(); M, Mf = bad.norms()
worst = 0.0
for k2 in (50.0, 300.0, 3000.0):
    for kP in (0.01, 0.1, 1.0):
        k1 = kP - k2; p1 = 1j*(-k1); p2 = 1j*(-k2)
        p1 = -1j*k1; p2 = -1j*k2
        f12 = bad.colour('12', p1, p2); f21 = bad.colour('21', p1, p2)
        S = f12 + f21
        worst = max(worst, abs(S)*k2/(Mf))
log(f"counter-test (one FF energy changed, (Sp') violated): max |f12+f21| * kappa_2 / Mflat in the strip = {worst:.3e} "
    f"(would be O(lam/kappa_2) -> 0 under (Sp'); an O(1) value means the 1/kappa_2 strip tails no longer cancel in S)")
log("ALL PASS" if allok else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'review_r3_1_logs', 'l8_general.log'), 'w') as fh:
    fh.write("\n".join(out) + "\n")
