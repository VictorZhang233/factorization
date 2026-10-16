# Stage-2 independent check of claim E01 (hybrid kernel delta term).
# Method: Lorentzian test functions phi(u) = R^2/(R^2+(u-u0)^2), whose Fourier transform is
# Phi(lam) = int du e^{i u lam} phi(u) = pi R e^{-R|lam|} e^{i u0 lam}.  Exact pairing of the
# distribution G(u) = int dlam/(2pi) e^{i u lam} g(lam), g = ln(lam^2/lamS^2) theta(|lam|-lamS):
#   <G,phi> = int dlam/(2pi) g(lam) Phi(lam) = 2R Re[ E1((R - i u0) lamS) / (R - i u0) ]   (closed form)
# compared with (a) printed prescription (NPB 964 eqs. (33)-(34)), (b) plus distribution on R.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30

def G_pw(u, lS):
    # pointwise transform for u != 0 (to be verified separately)
    return -1/abs(u) + 2*mp.si(u*lS)/(mp.pi*u)

def exact_pair(R, u0, lS):
    w = mp.mpc(R, -u0)
    return 2*R*mp.re(mp.e1(w*lS)/w)

def exact_pair_direct(R, u0, lS):
    # same, by direct numerical lambda integration (check of closed form)
    f = lambda lam: 2*mp.log(lam/lS)*mp.e**(-R*lam)*mp.cos(u0*lam)
    return (R/2)*2*mp.quad(f, [lS, lS+1, lS+10, mp.inf])

def phi(u, R, u0):
    return R**2/(R**2+(u-u0)**2)

def printed_pair(R, u0, lS):
    # -<1/|u|_+, phi> + <2Si(u lS)/(pi u), phi>, with
    # <1/|u|_+, phi> = lim_{b->0} [ int_{|u|>b} phi/|u| + 2 phi(0) ln b ]
    #               = int_{|u|<1} (phi(u)-phi(0))/|u| + int_{|u|>1} phi/|u|
    p0 = phi(0, R, u0)
    A = mp.quad(lambda u: (phi(u, R, u0)+phi(-u, R, u0)-2*p0)/u, [0, 1]) \
        + mp.quad(lambda u: (phi(u, R, u0)+phi(-u, R, u0))/u, [1, 10, 100, mp.inf])
    B = mp.quad(lambda u: 2*mp.si(u*lS)/(mp.pi*u)*(phi(u, R, u0)+phi(-u, R, u0)), [0, 1, 10, 100, 1000, mp.inf])
    return -A + B

def plusR_pair(R, u0, lS):
    # plus distribution on the whole real line: int du G_pw(u) (phi(u) - phi(0))
    p0 = phi(0, R, u0)
    f = lambda u: G_pw(u, lS)*(phi(u, R, u0)+phi(-u, R, u0)-2*p0)
    pts = [mp.mpf(0)] + [mp.mpf(k)*mp.pi/lS for k in range(1, 400)]
    s = mp.quad(f, pts)
    # tail beyond last point: G_pw ~ -2cos(u lS)/(pi lS u^2) + O(u^-3); integrate tail numerically with quadosc
    s += mp.quadosc(f, [pts[-1], mp.inf], omega=lS)
    return s

print("A. pointwise transform: Abel-regularized direct integral vs -1/|u| + 2Si(u lS)/(pi u)")
for lS in [mp.mpf('0.5'), mp.mpf(1), mp.mpf('3.7')]:
    for u in [mp.mpf('0.3'), mp.mpf('-1.7'), mp.mpf('5')]:
        eps = mp.mpf('1e-8')
        # (2/pi) int_lS^inf cos(u lam) ln(lam/lS) e^{-eps lam} dlam, computed by quadosc
        val = (2/mp.pi)*mp.quadosc(lambda lam: mp.cos(u*lam)*mp.log(lam/lS)*mp.e**(-eps*lam), [lS, mp.inf], omega=abs(u))
        print("  lS=%s u=%s  direct=%s  formula=%s" % (lS, u, mp.nstr(val, 12), mp.nstr(G_pw(u, lS), 12)))

print("B. closed form exact pairing vs direct lambda integral")
for (R, u0, lS) in [(1, 0, 1), (2, 0.7, 0.5), (0.5, -1.3, 3.7)]:
    R, u0, lS = mp.mpf(R), mp.mpf(u0), mp.mpf(lS)
    print("  ", mp.nstr(exact_pair(R, u0, lS), 15), mp.nstr(exact_pair_direct(R, u0, lS), 15))

print("C. printed - exact  vs  2 ln(lS e^gammaE) phi(0) ; plus-on-R - exact")
for (R, u0, lS) in [(1, 0, 1), (2, 0.7, 0.5), (0.5, -1.3, 3.7), (3, 2.0, 2.0), (1, 0, 0.2)]:
    R, u0, lS = mp.mpf(R), mp.mpf(u0), mp.mpf(lS)
    ex = exact_pair(R, u0, lS)
    pr = printed_pair(R, u0, lS)
    pl = plusR_pair(R, u0, lS)
    pred = 2*mp.log(lS*mp.e**mp.euler)*phi(0, R, u0)
    print("  R=%s u0=%s lS=%s: exact=%s printed-exact=%s predicted=%s ratio=%s | plusR-exact=%s" % (
        R, u0, lS, mp.nstr(ex, 12), mp.nstr(pr-ex, 12), mp.nstr(pred, 12), mp.nstr((pr-ex)/pred, 12), mp.nstr(pl-ex, 5)))

print("D. analytic: <1/|u|_+, R^2/(R^2+u^2)> = 2 ln R and (4/pi) int_0^inf Si(lS u)/(u(1+u^2/R^2)) du = 2[E1(lS R)+ln(lS R)+gammaE]")
for (R, lS) in [(1, 1), (5, 0.5), (0.3, 2)]:
    R, lS = mp.mpf(R), mp.mpf(lS)
    A = mp.quad(lambda u: (2*phi(u, R, 0)-2)/u, [0, 1]) + mp.quad(lambda u: 2*phi(u, R, 0)/u, [1, mp.inf])
    B = mp.quad(lambda u: 4*mp.si(lS*u)/(mp.pi*u)*phi(u, R, 0), [0, 1, 10, 100, 1000, mp.inf])
    print("  R=%s lS=%s  A=%s (2lnR=%s)  B=%s (pred=%s)" % (R, lS, mp.nstr(A, 14), mp.nstr(2*mp.log(R), 14), mp.nstr(B, 14), mp.nstr(2*(mp.e1(lS*R)+mp.log(lS*R)+mp.euler), 14)))

print("E. integral of printed bracket over u in (-U,U), U->inf, vs 2 ln(lS e^gammaE)")
for lS in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(2)]:
    for U in [mp.mpf(100), mp.mpf(10000)]:
        # -int 1/|u|_+ over (-U,U) = -2 ln U ;  int 2Si(u lS)/(pi u) over (-U,U) = (4/pi) int_0^{U lS} Si(v)/v dv
        I = -2*mp.log(U) + (4/mp.pi)*mp.quad(lambda v: mp.si(v)/v, mp.linspace(0, U*lS, 200))
        print("  lS=%s U=%s  integral=%s  2ln(lS e^gE)=%s" % (lS, U, mp.nstr(I, 10), mp.nstr(2*mp.log(lS)+2*mp.euler, 10)))

a = 0.3*(4/3.)/(2*mp.pi)
print("F. size at lS=1: 3a*gammaE =", mp.nstr(3*a*mp.euler, 6), "(alpha_s=0.3);", mp.nstr(3*(0.25*(4/3.)/(2*mp.pi))*mp.euler, 6), "(alpha_s=0.25)")
