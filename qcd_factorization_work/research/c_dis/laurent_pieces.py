"""
laurent_pieces.py -- prints, separately, the Laurent expansions (as distributions in z, mu = Q) of the real and
virtual O(alpha_s) contributions, used in DERIVATION.md; and the invariant (s,t,u) form of the D-dim squared
matrix elements of real_me.py (checked symbolically here).
Units: Fhat_a^q/(z e_q^2) = delta_{a2} delta(1-z) + (as/2pi) C_F (mu^2/Q^2)^eps [ ... ],
       Fhat_a^g/(z e_q^2) = (as/2pi) T_F (mu^2/Q^2)^eps [ ... ]   (one quark flavour, q and qbar both counted).
"""
import sys, os, io, contextlib
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import dis_nlo as m
import real_me
from distributions import Dist, expand_singular, expand_regular, z, eps

R = m.RESULTS
print('real, quark channel, F_2 (coefficient of eps^n):')
real2q = expand_singular(R['G2q'], order_max=0)
for n in (-2, -1, 0):
    print(f'  eps^{n}:', real2q[n].simplify().latex())
print('virtual (2 Re F^(1) in units (as/2pi) C_F (mu^2/Q^2)^eps) x delta(1-z):')
vser = sp.expand(m.clean(sp.series(R['Vff'], eps, 0, 2).removeO()))
for n in (-2, -1, 0, 1):
    print(f'  eps^{n}:', sp.nsimplify(sp.simplify(vser.coeff(eps, n))))
print('F_L quark (exact):  R_L^q =', sp.simplify(R['RLq']))
print('gluon channel F_2 (coefficient of eps^n), per T_F:')
real2g = expand_regular(R['R2g'], order_max=0)
for n in (-1, 0):
    print(f'  eps^{n}:', sp.factor(sp.simplify(real2g[n].reg)))

# ---------------------------------------------------------------- invariant forms of the squared MEs
y, Q2 = real_me.y, 1
s_ = (1 - z) / z
t_ = -y / z          # quark channel: t = (p-k)^2 ; gluon channel: t = (p-k1)^2
u_ = -(1 - y) / z    # quark channel: u = (q-k)^2 = (p-p')^2 ; gluon channel: u = (p-k2)^2 = (q-k1)^2
Tq_g, Tq_pp = real_me.quark_channel()
Tg_g, Tg_pp = real_me.gluon_channel()
forms = {
    'Tq_g  = 8(1-eps)[(1-eps)(-t/s - s/t) + 2uQ^2/(st) + 2eps]':
        (Tq_g, 8 * (1 - eps) * ((1 - eps) * (-t_ / s_ - s_ / t_) + 2 * u_ * Q2 / (s_ * t_) + 2 * eps)),
    'Tq_pp = -4(1-eps) u': (Tq_pp, -4 * (1 - eps) * u_),
    'Tg_g  = 8(1-eps)[(1-eps)(u/t + t/u) - 2sQ^2/(tu) - 2eps]':
        (Tg_g, 8 * (1 - eps) * ((1 - eps) * (u_ / t_ + t_ / u_) - 2 * s_ * Q2 / (t_ * u_) - 2 * eps)),
    'Tg_pp = 8 s': (Tg_pp, 8 * s_),
}
allok = True
for k, (a, b) in forms.items():
    good = sp.simplify(a - b) == 0
    allok &= good
    print(f'  [{"PASS" if good else "FAIL"}] {k}')
print('INVARIANT FORMS:', 'ALL PASS' if allok else 'FAIL')
