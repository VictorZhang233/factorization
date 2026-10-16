import sys,os; sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp, mpmath as mp
L=sp.symbols('L',real=True); pi=sp.pi
# single heavy-light Sudakov factor (one quark-link vertex), units alpha_s C_F:
Cp = (-4 - 5*pi**2/6 + 2*(L+sp.I*pi) - (L+sp.I*pi)**2)/(8*pi)
Cm = (-4 - 5*pi**2/6 + 2*(L-sp.I*pi) - (L-sp.I*pi)**2)/(8*pi)
H_TMD = (-2 + pi**2/12 - L**2/2 + L)/(2*pi)          # APPB (85) / PLB (25) one-loop, units alpha_s C_F
print('one-loop: (C+ + C-) - H_TMD =', sp.simplify(sp.expand(Cp+Cm) - H_TMD))
print('pair (LFWF, same sign) 2*C+ =', sp.simplify(sp.expand(2*Cp)), ' vs JLS(4.2): (alpha CF/4pi)(-4-5pi^2/6+2L+ - L+^2)')
print('Im part of 2*C+ (phase at one loop):', sp.simplify(sp.im(sp.expand(2*Cp))))
# (C.1) of 2312.05957: I_n = int dE/(2 pi i) e^{-nu|E|/sqrt2}[prod 1/(E-Ek-i0) - prod 1/(E-Ek+i0)] = sum_k e^{-nu Ek/sqrt2} prod_{j!=k} 1/(Ek-Ej)
mp.mp.dps=30
def rhs(E,nu): return sum(mp.e**(-nu*Ek/mp.sqrt(2))*mp.fprod([1/(Ek-Ej) for Ej in E if Ej!=Ek]) for Ek in E)
def mid(E,nu):   # i * int dw/pi sin(nu w/sqrt2) prod 1/(i w - Ek)
    f=lambda w: mp.sin(nu*w/mp.sqrt(2))*mp.fprod([1/(1j*w-Ek) for Ek in E])
    return 1j*mp.quadosc(f,[-mp.inf,mp.inf],omega=nu/mp.sqrt(2))/mp.pi
for E,nu in [([1.3,2.1],0.7),([0.5,1.7,2.9],1.1),([0.9,1.0,3.3,4.0],0.4)]:
    print('n=%d'%len(E),' rhs=',mp.nstr(rhs(E,nu),12),' middle=',mp.nstr(mid(E,nu),12))
