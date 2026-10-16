# Final review of X1 -- arithmetic of T2 Steps 3-8 (explicit constants).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
pi = np.pi
ok = True
# L8(g) -> E-constants
print("E1 coeff 2*12*4/(4 pi^2) =", 2*12*4/(4*pi**2), " vs 24/pi^2 =", 24/pi**2)
print("E2 coeff 6600/(2*4 pi^2) =", 6600/(8*pi**2), " vs 825/pi^2 =", 825/pi**2)
print("E3 coeff 2*3200/(4 pi^2) =", 6400/(4*pi**2), " vs 1600/pi^2 =", 1600/pi**2)
print("E4 coeff 2*86/(4 pi^2)   =", 172/(4*pi**2), " vs 43/pi^2 =", 43/pi**2)
print("E6 coeff 2*32/(4 pi^2)   =", 64/(4*pi**2), " vs 16/pi^2 =", 16/pi**2)
print("L8(g) strip: (256/3) =", 256/3, "<= 86;  generic 384*sqrt(17/16) =", 384*np.sqrt(17/16), "<= 400")
print("L8(c) axis band total 4/3+25/9+25/9+3.2*0.354 =", 4/3 + 25/9 + 25/9 + 3.2*np.sqrt(2)/4, "<= 9")
print("2E2 coefficient 1650/pi^2 =", 1650/pi**2, " (report: ~167)")
print("C_N: 2*1600+43 =", 2*1600 + 43, " (report 3243);  C_E: 1600+43+16+2*4 =", 1600 + 43 + 16 + 8, " (report 1667)")
# eps (1+2L)^2 <= 11.2 eps^1/2 for eps <= 1/16
eps = np.exp(-np.linspace(np.log(16), 200, 200001)); L = np.log(1/eps)
r = (eps*(1 + 2*L)**2/np.sqrt(eps)).max(); print(f"max eps^1/2 (1+2L)^2 over eps<=1/16 = {r:.4f} (<= 11.2)"); ok &= r <= 11.2
# sup_{eps<=1/16} eps^1/2 (1+L_B)^2 <= 3 + l_B^2, L_B = ln(1+4 eps^-1/2 x), l_B = ln(1+16x), x = lambda_B/mu_B >= 1
worst = 0
for x in np.exp(np.linspace(0, 12, 400)):
    LB = np.log(1 + 4*x/np.sqrt(eps)); lB = np.log(1 + 16*x)
    worst = max(worst, (np.sqrt(eps)*(1 + LB)**2).max()/(3 + lB**2))
print(f"max_x sup_eps eps^1/2(1+L_B)^2/(3+l_B^2) = {worst:.4f} (<= 1)"); ok &= worst <= 1
# L_B <= L/2 + ln(1+4x)
worst2 = 0
for x in np.exp(np.linspace(0, 12, 200)):
    worst2 = max(worst2, (np.log(1 + 4*x/np.sqrt(eps)) - (L/2 + np.log(1 + 4*x))).max())
print(f"max [L_B - L/2 - ln(1+4x)] = {worst2:.2e} (<= 0)"); ok &= worst2 <= 1e-12
# int |g| <= 4 Mflat (1+l_B) for lambda/mu >= 1 : 4 asinh(x) + 8 <= 4(1 + ln(1+16x)) ?
xs = np.exp(np.linspace(0, 20, 2001))
lhs = 2*2*np.arcsinh(xs) + 8; rhs = 4*(1 + np.log(1 + 16*xs))
print(f"max [int|g| bound / 4Mflat(1+l_B)] = {(lhs/rhs).max():.4f} (<= 1)"); ok &= (lhs/rhs).max() <= 1
print("ALL PASS" if ok else "SOME CHECK FAILED")
