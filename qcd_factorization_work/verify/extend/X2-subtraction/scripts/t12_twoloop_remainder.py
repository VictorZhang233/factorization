"""X2/T12: two-loop planar vertex: Collins remainder r = prod_R (1-T_R) Gamma (50 zeroing patterns, T8),
signed integral and integral norm over the fibered base, by randomized QMC; several m2.
Base: k2^+ in (-p2^+,0) U (0,inf) [log map], K^+ = k1^+ + k2^+ likewise, ln|k1T|, ln|k2T|, relative angle."""
import sys, os, json, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, warnings
from scipy.stats import qmc
import twoloop_dens as T
warnings.filterwarnings('ignore')
pats = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'twoloop_patterns.json')))
TERMS = [(c, {T.LINES[i]: set(p[i]) for i in range(6)}) for p, c in pats['r']]

def pmap(u, lo, kind, s_lo=-36.0, s_hi=8.0):
    s_lo, s_hi = RANGE_P
    if kind == 'neg':
        return lo*(1 - u), -lo*np.ones_like(u)
    s = s_lo + (s_hi - s_lo)*u
    x = np.exp(s); return x, x*(s_hi - s_lo)

RANGE_P = (-36.0, 8.0)
def estimate(kin, terms, nlog2=17, nrep=4, lT=(-24.0, 5.0), seed=0):
    out = {'signed': [], 'norm': []}
    for rep in range(nrep):
        S = 0.0; Nn = 0.0
        for k2kind in ['neg', 'pos']:
            for Kkind in ['neg', 'pos']:
                sob = qmc.Sobol(d=5, scramble=True, seed=seed + 977*rep + 3*(k2kind == 'pos') + 5*(Kkind == 'pos'))
                U = sob.random_base2(nlog2)
                k2p, j2 = pmap(U[:, 0], -kin.p2p, k2kind); Kp, jK = pmap(U[:, 1], -kin.p2p, Kkind)
                l1 = lT[0] + (lT[1] - lT[0])*U[:, 2]; l2 = lT[0] + (lT[1] - lT[0])*U[:, 3]; ph = 2*np.pi*U[:, 4]
                k1T = np.exp(l1); k2T = np.exp(l2); k1p = Kp - k2p
                val = 0.0
                for c, pat in terms:
                    val = val + c*T.density(pat, kin, k1p, k2p, k1T, k2T, np.cos(ph))
                val = np.nan_to_num(val, nan=0.0, posinf=0.0, neginf=0.0)
                jac = j2*jK*(2*np.pi)*k1T**2*k2T**2*(lT[1] - lT[0])**2*(2*np.pi)
                S += np.mean(val*jac); Nn += np.mean(np.abs(val)*jac)
        out['signed'].append(S); out['norm'].append(Nn)
    return {k: (np.mean(v), np.std(v)/np.sqrt(len(v))) for k, v in out.items()}

if __name__ == "__main__":
    nlog2 = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    P, Pp = 1/np.sqrt(2), 1/np.sqrt(2)     # Qt = 1
    for m2 in [4e-2, 1e-2, 2.5e-3, 6.25e-4]:
        kin = T.Kin(P, Pp, m2)
        t0 = time.time()
        Lm = np.log(m2)
        RANGE_P = (2*Lm - 4.0, 4.0)
        lT = (1.5*Lm - 4.0, 3.0)
        g = estimate(kin, [(1, {})], nlog2=nlog2, lT=lT)
        r = estimate(kin, TERMS, nlog2=nlog2, lT=lT)
        Q2 = (1 + m2)**2; t = m2/Q2
        lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
        ud = float(-(6/lam)*(mp.polylog(4, -1/(rho*t)) - mp.polylog(4, -rho*t)))/Q2**2
        L = np.log(1/m2)
        print(f"m2={m2:.3e}: int Gamma = {g['signed'][0]:.5e} +- {g['signed'][1]:.1e} (UD {ud:.5e}); "
              f"int r = {r['signed'][0]:+.4e} +- {r['signed'][1]:.1e} ({r['signed'][0]/m2:+.3f} m2, {r['signed'][0]/(m2*L*L):+.4f} m2 L^2); "
              f"norm = {r['norm'][0]:.4e} +- {r['norm'][1]:.1e} ({r['norm'][0]/m2:.3f} m2, {r['norm'][0]/(m2*L**3):.5f} m2 L^3, {r['norm'][0]/np.sqrt(m2):.4f} lam)"
              f"  [{time.time()-t0:.0f}s]", flush=True)
