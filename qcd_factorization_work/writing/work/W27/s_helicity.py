#!/usr/bin/env python3
"""W27 / Ch24 prop:front-smallx-helicity: writer check of the two closed forms quoted from Borden-Kovchegov
(PRD 108 (2023) 014001; also two verify/ records of claim E34(iv)):
  BK : DgGG(w) = (w/2)[1 - sqrt(1 - (16a/w^2) sqrt(1 - 4a/w^2))]
  BER: DgGG(w) = (w/2)[1 - sqrt(1 - (16a/w^2)(1 - 3a/w^2)/(1 - a/w^2))]     (pure glue, large Nc)
  a = alpha_s Nc/(2 pi).  Expansion coefficients of a^k/w^(2k-1) and intercepts (zero of the outer root)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
y = sp.symbols('y', positive=True)   # y = a/w^2 ; DgGG/w = (1/2)[1 - sqrt(...)] = sum c_k y^k  ->  DgGG = sum c_k a^k / w^(2k-1)
bk = sp.Rational(1, 2) * (1 - sp.sqrt(1 - 16*y*sp.sqrt(1 - 4*y)))
ber = sp.Rational(1, 2) * (1 - sp.sqrt(1 - 16*y*(1 - 3*y)/(1 - y)))
cbk = [sp.series(bk, y, 0, 7).removeO().coeff(y, k) for k in range(1, 6)]
cber = [sp.series(ber, y, 0, 7).removeO().coeff(y, k) for k in range(1, 6)]
print('BK  coefficients:', cbk); print('BER coefficients:', cber)
ok1 = cbk == [4, 8, 56, 496, 4824] and cber == [4, 8, 56, 504, 4920]
print(("[PASS] " if ok1 else "[FAIL] ") + "expansions 4,8,56,496,4824 (BK) vs 4,8,56,504,4920 (BER): agree through three loops")
u = sp.symbols('u', positive=True)   # u = w^2/a ; outer root vanishes at 1 = (16/u) sqrt(1-4/u)  <=>  u^3 - 256u + 1024 = 0
pbk = sp.expand(u**3 - 256*u + 1024); pber = sp.expand(u**2 - 17*u + 48)
rbk = max(sp.Poly(pbk, u).nroots(n=30), key=lambda r: sp.re(r)); rber = (17 + sp.sqrt(97))/2
chk_bk = sp.N((16/rbk)*sp.sqrt(1 - 4/rbk), 25); chk_ber = sp.N((16/rber)*(1 - 3/rber)/(1 - 1/rber), 25)
abk = sp.sqrt(rbk); aber = sp.sqrt(rber)
print(f"   BK  intercept sqrt(u) = {sp.N(abk, 12)}  (outer-root argument check {chk_bk})")
print(f"   BER intercept sqrt(u) = {sp.N(aber, 12)}  (check {chk_ber})")
c = mp.cbrt(mp.mpc(-9, mp.sqrt(111))); closed = 4/mp.cbrt(3)*mp.sqrt(mp.re(c))
ok2 = abs(float(abk) - 3.66074) < 5e-6 and abs(float(aber) - 3.66394) < 5e-6 and abs(float(closed) - float(abk)) < 1e-12
print(("[PASS] " if ok2 else "[FAIL] ") + f"intercepts 3.66074 (= (4/3^(1/3)) sqrt(Re[(-9+i sqrt111)^(1/3)]) = {mp.nstr(closed,10)}) and 3.66394 = sqrt((17+sqrt97)/2)")
# the inner branch point of BK (u = 4) lies to the left of the outer one, so the outer zero is the rightmost singularity
print(("[PASS] " if float(rbk) > 4 else "[FAIL] ") + f"rightmost singularity is the outer root: u_BK = {sp.N(rbk,10)} > 4")
