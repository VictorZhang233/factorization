"""X2/T14: two-loop planar vertex remainder: norm with the relative azimuth phi(k1T,k2T) in the FIBER,
i.e. int |int dphi rho_r| over (k2^+, K^+, |k1T|, |k2T|) -- expected second order (linear terms in k1T.k2T cancel)."""
import sys, os, json, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, warnings
from scipy.stats import qmc
import twoloop_dens as T
warnings.filterwarnings('ignore')
pats = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'twoloop_patterns.json')))
TERMS = [(c, {T.LINES[i]: set(p[i]) for i in range(6)}) for p, c in pats['r']]
NPHI = 32
# phi in (0, 2pi): use symmetric GL on (0, pi) and double (rho depends on cos phi only)
gn, gw = np.polynomial.legendre.leggauss(NPHI)
PH = 0.5*np.pi*(gn + 1); PW = 0.5*np.pi*gw*2.0
def pmap(u, lo, kind, rng):
    if kind == 'neg': return lo*(1 - u), -lo*np.ones_like(u)
    s = rng[0] + (rng[1] - rng[0])*u; x = np.exp(s); return x, x*(rng[1] - rng[0])
def run(m2, nlog2=15, nrep=4):
    kin = T.Kin(1/np.sqrt(2), 1/np.sqrt(2), m2)
    Lm = np.log(m2); RP = (2*Lm - 4.0, 4.0); lT = (1.5*Lm - 4.0, 3.0)
    res = {'avg': [], 'full': [], 'signed': []}
    for rep in range(nrep):
        A = F = S = 0.0
        for k2kind in ['neg', 'pos']:
            for Kkind in ['neg', 'pos']:
                U = qmc.Sobol(d=4, scramble=True, seed=31 + 911*rep + 3*(k2kind == 'pos') + 5*(Kkind == 'pos')).random_base2(nlog2)
                k2p, j2 = pmap(U[:, 0], -kin.p2p, k2kind, RP); Kp, jK = pmap(U[:, 1], -kin.p2p, Kkind, RP)
                l1 = lT[0] + (lT[1] - lT[0])*U[:, 2]; l2 = lT[0] + (lT[1] - lT[0])*U[:, 3]
                k1T = np.exp(l1); k2T = np.exp(l2); k1p = Kp - k2p
                acc = 0.0; accabs = 0.0
                for ph, w in zip(PH, PW):
                    val = 0.0
                    for c, pat in TERMS:
                        val = val + c*T.density(pat, kin, k1p, k2p, k1T, k2T, np.cos(ph)*np.ones_like(k1T))
                    val = np.nan_to_num(val, nan=0.0, posinf=0.0, neginf=0.0)
                    acc = acc + w*val; accabs = accabs + w*np.abs(val)
                jac = j2*jK*(2*np.pi)*k1T**2*k2T**2*(lT[1] - lT[0])**2
                A += np.mean(np.abs(acc)*jac); F += np.mean(accabs*jac); S += np.mean(acc*jac)
        res['avg'].append(A); res['full'].append(F); res['signed'].append(S)
    return {k: (np.mean(v), np.std(v)/np.sqrt(len(v))) for k, v in res.items()}
if __name__ == "__main__":
    for m2 in [4e-2, 1e-2, 2.5e-3, 6.25e-4]:
        t0 = time.time(); o = run(m2); L = np.log(1/m2); lam = np.sqrt(m2)
        print(f"m2={m2:.3e}: signed {o['signed'][0]:+.4e}+-{o['signed'][1]:.1e} ({o['signed'][0]/(m2*L**3):+.3f} m2 L^3); "
              f"full {o['full'][0]:.4e} ({o['full'][0]/(lam*L):.3f} lam L); "
              f"phi-averaged {o['avg'][0]:.4e}+-{o['avg'][1]:.1e} ({o['avg'][0]/m2:.2f} m2, {o['avg'][0]/(m2*L**3):.4f} m2 L^3, {o['avg'][0]/(m2*L**4):.5f} m2 L^4) [{time.time()-t0:.0f}s]", flush=True)
