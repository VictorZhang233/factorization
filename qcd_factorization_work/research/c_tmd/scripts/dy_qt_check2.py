# Robustness variant of dy_qt_check.py: second kinematic point and different PDF shapes, plus controls in which
# A1 or B1 is altered (the ratio must then fail to approach 1).  Same formulas as dy_qt_check.py.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.integrate import quad
import dy_qt_check as base                      # reuses msq_qqbar, msq_qg, constants (prints its own run first)

CF, TF, Nc = base.CF, base.TF, base.Nc
def run(Q, y, rs, qf, qbf, gf, A1=CF, B1=-1.5 * CF):
    base.q_, base.qb, base.gl = qf, qbf, gf
    def css(qT):
        s = rs**2; xA, xB = Q / rs * np.exp(y), Q / rs * np.exp(-y)
        sigma0 = 4 * np.pi * base.alpha**2 / (3 * Nc * Q * Q * s)
        L = np.log(Q * Q / qT**2)
        qq = sigma0 * base.alphas / (2 * np.pi) / qT**2 * ((2 * A1 * L + 2 * B1) * qf(xA) * qbf(xB)
                                                          + base.conv_qq(qf, xA) * qbf(xB) + qf(xA) * base.conv_qq(qbf, xB))
        qg = sigma0 * base.alphas / (2 * np.pi) / qT**2 * base.conv_qg(gf, xA) * qbf(xB)
        return qq, qg
    out = []
    for qT in [Q * 1e-2, Q * 1e-3, Q * 1e-4]:
        ex = base.exact(Q, y, qT, rs)
        cq, cg = css(qT)
        out.append((qT / Q, ex['qqbar'] / cq, ex['qg'] / cg))
    return out

qf = lambda x: 1.7 * x**-0.45 * (1 - x)**2.5 * (1 + 3 * x)
qbf = lambda x: 0.3 * x**-0.35 * (1 - x)**7
gf = lambda x: 1.2 * x**-1.1 * (1 - x)**4 * (1 + x)
ok = True
print('\nconfiguration 2: Q=50, y=-0.7, sqrt(s)=500, different PDF shapes')
r = run(50.0, -0.7, 500.0, qf, qbf, gf)
for (rq, a, b) in r:
    print('   qT/Q=%.0e  exact/CSS-expansion  qqbar: %.7f   qg: %.7f' % (rq, a, b))
ok &= abs(r[-1][1] - 1) < 1e-4 and abs(r[-1][2] - 1) < 1e-4
nominal = abs(r[-1][1] - 1)
for lab, kw in [('A1 -> 0.9 C_F', dict(A1=0.9 * CF)), ('B1 -> -1.4 C_F', dict(B1=-1.4 * CF)), ('B1 -> -C_F', dict(B1=-1.0 * CF))]:
    rc = run(50.0, -0.7, 500.0, qf, qbf, gf, **kw)
    print('   control %-14s: qqbar ratio at qT/Q=1e-4 = %.6f  (|r-1| = %.1e vs nominal %.1e)' % (lab, rc[-1][1], abs(rc[-1][1] - 1), nominal))
    ok &= abs(rc[-1][1] - 1) > 1e3 * nominal
print('robustness check:', 'PASS' if ok else 'FAIL')
