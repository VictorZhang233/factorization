# N12 (stage 2), part (a): finite-eps check of the four subtraction integrals as ABSOLUTELY CONVERGENT
# parametric integrals of the combined (pointwise-summed) integrands, with a tail map a = y^(-1/eps)
# that makes the slowly decaying a^(-1-eps) tails smooth.  No scaleless-integral convention is used.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += ok; nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""))
A_ = lambda e: mp.gamma(1+e)*mp.gamma(1-e)**2/(e**2*mp.gamma(1-2*e))
B_ = lambda e: mp.gamma(1+e)**2*mp.gamma(1-e)/e**2
def quad2(f, e):
    # int_0^inf int_0^inf f(a,b) da db ; on [1,inf): a = y^(-1/e), da = (1/e) y^(-1/e-1) dy
    def mapped(seg):
        if seg == 0:
            return lambda y: (y, mp.mpf(1))
        return lambda y: (y**(-1/e), y**(-1/e-1)/e)
    tot = 0
    for sa in (0, 1):
        for sb in (0, 1):
            ma, mb = mapped(sa), mapped(sb)
            def g(y, z):
                a, ja = ma(y); b, jb = mb(z)
                return f(a, b)*ja*jb
            tot += mp.quad(g, [0, 1], [0, 1])
    return tot
Pv, Ppv, m2v = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.02')
Qt2 = 2*Pv*Ppv
for e in [mp.mpf('0.3'), mp.mpf('0.15'), mp.mpf('0.45'), mp.mpf('0.7')]:
    G = mp.gamma(1+e)
    cs = G*quad2(lambda a, b: (a*b*Qt2 + (a+b)*m2v)**(-1-e), e)
    cc1 = G*quad2(lambda a, b: mp.expm1((-1+2*e)*mp.log1p(a))*(a*(b*Qt2 + m2v))**(-1-e), e)
    cc2 = G*quad2(lambda a, b: mp.expm1((-1+2*e)*mp.log1p(b))*(b*(a*Qt2 + m2v))**(-1-e), e)
    ch = G*quad2(lambda a, b: ((1+b)**(-1+2*e)*mp.expm1((-1+2*e)*mp.log1p(a/(1+b))) - mp.expm1((-1+2*e)*mp.log1p(a)))*(a*b*Qt2)**(-1-e), e)
    ex_s = (Qt2/m2v**2)**e*B_(e)/Qt2; ex_c = -(1/m2v)**e*A_(e)/Qt2; ex_h = (1/Qt2)**e*A_(e)/Qt2
    tag = "eps=%s" % mp.nstr(e, 3)
    check(tag + " C_S  = Qt^-2(mu^2 Qt^2/m^4)^eps B", abs(cs/ex_s - 1) < 1e-10, "%s vs %s" % (mp.nstr(cs, 14), mp.nstr(ex_s, 14)))
    check(tag + " C_C1 = -Qt^-2(mu^2/m^2)^eps A", abs(cc1/ex_c - 1) < 1e-10, "%s vs %s" % (mp.nstr(cc1, 14), mp.nstr(ex_c, 14)))
    check(tag + " C_C2 = C_C1", abs(cc2/ex_c - 1) < 1e-10, "%s" % mp.nstr(cc2, 14))
    check(tag + " C_H  = Qt^-2(mu^2/Qt^2)^eps A", abs(ch/ex_h - 1) < 1e-10, "%s vs %s" % (mp.nstr(ch, 14), mp.nstr(ex_h, 14)))
# also: the same with a second kinematic point (P, P', m^2) = (2.0, 0.35, 0.3)
Pv, Ppv, m2v = mp.mpf('2.0'), mp.mpf('0.35'), mp.mpf('0.3'); Qt2 = 2*Pv*Ppv
e = mp.mpf('0.25'); G = mp.gamma(1+e)
tot = G*quad2(lambda a, b: (a*b*Qt2 + (a+b)*m2v)**(-1-e)
                          + mp.expm1((-1+2*e)*mp.log1p(a))*(a*(b*Qt2 + m2v))**(-1-e)
                          + mp.expm1((-1+2*e)*mp.log1p(b))*(b*(a*Qt2 + m2v))**(-1-e)
                          + ((1+b)**(-1+2*e)*mp.expm1((-1+2*e)*mp.log1p(a/(1+b))) - mp.expm1((-1+2*e)*mp.log1p(a)))*(a*b*Qt2)**(-1-e), e)
ex = ((Qt2/m2v**2)**e*B_(e) - 2*(1/m2v)**e*A_(e) + (1/Qt2)**e*A_(e))/Qt2
check("second point, eps=0.25: sum_R C_R", abs(tot/ex - 1) < 1e-10, "%s vs %s" % (mp.nstr(tot, 14), mp.nstr(ex, 14)))
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
