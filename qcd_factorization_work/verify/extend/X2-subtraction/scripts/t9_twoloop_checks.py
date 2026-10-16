"""X2/T9: consistency checks of the two-loop fibered densities: (i) order independence (k1^- first vs k2^- first),
(ii) independence of the infinitesimal weights, (iii) support of rho_Gamma in (k1^+,k2^+)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, json
import twoloop_dens as T
from lcpt import iterated_residue
kin = T.Kin(0.8, 1.3, 0.02)
rng = np.random.default_rng(11)
N = 20000
k1p = rng.uniform(-0.05, 1.0, N); k2p = rng.uniform(-0.05, 1.0, N)
k1T = 10**rng.uniform(-3, 0.5, N); k2T = 10**rng.uniform(-3, 0.5, N); cph = np.cos(rng.uniform(0, 2*np.pi, N))
pats = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'twoloop_patterns.json')))
def dens_order(pattern, order, weights=None):
    if weights: T.WEIGHTS.update(weights)
    facs = [T.line_factor(l, set(pattern.get(l, ())), kin, k1p, k2p, k1T, k2T, cph) for l in T.LINES]
    return np.real(iterated_residue(facs, 2, order=order)/(1j*np.pi**2)**2)
Gam = {}
r01 = dens_order(Gam, [0, 1]); r10 = dens_order(Gam, [1, 0])
w0 = dict(T.WEIGHTS)
r01b = dens_order(Gam, [0, 1], {l: rng.uniform(0.5, 2) for l in T.LINES}); T.WEIGHTS.update(w0)
sc = np.max(np.abs(r01))
print("Gamma: order-independence max|diff|/max|rho| =", np.max(np.abs(r01 - r10))/sc, "; weight-independence:", np.max(np.abs(r01 - r01b))/sc)
# a few approximated patterns from the remainder
maxd = 0
for p, c in pats['r'][:50]:
    pat = {T.LINES[i]: set(p[i]) for i in range(6)}
    try:
        a = dens_order(pat, [0, 1]); b = dens_order(pat, [1, 0])
        d = np.max(np.abs(a - b))/max(np.max(np.abs(a)), 1e-300)
        maxd = max(maxd, d)
    except ValueError as e:
        print("pattern", p, "->", e)
print("50 remainder patterns: max order-dependence (relative) =", maxd)
nz = r01 != 0
print("support of rho_Gamma: k1p in [%.4f, %.4f], k2p in [%.4f, %.4f], k1p+k2p max %.4f; fraction nonzero %.3f" %
      (k1p[nz].min(), k1p[nz].max(), k2p[nz].min(), k2p[nz].max(), (k1p+k2p)[nz].max(), nz.mean()))
print("rho_Gamma sign: min %.3e max %.3e" % (r01.min(), r01.max()))
