# -*- coding: utf-8 -*-
"""
nlo_checks.py -- O(alpha_s) Drell-Yan in CDR + MS-bar: derivation pipeline and all cross-checks.

Output: logs/nlo_checks.log (PASS/FAIL list) and results_nlo.tex (LaTeX of the final coefficient functions).
Units: a = alpha_s(mu)/(2 pi), mu_R = mu; L = ln(mu^2/Q^2), LF = ln(mu_F^2/Q^2).
"""
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sympy as sp
import mpmath as mp
from dy_core import (eps, z, v, L, CF, TF, s, t, u, EG, T_qqbar, T_qg, real_qqbar_exact, real_qg_exact,
                     vertex_exact, Dist, dist_equal, expand_plus, expand_regular, P_qq, P_qg)

LF = sp.Symbol('L_F', real=True)
RES = []
t0 = time.time()


def report(name, ok, extra=''):
    RES.append((name, bool(ok)))
    print('[%s] %s %s' % ('PASS' if ok else 'FAIL', name, extra), flush=True)


z2, z3, z5 = sp.zeta(2), sp.zeta(3), sp.zeta(5)
tests = [lambda w: w**3, lambda w: mp.exp(w), lambda w: mp.cos(3 * w), lambda w: w**7 * (1 - w)**0 + mp.sqrt(w)]

# ------------------------------------------------------------------ 1. matrix elements
Tqq = T_qqbar()
Q2 = s + t + u
report('ME q qbar -> gamma* g:  T = 8(1-eps)[(1-eps)(u/t+t/u) + 2 s Q^2/(t u) - 2 eps]',
       sp.simplify(Tqq - 8 * (1 - eps) * ((1 - eps) * (u / t + t / u) + 2 * s * Q2 / (t * u) - 2 * eps)) == 0)
Tqg = T_qg()
report('ME q g -> gamma* q:  T = -8(1-eps)[(1-eps)(s/t+t/s) + 2 u Q^2/(s t) - 2 eps]   (t=(p_g-k)^2, u=(p_q-k)^2)',
       sp.simplify(Tqg - (-8) * (1 - eps) * ((1 - eps) * (s / t + t / s) + 2 * u * Q2 / (s * t) - 2 * eps)) == 0)
S_, T_, U_ = sp.symbols('S_ T_ U_')
crossed = -Tqq.subs({s: S_, t: T_, u: U_}).subs({S_: u, T_: s, U_: t})
report('crossing: T_qg(s,t,u) = -T_qqbar(s->u, t->s, u->t)  [p2 -> -k(out q), k -> -p2(in g)]', sp.simplify(Tqg - crossed) == 0)

# ------------------------------------------------------------------ 2. D-dim phase space
Dd = 4 - 2 * eps
Omega = lambda n: 2 * sp.pi**(n / 2) / sp.gamma(n / 2)       # area of unit sphere S^{n-1} in R^n
lhs = Omega(Dd - 2) * sp.sqrt(sp.pi) * sp.gamma((Dd - 2) / 2) / sp.gamma((Dd - 1) / 2)   # Omega_{D-3} * int sin^{D-3}
report('phase space: Omega_{D-3} int_0^pi sin^{D-3}(theta) dtheta = total solid angle in D-1 space dims',
       sp.simplify(sp.gammasimp(lhs / Omega(Dd - 1))) == 1)
# dPhi_2 = (1/8pi)(4pi/shat)^eps (1-z)^{1-2eps}/Gamma(1-eps) [v(1-v)]^{-eps} dv  <->  |k|^{D-3}/(4 sqrt(shat)(2pi)^{D-2}) dOmega_{D-2}
sh = sp.Symbol('shat', positive=True)
kabs = sp.sqrt(sh) * (1 - z) / 2
full = kabs**(Dd - 3) / (4 * sp.sqrt(sh) * (2 * sp.pi)**(Dd - 2)) * Omega(Dd - 1)
mine = (1 / (8 * sp.pi)) * (4 * sp.pi / sh)**eps * (1 - z)**(1 - 2 * eps) / sp.gamma(1 - eps) * sp.gamma(1 - eps)**2 / sp.gamma(2 - 2 * eps)
num_ok = all(abs(complex(sp.N((full / mine).subs({eps: e_, z: zz, sh: 3.3}), 30)) - 1) < 1e-25 for e_ in [sp.Rational(-1, 3), sp.Rational(1, 7), sp.Rational(-3, 2)] for zz in [sp.Rational(1, 3), sp.Rational(4, 5)])
report('phase space: total 2-body volume of the v-parametrisation = |k|^{D-3} Omega_{D-1}/(4 sqrt(s)(2pi)^{D-2})', num_ok)

# ------------------------------------------------------------------ 3. exact real contributions and closed forms
Kr = sp.exp(eps * EG) * sp.gamma(1 - eps) / sp.gamma(1 - 2 * eps)
Kv = sp.exp(eps * EG) * sp.gamma(1 + eps) * sp.gamma(1 - eps)**2 / sp.gamma(1 - 2 * eps)
Pref, Greg, _, Iv = real_qqbar_exact()
closed_qq = -2 / eps * Kr * (1 + z**2 + 2 * eps**2 * (1 - z)**2 / (1 - 2 * eps))    # = Pref*Greg
report('real q qbar exact:  Delta^R/a = -(2C_F/eps) e^{eps L} K_r z^eps (1-z)^{-1-2eps}[1+z^2+2eps^2(1-z)^2/(1-2eps)]',
       sp.simplify(sp.gammasimp(Pref * Greg / closed_qq)) == 1)
Pq, Hreg, _, Ivq = real_qg_exact()
closed_qg = -Kr / (2 * eps) * (2 * (z**2 + (1 - z)**2) - eps * (5 * z**2 - 6 * z + 7) + eps**2 * (1 + z)**2) / ((1 - eps) * (1 - 2 * eps))
report('real q g exact:  Delta^R/a = -(T_F/2eps) e^{eps L} K_r z^eps (1-z)^{-2eps}[2(z^2+(1-z)^2) - eps(5z^2-6z+7) + eps^2(1+z)^2]/((1-eps)(1-2eps))',
       sp.simplify(sp.gammasimp(Pq * Hreg / closed_qg)) == 1)

# ------------------------------------------------------------------ 4. virtual
f_dir, n0, N2 = vertex_exact()
f_closed = -Kv * (2 - eps + 2 * eps**2) / (eps**2 * (1 - 2 * eps))
okv = all(abs(complex(sp.N((f_dir / f_closed).subs(eps, e_), 40)) - 1) < 1e-35 for e_ in [sp.Rational(1, 7), sp.Rational(-2, 9), sp.Rational(3, 11), sp.Rational(-5, 13), sp.Rational(9, 10)])
report('vertex (Feynman parameters) = -e^{eps gE}Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps) (2-eps+2eps^2)/(eps^2(1-2eps))  [5 points, 35 digits]', okv)
mvv = (-2 / eps**2 - 3 / eps - 8 + z2 + eps * (-16 + sp.Rational(3, 2) * z2 + sp.Rational(14, 3) * z3)
       + eps**2 * (-32 + 4 * z2 + 7 * z3 + sp.Rational(47, 20) * z2**2)
       + eps**3 * (-64 + 8 * z2 + sp.Rational(56, 3) * z3 + sp.Rational(141, 40) * z2**2 - sp.Rational(7, 3) * z2 * z3 + sp.Rational(62, 5) * z5))
dser = sp.expand(sp.series(f_closed, eps, 0, 4).removeO() - mvv)
report('LIT: one-loop quark form factor = Moch-Vermaseren-Vogt, JHEP 08(2005)049, eq.(ff1loopexplicit), through eps^3',
       all(abs(sp.N(dser.coeff(eps, k), 40)) < 1e-35 for k in range(-2, 4)))
print('      f(eps) = %s + O(eps)' % sp.expand(sp.series(f_closed, eps, 0, 1).removeO()))

# ------------------------------------------------------------------ 5. Laurent expansion, assembly, mass factorisation
ORDER = 0
Hqq = CF * sp.exp(eps * L) * z**eps * closed_qq
R_qq = expand_plus(Hqq, ORDER)
Vexp = sp.expand(sp.series(CF * sp.exp(eps * L) * sp.cos(sp.pi * eps) * f_closed, eps, 0, ORDER + 1).removeO())
V_qq = {p: Dist(delta=Vexp.coeff(eps, p)) for p in range(-2, ORDER + 1) if Vexp.coeff(eps, p) != 0}
CT = {}
ctser = sp.expand(sp.series(sp.exp(eps * (L - LF)) / eps, eps, 0, ORDER + 1).removeO())
for p in range(-1, ORDER + 1):
    c = ctser.coeff(eps, p)
    if c != 0:
        CT[p] = P_qq().scale(2 * c)       # + 2 (1/eps)(mu^2/mu_F^2)^eps P_qq   (two incoming partons)
def collect(*dicts):
    out = {}
    for d in dicts:
        for p, dd in d.items():
            out[p] = out.get(p, Dist()) + dd
    return {p: dd.simplify() for p, dd in out.items()}
bare_qq = collect(R_qq, V_qq)
print('      bare q qbar (real+virtual): eps^-2 delta-coefficient = %s ; eps^-1 part = %s' % (bare_qq.get(-2, Dist()).delta, bare_qq.get(-1)))
report('soft double pole cancels between real and virtual (eps^-2 coefficient = 0)',
       (-2 not in bare_qq) or all(x == 0 for x in [sp.simplify(bare_qq[-2].delta), sp.simplify(bare_qq[-2].reg)] + list(bare_qq[-2].plus.values())))
pole_expected = P_qq().scale(-2)
dd, dp, dr, dn = dist_equal(bare_qq[-1], pole_expected)
report('remaining single pole of real+virtual = -(2/eps) P_qq(z)  [initial-state collinear, both legs]', dd and dp and dr)
tot_qq = collect(R_qq, V_qq, CT)
dd_ = [sp.simplify(tot_qq[p].delta) == 0 and all(sp.simplify(c) == 0 for c in tot_qq[p].plus.values()) and sp.simplify(tot_qq[p].reg) == 0 for p in tot_qq if p < 0]
report('MS-bar mass factorisation removes all poles in the q qbar channel', all(dd_))
Delta_qq = tot_qq[0].simplify()
print('      Delta_qqbar^(1) =', Delta_qq)

Hqg = TF * sp.exp(eps * L) * z**eps * (1 - z)**(-2 * eps) * closed_qg
R_qg = expand_regular(Hqg, ORDER)
CTg = {}
for p in range(-1, ORDER + 1):
    c = ctser.coeff(eps, p)
    if c != 0:
        CTg[p] = P_qg().scale(c)          # + (1/eps)(mu^2/mu_F^2)^eps P_qg   (gluon -> qbar, one leg)
dpole = sp.simplify(R_qg[-1].reg + P_qg().reg)
report('q g channel: collinear pole = -(1/eps) P_qg(z) = -(T_F/eps)[z^2+(1-z)^2]', dpole == 0)
tot_qg = collect(R_qg, CTg)
report('MS-bar mass factorisation removes the pole in the q g channel', all(sp.simplify(tot_qg[p].reg) == 0 for p in tot_qg if p < 0))
Delta_qg = tot_qg[0].simplify()
print('      Delta_qg^(1) =', Delta_qg)

# independence of the renormalisation-scale-type log L (mu), only L_F remains
dL = [sp.simplify(sp.diff(e_, L)) for e_ in [Delta_qq.delta, Delta_qq.reg, Delta_qg.reg] + list(Delta_qq.plus.values())]
report('result independent of mu (L) at this order; depends only on mu_F  [d/dL of every component = 0]', all(d_ == 0 for d_ in dL))
Delta_qq = Dist(Delta_qq.delta, Delta_qq.plus, sp.simplify(Delta_qq.reg.subs(L, 0)))
Delta_qg = Dist(Delta_qg.delta, Delta_qg.plus, sp.simplify(Delta_qg.reg.subs(L, 0)))
NUM = {CF: sp.Rational(4, 3), TF: sp.Rational(1, 2), LF: sp.Rational(7, 10)}

# ------------------------------------------------------------------ 6. comparison with the expected (task) formulas
D1 = lambda g: Dist.g_times_Dk(g, 1)
exp_qq = (D1(4 * CF * (1 + z**2)) + Dist(delta=CF * (2 * sp.pi**2 / 3 - 8), reg=-2 * CF * (1 + z**2) / (1 - z) * sp.log(z))
          + P_qq().scale(-2 * LF))                          # + 2 P_qq ln(Q^2/mu_F^2)
exp_qg = Dist(reg=TF * ((z**2 + (1 - z)**2) * sp.log((1 - z)**2 / z) + sp.Rational(1, 2) + 3 * z - sp.Rational(7, 2) * z**2)) + P_qg().scale(-LF)
r1 = dist_equal(Delta_qq, exp_qq)
r1n = dist_equal(Delta_qq.subs(NUM), exp_qq.subs(NUM), tests=tests)
report('Delta_qqbar = C_F[4(1+z^2)(ln(1-z)/(1-z))_+ - 2(1+z^2)/(1-z) ln z + (2pi^2/3-8)delta(1-z)] + 2 P_qq ln(Q^2/mu_F^2)  [term by term]',
       all(r1) and all(r1n), '(delta, D_k, regular, test functions) = %s' % (r1n,))
r2 = dist_equal(Delta_qg, exp_qg)
r2n = dist_equal(Delta_qg.subs(NUM), exp_qg.subs(NUM), tests=tests)
report('Delta_qg = T_F[(z^2+(1-z)^2) ln((1-z)^2/z) + 1/2 + 3z - 7z^2/2] + P_qg ln(Q^2/mu_F^2)  [term by term]', all(r2) and all(r2n))
# term-by-term decomposition of the regular part of Delta_qg at L_F = 0
reg_qg0 = sp.expand(sp.expand_log(Delta_qg.subs({LF: 0}).reg / TF, force=True))
pieces = {'(z^2+(1-z)^2) ln(1-z)': sp.expand(reg_qg0).coeff(sp.log(1 - z)), '(z^2+(1-z)^2) ln z': sp.expand(reg_qg0).coeff(sp.log(z)),
          'rational': sp.simplify(reg_qg0 - sp.expand(reg_qg0).coeff(sp.log(1 - z)) * sp.log(1 - z) - sp.expand(reg_qg0).coeff(sp.log(z)) * sp.log(z))}
print('      Delta_qg/T_F term by term:', {k: sp.factor(vv) for k, vv in pieces.items()})
report('   ... coefficient of ln(1-z) is 2[z^2+(1-z)^2], of ln z is -[z^2+(1-z)^2], rational part 1/2+3z-7z^2/2; overall colour factor T_F (=1/2)',
       sp.simplify(pieces['(z^2+(1-z)^2) ln(1-z)'] - 2 * (z**2 + (1 - z)**2)) == 0 and sp.simplify(pieces['(z^2+(1-z)^2) ln z'] + (z**2 + (1 - z)**2)) == 0
       and sp.simplify(pieces['rational'] - (sp.Rational(1, 2) + 3 * z - sp.Rational(7, 2) * z**2)) == 0)

# ------------------------------------------------------------------ 7. literature: Duhr-Dulat-Mistlberger ancillary file (arXiv:2007.13313v2)
# Hand transcription (verbatim structure) of the NLO entries:  a_S = alpha_s/pi ;  zb = 1-z ; G[0,zb]=ln(zb), G[1,zb]=ln(1-zb)=ln z
nc = sp.Integer(3)
zb = 1 - z
Lq = sp.Symbol('LQ')          # Log[Q2/muf2] (= Log[MH2/muf2] in Distributions.m)
G0, G1 = sp.log(zb), sp.log(1 - zb)
# Distributions.m, NLO entry (d ubar):  (8*Log[MH2/muf2]*PlusD[zb,0])/3 + (16*PlusD[zb,1])/3 - ((1440 - 120*Pi^2 - 540*Log[MH2/muf2])*delta[zb])/270
ddm_dist = Dist(delta=-(1440 - 120 * sp.pi**2 - 540 * Lq) / 270, plus={0: sp.Rational(8, 3) * Lq, 1: sp.Rational(16, 3)})
# XSReg.m, lst[[2,1]] (d ubar), V2[1,2] -> 1:
ddm_reg_qq = ((-1 + nc) * (1 + nc) * (-2 + zb) * G0) / nc - ((-1 + nc) * (1 + nc) * (2 - 2 * zb + zb**2) * G1) / (2 * nc * zb) \
             + ((-1 + nc) * (1 + nc) * (-2 + zb) * Lq) / (2 * nc)
# XSReg.m, lst[[2,2]] (g ubar), V2[1,s] -> 1:
ddm_reg_qg = -(zb * (-8 + 7 * zb)) / 8 + ((1 - 2 * zb + 2 * zb**2) * G0) / 2 - ((1 - 2 * zb + 2 * zb**2) * G1) / 4 + ((1 - 2 * zb + 2 * zb**2) * Lq) / 4
ddm_qq = (ddm_dist + Dist(reg=ddm_reg_qq)).scale(2)       # alpha_s/pi -> alpha_s/2pi units
ddm_qg = Dist(reg=ddm_reg_qg).scale(2)
ours_qq = Delta_qq.subs({CF: sp.Rational(4, 3), LF: -Lq})
ours_qg = Delta_qg.subs({TF: sp.Rational(1, 2), LF: -Lq})
c1 = dist_equal(ours_qq, ddm_qq)
c2 = dist_equal(ours_qg, ddm_qg)
report('LIT: Delta_qqbar (incl. mu_F terms) = 2 x eta^(1)_{d ubar} of Duhr-Dulat-Mistlberger JHEP 11(2020)143 ancillary files', all(c1), str(c1))
report('LIT: Delta_qg    (incl. mu_F terms) = 2 x eta^(1)_{g ubar} of Duhr-Dulat-Mistlberger JHEP 11(2020)143 ancillary files', all(c2), str(c2))

# ------------------------------------------------------------------ 8. literature: Moch-Vogt PLB 631 (2005) 48, g01 (DY) = C_F(-16 + 16 zeta2 + 8 gamma_e^2), a_s = alpha_s/(4pi)
mp.mp.dps = 30
D0 = Delta_qq.subs({LF: 0, CF: 1})
def mellin(dist, N):
    """<dist, z^{N-1}>: exact harmonic sums for D_0, D_1; regular part by quadrature with breakpoints near z=1."""
    N = int(N)
    S1 = mp.harmonic(N - 1); S2 = mp.zeta(2) - mp.zeta(2, N)
    val = mp.mpf(sp.N(dist.delta, 30))
    for k, c in dist.plus.items():
        ck = mp.mpf(sp.N(c, 30))
        if k == 0:
            val += ck * (-S1)
        elif k == 1:
            val += ck * (S1**2 + S2) / 2
        else:
            raise NotImplementedError
    if dist.reg != 0:
        f = sp.lambdify(z, dist.reg, 'mpmath')
        pts = [0, mp.mpf(1) / 2] + [1 - mp.mpf(c) / N for c in (50, 10, 3, 1, mp.mpf(1) / 10, mp.mpf(1) / 100)] + [1]
        pts = sorted(set([p for p in pts if 0 <= p <= 1]))
        cut = 1 - mp.mpf(10)**(-25)          # removable singularities (e.g. ln z/(1-z)) at z = 1
        val += mp.quad(lambda w: f(min(w, cut)) * w**(N - 1), pts)
    return val
g01 = -16 + 16 * mp.zeta(2) + 8 * mp.euler**2
devs = []
for N in [200, 2000, 20000]:
    MN = 2 * mellin(D0, N)                  # a_s units
    asym = 8 * mp.log(N)**2 + 16 * mp.euler * mp.log(N) + g01
    devs.append((N, MN - asym))
print('      large-N: 2 Delta_N - [8 ln^2 N + 16 gamma_E ln N + g01] =', [(N, mp.nstr(d, 6)) for N, d in devs])
ok_g01 = abs(devs[-1][1]) < 2e-2 and abs(devs[-1][1]) < abs(devs[0][1]) / 20
report('LIT: large-N constant of Delta_qqbar = g01^{DY} = C_F(-16+16 zeta_2+8 gamma_E^2) of Moch-Vogt (a_s=alpha_s/4pi); residual O(ln N/N)', ok_g01)
# exact Mellin of the distribution part at large N via harmonic sums: <D1, z^{N-1}> = (S1(N-1)^2 + S2(N-1))/2
Nn = 50
S1 = mp.harmonic(Nn - 1); S2 = mp.zeta(2) - mp.zeta(2, Nn)
ok_d1 = abs(Dist(plus={1: 1}).act(lambda w: w**(Nn - 1)) - (S1**2 + S2) / 2) < 1e-20
report('Mellin transform identity <D_1, z^{N-1}> = [S_1(N-1)^2 + S_2(N-1)]/2  (N=50, 20 digits)', ok_d1)

# ------------------------------------------------------------------ 9. DIS scheme (requires the MS-bar DIS coefficient functions C_2^q, C_2^g)
C2q = Dist(delta=CF * (-(sp.Rational(9, 2) + sp.pi**2 / 3)), plus={1: 2 * CF, 0: -sp.Rational(3, 2) * CF},
           reg=CF * (-(1 + z) * sp.log(1 - z) - (1 + z**2) / (1 - z) * sp.log(z) + 3 + 2 * z))
C2g = Dist(reg=TF * ((z**2 + (1 - z)**2) * sp.log((1 - z) / z) - 8 * z**2 + 8 * z - 1))
DIS_qq = (Delta_qq.subs({LF: 0}) - C2q.scale(2)).simplify()
DIS_qg = (Delta_qg.subs({LF: 0}) - C2g).simplify()
aem_qq = D1(2 * CF * (1 + z**2)) + Dist(delta=CF * (1 + 4 * sp.pi**2 / 3), plus={0: 3 * CF}, reg=CF * (-6 - 4 * z))
aem_qg = Dist(reg=TF * ((z**2 + (1 - z)**2) * sp.log(1 - z) + sp.Rational(3, 2) - 5 * z + sp.Rational(9, 2) * z**2))
report('DIS scheme: Delta^DIS_qqbar = Delta_qqbar - 2 C_2^q = C_F[(1+4pi^2/3)delta + 2(1+z^2)D_1 + 3 D_0 - 6 - 4z]', all(dist_equal(DIS_qq, aem_qq)) and all(dist_equal(DIS_qq.subs(NUM), aem_qq.subs(NUM), tests=tests)))
report('DIS scheme: Delta^DIS_qg = Delta_qg - C_2^g = T_F[(z^2+(1-z)^2) ln(1-z) + 3/2 - 5z + 9z^2/2]', all(dist_equal(DIS_qg, aem_qg)) and all(dist_equal(DIS_qg.subs(NUM), aem_qg.subs(NUM), tests=tests)))

# ------------------------------------------------------------------ 10. alternative forms used in the literature
# (a) 4(1+z^2) D_1 = 8 D_1 - 4(1+z) ln(1-z) ;  (b) plus prescription on the whole [ ] (equivalent forms)
alt = Dist(delta=CF * (2 * sp.pi**2 / 3 - 8), plus={1: 8 * CF}, reg=CF * (-4 * (1 + z) * sp.log(1 - z) - 2 * (1 + z**2) / (1 - z) * sp.log(z)))
report('equivalent form: Delta_qqbar = C_F[8 D_1 - 4(1+z)ln(1-z) - 2(1+z^2)ln z/(1-z) + (2pi^2/3-8)delta]', all(dist_equal(Delta_qq.subs({LF: 0}), alt)) and all(dist_equal(Delta_qq.subs({LF: 0}).subs(NUM), alt.subs(NUM), tests=tests)))
# first moment (N=1) and second moment numbers for reference
for N in [1, 2]:
    mq = Delta_qq.subs({LF: 0, CF: sp.Rational(4, 3)}).act(lambda w: w**(N - 1))
    mg = Delta_qg.subs({LF: 0, TF: sp.Rational(1, 2)}).act(lambda w: w**(N - 1))
    print('      Mellin moment N=%d (C_F=4/3, T_F=1/2, mu_F=Q): Delta_qq = %s, Delta_qg = %s' % (N, mp.nstr(mq, 15), mp.nstr(mg, 15)))

# ------------------------------------------------------------------ LaTeX output
def latex_dist(dd):
    return 'delta: %s ; plus: %s ; reg: %s' % (sp.latex(dd.delta), {k: sp.latex(c) for k, c in dd.plus.items()}, sp.latex(dd.reg))
with open(os.path.join(HERE, 'results_nlo.tex'), 'w') as fh:
    fh.write('%% generated by nlo_checks.py -- canonical forms, a=alpha_s/(2pi), L_F = ln(mu_F^2/Q^2)\n')
    fh.write('%% Delta_qqbar^(1): ' + latex_dist(Delta_qq) + '\n')
    fh.write('%% Delta_qg^(1):    ' + latex_dist(Delta_qg) + '\n')
    fh.write('%% virtual f(eps) = ' + sp.latex(f_closed) + '\n')
    fh.write('%% real qqbar (Pref*Greg) = ' + sp.latex(closed_qq) + '\n')
    fh.write('%% real qg (Pref*Hreg) = ' + sp.latex(closed_qg) + '\n')

print()
print('SUMMARY nlo_checks: %d/%d PASS   (%.0f s)' % (sum(ok for _, ok in RES), len(RES), time.time() - t0))
