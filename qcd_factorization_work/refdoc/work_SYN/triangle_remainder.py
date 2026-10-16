"""Synthesizer check (REFDOC_ANALYSIS S30, ERR-m25).
One-loop off-shell scalar triangle, massless internal lines, p1^2=p2^2=-m^2,
p1=(P,-m^2/(2P),0_T), p2=(m^2/(2P'),-P',0_T), Qt^2=2PP', Q^2=-(p1+p2)^2=(Qt^2+m^2)^2/Qt^2.
Exact: Q^2 I = Phi1(t,t) (Usyukina-Davydychev), t=m^2/Q^2.
Sum of Collins subtraction terms at eps->0 (reference eq. (D.32)): Qt^-2 [ln^2(Qt^2/m^2)+pi^2/3].
Claims checked:
 (1) R6 value of the remainder at m^2=0.02, P=0.8, P'=1.3: -0.0173434339581;
 (2) Q^2 I = L^2+pi^2/3 + t(2L^2-4L-4+2pi^2/3) + t^2(6L^2-14L-11+2pi^2) + O(t^3 L^2), L=ln(Q^2/m^2);
 (3) Q^2 (I - D32) = -4t + t^2 (L^2-15+pi^2/3) + O(t^3 L^2): no logarithm at NLP.
"""
from mpmath import mp, mpf, polylog, log, sqrt, pi, quad
mp.dps = 50
def Phi1(t):
    rho = 2/(1-2*t+sqrt(1-4*t))
    return (4*polylog(2,-rho*t)+log(rho*t)**2+pi**2/3)/sqrt(1-4*t)
def I_direct(t):
    return quad(lambda u: log(u*(1-u)/t)/(u*(1-u)-t), [0, mpf(1)/2, 1])
ok = True
for t in [mpf('0.1'), mpf('0.01'), mpf('1e-4')]:
    d = abs(Phi1(t)-I_direct(t))
    print("closed form vs 1D integral, t=%s: |diff|=%s" % (t, mp.nstr(d,3))); ok &= d < mpf('1e-30')
def remainder_Qt(Qt2, m2):
    Q2 = (Qt2+m2)**2/Qt2; t = m2/Q2
    return Phi1(t)/Q2 - (log(Qt2/m2)**2+pi**2/3)/Qt2, Q2, t
r, Q2, t = remainder_Qt(2*mpf('0.8')*mpf('1.3'), mpf('0.02'))
print("(1) remainder at R6 point:", mp.nstr(r,15), " (R6: -0.0173434339581)"); ok &= abs(r-mpf('-0.0173434339581')) < mpf('1e-12')
print("(2),(3) expansions:")
for k in [6, 8, 10, 12, 14]:
    t = mpf(10)**(-k); L = log(1/t); Q2 = mpf(1); m2 = t
    I = Phi1(t)
    nnlp = (I - L**2 - pi**2/3 - t*(2*L**2-4*L-4+2*pi**2/3))/t**2 - (6*L**2-14*L-11+2*pi**2)
    # remainder as a function of t: Qt2 from Q2=(Qt2+m2)^2/Qt2 with Q2=1
    s = 2*t/(1-2*t+sqrt(1-4*t))     # s=m2/Qt2: small root of t=s/(1+s)^2 (numerically stable form)
    Qt2 = m2/s
    rem = I - (log(Qt2/m2)**2+pi**2/3)/Qt2
    c2 = (rem + 4*t)/t**2 - (L**2-15+pi**2/3)
    print("  t=1e-%d: NNLP(I) residual/t = %s ; remainder: Q^2 r/t = %s ; t^2-coefficient residual = %s" % (k, mp.nstr(nnlp/(t*L**2),4), mp.nstr(rem/t,16), mp.nstr(c2/(t*L**2),4)))
    ok &= abs(nnlp) < 100*t*L**2 and abs(c2) < 100*t*L**2
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
