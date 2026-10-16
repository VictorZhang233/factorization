# Independent check of the ray identity L6:  Int_0^inf dk/k Im rho(i k) = -pi/2 - pi * sum_p Res_{k_p} rho / k_p
# for rho holomorphic in the first quadrant, rho(0)=1, rho -> 0 at infinity, real on the positive axis except
# simple poles there (boundary value rho(k+i0)).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
rng = __import__('random'); rng.seed(7)
def make_rho():
    nneg = rng.randint(1, 3); npos = rng.randint(0, 2)
    bs = [mp.mpf(rng.uniform(0.2, 5)) for _ in range(nneg)]        # poles at -b (outside quadrant)
    cs = [mp.mpf(rng.uniform(0.3, 4)) for _ in range(npos)]        # poles at +c (on positive axis)
    # rho = prod 1/(1+k/b) * prod 1/(1-k/c) * (1 + e k) with small polynomial factor keeping decay
    e = mp.mpf(rng.uniform(-0.5, 0.5)) if (nneg + npos) >= 2 else 0
    def rho(k):
        v = (1 + e*k)
        for b in bs: v /= (1 + k/b)
        for c in cs: v /= (1 - k/c)
        return v
    # residues at k = c
    res = []
    for c in cs:
        v = (1 + e*c)
        for b in bs: v /= (1 + c/b)
        for c2 in cs:
            if c2 != c: v /= (1 - c/c2)
        res.append((c, v*(-c)))      # 1/(1-k/c) = -c/(k-c)
    return rho, res, bs, cs, e
for trial in range(8):
    rho, res, bs, cs, e = make_rho()
    if len(bs) + len(cs) < 2 and e != 0: continue
    lhs = mp.quad(lambda t: mp.im(rho(1j*mp.e**t)), [-40, -5, 0, 5, 40])
    rhs = -mp.pi/2 - mp.pi*sum(r/c for (c, r) in res)
    print(f"trial {trial}: neg poles {len(bs)}, axis poles {len(cs)}, e={float(e):+.2f}:  lhs = {mp.nstr(lhs, 15)}   rhs = {mp.nstr(rhs, 15)}   diff = {mp.nstr(lhs-rhs, 3)}")
