# Reviewer r3_2: two-loop planar vertex, exact integrated remainder values from the UD closed form (units Qt=1).
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
def UD2(m2):
    L = mp.log(1/m2)
    return (1+m2)/((1-m2)*(1+m2)**4)*(12*mp.polylog(4, -m2) + L**4/4 + mp.pi**2*L**2/2 + 7*mp.pi**4/60)
def LP(m2):
    L = mp.log(1/m2)
    return L**4/4 + mp.pi**2*L**2/2 + 7*mp.pi**4/60
for m2 in ['0.04', '0.01', '1e-3', '1e-4', '1e-5', '1e-6']:
    m2 = mp.mpf(m2); L = mp.log(1/m2)
    r = UD2(m2) - LP(m2)
    nlp = -m2*(L**4/2 + mp.pi**2*L**2 + 12 + 7*mp.pi**4/30)
    print(f"m2={mp.nstr(m2,3)}: int r = {mp.nstr(r, 8)}   NLP = {mp.nstr(nlp, 8)}   ratio = {mp.nstr(r/nlp, 7)}   UD2 = {mp.nstr(UD2(m2), 8)}")
# one-loop: int r = Phi1/Q^2 - (L^2+pi^2/3), check -4 m2 leading term
for m2 in ['1e-2', '1e-4', '1e-6']:
    m2 = mp.mpf(m2); L = mp.log(1/m2)
    r1 = 4*mp.polylog(2, -m2)/(1-m2**2) + (L**2 + mp.pi**2/3)*m2**2/(1-m2**2)
    print(f"one loop m2={mp.nstr(m2,3)}: int r = {mp.nstr(r1, 10)}  /(-4 m2) = {mp.nstr(r1/(-4*m2), 10)}")
