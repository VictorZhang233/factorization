"""
e26_logs.py -- stage-2 verifier (batch E26_s2), claim E26.
Default value of the QCDF endpoint parameters X_H, X_A = ln(m/Lambda_h), Lambda_h = 0.5 GeV:
only m = m_B (or m_b) gives ~2.4; any light-meson mass M gives a negative or ~0 logarithm.
Run: python3 -I e26_logs.py
"""
import math
Lh = 0.5
for name, m in [('m_B = 5.2793 GeV (B0)', 5.2793), ('m_B = 5.28 GeV', 5.28), ('m_b(pole) = 4.8 GeV', 4.8),
                ('m_b(MSbar, m_b) = 4.2 GeV', 4.2), ('m_pi = 0.13957 GeV', 0.13957), ('m_K = 0.49368 GeV', 0.49368),
                ('m_rho = 0.775 GeV', 0.775), ('m_K* = 0.892 GeV', 0.892)]:
    print('ln(%-26s / 0.5 GeV) = %+.4f' % (name, math.log(m / Lh)))
