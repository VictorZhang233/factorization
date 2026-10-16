# W26 / Ch23 -- s02: hyperbolic angle of single-time-ordered (T) soft functions; check of tab:yzliu-theta (VF-YZL-4)
# and of the complex Lorentz map Lambda(t,z) = (iz, it) used in thm:yzliu-time-ordering (VF-YZL-12 note).
#
# One-loop exchange between an incoming line (tangent q1, points s*q1, s<0) and an outgoing line (tangent q2, points
# t*q2, t>0) with the Feynman propagator 1/(-x^2+i0):  x = s q1 - t q2,  -x^2 + i0 = -t^2 [Q(rho) - i0],
# Q(rho) = rho^2 q1^2 + 2 rho q1.q2 + q2^2 (rho = -s/t > 0).  The angle-dependent part of the cusp is
#     F(q1,q2) = q1.q2 * Int_0^oo d rho / (Q(rho) - i0)  ==  theta coth theta,
# which fixes theta (up to theta -> -theta).  We compare with Liu's Table 1 and with two candidate closed forms
#     cosh theta = (q1.q2 - i0)/( sqrt(q1^2 -/+ i0) sqrt(q2^2 -/+ i0) ).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30

def dot(a, b):  # (t,z) with metric (+,-)
    return a[0]*b[0] - a[1]*b[1]

def F_integral(q1, q2):
    A, B, C = dot(q1, q1), dot(q1, q2), dot(q2, q2)
    # roots of Q(rho) on (0, inf)
    roots = []
    disc = B*B - A*C
    if disc > 0:
        for sgn in (+1, -1):
            r = (-B + sgn*mp.sqrt(disc))/A if A != 0 else None
            if r is not None and r > 0:
                roots.append(r)
    roots.sort()
    # principal value by symmetric excision + i*pi*sum 1/|Q'|
    eps = mp.mpf('1e-12')
    pts = [mp.mpf(0)]
    for r in roots:
        pts += [r - eps, r + eps]
    pts.append(mp.inf)
    Q = lambda rho: A*rho*rho + 2*B*rho + C
    pv = mp.mpf(0)
    for i in range(0, len(pts) - 1, 2):
        pv += mp.quad(lambda rho: 1/Q(rho), [pts[i], pts[i+1]])
    im = sum(mp.pi/abs(2*A*r + 2*B) for r in roots)
    return B*(pv + 1j*im)

def thcoth(th):
    return th*mp.coth(th)

def theta_formula(q1, q2, s, ratio=1):
    # s = -1: sqrt(q^2 - i0) ; s = +1: sqrt(q^2 + i0)  (Liu APPB eq. (123) prints +i0)
    # ratio = (infinitesimal in the square roots)/(infinitesimal in q1.q2); ratio=1: one common -i0 as in Q(rho)-i0
    eta = mp.mpf('1e-25')
    c = (dot(q1, q2) - 1j*eta)/(mp.sqrt(dot(q1, q1) + s*1j*eta*ratio)*mp.sqrt(dot(q2, q2) + s*1j*eta*ratio))
    return mp.acosh(c)

Y, Yp = mp.mpf('1.3'), mp.mpf('0.7')
Yc = Y + Yp
v  = (mp.cosh(Y),  mp.sinh(Y))      # time-like, future, moving +z      (Liu: gamma(1,beta))
vp = (mp.cosh(Yp), -mp.sinh(Yp))    # time-like, future, moving -z      (Liu: gamma'(1,-beta'))
u  = (mp.sinh(Y),  mp.cosh(Y))      # space-like  (Liu: gamma(beta,1))
up = (-mp.sinh(Yp), mp.cosh(Yp))    # space-like  (Liu: gamma'(-beta',1)); staple along +u' lies at t<0 (past)
neg = lambda q: (-q[0], -q[1])
configs = [
    ('space/space  past/past  (Collins DY)', u, up,      Yc),
    ('time/time    past/past  (time-like DY)', v, neg(vp), Yc - 1j*mp.pi),
    ('time/time    past/future (form factor)', v, vp,     Yc),
    ('space/space  past/future (space-like SIDIS)', u, neg(up), Yc + 1j*mp.pi),
    ('time/space   past/future', v, neg(up), Yc + 1j*mp.pi/2),
    ('time/space   past/past',   v, up,      Yc - 1j*mp.pi/2),
]
ok_table = True; ok_minus = True; ok_plus = True
for name, q1, q2, th_tab in configs:
    Fint = F_integral(q1, q2)
    Ftab = thcoth(th_tab)
    thm = theta_formula(q1, q2, -1)
    thp = theta_formula(q1, q2, +1, ratio=mp.mpf('1e-6'))   # +i0 in the roots, subleading to the -i0 of q1.q2
    e_tab = abs(Fint - Ftab)
    e_m = abs(Fint - thcoth(thm))
    e_p = abs(Fint - thcoth(thp))
    ok_table &= e_tab < 1e-8; ok_minus &= e_m < 1e-8; ok_plus &= e_p < 1e-8
    print('%-46s F_int = %s' % (name, mp.nstr(Fint, 12)))
    print('      table theta = %-28s |F_int - theta coth theta| = %.1e' % (mp.nstr(th_tab, 8), e_tab))
    print('      sqrt(q^2-i0): theta = %-24s dev = %.1e ;  sqrt(q^2+i0): theta = %-24s dev = %.1e'
          % (mp.nstr(thm, 8), e_m, mp.nstr(thp, 8), e_p))
print('Table 1 (VF-YZL-4) reproduced by the one-loop single-T integral:', ok_table)
print('closed form with sqrt(q^2 - i0) reproduces all six rows       :', ok_minus)
print('closed form with sqrt(q^2 + i0) (as printed) reproduces all six:', ok_plus, '(fails for the two mixed rows)')

# ---- complex Lorentz map Lambda(t,z) = (i z, i t): proper (det = +1), preserves t^2 - z^2, boost of rapidity i*pi/2
import sympy as sp
t, z, lam, nu, Ys = sp.symbols('t z lambda nu Y', real=True)
L = sp.Matrix([[0, sp.I], [sp.I, 0]])
print('det Lambda =', L.det(), ';  Lambda^T g Lambda = g ?', sp.simplify(L.T*sp.diag(1, -1)*L - sp.diag(1, -1)) == sp.zeros(2))
eta_b = sp.I*sp.pi/2
Bst = sp.Matrix([[sp.cosh(eta_b), sp.sinh(eta_b)], [sp.sinh(eta_b), sp.cosh(eta_b)]])
print('boost(i pi/2) == Lambda ?', sp.simplify(Bst - L) == sp.zeros(2))
n = sp.Matrix([1, 1])/sp.sqrt(2); nb = sp.Matrix([1, -1])/sp.sqrt(2)
ez = sp.Matrix([0, 1]); et = sp.Matrix([1, 0])
chk = [sp.simplify(L*(-sp.I*lam*n) - lam*n), sp.simplify(L*(-sp.I*lam*nb) + lam*nb), sp.simplify(L*(-nu*ez) + sp.I*nu*et)]
vY = n + sp.exp(-Ys)*nb; vpY = nb + sp.exp(-Ys)*n; nY = n - sp.exp(-Ys)*nb; nbY = nb - sp.exp(-Ys)*n
chk += [sp.simplify(L*vY - sp.I*nY), sp.simplify(L*vpY + sp.I*nbY)]
print('Lambda(-i lam n)=lam n, Lambda(-i lam nb)=-lam nb, Lambda(-nu e_z)=-i nu e_t, Lambda v = i n_Y, Lambda v\' = -i nb_Y :',
      all(c == sp.zeros(2, 1) for c in chk))
# the slip (it, iz) is i*identity: reverses every interval (det = -1 in 2D, maps t^2-z^2 -> -(t^2-z^2))
W = sp.Matrix([[sp.I, 0], [0, sp.I]])
print('(t,z)->(it,iz): Lambda^T g Lambda =', W.T*sp.diag(1, -1)*W, ' (= -g, not a Lorentz transformation)')
