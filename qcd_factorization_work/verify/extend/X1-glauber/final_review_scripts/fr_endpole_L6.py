# Final review of X1 -- T2'(b) end-pole prediction recomputed from the model parameters of
# scripts/twoexch_rotated_fast.py, and an independent check of L6 (ray identity) on the scalar-model rho_12.
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
from scipy import integrate
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, '..', 'scripts'))
import twoexch_rotated_fast as m
lam = 1.0
sc = lambda v: (lam*v[0], lam*v[1])
k1T = sc((0.8, 0.1)); k2T = sc((-0.3, 0.9)); k1Tm = (-k1T[0], -k1T[1]); k2Tm = (-k2T[0], -k2T[1])
a1 = k1T[0]**2 + k1T[1]**2; a2 = k2T[0]**2 + k2T[1]**2
for name in ('base', 'apole', 'alt'):
    (MA, maA, msA, xA, sTA), (MB, maB, msB, xB, sTB) = m.sets[name]
    pa = m.jet_params(MA*lam, maA*lam, msA*lam, xA, sc(sTA), k1T, k2T)
    pb = m.jet_params(MB*lam, maB*lam, msB*lam, xB, sc(sTB), k1Tm, k2Tm)
    pred = 0.0
    if pa['al1'] > 0: pred += 0.5*a1*pa['al1']/(a1*pa['al1'] + a2*abs(pa['d10']))
    if pa['al2'] > 0: pred += 0.5*a2*pa['al2']/(a2*pa['al2'] + a1*abs(pa['d20']))
    # mirror (pole in J_B, rotation of k^-): same formula with B's energies
    predB = 0.0
    if pb['al1'] > 0: predB += 0.5*a1*pb['al1']/(a1*pb['al1'] + a2*abs(pb['d10']))
    if pb['al2'] > 0: predB += 0.5*a2*pb['al2']/(a2*pb['al2'] + a1*abs(pb['d20']))
    print(f"{name:6s}: A al0,al1,al2 = {pa['al0']:+.4f},{pa['al1']:+.4f},{pa['al2']:+.4f};  B al0,al1,al2 = {pb['al0']:+.4f},{pb['al1']:+.4f},{pb['al2']:+.4f};"
          f"  end-pole Re p_opp: A-poles {pred:.4f}, B-poles (mirror) {predB:.4f}")
# L6 on rho_12(k) = a1 a2/((a1 - 2 d10 k)(a2 - 2 al1 k)) : int_0^inf Im rho(i kappa) dkappa/kappa
for name in ('base', 'apole'):
    (MA, maA, msA, xA, sTA), _ = m.sets[name]
    pa = m.jet_params(MA, maA, msA, xA, sTA, k1T, k2T)
    d10, al1 = pa['d10'], pa['al1']
    rho = lambda k: a1*a2/((a1 - 2*d10*k)*(a2 - 2*al1*k))
    val = integrate.quad(lambda t: (rho(1j*np.exp(t))).imag, -40, 40, limit=800)[0]
    pole = 0.0
    if al1 > 0:
        kp = a2/(2*al1); res = a1*a2/((a1 - 2*d10*kp)*(-2*al1))
        pole = -np.pi*res/kp
    print(f"L6 {name:6s}: int Im rho(i kappa) dkappa/kappa = {val:+.10f};  prediction -pi/2 {'- pi Res/k_p' if al1>0 else ''} = {-np.pi/2 + pole:+.10f}")
