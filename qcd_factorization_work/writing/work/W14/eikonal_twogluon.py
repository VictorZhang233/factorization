r"""W14 -- independent re-derivation of prop:dy-eikonal-twogluon (VF-REF-9, VF-REF-10).

Setting (our conventions): two infinite time-like Wilson lines v_A, v_B, v^2=1, v_A.v_B=cosh Y,
two gluons of mass m with exact Feynman-gauge propagators -i g/(k^2-m^2+i0), fixed transverse momenta.
x_A = v_A.k, x_B = v_B.k ; dk^0 dk^3 = dx_A dx_B / sinh Y ;
Q = k_par^2 = (2 cosh Y x_A x_B - x_A^2 - x_B^2)/sinh^2 Y ;  g(Q) = 1/((Q-a+i0)(Q-b+i0)).
J_box  = int dx_A dx_B [i/(x_A+i0)] [i/(-x_B+i0)] g ,
J_cross= int dx_A dx_B [i/(x_A+i0)] [i/( x_B+i0)] g .
Claims: J_box = 2 pi (pi + i Y)/(a b),  J_cross = -2 pi i Y/(a b).

Checks performed here (all independent of the R3 scripts):
 (1) kappa(Y) = int_R du / (sqrt(u^2-1+i0) (u^2+sinh^2 Y)) = (2Y - i pi)/(sinh Y cosh Y)   [closed form used in the text]
 (2) residue formulas for the inner x_B integral vs direct numerical x_B quadrature at finite i*eps
 (3) the outer x_A integral (PV + delta term) vs the closed forms
 (4) brute-force: finite eps in BOTH eikonal denominators and in g, iterated quadrature, extrapolated eps->0
 (5) colour factors c_box = X^2, c_cross = X^2 + C_A/2 X in explicit SU(2), SU(3) representations
 (6) normalization: A_2 = (1/2)(-i chi X)^2 + i (C_A Y/(4 pi)) chi^2 X  with chi(b) = g^2 coth Y K0(m b)/(2 pi),
     i.e. p_opp = -i Y/pi, and A_2 + A_2^dag + A_1^dag A_1 = 0 ; convolution identity checked numerically.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import numpy as np

mp.mp.dps = 30
LOG = []
def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s); LOG.append(s)

def sqrt_ip(x):
    # sqrt(x + i0) with Im >= 0 (principal branch, x real)
    return mp.sqrt(x) if x >= 0 else 1j*mp.sqrt(-x)

# ---------------- (1) kappa(Y)
def kappa_num(Y):
    s2 = mp.sinh(Y)**2
    f1 = lambda u: 1/(1j*mp.sqrt(1-u**2)*(u**2+s2))
    f2 = lambda u: 1/(mp.sqrt(u**2-1)*(u**2+s2))
    return 2*(mp.quad(f1, [0, 1]) + mp.quad(f2, [1, mp.inf]))
def kappa_cf(Y):
    return (2*Y - 1j*mp.pi)/(mp.sinh(Y)*mp.cosh(Y))
log('(1) kappa(Y): numeric vs closed form (2Y-i pi)/(sinh Y cosh Y)')
for Y in [mp.mpf('0.3'), mp.mpf(1), mp.mpf('2.5'), mp.mpf(5)]:
    kn, kc = kappa_num(Y), kappa_cf(Y)
    log('   Y=%s  num=%s  cf=%s  |diff|=%s' % (mp.nstr(Y,3), mp.nstr(kn,15), mp.nstr(kc,15), mp.nstr(abs(kn-kc),3)))

# ---------------- residue formulas
def xpm(xA, c, Y, sgn):
    R = sqrt_ip(xA**2 - c)
    return mp.cosh(Y)*xA + sgn*mp.sinh(Y)*R, R
def inner_cross_res(xA, a, b, Y):
    # int dx_B [1/(x_B+i0)] g  (spec normalization: WITHOUT the factor i of the eikonal propagator)
    xpa, Ra = xpm(xA, a, Y, +1); xpb, Rb = xpm(xA, b, Y, +1)
    return -1j*mp.pi*mp.sinh(Y)/(a-b)*(1/(Ra*xpa) - 1/(Rb*xpb))
def inner_box_res(xA, a, b, Y):
    # int dx_B [1/(-x_B+i0)] g
    xma, Ra = xpm(xA, a, Y, -1); xmb, Rb = xpm(xA, b, Y, -1)
    return 1j*mp.pi*mp.sinh(Y)/(a-b)*(1/(Ra*xma) - 1/(Rb*xmb))

def Qf(xA, xB, Y):
    return (2*mp.cosh(Y)*xA*xB - xA**2 - xB**2)/mp.sinh(Y)**2

# ---------------- (2) inner integral vs direct quadrature at finite eps (eikonal) and eta (gluon)
def inner_num(xA, a, b, Y, which, eps, eta):
    def f(xB):
        Q = Qf(xA, xB, Y)
        g = 1/((Q - a + 1j*eta)*(Q - b + 1j*eta))
        e = 1/(xB + 1j*eps) if which == 'cross' else 1/(-xB + 1j*eps)
        return e*g
    # break points near the poles in x_B
    pts = [-mp.inf]
    cand = [0]
    for c in (a, b):
        for sg in (+1, -1):
            xp, R = xpm(xA, c, Y, sg)
            cand.append(mp.re(xp))
    for c in sorted(cand):
        pts.append(c)
    pts.append(mp.inf)
    return mp.quad(f, pts, maxdegree=10)

a0, b0, Y0 = mp.mpf('1.3'), mp.mpf('0.7'), mp.mpf('1.1')
log('(2) inner x_B integral: residue formula vs direct quadrature (eps=eta=1e-7), a=%s b=%s Y=%s' % (a0, b0, Y0))
for xA in [mp.mpf('-2.1'), mp.mpf('-0.4'), mp.mpf('0.25'), mp.mpf('0.9'), mp.mpf('1.7'), mp.mpf('3.3')]:
    for which in ('cross', 'box'):
        rn = inner_num(xA, a0, b0, Y0, which, mp.mpf('1e-7'), mp.mpf('1e-7'))
        rr = inner_cross_res(xA, a0, b0, Y0) if which == 'cross' else inner_box_res(xA, a0, b0, Y0)
        log('   xA=%5s %5s: quad=%s  res=%s  |d|=%s' % (mp.nstr(xA,3), which, mp.nstr(rn,12), mp.nstr(rr,12), mp.nstr(abs(rn-rr),2)))

# ---------------- (3) outer integral: J = -[PV int inner/x_A - i pi inner(0)]
def J_from_inner(inner, a, b, Y):
    # PV integral: symmetrize f(x)/x -> (f(x)-f(-x))/x on (0,inf)
    def h(x):
        return (inner(x, a, b, Y) - inner(-x, a, b, Y))/x
    # integrable singularities (square-root) at x=sqrt(a), sqrt(b)
    pts = sorted(set([mp.mpf(0), mp.sqrt(b), mp.sqrt(a), 2*mp.sqrt(max(a, b))]))
    pv = mp.quad(h, pts + [mp.inf])
    return -(pv - 1j*mp.pi*inner(mp.mpf(0), a, b, Y))
log('(3) J from the residue form (outer x_A integral done numerically) vs closed forms')
maxdev = 0
for (a, b, Y) in [(mp.mpf('1.3'), mp.mpf('0.7'), mp.mpf('1.1')), (mp.mpf('0.5'), mp.mpf('2.0'), mp.mpf('0.3')),
                  (mp.mpf('1.0'), mp.mpf('1.7'), mp.mpf('3.0')), (mp.mpf('4.0'), mp.mpf('0.2'), mp.mpf('6.0'))]:
    Jc = J_from_inner(inner_cross_res, a, b, Y)
    Jb = J_from_inner(inner_box_res, a, b, Y)
    Jc0 = -2j*mp.pi*Y/(a*b); Jb0 = 2*mp.pi*(mp.pi + 1j*Y)/(a*b)
    dev = max(abs(Jc-Jc0)/abs(Jc0), abs(Jb-Jb0)/abs(Jb0)); maxdev = max(maxdev, dev)
    log('   a=%s b=%s Y=%s: Jcross=%s (cf %s)  Jbox=%s (cf %s)  rel.dev=%s' % (mp.nstr(a,4), mp.nstr(b,5), mp.nstr(Y,3),
        mp.nstr(Jc,12), mp.nstr(Jc0,12), mp.nstr(Jb,12), mp.nstr(Jb0,12), mp.nstr(dev,2)))
log('   max rel. deviation (3):', mp.nstr(maxdev, 3))

# ---------------- (4) brute force with finite eps in all denominators (scipy, double precision), eps -> 0
from scipy import integrate
import math, cmath
def J_brute_sp(which, a, b, Y, eps):
    ch, sh = math.cosh(Y), math.sinh(Y)
    def g(xA, xB):
        Q = (2*ch*xA*xB - xA*xA - xB*xB)/sh**2
        return 1/((Q - a + 1j*eps)*(Q - b + 1j*eps))
    def inner(xA, part):
        e = (lambda xB: 1/(xB + 1j*eps)) if which == 'cross' else (lambda xB: 1/(-xB + 1j*eps))
        f = lambda xB: (e(xB)*g(xA, xB)).real if part == 0 else (e(xB)*g(xA, xB)).imag
        pts = [0.0]
        for c in (a, b):
            disc = xA*xA - c
            if disc >= 0:
                r = math.sqrt(disc)
                pts += [ch*xA + sh*r, ch*xA - sh*r]
            else:
                pts += [ch*xA]
        lo, hi = min(pts) - 50, max(pts) + 50
        v1 = integrate.quad(f, lo, hi, points=sorted(set(pts)), limit=800, epsabs=1e-11, epsrel=1e-10)[0]
        v2 = integrate.quad(f, hi, math.inf, limit=200, epsabs=1e-12)[0] + integrate.quad(f, -math.inf, lo, limit=200, epsabs=1e-12)[0]
        return v1 + v2
    def outer(part):
        def h(xA):
            I = inner(xA, 0) + 1j*inner(xA, 1)
            val = -I/(xA + 1j*eps)
            return val.real if part == 0 else val.imag
        pts = sorted(set([0.0, math.sqrt(a), -math.sqrt(a), math.sqrt(b), -math.sqrt(b)]))
        L = 60.0
        v = integrate.quad(h, -L, L, points=pts, limit=800, epsabs=1e-10, epsrel=1e-9)[0]
        v += integrate.quad(h, L, math.inf, limit=200)[0] + integrate.quad(h, -math.inf, -L, limit=200)[0]
        return v
    return outer(0) + 1j*outer(1)
log('(4) brute force (scipy): finite eps in eikonal and gluon denominators, a=1.3 b=0.7 Y=1.1')
a_, b_, Y_ = 1.3, 0.7, 1.1
res = {}
epss = [0.04, 0.02, 0.01]
for eps_ in epss:
    for which in ('cross', 'box'):
        res[(which, eps_)] = J_brute_sp(which, a_, b_, Y_, eps_)
        log('   eps=%.3f %5s: J=%s' % (eps_, which, res[(which, eps_)]))
for which, cf in (('cross', -2j*math.pi*Y_/(a_*b_)), ('box', 2*math.pi*(math.pi+1j*Y_)/(a_*b_))):
    r1, r2, r3 = (res[(which, e)] for e in epss)
    R12 = 2*r2 - r1; R23 = 2*r3 - r2; Rich = (4*R23 - R12)/3
    log('   %5s: Richardson eps->0: %s ; closed form %s ; rel.dev %.2e' % (which, Rich, cf, abs(Rich-cf)/abs(cf)))

# ---------------- (5) colour factors
def su2():
    s1 = np.array([[0,1],[1,0]],complex); s2 = np.array([[0,-1j],[1j,0]]); s3 = np.array([[1,0],[0,-1]],complex)
    return [s/2 for s in (s1,s2,s3)], 2
def su3():
    l = np.zeros((8,3,3),complex)
    l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j; l[2][0,0]=1; l[2][1,1]=-1
    l[3][0,2]=l[3][2,0]=1; l[4][0,2]=-1j; l[4][2,0]=1j; l[5][1,2]=l[5][2,1]=1; l[6][1,2]=-1j; l[6][2,1]=1j
    l[7]=np.diag([1,1,-2])/np.sqrt(3)
    return [x/2 for x in l], 3
def adjoint(T):
    n = len(T)
    f = np.zeros((n,n,n))
    for a_ in range(n):
        for b_ in range(n):
            comm = T[a_]@T[b_]-T[b_]@T[a_]
            for c_ in range(n):
                f[a_,b_,c_] = np.real(-2j*np.trace(comm@T[c_]))
    return [-1j*f[a_] for a_ in range(n)]
log('(5) colour factors: c_box = X^2, c_cross = X^2 + (C_A/2) X')
for name, (T, N) in (('SU(2)', su2()), ('SU(3)', su3())):
    F = adjoint(T); CA = N
    for repA, repB, lab in ((T, T, 'FxF'), (T, [-t.conj() for t in T], 'FxFbar'), (T, F, 'FxA'), (F, F, 'AxA')):
        dA, dB = repA[0].shape[0], repB[0].shape[0]
        X = sum(np.kron(repA[i], repB[i]) for i in range(len(T)))
        cbox = sum(np.kron(repA[i]@repA[j], repB[i]@repB[j]) for i in range(len(T)) for j in range(len(T)))
        ccross = sum(np.kron(repA[i]@repA[j], repB[j]@repB[i]) for i in range(len(T)) for j in range(len(T)))
        e1 = np.max(abs(cbox - X@X)); e2 = np.max(abs(ccross - X@X - CA/2*X))
        log('   %s %-6s: |c_box-X^2|=%.1e  |c_cross-X^2-CA/2 X|=%.1e' % (name, lab, e1, e2))

# ---------------- (6) normalization of A_1, A_2 and p_opp
# A_1 = -i chi X, chi = g^2 coth Y K0(m b)/(2 pi): check the 2D Fourier transform and the delta-function Jacobian
m_, bb = mp.mpf('0.8'), mp.mpf('1.3')
ft = mp.quadosc(lambda k: k*mp.besselj(0, k*bb)/(k**2+m_**2), [0, mp.inf], omega=bb)/(2*mp.pi)   # int d^2k/(2pi)^2 e^{ikb}/(k^2+m^2); oscillatory -> quadosc
log('(6a) int d^2k/(2pi)^2 e^{ik.b}/(k^2+m^2) = %s ; K0(mb)/(2pi) = %s' % (mp.nstr(ft,15), mp.nstr(mp.besselk(0,m_*bb)/(2*mp.pi),15)))
# convolution identity: FT_b[K0(mb)^2/(2pi)^2](K) = int d^2k/(2pi)^2 1/((k^2+m^2)((K-k)^2+m^2))
K = mp.mpf('0.9')
lhs = mp.quad(lambda r: r*mp.besselj(0, K*r)*(mp.besselk(0, m_*r)/(2*mp.pi))**2, [0, mp.inf])*2*mp.pi
def conv_integrand(k, phi):
    return k/((k**2+m_**2)*(K**2+k**2-2*K*k*mp.cos(phi)+m_**2))
rhs = mp.quad(conv_integrand, [0, mp.inf], [0, 2*mp.pi])/(2*mp.pi)**2
log('(6b) convolution identity: b-space %s ; k-space %s' % (mp.nstr(lhs,15), mp.nstr(rhs,15)))
# A_2 = -g^4 coth^2Y int d^2K/(2pi)^2 e^{iKb} int d^2k/(2pi)^4 [J_box X^2 + J_cross(X^2 + CA/2 X)]
#     = -(chi^2) * (1/(2 pi)) [pi X^2 - i Y CA/2 X]  =>  A_2 = -chi^2 X^2/2 + i (CA Y/(4 pi)) chi^2 X
# compare with (( -i chi)^2/2)[X^2 + p_opp CA/2 X]  =>  p_opp = -i Y/pi
import sympy as sp
chi, Ysym, CAs = sp.symbols('chi Y C_A', positive=True)
Xs = sp.Symbol('X')
popp = sp.Symbol('p')
A2 = -chi**2*Xs**2/2 + sp.I*CAs*Ysym/(4*sp.pi)*chi**2*Xs
sol = sp.solve(sp.Eq(sp.expand(A2), sp.expand((-sp.I*chi)**2/2*(Xs**2 + popp*CAs/2*Xs))), popp)
log('(6c) p_opp from the normalization:', sol)
A1 = -sp.I*chi*Xs
unit = sp.simplify(A2 + sp.conjugate(A2).subs(sp.conjugate(Xs), Xs) + sp.conjugate(A1).subs(sp.conjugate(Xs), Xs)*A1)
log('(6d) A_2 + A_2^dag + A_1^dag A_1 (X Hermitian, chi real) =', unit)
# strict window p_opp = 1/2 residual
A2s = (-sp.I*chi)**2/2*(Xs**2 + sp.Rational(1,2)*CAs/2*Xs)
log('(6e) strict window (p_opp=1/2): residual =', sp.simplify(A2s + sp.conjugate(A2s).subs(sp.conjugate(Xs), Xs) + chi**2*Xs**2))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs', 'eikonal_twogluon.log'), 'w').write('\n'.join(LOG) + '\n')
