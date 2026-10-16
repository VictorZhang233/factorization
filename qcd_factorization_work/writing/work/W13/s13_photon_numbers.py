"""W13 / s13: point-like photon structure (prop:coll-photon-sf): eigenvalue structure and an example (n_f = 5).
LO anomalous dimensions (prop:pdf-lo-kernels (c), our normalization): gamma_qq, gamma_qg, gamma_gq, gamma_gg.
Moments of the photon's parton densities obey (t = ln mu^2, a_s = alpha_s/2pi, a = alpha/2pi):
  d(q_f+qbar_f)_n/dt = a_s[gamma_qq (q_f+qbar_f)_n + 2 gamma_qg g_n] + a * 2 N_c e_f^2 khat_n,
  dg_n/dt = a_s[gamma_gq sum_f (q_f+qbar_f)_n + gamma_gg g_n],     khat_n = (n^2+n+2)/(n(n+1)(n+2)).
Point-like solution A^pl = (2 alpha/alpha_s)(beta0 - 2 Gamma)^{-1} K  (s7 (b)).
Checks: (a) eigenvalues of the (singlet) matrix are <= 0 for even n >= 2, with a zero eigenvalue only at n = 2;
        hence beta0 - 2 Gamma is invertible for all even n >= 2;
        (b) the matrix point-like solution solves the inhomogeneous RG equation at LO (direct substitution);
        (c) example: (u+ubar-d-dbar)_2^pl = (alpha/alpha_s) 12/101 for n_f = 5; at Q = 20 GeV with
            alpha_s = 0.1533 (VF-QCD-7) and alpha = 1/137.036 it equals 0.00566.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

npass = 0; nfail = 0
def check(name, ok):
    global npass, nfail
    print(('PASS ' if ok else 'FAIL ') + name, flush=True)
    if ok: npass += 1
    else: nfail += 1

CF, CA, TF = sp.Rational(4, 3), 3, sp.Rational(1, 2)
def S1(n): return sum(sp.Rational(1, k) for k in range(1, n + 1))
def gams(n):
    gqq = CF*(sp.Rational(3, 2) + sp.Rational(1, n*(n + 1)) - 2*S1(n))
    gqg = TF*sp.Rational(n**2 + n + 2, n*(n + 1)*(n + 2))
    ggq = CF*sp.Rational(n**2 + n + 2, (n - 1)*n*(n + 1))
    return gqq, gqg, ggq
def beta0(nf): return 11 - sp.Rational(2, 3)*nf
for nf in (3, 4, 5):
    ok = True; inv = True
    for n in range(2, 13, 2):
        gqq, gqg, ggq = gams(n)
        ggg = 2*CA*(sp.Rational(1, n*(n - 1)) + sp.Rational(1, (n + 1)*(n + 2)) - S1(n)) + beta0(nf)/2
        M = sp.Matrix([[gqq, 2*nf*gqg], [ggq, ggg]])
        ev = [sp.nsimplify(e) for e in M.eigenvals().keys()]
        evn = [float(e) for e in ev]
        if n == 2:
            ok &= any(abs(e) < 1e-12 for e in evn) and all(e <= 1e-12 for e in evn)
        else:
            ok &= all(e < 0 for e in evn)
        ok &= gqq < 0
        inv &= (beta0(nf)*sp.eye(2) - 2*M).det() != 0
    check('(a) n_f=%d: singlet eigenvalues <= 0 (zero only at n=2), gamma_qq(n) < 0, beta0 - 2 Gamma invertible (n=2..12)' % nf, ok and inv)
# (b) matrix point-like solution solves the inhomogeneous equation (symbolic in alpha_s)
als, al = sp.symbols('alpha_s alpha', positive=True)
n, nf = 4, 5
gqq, gqg, ggq = gams(n)
ggg = 2*CA*(sp.Rational(1, n*(n - 1)) + sp.Rational(1, (n + 1)*(n + 2)) - S1(n)) + beta0(nf)/2
G = sp.Matrix([[gqq, 2*nf*gqg], [ggq, ggg]])
K = sp.Matrix([2*3*sp.Rational(11, 9)*sp.Rational(n**2 + n + 2, n*(n + 1)*(n + 2)), 0])   # sum_f e_f^2 = 11/9
A = 2*al/als*(beta0(nf)*sp.eye(2) - 2*G).inv()*K
# dA/dt = dA/dalpha_s * dalpha_s/dt,  dalpha_s/dt = -beta0 alpha_s^2/(4 pi)
lhs = sp.diff(A, als)*(-beta0(nf)*als**2/(4*sp.pi))
rhs = als/(2*sp.pi)*G*A + al/(2*sp.pi)*K
check('(b) A^pl = (2 alpha/alpha_s)(beta0 - 2 Gamma)^{-1} K solves dA/dt = (alpha_s/2pi) Gamma A + (alpha/2pi) K (n=4, n_f=5)',
      sp.simplify(lhs - rhs) == sp.zeros(2, 1))
# (c) example
gqq2 = gams(2)[0]
val = 2*(2*3*(sp.Rational(4, 9) - sp.Rational(1, 9))*sp.Rational(1, 3))/(beta0(5) - 2*gqq2)
print('   (u+ubar-d-dbar)_2^pl / (alpha/alpha_s) =', sp.nsimplify(val))
check('(c) (u+ubar-d-dbar)_2^pl = (alpha/alpha_s) 12/101 (n_f = 5)', val == sp.Rational(12, 101))
num = float(val)*(1/137.036)/0.1533
print('   at Q = 20 GeV: alpha/alpha_s = %.5f, (u+ubar-d-dbar)_2 = %.5f' % ((1/137.036)/0.1533, num))
check('(c) numerical value 0.00566 at Q = 20 GeV', abs(num - 0.00566) < 2e-5)
print('\nSUMMARY s13: %d PASS, %d FAIL' % (npass, nfail))
