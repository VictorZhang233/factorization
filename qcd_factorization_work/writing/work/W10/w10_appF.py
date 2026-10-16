"""
W10 / App F ex:appF-telescoping -- the finite light-like Wilson line of the quark PDF and the Ward identity of the
gauge-invariant light-ray operator at tree level (book conventions: A(x) = int d^4k/(2pi)^4 e^{-ik.x} At(k), k flows
INTO the line; W[b,a] = P exp(i g int_a^b dz.A), later points to the left; w = (0^+, w^-, 0_T) = w^- n_B).
 (1) W^(1)[w,0] = g t^a nB.At(k) (1 - e^{-i k^+ w^-})/k^+   (entire in k^+)
 (2) = W^(1)[infty nB,0] + W^(1)[w, infty nB] = g/(k^+ - i0) - g e^{-ik^+w^-}/(k^+ - i0)   (i0 cancels)
     = W^(1)[-infty nB,0] + W^(1)[w,-infty nB] = g/(k^+ + i0) - g e^{-ik^+w^-}/(k^+ + i0)
 (3) tree-level matrix element <q(p')| psibar(w) gamma^+ W[w,0] psi(0) |q(p) + K gluon(k)>:
     the three attachments (incoming quark, outgoing quark, Wilson line) sum to zero (abelian colour structure t^a)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from w10_dirac import *

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

g_, kp, wm, s, eps = sp.symbols('g kp wm s epsilon', positive=True)
kpr = sp.symbols('kpr', real=True)
# (1) W^(1)[w,0] = i g int_0^1 ds w.A(s w) -> i g wm int_0^1 ds exp(-i s kp wm) (times nB.At(k) t^a)
W1 = sp.I*g_*wm*sp.integrate(sp.exp(-sp.I*s*kpr*wm), (s, 0, 1))
W1 = sp.simplify(W1)
target = g_*(1 - sp.exp(-sp.I*kpr*wm))/kpr
check('(1) W^(1)[w,0] = g (1 - e^{-i k^+ w^-})/k^+', sp.simplify(sp.piecewise_fold(W1).rewrite(sp.exp) - target) == 0 or
      sp.simplify((W1 - target).subs(kpr, sp.Rational(7, 3)).subs(wm, sp.Rational(5, 2))) == 0, W1)
check('(1) it is entire at k^+ = 0 (limit g w^-)', sp.limit(target, kpr, 0) == sp.I*g_*wm*1 or sp.limit(target, kpr, 0) == g_*sp.I*wm,
      sp.limit(target, kpr, 0))
# (2) semi-infinite lines with adiabatic damping
# W[infty nB, 0]: path z = s nB, s: 0 -> infty, damping e^{-eps s}:  i g int_0^inf ds e^{-i s kp} e^{-eps s}
Wf = sp.I*g_*sp.integrate(sp.exp(-sp.I*s*kpr - eps*s), (s, 0, sp.oo), conds='none')
check('(2) W^(1)[infty nB,0] = g/(k^+ - i eps)', sp.simplify(Wf - g_/(kpr - sp.I*eps)) == 0, sp.simplify(Wf))
# W[w, infty nB]: path from w + infty nB down to w: int_inf^0 ds nB.A(w + s nB) = - int_0^inf ...
Wb = -sp.I*g_*sp.exp(-sp.I*kpr*wm)*sp.integrate(sp.exp(-sp.I*s*kpr - eps*s), (s, 0, sp.oo), conds='none')
check('(2) W^(1)[w, infty nB] = -g e^{-ik^+w^-}/(k^+ - i eps)', sp.simplify(Wb + g_*sp.exp(-sp.I*kpr*wm)/(kpr - sp.I*eps)) == 0)
check('(2) sum of the two semi-infinite lines -> W^(1)[w,0] as eps -> 0 (i0 cancels)', sp.simplify(sp.limit(Wf + Wb, eps, 0) - target) == 0)
# past-pointing version: W[-infty nB, 0] (path 0 -> -infty, orientation -nB): -i g int_0^inf ds e^{+i s kp} e^{-eps s}
Wp = -sp.I*g_*sp.integrate(sp.exp(sp.I*s*kpr - eps*s), (s, 0, sp.oo), conds='none')
check('(2) W^(1)[-infty nB,0] = g/(k^+ + i eps)', sp.simplify(Wp - g_/(kpr + sp.I*eps)) == 0, sp.simplify(Wp))
Wp2 = sp.I*g_*sp.exp(-sp.I*kpr*wm)*sp.integrate(sp.exp(sp.I*s*kpr - eps*s), (s, 0, sp.oo), conds='none')
check('(2) W^(1)[w,-infty nB] = -g e^{-ik^+w^-}/(k^+ + i eps), and the sum -> W^(1)[w,0]',
      sp.simplify(Wp2 + g_*sp.exp(-sp.I*kpr*wm)/(kpr + sp.I*eps)) == 0 and sp.simplify(sp.limit(Wp + Wp2, eps, 0) - target) == 0)
# K-gluon contraction: k_mu nB^mu = k^+
check('(2) K gluon on the operator vertex: k^+ W^(1)[w,0]/(g nB.At) = g(1 - e^{-ik.w}) (difference of two injections)',
      sp.simplify(kpr*target - g_*(1 - sp.exp(-sp.I*kpr*wm))) == 0)

# (3) tree-level Ward identity of the gauge-invariant operator
rng = np.random.default_rng(99)
g = 1.0
def onshell(mass):
    pv = rng.normal(size=3); E = np.sqrt(pv @ pv + mass**2)
    return np.array([E, *pv], dtype=complex)
gplus = (GAM[0] + GAM[3])/np.sqrt(2)          # gamma^+ = (gamma^0 + gamma^3)/sqrt2
for m in [0.0, 0.3]:
    p = onshell(m); pp = onshell(m); k = rnd_vec(rng)
    wv = lc(0.0, 1.7)                           # w = (0^+, w^-, 0_T)
    ph = lambda q: np.exp(1j*mdot(q, wv))       # e^{i q.w} from psibar(w) creating momentum q
    for u in u_spinors(p, m)[:1]:
        for up in u_spinors(pp, m)[:1]:
            ub = bar(up)
            t_in = ph(pp)*(ub @ gplus @ S(p+k, m) @ (1j*g*slash(k)) @ u)        # gluon absorbed by the incoming quark
            t_out = ph(pp-k)*(ub @ (1j*g*slash(k)) @ S(pp-k, m) @ gplus @ u)    # gluon absorbed by the outgoing quark
            kplus = plus(k)
            Wterm = g*(1 - np.exp(-1j*mdot(k, wv)))/kplus                       # first-order finite line, nB.At -> k^+ below
            t_W = ph(pp)*(ub @ gplus @ u)*kplus*Wterm
            tot = t_in + t_out + t_W
            check('(3) Ward identity of psibar(w) gamma^+ W[w,0] psi(0), one K gluon, m=%.1f: sum = 0' % m,
                  abs(tot)/max(abs(t_in), abs(t_out), abs(t_W)) < 1e-12, '%.2e' % (abs(tot)/abs(t_in)))
            check('    term (i) = -g e^{ip\'.w} ubar gamma^+ u', abs(t_in - (-g)*ph(pp)*(ub @ gplus @ u))/abs(t_in) < 1e-12)
            check('    term (ii) = +g e^{i(p\'-k).w} ubar gamma^+ u', abs(t_out - g*ph(pp-k)*(ub @ gplus @ u))/abs(t_out) < 1e-12)
print('\n=== w10_appF: %d PASS, %d FAIL ===' % (npass, nfail))
