import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import twoexch_model as T
mp.mp.dps = 20
import itertools
lam = float(sys.argv[1]); er = float(sys.argv[2])
sc = lambda v: (lam*v[0], lam*v[1])
k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9))
pa = T.jet_params(lam, 0.9*lam, 0.5*lam, 0.7*lam, 0.4, sc((0.3, 0.2)), k1T, k2T)
k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
pb = T.jet_params(lam, 0.8*lam, 0.6*lam, 0.5*lam, 0.55, sc((-0.25, 0.4)), k1Tm, k2Tm)
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
eta = er*lam**2
t0 = time.time()
res = {}
for cA, cB in itertools.product(('12','21'), repeat=2):
    res[(cA, cB)] = T.Ival(pa, pb, a1, a2, eta, cA, cB)
N = sum(res.values())
N0 = (T.I/pa['d0'])*(T.I/pb['d0'])/(a1*a2)
popp = (res[('12','21')] + res[('21','12')])/N
print(f"lam={lam} eta/lam^2={er}  N/N0={mp.nstr(N/N0,10)}  p_opp={mp.nstr(popp,10)}  W12,12={mp.nstr(res[('12','12')]/N,8)} W21,21={mp.nstr(res[('21','21')]/N,8)}  [{time.time()-t0:.0f}s]", flush=True)
