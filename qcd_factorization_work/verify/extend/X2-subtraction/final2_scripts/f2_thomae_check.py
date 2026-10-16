"""X2 final2 / f2_thomae_check.py -- Prop E.4(d): the Thomae relation used for C1C1,
   3F2(a,b,c;d,e;1) = G(d)G(e)G(s)/(G(a)G(s+b)G(s+c)) 3F2(d-a,e-a,s;s+b,s+c;1),  s = d+e-a-b-c,
follows from applying DLMF eq. 16.4.11,
   3F2(al,be,ga;de,et;1) = G(et)G(sig)/(G(et-al)G(sig+al)) 3F2(al,de-be,de-ga;de,sig+al;1),  sig = de+et-al-be-ga,
   valid for Re(sig) > 0, Re(et-al) > 0,
twice (with the symmetry of 3F2 in its numerator and in its denominator parameters).  Symbolic search of the two-step
chains; validity conditions checked at (a,b,c;d,e) = (1, 1-eps, 1-2eps; 2-2eps, 1-3eps) for -1/2 < eps < 0; numerical
check of the composite identity at random generic parameters."""
import sys, os, itertools, random
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
import mpmath as mp
a, b, c, d, e = sp.symbols('a b c d e'); ep = sp.Symbol('epsilon')
G = sp.gamma
def T(num, den, ia, idl):
    al = num[ia]; be, ga = [num[i] for i in range(3) if i != ia]
    de = den[idl]; et = den[1 - idl]
    s = sp.expand(de + et - al - be - ga)
    return G(et)*G(s)/(G(et - al)*G(s + al)), (al, sp.expand(de - be), sp.expand(de - ga)), (de, sp.expand(s + al)), (s, sp.expand(et - al))
s0 = d + e - a - b - c
tn = sorted([sp.expand(d - a), sp.expand(e - a), sp.expand(s0)], key=str); td = sorted([sp.expand(s0 + b), sp.expand(s0 + c)], key=str)
tf = G(d)*G(e)*G(s0)/(G(a)*G(s0 + b)*G(s0 + c))
chains = []
for ia, idl in itertools.product(range(3), range(2)):
    f1, n1, d1, c1 = T((a, b, c), (d, e), ia, idl)
    for ja, jdl in itertools.product(range(3), range(2)):
        f2, n2, d2, c2 = T(n1, d1, ja, jdl)
        if sorted(n2, key=str) == tn and sorted(d2, key=str) == td and sp.simplify(sp.gammasimp(f1*f2/tf)) == 1:
            chains.append(((ia, idl), (ja, jdl), c1, c2))
print("two-step chains of DLMF 16.4.11 giving the Thomae form (prefactor ratio 1):", len(chains))
sub = {a: 1, b: 1 - ep, c: 1 - 2*ep, d: 2 - 2*ep, e: 1 - 3*ep}
ok_any = False
for ch in chains:
    conds = [sp.simplify(x.subs(sub)) for x in (ch[2] + ch[3])]
    good = all(sp.simplify(cc.subs(ep, sp.Rational(-1, 4))) > 0 and sp.simplify(cc.subs(ep, sp.Rational(-1, 100))) > 0
               and sp.simplify(cc.subs(ep, sp.Rational(-49, 100))) > 0 for cc in conds)
    print(f"   chain {ch[0]} then {ch[1]}: validity conditions (Re sig > 0, Re(et-al) > 0) at our parameters: {conds}"
          f" -> all > 0 on (-1/2, 0): {good}")
    ok_any |= good
mp.mp.dps = 30; random.seed(3); okn = True
for _ in range(3):
    A = mp.mpf(random.uniform(0.6, 0.9)); Bv, C = [mp.mpf(random.uniform(0.1, 0.9)) for _ in range(2)]
    D, E = A + Bv + C + mp.mpf(random.uniform(0.6, 1.0)), mp.mpf(random.uniform(1.0, 2.0))
    S = D + E - A - Bv - C
    lhs = mp.hyp3f2(A, Bv, C, D, E, 1)
    rhs = mp.gamma(D)*mp.gamma(E)*mp.gamma(S)/(mp.gamma(A)*mp.gamma(S + Bv)*mp.gamma(S + C))*mp.hyp3f2(D - A, E - A, S, S + Bv, S + C, 1)
    okn &= abs(lhs/rhs - 1) < mp.mpf('1e-20')
    print(f"   numeric check at generic parameters: lhs {mp.nstr(lhs, 20)} rhs {mp.nstr(rhs, 20)}")
print("ALL CHECKS PASS" if (chains and ok_any and okn) else "SOME CHECK FAILED")
