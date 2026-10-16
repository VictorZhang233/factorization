"""
ope_wilson.py -- one-loop OPE Wilson coefficients from the forward Compton amplitude, renormalised in MS-bar,
compared with the Mellin moments of the x-space coefficient functions (closed forms in moments.py).

The forward amplitude of an on-shell massless parton is expanded in the hard region (ope_check.py): for
p^2 = 0 all other regions are scaleless, so the Taylor coefficient of omega^N (omega = 2p.q/Q^2 = 1/x) equals
   C_N^bare(eps) * <O_N>^bare_parton ,   <O_N>^bare_parton = tree (all loop corrections scaleless).
MS-bar operator renormalisation removes the remaining 1/eps pole (no 1/eps^2 survives: checked), so the
renormalised Wilson coefficient at mu = Q is the eps^0 term of the bare one, and the residue of the pole is
minus the LO anomalous dimension (= Mellin moment of P_ij).  K = e^{eps gE} Gamma(1+eps)Gamma(1-eps)^2/Gamma(1-2eps)
restores the MS-bar normalisation of the loop integrals (ope_check strips K_G = e^{-eps gE} K).
Usage:  python3 -I ope_wilson.py [NMAX]
"""
import sys, os, time
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import ope_check as oc
import moments as mo

eps, om = oc.eps, oc.om
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
K = sp.exp(eps * sp.EulerGamma) * sp.gamma(1 + eps) * sp.gamma(1 - eps) ** 2 / sp.gamma(1 - 2 * eps)
Kser = sp.series(K, eps, 0, 4).removeO()
CF, TF = mo.CF, mo.TF


def laurent(expr, nmin=-2, nmax=0):
    ser = sp.expand(sp.series(sp.expand(Kser) * expr, eps, 0, nmax + 1).removeO())
    return {n: sp.nsimplify(sp.simplify(ser.coeff(eps, n))) for n in range(nmin, nmax + 1)}


t0 = time.time()
qa = oc.quark_amplitudes(NMAX)
tree2 = sp.expand((qa['g']['tree'] + (3 - 2 * eps) * 4 * qa['pp']['tree'] / om ** 2) / (1 - eps))
loop2 = sp.expand(sum((qa['g'][k] + (3 - 2 * eps) * 4 * qa['pp'][k] / om ** 2) / (1 - eps)
                      for k in ('box', 'v1', 'v2', 'se')))
loopL = sp.expand(8 * sum(qa['pp'][k] for k in ('box', 'v1', 'v2', 'se')) / om ** 2)
ct, c2, cL = oc.coeffs(tree2, NMAX), oc.coeffs(loop2, NMAX), oc.coeffs(loopL, NMAX)
ga = oc.gluon_amplitude(NMAX)
Dv = 4 - 2 * eps
g2 = oc.coeffs(sp.expand((ga['g'] + (3 - 2 * eps) * 4 * ga['pp'] / om ** 2) / (1 - eps)), NMAX)
gL = oc.coeffs(sp.expand(8 * ga['pp'] / om ** 2), NMAX)
print(f'forward amplitudes up to omega^{NMAX} computed ({time.time() - t0:.1f}s)')

allok = True
print('quark:  W_N = K * (one-loop/tree)/2  in units (as/2pi) C_F ;  expect  W_N = -P_qq(N)/(C_F eps) + C_2^q(N)/C_F')
for N in range(1, NMAX + 1):
    w2 = laurent(c2[N] / ct[N] / 2)
    wL = laurent(cL[N] / ct[N] / 2)
    ok = (w2[-2] == 0 and sp.simplify(w2[-1] + mo.Pqq_N(N) / CF) == 0 and sp.simplify(w2[0] - mo.C2q_N(N) / CF) == 0
          and wL[-2] == 0 and wL[-1] == 0 and sp.simplify(wL[0] - mo.CLq_N(N) / CF) == 0)
    allok &= ok
    print(f'  N={N}:  C_2^q(N)/C_F = {w2[0]},  pole residue = {w2[-1]},  C_L^q(N)/C_F = {wL[0]}   {"PASS" if ok else "FAIL"}')
print('gluon (even N; per flavour):  W_N = K * (2/(D-2)) * (box)/(2*2*tree) / 2  in units (as/2pi) T_F ;')
print('       expect  W_N = -P_qg(N)/(T_F eps) + C_2^g(N)/T_F   [F_2^g = e_q^2 (as/2pi) 2 C_2^g]')
for N in range(2, NMAX + 1, 2):
    w2 = laurent((2 / (Dv - 2)) * g2[N] / (2 * ct[N]) / 4)
    wL = laurent((2 / (Dv - 2)) * gL[N] / (2 * ct[N]) / 4)
    ok = (w2[-2] == 0 and sp.simplify(w2[-1] + mo.Pqg_N(N) / TF) == 0 and sp.simplify(w2[0] - mo.C2g_N(N) / TF) == 0
          and wL[-1] == 0 and sp.simplify(wL[0] - mo.CLg_N(N) / TF) == 0)
    allok &= ok
    print(f'  N={N}:  C_2^g(N)/T_F = {w2[0]},  pole residue = {w2[-1]},  C_L^g(N)/T_F = {wL[0]}   {"PASS" if ok else "FAIL"}')
print('OPE WILSON COEFFICIENTS:', 'ALL PASS' if allok else 'FAILURES', f'({time.time() - t0:.1f}s)')
