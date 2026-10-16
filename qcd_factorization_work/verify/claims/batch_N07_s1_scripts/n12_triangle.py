#!/usr/bin/env python3
"""N12 independent check: one-loop off-shell triangle, Collins subtraction terms, exact remainder.

Own derivations (see report):
  * Feynman parameters: Q^2 I = int_simplex 1/(t x1(1-x1) + x2 x3) = int_0^1 du ln(u(1-u)/t)/(u(1-u)-t), t=m^2/Q^2.
  * Usyukina-Davydychev Phi^(1)(x,y) in its general (x,y) form, evaluated at x=y=t.
  * k^- residues of Gamma and of the four C_R Gamma (densities rho_X(k+,K), K=k_T^2), own code;
    d-dimensional values of int C_R Gamma at eps=0.3 by 2D quadrature with the K^{-eps}/Gamma(1-eps) measure,
    compared with (a); d=4 remainder density integrated and compared with I - (D.32).
  * exact closed form of the remainder in sigma = m^2/Qt^2 (derived here):
        int r = [4 Li2(-sigma) + sigma^2 (ln^2 sigma + pi^2/3)] / (Qt^2 (1 - sigma^2)),
    and its expansion in t.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
import sympy as sp

res = []
def rep(name, ok, extra=""):
    ok = bool(ok); res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + extra) if extra else ""))

mp.mp.dps = 40
def I_feyn(t):                      # Q^2 I from my Feynman-parameter derivation
    t = mp.mpf(t)
    def f(u):
        w = u*(1-u); d = (w-t)/t
        if abs(d) < mp.mpf('1e-12'):
            return (1 - d/2 + d*d/3)/t          # ln(1+d)/(t d) expanded
        return mp.log(w/t)/(w-t)
    # removable singularity where u(1-u)=t: split there
    u0 = (1-mp.sqrt(1-4*t))/2
    return 2*mp.quad(f, [0, u0, mp.mpf(1)/2])      # symmetric under u -> 1-u (avoids nodes rounding to u=1)
def Phi1(x, y):                     # Usyukina-Davydychev general form
    lam = mp.sqrt((1-x-y)**2-4*x*y); rho = 2/(1-x-y+lam)
    return (2*(mp.polylog(2, -rho*x)+mp.polylog(2, -rho*y)) + mp.log(y/x)*mp.log((1+rho*y)/(1+rho*x))
            + mp.log(rho*x)*mp.log(rho*y) + mp.pi**2/3)/lam
for tv in ['0.2', '0.05', '1e-3', '1e-6']:
    a = I_feyn(tv); b = Phi1(mp.mpf(tv), mp.mpf(tv))
    rep("Q^2 I: Feynman-parameter integral == UD Phi1(t,t), t=%s" % tv, abs(a-b) < mp.mpf('1e-30')*abs(b), mp.nstr(a, 20))
# asymmetric check of Phi1 against a direct 2D Feynman-parameter integral (x != y), to test the UD formula itself
def I2_feyn(x, y):   # Q^2 I with p1^2 = x Q^2, p2^2 = y Q^2 (Euclidean): Delta = x a1 a2 + y a1 a3 + a2 a3 ... (simplex)
    # Delta/Q^2 = x*x1*x2 + y*x1*x3 + x2*x3   (x1 joins the two lines adjacent to p1 and p2 appropriately)
    g = lambda r, u: 1/(x*(1-r)*r*u + y*(1-r)*r*(1-u) + r*r*u*(1-u)) * r
    return mp.quad(lambda r: mp.quad(lambda u: g(r, u), [0, 1]), [0, 1])
a = I2_feyn(mp.mpf('0.1'), mp.mpf('0.03')); b = Phi1(mp.mpf('0.1'), mp.mpf('0.03'))
rep("UD Phi1(x,y) == direct 2D Feynman-parameter integral for x=0.1,y=0.03", abs(a-b) < mp.mpf('1e-15')*abs(b), "%s vs %s" % (mp.nstr(a, 18), mp.nstr(b, 18)))

# ---------------- residue densities (own code) ----------------
mp.mp.dps = 25
def make(P, Pp, m2):
    P, Pp, m2 = mp.mpf(P), mp.mpf(Pp), mp.mpf(m2)
    a2 = m2/Pp
    def ksq(kp, km, K): return 2*kp*km - K
    def rhoG(kp, K):
        if 0 < kp < P:
            km = -(m2*(1-kp/P)+K)/(2*(P-kp))        # D1 pole (upper half plane), closed above
            k2 = ksq(kp, km, K); Dg = -k2
            D2 = m2 - (m2/Pp)*km + 2*Pp*kp - k2
            return 1/((P-kp)*Dg*D2)
        if -m2/(2*Pp) < kp <= 0:
            km = (m2+2*Pp*kp+K)/(a2+2*kp)            # D2 pole (lower half plane), closed below
            k2 = ksq(kp, km, K); Dg = -k2
            D1 = m2 + 2*P*km - (m2/P)*kp - k2
            return 2/((a2+2*kp)*Dg*D1)
        return mp.mpf(0)
    def rhoS(kp, K):         # 1/(Dg e1 e2): Dg pole for kp>0
        return 1/((kp*m2+P*K)*(m2+2*Pp*kp)) if kp > 0 else mp.mpf(0)
    def rhoC1(kp, K):        # (1/(Dg h2)) (1/D1 - 1/e1)
        A = kp*m2*(1-kp/P)+P*K; B = kp*m2+P*K
        if 0 < kp < P: return (1/A-1/B)/(2*Pp*kp)
        if kp >= P: return -(1/B)/(2*Pp*kp)
        return mp.mpf(0)
    def rhoC2(kp, K):        # (1/(Dg h1)) (1/D2 - 1/e2), h1 = 2P k^-
        if kp > 0:
            # D2 and Dg poles both lower; e2 indep of k^-, h1 pole at k^-=+i0 (upper): close upper -> h1 residue at k^-=0
            # 1/D2 - 1/e2 at k^-=0: 1/(m2+2Pp kp+K) - 1/(m2+2Pp kp); 1/Dg at k^-=0 = 1/K ; residue factor of 1/h1: 1/(2P)
            # integral = 2 pi i/(2P) * (1/K)*(...); rho = (1/(i pi)) * integral
            return (1/P)*(1/K)*(1/(m2+2*Pp*kp+K) - 1/(m2+2*Pp*kp))
        if -m2/(2*Pp) < kp <= 0:
            km = (m2+2*Pp*kp+K)/(a2+2*kp)            # only D2 pole lower (Dg upper for kp<0, h1 upper)
            k2 = ksq(kp, km, K); Dg = -k2; h1 = 2*P*km
            return 2/((a2+2*kp)*Dg*h1)
        return mp.mpf(0)
    def rhoH(kp, K):         # Dg/(t1 h1 t2 h2)
        if 0 < kp < P:
            v = kp/P; Qt2 = 2*P*Pp
            return -v/(P*(Qt2*v*(1-v)+K)*(Qt2*v+K))
        if kp >= P: return (1/P)/((2*Pp*kp+K)*(2*Pp*kp))
        return mp.mpf(0)
    return rhoG, rhoS, rhoC1, rhoC2, rhoH

# NOTE on rhoC2 for kp>0: R6 wrote -(1/P)/((m2+2Pp kp+K)(m2+2Pp kp)) ; mine: (1/(P K))[1/(m2+2Pp kp+K) - 1/(m2+2Pp kp)]
# = (1/(P K)) * (-K)/((m2+2Pp kp+K)(m2+2Pp kp)) = -(1/P)/((m2+2Pp kp+K)(m2+2Pp kp))  -> identical.

P, Pp, m2 = mp.mpf('0.8'), mp.mpf('1.3'), mp.mpf('0.02')
Qt2 = 2*P*Pp; Q2 = (Qt2+m2)**2/Qt2; t = m2/Q2
rhoG, rhoS, rhoC1, rhoC2, rhoH = make(P, Pp, m2)
exactI = Phi1(t, t)/Q2
regsum = (mp.log(Qt2/m2)**2 + mp.pi**2/3)/Qt2
kpb = [-m2/(2*Pp), 0, m2**2, m2/10, m2, mp.sqrt(m2), P/2, P, 2*P, 10*P, mp.inf]
Kb = [0, m2**2, m2/10, m2, mp.mpf(1)/10, 1, 10, mp.inf]
def int2(f, eps=0):
    eps = mp.mpf(eps)
    w = (lambda K: K**(-eps)/mp.gamma(1-eps)) if eps != 0 else (lambda K: 1)
    return mp.quad(lambda kp: mp.quad(lambda K: w(K)*f(kp, K), Kb), kpb)
valG = int2(rhoG)
rep("d=4: int rho_Gamma = exact I (UD)", abs(valG-exactI) < mp.mpf('1e-12'), "%s vs %s" % (mp.nstr(valG, 15), mp.nstr(exactI, 15)))
rem = int2(lambda kp, K: rhoG(kp, K)-rhoS(kp, K)-rhoC1(kp, K)-rhoC2(kp, K)-rhoH(kp, K))
rep("d=4: int remainder density = I - (D.32)", abs(rem-(exactI-regsum)) < mp.mpf('1e-12'), "%s vs %s" % (mp.nstr(rem, 15), mp.nstr(exactI-regsum, 15)))
rep("remainder value = -0.0173434339581 (claim)", abs(rem-mp.mpf('-0.0173434339581')) < mp.mpf('1e-12'), mp.nstr(rem, 15))

# d-dimensional values at eps = 0.3 (mu = 1)
eps = mp.mpf('0.3')
A = mp.gamma(1+eps)*mp.gamma(1-eps)**2/(eps**2*mp.gamma(1-2*eps))
B = mp.gamma(1+eps)**2*mp.gamma(1-eps)/eps**2
vals = {'S': int2(rhoS, eps), 'C1': int2(rhoC1, eps), 'C2': int2(rhoC2, eps), 'H': int2(rhoH, eps)}
pred = {'S': (Qt2/m2**2)**eps*B/Qt2, 'C1': -(1/m2)**eps*A/Qt2, 'C2': -(1/m2)**eps*A/Qt2, 'H': (1/Qt2)**eps*A/Qt2}
for k in ['S', 'C1', 'C2', 'H']:
    rep("eps=0.3: int C_%s Gamma = closed form (a) [rel. tol 1e-7; 2D quadrature with K^-eps endpoint]" % k, abs(vals[k]-pred[k]) < mp.mpf('1e-7')*abs(pred[k]),
        "%s vs %s" % (mp.nstr(vals[k], 14), mp.nstr(pred[k], 14)))

# (b) symbolic eps-expansion of the sum
e, lQ, lm = sp.symbols('epsilon ellQ ellm')
Aexp = sp.gamma(1+e)*sp.gamma(1-e)**2/(e**2*sp.gamma(1-2*e))
Bexp = sp.gamma(1+e)**2*sp.gamma(1-e)/e**2
tot = sp.exp(e*lQ)*Aexp - 2*sp.exp(e*lm)*Aexp + sp.exp(e*(2*lm-lQ))*Bexp
ser = sp.series(tot, e, 0, 1).removeO()
ser = sp.simplify(sp.expand(ser))
rep("(b) eps-poles cancel and finite part = (lm-lQ)^2 + pi^2/3", sp.simplify(ser - ((lm-lQ)**2 + sp.pi**2/3)) == 0, str(ser))

# (c) exact closed form of the remainder in sigma = m^2/Qt^2, and its t-expansion
sig = m2/Qt2
closed = (4*mp.polylog(2, -sig) + sig**2*(mp.log(sig)**2 + mp.pi**2/3))/(Qt2*(1-sig**2))
rep("closed form [4Li2(-s)+s^2(ln^2 s+pi^2/3)]/(Qt^2(1-s^2)) = I - (D.32) at R6 point", abs(closed-(exactI-regsum)) < mp.mpf('1e-20'),
    mp.nstr(closed, 18))
mp.mp.dps = 40
for tv in ['1e-2', '1e-4', '1e-7']:
    tt = mp.mpf(tv); s_ = (1-2*tt-mp.sqrt(1-4*tt))/(2*tt)     # sigma as function of t (small root of t = s/(1+s)^2)
    Qt2_ = 1/(1+s_)**2   # Q^2 = 1
    m2_ = tt
    r_direct = Phi1(tt, tt) - (mp.log(Qt2_/m2_)**2 + mp.pi**2/3)/Qt2_
    r_closed = (4*mp.polylog(2, -s_) + s_**2*(mp.log(s_)**2 + mp.pi**2/3))/(Qt2_*(1-s_**2))
    rep("closed form == Phi1 - (D.32) at t=%s (Q^2=1)" % tv, abs(r_direct-r_closed) < mp.mpf('1e-30'), mp.nstr(r_closed, 20))

# series in t (symbolic): sigma(t) power series, L = ln(1/t)
tt, L = sp.symbols('t L', positive=True)
sigma_t = sp.series((1-2*tt-sp.sqrt(1-4*tt))/(2*tt), tt, 0, 6).removeO()
lnsig = -L + sp.series(sp.log(sigma_t/tt), tt, 0, 5).removeO()     # ln sigma = ln t + ln(sigma/t)
Li2 = sum((-sigma_t)**k/k**2 for k in range(1, 6))
Q2r = sp.expand(((4*Li2 + sigma_t**2*(lnsig**2 + sp.pi**2/3))*(1+sigma_t)**2/(1-sigma_t**2)))  # Q^2 r = Q^2/Qt^2 * [...]/(1-s^2), Q^2/Qt^2=(1+s)^2
Q2r_ser = sp.series(Q2r, tt, 0, 4).removeO()
c1 = sp.simplify(Q2r_ser.coeff(tt, 1)); c2 = sp.simplify(Q2r_ser.coeff(tt, 2)); c3 = sp.expand(Q2r_ser.coeff(tt, 3))
rep("Q^2 r: O(t) coefficient = -4 (no NLP log)", sp.simplify(c1+4) == 0, str(c1))
rep("Q^2 r: O(t^2) coefficient = L^2 - 15 + pi^2/3", sp.simplify(c2-(L**2-15+sp.pi**2/3)) == 0, str(sp.expand(c2)))
print("   Q^2 r: O(t^3) coefficient =", c3)
# Q^2 I series
Q2I = sp.expand((1+sigma_t)/(1-sigma_t)*(4*Li2 + lnsig**2 + sp.pi**2/3))   # 1/sqrt(1-4t) = (1+s)/(1-s)
Q2I_ser = sp.series(Q2I, tt, 0, 3).removeO()
d0 = sp.simplify(Q2I_ser.coeff(tt, 0)); d1 = sp.expand(Q2I_ser.coeff(tt, 1)); d2 = sp.expand(Q2I_ser.coeff(tt, 2))
rep("Q^2 I: O(t^0) = L^2 + pi^2/3", sp.simplify(d0-(L**2+sp.pi**2/3)) == 0, str(d0))
rep("Q^2 I: O(t) = 2L^2 - 4L - 4 + 2pi^2/3", sp.simplify(d1-(2*L**2-4*L-4+2*sp.pi**2/3)) == 0, str(d1))
rep("Q^2 I: O(t^2) = 6L^2 - 14L - 11 + 2pi^2", sp.simplify(d2-(6*L**2-14*L-11+2*sp.pi**2)) == 0, str(d2))
# numeric sanity of the closed-form-based series for Q^2 I against Phi1 at tiny t
tv = mp.mpf('1e-9'); Lv = mp.log(1/tv)
approx = Lv**2+mp.pi**2/3 + tv*(2*Lv**2-4*Lv-4+2*mp.pi**2/3) + tv**2*(6*Lv**2-14*Lv-11+2*mp.pi**2)
rep("Q^2 I series vs Phi1 at t=1e-9 (residual O(t^3 L^2))", abs(Phi1(tv, tv)-approx) < 1e3*tv**3*Lv**2, mp.nstr(Phi1(tv, tv)-approx, 5))
print("SUMMARY n12: %d/%d PASS" % (sum(res), len(res)))
