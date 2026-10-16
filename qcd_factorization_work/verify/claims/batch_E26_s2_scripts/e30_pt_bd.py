"""
e30_pt_bd.py -- stage-2 verifier (batch E26_s2), claim E30 (T-odd TMDs: SIDIS vs DY sign).

Check of the Dirac-structure signs in the PT argument with Collins' OWN conventions of 1993
(hep-ph/9208213v2, appendix): Bjorken-Drell representation, antiunitary PT with
   (PT)^-1 psi(x) PT = M psi(-x),   M = i gamma^0 gamma^1 gamma^3.
(The stage-1 check used the Weyl representation with a matrix solved for; this one uses Collins' matrix.)

Derivation used (antiunitary V = PT, V^-1 |P,S> ~ |P,-S>, momenta unchanged):
  <P,S| psibar(0) G W psi(y) |P,S> = <P,-S| V^-1 [psibar(0) G W psi(y)] V |P,-S>^*
                                  = <P,-S| psibar(0) G' W' psi(-y) |P,-S>^*,  G' = g0 M^dag g0 G^* M
  then <X|O|X>^* = <X|O^dag|X> and translation by y give
  Phi^[G]_W(x,k_T;S) = Phi^[G'']_W~(x,k_T;-S),  G'' = g0 G'^dag g0,   W~ = PT image (future <-> past).
  If G'' = eta_G G:  future-pointing  Phi^[G](S) = eta_G * past-pointing Phi^[G](-S).
Expected: eta = +1 for gamma^+ (f1 even; Sivers term ~ eps k S f_1T^perp odd in S -> f_1T^perp flips),
          eta = -1 for i sigma^{j+} gamma5 (S-odd h1, h1L, h1T terms do not flip; S-even h1^perp flips),
          eta = -1 for gamma^+ gamma5 (S-odd helicity terms do not flip).
Also: without Wilson lines (W = 1, Collins 1993) the same relation with W~ = W forces the S-odd part
of Phi^[gamma+] to vanish -- Collins' 1993 conclusion, which fails once W~ != W.
Run: python3 -I e30_pt_bd.py
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np

ok_all = []


def ok(name, cond):
    ok_all.append(bool(cond))
    print(('PASS  ' if cond else 'FAIL  ') + name)


I2 = np.eye(2); Z2 = np.zeros((2, 2))
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
g0 = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
def gi(s):
    return np.block([[Z2, s], [-s, Z2]])
g1, g2, g3 = gi(sx), gi(sy), gi(sz)
g5 = 1j * g0 @ g1 @ g2 @ g3
gam = [g0, g1, g2, g3]
eta_mn = np.diag([1, -1, -1, -1])
ok('Clifford algebra (BD representation)', all(np.allclose(gam[m] @ gam[n] + gam[n] @ gam[m], 2 * eta_mn[m, n] * np.eye(4)) for m in range(4) for n in range(4)))

M = 1j * g0 @ g1 @ g3            # Collins 1993: PT = i gamma^0 gamma^1 gamma^3
Minv = np.linalg.inv(M)
# antiunitary symmetry of the Dirac equation requires M^-1 gamma^mu* M = gamma^mu
ok('M^-1 gamma^mu* M = gamma^mu (PT is a symmetry of the Dirac equation)', all(np.allclose(Minv @ gam[m].conj() @ M, gam[m]) for m in range(4)))
ok('M is unitary', np.allclose(M.conj().T @ M, np.eye(4)))

gp = (g0 + g3) / np.sqrt(2)      # gamma^+
def sigma(a, b):
    return 0.5j * (a @ b - b @ a)
structures = {
    'gamma^+': gp,
    'gamma^+ gamma5': gp @ g5,
    'i sigma^{1+} gamma5': 1j * sigma(g1, gp) @ g5,
    'i sigma^{2+} gamma5': 1j * sigma(g2, gp) @ g5,
    'gamma^+ gamma^1 gamma5': gp @ g1 @ g5,
    'gamma^+ gamma^2 gamma5': gp @ g2 @ g5,
}
expected = {'gamma^+': +1, 'gamma^+ gamma5': -1, 'i sigma^{1+} gamma5': -1, 'i sigma^{2+} gamma5': -1,
            'gamma^+ gamma^1 gamma5': -1, 'gamma^+ gamma^2 gamma5': -1}
for name, G in structures.items():
    herm = np.allclose(g0 @ G.conj().T @ g0, G)
    Gp = g0 @ M.conj().T @ g0 @ G.conj() @ M
    Gpp = g0 @ Gp.conj().T @ g0
    # determine eta: Gpp = eta * G
    nz = np.argmax(np.abs(G))
    etaG = (Gpp.flatten()[nz] / G.flatten()[nz])
    is_mult = np.allclose(Gpp, etaG * G)
    print('   %-24s  gamma0 G^dag gamma0 = G: %s ;  G\'\' = (%+.3f%+.3fi) G' % (name, herm, etaG.real, etaG.imag))
    ok('%s: eta = %+d' % (name, expected[name]), is_mult and np.isclose(etaG, expected[name]))

print("""
Consequences (with PT: P -> P, S -> -S, k_T -> k_T, future-pointing W <-> past-pointing W):
  gamma^+ :           f1(future) = f1(past);         Sivers term (odd in S):   f_1T^perp(future) = - f_1T^perp(past)
  i sigma^{j+}g5 :    h1, h1L^perp, h1T^perp (odd in S) unchanged;  Boer-Mulders (even in S): h1^perp(future) = - h1^perp(past)
  W = 1 (Collins 1993, no Wilson line): future = past, so the S-odd part of Phi^[gamma+] vanishes -> 'no Sivers function'.""")
print('\nALL PASS' if all(ok_all) else '\nSOME CHECKS FAILED')
