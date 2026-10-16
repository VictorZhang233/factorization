# W26 / Ch23 -- s09: one-loop quasi-GPD matching kernel near x = +-xi (prop:yzliu-gpd-oneloop; MD14 re-derivation)
# Explicit one-loop kernel: Liu, Wang, Xu, Zhang, Zhang, Zhao, Zhao, PRD 100 (2019) 034006 [arXiv:1902.00307v2],
# eqs. (39)-(43),(46) for Gamma = gamma^t (rendered page 7 checked).  Variables (rescaled, light-cone parton at y=1,
# 0<xi<1): x = quasi momentum fraction, p^z = parton momentum; f1 = (alpha_s C_F/2pi) G_i in four regions:
#   G1 (x<-xi), G2 (|x|<xi), G3 (xi<x<1), -G1 (x>1).
# Logarithms are written with  lp = ln|x+xi|, lm = ln|x-xi|, l1 = ln|1-x|, lmu = ln(4 p_z^2/mu^2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp

x, xi = sp.symbols('x xi', real=True)
lp, lm, l1, lmu = sp.symbols('lp lm l1 lmu', real=True)
# G1: -[1/(x-1) - x/(2xi) + (1+x)/(2(1+xi))] ln((x-1)/(x+xi)) + (xi -> -xi)
bp = 1/(x - 1) - x/(2*xi) + (1 + x)/(2*(1 + xi))
bm = 1/(x - 1) + x/(2*xi) + (1 + x)/(2*(1 - xi))
G1 = -bp*(l1 - lp) - bm*(l1 - lm)                    # x<-xi: ln((x-1)/(x+-xi)) = l1 - l(+-)
Gout = -G1                                           # x>1 : -G1, ln((x-1)/(x+-xi)) = l1 - l(+-) again
E = (x + xi)*(1 - x + 2*xi)/(2*(1 - x)*xi*(1 + xi))
G2 = E*(lmu + 2*l1 + lp - lm - 1) + (x + xi**2)/(xi*(1 - xi**2))*(lm - l1)
A = (1 + x**2 - 2*xi**2)/((1 - x)*(1 - xi**2))
G3 = A*(lmu + sp.Rational(1, 2)*(lp + lm) + l1 - 1) + (x + xi**2)/(2*xi*(1 - xi**2))*(lp - lm)
regions = [('x<-xi', G1), ('|x|<xi', G2), ('xi<x<1', G3), ('x>1', Gout)]

cp_closed = lambda sgn: sgn*(x + xi)/(1 + xi)*(1/(2*(1 - x)) + 1/(4*xi))   # coefficient of ln[4p^2(x+xi)^2/mu^2]
cm_closed = lambda sgn: sgn*(x - xi)/(1 - xi)*(1/(2*(1 - x)) - 1/(4*xi))   # coefficient of ln[4p^2(x-xi)^2/mu^2]
signs = {'x<-xi': (-1, -1), '|x|<xi': (+1, -1), 'xi<x<1': (+1, +1), 'x>1': (+1, +1)}   # signs of (x+xi), (x-xi)
allok = True
for name, G in regions:
    Ge = sp.expand(G)
    clp, clm, cl1, cmu = [sp.simplify(Ge.coeff(v)) for v in (lp, lm, l1, lmu)]
    # decomposition G = cP [lmu + 2 lp] + cM [lmu + 2 lm] + c1 [lmu + 2 l1] + rational, requires cmu = cP + cM + c1
    cP, cM, c1 = clp/2, clm/2, cl1/2
    consistent = sp.simplify(cmu - (cP + cM + c1)) == 0
    sp_, sm_ = signs[name]
    okP = sp.simplify(cP - cp_closed(sp_)) == 0
    okM = sp.simplify(cM - cm_closed(sm_)) == 0
    allok &= consistent and okP and okM
    print('%-7s: coeff of ln[4p^2(x+xi)^2/mu^2] = %s' % (name, sp.factor(cP)))
    print('         coeff of ln[4p^2(x-xi)^2/mu^2] = %s' % sp.factor(cM))
    print('         coeff of ln[4p^2(1-x)^2/mu^2]  = %s' % sp.factor(c1))
    print('         mu-log coefficient = sum of the three: %s ; closed forms |x+-xi|/(1+-xi)(1/(2(1-x)) +- 1/(4xi)): %s %s'
          % (consistent, okP, okM))
print('all regions: decomposition consistent and closed forms reproduced:', allok)
# vanishing at x = -+xi and the kink
print('cP at x=-xi:', sp.simplify(cp_closed(1).subs(x, -xi)), ' ; cM at x=+xi:', sp.simplify(cm_closed(1).subs(x, xi)))

# forward limit xi -> 0 vs VF-LAM-7 / VF-LAM-8
lim1 = sp.limit(G1.subs({l1: sp.log(1 - x), lp: sp.log(-x - xi), lm: sp.log(-x + xi)}).subs(x, sp.Rational(-1, 3)), xi, 0)
ref1 = (-(1 + x**2)/(1 - x)*sp.log(-x/(1 - x)) - 1).subs(x, sp.Rational(-1, 3))
print('forward limit x=-1/3: G1 ->', sp.N(lim1, 12), ' VF-LAM-7 ->', sp.N(ref1, 12))
xv = sp.Rational(2, 5); P = sp.Symbol('P', positive=True)
lim3 = sp.limit(G3.subs({l1: sp.log(1 - xv), lp: sp.log(xv + xi), lm: sp.log(xv - xi), lmu: sp.log(P)}).subs(x, xv), xi, 0)
ref3 = ((1 + xv**2)/(1 - xv)*(sp.log(P) + sp.log(xv*(1 - xv))) - xv*(1 + xv)/(1 - xv))
print('forward limit x=2/5: G3 - VF-LAM-8 bracket =', sp.simplify(lim3 - ref3))
assert sp.simplify(lim3 - ref3) == 0 and abs(sp.N(lim1 - ref1)) < 1e-12

# mu dependence vs GPD evolution kernel derived from the light-ray kernel (independent):
# B O(z1,z2) = -int da (1-a)/a [2O - O(z12^a,z2) - O(z1,z21^a)] + int_0^1 da int_0^{1-a} db O(z12^a, z21^b) - O/2,
# acting on a quark with light-cone fraction 1: y_eff = 1 - a(1-xi) - b(1+xi).
a_, b_ = sp.symbols('a b', positive=True)
def push(weight, ycond_list):
    return weight
# sail on z1: y = 1 - a(1-xi) -> a = (1-x)/(1-xi), jacobian 1/(1-xi), needs 0<a<1 <=> xi<x<1
sail1 = ((1 - a_)/a_).subs(a_, (1 - x)/(1 - xi))/(1 - xi)
# sail on z2: y = 1 - a(1+xi) -> a = (1-x)/(1+xi), 0<a<1 <=> -xi<x<1
sail2 = ((1 - a_)/a_).subs(a_, (1 - x)/(1 + xi))/(1 + xi)
# vertex: b = (1 - x - a(1-xi))/(1+xi), jacobian 1/(1+xi), a in [0, min((1-x)/(1-xi), (x+xi)/(2xi))]
vtx_DGLAP = ((1 - x)/(1 - xi))/(1 + xi)
vtx_ERBL = ((x + xi)/(2*xi))/(1 + xi)
V_DGLAP = sp.simplify(sail1 + sail2 + vtx_DGLAP)
V_ERBL = sp.simplify(sail2 + vtx_ERBL)
print('V (DGLAP, xi<x<1) from light-ray kernel =', sp.factor(V_DGLAP), ' ; == (1+x^2-2xi^2)/((1-x)(1-xi^2)):', sp.simplify(V_DGLAP - A) == 0)
print('V (ERBL, |x|<xi)  from light-ray kernel =', sp.factor(V_ERBL), ' ; == E :', sp.simplify(V_ERBL - E) == 0)
print('mu-log coefficients of the explicit kernel: G2 -> E, G3 -> A, G1 and -G1 -> 0 :',
      [sp.simplify(sp.expand(G).coeff(lmu) - ref) == 0 for G, ref in ((G2, E), (G3, A), (G1, 0), (Gout, 0))])
print('structure: cP = (1/2) x [(x+xi)-type part of the evolution kernel], cM = (1/2) x [(x-xi)-type part]:',
      sp.simplify(2*cp_closed(1) - sail2 - vtx_ERBL) == 0)
# Ji, Schaefer, Xiong, Zhang PRD 92 (2015) 014039 eq. (31) (cutoff scheme), ERBL region: coefficient of ln(eta+zeta)
Aj = (1 + x**2 - 2*xi**2)/(2*(1 - x)*(1 - xi**2)); Bj = (x + xi**2)/(2*xi*(1 - xi**2))
print('Ji et al. 2015, ERBL: coeff of ln(x+xi) = A/2 + B, equals 2 cP:', sp.simplify(Aj + Bj - 2*cp_closed(1)) == 0,
      '; coeff of ln(xi-x) = -A/2 + B, equals 2 cM (with |x-xi| = xi-x):', sp.simplify(-Aj + Bj - 2*cm_closed(-1)) == 0)
# compare with the form printed in Su et al. arXiv:2609.20545 eq. (7) for the INVERSE kernel (x = light-cone):
# (1/(2(y-x)) -+ 1/(4xi)) |x+-xi|/(y+-xi) ln[...]; at one loop the inverse kernel is minus the forward one:
y = sp.Symbol('y', positive=True)
inv_from_forward_p = -(1/(2*(y - x)) + 1/(4*xi))*(x + xi)/(y + xi)
su_p = (1/(2*(y - x)) - 1/(4*xi))*(x + xi)/(y + xi)
print('Su et al. eq.(7) [+] minus (-forward) =', sp.factor(sp.simplify(su_p - inv_from_forward_p)), ' (difference in the sign of the 1/(2(y-x)) term)')
print('PASS' if allok else 'FAIL')
