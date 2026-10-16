# R-M10 independent check: first moments of the NLO non-singlet splitting functions P^(1)+-,
# coded from Moch-Vermaseren-Vogt, NPB 688 (2004) 101, eqs. (4.6)-(4.7) [= CFP 1980 / Curci:1980uw],
# normalisation d q/d ln mu^2 = sum_n a_s^{n+1} P^(n) (x) (x) q,  a_s = alpha_s/(4 pi).
# Convert to the monograph's (alpha_s/2pi)^2 normalisation by dividing P^(1)_MVV by 4.
# All 1/(1-x) singularities are +-distributions (MVV, after eq. (4.7)); delta(1-x) terms added explicitly.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
z2, z3 = mp.zeta(2), mp.zeta(3)

# harmonic polylogarithms (Remiddi-Vermaseren), weights <= 2
H0 = lambda x: mp.log(x)
H00 = lambda x: mp.log(x)**2 / 2
Hm10 = lambda x: mp.log(x) * mp.log(1 + x) + mp.polylog(2, -x)
H10 = lambda x: -mp.log(x) * mp.log(1 - x) - mp.polylog(2, x)
H2 = lambda x: mp.polylog(2, x)          # H_{0,1}
pqq = lambda x: 2 / (1 - x) - 1 - x

# check the HPL closed forms against their defining integrals
for x in [mp.mpf('0.3'), mp.mpf('0.77')]:
    assert abs(Hm10(x) - mp.quad(lambda t: mp.log(t) / (1 + t), [0, x])) < 1e-25
    assert abs(H10(x) - mp.quad(lambda t: mp.log(t) / (1 - t), [0, x])) < 1e-25
    assert abs(H2(x) - mp.quad(lambda t: -mp.log(1 - t) / t, [0, x])) < 1e-25

def moment(reg, sing_coef, delta, N):
    """int_0^1 x^{N-1} [ reg(x) + sing_coef * (2/(1-x))_+ ] dx + delta,
    where reg is regular (integrable) and the +-prescription acts on 2/(1-x) times the constant sing_coef."""
    r = mp.quad(lambda x: x**(N - 1) * reg(x), [0, mp.mpf(1) / 2, 1])
    s = sing_coef * mp.quad(lambda x: 2 * (x**(N - 1) - 1) / (1 - x), [0, 1])
    return r + s + delta

def P1p_parts():
    # CA CF part: 4*( pqq(x)[67/18 - z2 + 11/6 H0 + H00] + pqq(-x)[z2 + 2Hm10 - H00] + 14/3 (1-x) + d[17/24 + 11/3 z2 - 3 z3] )
    def ca_reg(x):
        # pqq(x)*(11/6 H0 + H00) is integrable at x=1 (H0, H00 vanish there); the constant (67/18 - z2) multiplies
        # pqq(x) = 2/(1-x) - (1+x): keep -(1+x)*const in reg, 2/(1-x)*const as +-distribution
        return 4 * (pqq(x) * (mp.mpf(11) / 6 * H0(x) + H00(x)) - (1 + x) * (mp.mpf(67) / 18 - z2)
                    + pqq(-x) * (z2 + 2 * Hm10(x) - H00(x)) + mp.mpf(14) / 3 * (1 - x))
    ca = (ca_reg, 4 * (mp.mpf(67) / 18 - z2), 4 * (mp.mpf(17) / 24 + mp.mpf(11) / 3 * z2 - 3 * z3))
    # CF nf part: -4*( pqq(x)[5/9 + 1/3 H0] + 2/3 (1-x) + d[1/12 + 2/3 z2] )
    def nf_reg(x):
        return -4 * (pqq(x) * H0(x) / 3 - (1 + x) * mp.mpf(5) / 9 + mp.mpf(2) / 3 * (1 - x))
    nf = (nf_reg, -4 * mp.mpf(5) / 9, -4 * (mp.mpf(1) / 12 + mp.mpf(2) / 3 * z2))
    # CF^2 part: 4*( 2 pqq(x)[H10 - 3/4 H0 + H2] - 2 pqq(-x)[z2 + 2 Hm10 - H00] - (1-x)[1 - 3/2 H0] - H0 - (1+x) H00 + d[3/8 - 3 z2 + 6 z3] )
    # note H10 - 3/4 H0 + H2 -> 0 at x = 1? H10(1) = -Li2(1) + lim(-ln x ln(1-x)) = -z2, H2(1) = z2: sum 0, regular.
    def cf_reg(x):
        return 4 * (2 * pqq(x) * (H10(x) - mp.mpf(3) / 4 * H0(x) + H2(x)) - 2 * pqq(-x) * (z2 + 2 * Hm10(x) - H00(x))
                    - (1 - x) * (1 - mp.mpf(3) / 2 * H0(x)) - H0(x) - (1 + x) * H00(x))
    cf = (cf_reg, mp.mpf(0), 4 * (mp.mpf(3) / 8 - 3 * z2 + 6 * z3))
    return {'CA*CF': ca, 'CF*nf': nf, 'CF^2': cf}

# P^(1)- - P^(1)+ = 16 CF (CF - CA/2) * D(x),  D = pqq(-x)[z2 + 2Hm10 - H00] - 2(1-x) - (1+x) H0   (regular)
D = lambda x: pqq(-x) * (z2 + 2 * Hm10(x) - H00(x)) - 2 * (1 - x) - (1 + x) * H0(x)

parts = P1p_parts()
print('First moments (MVV normalisation a_s = alpha_s/4pi):')
mom1p = {k: moment(*v, N=1) for k, v in parts.items()}
intD = mp.quad(D, [0, mp.mpf(1) / 2, 1])
mom1m = dict(mom1p)
mom1m['CF^2'] += 16 * intD
mom1m['CA*CF'] += -8 * intD
for k in parts:
    print('  %-6s  int P(1)+ = %s   int P(1)- = %s' % (k, mp.nstr(mom1p[k], 15), mp.nstr(mom1m[k], 15)))
ok = all(abs(v) < 1e-20 for v in mom1m.values())
print('  quark-number conservation: int P(1)- = 0 for every colour factor:', ok)

# P^V(1)_{q qbar} in (alpha_s/2pi)^2 normalisation: P+ - P- = 2 P^V_{qqbar}  =>  P^V(1)_{qqbar,MVV} = -8 CF(CF-CA/2) D(x)
# => P^V(1)_{qqbar,(as/2pi)^2} = -2 CF(CF-CA/2) D(x)
val = -2 * intD
print('int_0^1 P^V(1)_{q qbar} / [CF (CF - CA/2)]  (alpha_s/2pi)^2 normalisation =', mp.nstr(val, 15))
print('13/4 - 3 zeta2 + 2 zeta3                                                =', mp.nstr(mp.mpf(13) / 4 - 3 * z2 + 2 * z3, 15))
print('agreement:', abs(val - (mp.mpf(13) / 4 - 3 * z2 + 2 * z3)) < 1e-20)
# same function as CFP/ESW form 2 pqq(-x) S2(x) + 2(1+x) ln x + 4(1-x)?
S2 = lambda x: -2 * mp.polylog(2, -x) + mp.log(x)**2 / 2 - 2 * mp.log(x) * mp.log(1 + x) - mp.pi**2 / 6
esw = lambda x: 2 * pqq(-x) * S2(x) + 2 * (1 + x) * mp.log(x) + 4 * (1 - x)
print('max |-2D(x) - ESW form| on test points:',
      mp.nstr(max(abs(-2 * D(x) - esw(x)) for x in [mp.mpf('0.01'), mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('0.999')]), 5))
# For SU(3): CF(CF-CA/2) = (4/3)(4/3-3/2) = -2/9
print('SU(3): int P^V(1)_{qqbar} =', mp.nstr(val * mp.mpf(4) / 3 * (mp.mpf(4) / 3 - mp.mpf(3) / 2), 12),
      ' ; int P^+(1)_ns = 2*that =', mp.nstr(2 * val * mp.mpf(4) / 3 * (mp.mpf(4) / 3 - mp.mpf(3) / 2), 12), ' (alpha_s/2pi)^2 units')
# Mellin moments N = 1..4 of P^+ - P^- (as/2pi)^2 normalisation = 2 int x^{N-1} P^V_{qqbar}
for N in range(1, 5):
    print('  N=%d: int x^{N-1} P^V(1)_{qqbar}/(CF(CF-CA/2)) = %s' % (N, mp.nstr(-2 * mp.quad(lambda x: x**(N - 1) * D(x), [0, 0.5, 1]), 15)))
