# P2 check: strict Glauber propagator + independent truncations of k^- (A side) and k^+ (B side).
# Eikonal two-insertion model of Lemma E.48(d): orderings give i/(+-2p k + i0); window [-K1,K2].
import sys,os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps=25
def weights(K1,K2,p=1,eps=mp.mpf('1e-9')):
    f12=lambda k: 1j/(2*p*k+1j*eps)
    f21=lambda k: 1j/(-2*p*k+1j*eps)
    I12=mp.quad(f12,[-K1,-1e-6,0,1e-6,K2]); I21=mp.quad(f21,[-K1,-1e-6,0,1e-6,K2])
    S=I12+I21
    return I12/S, I21/S
for (K1,K2) in [(1,1),(1,3),(1,mp.e**mp.pi),(mp.e**mp.pi,1)]:
    w12,w21=weights(K1,K2)
    print(f"window [-{mp.nstr(K1,4)},{mp.nstr(K2,4)}]: w12={mp.nstr(w12,8)}  w21={mp.nstr(w21,8)}  predicted 1/2 + i ln(K2/K1)/(2pi) = {mp.nstr(0.5+1j*mp.log(K2/K1)/(2*mp.pi),8)}")
# p_opp for independent A and B truncations: W(piA,piB)=wA(piA) wB(piB)
def popp(wa,wb): return wa[0]*wb[1]+wa[1]*wb[0]
for (a,b) in [((1,1),(1,1)),((1,3),(1,3)),((1,mp.e**mp.pi),(mp.e**mp.pi,1)),((1,mp.e**mp.pi),(1,mp.e**mp.pi))]:
    wa=weights(*a); wb=weights(*b)
    print(f"A-window {tuple(mp.nstr(x,4) for x in a)}, B-window {tuple(mp.nstr(x,4) for x in b)}: p_opp = {mp.nstr(popp(wa,wb),8)}")
# smooth even regulators with line-dependent scales (Lorentzian, |z|>>K): race of regulator poles
def w_lor(K1,K2):
    # line 1 regulator K1, line 2 regulator K2; u+ = u- = 1/2 each line
    init = K2/(K1+K2)   # both initial: time-reversed race, P(1 before 2)
    fin  = K1/(K1+K2)   # both final: forward race
    return 0.25*(init+fin+1+0)
print('Lorentzian, line-dependent scales (1,5): w12 =', w_lor(1.0,5.0))
# smooth NON-even, line-dependent regulators chi_e(k)=K1e K2e/((K1e+ik)(K2e-ik)): u+ = K2e/(K1e+K2e)
def w_asym(K1a,K2a,K1b,K2b):
    up1=K2a/(K1a+K2a); um1=1-up1; up2=K2b/(K1b+K2b); um2=1-up2
    init = K1b/(K1a+K1b)   # both initial: rates |iK1| ; P(1 before 2) = rate2/(rate1+rate2)
    fin  = K2a/(K2a+K2b)   # both final: rates K2 ; P(1 first)=rate1/(rate1+rate2)
    return up1*up2*init + um1*um2*fin + up1*um2*1 + um1*up2*0
print('asymmetric smooth, identical lines:', w_asym(1,3,1,3), '; line-dependent:', w_asym(1,3,4,0.5))
