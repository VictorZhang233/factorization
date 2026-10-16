# -*- coding: utf-8 -*-
s = open('s5_distributions.py', encoding='utf-8').read()
# --- M1 exact: replace sympy log integrals by the series identity plus an mpmath cross-check
i = s.index("# M1 Mellin table (exact)")
j = s.index("ok = True\nfor Nc in (mp.mpc(2.3, 1.1)")
s = s[:i] + r'''# M1 Mellin table: <D_0,z^{N-1}> = -S_1(N-1) (polynomial division, exact); <D_1,z^{N-1}> = sum_{m<N} S_1(m)/m
#    = (S_1^2+S_2)(N-1)/2 (exact rational identity), cross-checked by direct quadrature of the defining integrals
ok = True
mp.mp.dps = 25
for Nv in range(1, 11):
    S1 = sp.harmonic(Nv - 1); S2 = sp.harmonic(Nv - 1, 2)
    d0 = -sum(sp.Rational(1, j_ + 1) for j_ in range(0, Nv - 1))
    d1 = sum(sp.harmonic(m) / m for m in range(1, Nv))
    ok &= sp.simplify(d0 + S1) == 0 and sp.simplify(d1 - (S1**2 + S2) / 2) == 0
    q0 = mp.quad(lambda zz: (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    q1 = mp.quad(lambda zz: mp.log(1 - zz) * (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    ok &= abs(q0 - mp.mpf(sp.Rational(d0).p) / sp.Rational(d0).q) < 1e-15 and abs(q1 - mp.mpf(sp.Rational(d1).p) / sp.Rational(d1).q) < 1e-15
check('M1 <D_0,z^{N-1}> = -S_1(N-1), <D_1,z^{N-1}> = (S_1^2+S_2)(N-1)/2, N = 1..10 (exact + quadrature)', ok)
''' + s[j:]
# --- M4: numerical Mellin moments of the x-space coefficient functions vs the VF-DIS-8 table and closed forms
i = s.index("# M4 C_2 moments from x space (VF-DIS-7)")
j = s.index("# M5 convolution theorem")
s = s[:i] + r'''# M4 C_2 moments from x space (VF-DIS-7) by quadrature, vs the VF-DIS-8 table and closed forms (N = 1..8)
table_q = [0, sp.Rational(1, 6), sp.Rational(29, 24), sp.Rational(91, 40), sp.Rational(589, 180), sp.Rational(5281, 1260),
           sp.Rational(50791, 10080), sp.Rational(58703, 10080)]
table_g = [sp.Rational(1, 3), -sp.Rational(1, 4), -sp.Rational(7, 20), -sp.Rational(133, 360), -sp.Rational(23, 63),
           -sp.Rational(1777, 5040), -sp.Rational(27, 80), -sp.Rational(16231, 50400)]
TF = sp.Symbol('T_F')
okq = okg = okf = True
mp.mp.dps = 25
fr = lambda r: mp.mpf(sp.Rational(r).p) / sp.Rational(r).q
for Nv in range(1, 9):
    D0 = mp.quad(lambda zz: (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    D1 = mp.quad(lambda zz: mp.log(1 - zz) * (zz**(Nv - 1) - 1) / (1 - zz), [0, 0.5, 1])
    reg = mp.quad(lambda zz: zz**(Nv - 1) * (-(1 + zz) * mp.log(1 - zz) - (1 + zz**2) / (1 - zz) * mp.log(zz) + 3 + 2 * zz), [0, 0.5, 1])
    cq = 2 * D1 - mp.mpf(3) / 2 * D0 + reg - (mp.mpf(9) / 2 + mp.pi**2 / 3)
    okq &= abs(cq - fr(table_q[Nv - 1])) < 1e-15
    cg = mp.quad(lambda zz: zz**(Nv - 1) * ((zz**2 + (1 - zz)**2) * mp.log((1 - zz) / zz) - 8 * zz**2 + 8 * zz - 1), [0, 0.5, 1])
    okg &= abs(cg - fr(table_g[Nv - 1])) < 1e-15
    S1N = sp.harmonic(Nv); S2N = sp.harmonic(Nv, 2)
    fq = S1N**2 - S2N + sp.Rational(3, 2) * S1N - S1N / (Nv * (Nv + 1)) + sp.Rational(3, 2 * Nv) + sp.Rational(2, Nv + 1) + sp.Rational(1, Nv**2) - sp.Rational(9, 2)
    fg = -sp.Rational(Nv**2 + Nv + 2, Nv * (Nv + 1) * (Nv + 2)) * S1N + sp.Rational(1, Nv**2) - sp.Rational(1, Nv) + sp.Rational(6, (Nv + 1) * (Nv + 2))
    okf &= sp.simplify(fq - table_q[Nv - 1]) == 0 and sp.simplify(fg - table_g[Nv - 1]) == 0
check('M4 C_2^q moments from the x-space form (quadrature) = VF-DIS-8 table, N = 1..8', okq)
check('M4 C_2^g moments from the x-space form (quadrature) = VF-DIS-8 table, N = 1..8', okg)
check('M4 closed forms of C^q_{2,N}, C^g_{2,N} (VF-DIS-8) reproduce the table', okf)
''' + s[j:]
# --- A3: c_k by quadrature instead of sympy log integrals
s = s.replace("""c1 = sp.integrate((1 + zz_**2 - 2) * sp.log(1 - zz_) / (1 - zz_), (zz_, 0, 1))
c0 = sp.integrate((1 + zz_**2 - 2) / (1 - zz_), (zz_, 0, 1))
check('A3 c_1[1+z^2] = 7/4 (VF-DY-12), c_0[1+z^2] = -3/2 (so (1+z^2)D_0 = [(1+z^2)/(1-z)]_+ - 3/2 delta)',
      sp.simplify(c1 - sp.Rational(7, 4)) == 0 and sp.simplify(c0 + sp.Rational(3, 2)) == 0, 'c1=%s, c0=%s' % (c1, c0))""",
"""c1 = mp.quad(lambda zz: (zz**2 - 1) * mp.log(1 - zz) / (1 - zz), [0, 0.5, 1])
c0 = mp.quad(lambda zz: (zz**2 - 1) / (1 - zz), [0, 0.5, 1])
uu = sp.Symbol('u', positive=True)
c1x = sp.integrate(-(2 - uu) * sp.log(uu), (uu, 0, 1))       # u = 1 - z: (z^2-1)/(1-z) = -(1+z) = -(2-u)
check('A3 c_1[1+z^2] = 7/4 (VF-DY-12), c_0[1+z^2] = -3/2 (so (1+z^2)D_0 = [(1+z^2)/(1-z)]_+ - 3/2 delta)',
      abs(c1 - mp.mpf(7) / 4) < 1e-15 and abs(c0 + mp.mpf(3) / 2) < 1e-15 and sp.simplify(c1x - sp.Rational(7, 4)) == 0,
      'c1=%s (exact %s), c0=%s' % (mp.nstr(c1, 12), c1x, mp.nstr(c0, 12)))""")
open('s5_distributions.py', 'w', encoding='utf-8').write(s)
print('patched')
