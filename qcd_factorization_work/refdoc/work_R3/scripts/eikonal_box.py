# Two-gluon exchange between two infinite timelike Wilson lines v_A, v_B (rapidity difference Y),
# after the delta(v_A.K) delta(v_B.K) of the infinite lines. At fixed transverse momenta
# (a = k_T^2 + m^2, b = (K-k)_T^2 + m^2) the longitudinal integrals are
#   J_box   = Int dxA dxB [i/(xA+i0)] [i/(-xB+i0)] g(Q),   J_cross = Int ... [i/(xA+i0)] [i/(xB+i0)] g(Q)
#   g = 1/((Q-a+i0)(Q-b+i0)),  Q = k_par^2 = (-(xA^2+xB^2) + 2 cosh Y xA xB)/sinh^2 Y,  measure dk0 dk3 = dxA dxB / sinh Y
# Strict Glauber approximation (symmetric cutoff) gives J_box = J_cross = (J_box+J_cross)/2.
# Question: what does the exact eikonal integral give?  Unitarity at O(g^4) needs Re J_cross = 0.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
def roots(xA, a, Y):
    R = mp.sqrt(xA**2 - a + 1j*mp.mpf('1e-40'))   # principal branch => Im R >= 0
    if mp.im(R) < 0: R = -R
    xp = mp.cosh(Y)*xA + mp.sinh(Y)*R
    xm = mp.cosh(Y)*xA - mp.sinh(Y)*R
    return R, xp, xm
def inner_cross(xA, a, b, Y):
    # Int dxB g(Q)/(xB+i0): close in UHP (poles x_+^a, x_+^b)
    Ra, xpa, xma = roots(xA, a, Y); Rb, xpb, xmb = roots(xA, b, Y)
    return -1j*mp.pi*mp.sinh(Y)/(a-b)*(1/(Ra*xpa) - 1/(Rb*xpb))
def inner_box(xA, a, b, Y):
    # Int dxB g(Q)/(-xB+i0): close in LHP (poles x_-^a, x_-^b)
    Ra, xpa, xma = roots(xA, a, Y); Rb, xpb, xmb = roots(xA, b, Y)
    return 1j*mp.pi*mp.sinh(Y)/(a-b)*(1/(Ra*xma) - 1/(Rb*xmb))
def J(inner, a, b, Y):
    # J = - Int dxA inner(xA)/(xA + i0) = -[PV Int inner/xA - i pi inner(0)]
    sa, sb = mp.sqrt(a), mp.sqrt(b)
    pts = sorted([mp.mpf(0), sa, sb, -sa, -sb])
    # PV: symmetrize  Int_0^inf [inner(x) - inner(-x)]/x dx
    f = lambda x: (inner(x,a,b,Y) - inner(-x,a,b,Y))/x
    brk = [mp.mpf(0)] + sorted([sa, sb]) + [mp.inf]
    pv = mp.quad(f, brk)
    return -(pv - 1j*mp.pi*inner(mp.mpf(0),a,b,Y))
for (a,b,Y) in [(1.0,2.5,1.0),(1.0,2.5,3.0),(0.7,0.3,6.0),(1.3,1.31,2.0)]:
    a,b,Y = mp.mpf(a), mp.mpf(b), mp.mpf(Y)
    Jb = J(inner_box,a,b,Y); Jc = J(inner_cross,a,b,Y)
    S = 2*mp.pi**2/(a*b)
    print(f"a={float(a)}, b={float(b)}, Y={float(Y)}:")
    print(f"   J_box   = {mp.nstr(Jb,12)}")
    print(f"   J_cross = {mp.nstr(Jc,12)}")
    print(f"   J_box+J_cross = {mp.nstr(Jb+Jc,12)}   expected 2 pi^2/(ab) = {mp.nstr(S,12)}")
    print(f"   Re J_cross = {mp.nstr(mp.re(Jc),6)} ;  Re J_box/(2pi^2/ab) = {mp.nstr(mp.re(Jb)/S,12)} ; Im J_box = -Im J_cross ? {mp.nstr(mp.im(Jb)+mp.im(Jc),6)}")
