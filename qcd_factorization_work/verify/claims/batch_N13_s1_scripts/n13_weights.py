"""N13 -- independent check of the joint-localization ordering weights.

Setting (reference p. 195-196; R8 E1; ERR-S3): an SS line j has external factor
    G_j(k^-) = 1/(2 k_j^+ k^- - kT_j^2 + i0) = (1/(2k_j^+)) * 1/(k^- - z_j + i0 sgn k_j^+),  z_j = kT_j^2/(2 k_j^+).
Fourier transform G~(tau) = int dk^-/(2pi) e^{-i k^- tau} G(k^-):
    k^+ > 0 (pole in the LOWER half plane):  G~ = -(i/(2k^+)) theta(+tau) e^{-i z tau}
    k^+ < 0 (pole in the UPPER half plane):  G~ = +(i/(2k^+)) theta(-tau) e^{-i z tau}
If J(tau_1..tau_N) is piecewise constant near 0 with jumps only on tau_i = tau_j, the equal-time limit of
int dtau J prod G~_j is  sum_pi J_pi(0) * W_pi,  W_pi = (int over {tau_pi(1)<...<tau_pi(N)} prod G~_j)/(prod_j G_j(0)).
This script derives W_pi exactly and checks it numerically (nested quadrature at finite damping), for
  (a) all poles in the LHP, (b) all poles in the UHP, (c) mixed signs,
and compares with the claimed formula  w_pi = prod_j z_j / prod_m sum_{l>=m} z_{pi(l)}  ("for same-side poles").
It also checks sum_pi w_pi = 1, continuity/kinks at k_j^+ = 0, and a finite-scale (lambda_J) version.
Run: python3 -I -u n13_weights.py
"""
import sys, os, itertools
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
mp.mp.dps = 20

npass = nfail = 0
def report(ok, name, detail=''):
    global npass, nfail
    if ok: npass += 1
    else: nfail += 1
    print(('PASS ' if ok else 'FAIL ') + name + ('   [' + detail + ']' if detail else ''), flush=True)

# ---------------------------------------------------------------------------------------------
# 1. Fourier pair of the single-pole external factor, both signs of k^+ (exact inverse transform)
# ---------------------------------------------------------------------------------------------
apos, kTs = sp.symbols('a kT', positive=True)      # a = |k^+|
t = sp.symbols('t', real=True)
y = sp.symbols('y', positive=True); xr = sp.symbols('x', real=True)
for sgn in [+1, -1]:
    kplus = sgn*apos
    z = kTs**2/(2*kplus)
    if sgn > 0:   # G~ = -(i/(2k+)) theta(t) e^{-izt}; inverse transform converges for Im k^- > 0
        val = sp.integrate(sp.exp(sp.I*(xr + sp.I*y - z)*t)*(-sp.I/(2*kplus)), (t, 0, sp.oo), conds='none')
        target = 1/(2*kplus*(xr + sp.I*y) - kTs**2)
    else:         # G~ = +(i/(2k+)) theta(-t) e^{-izt}; converges for Im k^- < 0
        val = sp.integrate(sp.exp(sp.I*(xr - sp.I*y - z)*t)*(sp.I/(2*kplus)), (t, -sp.oo, 0), conds='none')
        target = 1/(2*kplus*(xr - sp.I*y) - kTs**2)
    report(sp.simplify(val - target) == 0,
           f'FT pair for k+ {"> 0: LHP pole <-> support tau>0" if sgn>0 else "< 0: UHP pole <-> support tau<0"}',
           'inverse transform reproduces 1/(2k+k- - kT^2 + i0) with the boundary value from the correct side')

# ---------------------------------------------------------------------------------------------
# 2. Exact ordering weights.  Kernel of insertion j: theta(s_j tau) e^{-i Z_j tau}, s_j = +1 (k_j^+>0), -1 (k_j^+<0).
#    Elementary iterated integration (done symbolically below by hand-coded antiderivatives):
#      int_a^inf e^{-iAt} dt = e^{-iAa}/(iA)   (Im A<0),     int_{-inf}^b e^{-iAt} dt = e^{-iAb}/(-iA)  (Im A>0).
# ---------------------------------------------------------------------------------------------
def region_integral(signs, Z, perm):
    """int over {tau_perm[0] < ... < tau_perm[N-1]} of prod_j theta(s_j tau_j) e^{-i Z_j tau_j}  (exact, symbolic)."""
    N = len(signs)
    sg = [signs[p] for p in perm]
    if any(sg[i] > 0 and sg[i+1] < 0 for i in range(N-1)):
        return sp.Integer(0)          # a positive-support variable would precede a negative-support one
    neg = [p for p in perm if signs[p] < 0]      # time-ordered, all < 0
    pos = [p for p in perm if signs[p] > 0]      # time-ordered, all > 0
    val = sp.Integer(1)
    # negative block: integrate earliest first: t_neg[0] from -inf to t_neg[1], ..., last from -inf to 0
    acc = sp.Integer(0)
    for p in neg:
        acc += Z[p]
        val *= 1/(-sp.I*acc)
    # positive block: integrate latest first: t_pos[-1] from t_pos[-2] to inf, ..., first from 0 to inf
    acc = sp.Integer(0)
    for p in reversed(pos):
        acc += Z[p]
        val *= 1/(sp.I*acc)
    return val
def norm(signs, Z):
    v = sp.Integer(1)
    for j, s in enumerate(signs):
        v *= 1/(sp.I*s*Z[j])
    return v
def weights(signs, Z):
    return {p: sp.simplify(region_integral(signs, Z, p)/norm(signs, Z)) for p in itertools.permutations(range(len(signs)))}

def claimed(perm, zs):     # prod_j z_j / prod_m sum_{l>=m} z_{pi(l)}
    num = sp.Integer(1)
    for zz in zs: num *= zz
    den = sp.Integer(1)
    for m in range(len(perm)):
        den *= sum(zs[perm[l]] for l in range(m, len(perm)))
    return num/den
def reversed_formula(perm, zs):   # prod_j z_j / prod_m sum_{l<=m} z_{pi(l)}
    num = sp.Integer(1)
    for zz in zs: num *= zz
    den = sp.Integer(1)
    for m in range(len(perm)):
        den *= sum(zs[perm[l]] for l in range(0, m+1))
    return num/den

z1, z2, z3 = sp.symbols('z1 z2 z3')
Wa = weights([+1, +1], [z1, z2])
report(sp.simplify(Wa[(0, 1)] - z1/(z1+z2)) == 0, 'N=2, k1+,k2+>0 (LHP): W(tau1<tau2) = z1/(z1+z2)', str(Wa[(0, 1)]))
Wb = weights([-1, -1], [z1, z2])
report(sp.simplify(Wb[(0, 1)] - z2/(z1+z2)) == 0, 'N=2, k1+,k2+<0 (UHP): W(tau1<tau2) = z2/(z1+z2)', str(Wb[(0, 1)]))
report(sp.simplify(Wb[(0, 1)] - claimed((0, 1), [z1, z2])) != 0,
       "N=2 UHP: the claimed 'same-side' rule w12 = z1/(z1+z2) is WRONG for k1+,k2+<0",
       f'claimed {claimed((0,1),[z1,z2])} vs exact {Wb[(0,1)]}')
Wc = weights([+1, -1], [z1, z2])
report(Wc[(0, 1)] == 0 and Wc[(1, 0)] == 1, 'N=2 mixed (k1+>0>k2+): W(tau1<tau2)=0, W(tau2<tau1)=1', str(Wc))
zs3 = [z1, z2, z3]
W3a = weights([+1, +1, +1], zs3)
report(all(sp.simplify(W3a[p] - claimed(p, zs3)) == 0 for p in W3a), 'N=3 LHP: claimed formula holds for all 6 orderings')
report(sp.simplify(sum(W3a.values()) - 1) == 0, 'N=3 LHP: weights sum to 1')
W3b = weights([-1, -1, -1], zs3)
report(all(sp.simplify(W3b[p] - reversed_formula(p, zs3)) == 0 for p in W3b)
       and not all(sp.simplify(W3b[p] - claimed(p, zs3)) == 0 for p in W3b),
       'N=3 UHP: W_pi = prod z / prod_m sum_{l<=m} z_pi(l) (reversed order); claimed formula fails')
report(sp.simplify(sum(W3b.values()) - 1) == 0, 'N=3 UHP: weights sum to 1')
W3c = weights([+1, +1, -1], zs3)
nz = {p: W3c[p] for p in W3c if W3c[p] != 0}
print('   N=3 mixed (k1+,k2+>0>k3+), non-zero weights:', nz)
report(set(nz) == {(2, 0, 1), (2, 1, 0)} and sp.simplify(nz[(2, 0, 1)] - z1/(z1+z2)) == 0,
       "N=3 mixed signs: weights are not 0/1 (insertion 3 first, then z1/(z1+z2), z2/(z1+z2))")
yy = sp.symbols('y1:5', positive=True)
tot = sum(claimed(p, list(yy)) for p in itertools.permutations(range(4)))
report(sp.simplify(sp.together(tot) - 1) == 0, 'N=4: sum of the LHP formula over all 24 orderings = 1 (eikonal identity, symbolic)')
from fractions import Fraction
import random
random.seed(7)
for N in [5, 6, 7]:
    for trial in range(3):
        zf = [Fraction(random.randint(1, 50), random.randint(1, 50)) for _ in range(N)]
        tot = Fraction(0)
        for p in itertools.permutations(range(N)):
            num = Fraction(1)
            for zz in zf: num *= zz
            den = Fraction(1)
            for m_ in range(N): den *= sum(zf[p[l]] for l in range(m_, N))
            tot += num/den
        if tot != 1: break
    report(tot == 1, f'N={N}: sum over all {len(list(itertools.permutations(range(N))))} orderings = 1 exactly (3 random rational z-sets)')

# numerical cross-check of the exact region integrals (nested quadrature, finite damping delta)
def num_region(signs, Zs, perm):
    N = len(signs)
    f = lambda *ts: mp.e**(-1j*sum(Zs[j]*ts[j] for j in range(N)))
    sg = [signs[p] for p in perm]
    if any(sg[i] > 0 and sg[i+1] < 0 for i in range(N-1)): return mp.mpf(0)
    # nested integration in time order; bounds depend on the previous variable
    def integrate_level(level, prev, fixed):
        p = perm[level]
        lo = prev if prev is not None else (-mp.inf if signs[p] < 0 else 0)
        if prev is not None and signs[p] > 0 and signs[perm[level-1]] < 0: lo = 0
        hi = 0 if signs[p] < 0 else mp.inf
        def g(tv):
            fx = dict(fixed); fx[p] = tv
            if level == N-1:
                return f(*[fx[j] for j in range(N)])
            return integrate_level(level+1, tv, fx)
        return mp.quad(g, [lo, hi])
    return integrate_level(0, None, {})
delta = mp.mpf('0.4')
cases = [([+1, +1], [mp.mpf('0.8'), mp.mpf('1.9')]), ([-1, -1], [mp.mpf('-0.8'), mp.mpf('-1.9')]),
         ([+1, -1], [mp.mpf('0.8'), mp.mpf('-1.9')])]
for signs, zr in cases:
    Zs = [zr[j] - 1j*signs[j]*delta for j in range(len(signs))]
    Zsym = [sp.nsimplify(str(zr[j])) - sp.I*signs[j]*sp.Rational(2, 5) for j in range(len(signs))]
    for perm in itertools.permutations(range(len(signs))):
        ex = complex(sp.N(region_integral(signs, Zsym, perm)))
        nu = complex(num_region(signs, Zs, perm))
        report(abs(ex - nu) < 1e-8, f'numeric nested quad vs exact region integral, signs={signs}, order={perm}', f'{nu:.8f} vs {ex:.8f}')
# one N=3 UHP ordering numerically
signs = [-1, -1, -1]; zr = [mp.mpf('-0.8'), mp.mpf('-1.9'), mp.mpf('-0.5')]
Zs = [zr[j] + 1j*delta for j in range(3)]
Zsym = [sp.nsimplify(str(zr[j])) + sp.I*sp.Rational(2, 5) for j in range(3)]
for perm in [(0, 1, 2)]:   # one 3D nested quadrature suffices (slow)
    ex = complex(sp.N(region_integral(signs, Zsym, perm))); nu = complex(num_region(signs, Zs, perm))
    report(abs(ex - nu) < 1e-7, f'numeric nested quad N=3 UHP order={perm}', f'{nu:.8f} vs {ex:.8f}')

# ---------------------------------------------------------------------------------------------
# 3. Continuity / kinks in k_j^+ (with the CORRECT weights) -- non-analyticity at k_j^+ = 0
# ---------------------------------------------------------------------------------------------
def w12_true(k1, k2, kT1=1.0, kT2=1.3):   # weight of tau1<tau2 (operator order O2 O1)
    a1 = kT1**2/(2*k1); a2 = kT2**2/(2*k2)
    if k1 > 0 and k2 > 0: return a1/(a1+a2)
    if k1 < 0 and k2 < 0: return a2/(a1+a2)
    return 1.0 if k1 < 0 < k2 else 0.0
def w12_claim(k1, k2, kT1=1.0, kT2=1.3):
    a1 = kT1**2/(2*k1); a2 = kT2**2/(2*k2)
    if k1*k2 > 0: return a1/(a1+a2)
    return 1.0 if k1 < 0 < k2 else 0.0
h = 1e-7
for k2 in [0.6, -0.6]:
    l, r = w12_true(-h, k2), w12_true(h, k2)
    dl = (w12_true(-h, k2) - w12_true(-2*h, k2))/h; dr = (w12_true(2*h, k2) - w12_true(h, k2))/h
    report(abs(l - r) < 1e-5 and abs(dl - dr) > 1e-3, f'true w12 continuous but kinked at k1+=0 (k2+={k2:+.1f})',
           f'w(0-)={l:.6f} w(0+)={r:.6f} dw/dk1(0-)={dl:.4f} dw/dk1(0+)={dr:.4f}')
    cl, cr = w12_claim(-h, k2), w12_claim(h, k2)
    print(f'   claimed same-side rule at k2+={k2:+.1f}: w(0-)={cl:.6f}, w(0+)={cr:.6f}' + ('  <- spurious JUMP' if abs(cl-cr) > 0.5 else ''))
vals = [w12_true(1e-3*a, 1e-3*b) for (a, b) in [(1, 1), (1, 3), (3, 1)]]
report(max(vals) - min(vals) > 0.1, 'true w12 is direction dependent at the corner k1+=k2+=0', str([round(v, 4) for v in vals]))

# ---------------------------------------------------------------------------------------------
# 4. Finite lambda_J: J(t1,t2) = e^{-lam(|t1|+|t2|)} [A theta(t2-t1) + B theta(t1-t2)]: limit and O(lam/z) error
# ---------------------------------------------------------------------------------------------
lam = sp.symbols('lam', positive=True)
Asym, Bsym = sp.symbols('A B')
for signs, zz in [([+1, +1], [sp.Rational(3, 2), sp.Rational(5, 7)]), ([-1, -1], [-sp.Rational(3, 2), -sp.Rational(5, 7)])]:
    Zl = [zz[j] - sp.I*signs[j]*lam for j in range(2)]      # the envelope e^{-lam s t} = shift z -> z - i s lam
    res = (Asym*region_integral(signs, Zl, (0, 1)) + Bsym*region_integral(signs, Zl, (1, 0)))/norm(signs, zz)
    lim = sp.simplify(res.subs(lam, 0))
    pred = (Asym*zz[0] + Bsym*zz[1])/(zz[0]+zz[1]) if signs[0] > 0 else (Asym*zz[1] + Bsym*zz[0])/(zz[0]+zz[1])
    d1 = sp.simplify(sp.diff(res, lam).subs(lam, 0))
    report(sp.simplify(lim - pred) == 0, f'finite lambda_J, signs={signs}: lambda->0 gives the weighted sum of the two orders',
           f'limit={lim}; d/dlam at 0 = {d1}')

print(f'\nSUMMARY: {npass}/{npass+nfail} PASS')
