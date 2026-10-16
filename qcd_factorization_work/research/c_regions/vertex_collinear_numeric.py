#!/usr/bin/env python3
"""
vertex_collinear_numeric.py -- the collinear pinch of the massless one-loop vertex in light-cone variables
(research/c_regions)

Massless vertex gamma*(q) -> q(p1) qbar(p2), lines  D0 = k^2, D1 = (p1-k)^2, D2 = (p2+k)^2  (all + i0),
p1 = (p1^+,0,0_T), p2 = (0,p2^-,0_T), Q^2 = 2 p1^+ p2^- (timelike).  Light-cone conventions of CONTEXT.md:
v^pm = (v^0 pm v^3)/sqrt2,  v.w = v^+ w^- + v^- w^+ - v_T.w_T.

Checks:
  C1  pole positions in k^- for 0<x=k^+/p1^+<1: D0 and D2 poles in the lower half plane, D1 pole in the upper
      half plane; as k_T -> 0 the D0 and D1 poles pinch k^-=0 from opposite sides (collinear pinch)
  C2  outside 0<x<1 all poles lie on one side -> k^- integral vanishes (support property)
  C3  J(x,k_T) = int dk^- 1/(D0 D1 D2) = (2 pi i/(2 p1^+)) / [k_T^2 (x Q^2 - k_T^2/(1-x))]   (residue),
      checked by direct numerical integration with finite i*epsilon
  C4  logarithmic scaling in normal coordinates:  k_T^2 J -> 2 pi i/(2 p1^+ x Q^2) as k_T -> 0, so the shell
      lambda<|k_T|<2 lambda contributes a lambda-independent amount  (pi ln4) * 2 pi i/(2 p1^+ x Q^2)
  C5  direct scaling of measure x integrand at k=(x p1^+, lambda^2 kappa, lambda tau): exponent 0
Run:  python3 -I vertex_collinear_numeric.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np

mp.mp.dps = 30
PASS = []
def check(name, cond):
    PASS.append((name, bool(cond))); print(('PASS ' if cond else 'FAIL ') + name)

Q2 = mp.mpf(1)
p1p = mp.sqrt(Q2/2); p2m = mp.sqrt(Q2/2)      # 2 p1^+ p2^- = Q^2

def Ds(kp, km, kT2, eps=0):
    D0 = 2*kp*km - kT2 + 1j*eps
    D1 = 2*(p1p - kp)*(0 - km) - kT2 + 1j*eps
    D2 = 2*(0 + kp)*(p2m + km) - kT2 + 1j*eps
    return D0, D1, D2

def poles(kp, kT2, eps):
    """k^- positions of the zeros of D_j + i eps (each D_j is linear in k^-)."""
    # D0: 2 kp km - kT2 + i eps = 0
    z0 = (kT2 - 1j*eps)/(2*kp) if kp != 0 else None
    # D1: -2(p1p-kp) km - kT2 + i eps = 0
    z1 = (-kT2 + 1j*eps)/(2*(p1p - kp)) if kp != p1p else None
    # D2: 2 kp (p2m + km) - kT2 + i eps = 0
    z2 = -p2m + (kT2 - 1j*eps)/(2*kp) if kp != 0 else None
    return z0, z1, z2

print('=== C1/C2: pole positions in the complex k^- plane ===')
eps = mp.mpf('1e-8')
ok1 = True
for x in (mp.mpf('0.3'), mp.mpf('0.7')):
    for kT in (mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001')):
        z0, z1, z2 = poles(x*p1p, kT**2, eps)
        print(f'  x={float(x):.1f} kT={float(kT):.0e}:  Im z0={float(mp.im(z0)):+.1e} (Re {float(mp.re(z0)):+.2e})'
              f'  Im z1={float(mp.im(z1)):+.1e} (Re {float(mp.re(z1)):+.2e})  Im z2={float(mp.im(z2)):+.1e}')
        ok1 &= (mp.im(z0) < 0) and (mp.im(z1) > 0) and (mp.im(z2) < 0)
check('C1 for 0<x<1: D0,D2 poles below, D1 pole above the real k^- axis', ok1)
z0a, z1a, _ = poles(mp.mpf('0.3')*p1p, mp.mpf('1e-6')**2, 0)
check('C1 pinch: Re z0, Re z1 -> 0 from opposite sides as kT -> 0 (|z0|,|z1| ~ kT^2)',
      abs(z0a) < 1e-11 and abs(z1a) < 1e-11 and mp.re(z0a) > 0 and mp.re(z1a) < 0)
ok2 = True
for x in (mp.mpf('-0.4'), mp.mpf('1.5')):
    z = poles(x*p1p, mp.mpf('0.01'), eps)
    sgn = [mp.sign(mp.im(zz)) for zz in z]
    ok2 &= len(set(sgn)) == 1
    print(f'  x={float(x):+.1f}: signs of Im(poles) = {sgn}')
check('C2 for x<0 or x>1 all three poles on the same side -> int dk^- = 0', ok2)

print('=== C3: residue formula vs direct numerical k^- integration (finite i eps) ===')
def J_residue(x, kT2):
    return (2j*mp.pi/(2*p1p)) / (kT2*(x*Q2 - kT2/(1 - x)))
def J_numeric(x, kT2, eps):
    kp = x*p1p
    f = lambda km: 1/mp.fprod(Ds(kp, km, kT2, eps))
    z = poles(kp, kT2, eps)
    pts = sorted(set([mp.re(zz) for zz in z]))
    L = mp.mpf(10)**4
    nodes = [-L] + [pp + d for pp in pts for d in (-10*eps, 0, 10*eps)] + [L]
    nodes = sorted(set(nodes))
    val = mp.quad(f, nodes, maxdegree=10)
    # analytic tail beyond |k^-|>L : integrand ~ 1/(c k^3) -> odd -> tails cancel to O(1/L^2)
    return val
maxrel = 0
for x, kT in ((mp.mpf('0.3'), mp.mpf('0.2')), (mp.mpf('0.6'), mp.mpf('0.05')), (mp.mpf('0.8'), mp.mpf('0.3'))):
    kT2 = kT**2
    jn = J_numeric(x, kT2, mp.mpf('1e-12')); jr = J_residue(x, kT2)
    rel = abs(jn - jr)/abs(jr); maxrel = max(maxrel, rel)
    print(f'  x={float(x)} kT={float(kT)}: numeric {mp.nstr(jn, 12)}   residue {mp.nstr(jr, 12)}   rel.diff {float(rel):.1e}')
check('C3 residue formula agrees with direct integration (rel. diff < 1e-6)', maxrel < 1e-6)

print('=== C4: logarithmic scaling in the normal coordinate k_T ===')
x = mp.mpf('0.4')
lim = 2j*mp.pi/(2*p1p*x*Q2)
ok4 = True
for kT in (mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')):
    r = kT**2*J_residue(x, kT**2)/lim
    shell = mp.quad(lambda kt: 2*mp.pi*kt*J_residue(x, kt**2), [kT, 2*kT])   # int d^2kT over lambda<|kT|<2 lambda
    print(f'  kT={float(kT):.0e}:  kT^2 J / limit = {mp.nstr(r, 10)}    shell integral / (pi ln4 * limit) = {mp.nstr(shell/(mp.pi*mp.log(4)*lim), 10)}')
    if kT < mp.mpf('1e-2'):
        ok4 &= abs(r - 1) < 1e-4 and abs(shell/(mp.pi*mp.log(4)*lim) - 1) < 1e-4
check('C4 each shell lambda<kT<2lambda gives the same contribution as lambda->0 (log divergence)', ok4)

print('=== C5: power counting in normal coordinates (k^- = lambda^2 kappa, k_T = lambda tau) ===')
rng = np.random.default_rng(1)
slopes = []
for trial in range(5):
    kap = mp.mpf(float(rng.uniform(-2, 2))); tau2 = mp.mpf(float(rng.uniform(0.1, 2))); xx = mp.mpf(float(rng.uniform(0.1, 0.9)))
    vals = []
    lams = [mp.mpf(10)**(-e) for e in (3, 4, 5, 6)]
    for lam in lams:
        D0, D1, D2 = Ds(xx*p1p, lam**2*kap, lam**2*tau2)
        meas = lam**2*lam**2           # dk^- d^2k_T  -> lambda^2 * lambda^2
        vals.append(mp.log(abs(meas/(D0*D1*D2))))
    sl = (vals[-1] - vals[0])/(mp.log(lams[-1]) - mp.log(lams[0]))
    slopes.append(float(sl))
print('  fitted exponents:', np.round(slopes, 6))
check('C5 measure x integrand scales as lambda^0 in the collinear region', max(abs(np.array(slopes))) < 1e-4)

print('\nSUMMARY: %d/%d checks passed' % (sum(p for _, p in PASS), len(PASS)))
