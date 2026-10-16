"""K12: joint-localization ordering weight used on p.195 and in E1 of R8 notes:
 for external factors with single poles z1, z2 in the lower half plane (time representation theta(tau) e^{-i z tau}),
 the weight of the ordering tau1 < tau2 is z1/(z1+z2); it depends on k_j^+ through z_j = kTj^2/(2 k_j^+).
 Also: Example E.38(3) remark -- the weight depends on kT1^2/kT2^2 as well as on k1^+/k2^+."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
t1, t2 = sp.symbols('tau1 tau2', positive=True)
z1, z2 = sp.symbols('z1 z2')
# use z = x - i y with y>0 so the integrals converge; do it with explicit positive damping
x1, x2, y1, y2 = sp.symbols('x1 x2 y1 y2', positive=True)
Z1 = x1 - sp.I*y1; Z2 = x2 - sp.I*y2
full = sp.integrate(sp.exp(-sp.I*Z1*t1), (t1, 0, sp.oo), conds='none')*sp.integrate(sp.exp(-sp.I*Z2*t2), (t2, 0, sp.oo), conds='none')
inner = sp.integrate(sp.exp(-sp.I*Z2*t2), (t2, t1, sp.oo), conds='none')
reg12 = sp.integrate(sp.exp(-sp.I*Z1*t1)*inner, (t1, 0, sp.oo), conds='none')
w12 = sp.simplify(reg12/full)
ok = sp.simplify(w12 - Z1/(Z1+Z2)) == 0
print('w(tau1<tau2) =', w12, '; equals z1/(z1+z2):', ok)
kT1, kT2, k1p, k2p = sp.symbols('kT1 kT2 k1p k2p', positive=True)
w = (kT1**2/(2*k1p))/((kT1**2/(2*k1p)) + (kT2**2/(2*k2p)))
print('with z_j = kTj^2/(2 kj^+): w12 =', sp.simplify(w), ' (depends on kT1^2 k2p and kT2^2 k1p, not only on k1p/k2p)')
print('K12 PASS' if ok else 'K12 FAIL')

# opposite half planes (k1^+ > 0 > k2^+): f1 ~ theta(tau1) e^{-i z1 tau1}, f2 ~ theta(-tau2) e^{-i z2 tau2} (Im z2 > 0)
x2b, y2b = sp.symbols('x2b y2b', positive=True)
Z2b = x2b + sp.I*y2b
full_b = sp.integrate(sp.exp(-sp.I*Z1*t1), (t1, 0, sp.oo), conds='none')*sp.integrate(sp.exp(-sp.I*Z2b*(-t2)), (t2, 0, sp.oo), conds='none')
# region tau1 < tau2 is empty because tau1 > 0 > tau2 on the supports
print('opposite half planes: support of (tau1,tau2) is tau1>0>tau2, so w(tau1<tau2) = 0 identically; full integral =', sp.simplify(full_b))
print('K12b PASS (weights are piecewise in k^+: z1/(z1+z2) for same sign, 0/1 for opposite sign)')
