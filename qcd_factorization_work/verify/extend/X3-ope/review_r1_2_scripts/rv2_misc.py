import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(5)
# (1) Prop 5.6 step 9: |1 - x^2 w^2| >= (Im w)^2/|w|^2 for x in [0,1], Im w != 0
worst = np.inf
for _ in range(200000):
    w = complex(rng.normal() * rng.uniform(0.01, 50), rng.normal() * rng.uniform(1e-4, 50))
    x = rng.uniform(0, 1) if rng.uniform() < 0.5 else min(1.0, 1 / abs(w) * rng.uniform(0.9, 1.1))
    lhs = abs(1 - x * x * w * w)
    rhs = w.imag ** 2 / abs(w) ** 2
    worst = min(worst, lhs / rhs)
print("(1) min |1-x^2 w^2| / ((Im w)^2/|w|^2) over 2e5 samples =", worst)
# analytic: minimum over real t = x*|w|... check the critical case x = 1/|w| exactly
th = np.linspace(1e-4, np.pi - 1e-4, 20001)
ratio = np.abs(1 - np.exp(2j * th)) / np.sin(th) ** 2      # w = |w| e^{i th}, x = 1/|w|
print("    at x = 1/|w|: min ratio =", ratio.min())
# (2) slice inequality exact identity  w2^2 - s2^2 = 2 w2^2 Q^2/(B + sqrt(A^2+4 w1^2 w2^2))
err = 0
for _ in range(20000):
    Q = rng.uniform(0.1, 10); w = complex(rng.normal() * 5, abs(rng.normal()) * 5 + 1e-6)
    s = np.sqrt(w * w + Q * Q); s = s if s.real > 0 else -s
    A = w.real ** 2 - w.imag ** 2 + Q * Q; B = abs(w) ** 2 + Q * Q
    lhs = w.imag ** 2 - s.imag ** 2
    rhs = 2 * w.imag ** 2 * Q * Q / (B + np.sqrt(A * A + 4 * w.real ** 2 * w.imag ** 2))
    err = max(err, abs(lhs - rhs) / max(1e-300, abs(rhs)))
print("(2) reviewer's closed form for (Im w)^2-(Im s)^2: max rel. error =", err)
