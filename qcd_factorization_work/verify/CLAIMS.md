# Claims register: errata, new results, reference-document corrections, attributions

Compiled 2026-10-10 by the claims-collector task of the workflow. Each claim has an id, its kind, a precise statement, the literature involved, the source file(s) in our material, and a recipe for verification. Duplicates across files are merged into one claim (merge map in §7). The structured output of the task lists the same claims under the same ids, with condensed statements; this file holds the full statements, literature and verification recipes.

## 1. Scope and method

Sources scanned completely:
- `frontier/lamet/LAMET.md`
- `frontier/yzliu/YZLIU.md`
- `frontier/others/OTHERS.md`
- `refdoc/REFDOC_ANALYSIS.md (§0, §1.9, §2 incl. §2.4-2.5, §3, synthesizer checks; S30, S37, S57-S60 of §5)`
- `research/{c_pdf,c_dis,c_dy,c_ee,c_regions,c_wilson,c_tmd,c_glauber,c_exclusive,c_scet}/DERIVATION.md`
- `research/critic/REVIEW.md`
- `research/survey/SURVEY.md`
- `spec/FINAL_OUTLINE.md (also keyword search: 新结果, new result, erratum, misprint, typo, spurious, credit, 首创)`
- `spec/VERIFIED_FORMULAS.md (also keyword search for erratum/misprint/spurious flags)`

Bibliographic data were taken from the project bib files (`spec/refs_merged.bib`, `frontier/*/*.bib`, `research/survey/survey_refs.bib`; keys as printed). Data marked 'recalled' or 'verify' were not checked against INSPIRE in our material. Grades [R]/[A]/[P]/[C]/[V] are those of CONTEXT.md.

Counts: errata in published papers and textbooks: 36, new results claimed in our material: 29, corrections of the reference document: 44, delicate attribution claims: 28; total 137.

Notes binding on anyone who prints these claims:
- The reference document `factorization_qcd-2.pdf` is not citable (REFDOC S62). The R-claims state what our monograph prints in its own words, with primary literature.
- Two R-claims (R-OUR1, R-OUR2) are corrections of OUR spec found by the reference readers, not errors of the reference. They are kept so that the printed physics statements get verified.
- E19 is a withdrawn claim and must not be printed.
- The Chinese name of Yizhuang Liu is UNVERIFIED (YZLIU §1.1). The two renderings appear in A02 only to flag the conflict between our files. Neither may be printed until verified. No personal identifiers from the habilitation summary are reproduced here.
- Only one statement in the material carries the marker 「本书新结果（待文献核查）」: N01. It requires a literature check before the marker is printed (REFDOC S59). FINAL_OUTLINE itself contains no such marker, and its master-table rule says 'No new results'.

## 2. Index

| id | kind | claim | source |
|---|---|---|---|
| E01 | erratum | Hybrid-scheme kernel: δ-term prescription violates ∫C = 1 | frontier/lamet/LAMET.md §0.3 item 1, §3.7 Prop. 3.4, §13 item 12, §14 item 1 |
| E02 | erratum | Quasi-TMD factorization: Collins–Soper exponent needs a factor ½ | frontier/lamet/LAMET.md §0.3 item 2, §10.2 'Correction', §14 item 2 |
| E03 | erratum | BVZ 2019 eq. (cR): missing q(x)ln(1−x) | frontier/lamet/LAMET.md §0.3 item 3, §5.3, §14 item 3 |
| E04 | erratum | IJJSZ 2018: inconsistent sign of g between the two links | frontier/lamet/LAMET.md §0.3 item 4, §1.1 table |
| E05 | erratum | JZZ 2018: same-dimension lattice mixing not mentioned | frontier/lamet/LAMET.md §0.3 item 5, §3.5 |
| E06 | erratum | Ji 2013 matching form superseded (hadron vs parton momentum) | frontier/lamet/LAMET.md §0.3 item 6, §2.1, §4.1 Thm 4.2 |
| E07 | erratum | LaMET literature errors reported by others | frontier/lamet/LAMET.md §5.1 (end), §10.4(c), §11 (after table), §4.6(e) |
| E08 | erratum | Γ_S^(2) sign (APPB eq. (81); PRD 105 eq. (72)) | frontier/yzliu/YZLIU.md §3.A5(e), §4.1 E2 |
| E09 | erratum | RMP eqs. (205)-(206): sign of the S_r RGE | frontier/yzliu/YZLIU.md §2 table (row 'constant of the large-angle cusp AD'), §4.1 E2' |
| E10 | erratum | PLB 811 eq. (26): γ_C^(2) incorrect | frontier/yzliu/YZLIU.md §3.B2, §4.1 E3 |
| E11 | erratum | Two-loop L_b² coefficient of ln S_I a factor 2 too large | frontier/yzliu/YZLIU.md §3.A5(f), §4.1 E4 |
| E12 | erratum | Guo–Ji–Liu 2021: spurious ½ in the gluon GPD | frontier/yzliu/YZLIU.md §3.F1, §4.1 E5 |
| E13 | erratum | APPB App. F: 'edge of the wedge' should be BHW | frontier/yzliu/YZLIU.md §3.A3 'Proof architecture', §4.1 E6 |
| E14 | erratum | Coleman–Norton 1965: proof gap (momentum vs parameter pinch) | frontier/others/OTHERS.md §1.4, §1.7 |
| E15 | erratum | ELOP §2.1 and textbook Landau-analysis errors | frontier/others/OTHERS.md §1.2, §1.4, §1.7 rows 4 and 8, §14.1 row 4 |
| E16 | erratum | One-jettiness has coherence-violating logs (contra Alioli et al.) | frontier/others/OTHERS.md §4.6, §4.7, §14.1 row 19 |
| E17 | erratum | Aybat–Rogers 2011 eq. (3): spurious factor 2 in ζ | research/c_tmd/DERIVATION.md §1 item 4, §7 row 1, §8 item 3 |
| E18 | erratum | Collins arXiv:0708.4410 eq. (10): spurious numerator factor | research/c_glauber/DERIVATION.md §2.4 'Remark (typo in the source)', §5 row 14, §6 item 3(c) |
| E19 | erratum | WITHDRAWN: Collins-2011 sign-misprint claim (do not print) | research/c_glauber/DERIVATION.md §0.3 |
| E20 | erratum | Ji PRL 1997 eq. (15): wrong iε in the second denominator | research/c_exclusive/DERIVATION.md §0 row 8, §7, §10 item 4 |
| E21 | erratum | Mankiewicz–Piller 2000: '9/τ' inconsistent with their eq. (10) | research/c_exclusive/DERIVATION.md §8, §10 item 10 |
| E22 | erratum | NLO γ*_T → V_T claim omitted collinear subtractions (Collins–Diehl) | research/c_exclusive/DERIVATION.md §8 (transverse photons) |
| E23 | erratum | Becher–Schwartz App. A: spurious C_F in Γ_1 | research/c_scet/DERIVATION.md §6 item 10 |
| E24 | erratum | Becher–Schwartz jet function: normalization implicit | research/c_scet/DERIVATION.md §3.1, §6 item 13 |
| E25 | erratum | BPS 2002: ghost term not collinear-gauge invariant | research/c_scet/DERIVATION.md §6 item 15 |
| E26 | erratum | BBNS 2001 / BN 2003: 'm_M' should read m_B | research/c_scet/DERIVATION.md §6 item 17 |
| E27 | erratum | Collins 2011 errata (Fig. 7.10, eqs. (11.4)-(11.6)); g-sign convention | research/c_wilson/DERIVATION.md §2.7, §6.2, §7, §8 items 2-3 |
| E28 | erratum | Sterman–Weinberg formula: ln 2ε vs ln ε | research/c_ee/DERIVATION.md §0 rows 4b and 4b', §8, §10 item 1 |
| E29 | erratum | GKL 1988 O(α_s³) R-ratio later corrected | research/c_ee/DERIVATION.md §6 |
| E30 | erratum | Collins 1993 T-odd argument invalid (Collins 2002) | research/survey/SURVEY.md items 11 and 30 |
| E31 | erratum | CSS 1988 errors corrected in Collins 2011 | research/survey/SURVEY.md item 8, §3.1 item 4 |
| E32 | erratum | 'Commonly quoted' C^{q,(1)}_{2,n} variant fails the Adler check | research/critic/REVIEW.md §6 (row 'One-loop coefficient moments'), §10 c2 |
| E33 | erratum | Published errata whose content was not examined | frontier/others/OTHERS.md App. A |
| E34 | erratum | NLP and small-x literature disagreements | frontier/others/OTHERS.md §5.2 (h→γγ), §6 (NLP TMD), §9.2 (NLO BK), §10 small-x helicity (lines 1176-1183), §0 item 3 |
| E35 | erratum | MS-bar positivity: CFH argument fails (CRS); Yukawa counterexample | frontier/others/OTHERS.md §7 (Props. 7.1, 7.2, table), §14.1 |
| E36 | erratum | Gaunt / RS Glauber-violation claims vs SYZ 2018 (disputed) | frontier/others/OTHERS.md §4.1(iv)-(v), §4.2(a)-(c), §4.7 |
| N01 | new_result | Two-gluon eikonal exchange: O(g⁴) unitarity and Regge phase (本书新结果) | refdoc/REFDOC_ANALYSIS.md §0 'New and sharpened results', ERR-S1, §3 E15, §5 S37, S57 (misconception M32), S59, S60 |
| N02 | new_result | Collins' Thm 3 = Gordan's alternative; min-norm margin | frontier/others/OTHERS.md §1.3, §14.2 item 1 |
| N03 | new_result | Coleman–Norton picture in momentum space incl. eikonal lines | frontier/others/OTHERS.md §1.5, §14.2 item 2 |
| N04 | new_result | Moment reduction of the bilocal BRST classification | frontier/others/OTHERS.md §8.3(b), §14.2 item 3 |
| N05 | new_result | One-loop quasi-PDF in the unphysical regions | frontier/lamet/LAMET.md §4.6, §14 item 4 |
| N06 | new_result | One-loop threshold factorization; H_thr = H_qTMD | frontier/lamet/LAMET.md §6.1, §14 item 6 |
| N07 | new_result | Exact target-mass correction for γ^0 | frontier/lamet/LAMET.md §5.1, §14 item 7 |
| N08 | new_result | Fourier lemma and endpoint dichotomy (BVZ vs RMP counting) | frontier/lamet/LAMET.md §5.2-5.3, §14 item 8 |
| N09 | new_result | Moments and convolution domain of the one-loop quasi-PDF | frontier/lamet/LAMET.md §4.6(d), §14 item 9 |
| N10 | new_result | Fourier-step theorems (strip, truncation bound, Slepian count) | frontier/lamet/LAMET.md §7.2-7.3, §14 item 10 |
| N11 | new_result | Lean-style dependency graph of the LaMET matching theorem | frontier/lamet/LAMET.md §4.5, §14 item 11 |
| N12 | new_result | Exact Collins remainder of the off-shell triangle (sharpened) | refdoc/REFDOC_ANALYSIS.md §0, §3 D24, §5 S30, ERR-m25, §2.5 item 2 |
| N13 | new_result | Joint-localization lemma with ordering weights (sharpened) | refdoc/REFDOC_ANALYSIS.md ERR-S3, §5 S59 list |
| N14 | new_result | Other 'surpass' items of the reference analysis | refdoc/REFDOC_ANALYSIS.md §3 (C9, E14 rows), §5 S59 |
| N15 | new_result | Sharpened Ex C.27 value; F3 lesson | refdoc/REFDOC_ANALYSIS.md ERR-m23, §3 C11, App M M.4 row |
| N16 | new_result | Cauchy–Schwarz proof of I_1(0)+I_2(0) < 0 | research/c_glauber/DERIVATION.md §2.4 [A4a-A4f] |
| N17 | new_result | Entanglement test C_F² + 4T_F²(N²−1)/N² | research/c_glauber/DERIVATION.md §2.5 [C6, C6b] |
| N18 | new_result | Gluonic-pole strength C_G = 1 + 2⟨T_a·T_b⟩/C_F | research/c_glauber/DERIVATION.md §2.3 |
| N19 | new_result | Further c_glauber results | research/c_glauber/DERIVATION.md §1.6, §2 (telescoping identity), §3.2-3.4 |
| N20 | new_result | Time-like vs space-like regulator lines: 2π² difference | research/c_tmd/DERIVATION.md R3′, §3.4, §6.2, §8 item 5 |
| N21 | new_result | Exact Isgur–Llewellyn Smith soft fractions | research/c_exclusive/DERIVATION.md §4.3 (lines 255-260) |
| N22 | new_result | Prescription dependence of the X_A model | research/c_scet/DERIVATION.md §5.7 |
| N23 | new_result | Own proofs of classical mathematical facts | research/c_pdf/DERIVATION.md §7 |
| N24 | new_result | R_{e⁺e⁻} finiteness route and exact cutting identity | research/c_ee/DERIVATION.md §5 |
| N25 | new_result | Abelian Glauber toy in DY; plus trap | research/c_dy/DERIVATION.md (Glauber toy, plus trap) |
| N26 | new_result | Eikonal identity exact only with the adiabatic regulator | research/c_wilson/DERIVATION.md (eikonal identity section) |
| N27 | new_result | Distributional verification of the one-loop LaMET kernels | frontier/lamet/LAMET.md §3.7, §4.6, §14 item 5 |
| N28 | new_result | OTHERS checked transcriptions | frontier/others/OTHERS.md §4.4, §5.2, §13 (LUXqed), §7, §9.1, §14.2 item 4 |
| N29 | new_result | YZLIU derived cross-checks | frontier/yzliu/YZLIU.md §3.B, §3.C, §3.D1, §5 checks |
| R-S1 | correction_of_reference_doc | Two-Glauber 'residual' is an artefact; C_A term = reggeization phase | refdoc/REFDOC_ANALYSIS.md §0 item 1, ERR-S1, §2.5 item 1, §5 S37, S57 (M32) |
| R-S2 | correction_of_reference_doc | TMD-breaking colour bookkeeping: T_a + 2T_b | refdoc/REFDOC_ANALYSIS.md ERR-S2 |
| R-S3 | correction_of_reference_doc | Ass. E.33(c1) false; ordering-weight lemma | refdoc/REFDOC_ANALYSIS.md ERR-S3 |
| R-S4 | correction_of_reference_doc | Super-leading configurations omitted | refdoc/REFDOC_ANALYSIS.md ERR-S4 |
| R-M1 | correction_of_reference_doc | 'No Euclidean pinch' false | refdoc/REFDOC_ANALYSIS.md ERR-M1 |
| R-M2 | correction_of_reference_doc | Prop 3.5: not Euclidean; π²/3 omitted | refdoc/REFDOC_ANALYSIS.md ERR-M2, §2.5 item 2 |
| R-M3 | correction_of_reference_doc | Parameter vs momentum pinch conflated | refdoc/REFDOC_ANALYSIS.md ERR-M3 |
| R-M4 | correction_of_reference_doc | Wilson-line Feynman rules (Fig 4) | refdoc/REFDOC_ANALYSIS.md ERR-M4 |
| R-M5 | correction_of_reference_doc | K-projection lacks i0 | refdoc/REFDOC_ANALYSIS.md ERR-M5 |
| R-M6 | correction_of_reference_doc | Thm 3.14 overclaimed | refdoc/REFDOC_ANALYSIS.md ERR-M6 |
| R-M7 | correction_of_reference_doc | Soft factor with a literal '⋯' | refdoc/REFDOC_ANALYSIS.md ERR-M7 |
| R-M8 | correction_of_reference_doc | Meson electroproduction: longitudinal photon only | refdoc/REFDOC_ANALYSIS.md ERR-M8 |
| R-M9 | correction_of_reference_doc | Quarkonium decay graded A* instead of [A] | refdoc/REFDOC_ANALYSIS.md ERR-M9 |
| R-M10 | correction_of_reference_doc | P^±_NS differ beyond LO | refdoc/REFDOC_ANALYSIS.md ERR-M10 |
| R-M11 | correction_of_reference_doc | Missing all-hard region in the two-rung ladder | refdoc/REFDOC_ANALYSIS.md ERR-M11 |
| R-M12 | correction_of_reference_doc | 'Combinatorics complete' overclaimed | refdoc/REFDOC_ANALYSIS.md ERR-M12 |
| R-M13 | correction_of_reference_doc | Cut sum vs 12π Im Π not shown | refdoc/REFDOC_ANALYSIS.md ERR-M13 |
| R-M14 | correction_of_reference_doc | One-loop PDF check incomplete | refdoc/REFDOC_ANALYSIS.md ERR-M14 |
| R-M15 | correction_of_reference_doc | Thm 10.3 step (iv) formula wrong | refdoc/REFDOC_ANALYSIS.md ERR-M15 |
| R-M16 | correction_of_reference_doc | W+Y 'uniformly' unqualified | refdoc/REFDOC_ANALYSIS.md ERR-M16 |
| R-M17 | correction_of_reference_doc | Transverse-photon failure misdescribed | refdoc/REFDOC_ANALYSIS.md ERR-M17 |
| R-M18 | correction_of_reference_doc | CQ/RM misreported; Collins 2007 missing | refdoc/REFDOC_ANALYSIS.md ERR-M18 |
| R-M19 | correction_of_reference_doc | NQS Wilson lines necessary at NNLO | refdoc/REFDOC_ANALYSIS.md ERR-M19 |
| R-M20 | correction_of_reference_doc | Two-loop phase-cancellation claim wrong | refdoc/REFDOC_ANALYSIS.md ERR-M20 |
| R-M21 | correction_of_reference_doc | BBNS status understated | refdoc/REFDOC_ANALYSIS.md ERR-M21 |
| R-M22 | correction_of_reference_doc | Conj 12.5 is not BBL's | refdoc/REFDOC_ANALYSIS.md ERR-M22 |
| R-M23 | correction_of_reference_doc | Gap observables: grade D → [C] | refdoc/REFDOC_ANALYSIS.md ERR-M23 |
| R-M24 | correction_of_reference_doc | Alien operators: forward on-shell caveat | refdoc/REFDOC_ANALYSIS.md ERR-M24, S58 forbidden phrase list |
| R-M25 | correction_of_reference_doc | Spectral assumption false in the chiral limit | refdoc/REFDOC_ANALYSIS.md ERR-M25 |
| R-M26 | correction_of_reference_doc | OPE literature not checked | refdoc/REFDOC_ANALYSIS.md ERR-M26 |
| R-M27 | correction_of_reference_doc | Space-like self-energies non-integrable | refdoc/REFDOC_ANALYSIS.md ERR-M27, §2.5 item 4 |
| R-M28 | correction_of_reference_doc | MS-bar is not a finite renormalization of BPHZ | refdoc/REFDOC_ANALYSIS.md ERR-M28 |
| R-M29 | correction_of_reference_doc | Glauber-specific content of inputs undercounted | refdoc/REFDOC_ANALYSIS.md ERR-M29 |
| R-M30 | correction_of_reference_doc | Gaunt cited without the SYZ rebuttal | refdoc/REFDOC_ANALYSIS.md ERR-M30, §5 S57 |
| R-M31 | correction_of_reference_doc | Rem E.54(b) ignores l_T·k_T | refdoc/REFDOC_ANALYSIS.md ERR-M31 |
| R-M32 | correction_of_reference_doc | Method is Aybat–Sterman 2009 (uncited) | refdoc/REFDOC_ANALYSIS.md ERR-M32, §5 S58 |
| R-m01 | correction_of_reference_doc | Minor corrections m1–m5 | refdoc/REFDOC_ANALYSIS.md ERR-m1 to m5 |
| R-m06 | correction_of_reference_doc | Minor corrections m6–m12 | refdoc/REFDOC_ANALYSIS.md ERR-m6 to m12 |
| R-m13 | correction_of_reference_doc | Minor corrections m13–m16 (incl. OUR-5) | refdoc/REFDOC_ANALYSIS.md ERR-m13 to m16, OUR-5 |
| R-m17 | correction_of_reference_doc | Minor corrections m17–m22 | refdoc/REFDOC_ANALYSIS.md ERR-m17 to m22 |
| R-m23 | correction_of_reference_doc | Minor corrections m23–m25 | refdoc/REFDOC_ANALYSIS.md ERR-m23 to m25 |
| R-m26 | correction_of_reference_doc | Minor corrections m26–m27 | refdoc/REFDOC_ANALYSIS.md ERR-m26, m27 |
| R-OUR1 | correction_of_reference_doc | INTERNAL: errors in our spec OUR-1–OUR-4 | refdoc/REFDOC_ANALYSIS.md §2.4 OUR-1 to OUR-4 |
| R-OUR2 | correction_of_reference_doc | INTERNAL: errors in our spec OUR-5–OUR-8 | refdoc/REFDOC_ANALYSIS.md §2.4 OUR-5 to OUR-8 |
| A01 | attribution | Author list of NPB 964 (2021) 115311 misquoted | frontier/lamet/LAMET.md line 89 (§0.3 item 1), line 101 |
| A02 | attribution | Identity of Yizhuang Liu; Chinese-name conflict | frontier/yzliu/YZLIU.md §1.1-1.3, line 857 (§6.1) |
| A03 | attribution | Liu-programme priority claims | frontier/yzliu/YZLIU.md §3 'Novelty' paragraphs (lines 186, 266, 332, 380, 442, 588), §3.D1 (line 666), §1.3 row I.5 |
| A04 | attribution | Liu-programme proof-status attributions | frontier/yzliu/YZLIU.md §3.A2(b),(c), A4 (line 296), A6 (line 380), B1 (lines 437-439), C4, D1, line 743, line 816 |
| A05 | attribution | LaMET attributions | frontier/lamet/LAMET.md §1.3 (Prop 1.4), §2.1, §3.1-3.5, §4, §6.1 (lines 940-948), §7.1, §10.2 (line 1287) |
| A06 | attribution | Literature-absence claims; unrefereed preprints | frontier/lamet/LAMET.md §4.5, §8.4, §13, §14 |
| A07 | attribution | GPDs at x = ±ξ: Braun 2024 vs Su et al. 2026 | frontier/lamet/LAMET.md §9.1 (lines 1140-1150) |
| A08 | attribution | Status of Collins 2020 (preprint only) | frontier/others/OTHERS.md §1.2, §1.7 |
| A09 | attribution | Rigour status of the OPE | frontier/others/OTHERS.md §2.1-2.7 |
| A10 | attribution | Method of regions: who proved what | frontier/others/OTHERS.md §3.1-3.6 |
| A11 | attribution | Glauber attributions (Cheng–Wu → AS09 / RS; RS scope) | research/c_glauber/DERIVATION.md §6 items 1-2 |
| A12 | attribution | Dipole formula fails at three loops | frontier/others/OTHERS.md §1.6 (line 284), §1.7 last row |
| A13 | attribution | Collins 2011: quotes, pages, conventions | research/survey/SURVEY.md §0.3, §3.1 item 9, §3.2, items 4, 8, 9, 27 |
| A14 | attribution | History of DY factorization and higher twist | research/survey/SURVEY.md items 3, 8, 9 (lines 170-176, 260-275, 313), §3.1 item 5 |
| A15 | attribution | DIS/DY attributions recalled, not checked | research/c_dis/DERIVATION.md §11-12 |
| A16 | attribution | e⁺e⁻ attributions | research/c_ee/DERIVATION.md §5-6, §12 |
| A17 | attribution | c_pdf attributions | research/c_pdf/DERIVATION.md §7, §10 |
| A18 | attribution | c_wilson attributions | research/c_wilson/DERIVATION.md §7-8 |
| A19 | attribution | TMD and Sivers attributions | research/c_tmd/DERIVATION.md R12, §6, §8 |
| A20 | attribution | Glauber/SLL literature as reported in the blueprint | research/c_glauber/DERIVATION.md §5 row 24, §6 items 1-10, §7 |
| A21 | attribution | Exclusive-process attributions | research/c_exclusive/DERIVATION.md §0, §3-4, §7, §10, references (line 488) |
| A22 | attribution | SCET/NRQCD/BBNS attributions | research/c_scet/DERIVATION.md §6 items 7-9, 11, 12, 16 |
| A23 | attribution | REVIEW §11 'verify' list | research/critic/REVIEW.md §11 |
| A24 | attribution | Misconception-box attributions | research/critic/REVIEW.md §7 (misconceptions 8, 11-13, 26 |
| A25 | attribution | Quarkonium, EW and DPS attributions | frontier/others/OTHERS.md §0 item 3, §6, §12, §13.2-13.3 (lines 1318-1350, 1405-1420) |
| A26 | attribution | Grade conflicts between our materials | frontier/others/OTHERS.md §1.7, §2.7 |
| A27 | attribution | Experimental status (Sivers) and twist-3 evolution dispute | research/survey/SURVEY.md item 11 (lines 328-345), item 21 (lines 488-491), item 27 (line 230), §3.1 item 7 |
| A28 | attribution | NLP endpoint-factorization status attributions | frontier/others/OTHERS.md §5.1-5.5 (status table lines 871-884), lines 820-830 |

## 3. Errata in published papers and textbooks (36)

### E01 — Hybrid-scheme kernel: δ-term prescription violates ∫C = 1

- **Kind:** erratum
- **Statement:** Hybrid-scheme one-loop quasi-PDF matching kernel: printed as C_hyb = C_ratio + (3a/2)[−1/|1−ξ|_+ + 2Si((1−ξ)λ_S)/(π(1−ξ))] with 1/|u|_+ ≡ lim_{β→0+}[θ(|u|−β)/|u| + 2δ(u)lnβ] (a = α_sC_F/2π, λ_S = z_S p^z). This violates vector-current conservation: ∫dξ C_hyb = 1 + 3a ln(λ_S e^{γ_E}) (≈10% for λ_S≈1, a≈0.06). Correct (LAMET Prop 3.4): the coordinate correction (3a/2)δ(1−α)ln(z²/z_S²)θ(|z|−z_S) vanishes at z=0, so the whole bracket must be a plus distribution on ℝ: (3a/2)[−1/|1−ξ| + 2Si((1−ξ)λ_S)/(π(1−ξ))]_{+(1)} over (−∞,∞), as printed later by Su et al. 2023. Side note: LAMET.md cites the 2021 paper as 'Ji, Liu, Liu, Zhang, Zhao et al.'; the INSPIRE author list is X. Ji, Y. Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang, Y. Zhao.
- **Literature:** Ji:2020brr NPB 964 (2021) 115311, arXiv:2008.03886, eq. (hybridm2); Ji:2020ect RMP 93 (2021) 035005, arXiv:2004.03543, eq. (hybridm2); Su:2022fiu NPB 991 (2023) 116201, arXiv:2209.01236, eq. (C1 hybrid).
- **Source:** frontier/lamet/LAMET.md §0.3 item 1, §3.7 Prop. 3.4, §13 item 12, §14 item 1
- **How to verify:** Read the arXiv sources (label hybridm2) and the journal versions for the 1/|u|_+ definition. By hand: ∫_{−U}^{U}du[−θ(|u|−β)/|u| − 2δ(u)lnβ] = −2lnU and (4/π)∫_0^{Uλ_S}Si(v)/v dv = 2ln(Uλ_S) + 2γ_E, so the sum is 2ln(λ_S e^{γ_E}). Re-run frontier/lamet/scripts/s2_ft_testfunctions.py (agreement to 1e−12). Check NNLO hybrid kernels used in lattice fits for ∫C_hyb = 1.

### E02 — Quasi-TMD factorization: Collins–Soper exponent needs a factor ½

- **Kind:** erratum
- **Statement:** Quasi-TMD factorization: the Collins–Soper factor is printed as e^{K ln(ζ_z/ζ)}, and the CS-kernel ratio as (ζ_{z1}/ζ_{z2})^K, although the same papers define 2ζ∂_ζ ln f^TMD = K and P^z∂_{P^z} ln f̃ = K + G. Correct: f̃(x,b⊥,μ,ζ_z)√S_I(b⊥,μ) = H(ζ_z/μ²) exp[½K(b⊥,μ)ln(ζ_z/ζ)] f^TMD(x,b⊥,μ,ζ) + O(Λ²/ζ_z, M²/P_z², 1/(b⊥²ζ_z)). The ratio is f̃(ζ_{z1})/f̃(ζ_{z2}) = (H_1/H_2)(ζ_{z1}/ζ_{z2})^{K/2} = (H_1/H_2)(P^z_1/P^z_2)^K, the ESZ form. The same ½ applies to quasi-LFWF amplitudes: ψ̃^±√S_rN = e^{½ln((∓ζ_z−i0)/ζ)K_N} H_N^± ψ_N^±. One-loop proof (a = α_sC_F/2π): f̃^(1) = a[−½L_b² + L_b(5/2 − L_z) − 3/2 − ½L_z² + L_z]; f^TMD(1) = a[−½L_b² + (3/2 − ln(ζ/μ²))L_b + ½ − π²/12]; S_r^(1) = K^(1) = −2aL_b. The printed K leaves a residual L_b(L_z − L_ζ). Grade of the printed form: [V], typo-level.
- **Literature:** Ji:2019ewn PLB 811 (2020) 135946, arXiv:1911.03840, eq. (22) ('factorization'); Liu:2022nnk APPB 53 (2022) 4-A2, eqs. (53),(75) (eq. (52) is correct); Ji:2020ect RMP 93 (2021) 035005, eqs. (209)-(210) ('quasiTMDmatch', 'TMD-CS_kernel'); Ji:2021znw PRD 105 (2022) 076014, arXiv:2106.05310, eqs. (49),(51),(73); correct form in Ebert:2018gzl (arXiv:1811.00026) and Ebert:2022fmh (arXiv:2201.08401).
- **Source:** frontier/lamet/LAMET.md §0.3 item 2, §10.2 'Correction', §14 item 2; frontier/yzliu/YZLIU.md §3.B1, §3.B3(iii)-(iv), §4.1 E1
- **How to verify:** Re-run frontier/yzliu/scripts/check_qtmd_1loop.py and frontier/lamet/scripts/s4_tmd_bvz.py. By hand, insert the one-loop pieces into ln f̃ + ½ln S_r − ln H − c·K ln(ζ_z/ζ) − ln f^TMD: the L_b ln(ζ_z/ζ) terms cancel iff c = ½. Check the journal versions (the LaMET report notes they were not checked).

### E03 — BVZ 2019 eq. (cR): missing q(x)ln(1−x)

- **Kind:** erratum
- **Statement:** Braun–Vladimirov–Zhang (2019), eq. (cR): the printed relative power corrections R^∥_Q and R^⊥_Q omit the term q(x)ln(1−x) inside the braces. The omission is relative to their own correct integral forms (t4-Qparallel), (t4-Qperp) with the standard [0,1] plus distribution: Q^∥(x) = q(x) + (κΛ²/(x²P_z²)){∫_{|x|}^1(dy/y) y²/[1−y]_+ q(x/y) + q(x) − |x|q'(x)}. As printed, (cR) differs by ≈30% (∥) and ≈24% (⊥) at x = 0.5. The asymptotic claim R ∝ Λ²/(x²(1−x)P_z²) is unaffected.
- **Literature:** Braun:2018brg PRD 99 (2019) 014013, arXiv:1810.00048, eqs. (cR), (t4-Qparallel), (t4-Qperp) (arXiv-source labels).
- **Source:** frontier/lamet/LAMET.md §0.3 item 3, §5.3, §14 item 3
- **How to verify:** Read the arXiv:1810.00048 source. Rewrite ∫_x^1 dy/y y²/[1−y]_+ q(x/y) with the [0,1] plus prescription and identify the extra q(x)ln(1−x). Evaluate both forms for a test PDF at x = 0.5. Re-run frontier/lamet/scripts/s4_tmd_bvz.py (20/20).

### E04 — IJJSZ 2018: inconsistent sign of g between the two links

- **Kind:** erratum
- **Statement:** Izubuchi–Ji–Jin–Stewart–Zhao (2018) use P exp(−ig∫A^+) for the light-cone link and P exp(−ig∫A^z) for the space-like link. Since A^z = −A_z, these correspond to opposite covariant-derivative conventions. This is an internal sign inconsistency, harmless at the O(g²) computed. The monograph uses the CONTEXT convention throughout.
- **Literature:** Izubuchi:2018srq PRD 98 (2018) 056004, arXiv:1801.03917.
- **Source:** frontier/lamet/LAMET.md §0.3 item 4, §1.1 table
- **How to verify:** Read the Wilson-line definitions in arXiv:1801.03917. With metric (+,−,−,−), check whether a single D_μ convention reproduces both links.

### E05 — JZZ 2018: same-dimension lattice mixing not mentioned

- **Kind:** erratum
- **Statement:** Ji–Zhang–Zhao (2018) state that no lower-dimension operator can mix with the space-like Wilson-line quark bilinear. This is correct, but incomplete. For chirally non-symmetric lattice fermions, same-dimension mixing exists: O^R_Γ(z) = Z_φ² e^{−m|z|} O_{Γ'}(z), with Γ' = Γ + r sgn(z){n̸,Γ} + r² n̸Γn̸. There is none for Γ = γ^t at O(a^0). The multiplicative-renormalizability statement must carry this proviso.
- **Literature:** Ji:2017oey PRL 120 (2018) 112001, arXiv:1706.08962; Constantinou:2017sej PRD 96 (2017) 054506, arXiv:1705.11193; Green:2017xeu PRL 121 (2018) 022004, arXiv:1707.07152.
- **Source:** frontier/lamet/LAMET.md §0.3 item 5, §3.5
- **How to verify:** Compare the JZZ statement with the GJS formula for O^R_Γ and with the one-loop lattice mixing of Constantinou–Panagopoulos.

### E06 — Ji 2013 matching form superseded (hadron vs parton momentum)

- **Kind:** erratum
- **Statement:** The original LaMET matching q̃(x,μ,P^z) = ∫_x^1 (dy/y) Z(x/y, μ/P^z) q(y,μ) (Ji 2013) is superseded. The correct form is q̃(x,P^z) = ∫_{−1}^{1}(dy/|y|) C(x/y, μ/(|y|P^z)) f(y,μ), whose argument is the parton momentum |y|P^z. Using the hadron momentum P^z is wrong at O(α_s), through terms ∝ ln|y| P_qq. The early form is graded [V].
- **Literature:** Ji:2013dva PRL 110 (2013) 262002, arXiv:1305.1539; Izubuchi:2018srq arXiv:1801.03917.
- **Source:** frontier/lamet/LAMET.md §0.3 item 6, §2.1, §4.1 Thm 4.2
- **How to verify:** Substitute λ' = yλ in the coordinate-space factorization (Thm 4.2). Compare the O(α_s) kernels with argument μ/P^z and with μ/(|y|P^z): the difference is ∝ ln|y| P_qq ⊗ f.

### E07 — LaMET literature errors reported by others

- **Kind:** erratum
- **Statement:** Literature errors reported by others, in the LaMET context. (i) The earlier quasi-PDF target-mass-correction formula of Alexandrou et al. (2015) does not conserve particle number (Chen et al. 2016). (ii) The 'bent' Euclidean soft functions of Ji–Sun–Xiong–Yuan (2015) and Ebert–Stewart–Zhao (2019) reproduce the one-loop logarithms. Their anomalous dimension is, however, the cusp at Euclidean angle π/2. So the ln μ²b⊥² structure is wrong from two loops (Ji–Liu–Liu 2020; ESSZ concur). (iii) Jia et al. (2024) correct an earlier 't Hooft-model quasi-PDF expression. (iv) The transverse-cutoff one-loop matching of Xiong et al. (2014) contains a linear divergence Λ_UV/((1−y)²P^z), which spoils the 1/P_z² counting (per the RMP).
- **Literature:** Alexandrou:2015rja PRD 92 (2015) 014502, arXiv:1504.07455; Chen:2016utp NPB 911 (2016) 246, arXiv:1603.06664, App. B; Ji:2014hxa PRD 91 (2015) 074009, arXiv:1405.7640; Ebert:2019okf JHEP 09 (2019) 037, arXiv:1901.03685; Ji:2019sxk NPB 955 (2020) 115054, arXiv:1910.11415; Korchemsky:1987wg NPB 283 (1987) 342; Jia:2024atq PRD 109 (2024) 014042, arXiv:2401.12786; Xiong:2013bka PRD 90 (2014) 014051, arXiv:1310.7471.
- **Source:** frontier/lamet/LAMET.md §5.1 (end), §10.4(c), §11 (after table), §4.6(e); frontier/yzliu/YZLIU.md §3.A1 'Novelty'
- **How to verify:** (i) Compute the particle-number integral of the Alexandrou TMC formula and compare with Chen et al. App. B. (ii) Compare the two-loop cusp at Euclidean angle π/2 with the large-hyperbolic-angle constant Γ_S. (iii), (iv): read the cited passages. (iii) was read at abstract level only.

### E08 — Γ_S^(2) sign (APPB eq. (81); PRD 105 eq. (72))

- **Kind:** erratum
- **Statement:** The two-loop Γ_S^(2) is quoted with the wrong sign relative to the papers' own one-loop Γ_S^(1) = +α_sC_F/π (in those conventions Γ_S = −γ_HH). Correct: Γ_S^(2) = (α_s²/π²)C_F[C_A(49/36 − π²/12 + ζ_3/2) − (5/18)n_f] = −γ_HH^(2). Here γ_HH = −α_sC_F/π + (α_s²/π²)C_F[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f] is the constant term of the large-angle cusp anomalous dimension, normalized by Γ(θ) = (α_sC_F/π)(θ coth θ − 1) + O(α_s²). The RMP (2021) and JHEP 08 (2023) 037, eq. (A.6), are correct.
- **Literature:** Liu:2022nnk APPB 53 (2022) 4-A2, eq. (81) (no arXiv version); Ji:2021znw PRD 105 (2022) 076014, eq. (72); Ji:2023pba JHEP 08 (2023) 037, arXiv:2305.04416, eq. (A.6); Becher:2009kw PRD 79 (2009) 125004, arXiv:0904.1021; Korchemsky:1987wg.
- **Source:** frontier/yzliu/YZLIU.md §3.A5(e), §4.1 E2
- **How to verify:** Re-run frontier/yzliu/scripts/check_GammaS2.py: large-β limit of the Becher–Neubert two-loop velocity-dependent cusp, with the zero-recoil check Γ(0) = 0. Check the n_f term against the running-coupling argument (−(5/9)T_Fn_f α_s/π times one loop). Read APPB eq. (81) on the journal PDF.

### E09 — RMP eqs. (205)-(206): sign of the S_r RGE

- **Kind:** erratum
- **Statement:** RMP 93 (2021) 035005, eqs. (205)-(206), print the RGE d ln S_r/d ln μ² = +Γ_S. This contradicts the stated Γ_S^(1) = +α_sC_F/π and S_r^(1) = −(α_sC_F/π)L_b. Correct: μ² d ln S_r/dμ² = −Γ_S (= γ_HH).
- **Literature:** Ji:2020ect RMP 93 (2021) 035005, arXiv:2004.03543, eqs. (205)-(206).
- **Source:** frontier/yzliu/YZLIU.md §2 table (row 'constant of the large-angle cusp AD'), §4.1 E2'
- **How to verify:** Differentiate S_r^(1) = −(α_sC_F/π)ln(μ²b²/b_0²) with respect to ln μ², and compare with the printed equations.

### E10 — PLB 811 eq. (26): γ_C^(2) incorrect

- **Kind:** erratum
- **Statement:** PLB 811 (2020), eq. (26), gives γ_C^(2) = (1/16π²)(a_1C_FC_A + a_2C_F² + a_3C_FN_f). This is incorrect. It differs from the correct value by −2γ_HH^(2) + C_Fn_f/(24π²): the two-loop Γ_S has the wrong sign and there is an extra n_f term. The C_F² term agrees. The correct value is given in JHEP 08 (2023) 037, eq. (A.13), in the convention dα/d ln μ = −β_0α² − …, β_0 = 11C_A/(6π) − n_f/(3π): γ̃_H^(1) = −C_F/π, γ̃_H^(2) = (1188ζ_3 − 99π² − 1108)/(432π²)·C_FC_A − (36ζ_3 + 6 − 7π²)/(12π²)·C_F² + (1/24 + 10/(27π²))·C_Fn_f.
- **Literature:** Ji:2019ewn PLB 811 (2020) 135946, eq. (26); Ji:2023pba arXiv:2305.04416, eqs. (A.2)-(A.13); Liu:2023onm JHEP 02 (2024) 204, arXiv:2311.06907, eqs. (2.41)-(2.42).
- **Source:** frontier/yzliu/YZLIU.md §3.B2, §4.1 E3
- **How to verify:** Re-run frontier/yzliu/scripts/check_gammaC2.py, which derives (A.13) from (A.2)-(A.5) and (A.11). Compare the n_f parts with the large-β_0 results of Liu–Su (2.41)-(2.42). Cross-check against the 41-term NNLO threshold limit (Li:2020xml, Chen:2020ody) and delRio:2023pse.

### E11 — Two-loop L_b² coefficient of ln S_I a factor 2 too large

- **Kind:** erratum
- **Statement:** The two-loop L_b² coefficient of ln S_I (𝒟) is printed as α_s²β_0C_F/(2π), with β_0 = −(1/2π)(11C_A/3 − 4N_fT_F/3), the coefficient of dα/d ln μ. This is a factor 2 too large. Correct: α_s²β_0C_F/(4π) in that convention, i.e. ln S_I = −(α_sC_F/π)L_b + α_s²[−(C_Fβ_0/(8π²))L_b² + γ̂_HH L_b + c_2] with β_0 = 11C_A/3 − (4/3)T_Fn_f (dα_s/d ln μ² = −β_0α_s²/(4π)), with γ̂_HH = (C_F/π²)[C_A(−49/36 + π²/12 − ζ_3/2) + (5/9)T_Fn_f]. In addition, the single-log sign in APPB eq. (81) is wrong.
- **Literature:** Liu:2022nnk APPB 53 (2022) 4-A2, eq. (81); Ji:2020ect RMP, eq. (208).
- **Source:** frontier/yzliu/YZLIU.md §3.A5(f), §4.1 E4
- **How to verify:** Impose μ² d ln S_I/dμ² = γ_HH(α_s(μ)) on the one-loop term with running α_s; the L_b² coefficient must cancel the β_0 α_s² L_b term. Re-run frontier/yzliu/scripts/check_RGE_structure.py.

### E12 — Guo–Ji–Liu 2021: spurious ½ in the gluon GPD

- **Kind:** erratum
- **Statement:** Guo–Ji–Liu (2021), eq. (16), define the gluon GPD with a spurious factor ½ from a trace. This propagates to their eqs. (24)-(26). The authors corrected it in Guo–Ji–Liu–Yang (2023), eqs. (1),(5), which gives a factor 4 in |G|². Corrected definition: F_g = (1/(P̄^+)²)∫(dλ/2π)e^{iλx}⟨P'|F^{a+i}(−λn/2)F^{a+}_i(λn/2)|P⟩. Corrected amplitude: |G|² = (4/ξ⁴){(1 − t/(4M_N²))E_2² − 2E_2(H_2+E_2) + (1−ξ²)(H_2+E_2)²}.
- **Literature:** Guo:2021ibg PRD 103 (2021) 096010, arXiv:2103.11506, eqs. (16),(24)-(26); Guo:2023pqw PRD 108 (2023) 034003, arXiv:2305.06992, eqs. (1),(5).
- **Source:** frontier/yzliu/YZLIU.md §3.F1, §4.1 E5
- **How to verify:** Compare the two definitions. Check the forward-limit normalization of the 2023 definition against xg(x) and the momentum sum rule.

### E13 — APPB App. F: 'edge of the wedge' should be BHW

- **Kind:** erratum
- **Statement:** Terminology: Liu (APPB 2022), App. F, cites the 'edge of the wedge' theorem for the complex Lorentz covariance of Wightman functions in the extended tube. The result actually used is the Bargmann–Hall–Wightman theorem. Edge-of-the-wedge enters gluing/locality arguments instead (e.g. Ji–Liu–Su 2026 §5.1). Liu (JHEP 09 (2024) 030) phrases it correctly.
- **Literature:** Liu:2022nnk APPB 53 (2022) 4-A2, App. F; Streater:1989vi (PCT, Spin and Statistics, and All That); Ji:2026vir arXiv:2601.12189 §5.1; Liu:2023pjb arXiv:2312.05957.
- **Source:** frontier/yzliu/YZLIU.md §3.A3 'Proof architecture', §4.1 E6
- **How to verify:** Read APPB App. F and compare with the statements of the BHW and edge-of-the-wedge theorems in Streater–Wightman ch. 2.

### E14 — Coleman–Norton 1965: proof gap (momentum vs parameter pinch)

- **Kind:** erratum
- **Statement:** Coleman–Norton (1965) prove the classical-process interpretation in Feynman-parameter space. The proof tacitly assumes that a momentum-space pinch is equivalent to a parameter-space pinch. This fails already for the simplest massless graph: the one-loop massless self-energy at p² = 0 has a collinear momentum-space pinch without a parameter-space pinch (F = −p²α_1α_2 vanishes identically at p² = 0). With eikonal propagators the parameter integral can pinch independently of the momentum integral. For massive theories the zero-eigenvalue case remains a gap. Verdict to print: proof [V], result true ('it is not the result that breaks down, but the proof').
- **Literature:** Coleman:1965xm Nuovo Cim. 38 (1965) 438; Collins:2020euz arXiv:2007.04085, §IV and App. D.1-D.2.
- **Source:** frontier/others/OTHERS.md §1.4, §1.7; research/c_regions/DERIVATION.md §1.3 'Caveat', §1.5; research/survey/SURVEY.md item 4; refdoc/REFDOC_ANALYSIS.md ERR-M3
- **How to verify:** Read arXiv:2007.04085 §IV and App. D. Compute F for the one-loop massless bubble. Re-run research/c_regions/landau_oneloop.py (check L3f).

### E15 — ELOP §2.1 and textbook Landau-analysis errors

- **Kind:** erratum
- **Statement:** Textbook Landau analysis. (i) The Landau derivation in ELOP (1966) §2.1 is avowedly heuristic: a deformation 'along the normal' is meaningless without a metric, non-zero first-order shifts are assumed, and condition (2.1.19b) lacks the positivity λ_j ≥ 0 needed for physical-region pinches. (ii) The textbook assumption that avoiding a singularity needs a strictly positive first-order shift is false: anomalous deformations exist in ≥2 complex dimensions, e.g. for 1/(E − p²/2m + iε) [V]. (iii) 'Landau condition ⇒ singularity of I(z)' is false: the condition is only necessary; Collins App. A gives a trapped contour without a singularity [V]. The Landau condition is necessary and sufficient for a trap of the contour, which is what factorization needs.
- **Literature:** Eden:1966dnq (ELOP, CUP 1966), §2.1, eq. (2.1.19b), p. 48; Collins:2020euz App. A, App. B.1; Collins 2011 §5.4.3 (p. 110, quoting ELOP p. 48).
- **Source:** frontier/others/OTHERS.md §1.2, §1.4, §1.7 rows 4 and 8, §14.1 row 4; research/survey/SURVEY.md item 4
- **How to verify:** Read ELOP §2.1 and Collins 2020 App. A and B.1. Reproduce the anomalous-deformation example numerically.

### E16 — One-jettiness has coherence-violating logs (contra Alioli et al.)

- **Kind:** erratum
- **Statement:** Banfi–Forshaw–Holguin (2026) find coherence-violating ('super-super-leading') logarithms in one-jettiness τ_1 for colour-singlet + jet production, starting at α_s⁴ln⁶(1/τ_1) relative to Born: dσ^CVL ≃ Σ_a 𝒜_a (α_s/π)⁴(−iπ)²(1/480)ln⁶(1/τ_1), with 𝒜_q = (8/3)N_c²T_R⁴ f^q_A f^g_B σ^(0)_qg and 𝒜_g = −(32/3)N_c²T_R⁴ f^g_A f^q_B σ^(0)_gq (PDFs at μ_F = τ_1Q). They expect α_s^nL^{2n−2} terms for n ≥ 4. Hence the standard exponentiated form σ e^{−(α_s/2π)L²(2C_F+C_A)}[g_0 + α_s g_1 + …] fails. This contradicts the claim of Alioli et al. (2024) that τ_1 in V+jet is free of non-global and super-leading logarithms, a claim underlying N³LL resummation and N-jettiness slicing. Single group; graded [V] at the level of an LL-CVL computation.
- **Literature:** Banfi:2025mra PRL 136 (2026) 221901, arXiv:2511.11799, eqs. (1)-(18); Alioli:2023rxx PRD 109 (2024) 094009, arXiv:2312.06496.
- **Source:** frontier/others/OTHERS.md §4.6, §4.7, §14.1 row 19
- **How to verify:** Read both papers and check the 1/480 coefficient and 𝒜_q, 𝒜_g. Check the exact wording of Alioli et al.'s claim, and search for independent confirmation.

### E17 — Aybat–Rogers 2011 eq. (3): spurious factor 2 in ζ

- **Kind:** erratum
- **Statement:** Aybat–Rogers (2011), eq. (3), prints ζ_F = 2M_p²x²e^{2(y_P − y_s)}. Since M²e^{2y_P} = 2(P^+)², this is twice the standard ζ = M²x²e^{2(y_P − y_n)} = 2(xP^+)²e^{−2y_n}. It contradicts their own √(ζ_Fζ_D) ≈ Q², and their one-loop results (A10),(A11),(B1) agree with ours only without the factor 2. We regard the factor 2 as a misprint; do not copy eq. (3).
- **Literature:** AybatRogers2011 PRD 83 (2011) 114042, arXiv:1101.5057v2, eqs. (3),(A10),(A11),(B1); Collins–Rogers PRD 87 (2013) 034018, arXiv:1210.2100, eqs. (zeta.A),(zeta.B).
- **Source:** research/c_tmd/DERIVATION.md §1 item 4, §7 row 1, §8 item 3; spec/VERIFIED_FORMULAS.md VF-TMD-9
- **How to verify:** Read eq. (3) in the arXiv v2 source. Substitute both ζ normalizations into their (B1) γ_F and the one-loop C̃_{q/q}. Re-run research/c_tmd/scripts/one_loop_tmd.py.

### E18 — Collins arXiv:0708.4410 eq. (10): spurious numerator factor

- **Kind:** erratum
- **Statement:** Collins, arXiv:0708.4410v1 (no journal publication), eq. (10) carries an extra factor Π_j(k_T² + m_q²) in the numerator. This contradicts the first line of the same equation and eq. (11) (mass dimension M^0 vs M^{−4}), as well as the stated cancellation ∫d²k_T(I_1+I_2) = 0. Consistent form: I_1 = 𝒩F(k_T)², I_2 = −𝒩G(k_T)/(k_T² + m_q²), 𝒩 = λ²g_1²g_2(g_2+g_1)x(1−x)/(256π⁷).
- **Literature:** Collins:2007jp arXiv:0708.4410v1, eqs. (10)-(11).
- **Source:** research/c_glauber/DERIVATION.md §2.4 'Remark (typo in the source)', §5 row 14, §6 item 3(c); spec/VERIFIED_FORMULAS.md VF-GLA-8; spec/FINAL_OUTLINE.md ex:break-c07
- **How to verify:** Read arXiv:0708.4410v1 eqs. (10)-(11) and count dimensions. Re-run research/c_glauber/scripts/tmd_breaking_abelian.py (check [A4f]).

### E19 — WITHDRAWN: Collins-2011 sign-misprint claim (do not print)

- **Kind:** erratum
- **Statement:** WITHDRAWN, do not print. An earlier draft of research/c_glauber/scripts/unitarity_cuts.py claimed a sign misprint in a specific equation of Collins (2011). The claim could not be verified (the book was not accessible to that agent) and was withdrawn.
- **Literature:** Collins:2011zzd.
- **Source:** research/c_glauber/DERIVATION.md §0.3
- **How to verify:** Check that the monograph asserts no Collins-2011 sign misprint other than the author's own published errata (E28).

### E20 — Ji PRL 1997 eq. (15): wrong iε in the second denominator

- **Kind:** erratum
- **Statement:** Ji's DVCS amplitude (PRL 1997, arXiv v1 eq. (15)) prints the second denominator as x + ξ_Ji/2 + iε. The correct prescription is −iε: Feynman propagator, required by the optical theorem. Correct LO result: T^{μν} = −g⊥^{μν}Σe_q²∫dx C_V F^q + iε⊥^{μν}Σe_q²∫dx C_A F̃^q, with C_V = −[1/(x−ξ'+i0) + 1/(x+ξ'−i0)] and C_A = −[1/(x−ξ'+i0) − 1/(x+ξ'−i0)]. Here ξ_Ji = 2ξ. The published version was not checked; VGG (1999) eq. (38) has −iε.
- **Literature:** Ji1997a PRL 78 (1997) 610, arXiv:hep-ph/9603249 v1, eq. (15); Vanderhaeghen–Guichon–Guidal PRD 60 (1999) 094017, arXiv:hep-ph/9905372, eq. (38).
- **Source:** research/c_exclusive/DERIVATION.md §0 row 8, §7, §10 item 4; spec/FINAL_OUTLINE.md Ch18; spec/VERIFIED_FORMULAS.md VF-EXC-8
- **How to verify:** Read v1 eq. (15) and the published PRL. Check Im T^{11} = 2πF_1 in the DIS limit with finite iε (research/c_exclusive/scripts/s7_dvcs.py).

### E21 — Mankiewicz–Piller 2000: '9/τ' inconsistent with their eq. (10)

- **Kind:** erratum
- **Statement:** Mankiewicz–Piller (2000) state in the text that the WW twist-3 integrands behave as '12/τ and 9/τ' for τ → 0. Their eq. (10) as printed, with eqs. (3)-(5) and φ_∥ = 6ττ̄ (g^v = (3/2)(τ² + τ̄²), g^a = 6ττ̄), gives 12/τ and 6/τ; in general 8g^v(0)/τ and 4g^v(0)/τ. The paper is internally inconsistent. This does not affect the logarithmic divergence, but '9/τ' must not be quoted.
- **Literature:** Mankiewicz:1999tt PRD 61 (2000) 074013, arXiv:hep-ph/9905287, eqs. (3)-(5),(10).
- **Source:** research/c_exclusive/DERIVATION.md §8, §10 item 10; spec/FINAL_OUTLINE.md Ch18
- **How to verify:** Read eqs. (3)-(5),(10) and expand the integrands for small τ. Re-run research/c_exclusive/scripts/s8_meson.py.

### E22 — NLO γ*_T → V_T claim omitted collinear subtractions (Collins–Diehl)

- **Kind:** erratum
- **Statement:** Attributed erratum: per Collins–Diehl (2000), an NLO calculation that claimed a non-zero leading-twist transversity contribution to γ*_T → V_T omitted necessary collinear subtractions. The leading-twist amplitude vanishes to all orders by chirality and helicity conservation (Diehl–Gousset–Pire 1999; Collins–Diehl 2000).
- **Literature:** CollinsDiehl2000 PRD 61 (2000) 114015, arXiv:hep-ph/9907498 (abstract); Diehl–Gousset–Pire PRD 59 (1999) 034023.
- **Source:** research/c_exclusive/DERIVATION.md §8 (transverse photons)
- **How to verify:** Read the Collins–Diehl abstract and reference list to identify the criticized NLO paper, then check the claim.

### E23 — Becher–Schwartz App. A: spurious C_F in Γ_1

- **Kind:** erratum
- **Statement:** Becher–Schwartz (2008), arXiv source App. A, print Γ_1 = 4C_F[C_A(67/9 − π²/3) − (20/9)C_FT_Fn_f]. The C_F inside the bracket is spurious. Correct: Γ_1 = 4C_F[(67/9 − π²/3)C_A − (20/9)T_Fn_f] (Korchemsky–Radyushkin 1987), with Γ_cusp = Σ_n(α_s/4π)^{n+1}Γ_n.
- **Literature:** BecherSchwartz2008 JHEP 07 (2008) 034, arXiv:0803.0342, App. A; KorchemskyRadyushkin1987 NPB 283 (1987) 342.
- **Source:** research/c_scet/DERIVATION.md §6 item 10; spec/VERIFIED_FORMULAS.md VF-CONV-23, VF-SCET-16; spec/FINAL_OUTLINE.md def:sudakov-cusp, App B
- **How to verify:** Read arXiv:0803.0342 App. A and the journal version, and compare with the two-loop cusp of Korchemsky–Radyushkin.

### E24 — Becher–Schwartz jet function: normalization implicit

- **Kind:** erratum
- **Statement:** Becher–Schwartz (2008) define J(p²) = (1/n̄·p)(1/π)Im[i∫d⁴x e^{−ipx}⟨0|T{χ̄_n(x)(n̸̄/2)χ_n(0)}|0⟩] = δ(p²) + O(α_s) without explicit Dirac or colour normalization. Read literally (fermionic T-ordering sign, Dirac and colour traces), the free field gives −2N_c δ(p²), so a factor −(1/2N_c)tr is implicit. Use instead the explicitly normalized cut definition Σ_X(2π)^Dδ^D(p − p_X)⟨0|χ_n|X⟩⟨X|χ̄_n|0⟩ = 2π(n̸/2)n̄·p J(p²)𝟙_c.
- **Literature:** BecherSchwartz2008 arXiv:0803.0342 (jet-function definition).
- **Source:** research/c_scet/DERIVATION.md §3.1, §6 item 13
- **How to verify:** Evaluate the Becher–Schwartz formula for free fields, including the fermionic T-ordering sign and the Dirac and colour traces (the 's1' check in research/c_scet/scripts/).

### E25 — BPS 2002: ghost term not collinear-gauge invariant

- **Kind:** erratum
- **Statement:** Bauer–Pirjol–Stewart (2002) state that the first two terms of their eq. (Lcg), the field-strength and ghost terms, are invariant under collinear gauge transformations. For the ghost term this is not literally true, because the outer derivative [i𝒟_μ,·] is not collinear covariant. Correct statement: the field-strength term is invariant under collinear and usoft transformations; the gauge-fixing and ghost terms are usoft covariant and BRST invariant, which is what the decoupling proof needs.
- **Literature:** BauerPirjolStewart2002 PRD 65 (2002) 054022, arXiv:hep-ph/0109045, eq. (Lcg).
- **Source:** research/c_scet/DERIVATION.md §6 item 15; spec/FINAL_OUTLINE.md Ch14
- **How to verify:** Transform the ghost term of (Lcg) under collinear gauge transformations, and check the BRST invariance of the gauge-fixing plus ghost terms.

### E26 — BBNS 2001 / BN 2003: 'm_M' should read m_B

- **Kind:** erratum
- **Statement:** BBNS (2001) and Beneke–Neubert (2003) call 'X_H = ln(m_M/Λ_h) ≈ 2.4' the default value, next to a parametrization written with ln(m_B/Λ_h). m_M must read m_B; BBNS 2001 has ln(m_B/Λ_h) ≈ 2.4 correctly elsewhere. Also, in BN 2003's general (M_1M_2) notation V always refers to the emitted meson M_2; BBNS 2001's πK-specific labels are a special case and must not be mixed with it.
- **Literature:** BenekeEtAl2001 NPB 606 (2001) 245, arXiv:hep-ph/0104110, (XHparam); BenekeNeubert2003 NPB 675 (2003) 333, arXiv:hep-ph/0308039.
- **Source:** research/c_scet/DERIVATION.md §6 item 17; spec/VERIFIED_FORMULAS.md VF-BQ-4; spec/FINAL_OUTLINE.md Ch19
- **How to verify:** Read the X_H default-value sentences in both papers; ln(5.28/0.5) = 2.36.

### E27 — Collins 2011 errata (Fig. 7.10, eqs. (11.4)-(11.6)); g-sign convention

- **Kind:** erratum
- **Statement:** Collins, Foundations of perturbative QCD (CUP 2011): Fig. 7.10 (Wilson-line vertices in parton densities) and the Grammer–Yennie eqs. (11.4)-(11.6) on p. 402 (upper and lower indices interchanged in the printing) must be used as corrected in the author's errata ('Corrections and updates to Nov. 2013 printing'). Corrected collinear K term: K_{μν} = k_μw_{2ν}/(k·w_2 − i0) with k flowing into H, which is future-pointing for DIS, and G = g − K. Collins' coupling sign is opposite to Peskin–Schroeder: D = ∂ + igA (his eq. (2.2)), so g_Collins = −g and his Wilson lines are P exp(−ig∫n·A) (e.g. eq. (13.40)).
- **Literature:** Collins:2011zzd (OA reissue DOI 10.1017/9781009401845), Fig. 3.1, Fig. 7.10, eqs. (2.2),(11.4)-(11.6),(13.40); the author's errata list.
- **Source:** research/c_wilson/DERIVATION.md §2.7, §6.2, §7, §8 items 2-3; research/survey/SURVEY.md §0.3 item 1; spec/FINAL_OUTLINE.md sec:method-gy, App F
- **How to verify:** Obtain the official errata list and compare the printed and corrected Fig. 7.10 and eqs. (11.4)-(11.6). Confirm the sign of g from Fig. 3.1 and eq. (2.2).

### E28 — Sterman–Weinberg formula: ln 2ε vs ln ε

- **Kind:** erratum
- **Statement:** Sterman–Weinberg two-jet cross section at O(α_s): σ_2j = σ_0{1 − (C_Fα_s/π)[4 ln δ ln 2ε + 3 ln δ + π²/3 − 5/2]} for ε < δ ≪ 1, when ε is the fraction of the total c.m. energy √s (the SW definition, free cone axis). The frequently quoted form with '4 ln δ ln ε' holds only if ε is the fraction of the beam energy √s/2; otherwise it is off by 4 ln2 |ln δ|·(4/3)(α_s/π). For ε ≫ δ, recoil generates extra ln(ε/δ) terms. SW's own typography was not checked.
- **Literature:** StermanWeinberg1977 PRL 39 (1977) 1436.
- **Source:** research/c_ee/DERIVATION.md §0 rows 4b and 4b', §8, §10 item 1; spec/VERIFIED_FORMULAS.md VF-EE-12
- **How to verify:** Read the SW 1977 definition of ε and the printed bracket. Re-run research/c_ee/sw_jets.py: at (ε,δ) = (1e−6, 0.003), c_2j = −288.2811 numerically, −288.2812 with ln 2ε, −304.39 with ln ε.

### E29 — GKL 1988 O(α_s³) R-ratio later corrected

- **Kind:** erratum
- **Statement:** The original O(α_s³) e⁺e⁻ R-ratio result of Gorishny–Kataev–Larin (1988) was later corrected (GKL 1991; Surguladze–Samuel 1991 and erratum). Corrected a³ coefficient (SU(3), MS-bar, μ² = s, a = α_s/π): −6.63694 − 1.20013n_f − 0.00518n_f² − 1.2395η, with η = (Σe_q)²/(3Σe_q²) and singlet coefficient 55/72 − (5/3)ζ_3 = −1.2395. Status in the source: 'recalled; verify'.
- **Literature:** Gorishny–Kataev–Larin PLB 212 (1988) 238 and PLB 259 (1991) 144 (GorishniiKataevLarin1991); SurguladzeSamuel1991 PRL 66 (1991) 560 [Erratum ibid. 2416].
- **Source:** research/c_ee/DERIVATION.md §6
- **How to verify:** Read GKL 1991 and Surguladze–Samuel 1991 and compare the corrected numbers; cross-check with Baikov–Chetyrkin–Kühn PRL 101 (2008) 012002.

### E30 — Collins 1993 T-odd argument invalid (Collins 2002)

- **Kind:** erratum
- **Statement:** Collins (1993) argued that time-reversal invariance makes the Sivers asymmetry vanish. Collins (2002), following Brodsky–Hwang–Schmidt (2002), showed this proof is invalidated by the path-ordered Wilson line: T exchanges future- and past-pointing staples, so f_1T^⊥,SIDIS = −f_1T^⊥,DY (also for Boer–Mulders h_1^⊥).
- **Literature:** Collins:1992kk NPB 396 (1993) 161, arXiv:hep-ph/9208213; Collins:2002kn PLB 536 (2002) 43, arXiv:hep-ph/0204004; Brodsky:2002cx.
- **Source:** research/survey/SURVEY.md items 11 and 30; research/critic/REVIEW.md §7 misconception 12; research/c_tmd/DERIVATION.md §6.2
- **How to verify:** Read the abstract and text of Collins 2002 and the 1993 argument. Reproduce the PT mapping of the staples (research/c_tmd/scripts/sivers_symmetry.py).

### E31 — CSS 1988 errors corrected in Collins 2011

- **Kind:** erratum
- **Statement:** Collins (2011) §14.4, p. 553: 'I will follow the proof given by Collins, Soper, and Sterman (1988), but with some important improvements and with correction of errors. That reference supersedes earlier work (Bodwin, 1985; Collins, Soper, and Sterman, 1985a).' The monograph therefore cites the CSS 1988 Glauber argument in Collins' corrected form.
- **Literature:** Collins:2011zzd §14.4 p. 553; Collins:1988ig; Bodwin1985 PRD 31 (1985) 2616; Collins:1985ue.
- **Source:** research/survey/SURVEY.md item 8, §3.1 item 4; spec/FINAL_OUTLINE.md lem:dy-fsi
- **How to verify:** Read p. 553 of the OA PDF and identify which errors of CSS 1988 are corrected.

### E32 — 'Commonly quoted' C^{q,(1)}_{2,n} variant fails the Adler check

- **Kind:** erratum
- **Statement:** A commonly quoted variant of the one-loop DIS moment C^{q,(1)}_{2,n} (units α_s/4π), with 2/(n+1) + 1/n² in place of 4/(n+1) + 2/n², fails the n = 1 Adler-sum-rule check. Correct: C^{q,(1)}_{2,n} = C_F[2S_1² − 2S_2 + 3S_1 − 2S_1/(n(n+1)) + 3/n + 4/(n+1) + 2/n² − 9], which vanishes at n = 1 and equals 2C^q_{2,N} of c_dis (units α_s/2π). The printed source of the variant is not specified.
- **Literature:** BardeenEtAl1978 PRD 18 (1978) 3998; Vermaseren–Vogt–Moch NPB 724 (2005) 3, arXiv:hep-ph/0504242, eqs. (A.3)-(A.4).
- **Source:** research/critic/REVIEW.md §6 (row 'One-loop coefficient moments'), §10 c2; research/c_dis/DERIVATION.md §11
- **How to verify:** Evaluate both forms at n = 1, and compare with the Mellin moments of C_2^q (research/c_dis/moments.py). Identify where the variant is printed.

### E33 — Published errata whose content was not examined

- **Kind:** erratum
- **Statement:** Published errata exist, but their content was not examined by the agents, for papers cited in the monograph: Bodwin PRD 31 (1985) 2616 [PRD 34 (1986) 3932]; Collins–Soper NPB 193 (1981) 381 [NPB 213 (1983) 545]; Collins PRD 57 (1998) 3051 [PRD 61 (2000) 019902]; Bodwin–Braaten–Lepage PRD 51 (1995) 1125 [PRD 55 (1997) 5853]; Becher–Neubert PRL 102 (2009) 162001 [PRL 111 (2013) 199905]; Henneaux PLB 313 (1993) 35 [PLB 316 (1993) 633]; Ebert–Gao–Stewart JHEP 06 (2022) 007 [07 (2023) 096]; Rodini–Vladimirov JHEP 08 (2022) 031 [12 (2022) 048]; Kovchegov–Pitonyak–Sievert JHEP 01 (2016) 072 [10 (2016) 148]; Cougoulic et al. JHEP 07 (2022) 095 [09 (2024) 052]; Dixon et al. JHEP 05 (2020) 135 [06 (2024) 143]; Forshaw–Holguin JHEP 12 (2021) 084 [04 (2024) 097]; Becher et al. JHEP 11 (2016) 019 [05 (2017) 154]; Bertone et al. JHEP 03 (2020) 135 [08 (2022) 108]; Diehl–Ostermeier–Schäfer JHEP 03 (2012) 089 [03 (2016) 001]; Kramer–Lampe ZPC 34 (1987) 497 [42 (1989) 504]; Penin PLB 745 (2015) 69 [two errata]; Floratos et al. two-loop kernels (+ erratum).
- **Literature:** As listed (INSPIRE records in frontier/others/OTHERS.md App. A and research/survey/survey_refs.bib).
- **Source:** frontier/others/OTHERS.md App. A; research/survey/SURVEY.md items 2, 8, 10, 14, 19; research/c_ee/DERIVATION.md §12
- **How to verify:** For each formula quoted from these papers, confirm that the corrected (erratum) version is used.

### E34 — NLP and small-x literature disagreements

- **Kind:** erratum
- **Statement:** Disagreements with earlier literature, reported by the papers themselves and printed in the frontier chapter as attributed statements. (i) Liu–Mecaj–Neubert–Wang (2021): their SCET endpoint-factorization theorem for h→γγ through a b-quark loop predicts the three-loop logarithms O(α_bα_s²L^k), k = 6,5,4,3, L = ln(−M_h²/m_b²). This agrees with a numerical computation and disagrees with earlier conventional predictions of the subleading-log series. (ii) Rodini–Vladimirov (2024), complete SIDIS at NLP, report 'several differences with earlier derivations'. (iii) Balitsky–Chirilli (2008): the forward linearization of the NLO BK kernel agrees with NLO BFKL up to a term ∝ α_s²ζ(3)×(original dipole), which they attribute to different longitudinal cutoffs. (iv) Small-x helicity: Borden–Kovchegov (2023) obtain the intercept α_h ≃ 3.66074√(α_sN_c/2π). Their resummed Δγ_GG(ω) agrees with fixed order through three loops but differs from Bartels–Ermolaev–Ryskin (intercept 3.66394√(α_sN_c/2π)) from four loops on. This is an open problem, with no verdict.
- **Literature:** Liu:2020wbn JHEP 01 (2021) 077, arXiv:2009.06779 (Secs. 3 and 6); Rodini:2023plb PRD 110 (2024) 034009, arXiv:2306.09495 (abstract); Balitsky:2007feb PRD 77 (2008) 014019, arXiv:0710.4330, Sec. VIII; Borden:2023ugd PRD 108 (2023) 014001, arXiv:2304.06161; Bartels–Ermolaev–Ryskin (BER; not in our bib, reference to be added and verified).
- **Source:** frontier/others/OTHERS.md §5.2 (h→γγ), §6 (NLP TMD), §9.2 (NLO BK), §10 small-x helicity (lines 1176-1183), §0 item 3
- **How to verify:** Read the cited passages, which were read at abstract level only for (ii). For (iv), compare the four-loop coefficients of Δγ_GG(ω) in Borden–Kovchegov and BER. Do not print a verdict.

### E35 — MS-bar positivity: CFH argument fails (CRS); Yukawa counterexample

- **Kind:** erratum
- **Statement:** Positivity of MS-bar PDFs. Collins–Rogers–Sato (2022) state that the argument of Candido–Forte–Hekhorn (2020), that NLO MS-bar PDFs are positive in the perturbative regime, fails at the step 'bare PDFs are positive'. In 'track B' (massless partonic collinear divergences regulated with n > 4) the UV-divergent contributions are positive for n < 4 but can become negative after continuation to n > 4. Counterexample, CRS eqs. (55)-(56), re-verified by OTHERS S2: in the massive Yukawa model, f_{q/p}(ξ;μ) = a_λ(1−ξ)[ln(μ²/Δ) − 1 + (m_q + ξm_p)²/Δ] with Δ = ξm_s² + (1−ξ)m_q² − ξ(1−ξ)m_p². This is negative for small μ: for m_q = 0.3, m_p = 1.0, m_s = 1.5 GeV, negative for ξ ∈ [0.28, 0.98] at μ = 0.8 GeV; the ξ→1 sign change is at μ_* = m_s exp{½[1 − (m_q+m_p)²/m_s²]} = 1.70 GeV. Hence 'MS-bar PDFs are positive for all μ' is [V]. Disputed remainder: Candido–Forte–Giani–Hekhorn (2024) agree that PDFs turn negative at a low enough, non-perturbative scale, and maintain positivity in the perturbative domain, Q² ≳ 5 GeV² (conservative). Positivity above some scale is graded [P].
- **Literature:** Candido:2020yat JHEP 11 (2020) 129, arXiv:2006.07377; Collins:2021vke PRD 105 (2022) 076010, arXiv:2111.01170, eqs. (55)-(59), Sec. VIII B; Candido:2023ujx EPJC 84 (2024) 335, arXiv:2308.00025, Secs. 3-4.
- **Source:** frontier/others/OTHERS.md §7 (Props. 7.1, 7.2, table), §14.1
- **How to verify:** Re-run frontier/others/scripts/s2_crs_yukawa_pdf.py: the MS-bar bracket, the counterterm −a_λ(1−ξ)S_ε/ε, agreement with the k_T-cutoff form to O(m²/μ²), the negative region and μ_*. Read CFH §2-3 to locate the bare-positivity step.

### E36 — Gaunt / RS Glauber-violation claims vs SYZ 2018 (disputed)

- **Kind:** erratum
- **Statement:** Contested claims of factorization violation by spectator–spectator (S–S) Glauber exchange. (a) Gaunt (2014): the CSS cancellation fails with two Glauber gluons between spectators for hadronic E_T. MPI-sensitive observables (E_T, beam thrust, transverse thrust) would then receive leading-power spectator-Glauber contributions. This is an argument, graded [C]. (b) Rothstein–Stewart (2016) §11.1: with Δp_⊥ ~ Q_* constrained, S–S Glauber exchanges 'spoil the factorization ... starting at O(α_s⁴)' for beam thrust, transverse thrust and E_T. (c) Schwartz–Yan–Zhu (2018) show, as an all-order argument [A], that for pure Glauber ladders all factorization-violating effects cancel at cross-section level for any IR-safe single-scale observable, ∫dz dz̄ Σ_cuts(ladders) = 0, and state that this 'disproves previous claims'. A leading violation then needs soft emission off the Glauber rungs (Lipatov vertex). Status printed: (b) disputed / not established, surviving only for multi-differential measurements. Zeng's (2015) model counterexample to generalized factorization (non-zero leading-power longitudinal-spin asymmetry in DY with jet veto / beam thrust) is [V] (model), outside SYZ's stated scope. Standard factorization for MPI-sensitive observables is [C].
- **Literature:** Gaunt:2014ska JHEP 07 (2014) 110, arXiv:1405.2080 (abstract and SYZ's summary); Rothstein:2016bsq JHEP 08 (2016) 025, arXiv:1601.04695, §11.1, eq. (11.13); Schwartz:2018obd PRD 97 (2018) 096017, arXiv:1801.01138, eq. (53) and scope statement; Zeng:2015iba JHEP 10 (2015) 189, arXiv:1507.01652 (abstract).
- **Source:** frontier/others/OTHERS.md §4.1(iv)-(v), §4.2(a)-(c), §4.7; refdoc/REFDOC_ANALYSIS.md ERR-M30; research/survey/SURVEY.md §3.1 item 6
- **How to verify:** Read the SYZ abstract and conclusions and the exact observables and orders claimed by Gaunt 2014 and RS §11.1; Zeng 2015 was read at abstract level only. Check that the monograph's prop:break-jet-veto states the scope correctly.

## 4. New results claimed in our material (29)

### N01 — Two-gluon eikonal exchange: O(g⁴) unitarity and Regge phase (本书新结果)

- **Kind:** new_result
- **Statement:** prop:dy-eikonal-twogluon [R, R_PT]. This is the only statement marked 「本书新结果（待文献核查）」. Setting: two infinite time-like Wilson lines (rapidity difference Y > 0, colour generators T_A, T_B) exchange two gluons of mass m with exact propagators, at fixed transverse momenta; a = k_T² + m², b = (K−k)_T² + m². (a) Longitudinal integrals: J_box = (2π/(ab))(π + iY), J_cross = −2πiY/(ab). With X = T_A·T_B, c_box = X² and c_cross = X² + (C_A/2)X, J_box c_box + J_cross c_cross = (2π/(ab))[πX² − iY(C_A/2)X]. (b) The first term is the exponentiation term ½(−iχ)²X²; the second is i × real × Hermitian, the one-loop reggeization phase ∝ C_A Y. (c) Hence p_opp = −iY/π, Re p_opp = 0, the strict-window residual −½C_Aχ²(Re p_opp)X vanishes, and V†V = 1 + O(χ³). Real cuts start at O(g⁶), because one-gluon emission from straight infinite lines is ∝ δ(v·k). Not shown: the other O(g⁴) graphs (argued to give only phases), non-eikonal spectators, all orders. The companion rem:dy-common-ordering says the RS regulator agrees: crossed Glauber boxes vanish.
- **Literature:** Ingredients: Cheng–Wu (1969, high-energy QED eikonal); Korchemskaya–Korchemsky NPB 437 (1995) 127; Korchemsky PLB 325 (1994) 459; Caron-Huot:2013fea JHEP 05 (2015) 093, arXiv:1309.6521; Rothstein:2016bsq arXiv:1601.04695, eqs. (9.1),(9.18),(9.19). None of these is in refs_merged.bib (S60).
- **Source:** refdoc/REFDOC_ANALYSIS.md §0 'New and sharpened results', ERR-S1, §3 E15, §5 S37, S57 (misconception M32), S59, S60
- **How to verify:** Re-run refdoc/work_R3/scripts/eikonal_box.py, eikonal_box_check.py and eikonal_box_closedform.py (residues vs brute-force iε quadrature, < 5e−16). Re-derive J_box, J_cross by k^+ and k^- residues. Literature check required before printing the marker: search INSPIRE (Cheng–Wu; Korchemsky; Caron-Huot; Aybat–Sterman 2009; Rothstein–Stewart §9) for the statement that the strict-truncation residual is an artefact.

### N02 — Collins' Thm 3 = Gordan's alternative; min-norm margin

- **Kind:** new_result
- **Statement:** OTHERS Prop. 1.2 [R]. Collins' geometric Theorem 3 in arXiv:2007.04085 (a good contour-deformation direction exists iff the point is not a Landau point; about 12 pp. in his Secs. V-VII, footnote 6: not found in the convex-geometry literature) is Gordan's theorem of the alternative (1873). For vectors D_j: either ∃w with D_j(w) > 0 ∀j, or ∃λ_j ≥ 0, not all zero, with Σλ_jD_j = 0. Constructive proof: w = the minimum-norm point of conv{D_j}. If w ≠ 0, then D_j(w) ≥ |w|² for all j, an explicit margin usable as a deformation recipe. The analytic half (Thm 2, anomalous deformations) is Collins' own. Checked on 400 random instances (226 of type I, 174 of type II). Whether this identification is already noted in the literature was not verified.
- **Literature:** Collins:2020euz arXiv:2007.04085, Thms 1-3, Secs. V-VII, footnote 6; P. Gordan, Math. Ann. 6 (1873) 23-28, DOI 10.1007/BF01442864.
- **Source:** frontier/others/OTHERS.md §1.3, §14.2 item 1; spec/FINAL_OUTLINE.md lem:appD-gordan; research/c_regions/DERIVATION.md Thm L3
- **How to verify:** Re-run frontier/others/scripts/s1_landau_gordan.py (S1(a)). Prove the margin by hand: for the min-norm point w of a convex set C, ⟨w, c − w⟩ ≥ 0 ∀c ∈ C. Search the literature (e.g. Pham, Landau-singularity texts; Collins 2020 refs) for prior use of Gordan's theorem in Landau analysis.

### N03 — Coleman–Norton picture in momentum space incl. eikonal lines

- **Kind:** new_result
- **Statement:** OTHERS Cor. 1.3 [R]†, inheriting the dagger of Collins Thm 1. This is a momentum-space derivation of the Coleman–Norton picture including massless lines and eikonal (Wilson) lines, with no Feynman parameters. A point is trapped iff there are λ_j ≥ 0, not all zero, supported on on-shell lines, with Σ_j η_{jL}λ_jΔ_j^μ = 0 for every loop L. Here Δ_j = k_j for propagators and Δ_j = n_j for eikonal lines. It is an algebraic corollary of Collins' Thm 1; that the sign condition (8.15) holds for all graphs used is checked in S1(c).
- **Literature:** Collins:2020euz arXiv:2007.04085, Thm 1, eq. (8.15); Coleman:1965xm Nuovo Cim. 38 (1965) 438.
- **Source:** frontier/others/OTHERS.md §1.5, §14.2 item 2
- **How to verify:** Re-derive the corollary from Thm 1 plus Gordan (N02). Re-run frontier/others/scripts/s1_landau_gordan.py (S1(b),(c),(d)). Check that (8.15) holds for eikonal propagators 1/(n·k ± i0).

### N04 — Moment reduction of the bilocal BRST classification

- **Kind:** new_result
- **Statement:** OTHERS Prop. 8.1 [A]: moment reduction of the BRST-classification problem for the standard bilocal PDF operator O_q(w^-) = ψ̄γ^+Wψ. Hypotheses: (H1) the Joglekar–Lee/Henneaux classification of local twist-2 all-plus operators; (H2) support in [−1,1]; (H3) the bare non-local operator is the generating function of the bare local operators. Then in physical matrix elements O^R = Z_OO ⊗ O_(0) with ∫dz z^{N−1}Z_OO(z) = Z^(N)_tw2, and the class A/B (BRST-exact, EOM) operators drop out. Uniqueness follows from compact support via Müntz–Szász (even/odd N separately). This closes the renormalization part of the gap in Collins 2011 §11.3.2 for physical matrix elements; the multilocal classification needed in the factorization proof remains [C].
- **Literature:** Collins:2011zzd §11.3.2 pp. 407-410; Joglekar–Lee, Ann. Phys. 97 (1976) 160; Henneaux:1993jn PLB 313 (1993) 35 [Erratum PLB 316 (1993) 633], arXiv:hep-th/9306101.
- **Source:** frontier/others/OTHERS.md §8.3(b), §14.2 item 3
- **How to verify:** Check each step: moment generation, interchange of renormalization with moments (needs H3), and the Müntz–Szász uniqueness on [−1,1] for even and odd N. Search the literature (Collins–Rogers 2008; Braun–Manashov light-ray operator renormalization) for an existing equivalent argument.

### N05 — One-loop quasi-PDF in the unphysical regions

- **Kind:** new_result
- **Statement:** LaMET one-loop quasi-PDF in the unphysical regions, derived from our own Feynman rules (a = α_sC_F/2π, ξ = x/y). Vertex: a∫_0^1dy′(1−y′)/|ξ−y′|. Sail: (a/(1−ξ))∫_0^1dy′(ξ+y′)/|ξ−y′|. Tadpole: −a/|1−ξ|. Sums: for ξ > 1, a[((1+ξ²)/(1−ξ))ln(ξ/(ξ−1)) + 1]; for ξ < 0, a[−((1+ξ²)/(1−ξ))ln(−ξ/(1−ξ)) − 1]. This agrees with IJJSZ App. B.
- **Literature:** Izubuchi:2018srq PRD 98 (2018) 056004, arXiv:1801.03917, App. B; Xiong:2013bka arXiv:1310.7471.
- **Source:** frontier/lamet/LAMET.md §4.6, §14 item 4
- **How to verify:** Re-run frontier/lamet/scripts/s1_kernels.py. Integrate the three graph expressions analytically for ξ > 1 and ξ < 0 and compare with IJJSZ App. B.

### N06 — One-loop threshold factorization; H_thr = H_qTMD

- **Kind:** new_result
- **Statement:** One-loop threshold factorization of the LaMET kernel, verified numerically to |λ| = 1e5 including the sign of the imaginary part. The threshold hard kernel equals the quasi-TMD hard kernel at one loop, H_threshold = H_quasi-TMD (universality). The summed one-loop anomalous dimensions, Γ_cusp[ln(λ²e^{2γ_E}) − iπ sgn z] plus the non-cusp terms, are μ-independent.
- **Literature:** Ji:2023pba JHEP 08 (2023) 037, arXiv:2305.04416; Ji:2019ewn arXiv:1911.03840.
- **Source:** frontier/lamet/LAMET.md §6.1, §14 item 6
- **How to verify:** Re-run frontier/lamet/scripts/s3_threshold.py and s4_tmd_bvz.py. Compare the threshold limit of the one-loop coordinate kernel with H^(1) of the quasi-TMD (YZLIU check_HL_and_C1.py).

### N07 — Exact target-mass correction for γ^0

- **Kind:** new_result
- **Statement:** Exact target-mass correction (TMC) of the quasi-PDF for Γ = γ^0 (LaMET Prop. 5.1(b)), with c = M²/(4P_z²). Moment factors: K^⊥_N = Σ_i binom(N−i,i)((N−2i)/N)c^i = K_N − (2c/N)dK_N/dc. In x-space, q̃_{γ0}(x) = q̃_{γz}(x) − 2c∫_0^1(dy/y)∂_c q̃_{γz}(x/y). K^⊥_1 = K^⊥_2 = 1, so there is no TMC for the normalization or for ⟨x⟩; K^⊥_3 = 1 + 2c/3, K^⊥_4 = 1 + 3c/2. At O(c), q − c(xq′ + 3q) + 2c∫_{|x|}^1(dy/y)q(x/y), which agrees with BVZ (target-⊥ case). TMC commutes with perturbative matching (Prop. 5.1(d)).
- **Literature:** Chen:2016utp NPB 911 (2016) 246, arXiv:1603.06664; Braun:2018brg arXiv:1810.00048; Radyushkin:2017cyf PRD 96 (2017) 034025, arXiv:1705.01488.
- **Source:** frontier/lamet/LAMET.md §5.1, §14 item 7
- **How to verify:** Re-run frontier/lamet/scripts/s6_tmc.py (40/40). By hand, expand the trace-subtracted local operators for γ^0 vs γ^z to obtain K^⊥_N, and check K^⊥_3, K^⊥_4.

### N08 — Fourier lemma and endpoint dichotomy (BVZ vs RMP counting)

- **Kind:** new_result
- **Statement:** LaMET Lemma 5.2 and Cor. 5.3. Lemma: with z² = −λ²/P_z², FT[z²Λ² r(λ)](x) = +(Λ²/P_z²)ρ″(x). If ρ ~ x^a near x = 0 and ~ (1−x)^b near 1, the relative endpoint factors are a(a−1)/x² and b(b−1)/(1−x)². Corollary (dichotomy): if ρ_4/q ~ (1−x)^δ, the relative power correction is ~ Λ²/((1−x)^{2−δ}P_z²). δ = 1 reproduces the BVZ rule Λ²/((1−x)P_z²); δ = 0 reproduces the RMP rule Λ²/((1−x)²P_z²). The P = 0 normalization adds −¼x̄x²q″/q to R^∥ (−5/12 for ⊥), because [k]_+ contains −¼δ(ᾱ) with ∫k = ¼.
- **Literature:** Braun:2018brg arXiv:1810.00048; Ji:2020ect RMP 93 (2021) 035005 (power-counting rule).
- **Source:** frontier/lamet/LAMET.md §5.2-5.3, §14 item 8
- **How to verify:** Re-run frontier/lamet/scripts/s5_lemmas.py. Prove the lemma by integrating by parts twice in the Fourier integral, and test the dichotomy on ρ_4 = q(1−x)^δ.

### N09 — Moments and convolution domain of the one-loop quasi-PDF

- **Kind:** new_result
- **Statement:** LaMET Props. 4.4 and 4.5: moments and convolution domain of the one-loop quasi-PDF. Large-|ξ| tails: C^MS-bar → −3a/(2|ξ|) and C^ratio → ∓4a/(3ξ²). Hence in MS-bar the zeroth moment of q̃ does not exist. In the ratio scheme ∫q̃ = 1 exactly, but the first moment is log-divergent (tail −4a⟨y⟩/(3x|x|)). The MS-bar convolution C ⊗ f converges iff ∫_0|f| < ∞; the ratio/hybrid convolution needs ∫_0|y f| < ∞. So a Regge-like sea or gluon ~ y^{−1−δ} makes the MS-bar quasi-PDF ill-defined.
- **Literature:** Izubuchi:2018srq arXiv:1801.03917; Ji:2020brr arXiv:2008.03886.
- **Source:** frontier/lamet/LAMET.md §4.6(d), §14 item 9
- **How to verify:** Re-run frontier/lamet/scripts/s1_kernels.py and s5_lemmas.py. Derive the large-|ξ| asymptotics of the one-loop kernels analytically and apply dominated convergence to the convolution integral near y = 0.

### N10 — Fourier-step theorems (strip, truncation bound, Slepian count)

- **Kind:** new_result
- **Statement:** LaMET Fourier-step theorems. Lemma 7.2: if the coordinate matrix element decays as e^{−m|z|}, the quasi-PDF extends analytically to the strip |Im x| < m/P^z (Morera + Fubini), making a statement of Ji–Liu–Su precise. Prop. 7.3: truncating the Fourier integral at z_L errs by at most (A P^z/(πm))e^{−m z_L}; e^{−m z_L} = 0.079 at 1 fm and 0.022 at 1.5 fm for m = 0.5 GeV. Prop. 7.4: the number of recoverable degrees of freedom from data on |λ| ≤ λ_L is ≈ 2λ_L/π (Slepian/Landau–Widom; classical). The number of eigenvalues > ½ is 3, 6, 10, 16 for λ_L = 5, 10, 15, 25. This gives a precise frame for the 'inverse problem' debate.
- **Literature:** Ji:2024oka NPB 1007 (2024) 116670, arXiv:2408.03378; Ji:2026vir arXiv:2601.12189; Slepian–Pollak / Landau–Widom (prolate spheroidal functions; classical).
- **Source:** frontier/lamet/LAMET.md §7.2-7.3, §14 item 10
- **How to verify:** Re-run frontier/lamet/scripts/s5_lemmas.py and s7_fourier.py (eigenvalue counts). Check e^{−0.5 GeV × 1 fm/0.1973 GeV fm} = 0.079 and the 1.5 fm value. Check the bound by majorizing the tail integral.

### N11 — Lean-style dependency graph of the LaMET matching theorem

- **Kind:** new_result
- **Statement:** Lean-style dependency graph of the LaMET matching theorem (nodes N0-N13). A node is [R] only if all parents are [R] and the implication is proven. The non-perturbative content is isolated in hypotheses (H3)-(H5). Key grades: N1 (QCD + space-like auxiliary field renormalizable) [A], asserted for space-like n; N3 = Thm 3.1 (multiplicative renormalizability) [A]; N4 = (H2) space-like OPE [A], with no Zimmermann-level proof; N5 = support [R] in PT.
- **Literature:** Ji:2017oey arXiv:1706.08962; Ishikawa:2017faj PRD 96 (2017) 094019, arXiv:1707.03107; Green:2017xeu arXiv:1707.07152; Izubuchi:2018srq arXiv:1801.03917.
- **Source:** frontier/lamet/LAMET.md §4.5, §14 item 11
- **How to verify:** Audit each edge of the §4.5 table against the cited proofs. Confirm that no node is graded above its weakest parent.

### N12 — Exact Collins remainder of the off-shell triangle (sharpened)

- **Kind:** new_result
- **Statement:** prop:appN-triangle-exact (sharpened explicit result, not marked new) [R, R_PT]. Scalar one-loop off-shell triangle with massless internal lines; p_1 = (P, −m²/(2P), 0_T), p_2 = (m²/(2P′), −P′, 0_T), Q̃² = 2PP′, Q² = (Q̃² + m²)²/Q̃². (a) ∫C_HΓ = Q̃^{−2}(μ²/Q̃²)^ε𝒜; ∫C_{C1}Γ = ∫C_{C2}Γ = −Q̃^{−2}(μ²/m²)^ε𝒜; ∫C_SΓ = Q̃^{−2}(μ²Q̃²/m⁴)^ε𝓑; 𝒜 = Γ(1+ε)Γ(1−ε)²/(ε²Γ(1−2ε)), 𝓑 = Γ(1+ε)²Γ(1−ε)/ε². (b) Σ_R = Q̃^{−2}[ln²(Q̃²/m²) + π²/3]. (c) With t = m²/Q², L = ln(Q²/m²), the exact Collins remainder is ∫r = −4m²/Q⁴ + (m⁴/Q⁶)(L² − 15 + π²/3) + O(m⁶Q^{−8}L²), with no logarithm at NLP. The NLP of the full integral, Q²I = L² + π²/3 + t(2L² − 4L − 4 + 2π²/3) + …, is reproduced by the subtraction terms through Q̃² ≠ Q². Numerically, ∫r = −0.0173434339581 at m² = 0.02, P = 0.8, P′ = 1.3.
- **Literature:** Usyukina–Davydychev 1993 (one-loop triangle Φ^(1)); Collins:2011zzd ch. 10; reference document Ex. D.47 and (D.32).
- **Source:** refdoc/REFDOC_ANALYSIS.md §0, §3 D24, §5 S30, ERR-m25, §2.5 item 2
- **How to verify:** Re-run refdoc/work_SYN/triangle_remainder.py and refdoc/work_R6/check_remainder_d4.py (12 digits). Independently expand Φ^(1)(t,t) to O(t²L²) and subtract (D.32), written in Q̃².

### N13 — Joint-localization lemma with ordering weights (sharpened)

- **Kind:** new_result
- **Statement:** lem:appO-joint-localization (sharpened from the reference's own analysis, not marked new). It replaces Assumption E.33(c1). The equal-light-cone-time limit of N non-commuting single-pole Glauber insertions on one spectator is the weighted sum over orderings π with weights w_π = Π_j z_j / Π_m Σ_{l≥m} z_{π(l)}, z_j = k_{Tj}²/(2k_j^+), for same-side poles; weights are 0 or 1 when the k_j^+ have opposite signs. For N = 2, w_12 = z_1/(z_1+z_2). The weights are piecewise in k_j^+ and non-analytic at k_j^+ = 0.
- **Literature:** Reference document pp. 195-198 (Ass. E.33(c1)); AybatSterman2009 PLB 671 (2009) 46, arXiv:0811.0246 (LCPT precedent).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-S3, §5 S59 list
- **How to verify:** Re-run refdoc/work_R8/check_weights.py (K12) and refdoc/work_R7/check_weights_colour.py. Derive the N = 2 weight from the time-ordered energy denominators and check that Σ_π w_π = 1.

### N14 — Other 'surpass' items of the reference analysis

- **Kind:** new_result
- **Statement:** Further 'surpass' items of the reference-document analysis. (i) lem:appJ-cut-hermiticity: the reference's Assumption E.18(iii) is provable (standard; not marked new). (ii) A side-independent window construction for E14, suggested by reader R7, still to be checked. (iii) An attempt (C9) to discharge the reference's Assumption C.24 (momentum-space OPE remainder) by citing Anikin–Zav'yalov 1978 / Zav'yalov 1990 together with the uniqueness Theorem C.25(iii). (iv) App. O supplies the reference's input D.27 (X1).
- **Literature:** Anikin:1978tj Ann. Phys. 116 (1978) 135; Zav'yalov, Renormalized Quantum Field Theory (Kluwer 1990).
- **Source:** refdoc/REFDOC_ANALYSIS.md §3 (C9, E14 rows), §5 S59
- **How to verify:** For (i), write the proof and check it against the reference's statement. For (iii), read Anikin–Zav'yalov and Zav'yalov 1990 to confirm the theory class (gauge theories?) and the remainder form; their scope is UNVERIFIED (SURVEY).

### N15 — Sharpened Ex C.27 value; F3 lesson

- **Kind:** new_result
- **Statement:** Sharpened example (reference Ex. C.27, unreduced OPE coefficients violate scaling). The combination is −κπ²/(2q⁴) + O(m²q^{−6}ln q), with no logarithm and an m-independent leading term (4D harmonicity), whereas the reference states only O(q^{−4}ln q²). Separately, the 'F3 lesson': per-order region exponents a = β_R/3 can be far from sharp (e.g. 1/243 for the two-loop (S,S) region, against the true O(λ²L²)).
- **Literature:** Reference document Ex. C.27, pp. 101-102; VF-REF-14.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m23, §3 C11, App M M.4 row
- **How to verify:** Re-run refdoc/work_R5/scripts/check1.py. Derive the coefficient from the 4D Laplacian of 1/x² in momentum space.

### N16 — Cauchy–Schwarz proof of I_1(0)+I_2(0) < 0

- **Kind:** new_result
- **Statement:** Proof (c_glauber's own) of a statement that Collins 2007 gives without proof: I_1(0) + I_2(0) < 0 in his scalar model. With dμ(b) = d²b/(2π)²·2πK_0(m_q b), ∫dμ = 1/m_q², F(0) = ∫dμ 2πK_0(m_g b), G(0) = ∫dμ[2πK_0(m_g b)]². Cauchy–Schwarz gives F(0)² ≤ G(0)/m_q², strictly since K_0(m_g b) is not constant. Hence I_1(0) + I_2(0) = 𝒩[F(0)² − G(0)/m_q²] has the sign of −𝒩. Also ∫d²k_T(I_1+I_2) = 0 (Parseval; collinear factorization survives), with F(k) = (π/√Λ)ln((s+√Λ)/(s−√Λ)), s = k² + m_g² + m_q², Λ = s² − 4m_g²m_q². Point values (I_1+I_2)/𝒩 = −21.0, −17.7, −7.19, −0.70, +0.38, +0.089 at k_T = 0, 0.3, 0.8, 1.5, 3, 6, for (m_g, m_q) = (0.5, 1).
- **Literature:** Collins:2007jp arXiv:0708.4410v1, eqs. (10)-(11).
- **Source:** research/c_glauber/DERIVATION.md §2.4 [A4a-A4f]; spec/VERIFIED_FORMULAS.md VF-GLA-8
- **How to verify:** Re-run research/c_glauber/scripts/tmd_breaking_abelian.py. Check the b-space forms F̃ = (2π)²K_0(m_g b)K_0(m_q b) and G̃ = (2π)³K_0(m_g b)²K_0(m_q b), and the Cauchy–Schwarz step.

### N17 — Entanglement test C_F² + 4T_F²(N²−1)/N²

- **Kind:** new_result
- **Statement:** Entanglement test (c_glauber's own) for TMD factorization breaking in pp → h_1h_2X. Attaching the gluon from each spectator to lines X, Y gives Σ_{X,Y}C(X,Y) = C_F² + 4T_F²(N²−1)/N², whereas the factorized prediction is (Σ_X C_1(X))(Σ_Y C_2(Y)) = C_F². For SU(3) this is 24/9 vs 16/9; the extra term has relative weight 4/(N²−1). In the abelian case the two sides agree identically.
- **Literature:** Collins:2007jp arXiv:0708.4410; RogersMulders2010 PRD 81 (2010) 094006, arXiv:1001.2977; CollinsQiu2007 PRD 75 (2007) 114014, arXiv:0705.2141.
- **Source:** research/c_glauber/DERIVATION.md §2.5 [C6, C6b]; spec/VERIFIED_FORMULAS.md VF-GLA-10; spec/FINAL_OUTLINE.md thm:break-tmd
- **How to verify:** Re-run research/c_glauber/scripts/colour_factors.py. Recompute the colour sums with explicit SU(N) generators for N = 2, 3, 4.

### N18 — Gluonic-pole strength C_G = 1 + 2⟨T_a·T_b⟩/C_F

- **Kind:** new_result
- **Statement:** Closed formula for the gluonic-pole strength (c_glauber [C1-C5]). With the pole rule P = −T_a − 2T_b, C_G = 1 + 2⟨T_a·T_b⟩/C_F (SIDIS +1, DY −1). Channel values (SU(3) in brackets): qq′→qq′ tt*, uu*: (N²−5)/(N²−1) (½); tu*: −(N²+3)/(N²−1) (−3/2); qq̄′→qq̄′ tt*: −(N²−3)/(N²−1) (−3/4); qq̄→q′q̄′ ss*, st*: (N²+1)/(N²−1) (5/4). QVY graph by graph: C_I/C_u = −2/(N²−1), C_F1/C_u = −1/(N²−1), C_F2/C_u = (N²−2)/(N²−1). This reproduces BBMP Table I and QVY exactly in N.
- **Literature:** BacchettaBomhofMuldersPijlman2005 PRD 72 (2005) 034030, arXiv:hep-ph/0505268, Table I, eqs. (B5)-(B6); QiuVogelsangYuan2007 PRD 76 (2007) 074029, arXiv:0706.1196, Table I, eqs. (25)-(28).
- **Source:** research/c_glauber/DERIVATION.md §2.3; spec/VERIFIED_FORMULAS.md VF-GLA-6; spec/FINAL_OUTLINE.md prop:break-colour
- **How to verify:** Re-run research/c_glauber/scripts/colour_factors.py and glauber_poles.py. Compare channel by channel with BBMP Table I and QVY Table I for general N.

### N19 — Further c_glauber results

- **Kind:** new_result
- **Statement:** Further c_glauber results (derived and script-checked; novelty not claimed). (i) Exact finite-ε cut-sum telescoping identity, using 2πδ(a) → 2ε/(a²+ε²) = i[(a+iε)^{−1} − (a−iε)^{−1}]. (ii) Ladder vs crossed-ladder colour factors for any representations, c = T_1·T_2: L = c², X = c² + (C_A/2)c; a Glauber phase does not commute with other soft exchanges, [T_A·T_B, T_A·T_j] ≠ 0. (iii) Abelian S–S kernel V = −ie_Ae_B/(k_T² + m_g²), so χ(b) = −e_Ae_B K_0(m_g b)/(2π). (iv) Diffractive dipole toy: singlet→octet leakage is quadratic in the phase difference, with coefficient C_F/(2N) = 2/9 for SU(3).
- **Literature:** Rothstein:2016bsq arXiv:1601.04695 (no explicit general ladder/crossed formula there); AybatSterman2009 arXiv:0811.0246.
- **Source:** research/c_glauber/DERIVATION.md §1.6, §2 (telescoping identity), §3.2-3.4; spec/VERIFIED_FORMULAS.md VF-GLA-9, VF-GLA-11
- **How to verify:** Re-run research/c_glauber/scripts/unitarity_cuts.py, ss_exchange.py, colour_factors.py and diffraction.py. Check the X formula with explicit SU(3) matrices in the fundamental and adjoint.

### N20 — Time-like vs space-like regulator lines: 2π² difference

- **Kind:** new_result
- **Statement:** New one-loop illustration (c_tmd R3′). For past-pointing (DY) vs future-pointing (SIDIS) non-light-like regulator Wilson lines: with space-like lines, V^SIDIS = (V^DY)* exactly. With time-like lines, Re V^DY − V^SIDIS = (α_sC_F/4π)·2π² + O(ε), because the past-pointing path-ordered operator is anti-time-ordered while Feynman rules compute the time-ordered one (a Coulomb-phase effect). Hence the PT (Sivers-sign) argument fails for time-like lines at finite rapidity. All such terms vanish in the light-like limit; the Fourier transform of the remainder is 2π²/(Λ_B b_T). This supports the space-like choice of Collins 2011 and of Aybat–Rogers (citing Collins–Metz 2004).
- **Literature:** Collins:2011zzd §10.8, §13; AybatRogers2011 arXiv:1101.5057; CollinsMetz2004 PRL 93 (2004) 252001, arXiv:hep-ph/0408249; Collins–Rogers PRD 87 (2013) 034018, arXiv:1210.2100.
- **Source:** research/c_tmd/DERIVATION.md R3′, §3.4, §6.2, §8 item 5; spec/VERIFIED_FORMULAS.md VF-TMD-9
- **How to verify:** Re-run research/c_tmd/scripts/virtual_vertex.py. Compute the one-loop vertex with n_B = (se^{2y_B}, 1, 0_T) for s = ±1 and both i0 prescriptions; the difference of the real parts is 2π²(α_sC_F/4π).

### N21 — Exact Isgur–Llewellyn Smith soft fractions

- **Kind:** new_result
- **Statement:** Exact Isgur–Llewellyn Smith soft fractions ('derived here', sympy exact). R is the fraction of the LO pion-form-factor u-line integral with gluon virtuality x̄ȳQ² < μ_0², c = μ_0²/Q² ≤ 1. R_as(c) = c[5c − 2(c+2)ln c − 4] for the asymptotic DA; R_CZ(c) = c[456c³ + 352c² − 675c − 132 − (144c³ + 768c² + 450c + 36)ln c] for the CZ DA. R(1) = 1; as c → 0, R_as ≃ 4c ln(1/c) and R_CZ ≃ 36c ln(1/c). For μ_0² = 1 GeV²: 0.87, 0.62, 0.15 at Q² = 4, 10, 100 GeV² (CZ: 0.98, 0.90, 0.48).
- **Literature:** IsgurLlewellynSmith1984 PRL 52 (1984) 1080; Isgur:1988iw NPB 317 (1989) 526; ChernyakZhitnitsky1984 Phys. Rept. 112 (1984) 173.
- **Source:** research/c_exclusive/DERIVATION.md §4.3 (lines 255-260)
- **How to verify:** Re-run research/c_exclusive/scripts/s4_pion_ff.py (analytic = numerical). By hand, integrate φ(x)φ(y)/(x̄ȳ) over the region uv < c with the asymptotic DA 6xx̄. Check whether closed forms already exist in the ILS papers.

### N22 — Prescription dependence of the X_A model

- **Kind:** new_result
- **Statement:** Prescription dependence of the BBNS/BN annihilation model (derived; a model, not a theorem). If the same divergent A_3^i integral is regulated by cutting both x < 1−δ and y > δ instead of the BN rule ∫_0^1dy/y → X_A, ∫_0^1(ln y/y)dy → −½X_A², the result differs by −21.6 at X_A = 13.8. Re-derived forms: A_1^i ≈ A_2^i ≈ πα_s[18(X_A − 4 + π²/3) + 2r_χ²X_A²]; A_3^i ≈ 6πα_s(r_χ^{M1} − r_χ^{M2})(X_A² − 2X_A + π²/3); A_3^f ≈ 6πα_s(r_χ^{M1} + r_χ^{M2})(2X_A² − X_A); A_1^f = A_2^f = 0.
- **Literature:** BenekeEtAl2001 NPB 606 (2001) 245, arXiv:hep-ph/0104110, (XAdef), (XHparam), (XAparam); BenekeNeubert2003 NPB 675 (2003) 333, arXiv:hep-ph/0308039, (XAdef), (XAmodel).
- **Source:** research/c_scet/DERIVATION.md §5.7
- **How to verify:** Re-run research/c_scet/scripts/s4_bbns.py. Evaluate the A_3^i integral with both cutoff prescriptions at the X_A corresponding to δ and compare.

### N23 — Own proofs of classical mathematical facts

- **Kind:** new_result
- **Statement:** Own full proofs of classical mathematical facts used in the monograph (novelty not claimed). c_pdf Thm 7.2: the even moments with k ≥ k_0 determine g via t = x² and Hausdorff. Cor. 7.3: even N gives q + q̄ and g, odd N gives q − q̄; even moments alone do not separate q and q̄. Prop. 7.5: the LO kernels are fixed by even moments within r + a[1/(1−x)]_+ + bδ. Prop. 7.7: a function holomorphic and polynomially bounded in Re z > σ_0 with zeros on an arithmetic progression vanishes (Jensen/Blaschke; replaces Carlson). The L² Müntz distance formula is 1/√(2λ+1)·Π|λ−λ_k|/(λ+λ_k+1); the distance of x to span{x^{k²+1}} → π/sinh(√3π) = 0.02722. Also: c_exclusive's Gegenbauer eigenfunction proof (hermiticity plus triangularity), and REVIEW counterexamples L1-L4 (sin(Q²x): moments O(1/Q²) but sup = 1; δ′(x): all even moments vanish; (1 − cos πn)/2 vanishes on even n).
- **Literature:** Titchmarsh, Theory of Functions (1939) §5.81; Boas, Entire Functions (1954) Thm 9.2.1 (both via Waldschmidt arXiv:2002.01223); Müntz–Szász theorem.
- **Source:** research/c_pdf/DERIVATION.md §7; research/c_exclusive/DERIVATION.md (ERBL eigenfunctions); research/critic/REVIEW.md (counterexamples)
- **How to verify:** Re-run research/c_pdf/scripts/s6_uniqueness.py and research/c_exclusive/scripts/s3_erbl_eigen.py. Check π/sinh(√3π) numerically, and check the Carlson location in Titchmarsh §5.81.

### N24 — R_{e⁺e⁻} finiteness route and exact cutting identity

- **Kind:** new_result
- **Statement:** c_ee Thm 5.1 (route, novelty not claimed), thm:ee-R-finite [R, R_PT]. All-order IR finiteness of R = 12π Im Π follows from Euclidean finiteness (Poggio–Quinn; Lowenstein–Zimmermann; Breitenlohner–Maison): the Laurent coefficients in ε are polynomials in L = ln(−s/μ²) that vanish for real L, hence identically, so continuation commutes with ε → 0. Identification with the DR sum over partonic cuts is [A] (cor:ee-cuts). Exact-in-ε cutting identity, proven analytically term by term: 2(D−1)s Im Π^(1)_bare = ρ_V + ρ_R. Also Π_MS-bar = N_c e²/(12π²)[5/3 − L + (α_s/π)(3C_F/4)(55/12 − 4ζ_3 − L)].
- **Literature:** Poggio:1976qr = PoggioQuinn1976 PRD 14 (1976) 578; LowensteinZimmermann1975 CMP 44 (1975) 73; Lowenstein CMP 47 (1976) 53; BreitenlohnerMaison1977a/b/c CMP 52 (1977) 11, 39, 55.
- **Source:** research/c_ee/DERIVATION.md §5; spec/VERIFIED_FORMULAS.md VF-EE-8; spec/FINAL_OUTLINE.md thm:ee-R-finite
- **How to verify:** Re-run research/c_ee/cut_identity_analytic.py, pi_twoloop.py and rg_structure.py. Check that Breitenlohner–Maison II covers non-abelian gauge theory with ghosts ('to verify' in c_ee).

### N25 — Abelian Glauber toy in DY; plus trap

- **Kind:** new_result
- **Statement:** c_dy abelian Glauber toy (novelty not claimed). (G-i) χ(b) = −(g_Ag_B/2π)K_0(m|b|), exact eikonal. (G-ii) The exchange cancels inclusively in the relative spectator k_T. (G-iii) S–S exchange is trapped. (G-iv) Active–spectator exchange at one loop is not trapped in k^+: it saturates at |k^+| ~ Q and equals the A-collinear term with a past-pointing line (+i0) [P]; I_as = 2πiθ(−k^-)/(2p_b^-K² + 2k^-c_b). Also: the 'plus trap', (1+z²)𝒟_1 vs [(1+z²)/(1−z)]_+, differ by (7/4)δ(1−z), i.e. 7C_F in the δ coefficient of the DY coefficient function.
- **Literature:** Collins:2011zzd §14.3-14.4; Bodwin1985 PRD 31 (1985) 2616.
- **Source:** research/c_dy/DERIVATION.md (Glauber toy, plus trap); spec/FINAL_OUTLINE.md (Ch10 DY coefficient note)
- **How to verify:** Re-run research/c_dy/glauber_toy.py and plus_trap.py. Integrate ∫_0^1(1+z²)/(1−z) minus its plus-regularized form to obtain 7/4.

### N26 — Eikonal identity exact only with the adiabatic regulator

- **Kind:** new_result
- **Statement:** c_wilson: the eikonal (Ward) identity for Wilson lines is exact at finite ε only with the adiabatic regulator e^{−ε|t|}; with a uniform +iε in all eikonal propagators it is not exact at finite ε. Novelty not claimed.
- **Literature:** Collins:2011zzd ch. 7, 10-11.
- **Source:** research/c_wilson/DERIVATION.md (eikonal identity section)
- **How to verify:** Re-run research/c_wilson/scripts/s2_eikonal_identity.py. Check the two-gluon eikonal identity with both regulators at finite ε.

### N27 — Distributional verification of the one-loop LaMET kernels

- **Kind:** new_result
- **Statement:** Distributional verification of the complete one-loop MS-bar and ratio quasi-PDF kernels as Fourier transforms of the coordinate-space kernels, for both Γ = γ^0 and γ^z, to 1e−9 to 1e−12 on test functions. It uses FT[ln(z²μ²e^{2γ_E}/4)] = −2γ_E δ(x) − [1/|x|]_reg-type identities. Consistency remark: Ji's momentum-space RGE coefficient −(3/2)δ follows from the MS-bar kernel via d l_p/d ln P_z = −2.
- **Literature:** Izubuchi:2018srq arXiv:1801.03917; Ji:2020brr arXiv:2008.03886; Radyushkin:2017cyf arXiv:1705.01488.
- **Source:** frontier/lamet/LAMET.md §3.7, §4.6, §14 item 5
- **How to verify:** Re-run frontier/lamet/scripts/s2_ft_testfunctions.py. Pair both sides with smooth test functions, including ones that do not vanish at x = 1 and at large |x|.

### N28 — OTHERS checked transcriptions

- **Kind:** new_result
- **Statement:** OTHERS 'checked transcriptions', listed among the report's new statements (§14.2 item 4); these are not novel. (i) The BNS super-leading-log tower sums to ₂F₂(1,1;2,5/2;−w), first SLL coefficient (4/(15π²))C_FN_cα_s⁴L⁵ΔY σ̂_B, with ₂F₂ ~ (3/2)ln w/w (1.497 at w = 1e8). (ii) The h→γγ leading-double-log series ℳ_0L̂²Σ n!/(2n+2)!(−C_Fα_sL̂²/2π)^n = ℳ_0(L̂²/2)₂F₂(1,1;3/2,2;−C_Fα_sL̂²/(8π)), matching NLO terms L̂²/2 and (C_Fα_s/4π)(−L̂⁴/12). (iii) The LUXqed photon PDF in the point-like limit gives Frixione et al. eq. (4.189): xf_γ = (α/2π)[1+(1−x)²][ln(μ²/m²) − 2ln x − 1] + αm²x²(1−x)/(πμ²). Dropping F_L shifts this by (α/2π)·4(1−x); dropping the MS-bar conversion term shifts it by (α/2π)x². (iv) The CRS Yukawa MS-bar PDF and its sign structure (see E35). (v) The LO BK kernel eigenvalue χ(γ), with χ(½) = 4 ln 2.
- **Literature:** Becher:2021zkk PRL 127 (2021) 212002, arXiv:2107.01212; Liu:2019oav JHEP 04 (2020) 033, arXiv:1912.08818, eqs. (1),(3); Manohar:2016nzj PRL 117 (2016) 242002, arXiv:1607.04266, eq. (6); Frixione:2019lga JHEP 11 (2019) 158, arXiv:1909.03886, eq. (4.189); Collins:2021vke arXiv:2111.01170, eqs. (55)-(59); Balitsky:2007feb arXiv:0710.4330.
- **Source:** frontier/others/OTHERS.md §4.4, §5.2, §13 (LUXqed), §7, §9.1, §14.2 item 4
- **How to verify:** Re-run frontier/others/scripts/s3_luxqed_pointlike.py, s4_resummed_series.py and s5_bk_kernel.py. Check the hypergeometric identities term by term to n = 10.

### N29 — YZLIU derived cross-checks

- **Kind:** new_result
- **Statement:** YZLIU derived cross-checks of Liu-programme formulas (derived here; not claimed novel; printed as verified formulas). (i) H = C_HL^+C_HL^- with C_HL^± = 1 + (α_sC_F/8π)(−4 − 5π²/6 + 2L_± − L_±²); H^(1) = (α_sC_F/2π)(−2 + π²/12 − L_z²/2 + L_z) (ESZ form); G^(1) = (α_sC_F/π)(1 − ln(ζ_z/μ²)). (ii) c_H = (241ζ_3/(144π²) + 11π²/320 − 559/1728 − 971/(324π²))C_FC_A + (−45ζ_3 − 2π⁴ + 30π² − 30)/(24π²)C_F² + (36ζ_3 + 51π² + 1312)/(1296π²)C_Fn_fT_F ≈ 0.0725C_F² − 0.0840C_FC_A + 0.1453C_Fn_fT_F. (iii) γ̃_J^(2) = C_FC_A(−1396/27 + 23π²/9 + 20ζ_3) + C_Fn_f(232/27 − 2π²/9), in units of (α_s/4π)², from JLS (A.4)-(A.5). (iv) N_m = C_F e^{5/6}/π ≈ 0.977. (v) 𝒟_1 = (𝒟 + 𝒟_2)/2. (vi) The final-state-sum identity (C.1) of Liu 2024 checked for n = 2, 3, 4. (vii) GN inequalities (4.2)-(4.5) checked on 4000 points. (viii) One-loop threshold: for 0 < y < 1, (α_sC_F/2π)·2/(1−y)·(L_z + ln(1−y) − 1) = J_f^(1).
- **Literature:** Ji:2023pba arXiv:2305.04416, eqs. (A.4)-(A.5), (A.13); Liu:2023onm arXiv:2311.06907, eqs. (2.41)-(2.42), (2.52); Liu:2023pjb arXiv:2312.05957, eq. (C.1); Liu:2024omb arXiv:2403.06787, eqs. (4.2)-(4.5); Ebert:2018gzl arXiv:1811.00026.
- **Source:** frontier/yzliu/YZLIU.md §3.B, §3.C, §3.D1, §5 checks
- **How to verify:** Re-run frontier/yzliu/scripts/check_HL_and_C1.py, check_gammaC2.py, check_GN_ineq.py and crossref_check.py. Evaluate the c_H closed form numerically against the quoted decimals.

## 5. Corrections of the reference document (factorization_qcd-2.pdf) (44)

### R-S1 — Two-Glauber 'residual' is an artefact; C_A term = reggeization phase

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-S1, the main correction; reference pp. 57-58 (Prop 9.3, Fig 36), 61 (§9.5), 85 (§15.1), and App E (Prop E.31(iv), Ex E.38, Lemma E.48(d), Rem E.49). The reference claims that non-abelian spectator–spectator two-Glauber exchanges leave the residual −¼C_Aχ²T_A·T_B, that the common ordering is a 'regularization convention', and that Ass. E.33(c) 'including real emission' is needed. This is its justification for grading DY B′ instead of B. Correction to print: the colour algebra is right for independent symmetric cutoffs (p_opp = ½). But the exact eikonal box and crossed box give p_opp = −iY/π, so Re p_opp = 0 and the residual −½C_Aχ²(Re p_opp)X vanishes. The C_A term is the one-loop reggeization phase, −iY(C_A/2)X·2π/(ab). Hence V†V = 1 + O(χ³) with no real emission; the residual is an artefact of the strict instantaneous truncation, which discards principal-value parts near 2k^+k^- = k_T². What stays open is non-eikonal spectators and active partons. Reader disagreement resolved: (E.51) on p. 217 has A_2 = ½(−iχ)²(X² + ¼C_AX), so the reference's residual is −¼C_Aχ²X; reader R4's '−1/8' is a slip. Formulas: see N01.
- **Literature:** Reference document (factorization_qcd-2.pdf; not citable) pp. 57-61, 85, 198-223, (E.51) p. 217; Rothstein:2016bsq arXiv:1601.04695, eqs. (9.1),(9.18),(9.19); Caron-Huot:2013fea arXiv:1309.6521; Korchemskaya–Korchemsky NPB 437 (1995) 127.
- **Source:** refdoc/REFDOC_ANALYSIS.md §0 item 1, ERR-S1, §2.5 item 1, §5 S37, S57 (M32)
- **How to verify:** Re-run refdoc/work_R3/scripts/eikonal_box*.py. Read reference p. 217, (E.51), at 200 dpi to confirm the ¼C_A coefficient. Check the literature for prior statements (see N01).

### R-S2 — TMD-breaking colour bookkeeping: T_a + 2T_b

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-S2, reference p. 74 (argument for Thm 12.3, TMD breaking colour bookkeeping). The reference claims that, with a uniform eikonal numerator and T_a + T_b = T_c + T_d, the combination η_bT_b + η_cT_c + η_dT_d is irreducible 'because η_b ≠ η_{c,d}'. With those conventions it reduces to −η_bT_a, which would predict no Sivers sign flip and contradicts Collins–Qiu's iπ(g_1 + 2g_2). Correct: with all-outgoing charges (Σ_jT_j = 0; initial lines 1/(n·k + i0), final lines 1/(n·k − i0)), the Glauber part is ∝ T_b − T_c − T_d = T_a + 2T_b, which is irreducible. SIDIS gives +T_a and DY gives −T_a (sign flip). The monograph's prop:break-colour, P = −T_a − 2T_b, is correct.
- **Literature:** Reference p. 74; CollinsQiu2007 PRD 75 (2007) 114014, arXiv:0705.2141, eqs. (4.1)-(4.3).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-S2
- **How to verify:** Re-run refdoc/work_R4/checks_R4.py. Redo the colour algebra for qq′ → qq′ with both conventions and compare with CQ eq. (4.3).

### R-S3 — Ass. E.33(c1) false; ordering-weight lemma

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-S3, reference p. 198 (Ass E.33(c1); consequences in Prop E.35, Thm E.8(i)(ii)). The reference asserts a fixed localization order for non-commuting equal-time Glauber insertions on one spectator. Its own analysis (pp. 195-196) gives a weighted sum w_12O_2O_1 + w_21O_1O_2 with w_12 = z_1/(z_1+z_2), z_j = k_Tj²/(2k_j^+), for same-side poles, and weights 0/1 for k_1^+k_2^+ < 0. A fixed order errs by w_21[O_1,O_2] = O(1), so (c1) is generically false per graph. Correction: replace (c1) by a lemma with ordering weights Π_jz_j/Π_mΣ_{l≥m}z_{π(l)} (see N13), keep only (c2) as an assumption, and note the non-analyticity at k_j^+ = 0.
- **Literature:** Reference pp. 195-198.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-S3
- **How to verify:** Re-run refdoc/work_R8/check_weights.py (K12) and work_R7/check_weights_colour.py. Re-derive w_12 from two sequential energy denominators.

### R-S4 — Super-leading configurations omitted

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-S4, reference pp. 19 (Cor 3.8) and 22 (Thm 3.12, 'p(R) ≥ 0'). Super-leading configurations are omitted. By (3.8) with c_J = 2, (n_F,n_T) = (0,0) has p_J = −2 and (0,1) has p_J = −1; 'all other combinations are suppressed by ≥ λ' is false. Correction: state these configurations and their cancellation in gauge-invariant sums (Ward identity + colour neutrality, CSS 1989 §8.6) [A]. Their O(λ), O(λ²) remainders are leading and build F^{+j}. For a gluon as the only active parton, k·H = 0 and the G term ∝ k^+A^j − k^jA^+ is leading; 'n_T transverse gluons' is not gauge-invariant bookkeeping in the gluon channel.
- **Literature:** Reference pp. 19-22, eq. (3.8); Collins:1989gx Adv. Ser. Direct. HEP 5 (1989) 1, arXiv:hep-ph/0409313, §8.6.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-S4
- **How to verify:** Recompute p_J from (3.8) for (n_F,n_T) = (0,0),(0,1). Read CSS 1989 §8.6.

### R-M1 — 'No Euclidean pinch' false

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M1, reference p. 15 (Cor 3.4), 'no pinch in the Euclidean region'. This is false as stated: zero-momentum massless lines solve the Landau equations for any external kinematics. Correct: in the Euclidean non-exceptional region the only Landau solutions are sets of zero-momentum massless lines, which are IR convergent by power counting (Lowenstein–Zimmermann; IR degree d = A + ½A_q ≥ 2, thm:ee-euclid-ir). With massive lines ℱ > 0 and there is no solution.
- **Literature:** Reference p. 15; LowensteinZimmermann1975 CMP 44 (1975) 73.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M1
- **How to verify:** Exhibit the simplex-corner solutions of the reference's (3.3). Check the IR power-counting degree for zero-momentum gluon and quark lines (refdoc/work_R1/check_kinematics_pc.py).

### R-M2 — Prop 3.5: not Euclidean; π²/3 omitted

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M2, reference pp. 16-17 (Prop 3.5). (3.3) is called 'Euclidean kinematics', but p_i² = −m² with (p_1+p_2)² = −Q², Q ≫ m, is not realizable with Euclidean vectors. The proof assumes an unproven multi-facet regions expansion and omits the constant π²/3. Correct: compute the four regions explicitly and tag [P] (verified at one loop): Q²I = ln²(Q²/m²) + π²/3 + t(2L² − 4L − 4 + 2π²/3) + …, t = m²/Q², L = ln(Q²/m²), exact via Φ^(1)(t,t) (Usyukina–Davydychev). Sign convention of L resolved (§2.5 item 2): with L = ln(Q²/m²) the NLP term has −4L; c_regions writes +4L with L = ln t.
- **Literature:** Reference pp. 16-17, eq. (3.3); UsyukinaDavydychev1993a PLB 298 (1993) 363.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M2, §2.5 item 2; research/c_regions/DERIVATION.md (NLP/NNLP expansion)
- **How to verify:** Re-run refdoc/work_R1/check_sudakov.py, check_sudakov2.py and research/c_regions/sudakov_regions.py. Check the reference's Table 5 at t = 1e−10 (difference 9.71e−8, reproduced only by the −4L form).

### R-M3 — Parameter vs momentum pinch conflated

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M3, reference pp. 14-15 (Thm 3.1, §3.1). The parameter-space theorem (singularities in external p) is conflated with the momentum-space trapping criterion used for reduced diagrams. Parameter pinches ≠ momentum pinches for massless graphs (Collins 2020 App D.1; cf. E14). 'Endpoints do not occur' ignores second-type singularities and endpoint singularities after partial integration. Correct: two theorems with two proofs (α-space analyticity; Gordan-type momentum criterion), as in thm:ir-landau-alpha, thm:ir-landau-momentum, rem:ir-landau-status.
- **Literature:** Reference pp. 14-15; Collins:2020euz arXiv:2007.04085, App. D.1.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M3
- **How to verify:** Compare the reference's Thm 3.1 with Collins 2020 Thms 1-3. Use the massless bubble example (E14).

### R-M4 — Wilson-line Feynman rules (Fig 4)

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M4, reference p. 11 (Fig 4). The Wilson-line rules 'vertex igv^μt^a, propagator i/(v·k ± i0), ± future/past' have no momentum routing, do not distinguish W from W†, and are inconsistent with (2.7) and the table's own last row. Correct universal rule (VF-WL-1): vertex igt^av^μ (orientation +v), propagator i/(v·ℓ + i0) with ℓ along the orientation. Past W[0,−∞n]: Π_j i/(n·(k_1+…+k_j) + i0). Future W[∞n,0]: Π_j (−i)/(n·(k_j+…+k_m) − i0).
- **Literature:** Reference p. 11, Fig 4, eq. (2.7).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M4; spec/VERIFIED_FORMULAS.md VF-WL-1
- **How to verify:** Expand P exp(ig∫_{−∞}^0 dλ n·A(λn)) with the adiabatic factor to second order and read off the rules (research/c_wilson/scripts/s1_wilson_rules.py; refdoc/work_R1/check_dirac_wilson.py).

### R-M5 — K-projection lacks i0

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M5, reference pp. 23 (3.10) and 25 (step 3 of Thm 3.14). The collinear K-projection has no i0. The pure-gauge argument is blind to it and cannot fix the Wilson-line direction; it gives 'past' only because U was based at −∞. Correct: DIS K_μν = k_μw_2ν/(k·w_2 − i0), future-pointing (Collins 2011 eq. (11.6) with errata, cf. E27); DY +i0, past-pointing. The direction is fixed by the i0 of the replaced propagators and, for DY, by the contour.
- **Literature:** Reference pp. 23-25; Collins:2011zzd eq. (11.6) with the author's errata.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M5
- **How to verify:** Derive the eikonal approximation of a collinear-to-hard attachment with its i0 for an outgoing (DIS) and an incoming (DY) line (research/c_wilson/scripts/s6_i0_poles.py).

### R-M6 — Thm 3.14 overclaimed

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M6, reference pp. 23-25 (Thm 3.14). It is stated as a theorem for general H, but proven only for H built of quark lines with colour-singlet vertices at tree level. The non-abelian background-field identification is cited; 'one Wilson line' is claimed for two quark lines; gluon-initiated H is not covered. Correct grade: abelian/tree identity [R]; all-order non-abelian [A] (lem:method-ward-multi).
- **Literature:** Reference pp. 23-25.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M6
- **How to verify:** Check the proof steps of Thm 3.14 against its stated generality. Re-run research/c_wilson/scripts/s4_ward_tree.py for the tree-level identity.

### R-M7 — Soft factor with a literal '⋯'

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M7, reference p. 26 ((3.16), Cor 3.17). The soft factor contains a literal '⋯': positions, ordering, cut and future/past are unspecified, and the 'identical proof' to Thm 3.14 ignores that the base point of soft lines is physical. Correct: precise operator definitions (reference (8.2)/(E.48)) with the i0 inherited from the replaced jet propagators: future-pointing for e⁺e⁻ and DIS final states, past-pointing for DY.
- **Literature:** Reference p. 26, (3.16), (8.2), (E.48).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M7
- **How to verify:** Read reference (3.16) and check each unspecified element against (8.2)/(E.48).

### R-M8 — Meson electroproduction: longitudinal photon only

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M8, reference pp. 1 (abstract), 7, 84. Hard exclusive meson electroproduction is listed without 'longitudinal photon'. Correct: the Collins–Frankfurt–Strikman theorem covers σ_L only (thm:excl-meson-L [A]). γ*_T has endpoint divergences (prop:excl-meson-T [V]); see R-M17.
- **Literature:** CollinsFrankfurtStrikman1997 PRD 56 (1997) 2982, arXiv:hep-ph/9611433.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M8
- **How to verify:** Read the CFS abstract and theorem statement (longitudinal photons only).

### R-M9 — Quarkonium decay graded A* instead of [A]

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M9, reference pp. 7 (Def 1.1), 75, 84 (Table 1). Inclusive quarkonium decay is graded A/A* ('as rigorous as the OPE'). Correct: the decay rate is Minkowskian at a fixed physical point, so no Euclidean continuation is available and a non-perturbative statement needs local duality. Perturbatively it is [A] (BBL; including the NRQCD cutoff dependence of f_n and ⟨O_n⟩); thm:heavy-nrqcd-decay [A].
- **Literature:** Bodwin:1994jh PRD 51 (1995) 1125 [Erratum PRD 55 (1997) 5853], arXiv:hep-ph/9407339.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M9
- **How to verify:** Compare with BBL §V-VI on the status of the decay factorization.

### R-M10 — P^±_NS differ beyond LO

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M10, reference pp. 36-37 (Prop 5.4). 'DGLAP ⟺ OPE RG' is stated with a single kernel P_qq for all n, even and odd. Beyond LO, P^±_NS = P^V_qq ± P^V_qq̄ differ: ∫_0^1 P^{V(1)}_qq̄ = 0.71931 C_F(C_F − C_A/2) ≠ 0. Correct: even-n RG ⟺ DGLAP for the C-even set (q+q̄, g); odd-n ⟺ DGLAP for q−q̄ with P^-; separate Carlson continuations (rem:pdf-ns-plusminus).
- **Literature:** Curci–Furmanski–Petronzio NPB 175 (1980) 27; Moch:2004pa (three-loop NS).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M10
- **How to verify:** Re-run refdoc/work_R2/checks/check_Pplusminus.py: integrate the CFP two-loop P^{V(1)}_qq̄ over [0,1] and compare 0.71931 C_F(C_F − C_A/2).

### R-M11 — Missing all-hard region in the two-rung ladder

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M11, reference p. 41 (Fig 24; regions used in Thms 6.3, 6.6). The two-rung ladder is said to have 'two leading regions'. The maximal all-hard region R_0, which carries the two-loop coefficient, is missing; without it (6.4) is false. Correct: three regions R_2 < R_1 < R_H (as the reference's own Ex D.48 has).
- **Literature:** Reference p. 41, (6.4), Ex D.48.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M11
- **How to verify:** Enumerate the leading regions of the two-rung ladder and check (6.4) with and without R_H.

### R-M12 — 'Combinatorics complete' overclaimed

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M12, reference pp. 39 (§6 intro), 6-7 (Def 1.1). The claims '§6 fully executes the five steps' and 'the combinatorics are complete' are overstated. The regrouping of Σ_{Γ,R}C_RΓ into T̂ ⊗ f (subtractions on hard parts only, colour projection) takes three sentences. Correct: the regrouping is an input (App D Ass D.37 (W1)(W2); D.42 for DIS) and must be stated as such.
- **Literature:** Reference pp. 6-7, 39, App D Ass D.37, D.42.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M12
- **How to verify:** Read §6 and check whether the regrouping is proven or assumed.

### R-M13 — Cut sum vs 12π Im Π not shown

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M13, reference p. 29 (Thm 4.1(ii)). It proves finiteness of 12π Im Π but never shows that the DR sum over partonic cuts (ghosts, counterterms, D-dimensional cutting rules) equals it; the interchange of ε → 0 with continuation is glossed over. Correct: thm:ee-R-finite [R, R_PT] (Laurent coefficients polynomial in L, vanishing for real L, hence identically) plus cor:ee-cuts [A] (see N24).
- **Literature:** Reference p. 29; PoggioQuinn1976; BreitenlohnerMaison1977a.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M13
- **How to verify:** See N24. Check that the reference's proof contains no step identifying the cut sum with Im Π.

### R-M14 — One-loop PDF check incomplete

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M14, reference p. 47 (Prop 7.1), the one-loop PDF 'check'. The virtual δ term is fixed by a sum rule. The ξ → 1 rapidity divergences of the Wilson-line real and virtual graphs and their cancellation in [2ξ/(1−ξ)]_+ are not shown, nor is the self-energy −½δ. Correct: prop:pdf-pqq-operator (gluon mass, every graph, gauge independence; VF-PDF-3/13/14), with f^(1) finite part (α_s/2π){P ln(μ²/m²) + C_F[−(1−ξ)(2 + ln ξ) − [2ξ ln ξ/(1−ξ)]_+ + ¼δ]}.
- **Literature:** Reference p. 47; Collins:2011zzd ch. 9.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M14; research/c_pdf/DERIVATION.md (one-loop gluon-mass PDF)
- **How to verify:** Re-run research/c_pdf/scripts/s2_oneloop_qq.py and s5b_gauge_independence.py.

### R-M15 — Thm 10.3 step (iv) formula wrong

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M15, reference p. 64 (proof of Thm 10.3, step (iv)). The printed identity f̃^unsub_A f̃^unsub_B S̃(+∞,−∞)/[S̃(+∞,−∞)S̃(+∞,−∞)] = f̃_A f̃_B, with identical arguments, gives f̃^unsub_A f̃^unsub_B/S̃, which is rapidity divergent. Correct: f̃^unsub_A(y_{P_A} − y_B) f̃^unsub_B(y_A − y_{P_B}) S̃(y_A,y_B)/[S̃(+∞,y_B)S̃(y_A,−∞)], with limits taken after combining. Inserting y_n and using linearity of ln S̃ gives (10.4).
- **Literature:** Reference p. 64, (10.4); Collins:2011zzd §13.7 (TMD definition).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M15
- **How to verify:** Read p. 64 at 200 dpi. Check rapidity-divergence cancellation using the one-loop ln S̃ linear in y_A − y_B (research/c_tmd/scripts/soft_factor.py).

### R-M16 — W+Y 'uniformly' unqualified

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M16, reference p. 64 (Thm 10.3 box): 'with the Y term the error is uniformly O((Λ/Q)^a)', stated without qualification. Correct: the standard W+Y construction needs modified cutoffs near q_T ~ Q and q_T ~ Λ (Collins–Gamberg–Prokudin–Rogers–Sato–Wang 2016, to verify). The reference itself excludes Y from its conditional theorem.
- **Literature:** Collins–Gamberg–Prokudin–Rogers–Sato–Wang 2016 (improved W+Y matching; as cited by REFDOC; not in our bib, verify on INSPIRE).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M16
- **How to verify:** Verify the CGPRSW reference on INSPIRE and read its modified W+Y prescription.

### R-M17 — Transverse-photon failure misdescribed

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M17, reference p. 71 (proof of Thm 11.4). The transverse-photon failure is described as '∫dz φ(z)/z²-type'. Correct: in the WW approximation the twist-3 integrals diverge logarithmically because g_⊥^(v)(0) = ½∫du φ_∥(u)/u ≠ 0, and there are double poles (ξ ∓ x − i0)^{−2} in the GPD convolution (Mankiewicz–Piller 2000; but see E21 for their '9/τ'). The leading-twist γ*_T → V_T amplitude vanishes to all orders by chirality/helicity (Diehl–Gousset–Pire 1999; Collins–Diehl 2000).
- **Literature:** Mankiewicz:1999tt PRD 61 (2000) 074013, arXiv:hep-ph/9905287; Diehl:1998pd PRD 59 (1999) 034023, arXiv:hep-ph/9808479; CollinsDiehl2000 PRD 61 (2000) 114015, arXiv:hep-ph/9907498.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M17; research/c_exclusive/DERIVATION.md §8
- **How to verify:** Re-run research/c_exclusive/scripts/s8_meson.py. Evaluate g_⊥^(v)(0) for φ_∥ = 6uū (= 3/2 ≠ 0) and show the log divergence.

### R-M18 — CQ/RM misreported; Collins 2007 missing

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M18, reference p. 74 (description of RM, CQ). Collins–Qiu's model is abelian, not non-abelian as the reference says. Rogers–Mulders' counterexample is a double-Sivers asymmetry with a colour-singlet hard exchange and colour factor Tr[t^at^b]Tr[t^bt^a] = T_F²(N_c²−1), against the prediction 0 from colour-traced Wilson loops; it is not a 'difference ∝ [t^a,t^b]'. Collins 2007 (unpolarized, two gluons) is not cited. Correct as in thm:break-tmd: entanglement test C_F² + 4T_F²(N²−1)/N² (N17) and the C07 anomaly (N16).
- **Literature:** CollinsQiu2007 arXiv:0705.2141; RogersMulders2010 PRD 81 (2010) 094006, arXiv:1001.2977; Collins:2007jp arXiv:0708.4410.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M18; research/c_glauber/DERIVATION.md §2
- **How to verify:** Read CQ §4 (model content) and RM's colour factor. Recompute Tr[t^at^b]Tr[t^bt^a] = T_F²(N²−1).

### R-M19 — NQS Wilson lines necessary at NNLO

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M19, reference p. 76 (NQS): 'these Wilson lines do not change the numerical result at NNLO' is wrong. Nayak–Qiu–Sterman find uncancelled NNLO poles ∝ α_s²v²/ε, generated by the gauge-completed colour-octet operators. The Wilson lines are necessary at NNLO (relative order v²); beyond NNLO new non-local operators may be needed.
- **Literature:** Nayak:2005rw PLB 613 (2005) 45, arXiv:hep-ph/0501235; Nayak:2005rt PRD 72 (2005) 114012, arXiv:hep-ph/0509021.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M19
- **How to verify:** Read NQS PLB 2005 and PRD 2005 conclusions on the gauge-completed octet operators.

### R-M20 — Two-loop phase-cancellation claim wrong

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M20, reference p. 73 (Rem 12.2): 'for one- and two-loop cross sections the phase terms cancel after the colour sum'. Correct: at one loop yes (anti-Hermitian). At two loops Catani–de Florian–Rodrigo find a Hermitian operator in P^(2) for ≥ 5 partons. Forshaw–Seymour–Siódmok: its expectation value vanishes on pure-QCD trees (one step unproven) but not with QCD+EW phases. Pure-QCD non-inclusive violation starts at three loops, with mass singularities possibly from N³LO. Guan–Herzog–Ma–Mistlberger–Suresh (2025): the violating terms appear to cancel in cross sections in pure QCD up to NNLO.
- **Literature:** Catani:2011st JHEP 07 (2012) 026, arXiv:1112.4405; Forshaw:2012bi JHEP 11 (2012) 066, arXiv:1206.6363; Guan:2024hlf JHEP 01 (2025) 090, arXiv:2408.03019.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M20; research/c_glauber/DERIVATION.md (CdFR order table)
- **How to verify:** Read the CdFR abstract/§6, FSS conclusions and GHMMS abstract for the orders quoted.

### R-M21 — BBNS status understated

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M21, reference pp. 72 (§11.3(c)), 84: 'BBNS holds at O(α_s) and LP', with B → π and B → ππ lumped as C. Correct: BBNS argued LP to all orders (two-loop IR analysis). SCET LP derivations exist (Chay–Kim 2004; Bauer–Pirjol–Rothstein–Stewart 2004, with the charming-penguin caveat). Heavy-to-light form factor = soft overlap + hard spectator is a theorem-level LP statement (BPS 2003; Beneke–Feldmann 2004); only the further factorization of ξ_π fails.
- **Literature:** BenekeEtAl2001 arXiv:hep-ph/0104110; Bauer:2004tj PRD 70 (2004) 054015, arXiv:hep-ph/0401188; Bauer:2002aj PRD 67 (2003) 071502, arXiv:hep-ph/0211069; Beneke:2003pa NPB 685 (2004) 249, arXiv:hep-ph/0311335; Chay–Kim 2004 (bib entry to be verified; refs_merged.bib's Chay:2004zn is a different paper).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M21
- **How to verify:** Read the BBNS 2000/2001 statements on all-order LP and the SCET papers. Identify the correct Chay–Kim 2004 reference on INSPIRE.

### R-M22 — Conj 12.5 is not BBL's

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M22, reference p. 76 (Conj 12.5). 'For p_T ≫ m_Q or √s ≫ m_Q, at leading velocity power' is not BBL's conjecture, and the large-p_T two-step structure is omitted. Correct: BBL conjecture all inclusive production with m_Q hard, order by order in v. At p_T ≫ m_Q there is QCD factorization into single-parton (LP) and double-parton (NLP) fragmentation (Kang–Qiu–Sterman 2012; KMQS 2014; FLMR 2012), then NRQCD for the fragmentation functions.
- **Literature:** Bodwin:1994jh arXiv:hep-ph/9407339; Kang:2011mg PRL 108 (2012) 102002, arXiv:1109.1520; Kang:2014tta PRD 90 (2014) 034006, arXiv:1401.0923; Fleming:2012wy PRD 86 (2012) 094012, arXiv:1207.2578.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M22
- **How to verify:** Read BBL's statement of the production conjecture and the KQS/KMQS abstracts.

### R-M23 — Gap observables: grade D → [C]

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M23, reference pp. 73, 84. Gap/non-global pp observables are graded D ('standard collinear factorization fails'). Correct: strict collinear factorization of amplitudes is violated [V]; SLLs exist at fixed order and are resummed; PDF factorization of gap cross sections is open, with evidence for restoration (Becher–Hager–Jaskiewicz–Neubert–Schwienbacher 2025), so the grade is [C].
- **Literature:** Becher:2024kmk PRL 134 (2025) 061901, arXiv:2408.10308; Becher:2021zkk arXiv:2107.01212; Becher:2023mtx JHEP 12 (2023) 116, arXiv:2307.06359.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M23; frontier/others/OTHERS.md §4.4-4.5
- **How to verify:** Read the BHJNS abstract (factorization restoration through Glauber gluons) and the BNSS SLL papers.

### R-M24 — Alien operators: forward on-shell caveat

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M24, reference pp. 108-109 (Lemma C.41(a)), 127 (Table 2). EOM (alien) operators are said to vanish between on-shell partonic states 'including forward', for an imprecise reason. Correct: this holds for non-zero momentum transfer or IR-regulated legs. Forward on-shell massless gluon matrix elements have known IR subtleties (the Hamberg–van Neerven 1992 puzzle; Collins–Scalise 1994; modern alien counterterms: Falcioni–Herzog 2022, Gehrmann–von Manteuffel–Yang 2023, to verify). Grade: 'proved off-forward/IR-regulated'.
- **Literature:** Hamberg:1991qt NPB 379 (1992) 143; Collins:1994ee PRD 50 (1994) 4117, arXiv:hep-ph/9403231; Falcioni:2022fdm JHEP 05 (2022) 177, arXiv:2203.11181; Gehrmann:2023ksf JHEP 04 (2023) 041, arXiv:2302.00022.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M24, S58 forbidden phrase list
- **How to verify:** Read Collins–Scalise §1 and Falcioni–Herzog §1-2 on forward on-shell matrix elements of alien operators.

### R-M25 — Spectral assumption false in the chiral limit

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M25, reference p. 118 (Ass C.56 (W2)). 'Baryon-number-1 spectrum ⊂ {p² = M²} ∪ {p² ≥ M_1²}, M_1 > M, nucleon isolated' is false in the chiral limit (massless pions: the Nπ continuum starts at M) and for m_u ≠ m_d or with QED (p and n both below threshold). Correct: state the spectral condition in the superselection sector of the target's conserved flavour numbers. Lemma C.64 needs only spec ⊂ {p² ≥ M²}; isolation is needed only for Haag–Ruelle. Massive light quarks must be stated and reconciled with massless MS-bar coefficients.
- **Literature:** Reference p. 118, Lemma C.64; Haag–Ruelle scattering theory (standard).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M25
- **How to verify:** Check the spectral claim against chiral-limit kinematics (M + m_π → M) and the p/n threshold structure.

### R-M26 — OPE literature not checked

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M26, reference pp. 88, 93, 103, 110-111, 127. The reference says there is 'no verbatim proof in the literature' of the momentum-space OPE remainder (hence its Ass C.24) and of the gauge-variant-basis statement (hence (B1)(B2)), without checking Anikin–Zav'yalov 1978 (its own ref. [116]), Zav'yalov 1990, Joglekar 1977 I+II and Hollands 2008. By uniqueness (Thm C.25(iii)) any proven momentum-space OPE with that remainder would discharge C.24. Correct: check and cite; C.24 may become a cited theorem via uniqueness; (B1)(B2) may be partly discharged (pure YM: Hollands 2008). Scope to be verified by the refs agent.
- **Literature:** Anikin:1978tj Ann. Phys. 116 (1978) 135; Zav'yalov 1990 (Kluwer); Joglekar:1976eb Ann. Phys. 108 (1977) 233; Joglekar:1976pe Ann. Phys. 109 (1977) 210; Hollands:2007zg RMP 20 (2008) 1033, arXiv:0705.3340.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M26; frontier/others/OTHERS.md §2.3, §2.7
- **How to verify:** Read the abstracts and theorem statements of the four sources for theory class and remainder form (see A09).

### R-M27 — Space-like self-energies non-integrable

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M27, reference p. 143 (Table 4 row 6) and p. 63 (Fig 39 caption). Self-energy terms of space-like regulator lines n_A(y_A) are called 'a finite term indispensable in the rapidity-regularization scheme'. Correct: they are non-integrable. n_A·k ∝ sinh(y_k − y_A) vanishes inside the real-gluon phase space, giving a 1/sinh² double pole (a length divergence). Any self-energy constant cancels identically in Collins' combination (D.22). They must be excluded, or defined by a convention used consistently in f̃^unsub and S̃.
- **Literature:** Reference pp. 63, 143, (D.22); Collins:2011zzd §10.8.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M27, §2.5 item 4; research/c_tmd/DERIVATION.md (σ = 0 'no S.I.' for space-like lines)
- **How to verify:** Write the real-emission self-energy of a space-like line in rapidity variables and show the 1/sinh²(y − y_A) non-integrability (research/c_tmd/scripts/rapidity_checks.py).

### R-M28 — MS-bar is not a finite renormalization of BPHZ

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M28, reference p. 152 (Ass D.41 (U1)): 'the passage to MS-bar is a finite renormalization (finite redefinitions of couplings and fields)'. Correct: in non-abelian theories BPHZ(L) Taylor subtractions break the Slavnov–Taylor identities. Equivalence with DR + MS-bar needs extra finite non-invariant counterterms (algebraic renormalization; Breitenlohner–Maison 1977). Graphical Ward identities then hold exactly only for DR graphs, and the compatibility of (U1) with (W1)/(Z2) is not addressed.
- **Literature:** BreitenlohnerMaison1977a CMP 52 (1977) 11 (and 39, 55); Piguet:1995er, Algebraic Renormalization, Lect. Notes Phys. m28 (1995).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M28
- **How to verify:** Read BM 1977 on non-invariant counterterms, and check whether (U1) is used in combination with the Ward identities (W1)/(Z2).

### R-M29 — Glauber-specific content of inputs undercounted

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M29, reference pp. 223 (Rem E.52(1)), 225 (Table 8 caption), 226. The claim that the App D inputs are unrelated to the Glauber region and equally needed for DIS and e⁺e⁻ → hX, with only E.33(c), E.44(a)-(d), E.33(a)(b) Glauber-specific, undercounts. Correct: (H1)(H2) for rewritten and family-summed forms carry Glauber-specific content, namely localized spectator terms vs external-endpoint distributions at n·K_i = 0 (Prop E.46 step 2) and the allocation of SA/AS endpoints between regions (E.46(c)). E.34 is DY-specific too. Count them as Glauber-specific open inputs.
- **Literature:** Reference pp. 223-226, Prop E.46, E.34.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M29
- **How to verify:** Trace where (H1)(H2) are used in Prop E.46 and whether the DIS analogue needs the same forms.

### R-M30 — Gaunt cited without the SYZ rebuttal

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M30, reference p. 229 (Rem E.55). Gaunt 2014 is cited as showing that the CSS argument fails with two Glauber gluons between spectators for hadronic E_T, without the rebuttal in the reference's own ref. [137] (SYZ 2018). Correct: contested. SYZ show pure Glauber ladders cancel for single-scale observables (including E_T and beam thrust), so the leading violation needs Glauber–soft mixing. MPI-sensitive observables remain non-factorizing, and Zeng 2015 gives an explicit counterexample for generalized factorization. See E36. Note (not a reference error): NNLO/N³LO DY agreement does not test the Glauber cancellation (partonic, no spectators; misconception M30).
- **Literature:** Gaunt:2014ska arXiv:1405.2080; Schwartz:2018obd arXiv:1801.01138; Zeng:2015iba arXiv:1507.01652.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M30, §5 S57
- **How to verify:** See E36.

### R-M31 — Rem E.54(b) ignores l_T·k_T

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M31, reference p. 228 (Rem E.54(b)). The argument '2l·k ∋ 2l^+k^-, l^+ ~ Q, so J_1 depends on k^- at scale λ²' ignores −2l_T·k_T ~ Qλ for a central jet. Correct: the relevant pinch region is Glauber relative to the pair (n_A, w_1), with k·n_A ~ k·w_1 ~ λ² and k_T nearly orthogonal to w_1T. There J_1 depends on k^- at scale λ², so the conclusion survives.
- **Literature:** Reference p. 228.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M31
- **How to verify:** Re-run refdoc/work_R8/check_kinematics.py. Expand (l + k)² for a central jet with k in the stated Glauber scaling.

### R-M32 — Method is Aybat–Sterman 2009 (uncited)

- **Kind:** correction_of_reference_doc
- **Statement:** ERR-M32, reference pp. 162-230 (all of App E; bibliography); an attribution correction. The method — hybrid LCPT (x^+ for one jet, x^- for the other), pinch replaced by a mismatch of deformation directions, FSI phases cancelled by unitarity — is that of Aybat–Sterman (2009), which is not cited anywhere. Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016 (LCPT for single and double DY) is not compared. Correct: credit Aybat–Sterman 2009 and DGOPS 2016 as precedents. The phrase 「Glauber 相消的方法是 Collins (2011) 首创的光锥序处理」 is forbidden.
- **Literature:** AybatSterman2009 PLB 671 (2009) 46, arXiv:0811.0246, eq. (14); Diehl:2015bca JHEP 01 (2016) 076, arXiv:1510.08696, §4.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-M32, §5 S58; research/c_glauber/DERIVATION.md §1.5-1.6
- **How to verify:** Read Aybat–Sterman 2009 (4 pp.) and compare its method with reference App E. Read DGOPS 2016 §4.

### R-m01 — Minor corrections m1–m5

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m1 to m5. m1 (pp. 16-17): the 'hard point (α_k = 0, all lines off shell)' is listed as a Landau solution but is the absence of a pinch; the soft-quark corners k = p_1, −p_2 are omitted. m2 (p. 25, Rem 3.15): U(+∞) is a field-dependent operator, not a constant colour matrix; the conclusion holds via W[w,∞]W[∞,0] = W[w,0]. m3 (p. 23): the original Grammer–Yennie K-photon is the symmetric b_k k_μk_ν; the one-sided form with i0 is Collins' adaptation. m4 (pp. 13-14, Prop 2.4): positivity of the unrenormalized PDF is formal (UV divergent); the light-cone-gauge proof inherits the 1/k^+ ambiguity; the anticommutator ∝ δ(w^-)δ²(0) is a divergent constant; renormalized support is not addressed. m5 (pp. 6, 12): (1.1) has an absolute remainder and schematic σ̂; ν = P·q clashes with the Lorentz index; grade C mixes [P] and [C].
- **Literature:** GrammerYennie1973 PRD 8 (1973) 4332 (original via Sen–Indumathi–Choudhury arXiv:1812.06468, eqs. (7)-(9)); Collins:2011zzd ch. 10-11.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m1 to m5; research/c_wilson/DERIVATION.md (GY attribution)
- **How to verify:** m3: read GY 1973 (original not seen by our agents). Others: read the cited reference pages.

### R-m06 — Minor corrections m6–m12

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m6 to m12. m6 (p. 34, Ex 5.2): for the T_2 structure γ^{μ1} is a vertex γ and k̸ supplies the derivative; q̸ feeds T_1 and gauge terms. m7 (p. 32): the duality-violation example e^{−c√s/Λ}sin(…) is non-standard (instanton models give power-damped oscillations; resonance models e^{−δ−γs}sin(α+βs)). m8 (p. 49, Rem 7.5): 'α_s^n ln^{2n−1}(1−z)' should be α_s^n[ln^{2n−1}(1−z)/(1−z)]_+ ⟷ α_s^n ln^{2n}N. m9 (p. 49 vs 12): τ = Q²/ŝ vs Q²/s. m10 (pp. 39-40): the colour projection Tr_c[HJ] ≃ (1/N_c)Tr_cH Tr_cJ is missing. m11 (p. 29): 'a_n has degree n−1' holds for n ≥ 1; the degree of Π is max(1,n). m12 (p. 49, Prop 7.4): the finite parts of c_q, C_{2,g} are quoted, not derived; the gluon-average 1/(D−2) convention, DIS scheme and F_L are not mentioned.
- **Literature:** Shifman 2000 (hep-ph/0009131) for duality-violation models; Vermaseren–Vogt–Moch NPB 724 (2005) 3.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m6 to m12
- **How to verify:** m8: Mellin-transform [ln^k(1−z)/(1−z)]_+ to get ln^{k+1}N leading behaviour. m11: check against the RG structure of Π (research/c_ee/rg_structure.py). Others: read the pages.

### R-m13 — Minor corrections m13–m16 (incl. OUR-5)

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m13 to m16. m13 (p. 56, Fig 34): 'the square of (e) diverges…' is gauge dependent. In Feynman gauge 2Re(M_dM_e*) also has the 1/t pole (t|M_e|² → −80, t·2Re → +33.6, sum ∝ P_qg); only in an axial gauge does it come from |(e)|² alone. m14 (p. 67): no Hermitian conjugation is needed for the vector bilinear; the colour bookkeeping t^a → t^{a*} reverses path ordering; ε_T^{12} sign unstated (Trento: +1). m15 (pp. 68-69): the (11.2) remainder O(Λ²/Q⁴) should be O((Λ²/Q⁴)ln(Q²/Λ²)). m16 (pp. 53-71): (9.3) omits (2π)²; χ(b) as written is IR divergent; Rem 9.6 'no Glauber region in DIS' holds only for unphysical ω; the small-b remainder O(b_TΛ) should be O((b_Tm)²) for unpolarized TMDs (to verify; our spec copied O(b_Tm), OUR-5); Fig 46 omits −1 < x < −ξ; f_π is an older PDG value.
- **Literature:** BacchettaEtAl2004 (Trento conventions) PRD 70 (2004) 117504, arXiv:hep-ph/0410050; Collins:2011zzd §13.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m13 to m16, OUR-5
- **How to verify:** m13: re-run refdoc/work_R3/scripts/qg_feynman_gauge.py. m14: refdoc/work_R3/scripts/pt_bilinear.py. m16: check the twist-4 order of the small-b OPE of unpolarized TMDs.

### R-m17 — Minor corrections m17–m22

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m17 to m22. m17 (p. 73, (12.2)): T_coll is undefined; it must be T_2, the charge of the collinear parton with negative momentum fraction, and genuine colour correlations need ≥ 4 coloured partons. m18 (pp. 77-78, Rem 13.2): LO SCET rules already give the future-pointing line for outgoing collinear quarks, the direction being fixed by external states; the λ²Q mode is ultrasoft, not soft. m19 (p. 81, Prop 14.1): labelled 命题 but only argued; the proven renormalon case is the large-N O(N) σ-model (David; NSVZ; Beneke–Braun–Kivel 1998). m20 (p. 83): 'twist parity = chirality' holds only for symmetric traceless operators (false for transversity). m21 (p. 72, (12.1)): σ̂_{ab→c} must be the invariant E_c dσ̂/d³p_c (1/z² = Jacobian). m22 (pp. 231-238): bibliography issues ([27], [34], [53], [54], [56], [59], [60], [139]); misattributions [53], [60] (= R-M18, R-M19); missing key references (Collins 2007, Aybat–Sterman 2009, Mitov–Sterman 2012, Becher et al. 2025, KQS 2012, NQS PLB 2005, BBNS 2000, Nachtmann 1973).
- **Literature:** Beneke1999 Phys. Rep. 317 (1999) 1, arXiv:hep-ph/9807443 (renormalon review); Beneke–Braun–Kivel 1998, David, NSVZ (as cited by REFDOC; not in our bib, verify); Mitov:2012gt PRD 86 (2012) 114038, arXiv:1209.5798.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m17 to m22
- **How to verify:** m19: verify the Beneke–Braun–Kivel reference and the David/NSVZ sources on INSPIRE. m22: compare the reference bibliography with INSPIRE (refdoc/work_R4/bibcheck.py).

### R-m23 — Minor corrections m23–m25

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m23 to m25. m23 (pp. 101-102, Ex C.27): the result is −κπ²/(2q⁴) + O(m²q^{−6}ln q), not 'O(q^{−4}ln q²)' (see N15). m24 (pp. 91-123): Fig 55 has cubic vertices outside the stated model; Cor C.18 needs ω for disconnected γ; routing compatibility for frozen q is omitted; the 1D-slice edge-of-the-wedge step in Lemma C.64 needs Q²-smearing; ||γ|| ≤ Cα needs rescaling for mass-mixing entries. m25 (pp. 141-158): Lemma D.20 is misinvoked for DIS (Prop D.28(a)). Table 5's fit '2λ²L² − 3.9λ²L' should be t(2L² − 4L − 4 + 2π²/3), and Table 5 compares I with L² + π²/3 written in Q², not with (D.32) in Q̃² = 2PP′, so it does not test the Collins remainder (see N12). The C_S k^+ integral is a Beta function, not J(ε). There is an edge case in Lemma D.23(iii), and a typo '假设假设'.
- **Literature:** Reference pp. 91-158, Table 5, (D.32).
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m23 to m25
- **How to verify:** Re-run refdoc/work_R5/scripts/check1.py, refdoc/work_R6/check_triangle_numerics.py and refdoc/work_SYN/triangle_remainder.py.

### R-m26 — Minor corrections m26–m27

- **Kind:** correction_of_reference_doc
- **Statement:** Minor corrections ERR-m26 and m27. m26 (pp. 162-195): the Lemma E.28(iii) proof gap is fixable by closing in the LHP, ∫ER_↓ = −iΣr_iE(z_i), |E(z_i)| ≤ 2Mλ_J/|z_i|². The window-shape claim needs K_{1,2} ≤ Λ/2, with error O(λ_J/min K). The vertex sign '−igJ^{+a}' should be +ig with the reference's own D_μ. (E.30) should be absolute, not relative; δ is reused; E.18(iii) is provable; Θ(−k_T) = Θ(k_T) is needed. m27 (pp. 198-223): Rem E.49(2) sign wording (the compensating term is +¼C_Aχ²X); σ is missing in Im(n·K) = tσΣf_a; Def E.39 'k^- does not move at Θ′ < 1' is inaccurate; w_12 also depends on k_T1²/k_T2²; the Prop E.35 boundary-layer estimate may fail for endpoints set by other N_R′ (plausible); Rem E.52(1) 'complete' should read 'up to (H1)(H2)' for TMD.
- **Literature:** Reference pp. 162-223.
- **Source:** refdoc/REFDOC_ANALYSIS.md ERR-m26, m27
- **How to verify:** Re-run refdoc/work_R7/check_e28.py, check_e28_asym.py, check_e20.py, check_e31.py and refdoc/work_R8/check_colour.py.

### R-OUR1 — INTERNAL: errors in our spec OUR-1–OUR-4

- **Kind:** correction_of_reference_doc
- **Statement:** [INTERNAL: corrections of OUR OWN spec found by the reference readers; the reference is not in error here; recorded so that the printed physics statements are checked.] OUR-1: the FF prefactor 1/(4N_cz) 'in the frame with p_hT = 0' gives z^{−2} × the correct O(α_s) number density, which the free-quark δ(1−z) check cannot detect. Correct: in the hadron frame the prefactor is z^{1−2ε}/(4N_c) = z^{d−3}/(4N_c) (Collins–Soper 1982; Collins 2011 ch. 12), with Jacobian d^{2−2ε}p_hT = z^{2−2ε}d^{2−2ε}k_T. In the parton frame, 1/(4N_cz) goes with an explicit ∫d^{2−2ε}p_hT. It reproduces (α_s/2π)C_F(1+z²)/(1−z) dl_T²/l_T². OUR-2: the 'key compatibility property… induction' for thm:method-subtraction is the naive termwise argument refuted by reference Ex D.1/D.48; restate as a precise conditional theorem. OUR-3: for hadrons the Euclidean OPE informs only on |ω| ≤ √3M/Q; use the Thm C.50/Lemma C.64 route. OUR-4: prop:method-glauber-deformation needs the simultaneous two-component deformation along e_G = n_B − n_A; one component leaves |k^+k^-| ~ λ³.
- **Literature:** Collins–Soper NPB 194 (1982) 445; Collins:2011zzd ch. 12; reference Ex D.1, D.48, Lemma D.20(b), (E.42), Thm C.50, Lemma C.64.
- **Source:** refdoc/REFDOC_ANALYSIS.md §2.4 OUR-1 to OUR-4; spec/VERIFIED_FORMULAS.md VF-CONV-17 audit correction (line 181); spec/FINAL_OUTLINE.md def:pdf-ff
- **How to verify:** OUR-1: re-run refdoc/work_R1/check_ff_norm.py; derive the boost Jacobian k_T = −p_hT/z. OUR-4: check the amplitude bound κ ~ k_T²/|k^±| from Lemma D.20(b) with one deformed component.

### R-OUR2 — INTERNAL: errors in our spec OUR-5–OUR-8

- **Kind:** correction_of_reference_doc
- **Statement:** [INTERNAL: corrections of OUR OWN spec, continued.] OUR-5: prop:tmd-small-b remainder 'O(b_Tm)' (copied from the reference) should be O((b_Tm)^p), with p = 2 for unpolarized leading-twist TMDs (twist 4); to verify; see R-m13 (ERR-m16). OUR-6: the distinction that remainder bounds on a real ω-segment do not continue to the discontinuity is absent from lem:disall-fsi and thm:disall-factorization; two routes (S27). OUR-7: refs_merged.bib Shifman2000 booktitle should be 'At the Frontier of Particle Physics' (World Scientific 2001), vol. 3, pp. 1447-1494, not '8th International Symposium on Heavy Flavor Physics'. OUR-8: thm:dis-moments/thm:dis-ope: the forward on-shell partonic statement is at exceptional momenta and is not covered by the Euclidean theorem; separate sub-statements with separate tags.
- **Literature:** Shifman hep-ph/0009131 (INSPIRE record); reference ERR-m16.
- **Source:** refdoc/REFDOC_ANALYSIS.md §2.4 OUR-5 to OUR-8
- **How to verify:** OUR-5: check the twist counting of the small-b OPE of f_1 (first correction O(b_T²)). OUR-7: query INSPIRE for hep-ph/0009131. OUR-6, OUR-8: read the spec statements against S19, S27.

## 6. Delicate attribution claims (28)

### A01 — Author list of NPB 964 (2021) 115311 misquoted

- **Kind:** attribution
- **Statement:** Author list of the hybrid-renormalization paper (the paper in E01). LAMET.md cites it as 'Ji, Liu, Liu, Zhang, Zhao et al., NPB 964 (2021) 115311'. The INSPIRE author list is X. Ji, Yizhuang Liu, A. Schäfer, W. Wang, Y.-B. Yang, J.-H. Zhang, Y. Zhao. 'Ji, Liu, Liu, Zhang, Zhao' is the author list of the RMP review (X. Ji, Yu-Sheng Liu, Yizhuang Liu, J.-H. Zhang, Y. Zhao). The PLB 811 citation 'Ji, Liu, Liu' (LAMET line 101) is correct (X. Ji, Yizhuang Liu, Yu-Sheng Liu).
- **Literature:** Ji:2020brr NPB 964 (2021) 115311, arXiv:2008.03886; Ji:2020ect RMP 93 (2021) 035005, arXiv:2004.03543; Ji:2019ewn PLB 811 (2020) 135946, arXiv:1911.03840.
- **Source:** frontier/lamet/LAMET.md line 89 (§0.3 item 1), line 101
- **How to verify:** Query INSPIRE for 'arxiv:2008.03886' and 'arxiv:2004.03543' and compare the author lists. Correct LAMET.md line 89.

### A02 — Identity of Yizhuang Liu; Chinese-name conflict

- **Kind:** attribution
- **Statement:** Identity of 'Yizhuang Liu' (REQUIREMENTS). INSPIRE author record 1981577, BAI Y.Liu.90, ORCID 0000-0002-0897-1165. The BAI search gives 73 literature items (July 2014 – Sept 2026); the name search gives 72, the BAI adding the APPB lecture notes with author string 'Liu, Y.'. LAMET.md's '72 records' is the name-search count. Three other INSPIRE stubs 'Liu, Yizhuang' (Y.Liu.28, .38, .68) are different people and were excluded. Career (habilitation summary cross-checked with INSPIRE affiliations): B.Sc. USTC 2012; Ph.D. Stony Brook 2018 (advisor I. Zahed); postdoc TDLI/SJTU 2018-2020; Regensburg 2020-2021; Jagiellonian University (adiunkt) since 2021. Habilitation 2023 on [H1]-[H7] = Ji:2021znw, Ji:2020brr, LatticeParton:2020uhz, Ji:2020ect, Ji:2019ewn, Ji:2019sxk, Ji:2023pba. Awards: Silsbee Prize 2016, Rector's Award 2022. The Chinese name is UNVERIFIED and must not be printed. Conflict in our material: LAMET.md line 9 (Chinese abstract) writes 刘义壮, while YZLIU.md line 857 (draft chapter title) and FINAL_OUTLINE.md line 137 (proposed Ch24 title) write 刘一壮. Personal identifiers in the habilitation summary must not be reproduced.
- **Literature:** INSPIRE author record 1981577 (BAI Y.Liu.90); ORCID 0000-0002-0897-1165; habilitation summary (local file; contains personal data, do not quote).
- **Source:** frontier/yzliu/YZLIU.md §1.1-1.3, line 857 (§6.1); frontier/lamet/LAMET.md line 9, §11; spec/FINAL_OUTLINE.md line 137 (§0.9 item 1)
- **How to verify:** Re-query INSPIRE (BAI Y.Liu.90) for the record count. For the Chinese name, search authoritative sources (institutional pages, Chinese-language publications or talks); until confirmed, delete both renderings from LAMET.md and the proposed Ch24 title. Do not use the habilitation summary for anything but professional data.

### A03 — Liu-programme priority claims

- **Kind:** attribution
- **Statement:** Priority ('first') claims for the Liu programme, which the frontier chapter would print. (A1) First representation of the Collins soft factor as a time-independent matrix element (HQET form factor of a QQ̄ pair); earlier 'bent' Euclidean soft functions have the wrong cusp beyond one loop. (A3) First systematic analytic-continuation framework connecting all off-light-cone soft functions; Table 2, three universality classes of which only Ψ and f^TMD have Euclidean realizations, is new. (A5) The intrinsic soft function S_I as a concept and 𝒟 = 2𝒟_1 − 𝒟_2. (A6) First explicit all-order argument that the DY soft factor in the exponential regulator is time-ordering insensitive and equals a single-time-ordered form factor; earlier uses in finite-LF-length/δ regulators: Vladimirov 2016/2017. (B1) First matching formula between a lattice-computable quasi-TMD and the scheme-independent TMDPDF with a Euclidean-computable soft factor; the single-line power-counting formula is new. (C2) First threshold factorization/resummation of LaMET kernels, with universality of the heavy–light Sudakov kernel. (D1) First exactly worked marginal (asymptotically free) theory, the 2D U(N) Gross–Neveu model at O(1/N), with a derived and pointwise-convergent twist expansion, for λ ∈ iℝ≥0 only (F_2, F_3 'similar'). (LAMET §11) Liu's 2D results are 'the only places where the twist expansion is established non-perturbatively to all powers'. (I.5) LPC 2020 as the 'first lattice extraction of S_I and the CS kernel': for the CS kernel this conflicts with the earlier Shanahan–Wagman–Zhao (arXiv:2003.06063, March 2020; LPC arXiv:2005.14572, May 2020).
- **Literature:** Ji:2019sxk NPB 955 (2020) 115054; Liu:2022nnk APPB 53 (2022) 4-A2; Liu:2023pjb JHEP 09 (2024) 030, arXiv:2312.05957; Ji:2019ewn arXiv:1911.03840; Ji:2023pba arXiv:2305.04416; Liu:2024omb JHEP 09 (2024) 093, arXiv:2403.06787; LatticeParton:2020uhz PRL 125 (2020) 192001, arXiv:2005.14572; Shanahan:2020zxr PRD 102 (2020) 014511, arXiv:2003.06063; Vladimirov:2016dll PRL 118 (2017) 062001; Vladimirov:2017ksc JHEP 04 (2018) 045; Ji:2014hxa; Ebert:2019okf.
- **Source:** frontier/yzliu/YZLIU.md §3 'Novelty' paragraphs (lines 186, 266, 332, 380, 442, 588), §3.D1 (line 666), §1.3 row I.5; frontier/lamet/LAMET.md §11
- **How to verify:** For each claim, run INSPIRE searches for earlier work (e.g. 'Collins soft factor Euclidean', 'threshold resummation quasi-PDF', 'Collins-Soper kernel lattice' before 2020-05). Phrase I.5 as 'first lattice extraction of S_I' and cite SWZ 2020 for the CS kernel unless a narrower 'first' (e.g. dynamical fermions) is verified.

### A04 — Liu-programme proof-status attributions

- **Kind:** attribution
- **Statement:** Proof-status attributions for the Liu programme. (i) Liu's self-assessment (APPB §6): 'all the proofs in the paper, except the ones for the analyticity, follow the typical rigorous standards in the TMD factorization literature'. The PLB version is explicitly only a 'sketch of mathematical proof'. (ii) Independent confirmations of quasi-TMD factorization: Vladimirov–Schäfer 2020 (SCET, one loop); Ebert–Schindler–Stewart–Zhao 2022 (all-order, via a Large-Rapidity scheme; no flavour mixing); NNLO del Río–Vladimirov 2023 and Ji–Liu–Su 2023. JLL's leading-region analysis is a sketch with 'details to a future publication'. (iii) The multiplicative-renormalizability proofs used are not by Liu. (iv) Liu notes that Collins–Soper 1981 give no detailed explanation of rapidity-divergence factorization beyond one loop; it agrees with Vladimirov's conformal-map proof. Vladimirov 2018 calls SIDIS soft-factor rapidity factorization 'the open question'. (v) Dividing out staple self-interactions goes back to Collins 2008 (PoS LC2008) and Ji–Jin–Yuan–Zhang 2019; A2 supplies the all-order justification. (vi) APPB's ultrasoft wording ('beyond three loops', 'α_s⁴', 'from the 3-loop level') refers to one ADM-type effect; do not print an exact loop order. (vii) N_m = C_Fe^{5/6}/π ≈ 0.977 beyond large β_0 is conjecture (2.52) [C]. (viii) The time-ordering theorem is conditional on DR analyticity [A]; DY = SIDIS is [P]. (ix) Liu states that collinear factorization 'strictly speaking, has no exact derivation up to now'. (x) Y6's 'super-renormalizable' remark is ours (LAMET); Y7 (instantons) is unpublished.
- **Literature:** Liu:2022nnk §3.3, §6; Ji:2019ewn; Vladimirov:2020ofp PRD 101 (2020) 074517, arXiv:2002.07527; Ebert:2022fmh JHEP 04 (2022) 178, arXiv:2201.08401; delRio:2023pse PRD 108 (2023) 114009, arXiv:2304.14440; Collins:1981uk NPB 193 (1981) 381; Vladimirov:2017ksc arXiv:1707.07606; Collins:2008ht PoS LC2008 028, arXiv:0808.2665; Ji:2018hvs PRD 99 (2019) 114006, arXiv:1801.05930; Liu:2023onm eq. (2.52); Liu:2024omb §1; Ji:2018waw; Liu:2021evw arXiv:2102.07248.
- **Source:** frontier/yzliu/YZLIU.md §3.A2(b),(c), A4 (line 296), A6 (line 380), B1 (lines 437-439), C4, D1, line 743, line 816; frontier/lamet/LAMET.md §10.2(A), §11 Y6-Y7
- **How to verify:** Read the quoted passages: APPB §6 and §3.3, PLB 811 below eq. (22), Liu 2024 §3.1 and App. C, and the Vladimirov 2018 quote as reproduced in Liu 2024. Check the INSPIRE status of Liu:2021evw (unpublished).

### A05 — LaMET attributions

- **Kind:** attribution
- **Statement:** LaMET attributions. (i) Exponential decay of space-like correlators from locality (Thm 7.1): Ji–Liu–Su 2026, building on Fredenhagen 1985 (cluster theorem); all-order spectral representation in φ³/φ⁴ 'proven'; for QCD [A]/[C]. (ii) Two routes to the quasi-PDF matching theorem: IJJSZ 2018 via the coordinate-space OPE; Ma–Qiu (arXiv 2014, published 2018) via collinear factorization. The RMP says the proof is given only for perturbative free-quark states. Ji 2014 asserted that the factorization 'can be proved order by order as in the renormalization program' without giving the proof. (iii) Multiplicative renormalizability: JZZ 2018 (auxiliary heavy field; the space-like extension of the HQET/BRST argument is asserted); GJS 2018; IMQY 2017 (superficial degree counting, not full BPHZ). Braun–Chetyrkin–Kniehl 2020: space-like = time-like anomalous dimensions (three loops / all orders, Thm 3.2). (iv) Support property (Prop 1.4): Radyushkin 1983 (cited from recall). (v) Threshold factorization (JLS 2023): two constants (c_a, c_H) were extracted from the NNLO comparison with 41 singular terms, c_H = 0.0725C_F² − 0.0840C_FC_A + 0.1453C_Fn_fT_F; del Río–Vladimirov confirm H. (vi) Lattice CS kernel: Avkhadiev–Shanahan–Wagman 2024 claim 'first such determination with systematic control of quark mass, operator mixing, and discretization effects'.
- **Literature:** Ji:2026vir arXiv:2601.12189; Fredenhagen:1984bz CMP 97 (1985) 461; Izubuchi:2018srq arXiv:1801.03917; Ma:2014jla PRD 98 (2018) 074021, arXiv:1404.6860; Ma:2017pxb PRL 120 (2018) 022003; Ji:2014gla Sci. China 57 (2014) 1407, arXiv:1404.6680; Ji:2017oey arXiv:1706.08962; Green:2017xeu arXiv:1707.07152; Ishikawa:2017faj arXiv:1707.03107; Braun:2020ymy JHEP 07 (2020) 161, arXiv:2004.01043; Radyushkin:1983wh PLB 131 (1983) 179; Ji:2023pba arXiv:2305.04416; delRio:2023pse arXiv:2304.14440; Avkhadiev:2024mgd PRL 132 (2024) 231901, arXiv:2402.06725.
- **Source:** frontier/lamet/LAMET.md §1.3 (Prop 1.4), §2.1, §3.1-3.5, §4, §6.1 (lines 940-948), §7.1, §10.2 (line 1287)
- **How to verify:** Read Ji:2026vir §7.1 and Fredenhagen 1985. Read Ji 2014 for the quoted assertion, the RMP statement on free-quark states, BCK 2020's scope (three loops vs all orders) and Radyushkin 1983 (support; currently recalled). Check that JLS state c_a, c_H were fitted.

### A06 — Literature-absence claims; unrefereed preprints

- **Kind:** attribution
- **Statement:** Literature-absence claims ('no proof/no paper exists'), each based on the searches stated. (1) No Zimmermann-level OPE proof for space-like Wilson-line operators (LaMET node N4). (2) No dedicated Glauber analysis for quasi-TMDs or finite staples (title searches, Oct 2026). (3) No N³LO quasi-PDF matching kernel. (4) No published refutation of the resolution of the Rossi–Testa critique. (5) The Rothstein–Stewart SCET factorization proof including ℒ_G (announced) has not appeared. (6) No BBNS endpoint refactorization. (7) No all-order proof of twist-3 SSA factorization. (8) No self-contained flow-equation proof of the OPE for QCD with quarks (INSPIRE 'flow equation + QCD/fermion'; explicitly 'not verified'). (9) No proof of the multilocal BRST classification. (10) Whether Gordan's theorem was already identified in the Landau-equation literature is unchecked (N02). (11) DGOPS 2016: Glauber cancellation established only for Drell–Yan among single hard processes. Status of preprints: Collins 2020, Fröb–Holland 2016, Beneke–Schnubel–Szafron 2026, Gamberg et al. 2022 and Bodwin et al. 2025 are unrefereed (†).
- **Literature:** Rossi–Testa critique as cited in LAMET §8.4; Rothstein:2016bsq arXiv:1601.04695; Diehl:2015bca arXiv:1510.08696 §1, §3.5; Collins:2020euz arXiv:2007.04085; Frob:2016mzv arXiv:1603.08012; Beneke:2026miy arXiv:2608.25502; Gamberg:2022lju arXiv:2211.13209; Bodwin:2025zzi arXiv:2512.11647.
- **Source:** frontier/lamet/LAMET.md §4.5, §8.4, §13, §14; frontier/others/OTHERS.md §0 items 1-2, §2.7, §8.3, §14.3; research/survey/SURVEY.md §3.3, item 8; research/c_scet/DERIVATION.md §5
- **How to verify:** Repeat INSPIRE searches before printing each claim, e.g. 'quasi-TMD Glauber', 'N3LO quasi-PDF', 'Rossi Testa', 'flow equation QCD quarks OPE', 'Rothstein Stewart Glauber factorization proof'. Re-check the journal status of each † preprint on the publication date.

### A07 — GPDs at x = ±ξ: Braun 2024 vs Su et al. 2026

- **Kind:** attribution
- **Statement:** GPDs near x = ±ξ in LaMET. Braun 2024 (renormalon analysis): at x = ±ξ the non-perturbative corrections to quasi-GPDs are suppressed by only the first power of the hard scale, from soft momenta, 'nothing to do with the known UV renormalon'. Su–Ji–Liu–Zhang 2026: the logs ln(4P_z²(x±ξ)²/μ²) in the one-loop kernel come multiplied by |x±ξ|, so 'there is no leading-twist contribution from the soft scales'. Their reanalysis of four lattice data sets gives GPDs continuous at x = ±ξ (with the regulator ordering ε_2 ≪ |ε_1| → 0); earlier discontinuities 'may arise from regulator-related numerical artifacts'. LaMET's assessment: the two are not strictly contradictory (no leading-twist soft term vs a power correction enhanced to 1/P^z). Together with Braun 2023's kinematic twist-3 discontinuities, the status is [C].
- **Literature:** Braun:2024snf PRD 109 (2024) 074510, arXiv:2401.08012 (abstract); Su:2026eta arXiv:2609.20545; Braun:2023alc JHEP 10 (2023) 134, arXiv:2308.04270; Collins:1998be (DVCS soft region).
- **Source:** frontier/lamet/LAMET.md §9.1 (lines 1140-1150); frontier/yzliu/YZLIU.md §3 (GPD at x = ±ξ, lines 636-646)
- **How to verify:** Read Braun 2024 in full (only the abstract was read) and Su et al. 2026 §§2-4. Check whether either paper claims the other is wrong.

### A08 — Status of Collins 2020 (preprint only)

- **Kind:** attribution
- **Statement:** Status of Collins 2020 (arXiv:2007.04085, 'Landau equations and the Coleman–Norton theorem'). Only v1 (8 Jul 2020, 39 pp.) exists, with no journal publication as of 2026-10-10 (arXiv and INSPIRE checked); Mühlbauer 2020 (arXiv:2011.10368, momentum-space Landau equations via isotopy, including second-type singularities) is likewise unpublished. OTHERS grades Collins' Thm 1 [R]† (with sign condition (8.15)) and [C] without (8.15); Collins himself flags his conditions (a),(b) as artefacts of the method. FINAL_OUTLINE §0.9 item 4 does not adopt the OTHERS [R]† grade (decision D3: the conservative survey/critic verdicts bind), so the monograph cites it as a preprint.
- **Literature:** Collins:2020euz arXiv:2007.04085 (Thm 1, Sec. VIII B, eq. (8.15)); Muhlbauer:2020kut arXiv:2011.10368.
- **Source:** frontier/others/OTHERS.md §1.2, §1.7; research/survey/SURVEY.md item 4 (lines 192-193), §3.1 item 2; spec/FINAL_OUTLINE.md §0.9 item 4
- **How to verify:** Re-check arXiv versions and INSPIRE journal status for 2007.04085 and 2011.10368 at print time. Confirm the grade decision with the lead author.

### A09 — Rigour status of the OPE

- **Kind:** attribution
- **Statement:** Rigour status of the OPE. (1) Zimmermann proved the OPE in renormalized PT for scalar theory; for QCD with quarks the standard sources assert it carries over (Collins 1984 §12.8: 'proved… the same way') or 'widely assume' it (IJJSZ 2018). (2) Hollands 2008 (RMP 20, 1033): perturbative YM on globally hyperbolic spacetimes; the OPE closes on gauge-invariant operators. This is pure YM only; matter fields are only discussed (Sec. 5.1, chiral-fermion anomalies). (3) Fröb–Holland arXiv:1603.08012 (unpublished): OPE existence for massless renormalizable theories (Thm 1); BRST Ward identity for OPE coefficients provided H^{1,4}_{E(4)}(ŝ|d) = 0, which holds for pure YM 'but not, for instance, in the presence of chiral fermions in non-real representations' (Thm 2). The bounds used (FHH 2016) are pure-YM only, so [R]†. (4) OPE convergence at finite distance is proven only for φ⁴_4 at fixed loop order: Hollands–Kopper CMP 313 (2012) eq. (7), massive; Holland–Hollands–Kopper CMP 342 (2016), massless. (5) Anikin–Zav'yalov 1978's theory class is UNVERIFIED. The OTHERS grade 'QCD OPE [R] in PT via classical results' is not adopted by FINAL_OUTLINE §0.9 item 4.
- **Literature:** Zimmermann (Brandeis 1970 lectures); Collins, Renormalization (CUP 1984) §12.8; Izubuchi:2018srq; Hollands:2007zg RMP 20 (2008) 1033, arXiv:0705.3340; Frob:2016mzv arXiv:1603.08012; Hollands:2011gf CMP 313 (2012) 257, arXiv:1105.3375, eq. (7); Holland–Hollands–Kopper CMP 342 (2016) 385; Anikin:1978tj Ann. Phys. 116 (1978) 135.
- **Source:** frontier/others/OTHERS.md §2.1-2.7; research/survey/SURVEY.md item 1 (lines 101-124), §3.1 item 1; spec/FINAL_OUTLINE.md §0.9 item 4
- **How to verify:** Read Hollands 2008 §5.1, FH 2016 §1.1 (Thms 1-2) and the HK 2012 abstract and eq. (7). Look up the exact bibliographic data of Zimmermann's Brandeis lectures and of Holland–Hollands–Kopper 2016 on INSPIRE. Read Anikin–Zav'yalov for the theory class.

### A10 — Method of regions: who proved what

- **Kind:** attribution
- **Statement:** Method of regions: who proved what. (1) Euclidean large-momentum/large-mass limits: rigorous (Smirnov CMP 134 (1990) 109; content via secondary summaries). (2) Jantzen 2011: a conditional general derivation; the gap is the convergence of the summation exchange (identity [R](cond.), applicability [P]). (3) Semenova–Smirnov–Smirnov 2019: proven at leading order for each facet and to all orders for one facet (positive polynomials); general case [C]. (4) Gardi–Herzog–Jones–Ma 2022 (on-shell expansion; commutativity, Thm 4). 'Regions = lower facets' is [V] in Minkowski kinematics (GHJM 2024, abstract only). Becher–Hager–Jaskiewicz–Neubert–Schwienbacher 2025: a three-loop active–active Glauber region missed by automated region finders. (5) Attribution correction (c_regions §4 item 2): the off-shell Sudakov regions example is not from Beneke–Smirnov 1998, who introduced the method for threshold expansion. The example is in Becher–Broggio–Ferroglia 2015 §2.2; the massive-exchange version is in Jantzen 2011 §6 and BBF §2.3.
- **Literature:** Smirnov:1990rz CMP 134 (1990) 109; Jantzen2011 JHEP 12 (2011) 076, arXiv:1111.2589, §6, eqs. (6.26)-(6.30); Semenova:2018cwy EPJC 79 (2019) 136, arXiv:1809.04325; Gardi:2022khw JHEP 07 (2023) 197, arXiv:2211.14845; Gardi:2024axt JHEP 08 (2024) 127, arXiv:2407.13738; Becher:2024kmk PRL 134 (2025) 061901, arXiv:2408.10308; BenekeSmirnov1998 NPB 522 (1998) 321, arXiv:hep-ph/9711391; BecherBroggioFerroglia2015 Lect. Notes Phys. 896, arXiv:1410.1892, §2.2-2.3, eqs. (2.39)-(2.52).
- **Source:** frontier/others/OTHERS.md §3.1-3.6; research/c_regions/DERIVATION.md §4 item 2; research/survey/SURVEY.md (MoR item)
- **How to verify:** Read BS 1998 §1-2 (threshold expansion) and BBF §2.2 to confirm the example's origin. Read the SSS 2019 and GHJM 2022 theorem statements. GHJM 2024 and BHJNS were read at abstract level only.

### A11 — Glauber attributions (Cheng–Wu → AS09 / RS; RS scope)

- **Kind:** attribution
- **Statement:** Glauber-cancellation attributions (besides E36 and R-M32). (1) The eikonal-phase attribution '(Cheng & Wu, verify)' is replaced by verified sources: Aybat–Sterman 2009 eq. (14) (explicit abelian phase) and Rothstein–Stewart eqs. (9.1), (9.18)-(9.19), (11.12)-(11.13). (2) RS do not give an independent full proof for DY: their S–S phase cancellation after the Δp_⊥ integral, 'taken alone it is far from a proof of factorization, even in the abelian case'. RS is 'supporting evidence' (S–S phase cancels after ∫Δp_⊥; A–A Glauber = soft zero-bin). (3) RS contains no e⁺e⁻-specific Glauber statement; cite it only for the general mechanism and for the rule 'ultrasoft Wilson line directions in SCET_I are determined by the physical directions'. (4) After the BPS field redefinition the Glauber Lagrangian still couples n and n̄ (RS §5.1), so usoft decoupling does not remove Glauber interactions. (5) Collins 2011 §14.4.5: the Glauber treatment of CSS 1988 was formulated for integrated PDFs but 'works equally well for the TMD case'.
- **Literature:** AybatSterman2009 arXiv:0811.0246, eq. (14); Rothstein:2016bsq arXiv:1601.04695, §5.1, eqs. (9.1),(9.18)-(9.19),(11.12)-(11.13); Collins:2011zzd §14.4.5; Collins:1988ig NPB 308 (1988) 833.
- **Source:** research/c_glauber/DERIVATION.md §6 items 1-2; research/c_scet/DERIVATION.md §6 item 14; frontier/others/OTHERS.md §4.1(iv); research/survey/SURVEY.md (line 317)
- **How to verify:** Read Aybat–Sterman eq. (14), RS §5.1, §9 and §11.1 (quote at eq. (11.13)), and Collins 2011 §14.4.5.

### A12 — Dipole formula fails at three loops

- **Kind:** attribution
- **Statement:** Dipole formula for the soft anomalous dimension: correct through two loops. It fails at three loops, where Almelid–Duhr–Gardi 2016 find non-dipole terms already for three coloured partons (a constant) plus kinematic dependence for four legs; graded [V], abstract-level reading. Caron-Huot 2015 §4 rules it out from four loops by a BFKL/Regge argument. The monograph states 'dipole formula beyond two loops: [V]'.
- **Literature:** Almelid:2015jia PRL 117 (2016) 172002, arXiv:1507.00047 (abstract); Caron-Huot:2013fea JHEP 05 (2015) 093, arXiv:1309.6521, §4.
- **Source:** frontier/others/OTHERS.md §1.6 (line 284), §1.7 last row
- **How to verify:** Read the ADG abstract and main result (three-loop correction Δ^(3)), and Caron-Huot §4.

### A13 — Collins 2011: quotes, pages, conventions

- **Kind:** attribution
- **Statement:** Statements quoted from Collins, Foundations of Perturbative QCD (CUP 2011; the 2023 OA version is a reissue, DOI 10.1017/9781009401845, not a revised edition; likewise Renormalization, DOI 10.1017/9781009401807). Quotes and locations to print: §5.4.3 p. 110 (no complete published proof of the Landau-equation results, quoting ELOP p. 48); §11.3.2 pp. 407-410 (the BRST classification of non-local operators is assumed, verbatim gap); §14.4 p. 553 (CSS 1988 'with some important improvements and with correction of errors'); §14.4.7 (BBL phases 'get moved into the parton densities'); §14.4.8 pp. 561-562 ('Issues remaining'); §14.6 pp. 569-570 (heavy-quark masses: m²/Q² × 1/ε terms can survive; keeping incoming masses 'is a bad idea'); §14.7 pp. 570-571 ('relative lack of detailed proofs'; NQS 2005 the 'notable exception', p. 571; TMD factorization 'appear[s] to fail' citing CQ 2007, RM 2010); §15.9 p. 580; §13.15.2; §13.17.1-13.17.5. Transcription hazards: Collins uses D = ∂ + igA (eq. (2.2)), so g_Collins = −g; and the TMD Fourier exponent e^{+ik·b} (eq. (13.35)). Some agents could not access the book (c_glauber: no Collins equation numbers quoted; REVIEW: chapter numbers from memory); no circumvention of access restrictions.
- **Literature:** Collins:2011zzd (OA reissue DOI 10.1017/9781009401845); Collins, Renormalization (CUP 1984; OA reissue DOI 10.1017/9781009401807); Collins:2012uy PRD 87 (2013) 034018 (for §3.3.2/§10.8 citations).
- **Source:** research/survey/SURVEY.md §0.3, §3.1 item 9, §3.2, items 4, 8, 9, 27; frontier/others/OTHERS.md §8.1, §13; research/c_glauber/DERIVATION.md §7; research/critic/REVIEW.md §11
- **How to verify:** Open the OA PDF and check each page number and quotation verbatim, especially pp. 110, 407-410, 553, 561-562, 569-571 and 580, and eqs. (2.2), (13.35).

### A14 — History of DY factorization and higher twist

- **Kind:** attribution
- **Statement:** History of DY factorization and higher twist. (1) BBL 1981: initial-state interactions 'violate the usual QCD factorization predictions… in leading twist'. BBL 1989: they 'can invalidate the parton-model form… unless the beam energy is greater than a scale that grows with the length of the target'. (2) Bodwin 1985: an all-order programme (erratum not examined). Two-loop checks by Lindsay–Ross–Sachrajda 1982-83; eikonal meson model by Brandt–Frenkel–Taylor 1989. (3) The non-abelian Bloch–Nordsieck failure for coloured initial states: Doria–Frenkel–Taylor 1980, confirmed by Di'Lieto–Gendron–Halliday–Sachrajda 1981 (which agrees on non-cancellation but disagrees on intermediate results) and by Andrási et al.; the non-cancelling terms are power-suppressed (Frenkel–Gatheral–Taylor 1984; Catani–Ciafaloni–Marchesini 1986, 'higher twist type'); CSS 1989 §10.2: at two loops at relative order m⁴/s² in DY. (4) Basu–Ramalho–Sterman 1984: factorization at higher twist in hadron–hadron scattering fails at m⁴/s². (5) KLN with a one-sided sum generically needs forward scattering and disconnected diagrams (Frye et al. 2019). (6) CSS 1986 call heavy-quark production factorization a 'conjecture'. (7) TMD Handbook: e⁺e⁻ → h_1h_2X was the first process with proven TMD factorization (Collins–Soper 1981 + erratum).
- **Literature:** Bodwin:1981fv PRL 47 (1981) 1799; Bodwin:1988fs PRD 39 (1989) 3287; Bodwin1985 PRD 31 (1985) 2616 [Erratum PRD 34 (1986) 3932]; Lindsay–Ross–Sachrajda 1982-83 (Lindsay:1982pu, Lindsay:1982gd); Brandt–Frenkel–Taylor 1989 (Brandt:1988xt); Doria:1980ak NPB 168 (1980) 93; DiLieto:1980nkq NPB 183 (1981) 223; Andrasi:1980qw; Frenkel:1983di NPB 233 (1984) 307; Catani:1985xt NPB 264 (1986) 588; Collins:1989gx §10.2; Basu:1984ba NPB 244 (1984) 221; Frye:2018xjj PRD 99 (2019) 056015; Collins:1985gm NPB 263 (1986) 37; Boussarie:2023izj arXiv:2304.03302 §2.11.4; Collins:1981uk NPB 193 (1981) 381 [Erratum NPB 213 (1983) 545].
- **Source:** research/survey/SURVEY.md items 3, 8, 9 (lines 170-176, 260-275, 313), §3.1 item 5; refdoc/REFDOC_ANALYSIS.md §4 (E28 additions); research/critic/REVIEW.md misconception 8
- **How to verify:** These were read at abstract level. Read the cited abstracts or texts once more, especially Di'Lieto et al. on the intermediate-result disagreement and CSS 1989 §10.2 on m⁴/s², and check the TMD Handbook §2.11.4 quote.

### A15 — DIS/DY attributions recalled, not checked

- **Kind:** attribution
- **Statement:** DIS/DY attributions recalled but not checked (c_dis, c_dy). (1) The DIS-scheme gluon fixed by the momentum sum rule: Diemoz–Ferroni–Longo–Martinelli 1988 (cite with '(see)'). (2) DIS scheme for quarks: Altarelli–Ellis–Martinelli 1979. (3) F_L at O(α_s): Altarelli–Martinelli 1978. (4) Bardeen–Buras–Duke–Muta 1978 was not opened; the sum-rule values come from T. Muta's report (Tokyo 1978). (5) Furmanski–Petronzio 1982 and ESW eq. (4.80) unverified. (6) AEM 1979 worked in the DIS scheme, so attributing the MS-bar form of the DY Δ_qq̄ to AEM must be phrased carefully (the MS-bar form appears later, e.g. ESW). The first full O(α_s²) DY is Hamberg–van Neerven–Matsuura 1991. NLO originals (Kubar-André–Paige; Harada–Kaneko–Sakai; Aurenche–Lindfors) were not consulted.
- **Literature:** DiemozEtAl1988 ZPC 39 (1988) 21; AltarelliEllisMartinelli1979 NPB 157 (1979) 461; AltarelliMartinelli1978 PLB 76 (1978) 89; BardeenEtAl1978 PRD 18 (1978) 3998; FurmanskiPetronzio1982 ZPC 11 (1982) 293; HambergVanNeervenMatsuura1991 NPB 359 (1991) 343; Ellis–Stirling–Webber, QCD and Collider Physics (CUP 1996).
- **Source:** research/c_dis/DERIVATION.md §11-12; research/c_dy/DERIVATION.md (attribution notes); spec/FINAL_OUTLINE.md prop:disall-dis-scheme
- **How to verify:** Open DFLM 1988, AEM 1979, AM 1978 and BBDM 1978 and confirm the attributed content. Read ESW §4.3 and §9.2 for the MS-bar DY coefficient.

### A16 — e⁺e⁻ attributions

- **Kind:** attribution
- **Statement:** e⁺e⁻ attributions (c_ee). (1) R_{e⁺e⁻} IR finiteness: Poggio–Quinn give a physics-level proof for 'any renormalizable' theory; rigorous versions are Lowenstein–Zimmermann 1975, Lowenstein 1976 and Breitenlohner–Maison 1977 I-III. That BM II spells out the hypotheses for non-abelian gauge theory with ghosts is 'to verify'. (2) ESW Ch. 3 prefactor H(ε) unverified. (3) Values recalled from memory, then verified by the critic (c4): r_2 = 1.9857 − 0.1153n_f (Chetyrkin–Kataev–Tkachov 1979; Dine–Sapirstein 1979; Celmaster–Gonsalves 1980); general-group a² coefficient −(3/32)C_F² + C_FC_A(123/32 − (11/4)ζ_3) + C_FT_Fn_f(−11/8 + ζ_3). (4) The a³ coefficient (see E29), with normalization conventions of Kataev–Starshenko to be checked. (5) MVV form-factor values recalled in c_ee but verified in c_dy.
- **Literature:** PoggioQuinn1976 PRD 14 (1976) 578; LowensteinZimmermann1975 CMP 44 (1975) 73; Lowenstein CMP 47 (1976) 53; BreitenlohnerMaison1977a/b/c CMP 52 (1977) 11, 39, 55; ChetyrkinKataevTkachov1979 PLB 85 (1979) 277; DineSapirstein1979 PRL 43 (1979) 668; CelmasterGonsalves1980a PRL 44 (1980) 560.
- **Source:** research/c_ee/DERIVATION.md §5-6, §12; research/critic/REVIEW.md c4
- **How to verify:** Confirm the r_2 references on INSPIRE and recompute r_2 from the general-group formula for n_f flavours. Read BM II for the gauge-theory scope.

### A17 — c_pdf attributions

- **Kind:** attribution
- **Statement:** c_pdf attributions. Locations of Carlson's theorem: Titchmarsh 1939 §5.81 and Boas 1954 Thm 9.2.1 (both via Waldschmidt arXiv:2002.01223). References cited from memory that need verification: Collins–Soper NPB 194 (1982) 445; Altarelli–Parisi NPB 126 (1977) 298; Gross–Wilczek; Georgi–Politzer; Curci–Furmanski–Petronzio NPB 175 (1980) 27; Catani–Seymour NPB 485 (1997) 291; Jaffe NPB 229 (1983) 205; Joglekar–Lee Ann. Phys. 97 (1976) 160; ESW Ch. 4. MVV normalization warning: eq. (3.4) γ_ns^(0) = C_F(2(S_1(N−1) + S_1(N+1)) − 3), with a factor 2 between conventions.
- **Literature:** Waldschmidt arXiv:2002.01223; Moch:2004pa NPB 688 (2004) 101, eq. (3.4); and the listed papers.
- **Source:** research/c_pdf/DERIVATION.md §7, §10
- **How to verify:** Look up each recalled reference on INSPIRE (journal, volume, page), and check Titchmarsh §5.81 and Boas Thm 9.2.1 directly if accessible.

### A18 — c_wilson attributions

- **Kind:** attribution
- **Statement:** c_wilson attributions. (1) The original Grammer–Yennie K-photon is symmetric (b_k k_μk_ν); the one-sided form with i0 is Collins' adaptation. This is known via Sen–Indumathi–Choudhury arXiv:1812.06468 eqs. (7)-(9); the original was not seen. Same as R-m01 (ERR-m3). (2) qq̄ → gg tree amplitudes: Combridge–Kripfganz–Ranft 1977; ESW Tab. 7.1 and Peskin–Schroeder §6.1 numbers still to verify. (3) The soft-photon theorem location is Weinberg, Phys. Rev. 140 (1965) B516. (4) Collins 2011 section and page numbers used by c_wilson (§11.9 p. 416; eqs. (11.4)-(11.6) p. 402; §10.3 p. 321; §10.8 p. 359; §11.4 p. 411; BRST pp. 407-411) must be checked against the book.
- **Literature:** GrammerYennie1973 PRD 8 (1973) 4332; Sen–Indumathi–Choudhury arXiv:1812.06468; Combridge–Kripfganz–Ranft PLB 70 (1977) 234; Weinberg Phys. Rev. 140 (1965) B516; Collins:2011zzd.
- **Source:** research/c_wilson/DERIVATION.md §7-8
- **How to verify:** Obtain GY 1973 and check the K-photon form. Check CKR 1977 and the Collins page numbers in the OA PDF.

### A19 — TMD and Sivers attributions

- **Kind:** attribution
- **Statement:** TMD and Sivers attributions (c_tmd, SURVEY item 11). (1) Transverse gauge links at light-cone infinity: Ji–Yuan 2002, Belitsky–Ji–Yuan 2003 (abstract level). (2) The Sivers sign reversal follows Collins 2002 after Brodsky–Hwang–Schmidt 2002 (see E30). (3) The spectator-model Sivers function f_1T^⊥,SIDIS = g²e_qe_s M(m + xM)(1−x)/(4(2π)⁴k_T²(k_T² + L²)) ln((k_T² + L²)/L²) agrees with Bacchetta–Conti–Radici 2008 eq. (SivBM2-s-pl) with e_qe_s = −e_c². (4) Lensing interpretation: Burkardt 2003, Lu–Schmidt 2006. (5) 'f_1T^⊥u is negative' is recalled, not verified. (6) T-odd fragmentation functions are universal (Collins–Metz 2004; Meissner–Metz 2009). (7) Space-like regulator lines: Aybat–Rogers 2011, citing Collins–Metz 2004 (see N20).
- **Literature:** Ji:2002aa PLB 543 (2002) 66; BelitskyJiYuan2003 NPB 656 (2003) 165; Collins:2002kn PLB 536 (2002) 43; Brodsky:2002cx PLB 530 (2002) 99; Bacchetta–Conti–Radici PRD 78 (2008) 074010, arXiv:0807.0323, eq. (SivBM2-s-pl); CollinsMetz2004 PRL 93 (2004) 252001; MeissnerMetz2009 PRL 102 (2009) 172003; AybatRogers2011.
- **Source:** research/c_tmd/DERIVATION.md R12, §6, §8; research/survey/SURVEY.md item 11; research/critic/REVIEW.md misconceptions 11-13
- **How to verify:** Re-run research/c_tmd/scripts/sivers_spectator.py against BCR 2008 eq. (SivBM2-s-pl) with e_c² → 4πC_Fα_s. Check the sign of the u-quark Sivers function in a recent global fit (e.g. Bury:2020vhj).

### A20 — Glauber/SLL literature as reported in the blueprint

- **Kind:** attribution
- **Statement:** Corrections to how the blueprint reports the Glauber/SLL literature (c_glauber §6). (1) CdFR do not show a cancellation: P^(1) is strictly factorized, P^(2) is not (non-zero for ≥ 5 QCD partons), and this 'may invalidate the factorization theorem of mass singularities starting at the N³LO'. FSS: two-loop expectation zero in pure QCD, violation at three loops. GHMMS: cancels in pure-QCD cross sections up to NNLO (see R-M20). (2) DDIS has a Glauber pinch in r^- for soft gluons attached to the target subgraph; Collins' 1998 proof escapes by deforming r^+ (§III D). (3) The RM counterexample is a double transverse-spin asymmetry; the unpolarized non-abelian case is only indicated (their Fig. 11). The abelian two-gluon terms are consistent with generalized but violate standard factorization. (4) First SLL at O(α_s⁴) relative to Born: σ_1,SLL = −σ_0(2α_s/π)⁴ln⁵(Q/Q_0)π²Y(3N²−4)/480 (FKS eqs. (3.22), (3.24); quoted, not recomputed). BNS 2021 give the tower α_s^{n+3}L^{2n+3}: 2→1 from four loops, and 2→0 (Higgs + jet veto) from five loops, 'contrary to earlier statements' that two coloured final-state partons are needed. (5) CDF 2000 diffractive-dijet factorization breaking 'by a factor of O(10)' is quoted from CDF's own summary (arXiv:1206.3955), not from the 2000 abstract. (6) H1's suppression of direct diffractive photoproduction (ZEUS differs) is not explained by Collins' proof: an open tension.
- **Literature:** Catani:2011st arXiv:1112.4405 (eq. (184) not transcribed); Forshaw:2012bi arXiv:1206.6363; Guan:2024hlf arXiv:2408.03019; Collins:1997sr PRD 57 (1998) 3051 [Erratum PRD 61 (2000) 019902], §III D; RogersMulders2010 arXiv:1001.2977, Fig. 11; Forshaw:2006fk JHEP 08 (2006) 059, arXiv:hep-ph/0604094, eqs. (3.22),(3.24); Becher:2021zkk arXiv:2107.01212, eqs. (13),(14); CDF PRL 84 (2000) 5043 and PRD 86 (2012) 032009, arXiv:1206.3955; H1 2007; Klasen–Kramer 2008.
- **Source:** research/c_glauber/DERIVATION.md §5 row 24, §6 items 1-10, §7
- **How to verify:** Read the CdFR conclusions, FKS §3, BNS PRL, Collins 1998 §III D and the CDF 2012 summary sentence. Recompute (3N²−4)/480 from FKS if possible.

### A21 — Exclusive-process attributions

- **Kind:** attribution
- **Statement:** Exclusive-process attributions (c_exclusive). (1) Reference warning: PRL 84 (2000) 2589 (Frankfurt–Polyakov–Strikman–Vanderhaeghen) is about decuplet baryons. The correct reference for hard pseudoscalar-meson production and the pion pole in Ẽ is Frankfurt–Pobylitsa–Polyakov–Strikman, PRD 60 (1999) 014010. (2) LO pion form-factor factorization: Lepage–Brodsky 1979/80, Efremov–Radyushkin 1980, Duncan–Mueller 1980, Farrar–Jackson 1979. (3) NLO hard kernel/ERBL kernel: Field–Gupta–Otto–Chang NPB 186 (1981) 429, Dittes–Radyushkin 1981, Braaten–Tse PRD 35 (1987) 2255, Melić–Nižić–Passek PRD 60 (1999) 074004; verified on INSPIRE, not re-derived. (4) The Lepage–Brodsky normalization ∫φ_LB = f_π/(2√N_c) is recalled. (5) The soft-overlap 1/Q⁴ scaling is quoted, not derived (Isgur–Llewellyn Smith). (6) Ji's J^q = ½[A^q(0) + B^q(0)] is read, not re-derived. (7) Collins–Freund v2 (DVCS factorization).
- **Literature:** Frankfurt:1999fp PRD 60 (1999) 014010, arXiv:hep-ph/9901429; PRL 84 (2000) 2589; Lepage:1980fj PRD 22 (1980) 2157; Efremov:1979qk PLB 94 (1980) 245; Duncan–Mueller PLB 90 (1980) 159, PRD 21 (1980) 1636; Field–Gupta–Otto–Chang NPB 186 (1981) 429; Braaten–Tse PRD 35 (1987) 2255; Melić–Nižić–Passek PRD 60 (1999) 074004; Ji1997a PRL 78 (1997) 610; Collins:1998be PRD 59 (1999) 074009, arXiv:hep-ph/9801262.
- **Source:** research/c_exclusive/DERIVATION.md §0, §3-4, §7, §10, references (line 488)
- **How to verify:** Query INSPIRE for PRL 84 (2000) 2589 and PRD 60 (1999) 014010 and compare the titles. Check the LB normalization in Lepage–Brodsky 1980 and the soft-overlap scaling statement in Isgur–Llewellyn Smith.

### A22 — SCET/NRQCD/BBNS attributions

- **Kind:** attribution
- **Statement:** SCET/NRQCD/BBNS attributions (c_scet §6). (1) Reference correction: PRD 66 (2002) 054005 is BPS 'Power counting in SCET'; the endpoint-singularity paper is BPS PRD 67 (2003) 071502. (2) The BPS 2002 footnote on reparameterization fixing the collinear action refers to the x-independent collinear transformations of Bauer–Stewart 2001, not to the Lorentz RPI of Manohar–Mehen–Pirjol–Stewart 2002. (3) BBNS 2005 comment vs BPRS 2005 reply on charming penguins: report without verdict. (4) BBL conventions: D = ∂ + igA flips the signs of the c_2, c_3, c_4 bilinears in CONTEXT conventions; in 2Im f_n/M^{d_n−4}, M is the heavy-quark pole mass; cite BBL Sec. II.F-G for decays and Sec. VI.A for production. (5) B → Dπ (BPS 2001) needs the endpoint-suppression assumption in the statement. (6) c_v = 1 − 2C_Fα_s/π, re-derived. (7) Verified references: Bauer–Lee–Manohar–Wise PRD 70 (2004) 034014; Fleming–Hoang–Mantry–Stewart PRD 77 (2008) 074010 and 114003. CTTW and DEFG are recalled; Korchemsky–Sterman 1999 is verified.
- **Literature:** BauerPirjolStewart2002 PRD 65 (2002) 054022; Bauer–Pirjol–Stewart PRD 66 (2002) 054005; Bauer:2002aj PRD 67 (2003) 071502, arXiv:hep-ph/0211069; BauerStewart2001 PLB 516 (2001) 134, arXiv:hep-ph/0107001; Manohar–Mehen–Pirjol–Stewart 2002 (Lorentz RPI; journal data recalled, verify); Bauer:2004tj PRD 70 (2004) 054015; Bodwin:1994jh; Korchemsky–Sterman NPB 555 (1999) 335.
- **Source:** research/c_scet/DERIVATION.md §6 items 7-9, 11, 12, 16; §4-5
- **How to verify:** Query INSPIRE for PRD 66 054005 and PRD 67 071502. Read the BPS 2002 footnote and BBL Sec. II.F-G.

### A23 — REVIEW §11 'verify' list

- **Kind:** attribution
- **Statement:** Critic REVIEW §11 'verify' list of attributions (21 items). Some were later verified by other agents (e.g. Mankiewicz–Piller → E21, Gaunt/SYZ → E36, BVZ → E03, Aybat–Sterman → R-M32). (1) Anikin–Zav'yalov Ann. Phys. 116 (1978) 135: light-cone expansion proof. (2) Lowenstein–Zimmermann NPB 86 (1975) 77: coverage of gauge-fixed QCD. (3) Frye et al. PRD 99 (2019) 056015: KLN forward/disconnected. (4) Gaunt JHEP 07 (2014) 110: exact claim. (5) Aybat–Sterman PLB 671 (2009) 46: scope. (6) FSS JHEP 11 (2012) 066: order. (7) CSS NPB 263 (1986) 37: heavy-particle Glauber completeness → [A]/[C]. (8) Collins PRD 58 (1998) 094002: 'error suppressed uniformly in m/Q'. (9) DFT 1980 / Di'Lieto 1981: power suppression for DY. (10) Beneke–Braun NPB 454 (1995) 253: absence of a 1/Q renormalon in DY. (11) BNRS 2016 / BNS 2021 data. (12) Mankiewicz–Piller 2000. (13) Ebert–Michel–Stewart–Sun 2022. (14) BVZ 2019. (15) Korchemsky–Sterman NPB 555 (1999) 335. (16) Shifman 2000 (hep-ph/0009131). (17) Graudenz 1994. (18) Page data for Li–Sterman 1992, Soffer 1995, Labastida–Sterman 1985, Kodaira 1980, Christ–Lee 1966. (19) FF factor z^{1−2ε} (Collins 2011 ch. 12). (20) Gluon d-dimensional average convention. (21) Collins 2011 chapter numbers (from memory).
- **Literature:** As listed (refs_merged.bib keys where present: Anikin:1978tj, Lowenstein:1974qt, Frye:2018xjj, Gaunt:2014ska, AybatSterman2009, Forshaw:2012bi, Collins:1985gm, Collins:1998rz, Doria:1980ak, DiLieto:1980nkq, Mankiewicz:1999tt, Braun:2018brg, Shifman2000).
- **Source:** research/critic/REVIEW.md §11
- **How to verify:** Mark each item as verified or still open by cross-referencing VERIFIED_FORMULAS, SURVEY and the c_* DERIVATION files. Look up the remaining items on INSPIRE and read the cited passages.

### A24 — Misconception-box attributions

- **Kind:** attribution
- **Statement:** Attributions in the misconception boxes (REVIEW §7 and FINAL_OUTLINE). (1) The original 'T-invariance forbids Sivers' argument is Collins 1993; the reversal is Collins 2002 after BHS 2002 (E30). (2) T-odd FFs are universal: Collins–Metz 2004, Meissner–Metz 2009. (3) Transverse links: Ji–Yuan 2002, BJY 2003. (4) The Lam–Tung relation is violated at O(α_s²). (5) Non-abelian Bloch–Nordsieck failure at two loops: DFT 1980, Di'Lieto–Gendron–Halliday–Sachrajda 1981. (6) Exact scaling in the 't Hooft model: Callan–Coote–Gross 1976, Einhorn 1976. (7) δ(x) terms in twist-3 distributions: Burkardt–Koike 2002. (8) P^+_NS − P^-_NS at NLO ∝ C_F(C_F − C_A/2): Curci–Furmanski–Petronzio 1980 (R-M10). (9) Gottfried sum rule / NMC violation. (10) Christ–Lee 1966.
- **Literature:** Collins:1992kk; Collins:2002kn; Brodsky:2002cx; CollinsMetz2004; MeissnerMetz2009; Ji:2002aa; BelitskyJiYuan2003; Doria:1980ak; DiLieto:1980nkq; Callan–Coote–Gross 1976 and Einhorn 1976 ('t Hooft-model scaling; journal data recalled, verify); Burkardt–Koike 2002 (δ(x) in twist-3; recalled, verify); Curci–Furmanski–Petronzio NPB 175 (1980) 27.
- **Source:** research/critic/REVIEW.md §7 (misconceptions 8, 11-13, 26; O21); spec/FINAL_OUTLINE.md misconception boxes
- **How to verify:** Confirm each reference on INSPIRE; journal data for CCG, Einhorn and Burkardt–Koike are recalled here. Read the relevant abstract sentences.

### A25 — Quarkonium, EW and DPS attributions

- **Kind:** attribution
- **Statement:** Frontier attributions in quarkonium, EW and DPS (OTHERS). (1) NRQCD production: NQS 2005-06 find that gauge completion with Wilson lines restores factorization at NNLO, to all orders in v for octet→singlet, with possibly further non-local operators beyond NNLO ([P]). Bodwin–Chung–Ee–Kim–Lee 2020 find universality at two loops, with results differing from NQS in some respects ('sources identified'); both are consistent with NRQCD factorization. (2) η_c tension: Butenschoen–He–Kniehl 2015 ('challenges NRQCD factorization') vs Han et al. 2015 and Zhang et al. 2015 (consistent). (3) EW Bloch–Nordsieck violation for non-singlet initial states: Ciafaloni–Ciafaloni–Comelli 2000 ([V]). (4) Leading-power non-factorizable EW corrections from O(α_s²α_W²log⁴(Q²/M_W²)): Baumgart–Erdoğan–Rothstein–Vaidya 2019 ([V] as computed). (5) DPS Glauber cancellation for double DY, all orders: Diehl–Gaunt–Ostermeier–Plößl–Schäfer 2016. (6) The Ebert–Gao–Stewart NLP TMD factorization is conditional on a Glauber assumption ([A](cond.)). (7) Gamberg et al. 2022 is an unrefereed preprint.
- **Literature:** NayakQiuSterman2005a PLB 613 (2005) 45; Nayak:2005rt PRD 72 (2005) 114012; NayakQiuSterman2006 PRD 74 (2006) 074007; Bodwin:2019bpf PRD 101 (2020) 096011, arXiv:1910.05497; Butenschoen–He–Kniehl PRL 114 (2015) 092004; Han et al. PRL 114 (2015) 092005; Zhang et al. PRL 114 (2015) 092006; Ciafaloni:2000df PRL 84 (2000) 4810; Baumgart:2018ntv PRD 100 (2019) 096008, arXiv:1811.04120; Diehl:2015bca arXiv:1510.08696; Ebert:2021jhy JHEP 06 (2022) 007 [Erratum 07 (2023) 096]; Gamberg:2022lju arXiv:2211.13209.
- **Source:** frontier/others/OTHERS.md §0 item 3, §6, §12, §13.2-13.3 (lines 1318-1350, 1405-1420)
- **How to verify:** Read the abstracts (all abstract-level): NQS 2005, Bodwin et al. 2020 (the 'differences'), the three PRL 114 papers, CCC 2000 and BERV 2019.

### A26 — Grade conflicts between our materials

- **Kind:** attribution
- **Statement:** Grade conflicts between our materials, which must be resolved before printing. (1) OTHERS grades the OPE for QCD with quarks '[R] in PT via classical results' and Collins 2020 Thm 1 '[R]†'; FINAL_OUTLINE §0.9 item 4 does not adopt these (D3: conservative verdicts bind). (2) YZLIU grades the multiplicative renormalizability of space-like Wilson-line operators at [R]-level, while LAMET grades it [A] (N1-N3, with the space-like extension asserted). (3) LAMET grades the threshold factorization [R]_2L ('41 terms, two constants fitted'), while a fit cannot certify [R]; YZLIU grades the two-loop value [P]. (4) The OTHERS Gordan proposition [R] vs its use in the binding outline (lem:appD-gordan). (5) The reference document's B′ grade for DY rests on the residual refuted in R-S1.
- **Literature:** —
- **Source:** frontier/others/OTHERS.md §1.7, §2.7; frontier/yzliu/YZLIU.md §3.E2, line 743; frontier/lamet/LAMET.md §4.5, §6.1 (line 69 table, line 948); spec/FINAL_OUTLINE.md §0.9 item 4
- **How to verify:** Compare each statement's tag across the four files and record the lead author's decision in FINAL_OUTLINE.

### A27 — Experimental status (Sivers) and twist-3 evolution dispute

- **Kind:** attribution
- **Statement:** Experimental and phenomenological status statements (SURVEY). (1) Sivers sign change: COMPASS 2017 is 'consistent with' it; COMPASS final 2015+2018 data (PRL 133 (2024) 071902) 'consistent with the fundamental QCD prediction'. STAR W±/Z (2011 data): χ²/ndf = 7.4/6 with the sign change vs 19.6/6 without (KQ model, no TMD evolution), 'if TMD evolution effects are small'. Bury–Prokudin–Vladimirov 2021: a same-sign fit has χ²/N_pt = 1.0 and 'cannot exclude the same sign'. Echevarria–Kang–Terry 2021: tension with RHIC W/Z data. Verdict: consistent, not decisive. (2) Twist-3 evolution: Braun–Manashov–Pirnay 2009 'do not agree with the recent calculations' of Kang–Qiu 2009. The Sivers–T_F 'sign mismatch' (Kang et al. 2011) is addressed by the JAM 2020 common-origin analysis. (3) Collins 1998 (heavy-quark masses): factorization with remainders 'uniformly suppressed by a power of Λ/Q, independently of… M' (abstract quote).
- **Literature:** COMPASS:2017jbv; COMPASS:2023vqt PRL 133 (2024) 071902; STAR:2015vmv PRL 116 (2016) 132301, arXiv:1511.06003; Bury:2020vhj PRL 126 (2021) 112002, arXiv:2012.05135; Echevarria:2020hpy JHEP 01 (2021) 126, arXiv:2009.10710; Braun:2009mi PRD 80 (2009) 114002, arXiv:0909.3410; Kang:2008ey PRD 79 (2009) 016003, arXiv:0811.3101; Kang:2011hk; Cammarota:2020qcw (JAM 2020); Collins:1998rz PRD 58 (1998) 094002, arXiv:hep-ph/9806259.
- **Source:** research/survey/SURVEY.md item 11 (lines 328-345), item 21 (lines 488-491), item 27 (line 230), §3.1 item 7
- **How to verify:** Read the STAR 2016 text for the χ² values, the BPV 2021 conclusion sentence, the BMP 2009 abstract and the JAM 2020 abstract.

### A28 — NLP endpoint-factorization status attributions

- **Kind:** attribution
- **Statement:** Who established what in next-to-leading-power (NLP) endpoint factorization, as OTHERS §5.5 prints it. (1) Endpoint divergences are generic at NLP, and MS-bar renormalization of the individual functions is insufficient: [R] by explicit examples (Liu–Neubert 2020; Beneke–Broggio–Jaskiewicz–Vernazza 2020). (2) h→γγ via a b-quark loop: the renormalized endpoint-factorized theorem holds to all orders [A] (LN 2020; LMNW 2021). The D-dimensional refactorization conditions are 'proven' within SCET (LMNW 2021 §3, eqs. (3.12)-(3.14)), so the theorem rests on SCET's own assumptions. (3) gg → h via light quarks (LNSW 2023, RBS scheme): [A]. (4) Threshold DY at NLP: a bare d-dimensional factorization that fails if d → 4 is taken first (BBJV 2020) [P]. (5) LL resummation at NLP for DY, gg→H, off-diagonal DIS and gluon thrust (Beneke et al. 2019-2022): [A] at LL only. (6) NLP DIS and the MS-bar ↔ endpoint scheme (Beneke–Schnubel–Szafron 2026): [A]†, an unrefereed preprint. (7) Bodwin et al.'s position-space SCET papers scrutinize individual ingredients ('hidden self-energy contributions', arXiv:2512.11647†).
- **Literature:** Liu:2019oav JHEP 04 (2020) 033, arXiv:1912.08818; Liu:2020wbn JHEP 01 (2021) 077, arXiv:2009.06779, §3; Liu–Neubert–Schnubel–Wang JHEP 06 (2023) 183; Beneke:2019oqx JHEP 07 (2020) 078 (BBJV); Beneke:2026miy arXiv:2608.25502; Bodwin:2021cpx PRD 104 (2021) 016010; Bodwin:2021epw PRD 104 (2021) 116025; Bodwin:2023asf PRD 109 (2024) 056020; Bodwin:2025zzi arXiv:2512.11647.
- **Source:** frontier/others/OTHERS.md §5.1-5.5 (status table lines 871-884), lines 820-830
- **How to verify:** Read LMNW §3 to confirm the refactorization conditions are proven (and under which SCET assumptions), the BBJV abstract on the d → 4 ordering, and the BSS 2026 status on arXiv/INSPIRE.

## 7. Duplicate-merge map

| claim | merged source items |
|---|---|
| E01 | LAMET §0.3 item 1, §3.7 Prop 3.4, §13 item 12, §14 item 1; the author-list side issue is A01 |
| E02 | LAMET §0.3 item 2, §10.2, §14 item 2; YZLIU E1 (incl. the quasi-LFWF version) |
| E07 | LAMET §5.1, §10.4(c), §11, §4.6(e); YZLIU A1 'Novelty' (bent soft functions) |
| E08-E11 | YZLIU E2, E2′, E3, E4 (and B2, C3 checks); YZLIU §2 sign-convention table |
| E14 | OTHERS §1.4, §1.7; c_regions §1.3; SURVEY item 4; REFDOC ERR-M3 (reference-doc counterpart R-M3) |
| E15 | OTHERS §1.2, §1.4, §1.7 rows 4 and 8; SURVEY item 4; Collins 2011 §5.4.3 quote (A13) |
| E17 | c_tmd §1 item 4, §7, §8 item 3; VF-TMD-9; FINAL_OUTLINE line 844 |
| E18 | c_glauber §2.4, §5 row 14, §6 item 3(c); VF-GLA-8; FINAL_OUTLINE ex:break-c07 (line 1326) |
| E20 | c_exclusive §0 row 8, §7, §10 item 4; VF-EXC-8 |
| E21 | c_exclusive §8, §10 item 10; mentioned in REFDOC ERR-M17 (R-M17) |
| E23 | c_scet §6 item 10; VF-CONV-23; VF-SCET-16; FINAL_OUTLINE def:sudakov-cusp (line 344) and App B (line 1758) |
| E26 | c_scet §6 item 17; VF-BQ-4; FINAL_OUTLINE line 1478 |
| E27 | c_wilson §2.7, §6.2; VF-WL-10; FINAL_OUTLINE lines 552, 1836; SURVEY §0.3; REFDOC ERR-M5 (R-M5) |
| E28 | c_ee §0, §8, §10 item 1; VF-EE-12; FINAL_OUTLINE line 1122 |
| E30 | SURVEY items 11 and 30; REVIEW misconception 12; c_tmd §6.2; A24 item 1 |
| E31 | SURVEY item 8, §3.1 item 4; FINAL_OUTLINE lem:dy-fsi (line 722) |
| E34 | OTHERS §5.2, §6, §9.2 and small-x helicity (lines 1176-1183); OTHERS §0 item 3 |
| E35 | OTHERS §7 (Props 7.1, 7.2); the positivity debate of the earlier plan is merged here |
| E36 | OTHERS §4.1(iv)-(v), §4.2(a)-(c), §4.7; REFDOC ERR-M30 (R-M30); SURVEY §3.1 item 6; c_glauber §6 item 10 |
| N01 | REFDOC §0, ERR-S1, §3 E15, S37, S57 (M32), S59, S60; reference-doc counterpart R-S1 |
| N02 | OTHERS §1.3, §14.2 item 1; FINAL_OUTLINE lem:appD-gordan; c_regions Thm L3 |
| N12 | REFDOC S30, §3 D24, ERR-m25, §2.5 item 2; R-M2, R-m23 |
| N13 | REFDOC ERR-S3 (R-S3), S59 list |
| N16-N19 | c_glauber §1.6, §2.3-2.5, §3; VF-GLA-6, -8, -9, -10, -11; FINAL_OUTLINE prop:break-colour, thm:break-tmd |
| N20 | c_tmd R3′, §3.4, §6.2; VF-TMD-9 |
| N24 | c_ee §5; VF-EE-8; FINAL_OUTLINE thm:ee-R-finite; REFDOC ERR-M13 (R-M13) |
| N28 | OTHERS §14.2 item 4 (the LUXqed/Frixione comparison of the earlier plan is merged here) |
| A03, A04 | YZLIU 'Novelty' paragraphs and grade discussions; LAMET §10.2, §11 |
| A08 | OTHERS §1.2, §1.7; SURVEY item 4, §3.1 item 2; FINAL_OUTLINE §0.9 item 4 |
| A09 | OTHERS §2; SURVEY item 1, §3.1 item 1; REFDOC ERR-M26 (R-M26); FINAL_OUTLINE §0.9 item 4 |
| A11 | c_glauber §6 items 1-2; c_scet §6 item 14; OTHERS §4.1(iv); SURVEY line 317 |
| A18 | c_wilson §7-8; REFDOC ERR-m3 (R-m01) |
| R-m13 | REFDOC ERR-m13 to m16 and OUR-5 (small-b remainder O((b_Tm)²)) |

## 8. Considered but not entered as claims

- Sterman, TASI'95 lectures, eq. (63) presupposes a connected S; c_regions states explicitly that this is not an error of the source.
- Corrections of our own outline/blueprint that concern neither the literature nor the reference document. c_pdf: missing gluon-PDF definition, support [−1,1], Z sign convention, left vs right derivative, per-graph gauge dependence. c_regions (critic O11 → VF-REG-12): pure DR suffices for on-shell massive legs with a massless gluon but fails for massive exchange. c_tmd: blueprint P11.11/P11.13 mixed MS-bar conventions. c_scet §6 items 1-6: γ^S = γ^H − 2γ^J convention, plus-distribution conventions, Glauber-mode orderings, decoupling-theorem details, W_n orientation (no sign change of g). c_dy: 'soft factor = 1 for inclusive' holds only q_T-integrated. c_glauber §6 items 1, 8, 9 (blueprint P10.4, L10.5/P7.17 section numbers, E7.24). The FINAL_OUTLINE audit's over-claim fixes (CHANGELOG).
- Convention hazards, not errors of the sources. Collins' sign of g and of the TMD Fourier exponent (A13). Plus-prescription conventions in P_gg (SURVEY §3.2). Larin's γ^μγ_5 replacement: the literature form assumes ε_{0123} = +1; with the binding ε^{0123} = +1 the sign flips (VF-CONV-24). B → Dπ: with (V−A)⊗(V−A) operators instead of P_L projectors, N is 4 times larger (VF-BQ-6). Γ_S sign conventions differ between PLB, APPB/PRD 105 and JHEP 2023; use γ_HH only (YZLIU §2; the genuine inconsistency is E09). APPB eq. (21), ζ = 2(xP^+)²e^{2y_n}, may use a y_n convention opposite to Collins' book (YZLIU §2, UNVERIFIED). Gluon spin average 1/(D−2) vs 1/2 shifts C_2g by +P_qg (c_dis).
- VF-POL-3 (LO transversity kernel) has status C ('standard; not derived by an agent'). This is a verification status, not a claim of the four kinds.
- FINAL_OUTLINE §0.9 item 3 says REFDOC_ANALYSIS 'looks unfinished (stops inside S28)'. The file now runs to S63 (1850 lines). This is a stale internal note.
- Reference-document items that the readers found correct (REFDOC §1.9 inventory, e.g. App C chain-expansion signs, Ex C.15/C.26, Lemma C.29) carry no claim. The '(E.19) pdftotext spurious minus' is an extraction artefact (the image is correct).
