# Round-2 reviewer #1: predicted end-pole values of T2'(b) for the apole and alt parameter sets
# (Re p_opp = 1/2 a1 al1/(a1 al1 + a2|d10|) for an A-side alpha_1 > 0 pole; mirror for a B-side alpha_2 > 0 pole),
# computed from the model parameters of scripts/twoexch_rotated_fast.py (lambda = 1 units).
def E(pT, m, x): return (pT[0]**2 + pT[1]**2 + m**2)/(2*x)
def jp(M, ma, ms, xs, sT, k1T, k2T):
    P = M**2/2; sub = lambda u, v: (u[0]-v[0], u[1]-v[1])
    s0T = sub(sub(sT, k1T), k2T); s1T = sub(sT, k2T); s2T = sub(sT, k1T); aT = (-s0T[0], -s0T[1])
    Ea = E(aT, ma, 1-xs); Es = E(sT, ms, xs); Es0 = E(s0T, ms, xs); Es1 = E(s1T, ms, xs); Es2 = E(s2T, ms, xs)
    return dict(d0=P-Ea-Es0, d10=P-Ea-Es1, d20=P-Ea-Es2, beta=Ea+Es-P, al0=Es-Es0, al1=Es-Es1, al2=Es-Es2)
k1T = (0.8, 0.1); k2T = (-0.3, 0.9); a1 = 0.65; a2 = 0.90
pa = jp(0.9, 0.5, 0.7, 0.4, (-0.3, 1.0), k1T, k2T)
print("apole jet A:", {k: round(v, 4) for k, v in pa.items()})
print("  predicted Re p_opp =", round(0.5*a1*pa['al1']/(a1*pa['al1'] + a2*abs(pa['d10'])), 5), " (report 0.2517; numerics 0.2626, 0.2536, 0.2520)")
pb = jp(0.8, 0.6, 0.5, 0.55, (-0.9, 1.1), (-0.8, -0.1), (0.3, -0.9))
print("alt jet B:", {k: round(v, 4) for k, v in pb.items()})
print("  predicted Re p_opp =", round(0.5*a2*pb['al2']/(a2*pb['al2'] + a1*abs(pb['d20'])), 5), " (report 0.0483; numerics 0.0692, 0.0520, 0.0490)")
