# W26 / Ch23 -- s14: independent re-check (resumed session) of prop:yzliu-gpd-oneloop.
# Source kernel: Liu:2019urm (arXiv:1902.00307) eqs. (40)-(46), gamma^t, transcribed from the rendered page 7.
# x' = quasi/parent momentum fraction, xi' = skewness/parent; L = ln(4 p_z^2/mu^2).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
x, xi, L = sp.symbols('x xi L', real=True)
lp, lm, l1 = sp.symbols('lp lm l1', real=True)   # ln|x+xi|, ln|x-xi|, ln|1-x|
# eq. (41): G1 = -[1/(x-1) - x/(2xi) + (1+x)/(2(1+xi))] ln((x-1)/(x+xi)) + (xi -> -xi),  valid for x < -xi
bp = 1/(x-1) - x/(2*xi) + (1+x)/(2*(1+xi)); bm = bp.subs(xi, -xi)
G1 = -bp*(l1-lp) - bm*(l1-lm)
# eq. (43): G2, |x|<xi
E = (x+xi)*(1-x+2*xi)/(2*(1-x)*xi*(1+xi)); D = (x+xi**2)/(xi*(1-xi**2))
G2 = E*(L + 2*l1 + lp - lm - 1) + D*(lm - l1)
# eq. (46): G3, xi<x<1
A = (1+x**2-2*xi**2)/((1-x)*(1-xi**2)); B = (x+xi**2)/(2*xi*(1-xi**2))
G3 = A*(L + (lp+lm)/2 + l1 - 1) + B*(lp - lm)
# closed forms claimed in the chapter: c_pm = |x pm xi|/(1 pm xi) [1/(2(1-x)) pm 1/(4 xi)]
def cpm(s, absval):  # absval = |x + s xi| as an expression valid in the region
    return absval/(1+s*xi)*(1/(2*(1-x)) + s/(4*xi))
regions = {
  'x<-xi'   : (G1, -(x+xi), -(x-xi)),
  '|x|<xi'  : (G2,  (x+xi), -(x-xi)),
  'xi<x<1'  : (G3,  (x+xi),  (x-xi)),
  'x>1'     : (-G1, (x+xi),  (x-xi)),
}
allok = True
for name, (G, ap, am) in regions.items():
    G = sp.expand(G)
    cL = sp.simplify(sp.diff(G, L)); clp = sp.diff(G, lp); clm = sp.diff(G, lm); cl1 = sp.diff(G, l1)
    # ell(s) = L + 2 ln|s|  ->  c_+ = clp/2, c_- = clm/2, c_1 = cl1/2, and consistency cL = c_+ + c_- + c_1
    ok1 = sp.simplify(cL - (clp + clm + cl1)/2) == 0
    ok2 = sp.simplify(clp/2 - cpm(+1, ap)) == 0
    ok3 = sp.simplify(clm/2 - cpm(-1, am)) == 0
    allok &= ok1 and ok2 and ok3
    print('%-8s  decomposition consistent: %s ; c_+ closed form: %s ; c_- closed form: %s' % (name, ok1, ok2, ok3))
print('all four regions:', allok)
# variable change: direct matching  Ftilde(y) = int dx/|x| C(y/x, xi/x, mu/(x P)) F(x), y quasi, x light-cone, x > |xi|, x>0
X, Y, XI = sp.symbols('X Y XI', positive=True)   # X light-cone, Y quasi, XI skewness (generic signs handled by abs)
cp_direct = (cpm(+1, sp.Abs(x+xi))/X).subs({x: Y/X, xi: XI/X})
target_direct = sp.Abs(Y+XI)/(X+XI)*(1/(2*(X-Y)) + 1/(4*XI))
print('direct kernel term  == |y+xi|/(x+xi)[1/(2(x-y)) + 1/(4xi)] :', sp.simplify(cp_direct - target_direct) == 0)
# inverse kernel at one loop: F(x) = int dy/|y| C^{-1}(x/y, xi/y, mu/(yP)) Ftilde(y), C^{-1,(1)} = - C^{(1)} with arguments (x/y, xi/y)
cp_inverse = (-cpm(+1, sp.Abs(x+xi))/Y).subs({x: X/Y, xi: XI/Y})
target_inverse = sp.Abs(X+XI)/(Y+XI)*(1/(2*(X-Y)) - 1/(4*XI))
su_eq7 = sp.Abs(X+XI)/(Y+XI)*(1/(2*(Y-X)) - 1/(4*XI))
print('inverse kernel term == |x+xi|/(y+xi)[1/(2(x-y)) - 1/(4xi)] :', sp.simplify(cp_inverse - target_inverse) == 0)
print('Su et al. eq. (7) (upper sign) minus inverse term          :', sp.simplify(su_eq7 - cp_inverse))
# the other reading of Su (7): x quasi, y light-cone (direct kernel C(x/y, xi/y, mu/(yP)))
cp_direct2 = (cpm(+1, sp.Abs(x+xi))/Y).subs({x: X/Y, xi: XI/Y})
print('Su et al. eq. (7) minus direct term with x quasi, y light-cone:', sp.simplify(su_eq7 - cp_direct2))
print('vanishing at x = -xi (inverse form):', sp.simplify(target_inverse.subs(X, -XI)) == 0)
