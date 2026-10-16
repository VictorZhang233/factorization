"""X2/T10: two-loop planar vertex: int rho_Gamma (5D QMC over the fibered base) vs exact Usyukina-Davydychev
   I_2 = Phi^(2)(t,t)/Q^4,  Phi^(2)(t,t) = -(6/lam)[Li4(-1/(rho t)) - Li4(-rho t)],  t = m2/Q^2.
Base variables: k2^+ and K^+ = k1^+ + k2^+ (each split into the negative sliver (-p2^+,0) and (0,P) with a logistic map),
ln|k1T|, ln|k2T|, relative angle phi.  Measure dk1+ dk2+ d^2k1T d^2k2T = dK+ dk2+ (2pi) k1T dk1T k2T dk2T dphi."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp, warnings
from scipy.stats import qmc
import twoloop_dens as T
warnings.filterwarnings('ignore')

def UD2(t):
    t = mp.mpf(t); lam = mp.sqrt(1 - 4*t); rho = 2/(1 - 2*t + lam)
    return -(6/lam)*(mp.polylog(4, -1/(rho*t)) - mp.polylog(4, -rho*t))

def plus_map(u, lo, hi, kind):
    """map u in (0,1) to x and jacobian. kind 'neg': x in (lo,0) linear; 'pos': x in (0,hi) logistic in s in [-S1,S2]"""
    if kind == 'neg':
        x = lo*(1 - u); return x, -lo*np.ones_like(u)
    S1, S2 = 36.0, 28.0
    s = -S1 + (S1 + S2)*u
    sig = 1/(1 + np.exp(-s)); om = 1/(1 + np.exp(s))
    return hi*sig, hi*sig*om*(S1 + S2)

def integrate_pattern_sum(terms, kin, nlog2=20, lT=(-25.0, 6.0), seed=0, absval=False, nrep=4):
    """terms: list of (coeff, pattern dict). Returns estimate and std over randomized QMC replicas."""
    ests = []
    for rep in range(nrep):
        tot = 0.0
        for k2kind in ['neg', 'pos']:
            for Kkind in ['neg', 'pos']:
                sob = qmc.Sobol(d=5, scramble=True, seed=seed + 1000*rep + 7*(k2kind == 'pos') + 13*(Kkind == 'pos'))
                U = sob.random_base2(nlog2)
                k2p, j2 = plus_map(U[:, 0], -kin.p2p, kin.P, k2kind)
                Kp, jK = plus_map(U[:, 1], -kin.p2p, kin.P, Kkind)
                l1 = lT[0] + (lT[1] - lT[0])*U[:, 2]; l2 = lT[0] + (lT[1] - lT[0])*U[:, 3]
                ph = 2*np.pi*U[:, 4]
                k1T = np.exp(l1); k2T = np.exp(l2)
                k1p = Kp - k2p
                val = 0.0
                for c, pat in terms:
                    val = val + c*T.density(pat, kin, k1p, k2p, k1T, k2T, np.cos(ph))
                val = np.nan_to_num(val, nan=0.0, posinf=0.0, neginf=0.0)
                if absval: val = np.abs(val)
                jac = j2*jK*(2*np.pi)*k1T**2*k2T**2*(lT[1] - lT[0])**2*(2*np.pi)
                tot += np.mean(val*jac)
        ests.append(tot)
    ests = np.array(ests)
    return ests.mean(), ests.std()/np.sqrt(len(ests))

if __name__ == "__main__":
    for (P, Pp, m2) in [(0.8, 1.3, 0.02), (0.8, 1.3, 0.005)]:
        kin = T.Kin(P, Pp, m2)
        Qt2 = 2*P*Pp; Q2 = (Qt2 + m2)**2/Qt2; t = m2/Q2
        exact = float(UD2(t))/Q2**2
        est, err = integrate_pattern_sum([(1, {})], kin, nlog2=19)
        print(f"P={P} P'={Pp} m2={m2}: QMC int rho_Gamma = {est:.6e} +- {err:.1e}   UD exact = {exact:.6e}   rel diff {abs(est-exact)/exact:.2e}")
