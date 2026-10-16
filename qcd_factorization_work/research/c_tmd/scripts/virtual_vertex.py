# Virtual vertex graph of the unsubtracted TMD (quark target, massless on-shell p = (p+,0,0_T)) with a
# NON-light-like time-like Wilson-line direction n (n^2 > 0, n.p > 0), Feynman gauge, pure DR.
#   SIDIS (future-pointing line, factor g n^mu/(n.l - i0)),  DY (past-pointing, g n^mu/(n.l + i0)):
#   V = i g^2 C_F mu^{2eps} int d^Dl/(2pi)^D N(l) / [(n.l -/+ i0)(l^2+i0)((p-l)^2+i0)],
#   N(l) = ubar gamma^+ (pslash - lslash) nslash u / (ubar gamma^+ u).
# Results (derived in DERIVATION.md Sec. 3.4):
#   V_SIDIS = -(alpha_s C_F/4pi) (pi mu^2 n^2/(p.n)^2)^eps * 2 Gamma(1+eps) [ B(-2e,2) B(-e,1+2e) - B(1-e,2e)/(1-2e) ]
#           = -(alpha_s C_F/4pi) (pi mu^2 n^2/(p.n)^2)^eps Gamma(1-e)Gamma(1+2e)(1-e)/((1-2e) e^2)
#   V_DY    = +(alpha_s C_F/4pi) (pi mu^2 n^2/(p.n)^2)^eps * 2 Gamma(1+eps) [ B(-2e,2)(e^{i pi(1+e)}B(-e,-e)+B(1+2e,-e))
#                                                                     + (e^{i pi(1+e)}B(1-e,-e)+B(2e,-e))/(1-2e) ]
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from dirac import Dots, trace, D
mp.mp.dps = 30
ok = True

# ---- (1) numerator reduction: N(l) = Tr[pslash g+ (p-l)slash nslash]/Tr[pslash g+]  (spin sum; helicity conserving) ----
pp, npl, nmi, lp, lm, lT2, x, lam = sp.symbols('p_plus n_plus n_minus l_plus l_minus lT2 x lambda')
# vectors: p=(pp,0,0), n=(npl,nmi,0), l=(lp,lm,lT), v: v.a = a^+  (gamma^+ = vslash), lT transverse, l.l = 2 lp lm - lT2
tab = {('p', 'p'): 0, ('p', 'n'): pp * nmi, ('p', 'l'): pp * lm, ('p', 'v'): pp,
       ('n', 'n'): 2 * npl * nmi, ('n', 'l'): npl * lm + nmi * lp, ('n', 'v'): npl,
       ('l', 'l'): 2 * lp * lm - lT2, ('l', 'v'): lp, ('v', 'v'): 0}
dot = Dots(tab)
num = trace(['p', 'v', 'p', 'n'], dot) - trace(['p', 'v', 'l', 'n'], dot)
N = sp.simplify(num / trace(['p', 'v'], dot))
N_claim = 2 * tab[('p', 'n')] - 2 * tab[('n', 'l')] + sp.simplify(trace(['p', 'v', 'n', 'l'], dot) / trace(['p', 'v'], dot))
print('(1) N(l) =', sp.factor(N), ' ; equals 2p.n - 2n.l + T(l):', sp.simplify(N - N_claim) == 0)
ok &= sp.simplify(N - N_claim) == 0
# evaluate at the shifted momentum l = x p + lam n/2 (SIDIS) and l = x p - lam n/2 (DY): only these survive (N linear in l)
def at(lvec):
    lp_, lm_, lT2_ = lvec
    return sp.simplify(N.subs({lp: lp_, lm: lm_, lT2: lT2_}))
NS = at((x * pp + lam * npl / 2, lam * nmi / 2, 0))
ND = at((x * pp - lam * npl / 2, -lam * nmi / 2, 0))
pn, n2 = pp * nmi, 2 * npl * nmi
print('    SIDIS: N(xp + lam n/2) =', sp.factor(NS), '  claim 2(1-x)p.n - lam n^2/2:', sp.simplify(NS - (2 * (1 - x) * pn - lam * n2 / 2)) == 0)
print('    DY   : N(xp - lam n/2) =', sp.factor(ND), '  claim 2(1-x)p.n + lam n^2/2:', sp.simplify(ND - (2 * (1 - x) * pn + lam * n2 / 2)) == 0)
ok &= sp.simplify(NS - (2 * (1 - x) * pn - lam * n2 / 2)) == 0 and sp.simplify(ND - (2 * (1 - x) * pn + lam * n2 / 2)) == 0

# ---- (2) Beta-function integrals, each checked numerically inside its own convergence domain ----
B = lambda a, b: mp.gamma(a) * mp.gamma(b) / mp.gamma(a + b)
chk = [
    ('int_0^inf t^(-1-e)(1+t)^(-1-e) = B(-e,1+2e)', mp.mpf('-0.3'), lambda e: mp.quad(lambda t: t**(-1 - e) * (1 + t)**(-1 - e), [0, 1, mp.inf]), lambda e: B(-e, 1 + 2 * e)),
    ('int_0^inf t^(-e)(1+t)^(-1-e)   = B(1-e,2e)', mp.mpf('0.3'), lambda e: mp.quad(lambda t: t**(-e) * (1 + t)**(-1 - e), [0, 1, mp.inf]), lambda e: B(1 - e, 2 * e)),
    ('int_0^1 x^(-1-2e)(1-x)         = B(-2e,2)', mp.mpf('-0.3'), lambda e: mp.quad(lambda t: t**(-1 - 2 * e) * (1 - t), [0, 1]), lambda e: B(-2 * e, 2)),
    ('int_0^1 t^(-1-e)(1-t)^(-1-e)   = B(-e,-e)', mp.mpf('-0.3'), lambda e: mp.quad(lambda t: t**(-1 - e) * (1 - t)**(-1 - e), [0, 0.5, 1]), lambda e: B(-e, -e)),
    ('int_1^inf t^(-1-e)(t-1)^(-1-e) = B(1+2e,-e)', mp.mpf('-0.3'), lambda e: mp.quad(lambda t: t**(-1 - e) * (t - 1)**(-1 - e), [1, 2, mp.inf]), lambda e: B(1 + 2 * e, -e)),
    ('int_1^inf t^(-e)(t-1)^(-1-e)   = B(2e,-e)  ', mp.mpf('-0.1'), lambda e: mp.quad(lambda t: t**(-e) * (t - 1)**(-1 - e), [1, 2, mp.inf]), lambda e: B(2 * e, -e)),
]
print('(2) Beta integrals:')
for name, ev, num_f, ana_f in chk:
    if name.startswith('int_1^inf t^(-e)'):
        # no common convergence strip (t->1 needs e<0, t->inf needs e>0): continue the t->1 end by subtraction,
        # int_1^2 t^-e (t-1)^(-1-e) = int_1^2 (t^-e - 1)(t-1)^(-1-e) + int_0^1 u^(-1-e) du,  the last = -1/e (continued)
        e = mp.mpf('0.2')
        val = (mp.quad(lambda t: (t**(-e) - 1) * (t - 1)**(-1 - e), [1, 2]) - 1 / e
               + mp.quad(lambda t: t**(-e) * (t - 1)**(-1 - e), [2, mp.inf]))
        good = abs(val - B(2 * e, -e)) < mp.mpf('1e-9')
        print('   %s  (e=0.2, continued at t=1): numeric %s  analytic %s  %s' % (name, mp.nstr(val, 15), mp.nstr(B(2 * e, -e), 15), 'ok' if good else 'MISMATCH'))
        ok &= good
        continue
    l_, r_ = num_f(ev), ana_f(ev)
    good = abs(l_ - r_) < mp.mpf('1e-9') * max(1, abs(r_))
    ok &= good
    print('   %s  (e=%s): numeric %s  analytic %s  %s' % (name, mp.nstr(ev, 2), mp.nstr(l_, 15), mp.nstr(r_, 15), 'ok' if good else 'MISMATCH'))

# ---- (3) closed forms; future (SIDIS) vs past (DY) pointing; time-like vs space-like n ----------------
# space-like n (n^2 = -|n^2|, p.n > 0; Collins 2011): same algebra with t-substitution lambda = 4x p.n t/|n^2|:
#   V_SIDIS^sp = -(.)^eps 2G(1+e){ B(-2e,2)[B(-e,-e) + e^{i pi(1+e)} B(1+2e,-e)] + [B(1-e,-e) + e^{i pi(1+e)} B(2e,-e)]/(1-2e) }
#   V_DY^sp    = +(.)^eps 2G(1+e) e^{i pi(1+e)} [ B(-2e,2) B(-e,1+2e) - B(1-e,2e)/(1-2e) ]        (.) = (alpha_s C_F/4pi)(pi mu^2|n^2|/(p.n)^2)
ph = lambda e: mp.e**(1j * mp.pi * (1 + e))
def bracket_S(e):
    return 2 * mp.gamma(1 + e) * (B(-2 * e, 2) * B(-e, 1 + 2 * e) - B(1 - e, 2 * e) / (1 - 2 * e))
def closed_S(e):
    return mp.gamma(1 - e) * mp.gamma(1 + 2 * e) * (1 - e) / ((1 - 2 * e) * e**2)
def cD_time(e):
    return +2 * mp.gamma(1 + e) * (B(-2 * e, 2) * (ph(e) * B(-e, -e) + B(1 + 2 * e, -e)) + (ph(e) * B(1 - e, -e) + B(2 * e, -e)) / (1 - 2 * e))
def cS_space(e):
    return -2 * mp.gamma(1 + e) * (B(-2 * e, 2) * (B(-e, -e) + ph(e) * B(1 + 2 * e, -e)) + (B(1 - e, -e) + ph(e) * B(2 * e, -e)) / (1 - 2 * e))
def cD_space(e):
    return +2 * mp.gamma(1 + e) * ph(e) * (B(-2 * e, 2) * B(-e, 1 + 2 * e) - B(1 - e, 2 * e) / (1 - 2 * e))
print('(3) V = (alpha_s C_F/4pi)(pi mu^2 |n^2|/(p.n)^2)^eps * c(eps)')
for e in [mp.mpf('0.17'), mp.mpf('-0.23'), mp.mpf('0.41'), mp.mpf('-0.07')]:
    cS = -bracket_S(e)
    g1 = abs(bracket_S(e) - closed_S(e)) < mp.mpf('1e-20')                       # closed form (time-like SIDIS)
    g2 = abs(cS_space(e) - mp.conj(cD_space(e))) < mp.mpf('1e-20')               # space-like: V_SIDIS = (V_DY)^*
    ok &= g1 and g2
    print('   eps=%5s: time-like c_SIDIS=%s (closed form ok:%s), Re c_DY - c_SIDIS = %s | space-like c_SIDIS=%s, c_DY=%s, c_SIDIS=conj(c_DY): %s' % (
        mp.nstr(e, 3), mp.nstr(cS, 12), g1, mp.nstr(mp.re(cD_time(e)) - cS, 8), mp.nstr(cS_space(e), 10), mp.nstr(cD_space(e), 10), g2))
for e in [mp.mpf('1e-6'), mp.mpf('-1e-7')]:
    d = mp.re(cD_time(e)) + bracket_S(e)
    print('   eps=%s: time-like  Re c_DY - c_SIDIS = %s   (2 pi^2 = %s)' % (mp.nstr(e, 2), mp.nstr(d, 12), mp.nstr(2 * mp.pi**2, 12)))
    ok &= abs(d - 2 * mp.pi**2) < mp.mpf('1e-4')
print('    => space-like lines: 2Re V identical for future/past pointing (PT invariance; path order = time order for space-like paths).')
print('       time-like lines: the past-pointing time-ordered line carries a Coulomb phase, Re V_DY - V_SIDIS -> 2 pi^2 (alpha_s C_F/4pi):')
print('       path ordering (= anti-time ordering) and the time ordering of Feynman rules differ for past-pointing time-like lines.')
print('       All of these are proportional to (|n^2|)^eps and vanish in the light-like limit taken first (Re eps > 0).')

# ---- (4) epsilon expansion (binding MSbar) and the light-like limit --------------------------------
eps, ell = sp.symbols('epsilon ell')    # ell = ln(Lambda^2/mu^2),  Lambda^2 = 4 (p.n)^2/n^2 = 2 (p^+)^2 e^{-2 y_B} for n = n_B
Vs = -sp.exp(-eps * ell) * sp.exp(sp.EulerGamma * eps) * sp.gamma(1 - eps) * sp.gamma(1 + 2 * eps) * (1 - eps) / ((1 - 2 * eps) * eps**2)
ser = sp.expand(sp.series(Vs, eps, 0, 1).removeO())
print('(4) V_SIDIS/((alpha_s C_F/4pi) S_eps) =', sp.collect(ser, eps))
expect = -(1 / eps**2 + (1 - ell) / eps + 2 + 5 * sp.pi**2 / 12 - ell + ell**2 / 2)
ok &= sp.simplify(ser - sp.expand(expect)) == 0
print('    = -[1/eps^2 + (1-ell)/eps + 2 + 5pi^2/12 - ell + ell^2/2] :', sp.simplify(ser - sp.expand(expect)) == 0)
print('    UV pole (large-l power counting, n-independent): +1/eps  =>  IR part: -[1/eps^2 + (2-ell)/eps + ...]')
print('    light-like limit y_B -> -inf (ell -> +inf) at fixed eps: |(mu^2/Lambda^2)^eps| -> 0 for Re eps > 0;')
print('    the eps-expanded form instead grows like ell^2/2: the limits do not commute (Collins 2011 Sec.10.8/10.11.1, per Collins-Rogers 2013).')
for e in [0.05, 0.1]:
    vals = [mp.nstr(abs(mp.e**(-e * L) * closed_S(mp.mpf(e))), 6) for L in (10, 40, 160)]
    print('    eps=%.2f : |V| at ell = 10, 40, 160 ->' % e, vals)
print('virtual vertex checks:', 'PASS' if ok else 'FAIL')
