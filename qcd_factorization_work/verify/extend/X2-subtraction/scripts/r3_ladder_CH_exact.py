"""X2 final revision / r3_ladder_CH_exact.py -- exact identification of the fibered C_H of the one-rung DIS ladder (M2)
(review r3_1 required fix 7, review r3_2 required fix 6; replaces the [P] grade of the fibered side in Prop C.4(e)).

Setting: d = 6 - 2 eps, Q = 1, x_B = x > 1, c = c_x = 1 - 1/x; measure int d^dk/(i pi^{d/2}); rung on shell.
  fibered C_H = (1/Gamma(2-eps)) int_0^1 dxi (1-xi) int_0^oo dt t^{-1-eps} [ <h0>(xi,t) - hhat(xi) ],
  <h0> = S^{3-2eps}-average of 1/(a + b cos), a = A + t/(1-xi), b = 2 sqrt(t), A = 1 - xi/x, hhat = 1/A.
Claims checked here (proofs in the report, Prop C.4(e)):
 (1) [transverse DR integral] for -1 < eps < 0:  int_0^oo dt t^{-1-eps} <h0> = Gamma(1+eps) Gamma(2-eps)(1-xi)
         int_0^1 dy y [(1-y)(1-xi)(xi c + y(1-xi))]^{-1-eps}           (Euclidean Feynman parameters in D = 4-2eps),
     and for 0 < eps < 1 the subtracted fibered integral equals the analytic continuation of this expression;
 (2) [simplex identity] T(eps) := int_0^1 ds s^{1-eps} int_0^1 dy y (1-y)^{-1-eps} (c(1-s) + y s)^{-1-eps}
         = B(-eps, 2-eps) int_0^1 dy y (c + y(1-c))^{-1-eps}
         = B(-eps, 2-eps) [ (1 - c^{1-eps})/(1-eps) + (c - c^{1-eps})/eps ] / (1-c)^2 ;
     proof: (alpha,beta,gamma) = (1-s, s y, s(1-y)) maps the unit square onto the 2-simplex with d(beta)d(gamma) = s ds dy,
     T = int_simplex beta gamma^{-1-eps} (c alpha + beta)^{-1-eps}; then (alpha,beta) = (1-gamma)(1-y', y').
 (3) hence fibered C_H = Gamma(1+eps) Q^{-2-2eps} B(-eps,2-eps) int_0^1 dy y (y + (1-y) c)^{-1-eps}   EXACTLY;
     the covariant parametric value of T_H Gamma (massless on-shell target, -1 < eps < 0) is the same expression
     (Gamma(1+eps) int_simplex x1 [x3 (x1 + x2 c)]^{-1-eps}, same substitution), continued to 0 < eps < 1;
 (4) the WHOLE-integrand parametric value of C_H (report formula and the independent form of review r3_1) agrees with
     the closed form numerically (several eps, including eps < 0);
 (5) the round-2 fibered quadrature (cut at t = e^-40) is repeated without the cut (working precision raised so that the
     cancellation <h0> - hhat = O(t) is resolved): the round-2 deviations 4e-15 (eps = 0.2) and 3.4e-13 (eps = 0.3) were
     the neglected part ~ e^{-40(1-eps)} = 1.3e-14, 6.9e-13 of the cut, not a mismatch."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
xB = mp.mpf(2); c = 1 - 1/xB

def closed(e):
    return mp.gamma(1 + e)*mp.beta(-e, 2 - e)*((1 - c**(1 - e))/(1 - e) + (c - c**(1 - e))/e)/(1 - c)**2
def closed_int(e):
    return mp.gamma(1 + e)*mp.beta(-e, 2 - e)*mp.quad(lambda y: y*(y + (1 - y)*c)**(-1 - e), [0, 1])

def T_square(e):
    """T(eps) on the unit square; for eps > 0 the y -> 1 end is continued: int (1-y)^{-1-e} g = int (1-y)^{-1-e}[g-g(1)] - g(1)/e"""
    def inner(s):
        g = lambda y: y*(c*(1 - s) + y*s)**(-1 - e)
        if e < 0:
            return mp.quad(lambda y: (1 - y)**(-1 - e)*g(y), [0, mp.mpf(1)/2, 1])
        g1 = g(mp.mpf(1))
        return mp.quad(lambda y: (1 - y)**(-1 - e)*(g(y) - g1), [0, mp.mpf(1)/2, 1]) - g1/e
    return mp.quad(lambda s: s**(1 - e)*inner(s), [0, mp.mpf(1)/2, 1])
def T_simplex(e):
    """T(eps) = int_simplex beta gamma^{-1-eps} (c alpha + beta)^{-1-eps}; continued in gamma for eps > 0"""
    def inner(gm):   # integrate beta in (0, 1-gm), alpha = 1 - gm - beta
        return mp.quad(lambda b: b*(c*(1 - gm - b) + b)**(-1 - e), [0, 1 - gm])
    if e < 0:
        return mp.quad(lambda gm: gm**(-1 - e)*inner(gm), [0, mp.mpf(1)/2, 1])
    i0 = inner(mp.mpf(0))
    return mp.quad(lambda gm: gm**(-1 - e)*(inner(gm) - i0), [0, mp.mpf(1)/2, 1]) - i0/e

def CH_fibered(e):
    """direct 2D fibered quadrature; the small-t end t < t0 = e^-40 is added analytically:
    <h0> - hhat = c1 t + O(t^2), c1 = -1/((1-xi) A^2) + 2/((2-eps) A^3)  =>  int_0^t0 t^{-1-eps}(...) = c1 t0^{1-eps}/(1-eps) + O(t0^{2-eps}).
    (The round-2 script omitted this tail: e^{-40(1-eps)} = 2.3e-16, 1.3e-14, 6.9e-13 for eps = 0.1, 0.2, 0.3.)"""
    lt0 = mp.mpf(-40); t0 = mp.e**lt0
    def inner(xi):
        A = 1 - xi/xB; hh = 1/A
        def f(lt):
            t = mp.e**lt
            a = A + t/(1 - xi); b2 = 4*t
            r = mp.sqrt(a**2 - b2)
            hav = 2/(a + r)*mp.hyp2f1(1, e, 2 - e, (a - r)/(a + r))
            return t**(-e)*(hav - hh)
        c1 = -1/((1 - xi)*A**2) + 2/((2 - e)*A**3)
        tail = c1*t0**(1 - e)/(1 - e)
        return (1 - xi)*(mp.quad(f, [lt0, -20, -6, -2, 0, 2, 6, mp.inf]) + tail)
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - e)

def CH_cov_report(e):
    """whole-integrand parametric value, form of the round-2 report"""
    def f1(x2, s):
        x3 = (1 - x2)*s; x1 = (1 - x2)*(1 - s)
        return (1 - x2)*(x3*(x1 + x2*c))**(-e)/(1 - x2/xB)
    def f2(x2, s):
        x3 = (1 - x2)*s; x1 = (1 - x2)*(1 - s)
        return (1 - x2)*x1*x3**(-e)*(x1 + x2*c)**(-1 - e)/(1 - x2/xB)
    I1 = mp.quad(f1, [0, mp.mpf(1)/2, 1], [0, mp.mpf(1)/2, 1]); I2 = mp.quad(f2, [0, mp.mpf(1)/2, 1], [0, mp.mpf(1)/2, 1])
    return -mp.gamma(e)*I1 + 2*mp.gamma(1 + e)*I2
def CH_cov_r31(e):
    """whole-integrand parametric value, independent form of review r3_1"""
    def f(x2, s):
        x3 = (1 - x2)*s; x1 = (1 - x2)*(1 - s)
        a = x3*(x1 + x2*c); bp = 1 - x2/xB
        return (1 - x2)*x1*((2*e - 2)*a**(-e)/(e*bp) + x3*a**(-1 - e)/bp - a**(-e)/(e*bp**2))
    return mp.gamma(1 + e)*mp.quad(f, [0, mp.mpf(1)/2, 1], [0, mp.mpf(1)/2, 1])
def THGamma_cov(e):
    """covariant parametric value of T_H Gamma (massless on-shell target), absolutely convergent for -1 < eps < 0;
    x3 = (1-x2) s, x1 = (1-x2)(1-s); the endpoint factor s^{-1-eps} is removed by s = sigma^{-1/eps}"""
    def f(x2, sg):
        sv = sg**(-1/e)
        return (1 - x2)**(1 - e)*(1 - sv)*((1 - x2)*(1 - sv) + x2*c)**(-1 - e)/(-e)
    return mp.gamma(1 + e)*mp.quad(f, [0, mp.mpf(1)/2, 1], [0, mp.mpf(1)/2, 1])

print("(2) simplex identity T(eps) = B(-eps,2-eps) int y (c+y(1-c))^{-1-eps} (x = 2):")
for es in ['-0.6', '-0.3', '0.1', '0.2', '0.3', '0.45']:
    e = mp.mpf(es)
    rhs = closed(e)/mp.gamma(1 + e)
    ts, tx = T_square(e), T_simplex(e)
    print(f"   eps={es:>5}: T(square) = {mp.nstr(ts, 25)}  T(simplex) rel.dev {mp.nstr(abs(tx/ts - 1), 3)}  closed rel.dev {mp.nstr(abs(ts/rhs - 1), 3)}", flush=True)
print("   closed form of the y-integral vs quadrature:", mp.nstr(abs(closed(mp.mpf('0.2'))/closed_int(mp.mpf('0.2')) - 1), 3))
print("(3) covariant T_H Gamma (massless target), -1 < eps < 0, vs closed form:")
for es in ['-0.6', '-0.3', '-0.1']:
    e = mp.mpf(es)
    print(f"   eps={es}: cov {mp.nstr(THGamma_cov(e), 22)}  closed {mp.nstr(closed(e), 22)}  rel.dev {mp.nstr(abs(THGamma_cov(e)/closed(e) - 1), 3)}", flush=True)
print("(4) whole-integrand parametric C_H (two independent forms) vs closed form:")
for es in ['-0.3', '0.1', '0.2', '0.3']:
    e = mp.mpf(es)
    cl = closed(e); a1 = CH_cov_report(e); a2 = CH_cov_r31(e)
    print(f"   eps={es:>4}: closed {mp.nstr(cl, 22)}  report-form rel.dev {mp.nstr(abs(a1/cl - 1), 3)}  r3_1-form rel.dev {mp.nstr(abs(a2/cl - 1), 3)}", flush=True)
print("(5) fibered 2D quadrature without the t-cut vs closed form:")
for es in ['0.1', '0.2', '0.3']:
    e = mp.mpf(es)
    fb = CH_fibered(e); cl = closed(e)
    print(f"   eps={es}: fibered {mp.nstr(fb, 22)}  closed {mp.nstr(cl, 22)}  rel.dev {mp.nstr(abs(fb/cl - 1), 3)};"
          f"  round-2 cut estimate e^(-40(1-eps)) = {mp.nstr(mp.e**(-40*(1 - e)), 3)}", flush=True)
