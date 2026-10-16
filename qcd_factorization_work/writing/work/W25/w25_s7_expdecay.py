#!/usr/bin/env python3
"""W25 / Ch22 -- s7: ingredients of the proof of thm:lamet-exp-decay (Ji-Liu-Su locality => exponential decay),
written out in the book via a Phragmen-Lindelof argument on the cut plane Omega = C minus {t real, |t| >= R}.

E1  S(w) = sqrt(R^2 - w^2) (principal branch) is holomorphic on Omega: R^2 - w^2 is real <= 0 only for w real, |w| >= R;
    Re S > 0 on Omega, S(0) = R.
E2  Re S(w) >= |Im w| on Omega, and Re S(w) - |Im w| <= R; Re S - |Im w| = O(R^2/|w|) at infinity.
E3  on the cuts (w = t +- i0, |t| > R): Re S = 0 and |R + S| = |t|; |S^2| = |t^2 - R^2|.
E4  zeta = arcsin(w/R) maps Omega conformally onto the strip |Re zeta| < pi/2, cuts -> edges; |w| ~ (R/2) e^{|Im zeta|}.
E5  sharpness: G(w) = exp(-dm S(w)) is holomorphic on Omega, |G| <= exp(-dm |Im w|) in both half planes, |G| = 1 on the cuts,
    G(0) = exp(-dm R): the bound |G(0)| <= C e^{-dm R} cannot be improved under these hypotheses.
E6  the spectral bound: for a measure supported in E - m >= dm, |int dmu(E) e^{-i(E-m)w}| <= |mu| e^{-dm |Im w|} for Im w < 0
    (and the mirror statement for G_<); vacuum + crossed vacuum channels give 2Z cos(m w) in both orderings.
E7  Phragmen-Lindelof check on a numerical example: Phi = G e^{dm S} S^{2k} / (R+S)^{N'} bounded by its boundary sup on a grid.
E8  free-field-like illustration: Lorentz-invariant two-point function of mass M with external rest frame, sqrt(R^2 - w^2) = sqrt(-x^2)
    (x = (w, z)), so e^{-M sqrt(-x^2)} type decay at w = 0 is e^{-M R}.
"""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
import cmath, math

NP = 0; NF = 0
def check(name, ok, extra=""):
    global NP, NF
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" : " + str(extra)) if extra != "" else ""))
    if ok: NP += 1
    else: NF += 1

R = 1.7
def S(w): return cmath.sqrt(R * R - w * w)          # principal branch: Re >= 0, cut where R^2 - w^2 <= 0

rng = np.random.default_rng(12345)
pts = [complex(x, y) for x, y in zip(rng.uniform(-8, 8, 4000), rng.uniform(-6, 6, 4000))]
pts = [w for w in pts if abs(w.imag) > 1e-6 or abs(w.real) < R - 1e-6]
# E1 holomorphy: Cauchy-Riemann by finite differences, and Re S > 0
h = 1e-6
okcr = True; okre = True
for w in pts[:1500]:
    if abs(w.imag) < 1e-3 and abs(w.real) > R - 1e-3: continue
    d1 = (S(w + h) - S(w - h)) / (2 * h); d2 = (S(w + 1j * h) - S(w - 1j * h)) / (2j * h)
    okcr &= abs(d1 - d2) < 1e-5 * (1 + abs(d1))
    okre &= S(w).real > 0
check("E1 S(w) = sqrt(R^2-w^2) holomorphic on Omega (Cauchy-Riemann on 1500 random points)", okcr)
check("E1 Re S > 0 on Omega; S(0) = R", okre and abs(S(0) - R) < 1e-15)
# continuity across the segment (-R,R): S(t+i0) = S(t-i0) = sqrt(R^2-t^2) > 0
check("E1 no cut on (-R,R): S(t+i0) = S(t-i0) = sqrt(R^2-t^2)",
      all(abs(S(complex(t, 1e-12)) - S(complex(t, -1e-12))) < 1e-9 for t in np.linspace(-R + 1e-3, R - 1e-3, 50)))
# E2
d = [S(w).real - abs(w.imag) for w in pts]
check("E2 Re S(w) >= |Im w| on Omega (4000 random points)", min(d) >= -1e-12, "min %.2e" % min(d))
check("E2 Re S(w) - |Im w| <= R on Omega", max(d) <= R + 1e-12, "max %.6f (R = %.2f)" % (max(d), R))
far = [complex(r * math.cos(t), r * math.sin(t)) for r in (50.0, 200.0, 1000.0) for t in np.linspace(0.05, 3.09, 30)]
check("E2 Re S - |Im w| = O(R^2/|w|) at infinity",
      all((S(w).real - abs(w.imag)) * abs(w) <= R * R + 1e-6 for w in far))
# E3 boundary values on the cuts
okc = True
for t in [R + 0.01, 2.5, 7.0, -2.0, -9.0]:
    for s in (+1, -1):
        v = S(complex(t, s * 1e-13))
        okc &= abs(v.real) < 1e-6 and abs(abs(R + v) - abs(t)) < 1e-9 and abs(abs(v)**2 - (t * t - R * R)) < 1e-9
check("E3 on the cuts: Re S = 0, |R + S| = |t|, |S|^2 = t^2 - R^2", okc)
# E4 arcsin map
okm = True
for w in pts[:800]:
    zt = cmath.asin(w / R)
    okm &= abs(zt.real) < math.pi / 2 + 1e-12 and abs(R * cmath.sin(zt) - w) < 1e-9
check("E4 zeta = arcsin(w/R): Omega -> strip |Re zeta| < pi/2 (and w = R sin zeta)", okm)
okb = all(abs(abs(cmath.asin(complex(t, 1e-14) / R).real) - math.pi / 2) < 1e-6 for t in (R + 0.5, 3.0, -4.0, -R - 0.2))
check("E4 cuts are mapped onto the edges Re zeta = +- pi/2", okb)
check("E4 |w| ~ (R/2) e^{|Im zeta|} for large |Im zeta|",
      all(abs(abs(R * cmath.sin(complex(0.3, y))) / (R / 2 * math.exp(abs(y))) - 1) < 1e-3 for y in (8.0, 12.0, -10.0)))
# E5 sharpness example
dm = 0.8
G = lambda w: cmath.exp(-dm * S(w))
okg = all(abs(G(w)) <= math.exp(-dm * abs(w.imag)) * (1 + 1e-12) for w in pts)
check("E5 G = exp(-dm S): |G| <= exp(-dm |Im w|) on Omega", okg)
check("E5 |G| = 1 on the cuts, G(0) = exp(-dm R)",
      all(abs(abs(G(complex(t, 1e-13))) - 1) < 1e-9 for t in (R + 0.3, 5.0, -3.0)) and abs(G(0) - math.exp(-dm * R)) < 1e-15)
# E6 spectral representation bound and the vacuum/crossed channels
Es = np.linspace(1.0 + 0.6, 30, 300)                       # m = 1, dm = 0.6
wts = np.exp(-0.1 * Es) * (1 + np.sin(Es))**2              # positive spectral weights
def Gt(w): return np.sum(wts * np.exp(-1j * (Es - 1.0) * w))
ok6 = all(abs(Gt(complex(t, -s))) <= np.sum(wts) * math.exp(-0.6 * s) * (1 + 1e-12) for t in (-3, 0, 2.2) for s in (0.1, 1.0, 4.0))
check("E6 |sum_n w_n e^{-i(E_n-m)w}| <= (sum w_n) e^{-dm |Im w|} for Im w < 0 (E_n - m >= dm)", ok6)
m_ = 1.3; Zc = 0.7
vac_gt = lambda t: Zc * cmath.exp(1j * m_ * t) + Zc * cmath.exp(-1j * m_ * t)   # vacuum + crossed vacuum in phi(t,z)phi(0)
vac_lt = lambda t: Zc * cmath.exp(-1j * m_ * t) + Zc * cmath.exp(1j * m_ * t)   # in phi(0)phi(t,z)
check("E6 vacuum + crossed vacuum channels give 2Z cos(m t) in both orderings (entire, no cut)",
      all(abs(vac_gt(t) - 2 * Zc * cmath.cos(m_ * t)) < 1e-14 and abs(vac_lt(t) - 2 * Zc * cmath.cos(m_ * t)) < 1e-14 for t in (0.3, -2.0, 5.5)))
# E7 PL on an example: G_ex = exp(-dm S) * (1 + w^2/9) / (w^2 - R^2)^k ... choose k = 1, polynomial degree N = 2
k_, Nexp = 1, 2
def Gex(w): return cmath.exp(-dm * S(w)) * (1 + w * w / 9.0) / (R * R - w * w)**k_ * (R * R - w * w)   # regular version
def Phi(w): return Gex(w) * cmath.exp(dm * S(w)) * S(w)**(2 * k_) / (R + S(w))**(Nexp + 2 * k_)
bsup = max(abs(Phi(complex(t, s * 1e-12))) for t in list(np.linspace(R + 1e-6, 60, 3000)) + list(np.linspace(-60, -R - 1e-6, 3000)) for s in (1, -1))
inner = [abs(Phi(w)) for w in pts]
check("E7 Phragmen-Lindelof example: sup over Omega of |Phi| <= sup over the cuts (%.4f <= %.4f)" % (max(inner), bsup), max(inner) <= bsup * (1 + 1e-9))
# the conclusion at w = 0
G0_bound = bsup * (2 * R)**(Nexp + 2 * k_) / R**(2 * k_) * math.exp(-dm * R)
check("E7 |G(0)| <= sup_cuts|Phi| (2R)^{N'} R^{-2k} e^{-dm R}", abs(Gex(0)) <= G0_bound, "%.4e <= %.4e" % (abs(Gex(0)), G0_bound))
# E8 Lorentz-invariant illustration: sqrt(R^2 - w^2) is sqrt(-x^2) for x = (w, z), |z| = R
check("E8 for x = (w, z), |z| = R: -x^2 = R^2 - w^2, so S(w) = sqrt(-x^2) (Euclidean distance at w = -i t_E)",
      all(abs(S(complex(0, -tE)) - math.sqrt(R * R + tE * tE)) < 1e-12 for tE in (0.0, 0.5, 3.0)))

print("\nSUMMARY w25_s7_expdecay: %d PASS, %d FAIL" % (NP, NF))
