"""X2 fix round 1 / r1_twoloop_qmc.py -- re-run of the t12 QMC estimates with many more independent randomizations
(nrep = 16 independently scrambled Sobol sequences of 2^17 points per sub-box, base seed 1000, disjoint from t12's seeds),
so that the quoted errors (std over randomizations / sqrt(nrep)) are themselves reliable.  The exact values of
int Gamma (UD Phi^(2)) and of int r (= int Gamma - LP, see r1_twoloop_exact.py) are printed with the pulls."""
import sys, os, time, json
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
import t12_twoloop_remainder as T12
import twoloop_dens as T

def exact(m2):
    m2 = mp.mpf(m2); Lt = mp.log(1/m2)
    g = (1 + m2)*(12*mp.polylog(4, -m2) + Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60)/((1 - m2)*(1 + m2)**4)
    return float(g), float(g - (Lt**4/4 + mp.pi**2*Lt**2/2 + 7*mp.pi**4/60))

if __name__ == "__main__":
    nlog2 = int(sys.argv[1]) if len(sys.argv) > 1 else 17
    nrep = int(sys.argv[2]) if len(sys.argv) > 2 else 16
    P, Pp = 1/np.sqrt(2), 1/np.sqrt(2)
    for m2 in [4e-2, 1e-2, 2.5e-3, 6.25e-4]:
        kin = T.Kin(P, Pp, m2); t0 = time.time()
        Lm = np.log(m2)
        T12.RANGE_P = (2*Lm - 4.0, 4.0)
        lT = (1.5*Lm - 4.0, 3.0)
        g = T12.estimate(kin, [(1, {})], nlog2=nlog2, nrep=nrep, lT=lT, seed=1000)
        r = T12.estimate(kin, T12.TERMS, nlog2=nlog2, nrep=nrep, lT=lT, seed=1000)
        gx, rx = exact(m2)
        print(f"m2={m2:.3e}: int Gamma = {g['signed'][0]:.5e} +- {g['signed'][1]:.1e} (exact {gx:.5e}, pull {(g['signed'][0]-gx)/g['signed'][1]:+.2f}); "
              f"int r = {r['signed'][0]:+.4e} +- {r['signed'][1]:.1e} (exact {rx:+.4e}, pull {(r['signed'][0]-rx)/r['signed'][1]:+.2f}); "
              f"norm = {r['norm'][0]:.4e} +- {r['norm'][1]:.1e} ({r['norm'][0]/np.sqrt(m2)/np.log(1/m2):.3f} lam L)  [{time.time()-t0:.0f}s]", flush=True)
