"""X2 fix round 2 / r2_ladder1_identification.py -- identification of the fibered and covariant values of the Collins
terms of the one-rung DIS ladder in (M2), d = 6 - 2 eps, measure mu^{2eps} int d^dk/(i pi^{d/2}) (O11 upgrade).

Gamma = S(k)^2 R(p-k) H0(k),  S = 1/(-k^2), R = 1/(-(p-k)^2), H0 = 1/(-(k+q)^2) = 1/(Q^2 - 2k.q - k^2), q+ = 0, x > 1.
C_R1 = S^2 R(p-k) Hhat,  Hhat = 1/(Q^2 - 2 n.k), n = (0, q-, 0_T)   (hard factor at k^ = (k+, 0, 0_T)).
C_H  = S^2 R(p^-k) (H0 - Hhat) = S^2 R(p^-k) (k^2 + 2 k.q_perp) H0 Hhat,  p^ = (p+, 0, 0_T),  q_perp = (0, 0, q_T).
Fibered (rung on shell, k- residue):  (1/Gamma(2-eps)) int_0^1 dxi/(1-xi) int_0^oo dt t^{1-eps} [H]/v^2 ,  t = |k_T|^2,
   with the S^{3-2eps} average <1/(a + b cos)> = (1/a) 2F1(1/2, 1; 2-eps; b^2/a^2)
   = 2/(a + r) 2F1(1, eps; 2-eps; (a-r)/(a+r)), r = sqrt(a^2 - b^2) (quadratic transformation; = S^3 closed form at eps=0).
(1) C_R1: both sides in closed form:  Gamma(eps) int_0^1 dxi (1-xi)^{1-eps} (xi m2)^{-eps} / (Q^2 (1 - xi/x))  [exact];
    numerical cross-checks of the fibered 2D integral and of the covariant parametric integral before the lambda-integral.
(2) C_H: covariant parametric representation of the WHOLE integrand (numerator included):
      C_H = -Gamma(eps) Q^{-2-2eps} int_simplex [x3(x1 + x2 c_x)]^{-eps}/(1 - x2/x)
            + 2 Gamma(1+eps) Q^{-2-2eps} int_simplex x1 x3^{-eps} (x1 + x2 c_x)^{-1-eps}/(1 - x2/x)
    vs the fibered 2D integral (numerical)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 25
xB = mp.mpf(2); Q2 = mp.mpf(1); cx = 1 - 1/xB

def CR1_closed(m2, e):
    return mp.gamma(e)*mp.quad(lambda xi: (1 - xi)**(1 - e)*(xi*m2)**(-e)/(Q2*(1 - xi/xB)), [0, mp.mpf(1)/2, 1])
def CR1_fibered(m2, e):
    def inner(xi):
        v = lambda t: xi*m2 + t/(1 - xi)
        f = lambda lt: mp.e**(lt*(2 - e))/v(mp.e**lt)**2          # t^{1-eps} dt = t^{2-eps} dlog t
        return mp.quad(f, [-mp.inf, mp.log(xi*m2*(1 - xi)) - 5, mp.log(xi*m2*(1 - xi)) + 5, mp.inf])/(1 - xi)/(Q2*(1 - xi/xB))
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - e)
def CR1_cov_param(m2, e):
    # Gamma(1+eps) int_0^1 dy y int_0^oo dl Delta^{-1-eps},  Delta = y(1-y) m2 + l Q^2 (1 - (1-y)/x)
    f = lambda y: y*mp.quad(lambda ll: (y*(1 - y)*m2 + mp.e**ll*Q2*(1 - (1 - y)/xB))**(-1 - e)*mp.e**ll, [-mp.inf, -5, 0, 5, mp.inf])
    return mp.gamma(1 + e)*mp.quad(f, [0, mp.mpf(1)/2, 1])

def CH_fibered(e):
    def inner(xi):
        A = Q2*(1 - xi/xB); hh = 1/A
        def f(lt):
            t = mp.e**lt
            a = A + t/(1 - xi); b2 = 4*t*Q2
            # S^{3-2eps} average via the quadratic transformation (stable as b -> a):
            # (1/a) 2F1(1/2,1;2-eps;b^2/a^2) = 2/(a+r) 2F1(1, eps; 2-eps; (a-r)/(a+r)),  r = sqrt(a^2-b^2)
            r = mp.sqrt(a**2 - b2)
            hav = 2/(a + r)*mp.hyp2f1(1, e, 2 - e, (a - r)/(a + r))
            return t**(-e)*(hav - hh)                          # t^{-1-eps} dt = t^{-eps} dlog t
        # the integrand is O(t^{1-eps}) as t -> 0 but <h0> - hhat suffers cancellation there: cut at t = e^{-40}
        # (neglected part O(e^{-40(1-eps)}) < 1e-15)
        return (1 - xi)*mp.quad(f, [-40, -20, -6, -2, 0, 2, 6, mp.inf])
    return mp.quad(inner, [0, mp.mpf(1)/2, 1])/mp.gamma(2 - e)
def CH_cov(e):
    # simplex x1 + x2 + x3 = 1: parametrize x2 in (0,1), x3 = (1-x2) s, x1 = (1-x2)(1-s), Jacobian (1-x2)
    def f1(x2, s):
        x3 = (1 - x2)*s; x1 = (1 - x2)*(1 - s)
        return (1 - x2)*(x3*(x1 + x2*cx))**(-e)/(1 - x2/xB)
    def f2(x2, s):
        x3 = (1 - x2)*s; x1 = (1 - x2)*(1 - s)
        return (1 - x2)*x1*x3**(-e)*(x1 + x2*cx)**(-1 - e)/(1 - x2/xB)
    I1 = mp.quad(f1, [0, 1], [0, 1]); I2 = mp.quad(f2, [0, mp.mpf(1)/2, 1], [0, mp.mpf(1)/2, 1])
    return (-mp.gamma(e)*I1 + 2*mp.gamma(1 + e)*I2)*Q2**(-1 - e)

print("(1) C_R1 of the one-rung ladder (x = 2, Q = 1):")
for m2, e in [(mp.mpf('1e-2'), mp.mpf('0.1')), (mp.mpf('1e-3'), mp.mpf('0.3'))]:
    c = CR1_closed(m2, e); fb = CR1_fibered(m2, e); cv = CR1_cov_param(m2, e)
    print(f"   m2={mp.nstr(m2,2)} eps={mp.nstr(e,2)}: closed {mp.nstr(c, 16)}  fibered 2D rel.dev {mp.nstr(abs(fb/c - 1), 3)}  covariant parametric rel.dev {mp.nstr(abs(cv/c - 1), 3)}", flush=True)
print("(2) C_H of the one-rung ladder (m-independent):")
for (aa, bb, ee) in [(mp.mpf(1), mp.mpf('0.5'), mp.mpf('0.1')), (mp.mpf(1), mp.mpf('0.999'), mp.mpf('0.3'))]:
    direct = mp.quad(lambda c: (1 - c**2)**(mp.mpf(1)/2 - ee)/(aa + bb*c), [-1, 0, 1])/mp.beta(mp.mpf(1)/2, mp.mpf(3)/2 - ee)
    rr = mp.sqrt(aa**2 - bb**2)
    print(f"   check of the S^(3-2eps) average a={aa} b={bb} eps={ee}: direct {mp.nstr(direct, 15)}  formula {mp.nstr(2/(aa + rr)*mp.hyp2f1(1, ee, 2 - ee, (aa - rr)/(aa + rr)), 15)}")
for e in [mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.3')]:
    fb = CH_fibered(e); cv = CH_cov(e)
    print(f"   eps={mp.nstr(e,2)}: fibered {mp.nstr(fb, 15)}   covariant (whole-integrand parametric) {mp.nstr(cv, 15)}   rel.dev {mp.nstr(abs(fb/cv - 1), 3)}", flush=True)
