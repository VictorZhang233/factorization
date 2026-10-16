# W14-write

(structured result persisted from wf_3924630b-621)

## summary

I finished Ch12 (Drell–Yan) as chapters/ch12_dy.tex. The session resumed from the earlier W14 drafts p0–p6. I audited and corrected them, wrote the missing parts p7–p10 (§NLO, §other, §twist, closing section), and assembled the unit.

The standalone build is clean. Errors 0, missing glyphs 0, no overfull box above 1 pt, undefined citations 0, duplicate labels 0, BibTeX warnings 0. check_unit_v2.py passes C1/C2/C4–C7/C8a. Two flags remain, both justified: C3 flags app:appN and app:appO (appendix chapter labels the script's pattern does not cover), and C8b flags one misconception-box item that quotes a misconception in order to correct it.

All 30 canonical statements are present with outline tags; no tag is weakened or strengthened. The chapter has the 9 canonical sections, tab:dy-status, tab:dy-correspondence, the 5 owned figures (copied verbatim), the opening box, a misconception box and the four-layer status of thm:dy-factorization. Grade propagation was checked by hand for every statement, and there are no hidden forward dependencies.

Every printed formula that is not a VF entry was re-derived and checked with scripts. Literature locations and quotations were verified against arXiv full texts (CSS 1989, Rothstein–Stewart 2016), INSPIRE abstracts and a Collins 2011 chapter-5 extract, or taken from records already verified in verify/ (A13, A14, N01, N25).

The main open issue is length: the chapter is 32 pages against an 18-page budget (21.6 with +20 %). The budget cannot be met without cutting required content.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch12_dy.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch12_dy.bib-additions
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p0_intro.tex
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p1_born.tex
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p2_regions.tex
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p3_orientation.tex
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p4_glauber.tex
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p5_model.tex
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p6_theorem.tex
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p7_nlo.tex
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p8_other.tex
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p9_twist.tex
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/parts/p10_summary.tex
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/p7_checks.py
15. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/dy_nlo_check.py
16. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/glauber_model_check.py
17. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/eikonal_twogluon.py
18. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/logs/p7_checks.log
19. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/logs/dy_nlo_check.log
20. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/logs/glauber_model_check.log
21. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/logs/eikonal_twogluon.log
22. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/tools/assemble.sh
23. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/tools/build.sh
24. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W14/tools/reglookup.py
25. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W14/test_dy.tex
26. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W14/test_dy.pdf
27. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W14/check_out.txt

## pages

32 pp (standalone build writing/test/W14/test_dy.pdf: chapter title on p. 1, last chapter page p. 32, bibliography from p. 33). Budget is 18 pp, or 21.6 pp at +20 %: the chapter is +78 % over budget (+48 % over the extended cap). Breakdown: §1.1 Born pp. 2–3; §1.2 regions pp. 4–5; §1.3 orientation pp. 6–8; §1.4 Glauber pp. 9–11; §1.5 models pp. 12–19 (two full-page figures); §1.6 theorem pp. 20–21; §1.7 NLO pp. 22–27; §1.8 other pp. 28–29; §1.9 twist p. 30; §1.10 closing pp. 31–32.

## compile_status

xelatex + bibtex + xelatex ×2 in writing/test/W14 (driver test_dy.tex; preamble_fact.tex; refs_merged_v2.bib with ch12_dy.bib-additions appended).
- Errors (LaTeX Error / Undefined control sequence / Emergency stop): 0
- Missing characters: 0
- Overfull hbox > 1 pt: 0 (two below 1 pt remain: 0.92 pt and 0.31 pt)
- Undefined citations: 0
- Multiply defined labels: 0
- BibTeX warnings: 0
- Undefined references: only other units' labels (listed in report item 4)
- Every page with a figure, table, box or long display was rendered at 110 dpi and inspected.

## checker_output

C1 canonical labels of this unit missing: OK
C1b canonical fig/tab labels of this unit missing: OK
C2 labels defined here but owned by another unit: OK
C3 external refs not canonical: ['app:appN', 'app:appO']  -> justified: these are the appendix chapter labels app:<key>, canonical by WRITER_SPEC §5.1; the script's pattern covers only def|thm|lem|prop|cor|conj|rem|ex|asm|sec|fig|tab
C4 \uses problems: OK
C5 cref/uses mismatches: OK
C6 tag/qualifier problems: OK
C7 statements without \uses or "% uses: none": OK
C8a planning markers: OK
C8b phrases to justify: one hit, 'Glauber 胶子在单举截面中总是相消', inside the misconception box (sec:dy-summary). It is quoted as a misconception and corrected in the same item, so it is not an over-claim.

## report_markdown

# W14 report — Ch12 `ch12_dy.tex` (Drell–Yan 过程与强子—强子碰撞)

**Context.** This session resumed the earlier W14 run, which had been interrupted by the quota limit. That run had written the parts p0–p6 and three check scripts, but no unit file existed yet.
- I audited p0–p6 against the binding files and corrected them (see items 11 and 13).
- I wrote p7–p10 (§NLO, §other, §twist, closing section) and assembled the unit with `writing/work/W14/tools/assemble.sh`.
- There is no `SPEC_V24_DELTA`, no `X1-glauber_final2.md` and no v2.4 changelog in FINAL_OUTLINE_v2. I therefore used `X1-glauber_final.md` together with its final review and the App O entries of the outline.

## 1. File
- **Unit:** `/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch12_dy.tex` (1269 lines).
- **Bib additions:** `chapters/ch12_dy.bib-additions` contains `Duhr:2020seh` (PRL 125 (2020) 172001, arXiv:2001.07717), re-verified on INSPIRE.
- **Pages:** 32 (pp. 1–32 of the standalone build; the bibliography starts on p. 33). The budget is 18 pp (21.6 pp at +20 %); see items 13 and 14.
- **Compile:** xelatex + bibtex + xelatex ×2.
  - Errors 0; missing characters 0.
  - Overfull > 1 pt: 0 (0.92 pt and 0.31 pt remain).
  - Undefined citations 0; multiply defined labels 0; BibTeX warnings 0.
- **Visual check:** every page was rendered at 110 dpi and inspected.

## 2. Canonical labels
All canonical labels of Ch12 are implemented, in reading order:
- **Statements (30):** `def:dy-kin`, `prop:dy-born`, `prop:dy-regions`, `prop:dy-glauber-pinch`, `lem:dy-poles-orientation`, `rem:dy-one-time-per-jet`, `lem:dy-fsi`, `ex:dy-future-vs-past`, `prop:dy-deformation`, `lem:dy-soft`, `prop:dy-universality`, `prop:dy-abelian-model`, `ex:dy-spectator-lcopt`, `ex:dy-glauber-model`, `prop:dy-eikonal-twogluon`, `rem:dy-common-ordering`, `thm:dy-factorization`, `rem:dy-nnlo-not-glauber`, `rem:dy-dft-premises`, `prop:dy-nlo`, `ex:dy-nlo`, `prop:dy-scale`, `rem:dy-dis-scheme`, `ex:dy-threshold`, `thm:dy-colour-singlet`, `thm:dy-polarized`, `conj:dy-coloured-final`, `conj:dy-polarized-jets`, `thm:dy-higher-twist`, `prop:dy-twist6-failure`.
- **Sections (9):** `sec:dy-born`, `sec:dy-regions`, `sec:dy-orientation`, `sec:dy-glauber`, `sec:dy-model`, `sec:dy-theorem`, `sec:dy-nlo`, `sec:dy-other`, `sec:dy-twist`.
- **Tables (2):** `tab:dy-status`, `tab:dy-correspondence`.
- **Figures (5):** `fig:dy-oneloop`, `fig:glauber-exchange`, `fig:dy-abelian-model`, `fig:dy-pole-orientation`, `fig:dy-two-gluon-exchange`.
- **Chapter label:** `ch:dy`.

`check_unit_v2.py` passes C1, C1b, C2, C4, C5, C6, C7 and C8a. Two flags remain:
- **C3** flags `app:appN` and `app:appO`. These are appendix chapter labels, canonical by §5.1; the script's pattern does not cover the `app:` prefix.
- **C8b** flags one phrase in the misconception box, where the misconception is quoted and corrected.

## 3. Additional labels
- **Equations:** `eq:dy-bare`, `eq:dy-leptontensor`, `eq:dy-master`, `eq:dy-LO`, `eq:dy-LOy`, `eq:dy-lc-fourier`, `eq:dy-future`, `eq:dy-universality`, `eq:dy-chi`, `eq:dy-Ias`, `eq:dy-JA-two-orderings`, `eq:dy-Jbox`, `eq:dy-factorization`, `eq:dy-dft`, `eq:dy-fact-nlo`, `eq:dy-Dqq`, `eq:dy-Dqg`, `eq:dy-mf`, `eq:dy-Tqq`, `eq:dy-Tqg`, `eq:dy-real-qq`, `eq:dy-real-qg`, `eq:dy-virt`.
- **`tab:dy-laurent`:** the Laurent table (VF-DY-7) inside the proof of `prop:dy-nlo`.
- **`sec:dy-summary`:** the closing section, holding the summary, `tab:dy-correspondence` and the misconception box.
- No auxiliary lemmas and no extra examples were added.

## 4. External labels (all canonical)
- **Appendix chapters:** `app:appN`, `app:appO`.
- **App N assumptions:** `asm:appN-brst-nonlocal` (named gap, text only), `asm:appN-collins`, `asm:appN-cutsum`, `asm:appN-envelope`, `asm:appN-multren`, `asm:appN-separation`, `asm:appN-uv`, `asm:appN-values`, `asm:appN-ward-product`.
- **App O assumptions:** `asm:appO-collinear-ends` (text only), `asm:appO-deformation`, `asm:appO-envelope`, `asm:appO-lcopt`, `asm:appO-mixing`, `asm:appO-rewritten-cs`.
- **Ch1 assumptions and definition:** `asm:intro-bridge`, `asm:intro-composite`, `def:intro-factorization`.
- **App O statements:** `cor:appO-interface`, `def:appO-lcopt`, `def:appO-leading-data`, `def:appO-orientation`, `def:appO-windows`, `lem:appO-cut-position`, `lem:appO-equal-time`, `lem:appO-glauber-operator`, `lem:appO-glauber-pc`, `lem:appO-hard-locality`, `lem:appO-joint-localization`, `lem:appO-lcopt`, `lem:appO-no-crossing`, `lem:appO-orientation`, `lem:appO-unitarity`, `prop:appO-eikonal`, `prop:appO-g6-ladder`, `prop:appO-one-sided`, `prop:appO-past-wilson`, `prop:appO-ss-cancel`, `prop:appO-strict-window-shape`, `prop:appO-target`, `prop:appO-twoexch-spectator`, `rem:appO-cut-ss`, `rem:appO-literature-comparison`, `thm:appO-main`.
- **App O sections and table:** `sec:appO-main`, `sec:appO-orientation`, `sec:appO-rewriting`, `sec:appO-unitarity`, `sec:appO-wilson`, `tab:appO-checklist`.
- **Other appendices:** `prop:appN-dy`, `def:appI-hvbm`, `prop:appI-larin`, `lem:appC-phase-space`, `lem:appJ-cut-hermiticity`.
- **Ch2–Ch5:** `lem:qcd-colour-identities`, `def:prelim-lightfront`, `def:prelim-plus`, `lem:prelim-eikonal-identity`, `lem:prelim-mellin`, `lem:prelim-plus-expansion`, `prop:prelim-wilson-covariance`, `prop:prelim-wilson-rules`, `def:ir-glauber`, `prop:ir-bn-failure`, `prop:ir-glauber-trapping`, `thm:ir-leading-regions`, `prop:sudakov-oneloop`.
- **Ch7–Ch11:** `thm:dis-moments`, `prop:dis-twist4`, `def:pdf-antiquark`, `def:pdf-ff`, `def:pdf-gluon`, `def:pdf-polarized`, `def:pdf-quark`, `prop:pdf-lo-kernels`, `prop:pdf-partonic-dr`, `thm:pdf-dglap`, `lem:method-i0-compat`, `lem:method-soft-unitarity`, `prop:method-fsi`, `prop:method-glauber-deformation`, `prop:method-glauber-oneloop`, `rem:method-two-component`, `thm:method-template`, `prop:disall-dis-scheme`, `prop:disall-nlo`, `lem:coll-final-poles`.
- **Forward pointers in text only (Ch13, Ch14, Ch18, Ch24):** `prop:thr-oneloop`, `def:tmd-soft`, `thm:tmd-factorization`, `thm:tmd-sivers-sign`, `prop:break-hh-diffraction`, `prop:break-mass-singularity`, `prop:break-measurement`, `prop:break-spacelike`, `thm:break-tmd`, `prop:front-syz`.
- **Figures of other units:** `fig:reduced-dy` (Ch4), `fig:glauber-contour`, `fig:method-glauber-direction` (Ch9).

## 5. Tags (final; none weakened or strengthened)
- **[R, R_PT]:** `prop:dy-born`, `prop:dy-glauber-pinch`, `lem:dy-poles-orientation`, `prop:dy-eikonal-twogluon`, `prop:dy-nlo`, `prop:dy-scale`. Each first sentence is the verbatim R_PT qualifier and then states the order.
- **[R, R_def]:** `ex:dy-future-vs-past`, `prop:dy-universality`.
- **[A]:** `prop:dy-regions`, `lem:dy-fsi`, `prop:dy-deformation`, `lem:dy-soft`, `thm:dy-factorization`, `thm:dy-colour-singlet`, `thm:dy-polarized`, `thm:dy-higher-twist`.
- **[P]:** `prop:dy-abelian-model`. The first sentence names the model, and the proof is a full proof of the model-internal claim.
- **[C]:** `conj:dy-coloured-final`, `conj:dy-polarized-jets`.
- **[V]:** `prop:dy-twist6-failure`.
- **No tag:** `def:dy-kin`, all remarks, all examples except the R_def one.
- **Status paragraphs:** a 「地位与缺口」 paragraph follows every [A], [P], [C] and [V] statement (C6 OK).
- **Grade propagation:** checked by hand for every `\uses` list; no conflict. Points that matter:
  - `lem:appO-unitarity` and `prop:appO-ss-cancel` are [R, R_cond] with content [A].
  - `lem:appJ-cut-hermiticity` is [R, R_def].
  - `prop:appI-larin` is [R, R_PT].
  - The global `asm:intro-*` entries are not counted.
- **`% errtype` comments:**
  - E-S: `prop:dy-regions`, `lem:dy-fsi`, `thm:dy-factorization`, `thm:dy-colour-singlet`, `thm:dy-polarized`, `thm:dy-higher-twist`. For the three process theorems the weakest step is the E-S scaling statement of the region analysis, per `tab:dy-status`; the draft had E-W.
  - E-W: `prop:dy-deformation`.
- **Tags in words at first use** of other units' statements were added as WRITER_SPEC §4.11 requires (33 places).

## 6. Assumptions
- **Defined:** none (Ch12 owns no assumption).
- **Used in `\uses`:** `asm:appO-lcopt`, `asm:appO-envelope`, `asm:appO-mixing`, `asm:appO-deformation`, `asm:appO-rewritten-cs`, `asm:appN-collins`, `asm:appN-cutsum`, `asm:intro-bridge`, `asm:intro-composite`.
- **Named in status paragraphs only:** `asm:appN-envelope`, `asm:appN-separation`, `asm:appN-ward-product`, `asm:appN-values` (a convention, so it is now excluded from "all technical inputs are [A]"), `asm:appN-uv`, `asm:appN-multren`, `asm:appO-collinear-ends` (physical reading of the model theorem in `rem:dy-common-ordering`(iii)).
- **Named gap:** `asm:appN-brst-nonlocal` [C] is named in layer (3) of `thm:dy-factorization`'s status and recalled from `thm:method-template`. It is never in a `\uses` list (MD1).
- **R_cond:** no R_cond statement in Ch12. The R_cond implications are App O and App N labels, quoted with their tags.
- **Non-perturbative status lines:**
  - `thm:dy-factorization`: `asm:intro-bridge` (MA1, MA2, MA4).
  - `thm:dy-colour-singlet`: bridge (MA1, MA2).
  - `thm:dy-polarized`: bridge (MA1, MA2, MA4).
  - `thm:dy-higher-twist`: bridge (MA1, MA2).
  - `prop:dy-scale`: `asm:intro-composite` (MA0; needed only for hadronic DGLAP). This line was added; the outline gives none.
  - The conjectures and `prop:dy-twist6-failure` get no line: their master-table rows show "—".
  - Partonic, operator and model statements say so explicitly. For `prop:dy-born`(b)(c) the text states that they are algebraic consequences of the factorized form.

## 7. `\uses`
- **C5:** clean, so no pointer justifications are needed. Statements of later units appear only as text pointers, outside the environments.
- **Entries added beyond the outline:**
  - `prop:dy-born`: `def:pdf-antiquark`, `def:intro-factorization`.
  - `prop:dy-regions`: `def:ir-glauber`.
  - `lem:dy-fsi`: `lem:appO-cut-position`, `lem:appJ-cut-hermiticity`.
  - `prop:dy-deformation`: `prop:appO-ss-cancel`.
  - `prop:dy-abelian-model`: `prop:dy-glauber-pinch`.
  - `prop:dy-nlo`: `prop:dy-born`, `def:prelim-plus`, `prop:pdf-lo-kernels`.
  - `prop:dy-scale`: `lem:prelim-mellin`, `asm:intro-composite`.
  - `thm:dy-colour-singlet`: `prop:dy-regions`, `lem:dy-fsi`, `prop:dy-deformation`, `def:pdf-gluon`, `prop:appI-larin`.
  - `thm:dy-polarized`: `def:appI-hvbm`.
  - `conj:dy-coloured-final`: `def:pdf-ff`.
- **Order and cycles:** no forward edges (C4).
- **Hidden forward dependencies:** none. I walked the App O, App N, App C, App I and App J `\uses` graph from every appendix label used, and none reaches a chapter after Ch12.

## 8. Formulas
- **VF IDs used:**
  - VF-DY-1 to VF-DY-14, all 14 (each marked in a `%` comment).
  - VF-REF-8 (rem:dy-dft-premises), VF-REF-9 (prop:dy-eikonal-twogluon) and VF-REF-11 (ex:dy-future-vs-past); VF-REF-10 appears only in a figure caption.
  - VF-CONV-6; VF-DIS-7 (C₂ in rem:dy-dis-scheme); VF-SUD-1/2 through `prop:sudakov-oneloop`.
  - No T-status formula is used.
- **Writer-derived formulas and their checks** (scripts and logs under `writing/work/W14/`):
  - `p7_checks.py` → `logs/p7_checks.log`:
    - Beta-function v-integrals and averaging prefactors for qq̄ and qg, giving VF-DY-5 exactly.
    - Expansions of K_r, K_v, cos πε and f.
    - The imaginary part Im F⁽¹⁾ = −(α_sC_F/2)(1/ε + L + 3/2) + O(ε): the infrared Coulomb phase.
    - Every Laurent row, the pole sum = −2P_qq (checked at numeric z), and the finite parts equal to VF-DY-8.
    - Term-by-term N=1 moments (7, 4ζ₂ − 5/2, 4ζ₂ − 8; qg −13/9, 13/18, 5/6).
    - The large-N leading correction 4C_F ln N̄/N (ratios 0.931, 0.991, 0.9990, 0.9999).
    - The Moch–Vogt constant, the DIS-scheme identities, the plus trap and the 4-dim-Born normalization shift.
  - `dy_nlo_check.py`: finite parts at finite ε < 0 via test functions (to 2×10⁻¹¹, poles < 2×10⁻¹⁴), moments, large N, μ_F independence.
  - `glauber_model_check.py`: Glauber pinch residues and contour shifts, K₀ Fourier transform, the binomial cancellation, I_as, the future-pointing identity, LCOPT two-ordering identity and weights, the FFT demonstration numbers, VF-REF-8 and the orientation signs.
  - `eikonal_twogluon.py`: κ(Y) to 3×10⁻¹⁷, x_B residues against quadrature, outer integral to 2×10⁻¹⁶, brute-force iε extrapolation to 3×10⁻⁴, colour factors in SU(2) and SU(3) (all representation pairs), and normalization and p_opp.
    - I fixed check (6a) of this script: it used plain `mp.quad` on an oscillatory Bessel integrand and printed a spurious 7 % mismatch. It now uses `quadosc` and agrees to 15 digits.
- **Hand re-derivation:** I also re-derived by hand the Born normalization, the master formula, the one-loop pinch residues, the abelian (G-i) to (G-iv) results and the two-gluon box/crossed-box algebra.

## 9. Verification items
- **「本书新结果」:** none printed.
- **`prop:dy-eikonal-twogluon`:** printed as 「本书给出的推导」, citing `Meggiolaro:1996hf` (§3, eqs. (3.23)–(3.26), (3.28)–(3.34), (3.36)) and `Giordano:2006vv` (eq. (4.24)). Record: `verify/CLAIM_VERDICTS.md` N01.
- **Abelian model:** presented as our derivation of known results (Collins §14.3); novelty not claimed. Record: N25.
- **Candidate errata:** sign misprints in Meggiolaro eq. (3.35) and Giordano–Meggiolaro eqs. (4.15)–(4.21), (4.27). They are already recorded under N01; the text avoids those equations and prints nothing about them.
- **Spec error:** the outline's text for `rem:dy-dft-premises` is wrong (see item 13).

## 10. Citations
- **Keys (53):** AltarelliEllisMartinelli1979, AnastasiouEtAl2015, Andrasi:1980qw, AybatSterman2009, Basu:1984ba, BenekeBraun1995b, Bodwin1985 (its bib note prints the erratum, as the outline asks), BodwinBraatenLepage1995, BodwinBrodskyLepage1981, Brandt:1988xt, Caron-Huot:2013fea, Catani:1985xt, CataniDeFlorianRodrigo2012, Chang:1973qi, Cheng:1969eh, Collins2011, Collins:1985gm, CollinsSoperSterman1985b, CollinsSoperSterman1988, CollinsSoperSterman1989, Dawson1991, DiLietoEtAl1981, Diehl:2015bca, DjouadiSpiraZerwas1991, DoriaFrenkelTaylor1980, DrellYan1970, Duhr:2020sdp, Duhr:2020seh (addition), Frenkel:1983di, Giordano:2006vv, GrammerYennie1973 (attribution only, in tab:dy-status), HambergVanNeervenMatsuura1991, HarlanderKilgore2002, JaffeJi1991, Kang:2016mcy, Kastella:1989ux, Kogut:1969xa, Korchemskaya:1994qp, Korchemsky:1993hr, KubarAndrePaige1979, Labastida:1984gy, Ligterink:1994tm, Lindsay:1982gd, Lindsay:1982pu, Meggiolaro:1996hf, Moch:2005ky, MochVermaserenVogt2005, NasonDawsonEllis1988, NayakQiuSterman2005b, QiuSterman1991a, QiuSterman1991b, RalstonSoper1979, RothsteinStewart2016.
- **Aliases:** all merged keys; none needed resolving.
- **「文献待补」:** none. **Preprints:** none cited.
- **「位置待核实」:** none printed. Locations were verified as follows:
  - **Collins 2011:**
    - §5.6.2 (one-loop Glauber pinch and its power counting): from the chapter-5 text.
    - §§5.8–5.11: from the table of contents (section titles).
    - §14.3, eqs. (14.11)–(14.16), §14.3.3–14.3.4: from N25.
    - §14.4 p. 553, §14.4.7, §14.4.8, §14.7 pp. 570–571: from A13.
    - §14.4.1, §13.17 and §14.4.6: from SURVEY [txt].
  - **CSS 1989 (fetched arXiv text):** §8.7, §9.3 with eq. (166), §10.2.
  - **Rothstein–Stewart 2016 (fetched arXiv text):** §5.2.1, §11.1 (verbatim quote), eqs. (5.30), (9.1), (9.18), (9.19), (11.12)–(11.13).
  - **Others:** AybatSterman2009 eq. (14) (A11); Diehl:2015bca §4 and §5 (SURVEY [txt]); CdFR §8 and BBL 1995 §VI (SURVEY [txt]).
- **Quotations:**
  - Collins 2011 §14.7 contains the misprint "One of notable notable exception", so only the fragment "relative lack of detailed proofs" is quoted.
  - Collins' "formidable" sentence (§14.4.8) and the 14.4.7 BBL sentence are quoted from [txt] records.
- **Abstract-level claims, hedged with 「据其摘要」:** DFT ("color averaged", re-checked on INSPIRE), Di'Lieto, Andrási, FGT, CCM, Lindsay–Ross–Sachrajda, Brandt–Frenkel–Taylor, Basu–Ramalho–Sterman, Qiu–Sterman I/II, Kastella–Milana–Sterman, AEM (DIS scheme via "parton densities derived from lepton production"), Kubar-André–Paige, Beneke–Braun (checked against the arXiv abstract).

## 11. Figures
- **Copied verbatim** from `writing/packs/W14/figblocks.tex`, which is identical to `figures/figset_C.tex` (2026-10-11 00:06) and `research/tikz2/figures2.tex` (checked by diff): `fig:glauber-exchange`, `fig:dy-pole-orientation`, `fig:dy-abelian-model`, `fig:dy-two-gluon-exchange`, `fig:dy-oneloop`. All are referenced in the text; `fig:reduced-dy` (Ch4) is referenced back.
- **M31:** the required two-component-deformation sentence is placed at the first reference to `fig:glauber-exchange`.
- **New figures:** none drawn. **Placeholders:** none.
- **Caption issues** (LA-10: reported, not edited):
  - `fig:dy-abelian-model`: "冲量参数空间" should be "冲击参数空间".
  - `fig:dy-abelian-model`: the caption prints the internal IDs "（VF-DY-13，VF-GLA-3）".
  - `fig:dy-two-gluon-exchange`: the caption prints "（VF-REF-9，VF-REF-10）".
  - Proposed fix: delete these parentheticals in `figures/figset_C.tex`.

## 12. Boxes and tables
- **Opening box** 「本章证明了什么／没有证明什么」 uses the spec frame and follows the outline.
- **`tab:dy-status`:** rows (O-1) to (O-8) filled from `tab:appO-checklist`. Columns: step, statement, status, error type, assumptions, literature.
- **`tab:dy-correspondence`:** 9 rows. It covers the outline's pairs plus `ex:dy-future-vs-past`, `lem:dy-soft`, `prop:dy-abelian-model` and `rem:dy-common-ordering`(iii).
- **Extra:** `tab:dy-laurent` (the VF-DY-7 table inside the proof of `prop:dy-nlo`).
- **Misconception box (9 items):** M7, M30, M31, M32, M33, the q_T soft-factor item, M25, C11/O14 and O13.
  - It uses the §6.6 frame with the title 「本章涉及的常见误解」.
  - C8 and O13 are also answered in the status paragraphs of `lem:dy-fsi` and `lem:dy-soft`.
  - The "Rothstein–Stewart proved DY factorization" over-claim is answered in layer (1) of `thm:dy-factorization`'s status.

## 13. Deviations and spec errors
1. **Page count:** 32 pp against 18 pp (21.6 pp at +20 %).
   - Duplications with App O and verbose prose were removed, but all required content was kept: 30 statements, five verbatim figures (about 3.6 pp, two of them full-page), three tables, two boxes, full [R] proofs, the full NLO proof and the four-layer status.
   - LA-8 says completeness wins; the lead author decides.
2. **Condensed proofs of `prop:dy-eikonal-twogluon` and `lem:dy-poles-orientation`.** The outline's proof-delivery table assigns the full proofs to App O (§O.8 and §O.3, `lem:appO-orientation`). The chapter keeps all steps with every key intermediate formula and points to `sec:appO-wilson` and `sec:appO-orientation` (WRITER_SPEC §4.10 item 6).
3. **`rem:dy-dft-premises` follows the verified literature instead of the outline.**
   - The outline says DFT concerns "fixed colour" quarks whose terms "vanish after averaging over the colours of the incoming partons".
   - The DFT abstract (INSPIRE) and verify A14/A23 say the non-cancellation holds for massive, colour-averaged initial quarks. The power suppression comes from FGT and CCM, and m⁴/s² from CSS §10.2.
   - The text now says that colour-averaged external quarks are not equivalent to colour-singlet hadrons. The outline text needs a fix.
4. **Non-perturbative line added** to `prop:dy-scale` (`asm:intro-composite`, also in its `\uses`; global, no grade effect).
5. **Extra `\uses` entries** (item 7) and the own labels of item 3.
6. **`% errtype`** of the three process theorems set to E-S.
7. **Corrections to the earlier drafts p0–p6:**
   - **`\uses` rendering:** every `\uses{a, b}` printed "??" for every label after the first, because cleveref keeps the spaces. All label lists are now written without spaces.
   - **Typography:**
     - U+2032 in "(a′)" was missing from the font; replaced with `$'$`.
     - Seven overfull displays were split.
     - "式式 (n)" was printed 16 times (cleveref already prints 式); fixed.
     - The status table had floated above its own section heading; repositioned.
   - **Physics and attribution:**
     - The undefined "NF 区域" in `rem:dy-common-ordering` was replaced, and the `asm:appO-collinear-ends` caveat added.
     - The strict-window mechanism was reworded to follow `prop:appO-strict-window-shape`.
     - Verified attributions were added: Collins §5.6.2 and CSS §9.3 (eq. (166)) for the one-loop pinch; CSS §9.3 for the semi-classical colour-singlet picture; RS eq. (5.30).
     - `asm:appN-values` is now excluded from "all technical inputs are [A]".
   - **Bookkeeping:** "Brandt" and the DFT group are hedged as abstract-level, and a bookkeeping phrase was removed.

## 14. Open items for the lead author
1. **Page budget:** decide whether to accept 32 pp (+78 %) or name what to cut. Candidates are optional material only, e.g. `ex:dy-glauber-model` details, ex:dy-nlo (b)/(c), parts of `rem:dy-dft-premises`. No statements or proofs would be cut.
2. **Figure captions:** apply the fixes of item 11 in `figures/figset_C.tex`; the integrator's re-sync will propagate them.
3. **Outline text:** correct the `rem:dy-dft-premises` text in FINAL_OUTLINE_v2 (item 13.3), and check App O `rem:appO-dft` and Ch4 `prop:ir-bn-failure` for the same wording.
4. **Cross-unit check (LA-9):**
   - The App O writer must deliver the full proofs of `prop:dy-eikonal-twogluon` (§O.8) and `lem:appO-orientation` (§O.3). Ch12 now points to them.
   - The chapter's (O-1) to (O-8) table must stay consistent with `tab:appO-checklist`.
5. **Integrator:** merge `chapters/ch12_dy.bib-additions` (`Duhr:2020seh`).
6. **check_unit_v2.py:** C3 does not recognise `app:` and `ch:` chapter labels; consider extending its pattern.
7. **Future re-verification:** the statement that the RS SCET proof is unpublished uses the dated wording 「据我们截至 2026 年 10 月在 INSPIRE 上的文献检索」 (A06) and needs a repeated search at print time.

## open_items

1. Page budget: Ch12 is 32 pp against an 18 pp budget (21.6 pp at +20 %). All required content is kept. The lead author decides whether to accept this or which optional parts (example details) to cut.
2. Figure captions (LA-10, to fix in figures/figset_C.tex): in fig:dy-abelian-model replace '冲量参数空间' with '冲击参数空间' and delete '（VF-DY-13，VF-GLA-3）'; in fig:dy-two-gluon-exchange delete '（VF-REF-9，VF-REF-10）'.
3. Spec error: the outline text of rem:dy-dft-premises ('fixed colour … vanish after averaging over colours') contradicts the DFT abstract and verify A14/A23 ('colour averaged'). The chapter follows the verified literature; the outline should be corrected, and App O rem:appO-dft and Ch4 prop:ir-bn-failure checked for the same wording.
4. Cross-unit (LA-9): the App O writer must deliver the full proofs of prop:dy-eikonal-twogluon (§O.8, sec:appO-wilson) and lem:appO-orientation (§O.3), which Ch12 now points to; keep tab:dy-status consistent with tab:appO-checklist.
5. Integrator: merge chapters/ch12_dy.bib-additions (Duhr:2020seh, INSPIRE-verified).
6. check_unit_v2.py C3 flags app:appN and app:appO (appendix chapter labels, canonical by §5.1); the script's pattern does not include app:/ch: prefixes.
7. Repeat the INSPIRE search on the announced Rothstein–Stewart SCET proof at print time (dated A06 wording).

