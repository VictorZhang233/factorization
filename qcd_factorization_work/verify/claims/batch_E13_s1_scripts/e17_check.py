import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
Pp, M, x, z, Phm, Mh, ys, yP, yh = sp.symbols('Pplus M x z Phminus Mh y_s y_P y_h', positive=True)
# light-cone convention of Aybat-Rogers (their Sec. III): V^pm=(V0 pm Vz)/sqrt2, V^2 = 2V+V- - VT^2
# proton along +z: P- = M^2/(2P+), y_P = 1/2 ln(P+/P-); hadron h along -z: Ph+ = Mh^2/(2Ph-), y_h = 1/2 ln(Ph+/Ph-)
eyP2 = Pp/(M**2/(2*Pp))          # e^{2 y_P}
eyh2 = (Mh**2/(2*Phm))/Phm       # e^{2 y_h}
print("M^2 e^{2yP} =", sp.simplify(M**2*eyP2), " ; Mh^2 e^{-2yh} =", sp.simplify(Mh**2/eyh2))
es = sp.symbols('es', positive=True)   # es = e^{2 y_s}
zetaF_AR = 2*M**2*x**2*eyP2/es; zetaD_AR = 2*(Mh**2/z**2)*es/eyh2
zetaF_std = M**2*x**2*eyP2/es;  zetaD_std = (Mh**2/z**2)*es/eyh2
Q2 = 2*x*Pp*Phm/z                 # SIDIS leading power: q+ = -x P+, q- = Ph-/z, Q^2 = -q^2 = 2 x P+ Ph-/z
print("AR eq.(3),(4):  sqrt(zetaF zetaD)/Q^2 =", sp.simplify(sp.sqrt(zetaF_AR*zetaD_AR)/Q2))
print("standard     :  sqrt(zetaF zetaD)/Q^2 =", sp.simplify(sp.sqrt(zetaF_std*zetaD_std)/Q2))
print("standard zetaF = 2 (x P+)^2 e^{-2ys}:", sp.simplify(zetaF_std - 2*(x*Pp)**2/es) == 0)
# RG consistency: H gamma_H + gamma_F(zetaF) + gamma_D(zetaD) = 0 with AR (B1) gamma_F = (as CF/pi)(3/2 - ln(zeta/mu^2)),
# gamma_D = gamma_F at O(as) (AR App. B), and the standard one-loop hard factor gamma_H = -(as CF/pi)(3 - 2 ln(Q^2/mu^2))
mu, zF, zD, Q2s = sp.symbols('mu zF zD Q2', positive=True)
gF = lambda zeta: sp.Rational(3, 2) - sp.log(zeta/mu**2)
LH = sp.log(Q2s/mu**2)
H1 = -LH**2 + 3*LH - 8 + sp.pi**2/6        # one-loop |C_V|^2 /(as CF/2pi), spacelike; only mu-dependence matters
gH = sp.diff(H1, mu)*mu/2                 # convert from (as CF/2pi) d/dln mu to units (as CF/pi)
total = sp.simplify(sp.expand_log(gH + gF(zF) + gF(zD), force=True))
print("gamma_H + gamma_F + gamma_D (units as CF/pi) =", total)
print("  -> vanishes iff zF*zD = Q^4 :", sp.simplify(total.subs(zD, Q2s**2/zF)) == 0)
print("  with AR-printed normalization (zF zD = 4 Q^4):", sp.simplify(total.subs(zD, 4*Q2s**2/zF)))
