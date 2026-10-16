# -*- coding: utf-8 -*-
"""
n28_others.py -- independent checks for claim N28 (OTHERS 'checked transcriptions').
Run: python3 -I n28_others.py
Formulas were READ from the arXiv sources (2107.01212 BNS; 1912.08818 Liu-Neubert; 1607.04266 LUXqed; 1909.03886 Frixione;
2111.01170 Collins-Rogers-Sato) and re-derived here independently of frontier/others/scripts.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np, sympy as sp, mpmath as mp
from scipy import integrate

RES = []
def rep(name, ok, extra=''):
    RES.append(bool(ok)); print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)
mp.mp.dps = 30

# =============================================================== (i) BNS super-leading logarithms, singlet qq -> qq, forward
# BNS eq. (dsigma): sigma_n = (as/4pi)^{n+3} L^{2n+3} (-4)^n n!/(2n+3)! sum_r (2r)!/(4^r (r!)^2) C_rn
# BNS: C_rn^(S) = sigma_B 2^{8-r} pi^2 (4Nc)^n CF [ -J43 + 2 J2 (1 - delta_r0) ],  forward: J2 = J43/2 = DY
a_s, L, Nc, CF, DY, sB = sp.symbols('alpha_s L N_c C_F DeltaY sigma_B', positive=True)
def C_rn(r, n):
    J2 = DY; J43 = 2*DY
    return sB*2**(8 - r)*sp.pi**2*(4*Nc)**n*CF*(-J43 + 2*J2*(0 if r == 0 else 1))
def sigma_n(n):
    pre = (a_s/(4*sp.pi))**(n + 3)*L**(2*n + 3)*(-4)**n*sp.factorial(n)/sp.factorial(2*n + 3)
    return sp.simplify(pre*sum(sp.factorial(2*r)/(4**r*sp.factorial(r)**2)*C_rn(r, n) for r in range(n + 1)))
w = Nc*a_s*L**2/sp.pi
ok = True
for n in range(0, 13):
    term_closed = -sB*4*CF/(3*sp.pi)*a_s**3*L**3*DY*sp.rf(1, n)**2/(sp.rf(2, n)*sp.rf(sp.Rational(5, 2), n)*sp.factorial(n))*(-w)**n
    ok = ok and sp.simplify(sigma_n(n) - term_closed) == 0
rep('(i-a) BNS tower: sum_n sigma_n^SLL (their eqs. dsigma + C_rn^(S), forward) = -sigma_B (4CF/3pi) as^3 L^3 DY 2F2(1,1;2,5/2;-w), term by term n=0..12', ok)
s1 = sp.simplify(sigma_n(1))
rep('(i-b) first super-leading term n=1: sigma_B (4/(15 pi^2)) CF Nc as^4 L^5 DY', sp.simplify(s1 - sB*sp.Rational(4, 15)*CF*Nc*a_s**4*L**5*DY/sp.pi**2) == 0, '[%s]' % s1)
rep('(i-c) n=0 term is -sigma_B (4CF/3pi) as^3 L^3 DY (single-log, not super-leading)', sp.simplify(sigma_n(0) + sB*4*CF/(3*sp.pi)*a_s**3*L**3*DY) == 0)
# asymptotics: 2F2(1,1;2,5/2;-w) = (3/2)(ln w - psi(3/2))/w + ...  (Mellin-Barnes double pole at s=-1)
okA = True; txt = []
for wv in (1e4, 1e6, 1e8):
    f = mp.hyp2f2(1, 1, 2, mp.mpf(5)/2, -mp.mpf(wv))
    pred = mp.mpf(3)/2*(mp.log(wv) - mp.digamma(mp.mpf(3)/2))/wv
    okA = okA and abs(f/pred - 1) < 5e-3
    txt.append('w=%.0e: w*F/ln w = %s, F/pred-1 = %.1e' % (wv, mp.nstr(wv*f/mp.log(wv), 6), float(f/pred - 1)))
rep('(i-d) large w: 2F2(1,1;2,5/2;-w) ~ (3/2)(ln w - psi(3/2))/w, so w*2F2/ln w -> 3/2 (1.4970 at w=1e8)', okA, '; '.join(txt))

# =============================================================== (ii) Liu-Neubert LDL series, their eq. (3)
x = sp.Symbol('x')
ok = True
for n in range(0, 16):
    lhs = sp.factorial(n)/sp.factorial(2*n + 2)               # coefficient of (-C_F a_s Lhat^2/2pi)^n times Lhat^2
    rhs = sp.Rational(1, 2)*sp.rf(1, n)**2/(sp.rf(sp.Rational(3, 2), n)*sp.rf(2, n)*sp.factorial(n))*sp.Rational(1, 4)**n
    ok = ok and sp.simplify(lhs - rhs) == 0
rep('(ii-a) Lhat^2 sum_n n!/(2n+2)! (-CF as Lhat^2/2pi)^n = (Lhat^2/2) 2F2(1,1;3/2,2;-CF as Lhat^2/(8pi)), n=0..15 exact', ok)
rep('(ii-b) n=0,1 LDL terms = Lhat^2/2 and (CF as/4pi)(-Lhat^4/12) = leading logs of LN eq. (1): (L^2/2 - 2) + (CF as/4pi)(-L^4/12 - ...)',
    sp.factorial(0)/sp.factorial(2) == sp.Rational(1, 2) and sp.simplify(sp.factorial(1)/sp.factorial(4)*(-1/(2*sp.pi)) - (1/(4*sp.pi))*sp.Rational(-1, 12)) == 0)

# =============================================================== (iii) LUXqed (eq. 6) on a point-like Dirac target vs Frixione (4.189)
xx, mu2, m2, al, zz, Q2 = sp.symbols('x mu2 m2 alpha z Q2', positive=True)
# elastic point-like target: G_E = G_M = 1 -> F2 = delta(1-x'), F_L = (4 m^2/Q^2) delta(1-x'), x' = x/z.
# int_x^1 dz/z delta(1 - x/z) F(z) = F(x)  (the elastic delta sits at z = x and is counted fully, as in LUXqed)
zp = 1 + (1 - xx)**2
Qmin, Qmax = xx**2*m2/(1 - xx), mu2/(1 - xx)
F2part = sp.integrate((zp + 2*xx**2*m2/Q2)/Q2, (Q2, Qmin, Qmax))
FLpart = sp.integrate(-xx**2*(4*m2/Q2)/Q2, (Q2, Qmin, Qmax))
conv = -xx**2
xf = al/(2*sp.pi)*(F2part + FLpart + conv)                      # alpha(Q^2) = alpha fixed at this order
frix = al/(2*sp.pi)*zp*(sp.log(mu2/m2) - 2*sp.log(xx) - 1)       # Frixione (4.189), MSbar (K=0), times x
power = al*m2*xx**2*(1 - xx)/(sp.pi*mu2)
rep('(iii-a) LUXqed point-like limit = (alpha/2pi)[1+(1-x)^2][ln(mu^2/m^2) - 2 ln x - 1] + alpha m^2 x^2 (1-x)/(pi mu^2)',
    sp.simplify(sp.expand_log(xf - frix - power, force=True)) == 0)
rep('(iii-b) i.e. Frixione JHEP 11 (2019) 158 eq. (4.189) (x times Gamma_{gamma/e}^{[1]}, alpha/2pi normalisation) up to the O(m^2/mu^2) term',
    sp.limit(sp.simplify((xf - frix)), m2, 0) == 0)
noFL = al/(2*sp.pi)*(F2part + conv)
d_FL = sp.simplify(sp.expand_log(noFL - xf, force=True))
rep('(iii-c) dropping F_L shifts xf by (alpha/2pi) 4(1-x) at leading power', sp.simplify(sp.limit(d_FL, m2, 0) - al/(2*sp.pi)*4*(1 - xx)) == 0, '[%s]' % sp.factor(d_FL))
rep('(iii-d) dropping the MSbar conversion term -z^2 F2(x/z,mu^2) shifts xf by (alpha/2pi) x^2', sp.simplify(-al/(2*sp.pi)*conv - al*xx**2/(2*sp.pi)) == 0)

# =============================================================== (iv) CRS Yukawa quark-in-nucleon pdf: integrand from the trace, DR + MSbar
k_T2, xi, M, mq, ms = sp.symbols('k_T2 xi M m_q m_s', positive=True)
# light-front: P=(P+, M^2/2P+, 0), k^+ = xi P+, spectator scalar on shell: k^2 - mq^2 = -(kT^2 + Delta)/(1-xi)
Delta = xi*ms**2 + (1 - xi)*mq**2 - xi*(1 - xi)*M**2
k2 = mq**2 - (k_T2 + Delta)/(1 - xi)
pk = (M**2 + k2 - ms**2)/2                                      # p.k with (p-k)^2 = ms^2
N_over_Pplus = 2*xi*pk - k2 + 2*mq*M*xi + mq**2                  # (1/4)Tr[g+ (kslash+mq)(Pslash+M)(kslash+mq)] / P+
rep('(iv-a) Dirac trace (1/4)Tr[gamma^+ (k+m_q)(P+M)(k+m_q)] = P^+ [k_T^2 + (m_q + xi M)^2] on the scalar mass shell',
    sp.simplify(N_over_Pplus - (k_T2 + (mq + xi*M)**2)) == 0)
# f(xi) = |lambda|^2 (1/(2(1-xi)P+)) (2pi)/(2pi)^4 int d^2kT  N (1-xi)^2/(kT^2+Delta)^2  = a_lambda (1-xi) int dkT^2 [kT^2+(mq+xi M)^2]/(kT^2+Delta)^2
lam2 = sp.Symbol('lambda2', positive=True)
pref = lam2/(2*(1 - xi))*(2*sp.pi)/(2*sp.pi)**4*sp.pi*(1 - xi)**2   # d^2kT = pi dkT^2; P+ cancels against N
rep('(iv-b) normalisation: prefactor = a_lambda (1-xi) with a_lambda = lambda^2/(16 pi^2)  (CRS eq. (58) integrand)',
    sp.simplify(pref - lam2/(16*sp.pi**2)*(1 - xi)) == 0)
# DR: int_0^inf dt t^{-e} (t + c)/(t + D)^2 = Gamma(e)Gamma(1-e) D^{-e} + (c/D - 1) D^{-e} Gamma(1-e)Gamma(1+e)
e = sp.Symbol('e', positive=True); cc, DD = sp.symbols('c D', positive=True)
dr = sp.gamma(e)*sp.gamma(1 - e)*DD**(-e) + (cc/DD - 1)*DD**(-e)*sp.gamma(1 - e)*sp.gamma(1 + e)
ser = sp.series(dr, e, 0, 1).removeO()
rep('(iv-c) DR integral = 1/e + [ -ln D - 1 + c/D ] + O(e): MSbar finite part ln(mu^2/Delta) - 1 + (m_q + xi M)^2/Delta (CRS eq. (55))',
    sp.simplify(ser - (1/e - sp.log(DD) - 1 + cc/DD)) == 0, '[%s]' % sp.simplify(ser))
# numerical check of the DR formula at e = 0.05 for sample values
cv, Dv, ev = 0.7, 0.4, 0.05
num = integrate.quad(lambda t: t**(-ev)*(t + cv)/(t + Dv)**2, 0, np.inf, limit=500)[0]
rep('(iv-d) numerical check of the DR integral at e=0.05', abs(num - float(dr.subs({e: ev, cc: cv, DD: Dv}))) < 1e-8, '(%.10f)' % num)
# sign structure: mq=0.3, M=1.0, ms=1.5 GeV
fq = lambda xv, muv: (1 - xv)*(np.log(muv**2/(xv*1.5**2 + (1 - xv)*0.09 - xv*(1 - xv))) - 1 + (0.3 + xv)**2/(xv*1.5**2 + (1 - xv)*0.09 - xv*(1 - xv)))
xs = np.linspace(0.01, 0.99, 99)
neg08 = [xv for xv in xs if fq(xv, 0.8) < 0]
rep('(iv-e) MSbar pdf negative at mu=0.8 GeV for xi in about [0.28, 0.98], positive for all xi at mu=2.5 GeV (m_q=0.3, M=1, m_s=1.5)',
    abs(min(neg08) - 0.28) < 0.011 and max(neg08) >= 0.97 and all(fq(xv, 2.5) > 0 for xv in xs), '(neg range %.2f-%.2f)' % (min(neg08), max(neg08)))

# =============================================================== (v) LO BK/BFKL eigenvalue
def chi_num(g):
    # (1/2pi) int d^2z r^2/((x-z)^2 (z-y)^2) [ ((x-z)^2)^g + ((z-y)^2)^g - (r^2)^g ],  r = |x-y| = 1, x=(0,0), y=(1,0)
    # plane = disk D_y={|z-y|<1/2} (polar around y)  U  complement (polar around x, angular range excluding D_y); symmetric in theta -> x2
    F = lambda a2, b2: (a2**g + b2**g - 1.0)/(a2*b2)
    def in_Dy():
        f = lambda rp: 2*rp*integrate.quad(lambda th: F(1 + rp*rp + 2*rp*np.cos(th), rp*rp), 0, np.pi, limit=200, epsabs=1e-13)[0]
        return integrate.quad(f, 0, 0.5, limit=400, epsabs=1e-12)[0]
    def out_Dy():
        def f(rho):
            c = (rho*rho + 0.75)/(2*rho)
            th0 = np.arccos(c) if c <= 1 else 0.0          # exclude theta in [0, th0) where |z-y| < 1/2
            return 2*rho*integrate.quad(lambda th: F(rho*rho, rho*rho + 1 - 2*rho*np.cos(th)), th0, np.pi, limit=200, epsabs=1e-13)[0]
        tot = 0.0
        for a_, b_ in [(0, 0.5), (0.5, 1.0), (1.0, 1.5), (1.5, 4), (4, 40)]:
            tot += integrate.quad(f, a_, b_, limit=400, epsabs=1e-12)[0]
        return tot + integrate.quad(f, 40, np.inf, limit=400)[0]
    return (in_Dy() + out_Dy())/(2*np.pi)
chi = lambda g: float(2*mp.digamma(1) - mp.digamma(g) - mp.digamma(1 - g))
okv = True; txt = []
for g in (0.5, 0.3, 0.7):
    cn = chi_num(g); okv = okv and abs(cn - chi(g)) < 1e-4; txt.append('g=%.1f: %.6f vs %.6f' % (g, cn, chi(g)))
rep('(v-a) dipole kernel on (r^2)^gamma: eigenvalue chi(gamma) = 2psi(1) - psi(gamma) - psi(1-gamma) (numerical, own code)', okv, '; '.join(txt))
rep('(v-b) chi(1/2) = 4 ln 2 exactly', sp.simplify(2*sp.polygamma(0, 1) - 2*sp.polygamma(0, sp.Rational(1, 2)) - 4*sp.log(2)) == 0)

print('\nSUMMARY n28: %d/%d PASS' % (sum(RES), len(RES)))
