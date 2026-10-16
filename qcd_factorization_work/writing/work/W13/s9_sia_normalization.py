"""W13 / s9: normalization chain for e+e- -> h X (def:coll-sia, ex:coll-sia-lo, rem:coll-sia-nlo) and example numbers.
Conventions as Collins 2011 eqs. (12.3)-(12.10):
  W^{mu nu}(q,p) = (1/4pi) sum_X int d^4z e^{iqz} <0|j^mu(z)|pX,out><pX,out|j^nu(0)|0>
                 = (-g + qq/q^2) F1 + ptilde ptilde F2/(p.q),   ptilde = p - (p.q/q^2) q,
  E dsigma/d^3p = (2 alpha^2/s^3) L_{mu nu} W^{mu nu},   L = l1 l2 + l2 l1 - g l1.l2   (photon exchange, massless).
Checks:
 (a) L.W = (s/2)[(1+c^2) W_T + (1-c^2) W_L],  W_T = F1, W_L = F1 + (z/2) F2   (from s1, rescaled by 1/4);
 (b) d^3p/E = (s/4) z dz dOmega  =>  dsigma/(dz dcos) = (pi alpha^2 z/(2s)) [(1+c^2) W_T + (1-c^2) W_L]
     = 3/8 (1+c^2) dsigma_T/dz + 3/4 (1-c^2) dsigma_L/dz  with  dsigma_T/dz = (4 pi alpha^2/(3s)) z F1,
       dsigma_L/dz = (pi alpha^2/(3s)) (2 z F1 + z^2 F2)  (= Collins (12.10a,b));
 (c) W_L = 4/(z^2 s) p_mu p_nu W^{mu nu}  and  -g_{mu nu} W^{mu nu} = (D-2) W_T + W_L  (projectors, any D);
 (d) LO: F1 = (N_c/z) sum e^2 (d + dbar), F2 = -(2 N_c/z^2) sum e^2 (d+dbar)  =>  dsigma_L = 0 and
     dsigma/dz = sigma_mumu N_c sum e^2 (d + dbar) with sigma_mumu = 4 pi alpha^2/(3s)  (VF-MISC-5);
 (e) numbers at sqrt(s) = 20 GeV with alpha_s(20 GeV) = 0.1533 (VF-QCD-7, two-loop exact, n_f = 5):
     sigma_L/sigma_0 = alpha_s/pi, sigma_T/sigma_0 = 1 (O(alpha_s)), sigma_L/sigma_tot, energy sum rule 2(1+alpha_s/pi).
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

s, z, th, ph = sp.symbols('s z theta phi', positive=True)
F1, F2, alpha = sp.symbols('F1 F2 alpha')
c = sp.cos(th)
g = sp.diag(1, -1, -1, -1)
def dot(a, b): return (a.T*g*b)[0]
def vec(*x): return sp.Matrix(x)
rs = sp.sqrt(s)
l1 = vec(rs/2, 0, 0, rs/2); l2 = vec(rs/2, 0, 0, -rs/2); q = l1 + l2
p = vec(z*rs/2, z*rs/2*sp.sin(th)*sp.cos(ph), z*rs/2*sp.sin(th)*sp.sin(ph), z*rs/2*c)
pt = p - dot(p, q)/dot(q, q)*q
def W(m, n): return (-g[m, n] + q[m]*q[n]/dot(q, q))*F1 + pt[m]*pt[n]/dot(p, q)*F2   # upper indices
def L(m, n): return l1[m]*l2[n] + l2[m]*l1[n] - g[m, n]*dot(l1, l2)               # upper -> lower via g g
LW = sp.simplify(sum(L(m, n)*g[m, m]*g[n, n]*W(m, n) for m in range(4) for n in range(4)))
WT = F1; WL = F1 + z*F2/2
check('(a) L_{mu nu} W^{mu nu} = (s/2)[(1+c^2) W_T + (1-c^2) W_L]', sp.simplify(LW - s/2*((1 + c**2)*WT + sp.sin(th)**2*WL)) == 0)
# (b): E dsigma/d^3p = 2 alpha^2/s^3 L.W ; d^3p/E = |p| dE dOmega = (s/4) z dz dOmega ; dOmega -> 2 pi dcos
dsig = sp.simplify(2*sp.pi*(s/4)*z*2*alpha**2/s**3*LW)
check('(b) dsigma/(dz dcos) = (pi alpha^2 z/(2s))[(1+c^2) W_T + (1-c^2) W_L]',
      sp.simplify(dsig - sp.pi*alpha**2*z/(2*s)*((1 + c**2)*WT + sp.sin(th)**2*WL)) == 0)
dsT = 4*sp.pi*alpha**2/(3*s)*z*F1
dsL = sp.pi*alpha**2/(3*s)*(2*z*F1 + z**2*F2)
check('(b) = 3/8 (1+c^2) dsigma_T/dz + 3/4 sin^2 dsigma_L/dz with Collins (12.10a,b)',
      sp.simplify(dsig - (sp.Rational(3, 8)*(1 + c**2)*dsT + sp.Rational(3, 4)*sp.sin(th)**2*dsL)) == 0)
cc = sp.Symbol('cc')
tot = sp.integrate((sp.Rational(3, 8)*(1 + cc**2)*dsT + sp.Rational(3, 4)*(1 - cc**2)*dsL), (cc, -1, 1))
check('(b) int dcos: dsigma/dz = dsigma_T/dz + dsigma_L/dz', sp.simplify(tot - dsT - dsL) == 0)
# (c) projectors
ppW = sp.simplify(sum(p[m]*p[n]*g[m, m]*g[n, n]*W(m, n) for m in range(4) for n in range(4)))
check('(c) p_mu p_nu W^{mu nu} = (z^2 s/4) W_L', sp.simplify(ppW - z**2*s/4*WL) == 0)
Dd = sp.Symbol('D')
# -g_{mu nu}(-g^{mu nu} + q q/q^2) = D - 1 ; -g_{mu nu} pt pt/(p.q) = -pt^2/(p.q)
gW = (Dd - 1)*F1 - dot(pt, pt)/dot(p, q)*F2
check('(c) -g_{mu nu} W^{mu nu} = (D-2) W_T + W_L', sp.simplify(gW - ((Dd - 2)*WT + WL)) == 0)
# (d) LO
Nc, S = sp.symbols('N_c S', positive=True)   # S = sum_q e_q^2 [d_q + d_qbar](z)
F1lo = Nc*S/z; F2lo = -2*Nc*S/z**2
check('(d) LO: dsigma_L/dz = 0 (Callan-Gross analogue F2 = -2 F1/z)', sp.simplify(dsL.subs({F1: F1lo, F2: F2lo})) == 0)
check('(d) LO: dsigma/dz = (4 pi alpha^2/(3s)) N_c sum e^2 (d+dbar)  (VF-MISC-5)',
      sp.simplify(dsT.subs({F1: F1lo}) - 4*sp.pi*alpha**2/(3*s)*Nc*S) == 0)
check('(d) LO angular distribution prop. to 1 + cos^2', sp.simplify(dsig.subs({F1: F1lo, F2: F2lo})/(1 + c**2)).has(th) is False)
# (e) numbers
a_s = sp.Rational(1533, 10000)
r = a_s/sp.pi
print('   alpha_s(20 GeV) = 0.1533 (VF-QCD-7):  alpha_s/pi = %.5f' % float(r))
print('   sigma_L/sigma_0 = %.5f, sigma_T/sigma_0 = 1 + O(alpha_s^2), sigma_tot/sigma_0 = %.5f, sigma_L/sigma_tot = %.5f'
      % (float(r), float(1 + r), float(r/(1 + r))))
print('   energy sum rule: sum_h int z dsigma^h/dz / sigma_0 = 2(1 + alpha_s/pi) = %.5f' % float(2*(1 + r)))
R0 = 3*(sp.Rational(4, 9)*2 + sp.Rational(1, 9)*3)
print('   R_0 (n_f = 5) =', R0, '; sigma_mumu = 86.8 nb/(s/GeV^2) -> at sqrt(s) = 20 GeV sigma_mumu = %.4f nb' % (86.8/400))
check('(e) R_0 = 11/3 for n_f = 5', R0 == sp.Rational(11, 3))
print('\nSUMMARY s9: %d PASS, %d FAIL' % (npass, nfail))
