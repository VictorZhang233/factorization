"""s8_mb_regions.py  (writer W05, Ch5 ex:sudakov-offshell)

Check, by a Mellin-Barnes representation, that the expansion by regions of the off-shell Sudakov
triangle reproduces the exact small-t expansion (VF-REF-2) not only at leading power but also at
next-to-leading and next-to-next-to-leading power, with the 1/eps poles cancelling order by order.

Integral (Ch5 eq. sudakov-triangle):  I = e^{eps gE} mu^{2eps} Int d^Dk/(i pi^{D/2}) 1/[(-k^2)(-(k+p1)^2)(-(k+p2)^2)],
p1^2 = p2^2 = -P^2, (p1-p2)^2 = -Q^2, t = P^2/Q^2.
Feynman parameters: F = P^2 a0 (a1+a2) + Q^2 a1 a2 ; with a0 = 1-r, a1 = r u, a2 = r(1-u) (Jacobian r):
  Q^2 I = e^{eps gE} (mu^2/Q^2)^eps Gamma(1+eps) Int dr du r [ t (1-r) r + r^2 u(1-u) ]^{-1-eps}.
MB split (A+B)^{-l} = 1/(2 pi i) Int dz Gamma(-z) Gamma(l+z)/Gamma(l) A^z B^{-l-z}, A = t r(1-r), B = r^2 u(1-u):
  Int dr r^{-1-2eps-z} (1-r)^z = B(-2eps-z, 1+z),  Int du (u(1-u))^{-1-eps-z} = B(-eps-z,-eps-z)
  => Q^2 I = e^{eps gE}(mu^2/Q^2)^eps 1/(2 pi i) Int dz t^z Gamma(-z)Gamma(1+eps+z)Gamma(1+z)
                 Gamma(-2eps-z) Gamma(-eps-z)^2 / [Gamma(1-2eps) Gamma(-2eps-2z)].
Right poles: z = n (hard region, analytic in t), z = n - eps (double: the two collinear regions, t^{-eps}),
z = n - 2 eps (ultrasoft region, t^{-2eps}).  Closing to the right: Q^2 I = - sum of residues.
The sum of the residues of family n (a small circle around n enclosing n, n-eps, n-2eps) is the
order-t^n term of the region expansion; it must be finite as eps -> 0 and equal the exact coefficient.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 40
PASS = []
def check(name, ok, info=''):
    PASS.append(bool(ok)); print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

def integrand(z, eps, t):
    return (t ** z * mp.gamma(-z) * mp.gamma(1 + eps + z) * mp.gamma(1 + z) * mp.gamma(-2 * eps - z)
            * mp.gamma(-eps - z) ** 2 / (mp.gamma(1 - 2 * eps) * mp.gamma(-2 * eps - 2 * z)))

def family_sum(n, eps, t, rad=mp.mpf('0.45')):
    """(1/2 pi i) closed contour (counter-clockwise) around z = n - eps (encloses n, n-eps, n-2eps)."""
    c = n - eps
    f = lambda th: integrand(c + rad * mp.e ** (1j * th), eps, t) * rad * mp.e ** (1j * th)
    return mp.quad(f, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2 * mp.pi)

def pref(eps):          # e^{eps gE} (mu^2/Q^2)^eps at mu = Q
    return mp.e ** (eps * mp.euler)

def exact_coeff(n, L):  # VF-REF-2 with L = ln(Q^2/P^2)
    if n == 0: return L ** 2 + mp.pi ** 2 / 3
    if n == 1: return 2 * L ** 2 - 4 * L - 4 + 2 * mp.pi ** 2 / 3
    if n == 2: return 6 * L ** 2 - 14 * L - 11 + 2 * mp.pi ** 2

# (1) family sums at small eps are finite and equal the exact coefficients (times t^n)
for t in [mp.mpf('1e-3'), mp.mpf('2e-2')]:
    L = mp.log(1 / t)
    for n in [0, 1, 2]:
        vals = []
        for eps in [mp.mpf('1e-4'), mp.mpf('-1e-4')]:
            vals.append(-pref(eps) * family_sum(n, eps, t))
        v = (vals[0] + vals[1]) / 2               # symmetric average removes the O(eps) term
        ref = t ** n * exact_coeff(n, L)
        check('(1) region family n=%d at t=%s reproduces VF-REF-2 coefficient' % (n, mp.nstr(t, 2)),
              abs(v / ref - 1) < 1e-6, (mp.nstr(v, 12), mp.nstr(ref, 12)))

# (2) each family is finite as eps -> 0: poles cancel order by order.  A 1/eps remnant c/eps would make
#     v(1e-5)-v(1e-4) ~ 9e4 c; a regular family has v(eps) = v0 + v1 eps + ..., so the successive
#     differences shrink by a factor 10 (linear scaling) and eps*v(eps) -> 0.
t = mp.mpf('1e-2')
for n in [0, 1, 2]:
    v = [-pref(e) * family_sum(n, e, t) for e in [mp.mpf('1e-3'), mp.mpf('1e-4'), mp.mpf('1e-5')]]
    d1, d2 = abs(v[0] - v[1]), abs(v[1] - v[2])
    check('(2) family n=%d regular at eps=0 (differences scale linearly in eps: ratio ~ 10)' % n,
          abs(d1 / d2 - 10) < 0.5, (mp.nstr(d1, 6), mp.nstr(d2, 6), mp.nstr(d1 / d2, 6)))

# (3) individual pole families at n=0 reproduce the region formulas of VF-REG-10 (finite eps)
eps = mp.mpf('0.137'); t = mp.mpf('0.01')
N = lambda e: mp.e ** (e * mp.euler) * mp.gamma(1 + e) * mp.gamma(-e) ** 2 / mp.gamma(1 - 2 * e)
H = N(eps)                                    # (mu^2/Q^2)^eps = 1 at mu = Q
C = -(1 / t) ** eps * N(eps)                  # each collinear region; (mu^2/P^2)^eps = t^{-eps}
S = -(1 / t) ** (2 * eps) * mp.e ** (eps * mp.euler) * mp.gamma(1 + eps) * mp.gamma(eps) * mp.gamma(-eps)
def res_at(z0, eps, t, rad=mp.mpf('0.02')):
    f = lambda th: integrand(z0 + rad * mp.e ** (1j * th), eps, t) * rad * mp.e ** (1j * th)
    return mp.quad(f, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2 * mp.pi)
rH = -pref(eps) * res_at(mp.mpf(0), eps, t)
rC = -pref(eps) * res_at(-eps, eps, t)
rS = -pref(eps) * res_at(-2 * eps, eps, t)
check('(3) residue at z=0 = hard region H (VF-REG-10)', abs(rH / H - 1) < 1e-15, (mp.nstr(rH, 15), mp.nstr(H, 15)))
check('(3) residue at z=-eps = C1+C2 (double pole = two collinear regions)', abs(rC / (2 * C) - 1) < 1e-15, (mp.nstr(rC, 15), mp.nstr(2 * C, 15)))
check('(3) residue at z=-2eps = ultrasoft region S', abs(rS / S - 1) < 1e-15, (mp.nstr(rS, 15), mp.nstr(S, 15)))

# (4) the MB representation itself equals the 1D integral of the exact result at eps -> 0 (straight contour)
t = mp.mpf('0.05'); eps = mp.mpf('-0.2')
c0 = mp.mpf('-0.1')    # Re z = c0 with -1 < c0 and c0 < -2eps? choose strip: Re(-z)>0? need Gamma(-z): Re z < 0; Gamma(1+z): Re z>-1;
# Gamma(-2eps-z): Re z < -2eps = 0.4 ; Gamma(-eps-z): Re z < 0.2 ; Gamma(1+eps+z): Re z > -0.8  -> c0 = -0.1 ok
f = lambda y: integrand(c0 + 1j * y, eps, t)
mb = mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * mp.pi)
# direct parametric integral at eps=-0.2: Q^2 I = e^{eps gE} Gamma(1+eps) Int dr du r [t r(1-r) + r^2 u(1-u)]^{-1-eps}
g = lambda r, u: r * (t * r * (1 - r) + r ** 2 * u * (1 - u)) ** (-1 - eps)
direct = mp.e ** (eps * mp.euler) * mp.gamma(1 + eps) * mp.quad(g, [0, 1], [0, 0.5, 1])
check('(4) MB representation = direct Feynman-parameter integral (eps=-0.2, t=0.05)', abs(pref(eps) * mb / direct - 1) < 1e-8,
      (mp.nstr(pref(eps) * mb, 12), mp.nstr(direct, 12)))

print('\n=== s8_mb_regions: %d/%d PASS ===' % (sum(PASS), len(PASS)))
sys.exit(0 if all(PASS) else 1)
