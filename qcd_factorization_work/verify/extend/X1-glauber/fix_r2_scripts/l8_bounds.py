# X1 fix round 2 -- numerical check of Lemma L8 (two-insertion jets on the rotated contour).
# Random jets of class (J) with N = 2 in the "factorized" form (gap functions depend only on the set of
# operations already performed), which satisfies (Sp) and the adjacent-pair hypothesis (Sp'):
#   Phi_S(K) = sum_j b_{S,j} prod_{i<=n_j} i/(A_{S,j,i} + K)   (S in {1,2,12}: initial gaps)
#   Phi_S(K) = sum_j b_{S,j} prod_{i<=n_j} i/(A'_{S,j,i} - K)  (S in {V,1V,2V}: final gaps, A' < 0 = NF)
#   sum_{j: n_j = 1} b_{S,j} = 1   (so every Jcal_sigma = c, i.e. (Sp)).
#   [12]: BB = c Phi_1(p1) Phi_12(P), BF = c Phi_1(p1) Phi_1V(p2), FF = c Phi_V(P) Phi_1V(p2)
#   [21]: BB = c Phi_2(p2) Phi_12(P), BF = c Phi_2(p2) Phi_2V(p1), FF = c Phi_V(P) Phi_2V(p1)
# Rotated contour: k^+ = e^{i theta} kappa, p = -k^+.  theta = pi/2 (main) and pi/4 (used in T3(e)).
# Claims (theta = pi/2), lambda = max|A|, mu = min|A|, <y> = sqrt(mu^2 + y^2), R = max(|k1|,|k2|):
#  (b) |J^(sigma)| <= Mflat_sigma/(<y1><y2>)
#  (c) off-strip (R >= 4 lambda, |kP| >= R/4): |f_pi| <= C_O Mflat lambda/(R^2 <min(|k1|,|k2|)>),  C_O = 400
#  (d) strip (R >= 4 lambda, |kP| < R/4): |f_12 - g/(i p2)|, |f_21 + g/(i p2)| <= C_S Mflat lambda/(R^2 <kP>),  C_S = 16
#  (e) |g(-iU)| <= min(2 Mflat/<U>, 4 M lambda/U^2);  int g(-iU) dU/(2 pi) = -i Jcal
#  (f) int S d^2kappa/(2pi)^2 = -Jcal        (g) integrated bounds
# theta = pi/4: same with every gap factor bound 2/<y> etc.; constants multiplied by 8 (claimed).
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(1234567)

def make_jet(mu, lam=1.0, nmulti=2):
    jet = {}
    for S in ('1', '2', '12', 'V', '1V', '2V'):
        terms = []
        ns = int(rng.integers(1, 3))                 # number of single-state terms
        bs = rng.normal(size=ns); bs = bs/np.sum(bs) if abs(np.sum(bs)) > 0.3 else np.ones(ns)/ns
        for b in bs:
            terms.append((complex(b), [-rng.uniform(mu, lam)]))
        for m in range(int(rng.integers(0, nmulti + 1))):
            n = int(rng.integers(2, 4))
            b = complex(rng.normal(), rng.normal())*lam**(n - 1)*0.5
            terms.append((b, list(-rng.uniform(mu, lam, size=n))))
        # force exact min/max present somewhere
        jet[S] = terms
    jet['1'][0][1][0] = -mu; jet['V'][0][1][0] = -lam
    jet['c'] = complex(rng.normal(), rng.normal())
    return jet

def Phi(jet, S, K):
    fin = 'V' in S
    out = 0
    for (b, As) in jet[S]:
        t = b
        for A in As:
            t = t*(1j/(A - K) if fin else 1j/(A + K))
        out = out + t
    return out

def norms(jet, S, lam, mu):
    Ml = sum(abs(b)*lam**(-(len(As) - 1)) for (b, As) in jet[S])
    Mf = sum(abs(b)*mu**(-(len(As) - 1)) for (b, As) in jet[S])
    return Ml, Mf

def sectors(jet, p1, p2):
    P = p1 + p2; c = jet['c']
    s12 = dict(BB=c*Phi(jet, '1', p1)*Phi(jet, '12', P), BF=c*Phi(jet, '1', p1)*Phi(jet, '1V', p2), FF=c*Phi(jet, 'V', P)*Phi(jet, '1V', p2))
    s21 = dict(BB=c*Phi(jet, '2', p2)*Phi(jet, '12', P), BF=c*Phi(jet, '2', p2)*Phi(jet, '2V', p1), FF=c*Phi(jet, 'V', P)*Phi(jet, '2V', p1))
    return s12, s21

def gfun(jet, P):
    return jet['c']*(Phi(jet, '12', P) + Phi(jet, 'V', P))

def jet_consts(jet, lam, mu):
    c = abs(jet['c'])
    pairs = {'12': [('1', '12'), ('1', '1V'), ('V', '1V')], '21': [('2', '12'), ('2', '2V'), ('V', '2V')]}
    Ml = 0; Mf = 0
    for col in pairs:
        for (S1, S2) in pairs[col]:
            a1, b1 = norms(jet, S1, lam, mu); a2, b2 = norms(jet, S2, lam, mu)
            Ml = max(Ml, c*a1*a2); Mf = max(Mf, c*b1*b2)
    return Ml, Mf

def bracket(y, mu):
    return np.sqrt(mu**2 + y**2)

worst = dict(b=0, c=0, d=0, e1=0, e2=0)
allok = True
for theta, fac in ((np.pi/2, 1.0), (np.pi/4, 8.0)):
    worst = dict(b=0, c=0, d=0, e1=0, e2=0)
    ph = np.exp(1j*theta)
    for trial in range(300):
        mu = 10**rng.uniform(-3, -0.2); lam = 1.0
        jet = make_jet(mu, lam)
        Ml, Mf = jet_consts(jet, lam, mu)
        for pt in range(400):
            R = 10**rng.uniform(np.log10(4*lam), 4)
            region = rng.integers(0, 4)
            sgn = rng.choice([-1, 1], size=2)
            if region == 0:     # generic
                k1 = sgn[0]*R; k2 = sgn[1]*R*rng.uniform(0.25, 1)
            elif region == 1:   # near axis k1 ~ 0
                k2 = sgn[1]*R; k1 = sgn[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
            elif region == 2:   # near axis k2 ~ 0
                k1 = sgn[0]*R; k2 = sgn[1]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
            else:               # strip
                k2 = sgn[1]*R*rng.uniform(0.8, 1.0); kP = sgn[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4.5)); k1 = kP - k2
            if max(abs(k1), abs(k2)) < 4*lam: continue
            Rr = max(abs(k1), abs(k2)); kP = k1 + k2
            p1 = -ph*k1; p2 = -ph*k2; P = p1 + p2
            s12, s21 = sectors(jet, p1, p2)
            # (b)
            gaps12 = dict(BB=(k1, kP), BF=(k1, k2), FF=(kP, k2)); gaps21 = dict(BB=(k2, kP), BF=(k2, k1), FF=(kP, k1))
            for (s, gp) in ((s12, gaps12), (s21, gaps21)):
                for key in s:
                    bnd = fac/8*4*Mf/(bracket(gp[key][0], mu)*bracket(gp[key][1], mu)) if theta != np.pi/2 else Mf/(bracket(gp[key][0], mu)*bracket(gp[key][1], mu))
                    worst['b'] = max(worst['b'], abs(s[key])/bnd)
            f12 = sum(s12.values()); f21 = sum(s21.values())
            if abs(kP) >= Rr/4:
                bnd = fac*400*Mf*lam/(Rr**2*bracket(min(abs(k1), abs(k2)), mu))
                worst['c'] = max(worst['c'], abs(f12)/bnd, abs(f21)/bnd)
            else:
                g = gfun(jet, P)
                E12 = f12 - g/(1j*p2); E21 = f21 + g/(1j*p2)
                bnd = fac*16*Mf*lam/(Rr**2*bracket(kP, mu))
                worst['d'] = max(worst['d'], abs(E12)/bnd, abs(E21)/bnd)
        # (e) pointwise g bound
        for U in 10**rng.uniform(np.log10(mu) - 2, 4, size=200)*rng.choice([-1, 1], size=200):
            gv = gfun(jet, -ph*U)
            b1 = fac*2*Mf/bracket(U, mu); b2 = (fac*4*Ml*lam/U**2) if abs(U) >= lam else np.inf
            worst['e1'] = max(worst['e1'], abs(gv)/min(b1, b2))
    print(f"theta/pi = {theta/np.pi:.2f} (constants x{fac:g}): max ratios  (b) {worst['b']:.3f}   (c) off-strip {worst['c']:.4f}   "
          f"(d) strip remainder {worst['d']:.4f}   (e) |g| {worst['e1']:.3f}")
    allok &= all(v <= 1 for v in worst.values())

# (e) integral of g and (f) integral of S, for a few jets (theta = pi/2), via quadrature
def gl(n, a, b):
    x, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*x + 0.5*(b + a), 0.5*(b - a)*w

for trial in range(3):
    mu = 10**rng.uniform(-2, -0.5); lam = 1.0
    jet = make_jet(mu, lam)
    Jcal = jet['c']
    # int g(-iU) dU/(2 pi): log grid both signs
    t, w = gl(8000, np.log(mu) - 14, np.log(1e10))
    U = np.exp(t)
    val = (np.sum(w*U*gfun(jet, -1j*U)) + np.sum(w*U*gfun(jet, 1j*U)))/(2*np.pi)
    okg = abs(val/(-1j*Jcal) - 1) < 1e-4
    # int S d^2 kappa/(2pi)^2 over R^2 at theta = pi/2: quadrant-wise, strip adapted (cf. fix_r1 regulator_indep.integrate)
    def Sfun(k1, k2):
        s12, s21 = sectors(jet, -1j*k1, -1j*k2)
        return sum(s12.values()) + sum(s21.values())
    tot = 0
    td, wd = gl(700, np.log(mu) - 10, np.log(1e6))
    T1, T2 = np.meshgrid(td, td, indexing='ij'); W2 = np.outer(wd, wd)
    for q in ((1, 1), (-1, -1)):
        tot += np.sum(W2*np.exp(T1 + T2)*Sfun(q[0]*np.exp(T1), q[1]*np.exp(T2)))
    tv, wv = gl(700, np.log(mu) - 10, np.log(1e6)); sg, wsg = gl(700, 0.0, np.log(1e6) - np.log(mu) + 18)
    tU, wU = gl(700, np.log(mu) - 18, np.log(1e6))
    for q in ((-1, 1), (1, -1)):
        TV, SG = np.meshgrid(tv, sg, indexing='ij'); v = np.exp(TV); Uu = v*np.exp(-SG); Wp = np.outer(wv, wsg)*v*Uu
        TV2, TAU = np.meshgrid(tv, tU, indexing='ij'); v2 = np.exp(TV2); U2 = -np.exp(TAU); Wm = np.outer(wv, wU)*v2*np.exp(TAU)
        for (vv, UU, WW) in ((v, Uu, Wp), (v2, U2, Wm)):
            if q == (-1, 1): k2 = vv; k1 = UU - vv
            else: k1 = vv; k2 = UU - vv
            tot += np.sum(WW*Sfun(k1, k2))
    valS = tot/(2*np.pi)**2
    okS = abs(valS/(-Jcal) - 1) < 2e-3
    allok &= okg and okS
    print(f"jet {trial}: mu={mu:.3g}: int g(-iU) dU/(2pi) / (-i Jcal) = {val/(-1j*Jcal):.8f} (ok={okg});  "
          f"int S d^2k/(2pi)^2 / (-Jcal) = {valS/(-Jcal):.6f} (ok={okS})")

# (g) integrated bounds at theta = pi/2 for a few jets and K
def fvals(jet, k1, k2):
    s12, s21 = sectors(jet, -1j*k1, -1j*k2)
    return sum(s12.values()), sum(s21.values())
for trial in range(3):
    mu = 10**rng.uniform(-2, -0.5); lam = 1.0
    jet = make_jet(mu, lam); Ml, Mf = jet_consts(jet, lam, mu)
    for K in (8.0, 40.0, 200.0):
        # (g1) square R <= K: grid in (k1,k2) with sinh spacing to resolve small |y|
        s = np.linspace(-np.arcsinh(K/mu), np.arcsinh(K/mu), 1601); ks = mu*np.sinh(s); dk = mu*np.cosh(s)*(s[1]-s[0])
        K1, K2 = np.meshgrid(ks, ks, indexing='ij'); W = np.outer(dk, dk)
        f12, f21 = fvals(jet, K1, K2)
        g1 = max(np.sum(W*np.abs(f12)), np.sum(W*np.abs(f21)))
        b1 = 12*Mf*np.log(1 + 4*K/mu)**2
        # (g2) off-strip outer region and (g3) strip remainder: polar-like grid in (R, phi) is awkward; use (kP, k2) and (k1, k2) grids on R>K
        # off-strip: sample on a large box [-L, L]^2 minus square, with sinh grid
        L = 4e4
        s = np.linspace(-np.arcsinh(L/mu), np.arcsinh(L/mu), 2401); ks = mu*np.sinh(s); dk = mu*np.cosh(s)*(s[1]-s[0])
        K1, K2 = np.meshgrid(ks, ks, indexing='ij'); W = np.outer(dk, dk)
        Rm = np.maximum(np.abs(K1), np.abs(K2)); KP = K1 + K2
        f12, f21 = fvals(jet, K1, K2)
        mask_o = (Rm > K) & (np.abs(KP) >= Rm/4)
        g2 = max(np.sum(W[mask_o]*np.abs(f12[mask_o])), np.sum(W[mask_o]*np.abs(f21[mask_o])))
        b2 = 8*400*Mf*(lam/K)*(1 + np.log(1 + 2*K/mu))
        # strip remainder: grid in (kP, k2)
        sP = np.linspace(-np.arcsinh(L/mu), np.arcsinh(L/mu), 2401); kPs = mu*np.sinh(sP); dkP = mu*np.cosh(sP)*(sP[1]-sP[0])
        KPg, K2g = np.meshgrid(kPs, ks, indexing='ij'); Wg = np.outer(dkP, dk); K1g = KPg - K2g
        Rg = np.maximum(np.abs(K1g), np.abs(K2g)); mask_t = (Rg > K) & (np.abs(KPg) < Rg/4)
        f12, f21 = fvals(jet, K1g, K2g); g = gfun(jet, -1j*KPg); p2 = -1j*K2g
        E12 = f12 - g/(1j*p2); E21 = f21 + g/(1j*p2)
        g3 = max(np.sum(Wg[mask_t]*np.abs(E12[mask_t])), np.sum(Wg[mask_t]*np.abs(E21[mask_t])))
        b3 = (16/3)*16*Mf*(lam/K)*(1 + np.log(1 + K/(2*mu)))
        ok = (g1 <= b1) and (g2 <= b2) and (g3 <= b3); allok &= ok
        print(f"(g) jet {trial} mu={mu:.3g} K={K:g}: int_sq|f| = {g1:.4g} <= {b1:.4g};  int_off|f| = {g2:.4g} <= {b2:.4g};  int_strip|E| = {g3:.4g} <= {b3:.4g};  ok={ok}")
print("ALL PASS" if allok else "SOME CHECK FAILED")
