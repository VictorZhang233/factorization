# W12-write

(structured result persisted from wf_3924630b-621)

## summary

I finished Ch10 (W12) from the previous session's partial draft. The chapter compiles cleanly and passes check_unit_v2.py, apart from items justified below as pointers or by the label scheme. It runs about 18.4 pp against a 13-pp budget (+41%), which is over the +20% allowed by LA-8; whether to accept that is your decision.

What changed this session:
- **Broken dependency lists fixed.** `\uses{a, b}` passes its argument to `\cref`, which does not strip spaces. Every label after ", " therefore printed as "??", which affected 56 labels in 17 lists, including 10 of this chapter's own. Other units may have the same problem.
- **Physics re-checked.** All six earlier scripts were re-run and pass. I added one new check (w12_nlo_polcheck.py): in the quark channel, the physical polarization sum gives the same result as −g. The text claimed this before, but no script backed it.
- **Literature claims checked against the papers.** These are now verified: VVM eqs. (4.1)–(4.4) and (B.3)–(B.4), MVV eq. (3), FONLL eqs. (49)–(53), both CSS 1989 quotations (§8.7, §10.1), and every Collins 2011 location, using the book's table of contents.
- **Text fixes.**
  - The FONLL agreement is now claimed for F_2 only; F_L is our own derivation.
  - I dropped a claim attributed to Guo:1997it, which no source note supports.
  - The LQS number is now stated exactly as their abstract gives it.
  - I added the Lam–Tung half of misconception M26, with two INSPIRE-verified references.
- **Spec compliance.** Four status paragraphs were missing a literature location or an upgrade path; one lemma was missing its partonic-state line. All five are fixed.
- **Layout.** I fixed three displays whose equation numbers were pushed to their own line, and tightened some prose where it did not lose content.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch10_disall.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch10_disall.bib-additions
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/parts/p0_intro.tex … p10_summary.tex (11 parts; concatenated by tools/build.sh)
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/tools/build.sh
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/tools/fix_spaces.py
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/tools/grade_check.py
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_nlo.py
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_nlo_polcheck.py
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_breit.py
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_scale.py
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_ladder_routes.py
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_heavy.py
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/w12_heavy_conv.py
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/dtrace.py
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W12/logs/ (w12_*.log, all PASS)
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W12/test_disall.tex
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W12/test_disall.pdf
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W12/check_final.log

## pages

Chapter body on pp. 1–19 of the standalone PDF, about 18.4 pp of text; p. 19 holds only the closing correspondence table, set as a float page. Bibliography on pp. 20–22; PDF total 22 pp. Budget is 13 pp: +41%, above LA-8's +20% cap.

## compile_status

xelatex + bibtex + xelatex ×2, run in writing/test/W12/. Results: 0 errors; no overfull box at all; 0 undefined citations; 0 multiply defined labels; 0 missing characters; 0 BibTeX warnings. 77 references are undefined, and all of them are labels owned by other units, as expected in a standalone build. The test copy of refs_merged_v2.bib is the spec file plus chapters/ch10_disall.bib-additions.

## checker_output

python3 -I check_unit_v2.py ch10_disall.tex Ch10 FINAL_OUTLINE_v2.md
C1 canonical labels of this unit missing: OK
C1b canonical fig/tab labels of this unit missing: OK
C2 labels defined here but owned by another unit: OK
C3 external refs not canonical: ['ch:break','ch:dis','ch:dy','ch:ir','ch:method','ch:pdf','ch:smallx','ch:thr']. These are chapter labels in the binding ch:<key> scheme (WRITER_SPEC §1.2, §5.1); the registry simply lists no chapter labels.
C4 \uses problems: OK
C5 cref/uses mismatches, all pointers:
 - prop:disall-two-routes → rem:dis-nonuniform: a pointer to a similar counterexample.
 - prop:disall-regions → asm:intro-bridge: a pointer saying what the hadron-level version needs.
 - cor:disall-consistency → prop:disall-two-routes, thm:disall-factorization: pointers. Listing them in \uses would break qualifier compatibility for an R_OPE statement, and the outline's \uses list leaves them out.
 - prop:disall-nlo → ex:disall-nlo, ex:disall-gluon: the examples show the intermediate algebra of proof steps (3)–(6), and they \uses the proposition, as the outline designs it.
 - thm:disall-heavy → ex:disall-heavy-lo: an illustration.
C6 tag/qualifier problems: OK
C7 statements without \uses: OK
C8a planning markers: OK
C8b: 「软因子等于 1」 appears only after 「对共线单举截面」, which is the qualified form the spec allows.

## report_markdown

## W12 report — Ch10 `disall` (WRITER_SPEC_v2 §13)

### 1. File
- **File:** `chapters/ch10_disall.tex`, 97 287 bytes. It is assembled from `writing/work/W12/parts/p0…p10` by `writing/work/W12/tools/build.sh`, and is identical to the tested copy.
- **Length:** the chapter body is pp. 1–19 of the standalone PDF, about **18.4 pp** of text; p. 19 holds only `tab:disall-correspondence` as a float page. Budget is 13 pp, so this is **+41%**, beyond LA-8's +20% (see item 14).
- **Compile** (xelatex + bibtex + xelatex ×2): 0 errors; 0 overfull boxes; 0 undefined citations; 0 multiply defined labels; 0 missing characters; BibTeX 0 warnings. 77 references are undefined; all are external labels.

### 2. Canonical labels
- **All implemented:** `ch:disall`, 9 `sec:disall-*`, all 20 statements, `tab:disall-correspondence`, and `fig:disall-seed`, `fig:disall-ladder-regions`, `fig:disall-heavy`.
- **check_unit_v2.py:** C1, C1b, C2, C4, C6, C7 and C8a are OK. C3 lists only `ch:*` chapter labels, which follow the binding scheme but are not in the registry. C5 items are all pointers (item 7). C8b is a qualified phrase.

### 3. Additional labels
- `sec:disall-summary`: the closing section 「本章小结：对应表与常见误解」, which holds the correspondence table and the misconception box.
- 20 equation labels: `eq:disall-breit`, `-proj`, `-proj-massive`, `-current-virtuality`, `-unphysical-offshell`, `-cauchy`, `-factorized`, `-chain`, `-renorm-start`, `-ladder`, `-main`, `-norm`, `-C`, `-Rq`, `-Rq-exp`, `-scale`, `-dis-scheme`, `-P1`, `-heavy`, `-heavy-lo`.
- No auxiliary lemmas and no extra examples.

### 4. External labels (all canonical)
- **Assumptions:** asm:appN-brst-nonlocal, -collins, -contour, -cutsum, -envelope, -ir-regulator, -multren, -separation, -uv, -ward-product; asm:appO-lcopt; asm:intro-bridge; asm:intro-np-ope.
- **Chapters:** ch:break, dis, dy, ir, method, pdf, smallx, thr.
- **Ch7:** def:dis-compton, def:dis-kinematics, ex:dis-oneloop-ope, prop:dis-c-oneloop, prop:dis-compton-analytic, prop:dis-dispersion, prop:dis-wilson-partons, rem:dis-nonuniform, thm:dis-moments, thm:dis-ope.
- **Ch9:** cor:method-removing-eps; def:method-collinear-approx, -collins-conditions, -power-suppressed, -subtraction; lem:method-local-accuracy, -meets, -no-pole, -soft-unitarity, -ward-multi; prop:method-chains, -collinear-wilson, -fsi, -product, -ward-tree; thm:method-subtraction, thm:method-template.
- **Ch8:** def:pdf-gluon, def:pdf-quark, prop:pdf-partonic-dr, rem:pdf-schemes, thm:pdf-dglap, thm:pdf-dis-xspace, thm:pdf-moments-local, thm:pdf-support-pt.
- **Ch2–Ch5:** def:prelim-msbar, prop:prelim-beta, rem:qcd-decoupling, lem:prelim-mellin, lem:prelim-plus-expansion, prop:sudakov-oneloop, thm:ir-leading-regions.
- **Ch1:** def:intro-error-types.
- **Appendices:** cor:appK-pdf, lem:appC-phase-space, lem:appN-algebra, lem:appN-error-table, prop:appF-induction, prop:appN-ladder, prop:appN-phi36-dis, sec:appN-examples, sec:appN-processes, thm:appN-structure, thm:appN-subtraction.
- **Figures:** fig:dis-oneloop, fig:reduced-dis.

### 5. Tags (all as in the outline; nothing weakened or strengthened)
- **Definition (no tag):** def:disall-breit.
- **[R, R_cond]:**
  - prop:disall-two-routes: premises asm:appN-collins (uniform on the complex disc), -contour, -envelope, -separation, -cutsum (for (c)).
  - prop:disall-factorized-subtraction: premises asm:appN-ward-product, -uv, plus prop:disall-regions.
  - thm:disall-renorm-compat: premises asm:appN-multren (Z1)(Z3)(i), asm:appN-ir-regulator, asm:appN-contour (b), plus the premises of the two propositions above. Content grade **[C]** is stated in the theorem, and no [A] statement uses it.
- **[A]:** lem:disall-fsi, prop:disall-regions, prop:disall-h2, prop:disall-h3h4, prop:disall-h5, thm:disall-factorization, thm:disall-heavy, prop:disall-nuclear. The last is composite: item (b) is \tagP and item (e) is \tagC, each stated in words and macro.
- **[R, R_OPE]:** cor:disall-consistency, with the full first-use qualifier sentence.
- **[R, R_PT]:** prop:disall-nlo (stated at one loop), prop:disall-scale, prop:disall-dis-scheme.
- **Examples (no tag):** ex:disall-ladder, ex:disall-nlo, ex:disall-gluon, ex:disall-heavy-lo.
- **Grade propagation and qualifier compatibility** were checked with `tools/grade_check.py` against the registry tags: no conflicts.
- **Error-type comments:** `% errtype:` is recorded on all tagged statements (E-S, E-N, E-W).

### 6. Assumptions
- None defined; Ch10 owns no assumptions.
- **Used:** the list in item 4.
  - `asm:appN-brst-nonlocal` is only named, as the named gap, in the status paragraphs of prop:disall-h2, thm:disall-factorization and thm:disall-heavy. It is never in a `\uses` list.
  - `asm:appO-lcopt` appears only as a status pointer, through prop:method-fsi.
- **R_cond premise sentences:** verbatim as in the outline.
- **Non-perturbative status lines:**
  - thm:disall-factorization: \cref{asm:intro-bridge} (MA1, MA2, MA4).
  - thm:disall-heavy and prop:disall-nuclear: (MA1, MA2).
- **Partonic-state line:** present on every partonic statement. I added the missing one to lem:disall-fsi.

### 7. `\uses`
- **Pointers flagged by C5:** see checker_output.
- **No forward edges or cycles.**
- **Systemic bug fixed:** `\uses` expands to `\cref{#1}`, and cleveref does not strip spaces. Every label after ", " was therefore undefined: 56 labels in 17 lists, including 10 internal ones. All lists are now comma-only.
- **Additions to the outline's `\uses` lists** (all earlier or appendix statements, all [R], mathematics or definitions, all compatible):
  - prop:disall-two-routes: + def:method-subtraction, def:method-collinear-approx, prop:dis-compton-analytic, prop:dis-dispersion.
  - lem:disall-fsi: + prop:dis-compton-analytic.
  - cor:disall-consistency: + lem:prelim-mellin, thm:pdf-moments-local.
  - prop:disall-dis-scheme: + thm:pdf-dglap, prop:prelim-beta.
  - ex:disall-heavy-lo: + def:disall-breit, prop:disall-nlo, def:pdf-quark.
  - prop:disall-nuclear: + def:pdf-quark, def:pdf-gluon.

### 8. Formulas
- **VF entries used:** VF-DIS-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -13, -14; VF-CONV-6, -7. All have status V; no T-status formula is used.
- **Writer-derived formulas, each re-derived by script (all logs PASS, re-run this session):**
  - Exact Breit frame with the Nachtmann variable x_N, and the projector contractions (w12_breit).
  - Off-shellness bound in the unphysical region, |ξω−1| ≥ 1−|ω| (w12_breit).
  - Normalization chain ∫Tr[γ⁺J] = 2f (w12_breit).
  - Dispersion coefficients T₂ = Σ4ω^{n−1}M_n and the Cauchy estimates (derived by hand).
  - The two counterexamples (w12_ladder_routes, 500-digit check).
  - Two-rung ladder chain algebra (w12_ladder_routes).
  - Matrix elements, D-dimensional phase space, y-integrals and distribution expansion (w12_nlo), plus the new quark-channel physical-polarization check (w12_nlo_polcheck).
  - Scale dependence and the DIS-scheme P'^{(1)} (w12_scale).
  - Massive LO γ*g→QQ̄ for F₂ and F_L, the m→0 limits, and the one-loop MS-bar f_{Q/g} = (α_s/2π)P_qg ln(μ²/m²) (w12_heavy).
  - Uniform boundedness of the subtracted coefficient (w12_heavy_conv).
  - The Altarelli–Martinelli relation, re-derived from C_L.
- **Literature cross-checks, made in the full texts this session:** VVM eqs. (4.3)–(4.4) equal 2C₂^q and 4n_f C₂^g; MVV eq. (3) equals 2C_L^q and 4n_f C_L^g; FONLL eqs. (49)–(51) equal our F₂ (their a_s = α_s/2π, eq. (24)). F_L is our own derivation.

### 9. Verification items
- No 「本书新结果」 in this chapter.
- No literature errata found.
- Spec slip: VF-DIS-10 writes ∂F₂/∂ln μ_R² where the right-hand side corresponds to F₂/x. The chapter states it for F₂/x.
- BBDM eq. (3.9) is cited per the verification record (CLAIM_VERDICTS A15, E32 literature check).

### 10. Citations
- **39 keys:** AbdulKhalek:2022fyi, Aivazis:1993kh, AivazisEtAl1994, AltarelliEllisMartinelli1979, AltarelliMartinelli1978, AmatiPetronzioVeneziano1978a/b, BardeenEtAl1978, Bodwin:1988fs, BodwinBrodskyLepage1981, Buza:1996wv, Collins1998b, Collins2011, Collins:2008sg, CollinsSoperSterman1989, CollinsWilczekZee1978, CurciFurmanskiPetronzio1980, DiemozEtAl1988, Ellis:1978sf, EllisEtAl1979, EllisStirlingWebber1996 (no equation number), Eskola:2021nhw, Forte:2010ta, Frankfurt:2011cs, FurmanskiPetronzio1982, Kovarik:2015cma, Kramer:2000hn, Lam:1980uc, LibbySterman1978a, Luo:1993ui, Luo:1994np, Mirkes:1992hu, Moch:2004xu, Mueller1978, QiuSterman1991a/b, Thorne:1997ga, Vermaseren:2005qc, Zee:1974du.
- **LA-14 additions** in `chapters/ch10_disall.bib-additions`: Zee:1974du (previous session), plus **Lam:1980uc** and **Mirkes:1992hu**. Both new ones were verified on INSPIRE (texkey and DOI); the attribution follows CLAIM_VERDICTS A24(4).
- **Locations verified this session:**
  - CSS 1989 §8.7 and §10.1 quotations, in the full text (hep-ph/0409313).
  - VVM eqs. (4.1)–(4.4) and (B.3)–(B.4); their ref. [50] is BBDM.
  - MVV eq. (3); FONLL eqs. (49)–(53).
  - Collins 2011: ch. 5, §8.9, ch. 10, §11.3 and §11.9, §12.6 from the book's table of contents; §11.3.2 pp. 407–410 and §14.6 pp. 569–570 per verification record A13.
  - Abstracts of Collins1998b, Bodwin:1988fs, Luo:1993ui, Collins:2008sg and Lam:1980uc.
- **Changes made because of these checks:**
  - Removed a claim attributed to Guo:1997it (A^{1/3} vs. A^{2/3}); it is documented only at bibliography level.
  - The LQS estimate is now worded exactly as their abstract, and avoids λ, which denotes the regulator ratio in this chapter.
  - The FONLL agreement is now limited to F₂.
- No 「文献待补」, no 「位置待核实」 printed, no preprints cited, no aliases needed.

### 11. Figures
- **Copied verbatim** from `figures/figset_B.tex` (Oct 11 00:28), via the pack's figblocks; identity checked by script: `fig:disall-seed`, `fig:disall-ladder-regions`, `fig:disall-heavy`.
- **Referred to:** `fig:reduced-dis` (Ch4) and `fig:dis-oneloop` (Ch7).
- All figures were rendered at 110 dpi and look correct.
- **Issue:** the `fig:disall-seed` caption prints the internal ID "VF-WL-8". Proposed fix: delete 「VF-WL-8，」 in figset_B.tex.
- To match `fig:disall-heavy`, the heavy-quark example now names the gluon momentum k.

### 12. Boxes and tables
- The box 「本章证明了什么／没有证明什么」, with per-statement premises.
- `tab:disall-correspondence` with an error-type column. Rows: two-routes, factorized-subtraction, renorm-compat, ex:disall-ladder, plus fsi/regions and the main theorem.
- A misconception box covering M4, O7, M25 and M26, including the Lam–Tung half.
- All pages with a figure, table, box or long display were inspected at 110 dpi.

### 13. Deviations and spec errors
- **def:disall-breit:** q is written with x_N, which makes 2P·q = Q²/x exact; the outline's form with x is exact only at leading power. The text states this.
- **Extra closing section** `sec:disall-summary`.
- **Lam–Tung sentence added** for M26, which is not covered elsewhere in the outline.
- **Caveat added:** the φ³₆ ladder bounds hold only at real x ≥ x₀ > 1 (per X2 final), not with the complex-disc uniformity that two-routes (b) needs.
- **Spec errors found:**
  - VF-DIS-10 normalization (item 9).
  - The figure caption ID (item 11).
  - The register's 「§10.8–§11.3 (位置待核实)」: the table of contents shows §11.3 is "Factorization for DIS" and §11.9 is "Ward identities to convert K gluons to Wilson line", which may help the App N writer.

### 14. Open items
See the open_items field.

## open_items

1. Page budget: about 18.4 pp against 13 (+41%), over the LA-8 +20% cap. Almost all of the length is material LA-8 says not to shorten: statements, the full proofs of the seven [R] statements, \uses lists, status paragraphs, boxes, the four required examples and three required figures. The remaining options are to accept the overrun or name specific cuts, for example the numerical remarks in ex:disall-heavy-lo or the counterexample in prop:disall-two-routes(c).
2. Integrator, important: cleveref does not strip spaces, so any unit that writes \uses{a, b} or \cref{a, b} prints '??' for every label after the first in the integrated book. Ch10 had 56 such cases, now fixed. All units should be scanned and the lists normalized, for example with the regex in writing/work/W12/tools/fix_spaces.py.
3. Figure source: the fig:disall-seed caption in figures/figset_B.tex prints the internal ID 'VF-WL-8'. Proposed fix: delete 'VF-WL-8，'.
4. Spec: VF-DIS-10 should read ∂(F_2/x)/∂ln μ_R² on the left, or the right-hand side should be multiplied by x. Ch10 prints the F_2/x form.
5. Checker: check_unit_v2.py C3 flags ch:<key> labels as non-canonical because the registry lists no chapter labels. Whitelisting ch:/app: labels would remove this.
6. Typesetting: in the standalone build the chapter title wraps with an orphan '靶' on the second line. This is a preamble or integrator matter; with '第 10 章' the line break will change.
7. M26 (Lam–Tung) is addressed only here, with two new INSPIRE-verified references in chapters/ch10_disall.bib-additions. If the integrator merges .bib-additions, Lam:1980uc and Mirkes:1992hu must be included.

