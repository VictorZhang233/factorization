# N12: C_S at eps = 0.7 with the corner singularity at a=b=0 removed by a = s w, b = s(1-w) (Jacobian s).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
B_ = lambda e: mp.gamma(1+e)**2*mp.gamma(1-e)/e**2
Qt2, m2 = mp.mpf('2.08'), mp.mpf('0.02')
for e in [mp.mpf('0.45'), mp.mpf('0.7')]:
    f = lambda s, w: s*(s*s*w*(1-w)*Qt2 + s*m2)**(-1-e)
    # s in [0,1] directly; s in [1,inf) via s = y^(-1/(2e)) (integrand ~ s^(-1-2e) at large s)
    I1 = mp.quad(f, [0, 1], [0, mp.mpf('0.5'), 1])
    g = lambda y, w: f(y**(-1/(2*e)), w)*y**(-1/(2*e)-1)/(2*e)
    I2 = mp.quad(g, [0, 1], [0, mp.mpf('0.5'), 1])
    num = mp.gamma(1+e)*(I1 + I2)
    ex = (Qt2/m2**2)**e*B_(e)/Qt2
    print("eps=%s  C_S num %s  exact %s  rel.diff %s  -> %s" % (mp.nstr(e, 3), mp.nstr(num, 16), mp.nstr(ex, 16), mp.nstr(num/ex - 1, 3), "PASS" if abs(num/ex-1) < 1e-12 else "FAIL"))
# The 2D tensor-product quadrature is limited (~1e-10) at eps=0.7 by a moving boundary layer w ~ m^2/(s Qt^2) in the
# large-s tail (which decays like s^(-1-eps)).  Inner b-integral in closed form (elementary):
#   int_0^inf db (b(a Qt^2+m^2) + a m^2)^(-1-eps) = (a m^2)^(-eps) / (eps (a Qt^2 + m^2)),  then 1D quadrature in a:
for e in [mp.mpf('0.45'), mp.mpf('0.7'), mp.mpf('0.9')]:
    f1 = lambda a: (a*m2)**(-e)/(e*(a*Qt2 + m2))
    num = mp.gamma(1+e)*mp.quad(f1, [0, m2/Qt2, 1, mp.inf])
    ex = (Qt2/m2**2)**e*B_(e)/Qt2
    print("eps=%s  C_S (inner closed, outer 1D) %s  exact %s  rel.diff %s  -> %s" % (mp.nstr(e, 3), mp.nstr(num, 16), mp.nstr(ex, 16), mp.nstr(num/ex - 1, 3), "PASS" if abs(num/ex-1) < 1e-15 else "FAIL"))
# endpoint-regularizing maps: a = u^(1/(1-eps)) on [0,1] (removes a^-eps), a = v^(-1/eps) on [1,inf) (removes a^(-1-eps) tail)
print("with endpoint-regularizing maps:")
for e in [mp.mpf('0.45'), mp.mpf('0.7'), mp.mpf('0.9')]:
    h = lambda a: (a*m2)**(-e)/(e*(a*Qt2 + m2))
    p0 = lambda u: h(u**(1/(1-e)))*u**(e/(1-e))/(1-e)
    p1 = lambda v: h(v**(-1/e))*v**(-1/e-1)/e
    num = mp.gamma(1+e)*(mp.quad(p0, [0, (m2/Qt2)**(1-e), 1]) + mp.quad(p1, [0, 1]))
    ex = (Qt2/m2**2)**e*B_(e)/Qt2
    print("eps=%s  C_S %s  exact %s  rel.diff %s  -> %s" % (mp.nstr(e, 3), mp.nstr(num, 16), mp.nstr(ex, 16), mp.nstr(num/ex - 1, 3), "PASS" if abs(num/ex-1) < 1e-20 else "FAIL"))
