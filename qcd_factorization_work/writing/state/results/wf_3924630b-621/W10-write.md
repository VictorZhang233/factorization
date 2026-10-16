# W10-write

(structured result persisted from wf_3924630b-621)

## summary

W10 resumed after the quota interruption. I audited and finished the existing drafts of Ch9 (`ch09_method.tex`) and App F (`appF_ward.tex`) against LEAD_DECISIONS, WRITER_SPEC_v2, the W10 pack/FINAL_OUTLINE_v2 and VERIFIED_FORMULAS_v2, and reconciled them with `X2-subtraction_final2.md` (which appeared after the first draft of the subtraction section). All 46 canonical statements are in outline order with the registry tags and qualifiers, and both units compile cleanly. check_unit_v2.py is clean except two items that must be justified: C3 flags only text inside the verbatim flowchart figure block, and C5 lists one set of App O/TMD assumptions that are pointers.

Physics and attribution fixes made in this session:
- **Triangle example:** it no longer implies the integrated triangle subtraction theorem unconditionally. That statement rests on X2 Prop B.3, whose second confirmation (LA-3) is not yet recorded. The example now cites only `prop:appN-triangle-cs`(a)(b) as established and states (c) as an implication.
- **Zero-bin formula:** now displayed and derived. A new sympy/mpmath check (`w10_zerobin.py`) verifies it and shows that the transverse integral needs ε>0 while the σ→0 end needs ε<0.
- **Cut-sum identity:** the text claimed exact checks up to N≤7, but the script only went to N≤5. The new `w10_cutsum_exact.py` checks N≤8 exactly at rational points, with a negative control.
- **Literature locations:** CSS 1989 §8, §8.2 eq. (131), §9.1, §9.2 and §10.1 were verified against the arXiv full text and the citations corrected (§8 → §8, 9.1; §9.2 added).
- **Attributions:** the DGOPS (Diehl et al. 2015) attribution was reworded to match its recorded content. The precise Labastida–Sterman result was added. The Ch24 pointer `prop:front-brst-bilocal` was added.
- **Error types and gaps:** error-type clauses were added to the [A] status paragraphs. The (Abs)-failure remark now matches `prop:appN-twoloop-algebra` precisely.
- **Back-references:** references to the Ch4 and Ch3 figures were added, with the conversion of their n, n̄ notation to n_A, n_B.
- **Spec alignment:** App Q row 19 is printed per LA-6. App N section numbers are now cross-references (`\cref`) instead of hard-coded numbers. The correspondence-table row for the template theorem now follows the outline.
- **Readability and layout:** undefined symbols in the error table are now defined, the triangle example is broken into paragraphs, the q q̄→gg kinematics can be reproduced, and float placement is improved.

All 12 pre-existing check scripts (11 runnable plus the Dirac helper module) were re-run and reproduce their stored logs exactly.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch09_method.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/appF_ward.tex
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p0_intro.tex
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p1_strategy.tex
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p2_regions.tex
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p3_gy.tex
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p4_ward.tex
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p5_subtraction.tex
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p6_unitarity.tex
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p7_glauber.tex
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/ch09_p8_template.tex
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/parts/appF_p0.tex
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/build_unit.py
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_zerobin.py
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_cutsum_exact.py
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_ward.py
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_glauber.py
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_gy.py
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_appF.py
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_unitarity.py
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_scale.py
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_triangle.py
23. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_poset.py
24. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_extra.py
25. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_final_checks.py
26. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/w10_dirac.py
27. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W10/logs/
28. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/test_method.tex
29. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/test_appF.tex
30. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/test_method.pdf
31. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/test_appF.pdf
32. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/checker_ch09.out
33. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W10/checker_appF.out

## pages

Ch09: 34 pp (pages 1–34 of the standalone build; bibliography starts p. 35). Budget 20 pp, LA-8 maximum 24 pp, so +70%. App F: 4 pp (bibliography p. 5). Budget 3 pp, maximum 3.6 pp, so +33%. Pages are densely filled: the largest blank run is 2–5% on most pages and 23% on the error-table float page. The length is content, not layout, and the overshoot is systematic across units (other writers' test builds: Ch4 26, Ch6 23, Ch10 22, Ch12 36, Ch22 57 total pages).

## compile_status

xelatex + bibtex + xelatex x2 (writing/test/W10). Both units: 0 errors, 0 missing glyphs, 0 undefined citations, 0 multiply-defined labels, 0 BibTeX warnings. Overfull boxes: Ch09 has one of 0.84 pt (status paragraph of thm:method-template), below the 1 pt threshold; App F has none. Undefined references are only labels of other units (372 occurrences in Ch09, 31 in App F; all canonical, listed in report item 4).

## checker_output

Ch09 (check_unit_v2.py ch09_method.tex Ch09):
- C1 OK; C1b OK; C2 OK.
- C3 not canonical: ['#1', 'app:appN', 'app:appO'], all inside the verbatim figure block fig:method-flowchart. '#1' is the parameter of the block's local `\fbref` macro. app:appN and app:appO are appendix chapter labels mandated by WRITER_SPEC §1.2 but absent from the §08 registry table. LA-10 forbids editing the block.
- C4 OK.
- C5: "thm:method-template: cref'd but not in uses: asm:appN-tmd, asm:appO-deformation, asm:appO-lcopt, asm:appO-mixing, asm:appO-rewritten-cs". Justified as pointers: the outline's binding uses list routes the App O inputs through prop:method-glauber-deformation and prop:method-fsi (master row III.9 "经 III.7、III.8"), and asm:appN-tmd belongs only to the TMD variant (Ch14).
- C6 OK; C7 OK; C8a OK; C8b OK.

AppF (check_unit_v2.py appF_ward.tex AppF): C1, C1b, C2, C3, C4, C5, C6, C7, C8a, C8b all OK.

## report_markdown

# W10 final report — Ch9 `method` and App F `appF` (WRITER_SPEC_v2 §13)

## 1. Files
- `chapters/ch09_method.tex` (177 kB): **34 pp**, i.e. pages 1–34 of `writing/test/W10/test_method.pdf`; the bibliography starts on p. 35. Budget 20 pp; LA-8 maximum 24 pp.
- `chapters/appF_ward.tex` (16 kB): **4 pp**; the bibliography starts on p. 5. Budget 3 pp; maximum 3.6 pp.
- **Compile** (xelatex + bibtex + xelatex ×2, drivers `test_method.tex` / `test_appF.tex` with `\appendix`): 0 errors, 0 missing glyphs, 0 undefined citations, 0 multiply-defined labels, 0 BibTeX warnings. Overfull boxes above 1 pt: none. The only overfull box is 0.84 pt (status paragraph of `thm:method-template`).
- **Renders:** every page of both PDFs was rendered at 110 dpi and inspected (all figures, tables, the two tcolorboxes, long displays). I fixed a 53 pt overfull line that one of my edits introduced, a half-empty page caused by the `placeins` section barrier, and a float that split a proposition from its 「依赖」 line.
- **Assembly:** units are built from `writing/work/W10/parts/*.tex` by `build_unit.py`, which substitutes the verbatim figure blocks (LA-10). The `chapters/` and `writing/test/W10/` copies are byte-identical.

## 2. Canonical labels
- All implemented, in outline reading order.
  - Ch9: 43 statements, 8 sections (`sec:method-strategy` … `sec:method-template`), 3 tables, 10 figures, `ch:method`.
  - App F: 3 statements (`ex:appF-telescoping`, `prop:appF-two-gluon`, `prop:appF-induction`), 4 sections, `app:appF`.
  - None missing.
- **check_unit_v2.py, Ch09:** C1/C1b/C2/C4/C6/C7/C8a/C8b OK.
  - C3 flags `#1`, `app:appN`, `app:appO`. All three are inside the verbatim block `fig:method-flowchart`: a local macro parameter, and appendix chapter labels mandated by WRITER_SPEC §1.2 that are missing from the §08 registry table.
  - C5: see item 7.
- **check_unit_v2.py, AppF:** C1–C8 all OK.

## 3. Additional labels
- **Ch9, 34 equation labels:** `eq:method-pinchset, -EN, -sigma, -NU, -PA, -Dtilde, -telescoping, -local, -gy-coll, -gy-soft, -seed, -qqgg, -ghostsum, -straight, -CR, -tri-kin, -CC2, -chains, -pairing, -product, -r-identity, -tri-CR, -CC1-res, -tri-values, -tri-sum, -zerobin (new in this session), -dis-gamma1, -C2q, -dis-CA, -soft-one, -cutsum, -glauber-oneloop, -eG, -template`.
- **App F:** `eq:appF-finite, eq:appF-telescope, eq:appF-two`, and the table `tab:appF-gy`. The table is the numerical Grammer–Yennie suppression table promised in the App F outline (VF-WL-10/11 numerics).
- No auxiliary lemmas, no extra examples.

## 4. External labels referenced (all canonical)
- **Ch9:**
  - Assumptions: asm:appN-brst-nonlocal, asm:appN-collins, asm:appN-contour, asm:appN-cutsum, asm:appN-endpoint, asm:appN-envelope, asm:appN-multren, asm:appN-separation, asm:appN-tmd, asm:appN-uv, asm:appN-values, asm:appN-ward-product, asm:appO-deformation, asm:appO-envelope, asm:appO-lcopt, asm:appO-mixing, asm:appO-rewritten-cs, asm:intro-bridge.
  - Other units' statements: conj:front-brst-multilocal, def:appN-meet-closed, def:intro-error-types, def:intro-factorization, def:ir-glauber, def:ir-pinch-surface, def:ir-scalings, def:pdf-gluon, def:pdf-quark, def:prelim-brst, def:prelim-feynman-rules, def:prelim-lightfront, def:prelim-wilson, ex:disall-ladder, ex:ir-regions-toy, ex:qcd-qqbar-gg, ex:sudakov-offshell, lem:appN-algebra, lem:appN-beta, lem:appN-error-table, lem:appO-cut-position, lem:appO-unitarity, lem:prelim-boost, lem:prelim-eikonal-identity, prop:appF-induction, prop:appF-two-gluon, prop:appN-triangle-cs, prop:appN-triangle-exact, prop:appN-twoloop-algebra, prop:appO-eikonal, prop:appO-target, prop:disall-h2, prop:disall-h3h4, prop:disall-h5, prop:disall-regions, prop:disall-two-routes, prop:dy-universality, prop:front-brst-bilocal, prop:ir-glauber-trapping, prop:ir-power-counting, prop:ir-super-leading, prop:pdf-partonic-dr, prop:pdf-pqq-operator, prop:prelim-beta, prop:prelim-wilson-covariance, prop:prelim-wilson-rules, prop:tmd-h1h5, rem:appN-abs-edge, rem:appN-fibered-allorders, rem:ir-regions-values, rem:pdf-schemes, thm:appN-structure, thm:appN-subtraction, thm:appO-main, thm:coll-sia, thm:dy-factorization, thm:ee-R-finite, thm:ir-leading-regions, thm:pdf-dglap, thm:prelim-cutting-rules, thm:prelim-slavnov-taylor.
  - Figures, sections, tables: fig:glauber-exchange (inside the verbatim caption of fig:glauber-contour), fig:momentum-regions, fig:soft-eikonal, sec:appF-gy, sec:appF-one, sec:appF-two, sec:appN-approximators, sec:appN-examples, sec:appN-setting, sec:appN-theorem, tab:appQ-errata-b.
- **App F:** asm:appN-brst-nonlocal, asm:appN-ward-product, def:method-collinear-approx, def:prelim-brst, def:prelim-feynman-rules, def:prelim-wilson, lem:method-gy, prop:appB-rules, prop:front-brst-bilocal, prop:method-collinear-wilson, prop:method-gy-suppression, prop:method-ward-one, prop:method-ward-tree, rem:appJ-nonlocal, rem:method-pure-gauge, tab:appQ-errata-b, thm:prelim-slavnov-taylor.
- `tab:appQ-errata-b` is defined by the App Q outline entry (§Q.2, class-Q2 table) but is absent from the §08 registry table.
- Chapter pointers are printed as 「第~N~章」 (the form used in WRITER_SPEC §4.5 item 4), because `ch:` labels are not in the registry.

## 5. Tags (final; each checked programmatically against the registry: all equal, none weakened)
- **[R, R_PT]:** lem:method-i0-compat, lem:method-ward-elementary, lem:method-ward-abelian, prop:method-ward-one, prop:method-ward-tree, ex:method-naive-induction (one-loop; qualifier first, then 「（单圈。）」), prop:method-glauber-oneloop, prop:method-scale-scheme, prop:appF-two-gluon (tree level).
- **[R, R_def]:** lem:method-soft-unitarity.
- **[R, R_cond]:** lem:method-local-accuracy; cor:method-removing-eps.
- **[A]:** lem:method-collinear-accuracy, lem:method-soft-accuracy, prop:method-gy-suppression, lem:method-ward-multi, prop:method-collinear-wilson, prop:method-soft-wilson, thm:method-subtraction, prop:method-fsi, prop:method-glauber-deformation, thm:method-template, prop:appF-induction.
- **Mathematics (no tag):** lem:method-meets, lem:method-covering, lem:method-telescoping, lem:method-gy, prop:method-chains, lem:method-pairing, prop:method-product, lem:method-no-pole.
- **No tag:** all definitions, remarks and the other examples.
- No grade-propagation conflict found. Each [A] statement carries a 「地位与缺口」 paragraph that names its `asm:` bottleneck, error type, a literature location of the gap, and the upgrade path.
- Error-type comments (`% errtype:`) are recorded on the accuracy lemmas, local accuracy, removing ε, the subtraction theorem, the FSI, Glauber and template statements, and G-suppression.

## 6. Assumptions
- None defined (neither unit owns an `asm:`).
- **R_cond premise sentences:**
  - lem:method-local-accuracy: 「前提：asm:appN-envelope、asm:appN-separation。」
  - cor:method-removing-eps: 「前提：asm:appN-contour(b)（及 thm:appN-subtraction 的前提）。」
- **Non-perturbative status line:** thm:method-template has 「非微扰地位：asm:intro-bridge（MA1、MA2、MA4）。」. Every other statement carries the partonic, operator or Feynman-integral remark.
- **Named gap** asm:appN-brst-nonlocal ([C]; MD1/LA-1): named, and never placed in a uses list, in lem:method-ward-multi, thm:method-template, prop:method-collinear-wilson (inherited), prop:appF-induction, tab:method-hypotheses and tab:method-correspondence.

## 7. Uses
- **C5 (Ch9):** thm:method-template mentions asm:appN-tmd, asm:appO-deformation, asm:appO-lcopt, asm:appO-mixing and asm:appO-rewritten-cs without listing them. These are pointers, not premises:
  - the outline's binding list routes the App O inputs through prop:method-glauber-deformation and prop:method-fsi, which list them (master row III.9: 「经 III.7、III.8」);
  - asm:appN-tmd belongs only to the TMD variant (listed by Ch14).
- **Additions to outline lists** (allowed by §4.5 item 2; definitions and appendix statements only, no grade change):
  - prop:method-ward-one + def:prelim-brst: the App F proof uses s c̄ = B and the B equation of motion.
  - ex:method-sudakov-subtraction + prop:appN-triangle-cs: its status sentence relies on it; this is consistent with the App N proof-delivery table.
- Otherwise the uses lists equal the outline's (checked by script). No forward edges (C4 OK), no cycles.

## 8. Formulas
- **VF used:** VF-WL-6, WL-7, WL-8, WL-9, WL-10, WL-11, WL-12; VF-REF-2, REF-3, REF-7, REF-18; VF-DIS-3, DIS-4, DIS-6; VF-PDF-5; VF-GLA-4. No T-status formula is used.
- **Writer-derived and checked** (scripts and logs in `writing/work/W10/`; all re-run in this session and identical to the stored logs):
  - (W1)–(W5) proofs, the fermion-line insertion identity, γ*→qq̄g, DIS seed, exact two-K-gluon identity, q q̄→g*g* identity, ghost sum, CKR cross section (4.3949316148 at E=1.3, θ=0.83; ghost fraction 3.97%): `w10_ward.py`, 38 PASS.
  - Grammer–Yennie algebra, H·k=0 form, soft G_s formula, suppression numerics: `w10_gy.py`, 13 PASS.
  - VF-WL-12 residues, e_G identity, i0-compatibility imaginary parts, one- vs two-component deformation numbers (0.008/0.0008/0.00008; 0.25), soft-approximation contour numbers (0.958 / 0.036), VF-GLA-4: `w10_glauber.py`, 19 PASS.
  - Triangle closed forms, remainder decompositions, VF-REF-18, pinch/scaling statements of ex:method-naive-induction, fibered vs closed-form values, pole cancellation, NLP remainder −4: `w10_triangle.py`, 42 PASS.
  - Poset, meets, Hasse diagram, β_R, chains, pairing, product formula and the (Abs)-breaking control: `w10_poset.py`, 21 PASS.
  - k⁻ residue of C_{C1}Γ, q q̄→gg t+u vs s channels, C_2^q bookkeeping, row-5 bound: `w10_extra.py`, 12 PASS.
  - Cut-position identity: `w10_unitarity.py`, 16 PASS; **new** `w10_cutsum_exact.py`, exact rational checks for N≤8, 8 PASS plus a negative control.
  - **New** `w10_zerobin.py`, the zero-bin formula eq:method-zerobin, 9 PASS. It also shows that the transverse integral requires ε>0, and the text now says so.
  - Finite Wilson-line telescoping and operator-vertex Ward identity: `w10_appF.py`, 14 PASS.
  - Scale/scheme relations and two-loop logarithms: `w10_scale.py`, 5 PASS.
  - Longitudinal propagator and projector checks: `w10_final_checks.py`, all PASS.

## 9. Verification items
- No 「本书新结果」 is printed in these units; the only marker is App N's own `prop:appN-triangle-cs`(a).
- **LA-3 / X2 final2:** X2 Prop B.3 (fibered = covariant value of Γ for the triangle) has one confirmation. No X2 confirmation-stage record exists in `verify/` (only `verify/extend/X3-ope/confirm2/`). Ch9 therefore prints:
  - the fibered (CS1)–(CS3) and the identification of the four Collins terms as established (`prop:appN-triangle-cs`(a)(b));
  - the integrated triangle subtraction theorem only as the implication (c).
- No new literature errata noticed.

## 10. Citations
- **Ch9 keys:** Collins2011, CollinsSoperSterman1989, LibbySterman1978a, Labastida:1984gy, CollinsSoperSterman1988, CollinsSoper1982a, AybatSterman2009, Zimmermann1969, SenIndumathiChoudhury2019, Ma2020, GrammerYennie1973, FeigeSchwartz2014, Diehl:2015bca, CombridgeKripfganzRanft1977, Collins:2008sg, Braun:2019qtp.
- **App F keys:** Collins2011, Weinberg1965, SenIndumathiChoudhury2019, GrammerYennie1973, CollinsSoperSterman1989, Collins:2008sg, Braun:2019qtp.
- No aliases needed, no 「文献待补」, no `.bib-additions`.
- **Preprint marked:** SenIndumathiChoudhury2019 (cited only next to GrammerYennie1973, per A18 / REFS_NOTES).
- **Locations verified in this session** against the arXiv full text hep-ph/0409313 (LA-7):
  - CSS 1989 §8 (gauge invariance, Ward identities), §8.2 eq. (131), §9.1 (longitudinal collinear gluons; corrections power suppressed), §9.2 (soft approximation and eikonal lines), §10.1 (quoted sentence).
  - The earlier unsupported 「第~8~节」 for the G-part suppression became 「第~8、9.1~节」.
- **Collins 2011 locations:** §11.3.2 pp. 407–410 and p. 410, §14.4, §14.4.8, §5.5.6, §10.6, §11.9.3, eqs. (11.4)–(11.6) p. 402 are confirmed by A13/A18. §10.3, §10.6.6, §10.8 and §11.9 p. 416 Fig. 11.6 are taken from the outline (Ch5/App N entries).
- **Attribution traps respected:** Grammer–Yennie per A18 (the symmetrized b_k is a later modification). Aybat–Sterman described as an outline (A23). DGOPS (Diehl:2015bca) described as clarifying the single-DY issues and extending the cancellation to double DY at all orders.

## 11. Figures
- **Owned (10), copied verbatim** from `writing/packs/W10/figblocks.tex` (built 2026-10-11 13:00). The blocks are byte-identical to the current sources:
  - `research/tikz2/figures2.tex` (2026-10-10 13:00): fig:ward-identity, fig:glauber-contour;
  - `figures/figset_B.tex` (2026-10-11 00:28): fig:method-flowchart, -nesting, -hasse, -neighbourhoods, -kg, -sudakov-plane, -coeff-minus-coll, -glauber-direction.
- All are rendered, inspected and referenced in the text.
- **Back-references added:** fig:momentum-regions (Ch4) and fig:soft-eikonal (Ch3), with the n, n̄ → n_A, n_B conversion. The mandated M31 sentence is printed at the first reference to fig:glauber-contour.
- **Figure issues for the lead (LA-10; blocks not edited):**
  1. fig:method-coeff-minus-coll caption prints 「（VF-DIS-6、VF-PDF-3）」. These are internal IDs, and the partonic-PDF entry is VF-PDF-5. Fix: delete the parenthetical.
  2. fig:method-glauber-direction caption prints 「VF-REF-7；」. Fix: delete it.
  3. The fig:method-flowchart block defines a local `\fbref` macro inside the figure group (allowed; reported) and cites `app:appN` / `app:appO` (flagged by C3).
  4. The fig:glauber-contour caption (a), 「…变形到 |k⁻|∼|k_T|，在那里软近似成立」, holds only for the jet that sees k⁻. Suggested caption addition at the next figure revision: 「（只对 J_A；离开 Glauber 区须沿 e_G 同时形变两个分量，见 fig:method-glauber-direction）」.

## 12. Boxes and tables
- **Box** 「本章证明了什么／没有证明什么」: present, with the outline's box labels and tags.
- **Misconception box:** M15, M24, M25, M31, M35; C2, C7, C14; O10, O13.
- **tab:method-errors:** 9 rows, with columns for bound type and inputs. The paragraph and caption now define h, n_A(y_A) and y_k.
- **tab:method-hypotheses:** now placed directly after the template theorem.
- **tab:method-correspondence:** contains the outline's rows plus a row for lem:method-ward-multi. The template-theorem row now names thm:appN-subtraction and the register, together with the assembled thm:appN-structure (content [C] through the named gap). The table has a column for error types.
- **App F:** tab:appF-gy.

## 13. Deviations and spec errors
- **Length:** over budget (item 1); not cut, per LA-8 ("completeness wins"; statements, proofs, uses lists, boxes never shortened).
- **Uses additions:** two (item 7).
- **ex:method-sudakov-subtraction status sentence** refined beyond the outline's wording to separate (a)(b) (established) from (c) (implication), as required by X2 final2 and LA-3.
- **App F Grammer–Yennie history** follows the verified A18 wording. The pack and outline text 「original GY K-photon is symmetric (b_k k_μk_ν)」 conflicts with A18 (the symmetrized b_k is a later modification).
- **Errata reference:** E27 is printed as 「附录~Q 第~19~条」 together with the reference to tab:appQ-errata-b (LA-6).
- **Spec issues found:**
  - VF IDs printed in two figure captions;
  - the registry table lacks tab:appQ-errata-b and all `ch:`/`app:` labels, so check_unit_v2.py C3 flags `\cref{app:…}`, which WRITER_SPEC §4.10 item 2 explicitly allows.

## 14. Open items for the lead author
1. **Page budgets:** Ch9 34 pp (budget 20, maximum 24); App F 4 pp (budget 3). Writers overshoot systematically (other builds: Ch4 26, Ch6 23, Ch10 22, Ch12 36, Ch22 57 pp including bibliography). A book-wide decision is needed.
2. **LA-3:** run or record the X2 confirmation of Prop B.3. If it passes, the triangle example's status sentence can state the integrated subtraction theorem as unconditional (`prop:appN-triangle-cs`(c)).
3. **Figure fixes:** apply the caption fixes of item 11 at the next figure synchronization.
4. **Checker/registry:** register tab:appQ-errata-b and the chapter labels, or teach check_unit_v2.py about them, so that C3 is clean.
5. **Cross-unit consistency** (Ch9 ↔ App N/O/F review):
   - App N must keep sec:appN-setting/-theorem/-approximators/-examples and the (a)/(b)/(c) structure of prop:appN-triangle-cs;
   - App O must keep prop:appO-eikonal, prop:appO-target, thm:appO-main, lem:appO-cut-position and lem:appO-unitarity;
   - Ch24 must own prop:front-brst-bilocal.

## open_items

1. Page budgets: Ch9 is 34 pp (budget 20, LA-8 maximum 24); App F is 4 pp (budget 3). The overshoot is systematic across writers and needs a book-wide decision.
2. LA-3: X2 Prop B.3 (fibered = covariant value of Γ, triangle) still has only one confirmation, and no X2 confirmation-stage record exists in verify/. If it passes, Ch9's triangle-example status sentence can state the integrated subtraction theorem prop:appN-triangle-cs(c) as unconditional.
3. Figure caption fixes (LA-10; writers do not edit blocks): delete '（VF-DIS-6、VF-PDF-3）' from the fig:method-coeff-minus-coll caption and 'VF-REF-7；' from the fig:method-glauber-direction caption. Optional: add the M31 clarification to the fig:glauber-contour caption (a).
4. Registry/checker: tab:appQ-errata-b (defined in App Q §Q.2) and the ch:/app: chapter labels are missing from the §08 registry table, so check_unit_v2.py C3 flags them, although WRITER_SPEC §4.10 explicitly allows \cref{app:…}.
5. Spec wording conflict: the pack/outline App F text calls the original Grammer–Yennie K-photon 'symmetric (b_k k_μ k_ν)', contradicting the verified A18 printable version. The text follows A18.
6. Cross-unit consistency: App N (W11) must keep sec:appN-setting/-theorem/-approximators/-examples and the (a)/(b)/(c) structure of prop:appN-triangle-cs; App O (W15) must keep prop:appO-eikonal, prop:appO-target, thm:appO-main, lem:appO-cut-position and lem:appO-unitarity; Ch24 must own prop:front-brst-bilocal.

