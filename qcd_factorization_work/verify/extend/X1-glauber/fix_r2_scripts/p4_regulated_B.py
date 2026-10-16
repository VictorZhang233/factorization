# X1 fix round 2 -- P4 in the G7-regulated setting: per-graph W(21,12) depends on the in-window SHAPE of J_B,
# not only on the window data D_win(J_B) = {Jcal_sigma, lambda_B}.
# Jet A localized (race weights; L1' weights with an even Lorentzian k^- regulator when K^- is given);
# jet B = scalar-model base set (fix_r1 regulator_indep.py) plus a perturbation with two-state gaps (so (Sp), (Sp'),
# (R) and Jcal_sigma, lambda_B are unchanged), either in the both-initial sector BB or in the MIXED sector BF:
#   BB: delta J^[12] = s*(-Jcal)*r*[i/(A1+p1)][i/(A2+p1)][i/(A3+P)][i/(A4+P)]     ([21]: p1 -> p2)
#   BF: delta J^[12] = s*(-Jcal)*r*[i/(A1+p1)][i/(A2+p1)][i/(A3-p2)][i/(A4-p2)]   ([21]: p1 <-> p2)
# Structural fact (sector selection, see P4 remark): with jet A localized, a term whose gaps are all initial (or all
# final) has all its k^+ poles in one half plane, so it enters the per-graph weights only through its total integral
# (here 0); only mixed-sector shapes can change W(pi_A, pi_B).
#   |A_i| <= lambda_B,  r real ~ lambda_B^2.
# Prediction (T2 Step 3 per graph, theta = pi/2): delta W(21,12) = (1/Jcal_B) int v delta f_12 + small (purely imaginary),
# delta W(12,21) = -(1/Jcal_B) int v delta f_21 + small.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fix_r1_scripts'))
import numpy as np
import regulator_indep as ri

k1T, k2T = (0.8, 0.1), (-0.3, 0.9)
pb = ri.jet_params(0.8, 0.6, 0.5, 0.55, (-0.25, 0.4), (-0.8, -0.1), (0.3, -0.9))   # base set, jet B
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2; a = np.sqrt(a1*a2)
lamB_all = max(abs(pb['d0']), abs(pb['beta']), abs(pb['al0']), abs(pb['al1']), abs(pb['al2']))
Jcal = 1j/pb['d0']
As = [-0.6*lamB_all, -0.9*lamB_all, -0.4*lamB_all, -0.75*lamB_all]
r = 0.5*lamB_all**2

SECTOR = 'BB'
def dJ(p1, p2, col, s):
    P = p1 + p2
    q = p1 if col == '12' else p2
    o = p2 if col == '12' else p1
    if SECTOR == 'BB':
        return s*(-Jcal)*r*(1j/(As[0] + q))*(1j/(As[1] + q))*(1j/(As[2] + P))*(1j/(As[3] + P))
    return s*(-Jcal)*r*(1j/(As[0] + q))*(1j/(As[1] + q))*(1j/(As[2] - o))*(1j/(As[3] - o))

def JB(p1, p2, col, s):
    return ri.JB_full(p1, p2, pb, col) + dJ(p1, p2, col, s)

def weights(Kp, Km, s, th):
    I = {}
    for cA in ('12', '21'):
        for cB in ('12', '21'):
            def fun(u1, u2, q, cA=cA, cB=cB):
                w = ri.W12(u1, u2, a1, a2, Km, q)
                if cA == '21': w = 1 - w
                return w*ri.lorentz(u1, Kp)*ri.lorentz(u2, Kp)*JB(-u1, -u2, cB, s)
            I[(cA, cB)] = ri.integrate(fun, th)
    N = sum(I.values())
    return {k: v/N for k, v in I.items()}, N/Jcal

print('NOTE: jet A is localized at all k^+ (race weights), i.e. it has no A-collinear end; without regulators the')
print('      base values W(pi_A,pi_B) of this run are therefore set by the finite quadrature range (Re p_opp = 1/4 is the')
print('      truncation artefact of the rotated contour) and carry no meaning.  Only the SHIFTS delta W are meaningful:')
print('      delta f decays like |kappa|^-4 and is concentrated at |kappa| ~ lambda_B.  With G7 regulators the base values')
print('      are physical (Re p_opp = 0.0137, cf. T2(c)).')
for SECTOR in ('BB', 'BF'):
  print('==== perturbation in sector', SECTOR)
  # check that the perturbation integrates to zero   (window data unchanged at the level of int J_B)
  for col in ('12', '21'):
      z = ri.integrate(lambda u1, u2, q: dJ(-u1, -u2, col, 1.0), np.pi/4)/Jcal
      print(f"int delta J^[{col}] / Jcal = {z:.2e}   (lambda_B = {lamB_all:.4f}, r = {r:.4f}, A_i = {[round(x,4) for x in As]})")

  # prediction (localized A, unregulated): W(pi_A,pi_B) N/N_0 = (1/Jcal) I[h_piA f_piB], where I[.] = integrate() includes
  # the rotation factor e^{2 i theta}, i.e. equals the real-contour integral; h_21 = 1/2 - v, h_12 = 1/2 + v, int delta f = 0
  def vfun(u1, u2, q):
      return ri.W12(u1, u2, a1, a2, None, q) - 0.5
  pred21 = ri.integrate(lambda u1, u2, q: -vfun(u1, u2, q)*dJ(-u1, -u2, '12', 1.0), np.pi/2)/Jcal
  pred12 = ri.integrate(lambda u1, u2, q: vfun(u1, u2, q)*dJ(-u1, -u2, '21', 1.0), np.pi/2)/Jcal
  print(f"prediction (unregulated, localized A): delta W(21,12) = {pred21:.6f},  delta W(12,21) = {pred12:.6f}")

  for (lab, Kp, Km) in (("no regulators", None, None), ("G7: K+ = 1e2 lambda_B, K+K-/a = 1e3", 1e2*abs(pb['d0']), 1e3*a/(1e2*abs(pb['d0'])))):
      for th in (np.pi/4,):
          W0, N0 = weights(Kp, Km, 0.0, th); W1, N1 = weights(Kp, Km, 1.0, th)
          d21 = W1[('21', '12')] - W0[('21', '12')]; d12 = W1[('12', '21')] - W0[('12', '21')]
          dpo = d21 + d12
          print(f"{lab}: W(21,12): {W0[('21','12')]:.6f} -> {W1[('21','12')]:.6f}  (delta = {d21:.6f});  "
                f"W(12,21): {W0[('12','21')]:.6f} -> {W1[('12','21')]:.6f} (delta = {d12:.6f});  delta p_opp = {dpo:.2e};  N/Jcal {N0:.5f} -> {N1:.5f}")
