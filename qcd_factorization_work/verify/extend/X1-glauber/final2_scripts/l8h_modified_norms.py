# X1 final2 -- correction of L8(h) (the pi/4 contour).  On p = -e^{i pi/4} kappa a gap factor satisfies
#   |A - e^{i pi/4} y| >= max(|A|, |y|)/sqrt2,
# so each EXTRA state of a multi-state gap costs sqrt2/mu instead of 1/mu.  The statement "(b)-(g) hold with every
# constant multiplied by 8" with the ORIGINAL norms M, Mflat therefore fails for many-state gaps; it holds with the
# sqrt2-weighted norms  M_{pi/4} = sum_t |c_t| (sqrt2/lambda)^{d_t},  Mflat_{pi/4} = sum_t |c_t| (sqrt2/mu)^{d_t}.
# (1) explicit counterexample to the original-norm statement (b) x 8;
# (2) random factorized jets (class (SEC)+(EQ)+(ADJ), all final energies negative) with up to 6-state gaps, including
#     adversarial gaps with all energies equal to -mu, at theta = pi/4: (b) with 4 Mflat_{pi/4}, (c), (d), (e) with the
#     constants x 8 and the modified norms.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(31415)
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
ph = np.exp(1j*np.pi/4)
br = lambda y, mu: np.sqrt(mu**2 + y**2)
ok_all = True
# (1) counterexample: one term, first gap with n states all at A = -mu, second gap single state at A = -lambda
mu, lam = 0.1, 1.0
log("(1) counterexample to L8(h)(b) with the original norm: term c * prod_{j<=n} i/(A_j+p1) * i/(A'-p2) (sector BF),")
log("    A_j = -mu, at kappa1 = -mu/sqrt2 (where |A - e^{i pi/4} kappa1| = mu/sqrt2), kappa2 = 3")
for n in (2, 3, 4, 5, 6, 8):
    k1, k2 = -mu/np.sqrt(2), 3.0
    p1, p2 = -ph*k1, -ph*k2
    val = abs(np.prod([1j/(-mu + p1)]*n)*(1j/(-lam - p2)))
    Mf = mu**(-(n - 1)); Mf4 = (np.sqrt(2)/mu)**(n - 1)
    bnd_orig = 8*Mf/(br(k1, mu)*br(k2, mu)); bnd_mod = 4*Mf4/(br(k1, mu)*br(k2, mu))
    log(f"    n = {n}: |J| / (8 Mflat/<y1><y2>) = {val/bnd_orig:.3f}   |J| / (4 Mflat_pi4/<y1><y2>) = {val/bnd_mod:.3f}")
    if n >= 6:
        ok_all &= val/bnd_orig > 1      # the original statement fails
    ok_all &= val/bnd_mod <= 1
# (2) random jets
def make_jet(mu, lam=1.0, nmax=6, adversarial=False):
    jet = {}
    for S in ('1', '2', '12', 'V', '1V', '2V'):
        terms = []
        ns = int(rng.integers(1, 3))
        bs = rng.normal(size=ns); bs = bs/np.sum(bs) if abs(np.sum(bs)) > 0.3 else np.ones(ns)/ns
        for b in bs:
            terms.append((complex(b), [-rng.uniform(mu, lam)]))
        for m in range(int(rng.integers(0, 3))):
            n = int(rng.integers(2, nmax + 1))
            b = complex(rng.normal(), rng.normal())*lam**(n - 1)*0.5
            As = [-mu]*n if (adversarial and rng.uniform() < 0.5) else list(-rng.uniform(mu, lam, size=n))
            terms.append((b, As))
        jet[S] = terms
    jet['1'][0][1][0] = -mu; jet['V'][0][1][0] = -lam
    jet['c'] = complex(rng.normal(), rng.normal())
    return jet
def Phi(jet, S, K):
    fin = 'V' in S
    outv = 0
    for (b, As) in jet[S]:
        t = b
        for A in As:
            t = t*(1j/(A - K) if fin else 1j/(A + K))
        outv = outv + t
    return outv
def gapnorm(jet, S, scale):
    return sum(abs(b)*scale**(-(len(As) - 1)) for (b, As) in jet[S])
def consts(jet, lam, mu):
    c = abs(jet['c'])
    pairs = [('1', '12'), ('1', '1V'), ('V', '1V'), ('2', '12'), ('2', '2V'), ('V', '2V')]
    Ml = Mf = Ml4 = Mf4 = 0
    for (S1, S2) in pairs:
        Ml = max(Ml, c*gapnorm(jet, S1, lam)*gapnorm(jet, S2, lam))
        Mf = max(Mf, c*gapnorm(jet, S1, mu)*gapnorm(jet, S2, mu))
        Ml4 = max(Ml4, c*gapnorm(jet, S1, lam/np.sqrt(2))*gapnorm(jet, S2, lam/np.sqrt(2)))
        Mf4 = max(Mf4, c*gapnorm(jet, S1, mu/np.sqrt(2))*gapnorm(jet, S2, mu/np.sqrt(2)))
    return Ml, Mf, Ml4, Mf4
for adv in (False, True):
    worst = dict(b=0, c=0, d=0, e=0); worst_orig_b = 0
    for trial in range(400):
        mu = 10**rng.uniform(-2.5, -0.3); lam = 1.0
        jet = make_jet(mu, lam, adversarial=adv)
        Ml, Mf, Ml4, Mf4 = consts(jet, lam, mu)
        c = jet['c']
        for pt in range(300):
            R = 10**rng.uniform(np.log10(4*lam), 4)
            region = rng.integers(0, 5); sgn = rng.choice([-1, 1], size=2)
            if region == 0:
                k1 = sgn[0]*R; k2 = sgn[1]*R*rng.uniform(0.25, 1)
            elif region == 1:
                k2 = sgn[1]*R; k1 = sgn[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
            elif region == 2:
                k1 = sgn[0]*R; k2 = sgn[1]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4))
            elif region == 3:
                k2 = sgn[1]*R*rng.uniform(0.8, 1.0); kP = sgn[0]*10**rng.uniform(np.log10(mu) - 2, np.log10(R/4.5)); k1 = kP - k2
            else:   # adversarial points kappa ~ -A/sqrt2 for the (b) check
                k1 = -mu/np.sqrt(2)*rng.choice([1, -1])*rng.uniform(0.5, 2); k2 = sgn[1]*10**rng.uniform(-3, 3)
            Rr = max(abs(k1), abs(k2)); kP = k1 + k2
            p1, p2 = -ph*k1, -ph*k2; P = p1 + p2
            s12 = dict(BB=c*Phi(jet, '1', p1)*Phi(jet, '12', P), BF=c*Phi(jet, '1', p1)*Phi(jet, '1V', p2), FF=c*Phi(jet, 'V', P)*Phi(jet, '1V', p2))
            s21 = dict(BB=c*Phi(jet, '2', p2)*Phi(jet, '12', P), BF=c*Phi(jet, '2', p2)*Phi(jet, '2V', p1), FF=c*Phi(jet, 'V', P)*Phi(jet, '2V', p1))
            g12 = dict(BB=(k1, kP), BF=(k1, k2), FF=(kP, k2)); g21 = dict(BB=(k2, kP), BF=(k2, k1), FF=(kP, k1))
            for (sd, gp) in ((s12, g12), (s21, g21)):
                for key in sd:
                    den = br(gp[key][0], mu)*br(gp[key][1], mu)
                    worst['b'] = max(worst['b'], abs(sd[key])/(4*Mf4/den))
                    worst_orig_b = max(worst_orig_b, abs(sd[key])/(8*Mf/den))
            if Rr < 4*lam or region == 4:
                continue
            f12 = sum(s12.values()); f21 = sum(s21.values())
            if abs(kP) >= Rr/4:
                bnd = 8*400*Mf4*lam/(Rr**2*br(min(abs(k1), abs(k2)), mu))
                worst['c'] = max(worst['c'], abs(f12)/bnd, abs(f21)/bnd)
            else:
                g = c*(Phi(jet, '12', P) + Phi(jet, 'V', P))
                E12 = f12 - g/(1j*p2); E21 = f21 + g/(1j*p2)
                bnd = 8*16*Mf4*lam/(Rr**2*br(kP, mu))
                worst['d'] = max(worst['d'], abs(E12)/bnd, abs(E21)/bnd)
        for U in 10**rng.uniform(np.log10(mu) - 2, 4, size=200)*rng.choice([-1, 1], size=200):
            gv = c*(Phi(jet, '12', -ph*U) + Phi(jet, 'V', -ph*U))
            b1 = 8*2*Mf4/br(U, mu); b2 = (8*4*Ml4*lam/U**2) if abs(U) >= lam else np.inf
            worst['e'] = max(worst['e'], abs(gv)/min(b1, b2))
    lab = 'adversarial (half the multi-state gaps at A = -mu)' if adv else 'random energies'
    log(f"(2) theta = pi/4, gaps with up to 6 states, {lab}: max ratios with the sqrt2-weighted norms:"
        f" (b)[4 Mflat_pi4] {worst['b']:.3f}  (c)[x8] {worst['c']:.4f}  (d)[x8] {worst['d']:.4f}  (e)[x8] {worst['e']:.3f};"
        f"   (b) with the ORIGINAL norm x8: {worst_orig_b:.3f}")
    ok_all &= all(vv <= 1 for vv in worst.values())
log("ALL PASS" if ok_all else "SOME CHECK FAILED")
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'final2_logs', 'l8h_modified_norms.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
