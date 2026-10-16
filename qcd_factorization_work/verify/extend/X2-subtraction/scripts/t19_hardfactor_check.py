"""X2/T19: check of Lemma 5.3 (hard factor): for a parent state (xi, v, K) with v >= |K|^2/(1-xi), child (z, l), k = l + zK,
child virtuality v' = z v + |l|^2/(1-z), hard denominator d = A(z xi) + v' + 2 k.q, A(y) = 1 - y/x, |q| = 1 (4D transverse):
 (i) d > 0 pointwise (convexity),  (ii) S^3-average over l-hat of 1/d <= 2/max(1-z, z xi (1-1/x))."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(5)
x = 1.3
worst_i = np.inf; worst_ii = 0.0
th = np.linspace(0, np.pi, 4001); wth = np.sin(th)**2; wth /= np.trapz(wth, th)
for _ in range(20000):
    xi = 10**rng.uniform(-6, 0); z = rng.uniform(0, 1); Kn = rng.uniform(0, 1)*np.sqrt(10**rng.uniform(-6, 1))
    v = Kn**2/(1 - xi)*(1 + 10**rng.uniform(-6, 1))          # satisfies v >= |K|^2/(1-xi)
    cK = rng.uniform(-1, 1)                                     # cos(K, q)
    l = 10**rng.uniform(-4, 1)
    vp = z*v + l**2/(1 - z)
    A = 1 - z*xi/x
    # need the child invariant: v' >= |k|^2/(1 - z xi) holds for chain states; restrict sample to it (worst case over sphere)
    dbar = A + vp + 2*z*Kn*cK
    dmin = dbar - 2*l
    kmax2 = (l + z*Kn)**2
    if vp < kmax2/(1 - z*xi):
        continue
    worst_i = min(worst_i, dmin)
    avg = np.trapz(wth/(dbar + 2*l*np.cos(th)), th)
    bound = 2/max(1 - z, z*xi*(1 - 1/x))
    worst_ii = max(worst_ii, avg/bound)
print("min pointwise denominator over samples (must be > 0):", worst_i)
print("max ratio <1/d>/bound (must be <= 1):", worst_ii)
