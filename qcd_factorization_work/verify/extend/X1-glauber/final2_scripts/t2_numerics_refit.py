# X1 final2 (Fix 7(b), LA-5) -- refit of the logged T2 numerics and decomposition of Re p_opp.
# Inputs (parsed, not retyped): review_r3_1_logs/t2_general.log (scalar base set and three non-factorized jet pairs,
# unregulated) and logs/twoexch_regulated.log (class-X k^+ regulator, K_c = lambda).
# (1) two-decade decay exponents of Re p_opp and first-decade slopes of Im p_opp per decade of eps (LA-5 values);
# (2) X := p_opp * Y with Y := N/N0 is the unnormalized opposite-ordering weight, (I(12,21)+I(21,12))/N0.  The C_A X
#     coefficient of the uncut side sum is proportional to Re X (normalization remark of T2); Re p_opp = Re(X/Y)
#     differs from it by the cross term.  Uncertainty of Re X from the printed digits is propagated.
import sys, os, re
sys.path.append(os.path.expanduser('~/Library/Python/3.9/lib/python/site-packages'))
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(here, '..')
out = []
def log(s=''):
    print(s, flush=True); out.append(s)
txt = open(os.path.join(base, 'review_r3_1_logs', 't2_general.log')).read()
def ndig_unc(sv):
    # half a unit in the last printed digit
    sv = sv.strip().lstrip('+-')
    if 'e' in sv or 'E' in sv:
        mant, ex = re.split('[eE]', sv); dec = len(mant.split('.')[1]) if '.' in mant else 0
        return 0.5*10**(-dec)*10**int(ex)
    dec = len(sv.split('.')[1]) if '.' in sv else 0
    return 0.5*10**(-dec)
rows = {}
# scalar base set lines: "lambda=0.01 (eps=1.167e-03), n=1600: p_opp = 0.0123468-2.113439i ;  N/N0 = 0.9984307-0.0057083i"
for m in re.finditer(r"lambda=([\d.]+) \(eps=([\d.e+-]+)\), n=1600: p_opp = ([\d.]+)([+-][\d.]+)i ;  N/N0 = ([\d.]+)([+-][\d.]+)i", txt):
    rows.setdefault('scalar base set', []).append((float(m.group(2)), m.group(3), m.group(4), m.group(5), m.group(6)))
# general pairs: "eps=8.92e-03 n=1200: Re p_opp = +0.0318461   Im p_opp = -1.60248   N/N0 = 0.993819-0.019797i"
blocks = re.split(r"\(1\) general pair (\d)", txt)
for i in range(1, len(blocks), 2):
    pair = 'pair ' + blocks[i]; body = blocks[i + 1].split('(1) general')[0].split('(2) P4')[0]
    best = {}
    for m in re.finditer(r"eps=([\d.e+-]+) n=(\d+): Re p_opp = ([+-][\d.]+)\s+Im p_opp = ([+-][\d.]+)\s+N/N0 = ([\d.]+)([+-][\d.]+)i", body):
        eps = float(m.group(1)); n = int(m.group(2))
        if eps not in best or n > best[eps][0]:
            best[eps] = (n, m.group(3), m.group(4), m.group(5), m.group(6))
    rows[pair] = [(e, v[1], v[2], v[3], v[4]) for e, v in sorted(best.items(), reverse=True)]
ok = True
log("(1) unregulated T2 numerics (review_r3_1_logs/t2_general.log; largest grid per eps):")
expo = {}
for name in ('scalar base set', 'pair 0', 'pair 1', 'pair 2'):
    pts = rows[name]
    eps = np.array([p[0] for p in pts]); re_ = np.array([float(p[1]) for p in pts]); im_ = np.array([float(p[2]) for p in pts])
    a = np.log(re_[0]/re_[-1])/np.log(eps[0]/eps[-1])
    slope1 = (im_[0] - im_[1])/np.log10(eps[0]/eps[1]); slope2 = (im_[1] - im_[2])/np.log10(eps[1]/eps[2])
    expo[name] = (a, slope1)
    log(f"    {name:16s}: eps = {', '.join(f'{e:.3g}' for e in eps)};  Re p_opp ~ eps^{a:.3f} over two decades;"
        f"  Im p_opp slope per decade: first {slope1:.3f}, second {slope2:.3f}   [(1/pi) ln 10 = {np.log(10)/np.pi:.3f}]")
ok &= abs(expo['pair 2'][0] - 0.63) < 0.006 and abs(expo['pair 1'][0] - 0.70) < 0.006 and abs(expo['pair 0'][0] - 0.73) < 0.006
ok &= abs(expo['pair 2'][1] - 0.680) < 0.001 and abs(expo['pair 1'][1] - 0.696) < 0.001 and abs(expo['pair 0'][1] - 0.717) < 0.001
log("    LA-5 values reproduced: exponents 0.63 (pair 2), 0.70 (pair 1), 0.73 (pair 0) [0.78 scalar base set];"
    " first-decade Im slopes 0.680 (pair 2), 0.696 (pair 1), 0.717 (pair 0)")
log("(2) decomposition Re p_opp = Re(X/Y), X = p_opp Y:  Re X  vs  cross term -Im X Im Y/|Y|^2 (unregulated):")
for name in ('scalar base set', 'pair 0', 'pair 1', 'pair 2'):
    for (e, sre, sim, syr, syi) in rows[name]:
        p = complex(float(sre), float(sim)); Y = complex(float(syr), float(syi)); X = p*Y
        unc = (ndig_unc(sre)*abs(Y) + ndig_unc(sim)*abs(Y) + abs(p)*(ndig_unc(syr) + ndig_unc(syi)))
        cross = -X.imag*Y.imag/abs(Y)**2
        log(f"    {name:16s} eps={e:.3g}: Re p_opp = {p.real:+.3e}; Re X = {X.real:+.2e} (+-{unc:.1e} from printed digits);"
            f" cross term = {cross:+.3e}; 1-Re Y = {1 - Y.real:+.2e}")
# regulated runs
txt2 = open(os.path.join(base, 'logs', 'twoexch_regulated.log')).read()
log("(3) class-X regulator runs (logs/twoexch_regulated.log, K_c = lambda, lambda_B ~ 4.4 lambda^2):")
reX = []
for m in re.finditer(r"lam=([\d.]+) set=(\w+) Kc=([\d.e+-]+) REGULATED: N/N0=([\d.]+)([+-][\d.]+)j  p_opp=([\d.]+)([+-][\d.]+)j", txt2):
    lam = float(m.group(1)); Y = complex(float(m.group(4)), float(m.group(5))); p = complex(float(m.group(6)), float(m.group(7)))
    X = p*Y; cross = -X.imag*Y.imag/abs(Y)**2
    log(f"    lambda={lam:<6g} {m.group(2):6s}: Re p_opp = {p.real:.5f};  Re X = {X.real:+.2e};  cross term = {cross:.5f};  1-Re Y = {1 - Y.real:.4f};  Im Y = {Y.imag:+.4f}")
    if m.group(2) == 'base':
        reX.append((lam, X.real, 1 - Y.real))
lam = np.array([r[0] for r in reX]); rx = np.array([abs(r[1]) for r in reX]); dy = np.array([r[2] for r in reX])
log(f"    base set: |Re X| ~ lambda^{np.log(rx[0]/rx[-1])/np.log(lam[0]/lam[-1]):.2f}, 1-Re Y ~ lambda^{np.log(dy[0]/dy[-1])/np.log(lam[0]/lam[-1]):.2f}"
    f" (lambda_B/K_c ~ lambda);  Re p_opp is the cross term -Im X Im Y/|Y|^2 up to Re X.")
# (4) the O(1) remainder Im p_opp + L/pi at the smallest eps (L = ln 1/eps), unregulated
log("(4) Im p_opp + L/pi (L = ln(1/eps)) at the smallest eps of each set (unregulated):")
for name in ('scalar base set', 'pair 0', 'pair 1', 'pair 2'):
    e, sre, sim, syr, syi = rows[name][-1]
    log(f"    {name:16s} eps={e:.3g}: Im p_opp + L/pi = {float(sim) + np.log(1/e)/np.pi:+.3f}")
log("ALL PASS" if ok else "SOME CHECK FAILED")
with open(os.path.join(base, 'final2_logs', 't2_numerics_refit.log'), 'w') as f:
    f.write('\n'.join(out) + '\n')
