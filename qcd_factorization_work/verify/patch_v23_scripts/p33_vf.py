import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
TARGET = 'VERIFIED_FORMULAS_v2.md'
V = lambda n: src.ln(n, 'VERIFIED_FORMULAS_v2.md')

FLAG_NEW = r'''**Flag (retired in v2.3).** Revision v2.2 appended a pending flag to the status of entries that supported a claimed literature erratum, a candidate 「本书新结果」, or an App M/N/O statement affected by the proof extensions X1–X3. The verify patch v2.3 (2026-10-11) resolved every flag: the outcome is now written in the status of each such entry and in the register at the end of this file (a record of outcomes). Entries whose claim was refuted were corrected (VF-LAM-9, VF-REF-12) or are marked "not printed".'''

LAM9_NEW = r'''$C^{\overline{\rm MS}}(\xi)\to-\frac{3a}{2|\xi|}$ and $C^{\rm ratio}(\xi)\to\mp\frac{4a}{3\xi^2}$ as $\xi\to\pm\infty$. Hence at $O(\alpha_s)$: the $\overline{\rm MS}$ quasi-PDF has no zeroth moment when $\int f\ne0$ ($\sim-\frac{3a}{2|x|}\int f$); in the ratio scheme $\int dx\,\tilde q=\int f$ but $\tilde q\to-\frac{4a}3{\rm sgn}(x)\langle y\rangle_{q+\bar q}/x^2$, so the first moment diverges logarithmically. Near $y=0$ the integrand of $\int\frac{dy}{|y|}C(\frac xy)f(y)$ is $-\frac{3a}{2|x|}f(y)(1+O(y))$ ($\overline{\rm MS}$), $\frac{3a}{2|x|}[\frac2\pi{\rm Si}(|x|z_SP^z)-1]f(y)(1+O(y))$ (hybrid, $\lambda_S=z_S|y|P^z$) and $O(|yf(y)|)$ (ratio): $\overline{\rm MS}$ and hybrid converge absolutely iff $\int_{|y|<\epsilon}|f|<\infty$, the ratio scheme needs only $\int|yf|<\infty$; for physical quark distributions (antiquarks at $y<0$) the $O(1)$ terms combine into $q-\bar q$, so all three schemes give finite quark quasi-PDFs when $q-\bar q$ and $y(q+\bar q)$ are integrable at small $y$ (e.g. a Regge-like sea $y^{-1-\delta}$, $\delta<1$).'''
LAM9_STATUS = r'''- **Status:** V for the tails and moments (LAMET s1 E, s5 L2; tails also from the kernels of `IzubuchiEtAl2018`, who state the $\overline{\rm MS}$ condition $f\sim y^{-1+a}$, $a>0$). v2.3: the convolution-domain part was **corrected** — claim N09 refuted as originally stated (the planning text claimed that the hybrid kernel needs only $\int|yf|<\infty$ and that a Regge-like sea makes the $\overline{\rm MS}$ formula ill-defined); the corrected statement is that of `verify/claims/batch_N07_s1.md` §4.3 (one confirmation; numerical checks there: slopes $-5.0001$ vs $-5$ and $-2.26110$ vs $-2.26104$); no novelty marker.'''

REF12_NEW = r'''Final group (all $k_e^+>0$, poles $z_e=\frac{k_{Te}^2}{2k_e^+}$ in the lower half-plane): $w_\pi=\prod_jz_j\big/\prod_m\sum_{l\ge m}z_{\pi(l)}$ ($N=2$: $w_{12}=\frac{z_1}{z_1+z_2}$); initial group (all $k_e^+<0$): **time-reversed**, $w_\pi=\prod_jz_j\big/\prod_m\sum_{l\le m}z_{\pi(l)}$; mixed signs: the weight of a sector is the product of the two groups' race weights (for $N=2$ with $k_1^+k_2^+<0$ the colour-order weight is 0 or 1); $\sum_\pi w_\pi=1$; as functions of $k^+$ the colour-order weights are continuous where at most one $k_e^+$ vanishes (with a kink there) and discontinuous where two or more vanish.'''
REF12_STATUS = r'''- **Status:** V (R8 `check_weights.py`; v2.3: X1 final report `checks_misc.py`, `refdoc/work_R7/check_weights_colour.py`, `fix_r2_scripts/l1_bound_quadrant.py`). The initial-group and mixed-sign forms correct the earlier entry (claim N13 refuted as stated: only the same-side lower-half-plane formula had been given); the race formula and $\sum w=1$ are classical (eikonal identity); never marked new.'''

OUT = {
 'VF-REF-9, VF-REF-10': ('N01 confirmed but known (`Meggiolaro:1996hf`, `Giordano:2006vv`): printed without marker', None),
 'VF-FRO-1': ('N02 confirmed; remark without novelty marker (search-date sentence)', None),
 'VF-FRO-3': ('N03 confirmed, not new in substance; E14 confirmed (Q3, attributed to `Collins:2020euz`)', None),
 'VF-FRO-15': ('N04 confirmed as [A] with prior art `Braun:2019qtp`', None),
 'VF-LAM-11': ('N07 confirmed, known in part (no marker); E07(i) confirmed (Q3, attributed to `Chen:2016utp`); E07(ii): VF-YZL-17 (new)', None),
 'VF-LAM-12': ('N08 confirmed, known in part (no marker)', None),
 'VF-LAM-9': ('N09 refuted as stated; entry corrected (hybrid domain; $q-\\bar q$ combination); no marker', None),
 'VF-LAM-17': ('N10 confirmed, known in substance (no marker)', None),
 'VF-GLA-10': ('N17 confirmed: attachment-sum form of `RogersMulders2010` eq. (34) (our derivation)', None),
 'VF-GLA-6': ('N18 confirmed: our compact derivation of known channel values', None),
 'VF-TMD-9': ('N20 confirmed (no marker); E17 confirmed: App Q row Q.2', None),
 'VF-EXC-14': ('N21 confirmed; novelty of the closed forms not asserted (ILS 1989 unread)', None),
 'VF-REF-2, VF-REF-3': ('N12 confirmed (never marked new); slot X2a delivered (`prop:appN-triangle-cs`)', None),
 'VF-REF-12': ('N13 refuted as stated; entry corrected; final `lem:appO-joint-localization`', None),
 'VF-REF-14': ('N15 confirmed (never marked new)', None),
 'VF-REF-1, VF-REF-4': ('X3 outcomes applied (FINAL_OUTLINE_v2 §00.4); VF-REF-4 threshold $n_0>A+1$', None),
 'VF-REF-7, VF-REF-11': ('X1 outcomes applied; formulas unchanged', None),
 'VF-LAM-7': ('N05 confirmed: our re-derivation of `IzubuchiEtAl2018` App. B', None),
 'VF-LAM-14': ('N06 confirmed: one-loop check of `Ji:2023pba`', None),
 'VF-GLA-8': ('N16 confirmed (our proof of a statement of `Collins2007`); E18 confirmed: App Q row Q.4', None),
 'VF-EE-8': ('N24 confirmed (our derivation; the BM II hypotheses are met by massless QCD in covariant gauges)', None),
 'VF-DY-12, VF-DY-13': ('N25 confirmed (novelty not claimed)', None),
 'VF-WL-2': ('N26 confirmed (operator-level regulator: `Echevarria:2015byo`; novelty not claimed)', None),
 'VF-LAM-8': ('N27 confirmed (a verification)', None),
 'VF-YZL-6, -9, -10, -11, -13': ('N29 confirmed (cross-checks)', None),
 'VF-GLA-9, VF-GLA-11': ('N19 confirmed (auxiliary; not printed as results)', None),
 'VF-BQ-3, VF-BQ-5': ('N22 refuted (the illustrative shift was wrong: $-\\pi^2$, independent of $X_A$); no illustration printed', None),
 'VF-FRO-7, VF-FRO-11': ('N28 confirmed (checked transcriptions)', None),
 'VF-LAM-10, VF-LAM-3': ('E01 confirmed: App Q row Q.8 (first corrected by `Chou:2022drv`)', None),
 'VF-LAM-15, VF-YZL-5, VF-LAM-16': ('E02 confirmed: App Q row Q.11 (noted by the authors, PRD 105 footnote 1)', None),
 'VF-LAM-13': ('E03 confirmed: App Q row Q.9', None),
 'VF-LAM-0': ('E04 confirmed: App Q row Q.10', None),
 'VF-LAM-2': ('E05 confirmed (Q3; the proviso is printed in Ch22)', None),
 'VF-LAM-6': ('E06 confirmed: author correction (`tab:appQ-errata-b`); the exact $O(\\alpha_s)$ difference is VF-LAM-19 (new)', 'App Q, Ch22'),
 'VF-YZL-3': ('E08, E09, E11 confirmed: App Q rows Q.12, Q.13, Q.15', None),
 'VF-YZL-7': ('E10 confirmed: App Q row Q.14 (the correct value appears in `Ji:2023pba` without noting the discrepancy); N29 confirmed', 'App Q, Ch23'),
 'VF-YZL-12': ('E13 confirmed: App Q row Q.16; N29 confirmed', None),
 'VF-YZL-15': ('E12 confirmed: author correction (`tab:appQ-errata-b`)', 'App Q, Ch19'),
 'VF-FRO-2': ('E15 confirmed (Q3, attributed to Collins); A08 confirmed', None),
 'VF-FRO-8': ('E16 confirmed, now by two groups (`Banfi:2025mra`, `Becher:2026kbr`)', None),
 'VF-EXC-8': ('E20 confirmed: App Q row Q.5', None),
 'VF-REF-15': ('E21 confirmed: App Q row Q.6', None),
 'VF-CONV-23, VF-SCET-16': ('E23 confirmed (also in the journal version): App Q row Q.1', None),
 'VF-SCET-9': ('E24 confirmed (Q3)', None),
 'VF-SCET-6': ('E25 confirmed: App Q row Q.3', None),
 'VF-BQ-4': ('E26 confirmed: App Q row Q.7; N22 refuted (no illustration printed)', None),
 'VF-WL-10': ('E27 confirmed: the author\'s errata list (`tab:appQ-errata-b`)', 'App Q, Ch9, App F'),
 'VF-EE-12': ('E28 confirmed as a convention remark (no App Q row)', None),
 'VF-EE-10': ('E29 confirmed: author correction (`tab:appQ-errata-b`)', 'App Q, Ch6'),
 'VF-DIS-8, VF-DIS-14': ('E32 refuted (no printed source of the variant): nothing printed', None),
 'VF-FRO-10': ('E35 confirmed (Q3); N28 confirmed', None),
 'VF-FRO-9, VF-FRO-12': ('E34: reported disagreements, no verdict (item (iii) withdrawn by its authors, `Balitsky:2009xg`); N28 confirmed', None),
 'VF-FRO-17': ('E34(iv): no verdict (2026 status `Borden:2025ehe`)', None),
}

def regen_register(t):
    lines = t.split('\n')
    h = next(i for i, l in enumerate(lines) if l.startswith('## Pending-verification register'))
    lines[h] = '## Verification register (outcomes of the verify patch v2.3)'
    k = next(i for i in range(h, len(lines)) if lines[i].startswith('| VF ID | claim | class |'))
    lines[k] = '| VF ID | claim | class | outcome (verify patch v2.3) | target |'
    j = k + 2
    seen = set()
    while j < len(lines) and lines[j].startswith('|'):
        cells = [c.strip() for c in lines[j].strip().strip('|').split('|')]
        key = cells[0]
        assert key in OUT, key
        seen.add(key)
        cells[3] = OUT[key][0]
        if OUT[key][1]:
            cells[4] = OUT[key][1]
        lines[j] = '| ' + ' | '.join(cells) + ' |'
        j += 1
    assert seen == set(OUT), set(OUT) - seen
    return '\n'.join(lines)

CHANGELOG = r'''

**2026-10-11 — revision v2.3 (spec patcher; verify patch).** All pending flags resolved: the outcome is written in the status of VF-REF-9, VF-LAM-9, VF-LAM-10, VF-LAM-11, VF-LAM-12, VF-LAM-13, VF-LAM-15, VF-LAM-17, VF-YZL-3, VF-FRO-1, VF-FRO-3, VF-FRO-15, VF-EXC-14; **VF-LAM-9 corrected** (convolution domain of the hybrid kernel, $q-\bar q$ combination; claim N09 refuted as stated), **VF-REF-12 corrected** (initial group time-reversed, mixed signs give products, continuity with a kink; claim N13), VF-REF-4 threshold $n_0>A+1$ (X3 final report); VF-FRO-8 status (E16 confirmed by two groups); **new entries VF-LAM-19** (E06 difference) **and VF-YZL-17** (E07(ii) two-loop mismatch), group index updated; the register at the end now records the outcomes. No other formula changed.'''

OPS = [
 ('rep', V(22) + '\n', FLAG_NEW + '\n'),
 ('sub', 'For every even $n_0>A+2$', 'For every even $n_0>A+1$', 'For every even $n_0>A+2$ ($A$ = polynomial growth exponent of $T_2$'),
 ('func', lambda t: _ref4_status(t)),
 ('sub', '**[PENDING-VERIFY]** for the novelty claim of `prop:dy-eikonal-twogluon`.', 'Verify patch v2.3: claim N01 confirmed, but the result is known (`Meggiolaro:1996hf` eqs. (3.23)–(3.26), (3.34), (3.36); `Giordano:2006vv` eq. (4.24)): no novelty marker.', '**[PENDING-VERIFY]** for the novelty claim'),
 ('range', 'Same-side poles: $w_{12}=\\frac{z_1}{z_1+z_2}$, $z_j=\\frac{k_{Tj}^2}{2k_j^+}$', '- **Used in:** `lem:appO-joint-localization`.', REF12_NEW + '\n' + REF12_STATUS + '\n', False),
 ('range', '$C^{\\overline{\\rm MS}}(\\xi)\\to-\\frac{3a}{2|\\xi|}$ and $C^{\\rm ratio}(\\xi)\\to\\mp\\frac{4a}{3\\xi^2}$ as $\\xi\\to\\pm\\infty$. Hence at $O(\\alpha_s)$', '- **Used in:** Ch22.', LAM9_NEW + '\n' + LAM9_STATUS + '\n', False),
 ('sub', 'The erratum claim is an App Q candidate **[PENDING-VERIFY]**.', 'Erratum confirmed: App Q row Q.8 (first corrected in print by `Chou:2022drv`).', 'The erratum claim is an App Q candidate **[PENDING-VERIFY]**.'),
 ('sub', '$\\gamma^0$ closed form: "this work", candidate 「本书新结果」 **[PENDING-VERIFY]**.', '$\\gamma^0$ closed form: our derivation; claim N07 confirmed, known in part (`Chen:2016utp` helicity analogue, `Braun:2018brg` at $O(c)$, `Bhattacharya:2019cme` for the first two moments): no novelty marker.', '$\\gamma^0$ closed form: "this work"'),
 ('sub', '"This work" (elementary), candidate 「本书新结果」 **[PENDING-VERIFY]**;', 'Our elementary reformulation; claim N08 confirmed, known in part (`Braun:2018brg` eq. (bR); both counting rules in `JiEtAl2021`): no novelty marker;', '"This work" (elementary), candidate'),
 ('sub', 'Erratum claim: App Q candidate **[PENDING-VERIFY]**.', 'Erratum confirmed: App Q row Q.9.', '- **Status:** V (LAMET s4, 20/20). The model is [P]/[C].'),
 ('sub', 'Erratum: App Q candidate **[PENDING-VERIFY]**.', 'Erratum confirmed: App Q row Q.11 (noted by the authors in PRD 105 (2022) 076014, footnote 1).', 'All-order statement [A]. Erratum: App Q candidate'),
 ('sub', 'Lemma and bound: "this work", candidates 「本书新结果」 **[PENDING-VERIFY]**;', 'Lemma and bound: claim N10 confirmed, known in substance (Paley–Wiener type; applied to quasi-PDFs also in `Monahan:2026skv`): no novelty marker;', 'Lemma and bound: "this work"'),
 ('sub', 'Errata: App Q candidates **[PENDING-VERIFY]**.', 'Errata confirmed: App Q rows Q.12 (E08), Q.13 (E09), Q.15 (E11).', 'Errata: App Q candidates **[PENDING-VERIFY]**.'),
 ('sub', '(`Gordan1873`; the identification with Collins\' geometric theorem is a "this work" remark, candidate **[PENDING-VERIFY]**)', '(`Gordan1873`; the identification with Collins\' geometric theorem: claim N02 confirmed, not found in print, elementary — a remark without novelty marker)', 'candidate **[PENDING-VERIFY]**).'),
 ('sub', '"This work" corollary, inherits the preprint status of VF-FRO-2; candidate **[PENDING-VERIFY]**.', 'Corollary (claim N03 confirmed, not new in substance: `Collins:2020euz` Thm 1 plus the Coleman–Norton closure); inherits the preprint status of VF-FRO-2.', '"This work" corollary, inherits the preprint status'),
 ('sub', 'Prop. 8.1 A ("this work" of the frontier agent; one-loop instance V in c_pdf §5.4), candidate **[PENDING-VERIFY]**. [A].', 'Prop. 8.1 A (claim N04 confirmed, with prior art `Braun:2019qtp`; one-loop instance V in c_pdf §5.4). [A].', 'Prop. 8.1 A ("this work" of the frontier agent'),
 ('sub', 'no novelty wording before the verify patch **[PENDING-VERIFY]**;', 'no novelty wording (claim N21 confirmed; the 1989 Isgur–Llewellyn Smith papers could not be checked, so the novelty of the closed forms is not asserted);', 'no novelty wording before the verify patch'),
 ('func', lambda t: _insert_before(t, '## YZL — Yizhuang Liu and collaborators', LAM19)),
 ('func', lambda t: _insert_before(t, '## FRO — other frontier results', YZL17)),
 ('sub', '- **Status:** TR (`Banfi:2025mra` read; single group).', '- **Status:** TR (`Banfi:2025mra` read); v2.3: confirmed for the $qg\\to q$ channel in SCET by `Becher:2026kbr` (two groups, different methods; claim E16).', '- **Status:** TR (`Banfi:2025mra` read; single group).'),
 ('sub', '| 19 | Ch22 (Ch23) |', '| 20 (VF-LAM-19 new in v2.3) | Ch22 (Ch23) |', '| **LAM** (new) |'),
 ('sub', '| 16 | Ch23 |', '| 17 (VF-YZL-17 new in v2.3) | Ch23 |', '| **YZL** (new) |'),
 ('func', regen_register),
 ('sub', '**The formulas themselves may be used as stated**', '(v2.3: every claim is now decided; the column "outcome" records the decision.) **The formulas themselves may be used as stated**', 'Spec v2.1: keyed to the claims register `verify/CLAIMS.md`'),
 ('rep', '**2026-10-10 (merge) — revision v2.2 (spec-v2 integrator).** "Used in" lines of VF-LAM-14, VF-LAM-15, VF-LAM-16, VF-LAM-18 and VF-YZL-5 aligned with the ownership of FINAL_OUTLINE_v2 (Ch22 owns the quasi-TMD theorem, the lattice CS kernel and TMD ratios; Ch23 owns the threshold factorization; merge decision MD9). No formula, status or check was changed.',
  '**2026-10-10 (merge) — revision v2.2 (spec-v2 integrator).** "Used in" lines of VF-LAM-14, VF-LAM-15, VF-LAM-16, VF-LAM-18 and VF-YZL-5 aligned with the ownership of FINAL_OUTLINE_v2 (Ch22 owns the quasi-TMD theorem, the lattice CS kernel and TMD ratios; Ch23 owns the threshold factorization; merge decision MD9). No formula, status or check was changed.' + CHANGELOG),
]

def _ref4_status(t):
    lines = t.split('\n')
    h = next(i for i, l in enumerate(lines) if l.startswith('### VF-REF-4'))
    k = next(i for i in range(h, h + 8) if lines[i].startswith('- **Status:** A (R5).'))
    lines[k] = '- **Status:** A (R5); v2.3: threshold $n_0>A+1$ as in `prop:dis-dispersion-np` and App M §M.8 (X3 final report).'
    return '\n'.join(lines)


LAM19 = r"""### VF-LAM-19 — 以强子动量代替部分子动量的 $O(\alpha_s)$ 差（早期匹配形式）
Replacing the parton momentum $|y|P^z$ by the hadron momentum $P^z$ in the one-loop $\overline{\rm MS}$ matching kernel changes it by
$$C\Big(\xi,\frac\mu{P^z}\Big)-C\Big(\xi,\frac\mu{|y|P^z}\Big)=-\frac{\alpha_sC_F}\pi\ln|y|\,\frac{1+\xi^2}{(1-\xi)_+}\,\theta(0<\xi<1)=-\frac{\alpha_s}\pi\ln|y|\Big[P_{qq}(\xi)-\frac32C_F\delta(1-\xi)\Big];$$
in the ratio scheme the difference is $-\frac{\alpha_s}\pi\ln|y|\,P_{qq}(\xi)$. The early range $\int_x^1$ also omits $|y|<|x|$ and $y<0$.
- **Status:** V (`verify/claims/batch_E01_s1.md` §7, `batch_E01_s2.md`; claim E06 confirmed; new in v2.3). The point is explicit in `IzubuchiEtAl2018` (text after eq. (27)); for quasi-GPDs `Ji:2015qla`.
- **Used in:** `rem:lamet-early-form`.

"""

YZL17 = r"""### VF-YZL-17 — 欧氏直角尖点与 $\gamma_{HH}$ 的两圈差
In units of $(\alpha_s/\pi)^2$: $\Gamma^{(2)}_{\rm cusp}(\frac\pi2)=C_FC_A(\frac{\pi^2}{24}-\frac{49}{36})+\frac59C_FT_Fn_f$ and $\gamma^{(2)}_{HH}=C_FC_A(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}2)+\frac59C_FT_Fn_f$, so
$$\Gamma^{(2)}_{\rm cusp}\big(\tfrac\pi2\big)-\gamma^{(2)}_{HH}=C_FC_A\Big(\frac{\zeta_3}2-\frac{\pi^2}{24}\Big)\approx0.190\,C_FC_A ;$$
at one loop both equal $-\alpha_sC_F/\pi$. The bent Euclidean soft functions (all cusps at Euclidean angle $\pi/2$) therefore give a wrong $\ln(\mu^2b^2)$ term at $O(\alpha_s^2)$.
- **Status:** V (`verify/claims/batch_E07_s1.md` §2.2, `batch_E07_s2.md`; claim E07(ii) confirmed; new in v2.3). The argument is that of `Ji:2019sxk`; the explicit value is our evaluation of the angle-dependent two-loop cusp anomalous dimension (`KorchemskyRadyushkin1987`).
- **Used in:** `thm:yzliu-soft-hqet` (status paragraph).

"""

def _insert_before(t, heading, block):
    lines = t.split('\n')
    i = next(k for k, l in enumerate(lines) if l.startswith(heading))
    # insert before the separator line preceding the heading, if any
    j = i
    while j > 0 and lines[j - 1].strip() in ('', '---------------------------------------------------------------------------------------------------'):
        j -= 1
    lines[j:j] = [''] + block.rstrip('\n').split('\n')
    return '\n'.join(lines)
