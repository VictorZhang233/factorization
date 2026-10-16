# Fixed-order O(alpha_s) Drell-Yan q_T distribution vs. the O(alpha_s) expansion of the CSS formula.
# Exact (q_T > 0):  dsigma/(dQ^2 dy d^2qT) = sum_ab int dxa/|xa s - sqrt(s) MT e^y| fa fb
#                     (alpha/(3 pi Q^2)) (1/(2 shat)) (1/(8 pi^2)) avg|M|^2
# CSS at O(alpha_s), q_T>0 (DERIVATION.md Sec. 6):
#   dsigma/(dQ^2 dy dqT^2) = sigma0 (alpha_s/2pi)(1/qT^2) { [2 A1 ln(Q^2/qT^2) + 2 B1] q(xA) qb(xB)
#                              + (P_qq x q)(xA) qb(xB) + q(xA)(P_qq x qb)(xB) + (P_qg x g)(xA) qb(xB) }
#   with A1 = C_F, B1 = -3 C_F/2 (units alpha_s/pi), sigma0 = 4 pi alpha^2/(3 N_c Q^2 s).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy.integrate import quad

Nc, CF, TF = 3.0, 4.0 / 3.0, 0.5
alpha, alphas, eq = 1.0, 1.0, 1.0          # overall normalizations cancel in the ratio
g2, e2 = 4 * np.pi * alphas, 4 * np.pi * alpha

q_ = lambda x: x**-0.3 * (1 - x)**3                 # quark in A
qb = lambda x: 0.5 * x**-0.2 * (1 - x)**5           # antiquark in B
gl = lambda x: 2.0 * x**-0.9 * (1 - x)**5           # gluon in A

def msq_qqbar(s, t, u, Q2):   # spin/colour averaged
    return e2 * eq**2 * g2 * CF / Nc * 2 * (t / u + u / t + 2 * Q2 * s / (t * u))
def msq_qg(s, t, u, Q2):      # q(pa) g(pb) -> gamma* q ; t=(pa-q)^2, u=(pb-q)^2 ; averaged
    return -e2 * eq**2 * g2 * TF / Nc * 2 * (s / t + t / s + 2 * Q2 * u / (s * t))

def exact(Q, y, qT, rs):
    s = rs**2; Q2 = Q * Q; MT = np.sqrt(Q2 + qT**2)
    xamin = (rs * MT * np.exp(y) - Q2) / (s - rs * MT * np.exp(-y))
    def integrand(xa, chan):
        den = xa * s - rs * MT * np.exp(y)
        xb = (xa * rs * MT * np.exp(-y) - Q2) / den
        if xb <= 0 or xb >= 1:
            return 0.0
        sh = xa * xb * s
        ta = Q2 - xa * rs * MT * np.exp(-y)     # (pa - q)^2
        tb = Q2 - xb * rs * MT * np.exp(y)      # (pb - q)^2
        if chan == 'qqbar':   # q(A) qbar(B); |M|^2 symmetric in t<->u
            m = msq_qqbar(sh, ta, tb, Q2); f = q_(xa) * qb(xb)
        else:                 # g(A) qbar(B) -> gamma* qbar : = q(pb) g(pa) by C; t=(p_quark-q)^2=tb, u=(p_gluon-q)^2=ta
            m = msq_qg(sh, tb, ta, Q2); f = gl(xa) * qb(xb)
        return f / abs(den) * (alpha / (3 * np.pi * Q2)) / (2 * sh) / (8 * np.pi**2) * m
    out = {}
    xA = Q / rs * np.exp(y)
    for chan in ('qqbar', 'qg'):
        v, _ = quad(integrand, xamin, 1, args=(chan,), points=[xA, min(1, xA * 1.0001), min(1, xA * 1.01)], limit=2000, epsabs=0, epsrel=1e-10)
        out[chan] = np.pi * v          # dsigma/dqT^2 = pi dsigma/d^2qT
    return out

def conv_qq(f, x):
    a, _ = quad(lambda z: (1 + z * z) / (1 - z) * (f(x / z) / z - f(x)), x, 1, limit=400)
    return CF * (a - f(x) * (-x - x * x / 2 - 2 * np.log(1 - x)))
def conv_qg(f, x):
    a, _ = quad(lambda z: TF * (z * z + (1 - z)**2) * f(x / z) / z, x, 1, limit=400)
    return a

def css(Q, y, qT, rs):
    s = rs**2; xA, xB = Q / rs * np.exp(y), Q / rs * np.exp(-y)
    sigma0 = 4 * np.pi * alpha**2 / (3 * Nc * Q * Q * s) * eq**2
    A1, B1 = CF, -1.5 * CF
    L = np.log(Q * Q / qT**2)
    qqbar = sigma0 * alphas / (2 * np.pi) / qT**2 * ((2 * A1 * L + 2 * B1) * q_(xA) * qb(xB)
                                                     + conv_qq(q_, xA) * qb(xB) + q_(xA) * conv_qq(qb, xB))
    qg = sigma0 * alphas / (2 * np.pi) / qT**2 * conv_qg(gl, xA) * qb(xB)
    return {'qqbar': qqbar, 'qg': qg}

Q, y, rs = 10.0, 0.3, 200.0
print('Q=%.1f  y=%.2f  sqrt(s)=%.1f   ratio exact/CSS-expansion  (-> 1 as qT -> 0)' % (Q, y, rs))
rows = []
for qT in [2.0, 1.0, 0.3, 0.1, 0.03, 0.01]:
    ex, cs = exact(Q, y, qT, rs), css(Q, y, qT, rs)
    r1, r2 = ex['qqbar'] / cs['qqbar'], ex['qg'] / cs['qg']
    rows.append((qT, r1, r2))
    print('  qT/Q=%.4f   qqbar: %.6f    qg: %.6f' % (qT / Q, r1, r2))
# quantify approach to 1: deviation should scale like (qT/Q)^p log
d = [(abs(r[1] - 1), abs(r[2] - 1)) for r in rows]
ok = d[-1][0] < 2e-3 and d[-1][1] < 2e-3 and d[-1][0] < d[2][0] and d[-1][1] < d[2][1]
print('CSS O(alpha_s) expansion reproduces fixed-order small-qT asymptotics (A1=C_F, B1=-3C_F/2):', 'PASS' if ok else 'FAIL')
# wrong-coefficient control: B1 -> 0 must fail
print('control: with B1=0 the qqbar ratio at qT/Q=1e-3 would be', end=' ')
qT = 0.01; s = rs**2; xA, xB = Q / rs * np.exp(y), Q / rs * np.exp(-y); L = np.log(Q * Q / qT**2)
sigma0 = 4 * np.pi * alpha**2 / (3 * Nc * Q * Q * s)
alt = sigma0 * alphas / (2 * np.pi) / qT**2 * ((2 * CF * L) * q_(xA) * qb(xB) + conv_qq(q_, xA) * qb(xB) + q_(xA) * conv_qq(qb, xB))
print('%.4f (i.e. clearly != 1)' % (exact(Q, y, qT, rs)['qqbar'] / alt))
