# N11 (stage 2): mechanical consistency audit of the LAMET.md section 4.5 dependency table.
# Rule: grade(node) <= min( grade(parents), grade(implication) ), order [R] > [A] > [P] > [C] > [V].
# Also: which [C] inputs each node ultimately depends on (non-perturbative content).
order = {'R': 4, 'A': 3, 'P': 2, 'C': 1, 'V': 0}
# (H*) hypotheses with their grades (LAMET 4.1); H4 is [A] in PT / [C] non-perturbatively -> use C for hadrons
hyp = {'H3': 'C', 'H4np': 'C', 'H5': 'C', 'IMQY': 'A', 'OPEext': 'A', 'alpha_rep': 'R', 'LCgauge_pc': 'A', 'Lorentz': 'R', 'ZX_pert_hybrid': 'A', 'ZX_pert_ratio': 'C'}
# node: (parents (any-of groups expressed as lists of alternatives), implication grade, printed grade)
table = {
 'N0':  ([], 'R', 'R'),
 'N1':  ([['N0']], 'A', 'A'),
 'N2':  ([['N1']], 'A', 'A'),
 'N3':  ([['N2', 'IMQY']], 'R', 'A'),          # route A (N2) or route B (IMQY)
 'N4':  ([['N3'], ['OPEext']], 'A', 'A'),
 'N5':  ([['alpha_rep']], 'R', 'R'),
 'N6':  ([['N4'], ['N5']], 'R', 'A'),
 'N7':  ([['N6']], 'R', 'A'),
 'N8':  ([['N0'], ['LCgauge_pc']], 'A', 'A'),
 'N9':  ([['N7', 'N8']], 'R', 'A'),
 'N10': ([['Lorentz']], 'R', 'R'),
 'N11': ([['H4np']], 'R', 'R(cond)'),
 'N12': ([['N9'], ['N10'], ['N11'], ['H3'], ['H5']], 'R', 'C'),
 'N13h': ([['N9'], ['ZX_pert_hybrid']], 'R', 'A'),
 'N13r': ([['N9'], ['ZX_pert_ratio']], 'R', 'C'),
}
grade = dict(hyp)
def g(x):
    if x in grade: return grade[x]
    parents, imp, printed = table[x]
    best = imp
    for alts in parents:
        a = max((g(p) for p in alts), key=lambda s: order[s])   # any-of: best alternative
        best = min(best, a, key=lambda s: order[s])
    grade[x] = best
    return best
ok_all = True
for n, (parents, imp, printed) in table.items():
    gn = g(n)
    pr = printed.replace('(cond)', '')
    if printed.endswith('(cond)'):
        status = "consistent (conditional on its hypothesis; unconditional grade %s)" % gn
        ok = True
    else:
        ok = order[pr] <= order[gn]
        status = ("OK" if ok else "VIOLATION") + " (printed %s, max allowed %s)" % (pr, gn)
    ok_all &= ok
    print("%-5s %s" % (n, status))
def npinputs(x):
    if x in hyp: return {x} if hyp[x] == 'C' else set()
    s = set()
    for alts in table[x][0]:
        # for any-of groups take the alternative with the best grade (fewest [C] inputs)
        cand = [npinputs(p) for p in alts]
        s |= min(cand, key=len)
    return s
print("\nnon-perturbative ([C]) inputs:")
for n in ['N9', 'N12', 'N13h', 'N13r']:
    print("  %-5s <- %s" % (n, sorted(npinputs(n)) or "none"))
print("\nmonotone grading:", "PASS" if ok_all else "FAIL")
print("N12 (Thm 4.3(ii), MS-bar) non-perturbative content = {H3, H4(np), H5}:", "PASS" if npinputs('N12') == {'H3', 'H4np', 'H5'} else "FAIL")
print("ratio/RI-MOM momentum-space matching (N13) needs an input outside (H3)-(H5):", "YES" if npinputs('N13r') - {'H3', 'H4np', 'H5'} else "NO")
