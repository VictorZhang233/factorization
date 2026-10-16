#!/usr/bin/env python3
"""E13 side issue: APPB App. F map (t,z)->(it,iz) vs Liu 2024 eq. (3.25) (t,z)->(iz,it)."""
import sys, os
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import sympy as sp
g = sp.diag(1, -1)
L_appb = sp.Matrix([[sp.I, 0], [0, sp.I]])   # (t,z) -> (it, iz)
L_liu = sp.Matrix([[0, sp.I], [sp.I, 0]])    # (t,z) -> (iz, it)
for name, L in [('APPB (it,iz)', L_appb), ('Liu24 (iz,it)', L_liu)]:
    print(f'{name}: L^T g L = {list(L.T*g*L)} (g = [1,0,0,-1]), det = {L.det()}')
n, nb = sp.Matrix([1, 1]), sp.Matrix([1, -1])
print('Liu24: L(-i n) =', list(L_liu*(-sp.I*n)), '= n ;  L(-i nbar) =', list(L_liu*(-sp.I*nb)), '= -nbar')
v0, vz = sp.symbols('v0 vz')
print('APPB map: L(-i v) =', list(L_appb*(-sp.I*sp.Matrix([v0, vz]))), '(= v, not n);  Liu24 map: L(-i v) =', list(L_liu*(-sp.I*sp.Matrix([v0, vz]))))
ok = (L_appb.T*g*L_appb == -g) and (L_liu.T*g*L_liu == g) and L_liu.det() == 1
print('PASS' if ok else 'FAIL', '(it,iz) is not Lorentz (maps g to -g, det -1); (iz,it) is a proper complex Lorentz map (boost with rapidity i pi/2)')
