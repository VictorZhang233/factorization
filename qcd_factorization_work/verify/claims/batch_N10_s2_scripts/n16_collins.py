# N16 (stage 2): Collins 2007 (arXiv:0708.4410v1) eqs. (10)-(11): I1 = N F(kT)^2, I2 = -N G(kT)/(kT^2+mq^2).
# (1) independent residue derivation of the l^- integrals of the FIRST line of eq. (10) -> no (kT^2+mq^2) factors;
# (2) F, G by b-space Hankel transforms and by an angular-integrated k-space convolution (methods different
#     from stage 1); (3) Parseval, (4) Cauchy-Schwarz, (5) point values; (6) the printed second line of (10)
#     would make int d^2k I1 diverge.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
npass = 0; nfail = 0
def check(name, ok, info=""):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(("PASS " if ok else "FAIL ") + name + ("  " + info if info else ""), flush=True)

# ---------- (1) residues and constants ----------
x, pp, km, l, Aj, eps = sp.symbols('x p_plus k_minus l A_j epsilon', positive=True)
# at l^+ = 0, M = 0 (p^- = 0), kT, ljT fixed: (k-l)^2 - mq^2 = 2 x p+ (k^- - l^-) - A_j ; (p-k+l)^2 - mq^2 = 2(1-x)p+(l^- - k^-) - A_j
# with A_j = (kT-ljT)^2 + mq^2.  Amplitude side: both +i eps ; conjugate side: both -i eps.
al_, be_ = 2*x*pp, 2*(1-x)*pp
a1 = al_*km - Aj; b1 = -be_*km - Aj
# int dl 1/((a1 - al_ l + i e)(b1 + be_ l + i e)): pole in UHP at l=(a1+ie)/al_, close in UHP
lpole = a1/al_
res_amp = 2*sp.pi*sp.I*sp.limit(1/((-al_)*(b1 + be_*l)), l, lpole)
res_amp = sp.simplify(res_amp)
check("l^- integral (amplitude side) = 2 pi i /(2 p+ A_j), independent of k^-", sp.simplify(res_amp - 2*sp.pi*sp.I/(2*pp*Aj)) == 0, str(res_amp))
# numerical check of the residue formula at finite epsilon
mp.mp.dps = 25
xv, pv, kmv, Av, ev = mp.mpf('0.3'), mp.mpf('2.0'), mp.mpf('0.17'), mp.mpf('1.4'), mp.mpf('1e-6')
alv, bev = 2*xv*pv, 2*(1-xv)*pv
fnum = lambda L: 1/((alv*kmv - Av - alv*L + 1j*ev)*(-bev*kmv - Av + bev*L + 1j*ev))
lp = (alv*kmv - Av)/alv; lm = (bev*kmv + Av)/bev
val = mp.quad(fnum, [-mp.inf, min(lp, lm) - 1, lp, lm, max(lp, lm) + 1, mp.inf])
check("numerical l^- integral at eps=1e-6 matches 2 pi i/(2 p+ A_j)", abs(val - 2j*mp.pi/(2*pv*Av)) < 1e-5, mp.nstr(val, 10))
# conjugate side (-i eps) gives the complex conjugate: product = (2 pi)^2/(4 p+^2 A1 A2)
fnc = lambda L: 1/((alv*kmv - Av - alv*L - 1j*ev)*(-bev*kmv - Av + bev*L - 1j*ev))
valc = mp.quad(fnc, [-mp.inf, min(lp, lm) - 1, lp, lm, max(lp, lm) + 1, mp.inf])
check("conjugate side gives the complex conjugate", abs(valc - mp.conj(val)) < 1e-10)
# assemble constants of the first line of (10):
lam, g1, g2 = sp.symbols('lambda g1 g2', positive=True)
pref = lam**2*g1**2*g2*(g2+g1)/(2*sp.pi)**12
pref *= x*pp                              # x p^+ (scalar-quark PDF definition)
pref *= (2*(1-x)*pp)**2                   # [2(p+-k+)+l1+][2(p+-k+)+l2+] at l+ = 0
pref *= (2*sp.pi)**2                      # (2pi)^2 delta(l1+) delta(l2+) : the l^+ integrals
pref *= 2*sp.pi/(2*(1-x)*pp)              # int dk^- 2 pi delta((p-k)^2 - mq^2) = 2pi/(2(1-x)p+)
pref *= (2*sp.pi)**2/(4*pp**2)            # product of the two l^- integrals (A1 A2 left in the integrand)
# gluon propagators (l_j^2 - mg^2) = -(ljT^2 + mg^2): two of them -> (+1) * 1/((l1T^2+mg^2)(l2T^2+mg^2))
pref = sp.simplify(pref)
Ncal = lam**2*g1**2*g2*(g2+g1)*x*(1-x)/(256*sp.pi**7)
check("constant of eq.(10) second line: N = lambda^2 g1^2 g2(g2+g1) x(1-x)/(256 pi^7), no p+ dependence", sp.simplify(pref - Ncal) == 0, str(pref))
print("   => I1 = N * int d2l1 d2l2 prod_j 1/((ljT^2+mg^2)((kT-ljT)^2+mq^2)) = N F(kT)^2 ; the printed factor prod_j (kT^2+mq^2) does not arise")
# dimension count of the first line of (10): [lambda]=1, [g]=0
dims = {'lambda^2': 2, 'x p+': 1, 'measure dk- d4l1 d4l2': 9, 'numerator': 2, 'propagators(6)': -12, 'deltas': -2-2}
D1 = sum(dims.values())
check("mass dimension of eq.(10) first line = -2 = dimension of N F^2 (printed second line would be +2)", D1 == -2, str(D1))

# ---------- (2) F and G ----------
mp.mp.dps = 25
mg, mq = mp.mpf('0.5'), mp.mpf(1)
def F_closed(k, mg=mg, mq=mq):
    s = k*k + mg*mg + mq*mq; Lm = s*s - 4*mg*mg*mq*mq
    # (s+sqrt L)/(s-sqrt L) = (s+sqrt L)^2/(4 mg^2 mq^2)  (cancellation-free form of the same expression)
    return mp.pi/mp.sqrt(Lm)*mp.log((s + mp.sqrt(Lm))**2/(4*mg*mg*mq*mq))
def F_hankel(k, mg=mg, mq=mq):
    f = lambda b: b*mp.besselj(0, k*b)*mp.besselk(0, mg*b)*mp.besselk(0, mq*b)
    return 2*mp.pi*mp.quad(f, [0, mp.mpf('0.5'), 2, 5, 10, 20, 40, 80])
def F_feyn(k, mg=mg, mq=mq):
    return mp.pi*mp.quad(lambda y: 1/(y*(1-y)*k*k + y*mq*mq + (1-y)*mg*mg), [0, 1])
for k in [mp.mpf('0.8'), mp.mpf(3)]:
    sv = k*k + mg*mg + mq*mq; Lv = sv*sv - 4*mg*mg*mq*mq
    lit = mp.pi/mp.sqrt(Lv)*mp.log((sv + mp.sqrt(Lv))/(sv - mp.sqrt(Lv)))
    check("literal closed form (pi/sqrt L) ln((s+sqrt L)/(s-sqrt L)) at k=%s" % mp.nstr(k, 3), abs(lit - F_closed(k)) < 1e-18)
for k in [mp.mpf(0), mp.mpf('0.8'), mp.mpf(3)]:
    a, b, c = F_closed(k), F_hankel(k), F_feyn(k)
    check("F(k=%s): closed form = Hankel(K0 K0) = Feynman" % mp.nstr(k, 3), abs(a-b) < 1e-15 and abs(a-c) < 1e-15, mp.nstr(a, 15))
def G_hankel(k, mg=mg, mq=mq):
    f = lambda b: b*mp.besselj(0, k*b)*mp.besselk(0, mg*b)**2*mp.besselk(0, mq*b)
    return (2*mp.pi)**2*mp.quad(f, [0, mp.mpf('0.5'), 2, 5, 10, 20, 40, 80])
def Fgg(qq, mg=mg):
    if qq == 0: return mp.pi/(mg*mg)
    s = qq*qq + 2*mg*mg; Lm = qq*qq*(qq*qq + 4*mg*mg)
    return mp.pi/mp.sqrt(Lm)*mp.log((s + mp.sqrt(Lm))**2/(4*mg**4))
def G_conv(k, mg=mg, mq=mq):
    # G(k) = int d^2q Fgg(q) / ((k-q)^2+mq^2); angular integral: 2 pi / sqrt((k^2+q^2+mq^2)^2 - 4 k^2 q^2)
    f = lambda qq: qq*Fgg(qq, mg)*2*mp.pi/mp.sqrt((k*k + qq*qq + mq*mq)**2 - 4*k*k*qq*qq)
    return mp.quad(f, [0, mp.mpf('0.5'), k if k > 0 else 1, 2*k + 1, 10, 100, mp.inf])
Gvals = {}
for k in [mp.mpf(0), mp.mpf('0.8'), mp.mpf(3)]:
    a, b = G_hankel(k), G_conv(k)
    Gvals[k] = a
    check("G(k=%s): Hankel(K0^2 K0) = angular-integrated convolution" % mp.nstr(k, 3), abs(a/b - 1) < 1e-12, "%s vs %s" % (mp.nstr(a, 15), mp.nstr(b, 15)))
check("G(0) = 54.72870771 (stage-1 value)", abs(Gvals[mp.mpf(0)] - mp.mpf('54.72870771')) < 1e-7, mp.nstr(Gvals[mp.mpf(0)], 13))

# ---------- (3) point values ----------
claimed = {'0': '-21.0', '0.3': '-17.7', '0.8': '-7.19', '1.5': '-0.70', '3': '0.38', '6': '0.089'}
for ks, cl in claimed.items():
    k = mp.mpf(ks)
    v = F_closed(k)**2 - G_hankel(k)/(k*k + mq*mq)
    tol = 0.5*10**(-(len(cl.split('.')[1])))
    check("(I1+I2)/N at kT=%s: claimed %s" % (ks, cl), abs(v - mp.mpf(cl)) <= tol + 1e-12, mp.nstr(v, 8))

# ---------- (4) Parseval ----------
bspace = (2*mp.pi)**3*mp.quad(lambda b: b*mp.besselk(0, mg*b)**2*mp.besselk(0, mq*b)**2, [0, mp.mpf('0.5'), 2, 5, 10, 20, 40, 80])
kF2 = 2*mp.pi*mp.quad(lambda k: k*F_closed(k)**2, [0, 1, 3, 10, 30, 100, mp.inf])
check("Parseval: int d^2k F^2 = (2pi)^3 int db b K0(mg b)^2 K0(mq b)^2", abs(kF2/bspace - 1) < 1e-15, "%s vs %s" % (mp.nstr(kF2, 15), mp.nstr(bspace, 15)))
# k-space form without Bessel functions: int d^2k G(k)/(k^2+mq^2) = int d^2q Fgg(q) * Fqq(q), where
# Fqq(q) = int d^2k 1/(((k-q)^2+mq^2)(k^2+mq^2)) is the same closed form with both masses mq.
def Fqq(qq, mq=mq):
    if qq == 0: return mp.pi/(mq*mq)
    s_ = qq*qq + 2*mq*mq; Lm = qq*qq*(qq*qq + 4*mq*mq)
    return mp.pi/mp.sqrt(Lm)*mp.log((s_ + mp.sqrt(Lm))**2/(4*mq**4))
kG = 2*mp.pi*mp.quad(lambda qq: qq*Fgg(qq)*Fqq(qq), [0, 1, 3, 10, 30, 100, mp.inf])
check("Parseval: int d^2k G/(k^2+mq^2) = int d^2q Fgg Fqq = same value  => int d^2k (I1+I2) = 0", abs(kG/bspace - 1) < 1e-15, "%s vs %s" % (mp.nstr(kG, 15), mp.nstr(bspace, 15)))
# second mass point
mg2, mq2 = mp.mpf('1.7'), mp.mpf('0.4')
bs2 = (2*mp.pi)**3*mp.quad(lambda b: b*mp.besselk(0, mg2*b)**2*mp.besselk(0, mq2*b)**2, [0, mp.mpf('0.5'), 2, 5, 10, 20, 40, 80, 160])
kF2b = 2*mp.pi*mp.quad(lambda k: k*F_closed(k, mg2, mq2)**2, [0, 1, 3, 10, 30, 100, mp.inf])
kGb = 2*mp.pi*mp.quad(lambda qq: qq*Fgg(qq, mg2)*Fqq(qq, mq2), [0, 1, 3, 10, 30, 100, mp.inf])
check("Parseval at (mg,mq)=(1.7,0.4): k-space int F^2 = int Fgg Fqq = b-space", abs(kF2b/bs2 - 1) < 1e-15 and abs(kGb/bs2 - 1) < 1e-15, "%s %s %s" % (mp.nstr(kF2b, 13), mp.nstr(kGb, 13), mp.nstr(bs2, 13)))

# ---------- (5) Cauchy-Schwarz ----------
def mu_checks(mg, mq):
    dmu = lambda f: mp.quad(lambda b: b*mp.besselk(0, mq*b)*f(b), [0, mp.mpf('0.5'), 2, 5, 10, 20, 40, 80, 200])  # d^2b/(2pi)^2 * 2pi K0 = b db K0
    tot = dmu(lambda b: 1)
    F0 = dmu(lambda b: 2*mp.pi*mp.besselk(0, mg*b))
    G0 = dmu(lambda b: (2*mp.pi*mp.besselk(0, mg*b))**2)
    return tot, F0, G0
tot, F0, G0 = mu_checks(mg, mq)
check("measure: int dmu = 1/mq^2", abs(tot - 1/mq**2) < 1e-18)
check("F(0) = int dmu 2 pi K0(mg b) = pi ln(mg^2/mq^2)/(mg^2-mq^2)", abs(F0 - F_closed(mp.mpf(0))) < 1e-15 and abs(F0 - mp.pi*mp.log(mg**2/mq**2)/(mg**2 - mq**2)) < 1e-15, mp.nstr(F0, 15))
check("G(0) = int dmu (2 pi K0(mg b))^2", abs(G0 - Gvals[mp.mpf(0)]) < 1e-12, mp.nstr(G0, 15))
check("Cauchy-Schwarz: F(0)^2 < G(0)/mq^2  (33.720 < 54.729)", F0**2 < G0/mq**2, "%s < %s" % (mp.nstr(F0**2, 8), mp.nstr(G0/mq**2, 8)))
worst = -1e9
for (a, b) in [(0.01, 1), (0.1, 1), (0.5, 1), (1, 1), (2, 1), (10, 1), (60, 1), (1, 0.05), (1, 0.003)]:
    a, b = mp.mpf(a), mp.mpf(b)
    t_, F0_, G0_ = mu_checks(a, b)
    rel = (F0_**2 - G0_/b**2)/(G0_/b**2)
    worst = max(worst, rel)
    print("     mg=%-6s mq=%-6s  F(0)^2 - G(0)/mq^2 = %s   relative %s" % (mp.nstr(a, 3), mp.nstr(b, 3), mp.nstr(F0_**2 - G0_/b**2, 8), mp.nstr(rel, 5)))
check("Cauchy-Schwarz strict for all scanned mass pairs (relative gap < 0)", worst < 0, "largest relative value %s" % mp.nstr(worst, 5))
# equality case of C-S would need K0(mg b) constant mu-a.e.: impossible (K0 strictly decreasing)

# ---------- (6) the printed second line of (10) cannot be right ----------
mp.mp.dps = 20
vals = [k*F_closed(k)**2*(k*k + mq*mq)**2 for k in (mp.mpf(10), mp.mpf(100), mp.mpf(1000))]
check("printed eq.(10) integrand k F^2 (k^2+mq^2)^2 grows (~ k ln^2 k): int d^2k I1 would diverge", vals[0] < vals[1] < vals[2], str([mp.nstr(v, 6) for v in vals]))
print("\nTOTAL: %d PASS, %d FAIL" % (npass, nfail))
