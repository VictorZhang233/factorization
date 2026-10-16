"""Audit fixes v2.3.1 on top of spec v2.3 (auditor of the verify patch, 2026-10-11).

Usage:  python3 -I apply_audit_v231.py SPECDIR
Every edit is an exact-match replacement that must match exactly once (it aborts otherwise),
so the script can be re-run only on the v2.3 files (backup: verify/audit_v231_backup/).
The findings behind each edit are listed in spec_v2/AUDIT_v2_patch.md (sections 3-4).
"""
import sys, os

SP = sys.argv[1]
EDITS = []          # (file, old, new)
APPEND = []         # (file, text) appended at the end of the file (CHANGELOG entries)


def E(fn, old, new):
    EDITS.append((fn, old, new))


FO = 'FINAL_OUTLINE_v2.md'
WS = 'WRITER_SPEC_v2.md'
VF = 'VERIFIED_FORMULAS_v2.md'
RN = 'REFS_NOTES_v2.md'

# ---------------------------------------------------------------- FINAL_OUTLINE_v2.md
# A1 header: companion-file revisions
E(FO, "writers use only this file, `WRITER_SPEC_v2.md` (revision v2.2), `ASSUMPTIONS.md` (revision v2.2), ",
      "writers use only this file, `WRITER_SPEC_v2.md` (revision v2.3.1), `ASSUMPTIONS.md` (revision v2.3), ")
# A2 §0.10: reason of the N13 refutation; N12 item letter
E(FO, "N13 refuted as a novelty claim (the lemma is kept, corrected and sharpened)",
      "N13 refuted as stated (the ordering-weight formula holds only when all $k_j^+>0$; the time-reversed form for $k_j^+<0$ and the product form for mixed signs, which differs from the 0/1 rule for $N\\ge3$, are the corrections now in `lem:appO-joint-localization`; the lemma is kept as a sharpened result, never marked new)")
E(FO, "| sharpened results (never marked new) | Ch5/Ch9 pointers to `prop:appN-triangle-exact`(c) |",
      "| sharpened results (never marked new) | Ch5/Ch9 pointers to `prop:appN-triangle-exact`(d) |")
# A3 Ch19: correct reason of the E22 refutation
E(FO, "(claim E22 refuted: the omission was acknowledged by its author, who confirmed the vanishing at one loop; nothing is printed about it)",
      "(claim E22 refuted as phrased: the criticized NLO calculation — Hoodbhoy–Lu, unpublished — concerned $\\gamma_L^*N\\to V_TN$, not $\\gamma_T^*\\to V_T$, and its author later redid it with the collinear subtractions and found zero; nothing is printed about it)")
# A4 Ch21: N12 item letter
E(FO, "exponents from the general method can be far from sharp (`prop:appN-triangle-exact`(c), claim N12 confirmed;",
      "exponents from the general method can be far from sharp (`prop:appN-triangle-exact`(d), claim N12 confirmed;")
# A5 Ch22 quasi-TMD (C): A04 item (ii)
E(FO, "factorized expression with a \"nonperturbative lattice related factor\" that cancels in ratios; one loop. **(D)**",
      "factorized expression with a \"nonperturbative lattice related factor\" that cancels in ratios; an SCET$_{\\rm II}$ derivation with a one-loop check (A04 item (ii)). **(D)**")
# A6 Ch22 prop:lamet-gluon-singlet: refuted N09 conclusion removed
E(FO, "mixing arises only in the matching; for Regge-like singlet distributions only ratio/hybrid-type schemes give convergent momentum-space convolutions (`prop:lamet-tails`).",
      "mixing arises only in the matching; small-$y$ convergence of the momentum-space convolutions: `prop:lamet-tails`(iii) for the quark kernels ($\\overline{\\rm MS}$ and hybrid need the same small-$y$ condition, the ratio scheme only $\\int|yf|<\\infty$, and for physical quark distributions the $O(1)$ terms combine into $q-\\bar q$), while the gluon and mixing kernels are not covered — never write that only ratio/hybrid-type schemes converge for Regge-like singlet distributions (claim N09 refuted as stated).")
# A7 Ch22 rem:lamet-open (9): A06 item (3)
E(FO, "(9) higher orders: N³LO non-singlet kernel, NNLO singlet/gluon kernels, NNLO momentum-space quasi-GPD kernels, three-loop heavy–light kernel;",
      "(9) higher orders: NNLO singlet/gluon kernels, NNLO momentum-space quasi-GPD kernels, three-loop heavy–light kernel (the N³LO non-singlet kernel exists, `Cheng:2024wyu`, `prop:lamet-twoloop`; A06 item (3));")
# A8 Part VII: the sub-item label "Pending" now holds outcomes
E(FO, "  - *Pending.* The printed forms of `Ji:2020brr`", "  - *Verification outcome.* The printed forms of `Ji:2020brr`")
E(FO, "  - *Pending.* `Braun:2018brg` eq. (cR)", "  - *Verification outcome.* `Braun:2018brg` eq. (cR)")
E(FO, "  - *Pending.* The printed exponent", "  - *Verification outcome.* The printed exponent")
E(FO, "*Pending:* the factor $\\frac12$ is prese", "*Verification outcome:* the factor $\\frac12$ is prese")
# A9 Ch23: A03 item I.5 is confirmed
E(FO, "phrase as \"the first lattice extraction of $S_I$\" only after the verify check, A03; the first lattice CS-kernel extraction is `Shanahan:2020zxr`)",
      "\"the first lattice calculation of $S_I$\" only as LPC's own claim, with 「据我们所知」 (A03 confirmed, item I.5); the first lattice CS-kernel determination is `Shanahan:2020zxr`)")
# A10 Ch24 prop:front-nlo-bk: E34 item (iii) withdrawn by its authors -> not printed as a disagreement
E(FO, "its forward linearization agrees with NLO BFKL up to a term $\\propto\\alpha_s^2\\zeta(3)\\times$(the original dipole), attributed by the authors to different longitudinal cutoffs (`Balitsky:2007feb`, abstract, §VIII checked; quark part and running coupling `Balitsky:2006wa`, `Kovchegov:2006vj`);",
      "its forward linearization agrees with the NLO BFKL kernel (`Balitsky:2007feb`; the $\\alpha_s^2\\zeta(3)\\times$(dipole) mismatch reported in its §VIII was traced by the same authors to an erroneous evaluation of an integral assumed to vanish and disappears after correction, `Balitsky:2009xg` §6, \"In QCD\"; quark part and running coupling `Balitsky:2006wa`, `Kovchegov:2006vj`);")
E(FO, "*Status and gap.* [A] within the eikonal framework; the $\\zeta(3)$ difference is reported as the paper states it, together with its later withdrawal by the authors (`Balitsky:2009xg` §6, \"In QCD\") (E34, Q3).",
      "*Status and gap.* [A] within the eikonal framework; no disagreement with NLO BFKL is printed: the $\\zeta(3)$ term of `Balitsky:2007feb` §VIII was withdrawn by its authors (`Balitsky:2009xg` §6, \"In QCD\"; claim E34 item (iii), refuted as a disagreement, Q3) — never attribute it to longitudinal cutoffs.")
# A11 Ch24 prop:front-glauber-bfkl: A11 item (3)
E(FO, "RS contain no $e^+e^-$-specific Glauber statement;",
      "for $e^+e^-$ RS treat the $n$–$\\bar n$ production current at one and two loops (Glauber phases explicit in SCET$_{\\rm II}$, equal to the soft zero-bin, or carried by ultrasoft graphs in SCET$_{\\rm I}$) and expect the same at any order without proof (A11 item (3), corrected);")
# A12 F5 annex: N02 outcome
E(FO, "`rem:front-gordan-collins` (N02 pending)", "`rem:front-gordan-collins` (N02 confirmed; no novelty marker)")
# A13 Ch25 OP-B1: no verification bookkeeping in printed text
E(FO, "the $\\Gamma$-identification of `prop:appN-triangle-cs`(c) awaits a second confirmation);",
      "the integrated form `prop:appN-triangle-cs`(c) is stated as an implication from the fibered–covariant identification of $\\Gamma$);")
# A14 §00.4 X2a row
E(FO, "part (c) an implication pending the second confirmation of the $\\Gamma$-identification);",
      "part (b) the identification of the four Collins terms; part (c) stated as an implication whose premise, the fibered–covariant identification of $\\Gamma$ (X2 Prop B.3, flagged new-final there), has one independent confirmation — the final review, `verify/extend/X2-subtraction/review_final_scripts/chk_B3.log` — not the two of the PASS rule);")
# A15 App O lem:appO-glauber-operator(e): pointer to the strict-window item of the joint-localization lemma
E(FO, "the strict-window weights of `lem:appO-joint-localization`(c), pointer)",
      "the strict-window weights of `lem:appO-joint-localization`(e), pointer)")
# A16 App N: lem:appN-identification remark
E(FO, "for the triangle and the one-rung ladder (FI) is proven directly (`prop:appN-triangle-cs`, `prop:appN-phi36-dis`), so the lemma is a general tool only.",
      "(FI) is proven directly for the four Collins terms of the triangle (`prop:appN-triangle-cs`(b); for $\\Gamma$ of the triangle it is the premise of `prop:appN-triangle-cs`(c)) and for the one-rung ladder (`prop:appN-phi36-dis`(c)), so the lemma is a general tool only.")
# A17 App N prop:appN-triangle-exact: the printed status sentence must not carry verification bookkeeping
E(FO, "**Status sentence (print verbatim in substance):** 「在 $k^-$ 留数表示中，(CS1)–(CS3) 对本例已完整验证（\\cref{prop:appN-triangle-cs}）；四个减除项的纤维化值与协变值精确相同，$\\Gamma$ 的相应等同已有证明、尚待第二次独立确认」;",
      "**Status sentence (print verbatim in substance):** 「在 $k^-$ 留数表示中，(CS1)–(CS3) 对本例已完整验证（\\cref{prop:appN-triangle-cs}）；四个减除项的纤维化值与协变值精确相同」 (the corresponding identity for $\\Gamma$ is the premise of `prop:appN-triangle-cs`(c) and is not asserted in print; X2 §11 gives the sentence to use once it is accepted; verification bookkeeping is never printed, WRITER_SPEC_v2 §6.12);")
# A18 App N prop:appN-triangle-cs: (b) restricted to what is confirmed; Gamma identification only as the premise of (c)
E(FO, "(b) *(identification)* the fibered values of the four Collins terms equal their covariant (whole-integrand parametric) values — the closed forms of `prop:appN-triangle-exact`(b) — for $0<\\varepsilon<1$, with no convention for scaleless integrals; the fibered value of $\\Gamma$ equals $I_\\Gamma=\\Gamma(1+\\varepsilon)\\int_{\\rm simplex}F^{-1-\\varepsilon}$, $F=x_gm^2(x_1+x_2)+x_1x_2Q^2$, for $\\varepsilon\\in(-1,1)$ (main part ↔ $\\{x_1>\\tau x_2\\}$, sliver ↔ $\\{x_1<\\tau x_2\\}$, $\\tau=m^2/\\tilde Q^2$). (c) *(integrated statement)* if the identification of (b) for $\\Gamma$ holds — it is proved in the X2 report by explicit changes of variables and checked symbolically and numerically to $10^{-17}$–$10^{-28}$, but still awaits a second independent confirmation —, then ",
      "(b) *(identification of the Collins terms)* the fibered values of the four Collins terms equal their covariant (whole-integrand parametric) values — the closed forms of `prop:appN-triangle-exact`(b) — for $0<\\varepsilon<1$, with no convention for scaleless integrals. (c) *(integrated statement; an implication)* if the fibered value of $\\Gamma$ equals its covariant value $I_\\Gamma=\\Gamma(1+\\varepsilon)\\int_{\\rm simplex}F^{-1-\\varepsilon}$, $F=x_gm^2(x_1+x_2)+x_1x_2Q^2$, for $\\varepsilon\\in(-1,1)$ (main part ↔ $\\{x_1>\\tau x_2\\}$, sliver ↔ $\\{x_1<\\tau x_2\\}$, $\\tau=m^2/\\tilde Q^2$), then ")
E(FO, "(b) by explicit $\\kappa$- and $x$-integrals (Beta functions) and the whole-integrand Feynman/Cheng–Wu representation, and for $\\Gamma$ by maps onto the two simplex sub-regions;",
      "(b) by explicit $\\kappa$- and $x$-integrals (Beta functions) and the whole-integrand Feynman/Cheng–Wu representation; (c) from (a) and `thm:appN-fibered-subtraction`(iii) given its premise (spec note, not printed: the premise is X2 Prop B.3 — the main part and the sliver mapped onto the two simplex sub-regions, checked symbolically and numerically to $10^{-17}$–$10^{-28}$ (`r3_FI_exact.py`) and independently by the final review (`review_final_scripts/chk_B3.log`, $10^{-25}$); it becomes part of (b), and (c) unconditional with the status sentence of X2 §11, once a second independent confirmation is recorded or the lead author accepts the final review as sufficient; until then the book may quote the numerical agreement as evidence, [P]);")
E(FO, "(confirmed by independent reviews); the closed forms of the $C_R$ are the known region values",
      "(confirmed by independent reviews: `verify/extend_reports/X2-subtraction-rev2-2.md`, `-rev3-1.md`, `-rev3-2.md`, archive re-verified by the final review, `verify/extend/X2-subtraction/review_final_scripts/rerun_r3_archive_verify_triangle.log`; literature check: X2 final report §12 and the queries of `-rev3-2.md`); the closed forms of the $C_R$ are the known region values")
# A19 tab:appN-status row
E(FO, "integrated form conditional on the second confirmation of the $\\Gamma$ identification);",
      "integrated form stated as an implication from the $\\Gamma$ identification);")
# A20 App Q: note numbering and version statements (inclusion rule 4)
E(FO, "(note Q.3) | `batch_E13_s1.md`", "(note Q.4) | `batch_E13_s1.md`")
E(FO, "Q.3 — $F(k)=\\int\\frac{d^2l}{(l^2+m_g^2)(", "Q.4 — $F(k)=\\int\\frac{d^2l}{(l^2+m_g^2)(")
E(FO, "| Q.3 | E25 | `BauerPirjolStewart2002`, sentence after eq. (24) |",
      "| Q.3 | E25 | `BauerPirjolStewart2002`, sentence after eq. (24) (arXiv:hep-ph/0109045 v1 = v2 = journal version) |")
E(FO, "| Q.6 | E21 | `Mankiewicz:1999tt`, text after eq. (10) |",
      "| Q.6 | E21 | `Mankiewicz:1999tt`, text after eq. (10) (arXiv:hep-ph/9905287v1; the journal text was not accessible) |")
E(FO, "| Q.7 | E26 | `BenekeEtAl2001` after eq. (71); `BenekeNeubert2003` after eq. (63) |",
      "| Q.7 | E26 | `BenekeEtAl2001` after eq. (71) (hep-ph/0104110v1); `BenekeNeubert2003` after eq. (63) (hep-ph/0308039v2); journal typesetting not seen |")
E(FO, "| Q.10 | E04 | `IzubuchiEtAl2018` eqs. (2), (5) |",
      "| Q.10 | E04 | `IzubuchiEtAl2018` eqs. (2), (5) (journal = arXiv numbering) |")
E(FO, "| Q.15 | E11 | `Liu:2022nnk` eq. (81); `JiEtAl2021` eq. (208) |",
      "| Q.15 | E11 | `Liu:2022nnk` eq. (81); `JiEtAl2021` eq. (208) (arXiv:2004.03543v2 numbering) |")

APPEND.append((FO, """
**2026-10-11 — v2.3.1: audit of the verify patch (auditor; `AUDIT_v2_patch.md`).** Script `verify/audit_v231_scripts/apply_audit_v231.py` (exact-match edits on the v2.3 files; backup `verify/audit_v231_backup/`).
1. Refuted claims no longer printed: `prop:lamet-gluon-singlet` (N09: "only ratio/hybrid schemes converge for Regge-like singlet distributions" removed); `rem:lamet-open`(9) (A06 item (3): the N³LO non-singlet kernel exists); `prop:front-nlo-bk` (E34 item (iii): the $\\zeta(3)$ mismatch withdrawn by its authors is not printed as a disagreement, and the "longitudinal cutoffs" attribution is removed); `prop:front-glauber-bfkl` (A11 item (3): RS do treat the $n$–$\\bar n$ current); the Ch22 quasi-TMD paragraph (A04 item (ii)).
2. Consistency of the X2a delivery: `prop:appN-triangle-cs`(b) asserts only the identification of the four Collins terms; the identification of $\\Gamma$ (X2 Prop B.3; one independent confirmation) appears only as the premise of the implication (c); the printed status sentence of `prop:appN-triangle-exact`, `tab:appN-status`, Ch25 OP-B1, §00.4 and the note on `lem:appN-identification` adjusted; record paths of the two confirmations and of the literature check added to the novelty note of (a).
3. Corrected internal references and reasons: `lem:appO-glauber-operator`(e) → `lem:appO-joint-localization`(e); `prop:appN-triangle-exact`(d) for N12 (§0.10, Ch21); reasons of the E22 and N13 refutations (Ch19, §0.10); N02 and A03 item I.5 outcomes (F5 annex, Ch23); Part VII sub-items "Pending" renamed "Verification outcome"; header revisions of the companion files.
4. App Q: note of row Q.4 (E18) renumbered (was "Q.3"); versions stated for rows Q.3, Q.6, Q.7, Q.10, Q.15 (inclusion rule 4).
5. Checks re-run: `checks/check_final_outline_v2.py` E1–E14, W1–W2 OK; `checks/keys_check.py`, `checks/figures_check.py` PASS.
"""))

# ---------------------------------------------------------------- WRITER_SPEC_v2.md
E(WS, "**N13 refuted as a novelty claim** (the lemma `lem:appO-joint-localization` is kept, corrected and sharpened)",
      "**N13 refuted as stated** (the ordering-weight formula holds only when all $k_j^+>0$; the time-reversed form for $k_j^+<0$ and the product form for mixed signs are the corrections in `lem:appO-joint-localization`, which is kept as a sharpened result, never marked new)")
E(WS, "N12 `prop:appN-triangle-exact`(c) (no logarithm at NLP;", "N12 `prop:appN-triangle-exact`(d) (no logarithm at NLP;")
E(WS, "A K1 or K2 statement printed before the patch follows §6.12 (comment with the claim ID, no marker).",
      "The pre-patch protocol of §6.12 (comment with the claim ID, no marker) is retired: write the final statements.")
E(WS, "the \"correct version\" column of refdoc §2 is binding unless VERIFIED_FORMULAS_v2 says otherwise.",
      "the \"correct version\" column of refdoc §2 is binding unless VERIFIED_FORMULAS_v2 says otherwise **or the verification refuted or superseded it** (v2.3.1; `verify/CLAIM_VERDICTS.md`): **ERR-M15** — refuted (claim R-M15): the proposed formula is identical to the printed one by the linearity of $\\ln\\tilde S$; the identity to use is $\\tilde f_A\\tilde f_B=\\tilde f^{\\rm unsub}_A(y_{P_A}-y_B)\\,\\tilde f^{\\rm unsub}_B(y_A-y_{P_B})/\\tilde S(y_A,y_B)$ (Collins 2011 eq. (13.106); `lem:tmd-sqrt-identity`); **ERR-M20** — refuted as worded (claim R-M20): never call the two-loop phase-cancellation statement \"wrong\"; it holds for unpolarized pure-QCD cross sections (FSS, one step unproven) and fails beyond pure QCD (REFS_NOTES_v2 §1.5, row A20); **ERR-S3** — the weight formula of its correct-version column holds only when all $k_j^+>0$ (time-reversed for $k_j^+<0$, products for mixed signs; `lem:appO-joint-localization`, VF-REF-12; claim N13); **ERR-M26** — the route \"via uniqueness\" is circular (`rem:appM-remainder-reduction`).")
E(WS, "for the printed kernel of `Ji:2020brr` — false (App Q row Q.8); cite `Chou:2022drv` for the correction.\n",
      "for the printed kernel of `Ji:2020brr` — false (App Q row Q.8); cite `Chou:2022drv` for the correction.\n"
      "- 「NLO BK 方程的前向线性化与 NLO BFKL 相差一个 $\\alpha_s^2\\zeta(3)$ 项」 — withdrawn by its authors (`Balitsky:2009xg` §6, \"In QCD\"; claim E34 item (iii)); never print it as a disagreement or attribute it to longitudinal cutoffs (v2.3.1).\n"
      "- 「对 Regge 型海夸克分布，只有比值／混合方案的准 PDF 卷积收敛」 — false (claim N09): $\\overline{\\rm MS}$ and hybrid need the same small-$y$ condition, and for physical quark distributions the $O(1)$ terms combine into $q-\\bar q$ (`prop:lamet-tails`(iii)); gluon kernels are not covered (v2.3.1).\n"
      "- 「Collins–Diehl 批评的 NLO 计算是关于 $\\gamma_T^*\\to V_T$ 的」 — it concerned $\\gamma_L^*\\to V_T$ (claim E22); nothing is printed about that calculation (v2.3.1).\n"
      "- A \"commonly quoted variant\" of $C^{q,(1)}_{2,n}$ — none was found in print (claim E32); print only the correct form with its sources (v2.3.1).\n")
E(WS, "If a later verification changes an item, the spec is patched again; writers never anticipate it.\n",
      "If a later verification changes an item, the spec is patched again; writers never anticipate it.\n\n"
      "**Verification bookkeeping is never printed** (v2.3.1): claim IDs (E/N/A/R-…), words such as 「已确认／被否定／未解决」 or \"second (independent) confirmation\", stage records and `verify/` paths stay in `%` comments and in the final report (§13). Exceptions: the 核实 column of `tab:appQ-errata` (App Q prints the record paths by design, §6.13) and the novelty wording of §6.5 item 3. Where an entry of FINAL_OUTLINE_v2 states that a premise \"has one independent confirmation\" or similar, the book prints the mathematics (an implication, or the evidence marked [P]) and not the bookkeeping.\n")

APPEND.append((WS, """
**2026-10-11 — spec v2.3.1 (audit of the verify patch; `AUDIT_v2_patch.md`).**
1. §6.5: reason of the N13 refutation corrected (the formula, not only the novelty, was wrong for $k_j^+<0$ and for mixed signs); K3 row: N12 is `prop:appN-triangle-exact`(d); the pre-patch sentence retired.
2. §6.9: four traps added (E34 item (iii); N09; E22; E32).
3. §6.10: the refdoc §2 "correct version" column is overridden where the verification refuted or superseded it (ERR-M15, ERR-M20, ERR-S3, ERR-M26).
4. §6.12: verification bookkeeping is never printed (exceptions: App Q's 核实 column, the novelty wording of §6.5).
"""))

# ---------------------------------------------------------------- VERIFIED_FORMULAS_v2.md
E(VF, "A commonly quoted variant with $\\frac2{N+1}+\\frac1{N^2}$ **fails** the Adler check (critic c2).",
      "A variant with $\\frac2{N+1}+\\frac1{N^2}$ would fail the Adler check (critic c2), but no printed source of it exists (claim E32 refuted): never mention a \"variant\"; the correct form and its Adler check are already in `BardeenEtAl1978` eqs. (3.9), (4.10).")
E(VF, "(claim N13 refuted as stated: only the same-side lower-half-plane formula had been given)",
      "(claim N13 refuted as stated: the lower-half-plane formula had been asserted for poles on either side, and the 0/1 rule for all $N$; for $k_j^+<0$ the order is time-reversed, and for mixed signs with $N\\ge3$ the weights are products)")
APPEND.append((VF, """
**2026-10-11 — revision v2.3.1 (audit of the verify patch; `AUDIT_v2_patch.md`).** VF-DIS-8: the "commonly quoted variant" sentence removed (claim E32 refuted: no printed source); VF-REF-12: the reason of the N13 refutation stated precisely. No formula changed.
"""))

# ---------------------------------------------------------------- REFS_NOTES_v2.md
E(RN, "\"first lattice extraction of $S_I$\" only after verification.",
      "\"the first lattice calculation of $S_I$\" only as LPC's own claim, with 「据我们所知」 (A03 confirmed, item I.5).")
APPEND.append((RN, """
**2026-10-11 — revision v2.3.1 (audit of the verify patch).** Row A03 (I.5): the LPC priority sentence finalized (A03 confirmed). No key changed.
"""))


def main():
    texts = {}
    for fn, old, new in EDITS:
        if fn not in texts:
            texts[fn] = open(os.path.join(SP, fn), encoding='utf-8').read()
        n = texts[fn].count(old)
        if n != 1:
            raise SystemExit('ABORT: %s: %d matches for %r' % (fn, n, old[:90]))
        texts[fn] = texts[fn].replace(old, new)
    for fn, add in APPEND:
        if fn not in texts:
            texts[fn] = open(os.path.join(SP, fn), encoding='utf-8').read()
        texts[fn] = texts[fn].rstrip('\n') + '\n' + add
    for fn, t in texts.items():
        open(os.path.join(SP, fn), 'w', encoding='utf-8').write(t)
        print('written', fn)
    print('%d edits, %d appended entries' % (len(EDITS), len(APPEND)))


if __name__ == '__main__':
    main()
