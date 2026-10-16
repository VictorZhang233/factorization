# Reviewer-2: brute-force numerical test of Lemma L1(a) for N = 2 at FINITE eta (exactness claim),
# with an LCOPT-type jet containing single- and double-state gaps, and external poles in mixed half planes.
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
rng = np.random.default_rng(7)
eta = 0.35
# sector gap data: for each sector, list of initial gaps (each a list of A's: product of i/(A+K+i eta))
# and final gaps (list of A' : product of i/(A'-K+i eta)); coefficient c_t
def rnd(n): return list(rng.uniform(-2.0, 1.0, n))
sectors = {}
for order in ((0, 1), (1, 0)):
    for nb in range(3):
        B = order[:nb]; F = order[nb:]
        gapsB = [rnd(rng.integers(1, 3)) for _ in B]   # 1 or 2 states per gap
        gapsF = [rnd(rng.integers(1, 3)) for _ in F]
        sectors[(order, nb)] = (B, F, gapsB, gapsF, rng.uniform(0.5, 1.5))
def J_sector(key, k):
    B, F, gB, gF, c = sectors[key]
    val = c
    for l in range(len(B)):
        K = sum(k[e] for e in B[:l+1])
        for A in gB[l]: val = val*1j/(A + K + 1j*eta)
    for l in range(len(F)):
        K = sum(k[e] for e in F[l:])
        for A in gF[l]: val = val*1j/(A - K + 1j*eta)
    return val
def J_order(order, k):
    return sum(J_sector((order, nb), k) for nb in range(3))
def test(z, r):
    calF = [e for e in range(2) if z[e].imag < 0]; calB = [e for e in range(2) if z[e].imag > 0]
    # formula
    pref = np.prod([(-1j*r[e]) if e in calF else (1j*r[e]) for e in range(2)])
    out = {}
    for order in ((0, 1), (1, 0)):
        f = 0
        for nb in range(3):
            Bs = set(order[:nb])
            if Bs == set(calB): f += J_sector((order, nb), z)
        out[order] = pref*f
    # brute force on a mapped grid k = s*tan(pi x/2), x in (-1,1)
    n = 3000; x, w = np.polynomial.legendre.leggauss(n); s = 1.3
    kk = s*np.tan(np.pi*x/2); dk = s*(np.pi/2)/np.cos(np.pi*x/2)**2*w
    K1, K2 = np.meshgrid(kk, kk, indexing='ij'); W = np.outer(dk, dk)
    bf = {}
    for order in ((0, 1), (1, 0)):
        integrand = J_order(order, (K1, K2))*r[0]/(K1 - z[0])*r[1]/(K2 - z[1])
        bf[order] = np.sum(W*integrand)/(2*np.pi)**2
    return out, bf
for trial in range(4):
    z = [complex(rng.uniform(-2, 2), rng.choice([-1, 1])*rng.uniform(0.2, 1.0)) for _ in range(2)]
    r = [rng.uniform(0.3, 1.0), rng.uniform(-1.0, -0.3)]
    out, bf = test(z, r)
    for order in out:
        print(f"trial {trial} z={[f'{q:.2f}' for q in z]} order {order}: L1 = {out[order]:.8f}  brute = {bf[order]:.8f}  |diff| = {abs(out[order]-bf[order]):.2e}")
