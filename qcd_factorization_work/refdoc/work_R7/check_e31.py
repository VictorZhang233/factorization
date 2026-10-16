"""Toy check of the SS-line localisation error (E.30)-(E.31) of the reference document.
J_A(k^-) = 1/((k-al+i0)(k-be-i0))   [spectator insertion on J_A, Example E.23 form, J_A(tau=0)=i/(be-al)]
J_B(p)   = 1/((p-al2+i0)(p-be2-i0)), p = -k^+ flowing into J_B          [J_B(tau=0) = i/(be2-al2)]
G        = 1/(2k^+k^- - kT^2 + i0)                                       [full connecting propagator]
exact  I  = int dk^-/2pi dk^+/2pi J_A J_B G
approx I0 = J_A(0) J_B(0) (-1/kT^2)
Claim (E.31): relative error ~ (nuA nuB/kT^2)(1 + ln(kT^2/(nuA nuB))).
Computation: k^- by residues (UHP: k^- = be, and the G pole when k^+<0); k^+ part 1 by residues,
part 2 (theta(-k^+)) by quadrature (no singularities on (-inf,0) for al,be>0, al2,be2<0)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import mpmath as mp
mp.mp.dps = 30
kT = mp.mpf(1)
def run(nuA, nuB):
    al, be = mp.mpf('0.7') * nuA, mp.mpf('1.9') * nuA
    al2, be2 = mp.mpf('-0.8') * nuB, mp.mpf('-2.1') * nuB
    I0 = (1j / (be - al)) * (1j / (be2 - al2)) * (-1 / kT**2)
    # part 1: i/(be-al) * int dk+/2pi J_B(-k+) G(k+, be); close UHP: pole k+ = -al2 (+i0); G pole in LHP (be>0)
    part1 = (1j / (be - al)) * 1j * (1 / (be2 - al2)) * (1 / (2 * be * (-al2) - kT**2))
    # part 2: i * int_{-inf}^0 dk+/2pi J_B(-k+) J_A(z)/(2k+), z = kT^2/(2k+)
    JA = lambda x: 1 / ((x - al) * (x - be))
    JB = lambda p: 1 / ((p - al2) * (p - be2))
    f = lambda kp: JB(-kp) * JA(kT**2 / (2 * kp)) / (2 * kp)
    pts = [-mp.inf] + sorted([-mp.mpf(10)**e for e in range(-12, 4)]) + [0]
    part2 = 1j * mp.quad(f, pts) / (2 * mp.pi)
    I = part1 + part2
    return I, I0
print(" nuA*nuB/kT^2     rel.err        rel.err / [x(1+ln(1/x))]    rel.err/x")
for (nuA, nuB) in [(1e-1, 1e-1), (3e-2, 3e-2), (1e-2, 1e-2), (3e-3, 3e-3), (1e-3, 1e-3), (1e-4, 1e-4), (1e-5, 1e-5), (1e-3, 1e-5)]:
    nuA, nuB = mp.mpf(nuA), mp.mpf(nuB)
    I, I0 = run(nuA, nuB)
    x = nuA * nuB / kT**2
    rel = abs(I - I0) / abs(I0)
    print(f" {mp.nstr(x,3):>10s}   {mp.nstr(rel,6):>12s}   {mp.nstr(rel/(x*(1+mp.log(1/x))),6):>12s}            {mp.nstr(rel/x,6):>10s}")
