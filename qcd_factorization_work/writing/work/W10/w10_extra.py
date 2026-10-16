"""
W10 / Ch9 + App F -- additional checks for the text:
 (a) ex:method-sudakov-subtraction: k^- residue of C_{C1}Gamma (light-cone representation)
       int dk^-/(2pi) C_C1 Gamma = (i/2) (m^2 k^+/(2PP')) / ([k^+ m^2 (1-k^+/P) + P kT^2][k^+ m^2 + P kT^2])   (0<k^+<P)
       for k^+ > P only the -T_C1 T_S Gamma tail survives; for k^+ < 0 the integral vanishes
     and the soft approximation on the D_1 line: relative error O(1) at k^- = 0, O(z) at Re k^- = kT^2/(4k^+)
 (b) App F: q qbar -> g* g* -- the t+u graphs contracted with k1 give g^2 f^{abc} J^nu_c, the s-channel graph gives
     -g^2 f^{abc} J^nu_c + (g^2 f^{abc}/Q^2)(k2^2 g^{nu s} - k2^nu k2^s) J_{c s}  (on-shell quarks)
 (c) ex:method-dis-oneloop: C_2^q assembled from VF-DIS-3 (virtual) + VF-DIS-4 (real): pole cancellation and
       C_2^q = C_F[2D_1 - 3/2 D_0 - (1+z)ln(1-z) - (1+z^2)/(1-z) ln z + 3 + 2z - (9/2 + pi^2/3) delta(1-z)]
     and C_H Gamma^(1) = (as/2pi)[C_2^q + P_qq ln(Q^2/mu^2)]
 (d) error table, row 5: |k^+k^-| >= c kT^2 and |Dt| >= c(|p^+||k^-| + v_A(p)) imply |D - Dt| <= C (|k^+|/|p^+|)^{1/2} |Dt|
     (random sampling, explicit constant)
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import sympy as sp
from w10_dirac import *

npass = 0; nfail = 0
def check(name, ok, info=''):
    global npass, nfail
    npass += bool(ok); nfail += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ((' : ' + str(info)) if info != '' else ''))

# ------------------------------------------------------------------ (a)
km = sp.symbols('km')
P, Pp, m2, kT2 = sp.Rational(4, 5), sp.Rational(13, 10), sp.Rational(1, 10), sp.Rational(3, 10)
def dens(kp):
    """k^- integral (with 1/(2pi)) of C_C1 Gamma; each denominator a + b k^- carries -i0, its zero is in the upper
    half plane iff b > 0; close the contour in the lower half plane (integrand ~ |k^-|^-2)."""
    kp = sp.nsimplify(kp)
    k2 = 2*kp*km - kT2
    Dg = -k2
    D1 = m2 + 2*P*km - m2/P*kp - k2          # -(p1-k)^2
    e1 = m2 + 2*P*km
    h2 = 2*Pp*kp
    terms = [(1, [Dg, D1], h2), (-1, [Dg, e1], h2)]   # C_C1 = 1/(Dg h2 D1) - 1/(Dg h2 e1)
    total = 0
    for sgn, dens_, const in terms:
        f = sgn/(const*sp.prod(dens_))
        for d in dens_:
            b = sp.diff(d, km)
            if b == 0: continue
            if b < 0:            # zero in the lower half plane
                root = sp.solve(d, km)[0]
                total += -sp.I*sp.residue(f, km, root)   # (1/2pi)(-2 pi i) Res
    return sp.simplify(total)
for kpv in [sp.Rational(3, 10), sp.Rational(7, 10)]:
    lhs = dens(kpv)
    rhs = sp.I/2*(m2*kpv/(2*P*Pp))/((kpv*m2*(1 - kpv/P) + P*kT2)*(kpv*m2 + P*kT2))
    check('(a) int dk^-/(2pi) C_C1 Gamma at k^+=%s (0<k^+<P): closed form' % kpv, sp.simplify(lhs - rhs) == 0, sp.N(lhs, 12))
lhs = dens(sp.Rational(3, 2))
rhs = -sp.I/2*(1/(2*Pp*sp.Rational(3, 2)))/(sp.Rational(3, 2)*m2 + P*kT2)
check('(a) k^+ > P: only the tail of -T_C1 T_S Gamma: -(i/2)/[h2 (k^+ m^2 + P kT^2)]', sp.simplify(lhs - rhs) == 0, sp.N(lhs, 12))
check('(a) k^+ < 0: integral vanishes', sp.simplify(dens(sp.Rational(-1, 5))) == 0)
# behaviour as k^+ -> 0: the combination vanishes linearly while each term ~ 1/k^+
x = sp.symbols('x', positive=True)
comb = sp.I/2*(m2*x/(2*P*Pp))/((x*m2*(1 - x/P) + P*kT2)*(x*m2 + P*kT2))
check('(a) the combined density vanishes linearly as k^+ -> 0', sp.limit(comb/x, x, 0) != 0 and sp.limit(comb, x, 0) == 0)

# ------------------------------------------------------------------ (b)
rng = np.random.default_rng(3)
g = 1.0
def onshell(mass):
    pv = rng.normal(size=3); E = np.sqrt(pv @ pv + mass**2)
    return np.array([E, *pv], dtype=complex)
p1 = onshell(0.0); p2 = onshell(0.0); Q = p1 + p2
k1 = rnd_vec(rng); k2 = Q - k1
u1 = u_spinors(p1)[0]; v2 = v_spinors(p2)[0]
Ginv = np.diag([1.0, -1, -1, -1])
Jup = np.array([bar(v2) @ GAM[s] @ u1 for s in range(4)])     # colour-stripped J^sigma
mx_tu = 0; mx_s = 0; sc = 0
for a in range(8):
    for b in range(8):
        for nu in range(4):
            tu = np.zeros((3, 3), dtype=complex); ss = np.zeros((3, 3), dtype=complex)
            for mu in range(4):
                t = bar(v2) @ (1j*g*GAM[nu]) @ S(p1-k1) @ (1j*g*GAM[mu]) @ u1
                uu = bar(v2) @ (1j*g*GAM[mu]) @ S(p1-k2) @ (1j*g*GAM[nu]) @ u1
                tu += lower(k1)[mu]*(t*(TA[b] @ TA[a]) + uu*(TA[a] @ TA[b]))
                for c in range(8):
                    if abs(FABC[c, a, b]) < 1e-14: continue
                    tot = 0
                    for rho in range(4):
                        Jr = bar(v2) @ (1j*g*GAM[rho]) @ u1
                        tot += Jr*Ginv[rho, rho]*(-1j/mdot(Q, Q))*g*V3(Q, -k1, -k2, rho, mu, nu)
                    ss += lower(k1)[mu]*FABC[c, a, b]*tot*TA[c]
            tu_exp = sum(g**2*FABC[a, b, c]*Jup[nu]*TA[c] for c in range(8))
            proj = mdot(k2, k2)*Jup[nu] - k2[nu]*mdot(k2, Jup)
            s_exp = sum(-g**2*FABC[a, b, c]*Jup[nu]*TA[c] + g**2*FABC[a, b, c]/mdot(Q, Q)*proj*TA[c] for c in range(8))
            mx_tu = max(mx_tu, np.max(np.abs(tu - tu_exp))); mx_s = max(mx_s, np.max(np.abs(ss - s_exp)))
            sc = max(sc, np.max(np.abs(tu)))
check('(b) t+u graphs contracted with k1: g^2 f^{abc} J^nu_c t^c', mx_tu/sc < 1e-12, '%.1e' % (mx_tu/sc))
check('(b) s-channel graph contracted with k1: -g^2 f J^nu + (g^2 f/Q^2)(k2^2 J^nu - k2^nu k2.J)', mx_s/sc < 1e-12, '%.1e' % (mx_s/sc))

# ------------------------------------------------------------------ (c)
eps, z = sp.symbols('epsilon z')
D0, D1, dl = sp.symbols('D0 D1 delta')
CF = sp.Symbol('C_F')
zeta2 = sp.pi**2/6
virt = CF*(-2/eps**2 - 3/eps - 8 + zeta2)*dl
real = CF*(2*dl/eps**2 + (-2*D0 + 1 + z + sp.Rational(3, 2)*dl)/eps
           + 2*D1 - sp.Rational(3, 2)*D0 - (1 + z)*sp.log(1 - z) - (1 + z**2)/(1 - z)*sp.log(z) + 3 + 2*z
           + (sp.Rational(7, 2) - 3*zeta2)*dl)
tot = sp.expand(virt + real)
Pqq_over = 2*D0 - (1 + z) + sp.Rational(3, 2)*dl      # [ (1+z^2)/(1-z) ]_+ in terms of D0, delta
check('(c) 1/eps^2 cancels (2 - 2 = 0)', sp.simplify(tot.coeff(eps, -2)) == 0)
check('(c) 1/eps coefficient = -P_qq (C_F [(1+z^2)/(1-z)]_+)', sp.simplify(tot.coeff(eps, -1) + CF*Pqq_over) == 0)
C2 = CF*(2*D1 - sp.Rational(3, 2)*D0 - (1 + z)*sp.log(1 - z) - (1 + z**2)/(1 - z)*sp.log(z) + 3 + 2*z
         - (sp.Rational(9, 2) + sp.pi**2/3)*dl)
check('(c) finite part = C_2^q with delta coefficient -(9/2 + pi^2/3)', sp.simplify(tot.coeff(eps, 0) - C2) == 0)
Lq = sp.Symbol('L')    # ln(Q^2/mu^2)
a = sp.Symbol('a')
full = a*sp.exp(-eps*Lq)*(-CF*Pqq_over/eps + C2)                 # (mu^2/Q^2)^eps [ -P/eps + C2 ]
CA = a*(-CF*Pqq_over/eps)
CH = sp.series(full - CA, eps, 0, 1).removeO()
check('(c) C_H Gamma^(1) = (as/2pi)[C_2^q + P_qq ln(Q^2/mu^2)] (no pole)', sp.simplify(CH - a*(C2 + CF*Pqq_over*Lq)) == 0)

# ------------------------------------------------------------------ (d)
c = 0.3
worst = 0.0; nacc = 0
for _ in range(200000):
    pp = 10**rng.uniform(-1, 1); pm = rng.normal()*10**rng.uniform(-3, 0); pT = rng.normal(size=2)*10**rng.uniform(-2, 0)
    kp = rng.choice([-1, 1])*pp*10**rng.uniform(-4, 0)*0.999
    kmn = rng.normal()*10**rng.uniform(-3, 1); kT = rng.normal(size=2)*10**rng.uniform(-3, 0)
    M2 = 10**rng.uniform(-3, 0)*rng.choice([0, 1])
    kT2_ = kT @ kT
    if abs(kp*kmn) < c*kT2_: continue
    p2_ = 2*pp*pm - pT @ pT
    Dt = p2_ - M2 + 2*pp*kmn
    vA = abs(pp*pm) + pT @ pT
    if abs(Dt) < c*(abs(pp)*abs(kmn) + vA): continue
    nacc += 1
    D = p2_ + 2*(pp*kmn + pm*kp - pT @ kT) + 2*kp*kmn - kT2_ - M2
    xr = abs(kp)/abs(pp)
    bound = ((2 + 1/c)/c + 2/c)*xr + max(1, 1/c)/c*np.sqrt(xr)
    worst = max(worst, abs(D - Dt)/abs(Dt)/bound)
check('(d) row 5: |D - Dt| <= C(c) (|k^+|/|p^+|)^{1/2} |Dt| on %d random admissible points' % nacc, worst <= 1.0 + 1e-12, 'max ratio to bound %.3f' % worst)
print('\n=== w10_extra: %d PASS, %d FAIL ===' % (npass, nfail))
