# W06-write

(structured result persisted from wf_1b1b7a35-b6e)

## summary

I picked up the W06 draft left by the interrupted run, audited it against the spec, edited it, rebuilt it and ran QA. Both unit files are in chapters/. Both build cleanly: 0 errors, no overfull boxes, no undefined citations, no multiply defined labels, 0 BibTeX warnings. check_unit_v2.py passes C1–C8 for both units, except five C5 items in Ch6; each is justified as a pointer in the report. One limit is open: Ch6 is 20 pp, about 40 % over its 14-pp budget and beyond the +20 % that LA-8 allows. App C is about 3.6 pp, within tolerance. Physics: I hand-checked the derivations. All 109 earlier script checks pass on re-run, and 13 new checks pass in two new scripts (soft-subset enumeration and a numerical example). Main changes: (1) a new chapter opening with motivation, the physical picture and a roadmap. (2) A new worked example ex:ee-soft-sets, which enumerates the soft subsets of the two-loop graphs and replaces a sentence that was only verification bookkeeping. (3) Physics and precision fixes. Each Minkowski integral picks up factors of i, so the claim that c_n is real now rests on the Euclidean Π being real. The spectral weight is stated as a positive measure. The IR count now says H must be connected. In conj:ee-duality(a), R̄_PT no longer includes the OPE power terms, which had contradicted the O(Λ⁴/Δ²) remainder. cor:ee-cuts no longer claims an error type (E-S) for a gap that is an identity, not an estimate. The phrase about a non-perturbative "laboratory" in the status of conj:ee-np-ope is rewritten. The E29 history sentence now follows the verified wording. (4) Spec-compliance fixes: non-perturbative status lines on prop:ee-adler-dispersion and prop:ee-contour, the partonic remark on cor:ee-R-alphas, tags repeated at the first use of other units' statements, and forward pointers marked as such. (5) Missing key citations added: Adler, KLN, Frye et al., BM 1977a, Symanzik, Kinoshita–Ukawa, Chetyrkin–Tkachov, CKK review, ESW, MVV, and the verified English Collins quote. I re-checked the four bib additions on INSPIRE/Crossref and confirmed eq. (45) of Colangelo–Khodjamirian in the arXiv text. (6) A numerical π² illustration at √s = 20 GeV. (7) The two large figures were moved so they print in the text flow instead of on half-empty pages of their own, which saved about 0.8 page. (8) The flow chart was redrawn, and the App C kernel remark is clearer.

## files

1. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch06_ee.tex
2. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/appC_dimreg.tex
3. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/chapters/ch06_ee.bib-additions
4. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/parts/
5. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/assemble.py
6. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/w06_ir_example.py
7. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/w06_numeric_example.py
8. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/logs/
9. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/work/W06/logs_rerun/
10. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W06/test_ee.tex
11. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W06/test_ee.pdf
12. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W06/test_appC.tex
13. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W06/test_appC.pdf
14. /Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/writing/test/W06/png/

## pages

Ch06: 20 pp from the chapter title to the bibliography, which starts on p. 21 of test_ee.pdf. The last page is about 60 % full, so about 19.6 pp of content. Budget 14 pp; the LA-8 maximum is 16.8 pp; the overrun is about +40 %. AppC: 4 pp, about 3.6 pp of content (the bibliography starts on p. 5). Budget 3 pp, so +20 %, within LA-8.

## compile_status

Both drivers were built in writing/test/W06/ with xelatex, bibtex, then xelatex twice (AppC with \appendix). The bib is spec_v2/refs_merged_v2.bib plus chapters/ch06_ee.bib-additions. Results for test_ee and test_appC: LaTeX errors / undefined control sequences / emergency stops 0; Missing character 0; Overfull \hbox 0; undefined citations 0; multiply defined labels 0; BibTeX warnings 0. The only undefined references are canonical labels of other units, as expected in a standalone build. I rendered every page at 110 dpi (png/ee-01..20, png/c-1..4) and inspected all of them. Both large figures now print in the text flow, not on half-empty pages of their own.

## checker_output

check_unit_v2.py ch06_ee.tex Ch06: C1 OK; C1b OK; C2 OK; C3 OK (44 external refs, all canonical); C4 OK; C5 flags five items, all pointers, justified in report item 7: prop:ee-analytic→lem:ee-single-scale, thm:ee-euclid-ir→rem:ir-euclid-corners, thm:ee-R-finite→asm:intro-bridge and asm:intro-wightman, thm:ee-ope→asm:intro-np-ope, conj:ee-np-ope→asm:intro-np-ope; C6 OK; C7 OK; C8a OK; C8b OK. check_unit_v2.py appC_dimreg.tex AppC: C1, C1b, C2, C3 (11 external refs, all canonical), C4, C5, C6, C7, C8a, C8b all OK.

## report_markdown

# W06 report: Ch06 `ch06_ee.tex` and AppC `appC_dimreg.tex` (WRITER_SPEC_v2 §13)

Context: the previous run had left a complete, compiling draft and was interrupted before reporting. This run audited it line by line against LEAD_DECISIONS, WRITER_SPEC_v2 (read in full), the W06 pack and FINAL_OUTLINE_v2 §0, CONTEXT, REQUIREMENTS, the c_ee sources, CLAIM_VERDICTS (N24, E29, A09, A16, A23), REVIEW (O3, O21, M27) and refdoc S17. It then corrected, completed, rebuilt and QA'd the units. No SPEC_V24_DELTA file exists, and FINAL_OUTLINE_v2 has had no changes since the pack was built.

## 1. Files, page counts, compile status
- `chapters/ch06_ee.tex`: 832 lines. 20 pp from the title to the bibliography (last page about 60 % full, so about 19.6 pp of content). Budget 14 pp; LA-8 allows at most 16.8 pp; the overrun is about +40 % (see item 13).
- `chapters/appC_dimreg.tex`: 133 lines. 4 pp (about 3.6 pp of content). Budget 3 pp, so +20 %, within LA-8.
- `chapters/ch06_ee.bib-additions`: 4 entries (item 10).
- Build (writing/test/W06; xelatex, bibtex, xelatex ×2): errors 0, missing characters 0, overfull boxes 0, undefined citations 0, multiply defined labels 0, BibTeX warnings 0. All pages were rendered at 110 dpi and inspected.
- Sources: parts in `writing/work/W06/parts/` are joined by `assemble.py`; figure blocks are inserted verbatim through `%%FIG:` markers.

## 2. Canonical labels and checker
- All 24 canonical Ch06 statements are implemented in outline order, with exact labels, types, titles, tags and qualifier sentences: def:ee-R, prop:ee-R-ImPi, lem:ee-single-scale, prop:ee-analytic, def:ee-adler, prop:ee-adler-dispersion, thm:ee-euclid-ir, prop:ee-adler-rg, thm:ee-R-finite, prop:ee-oneloop, ex:ee-quark-spectrum, prop:ee-twoloop, ex:ee-twoloop-route, prop:ee-cutting-exact, cor:ee-cuts, prop:ee-contour, cor:ee-R-alphas, ex:ee-pi2, rem:ee-status-layout, thm:ee-ope, conj:ee-np-ope, rem:ee-complex-ope, prop:ee-smearing, conj:ee-duality.
- All 8 canonical sec:ee-* labels, the 3 figure labels and ch:ee are present.
- App C: rem:appC-Seps, rem:appC-d-kernels, lem:appC-bubble, lem:appC-ibp, lem:appC-phase-space, the 4 sec:appC-* labels and app:appC are present.
- Nothing is missing.
- check_unit_v2.py: Ch06 C1–C4, C6–C8 OK; C5 lists five pointers (item 7). AppC: everything OK.

## 3. Additional labels
- `ex:ee-soft-sets` (例，no tag; `\uses{thm:ee-euclid-ir}`), new in this run. It is a worked example of the IR-degree count: the nine soft subsets of the two-loop gluon-exchange graph and the hard-island case of the self-energy graph. The enumeration is in w06_ir_example.py.
- `rem:ee-misconceptions` (注，no tag), from the earlier draft: the misconception box (M27, the O(α_s²) singlet term, "finiteness from DR").
- Equation labels:
  - `eq:ee-cGamma, -Rdef, -Pidef, -Wdef, -RImPi, -ImPi0, -rho, -Rratio, -single-scale, -F0, -KL, -once, -geom, -adler-disp, -PiMS, -irdeg, -irdeg2, -rge-eps, -arun, -structure, -virt, -real, -R1, -realme, -xspec, -Pi2bare, -PiMSbar, -topo, -cutexact, -contour, -Rexp, -rn-dn, -r3, -ope, -ope-coeff, -adler-ope, -smearing`
  - `eq:appC-expansions, -kernels, -master, -bubble, -tensor, -ibp, -PS2, -PS3, -ffred, -FF, -FFMS, -FFtime`
- No auxiliary lemmas were added.

## 4. External labels referenced (all canonical; C3 OK)
- Ch06: asm:intro-bridge, asm:intro-np-ope, asm:intro-wightman, def:intro-tags, def:ir-landau-setup, def:pdf-ff, def:prelim-dr-conventions, def:prelim-feynman-rules, def:prelim-msbar, def:qcd-dimreg, ex:prelim-vacpol, lem:appC-bubble, lem:appC-ibp, lem:appC-phase-space, lem:prelim-scaleless, prop:power-adler-large-beta0, prop:prelim-optical, prop:prelim-rg, prop:prelim-unitarity, prop:qcd-rge, prop:qcd-superficial-degree, prop:qcd-xi-independence, prop:sudakov-oneloop, rem:front-ope-qcd-status, rem:ir-euclid-corners, rem:prelim-cutting-dr, sec:appC-formfactor, sec:appG-ee, sec:appM-massless, sec:appM-np, sec:appQ-errata, sec:dis-ope, sec:ir-landau, sec:ir-pinch, sec:power-renormalons, tab:front-notation, thm:coll-sia, thm:dis-ope, thm:heavy-inclusive-b, thm:ir-kln, thm:method-template, thm:prelim-composite-renorm, thm:prelim-cutting-rules, thm:qcd-renormalizability.
- AppC: def:prelim-dr-conventions, def:prelim-msbar, def:qcd-dimreg, lem:prelim-scaleless, prop:disall-nlo, prop:dy-nlo, prop:ee-oneloop, prop:ee-twoloop, prop:pdf-lo-kernels, prop:sudakov-oneloop, rem:tmd-scheme-constants.
- Later-chapter labels (thm:dis-ope, def:pdf-ff, thm:coll-sia, thm:heavy-inclusive-b, thm:method-template, prop:power-adler-large-beta0, rem:front-ope-qcd-status, sec:dis-ope, sec:power-renormalons) appear only as forward pointers in running text, marked 「后文」. None is in any `\uses`.

## 5. Tags
All tags are exactly those of the outline; none was weakened or strengthened.
- [R, R_def]: prop:ee-R-ImPi, prop:ee-analytic, prop:ee-adler-dispersion, prop:ee-contour, prop:ee-smearing.
- [R, R_PT]: lem:ee-single-scale, thm:ee-euclid-ir, prop:ee-adler-rg, thm:ee-R-finite, prop:ee-oneloop (first sentence after the qualifier: "单圈，即 O(α_s)"), prop:ee-twoloop ("两圈，即 O(g_0²)"), prop:ee-cutting-exact ("O(g_0²) 阶"), cor:ee-R-alphas.
- [A]: cor:ee-cuts, thm:ee-ope. [C]: conj:ee-np-ope, conj:ee-duality.
- No tag: def:ee-R, def:ee-adler, the four examples, rem:ee-status-layout, rem:ee-complex-ope, rem:ee-misconceptions.
- App C: the remarks carry no tag; the lemmas are mathematics with no tag.
- Grade propagation: no conflicts.
  - R_def statements use only R_def premises and global asm:intro-* entries. This is why lem:ee-single-scale ([R, R_PT]) stays a pointer in prop:ee-analytic.
  - R_PT statements use R_def/R_PT/math/definitions only.
  - The [A] statements use rem:prelim-cutting-dr [A] and R_PT premises.
- Every [A]/[C] statement is followed by a 「地位与缺口」 paragraph.
- At the first use of each tagged statement of another unit, its tag is repeated: prop:prelim-optical, thm:qcd-renormalizability, prop:qcd-superficial-degree, prop:qcd-xi-independence, prop:qcd-rge, prop:prelim-rg, prop:sudakov-oneloop, thm:prelim-cutting-rules, prop:prelim-unitarity, thm:prelim-composite-renorm, thm:ir-kln, and the [A] forward pointers.
- No forbidden phrasing (manual grep and C8b).

## 6. Assumptions
- None defined (neither unit owns one).
- Used:
  - asm:intro-wightman: in `\uses` of prop:ee-R-ImPi, prop:ee-analytic, prop:ee-smearing (as in the outline) and of prop:ee-adler-dispersion and prop:ee-contour (added, item 13).
  - asm:intro-bridge: in the status line of thm:ee-R-finite.
  - asm:intro-np-ope: box, conj:ee-np-ope (identified as its vacuum part), rem:ee-complex-ope, and a pointer in the proof of thm:ee-ope.
- No R_cond statements in these units.
- Non-perturbative status lines:
  - prop:ee-R-ImPi, prop:ee-analytic, prop:ee-smearing: MA0.
  - thm:ee-R-finite: MA0 and MA1+MA2.
  - prop:ee-adler-dispersion, prop:ee-contour (added): MA0 for hadronic spectral functions, none at fixed order.
- Partonic remarks on every R_PT/A statement; added to cor:ee-R-alphas.
- The conjectures have no status line, consistent with master rows II.6 and II.7 (column "—"); they are the non-perturbative claims themselves.

## 7. `\uses`
C5 items, each a pointer and not a proof step:
- prop:ee-analytic → lem:ee-single-scale: comparison sentence. It cannot be a premise, because an R_def statement may only use R_def premises.
- thm:ee-euclid-ir → rem:ir-euclid-corners: identification remark ("these are exactly the Landau solutions of …").
- thm:ee-R-finite → asm:intro-wightman, asm:intro-bridge: named only in the 「非微扰地位」 line, as §4.4(6) and the register's "names it" rule intend. The outline's `\uses` excludes them.
- thm:ee-ope → asm:intro-np-ope: parenthesis on the non-perturbative vacuum, which is outside the [A] perturbative claim.
- conj:ee-np-ope → asm:intro-np-ope: identification ("its vacuum part"), not a premise.

Additions to the outline's `\uses` lists. All are earlier-chapter, earlier-same-unit, appendix or global labels and grade-compatible; there are no forward edges or cycles.
- thm:ee-euclid-ir: + prop:qcd-superficial-degree, lem:prelim-scaleless.
- prop:ee-adler-rg: + lem:ee-single-scale, thm:ee-euclid-ir.
- prop:ee-adler-dispersion: + prop:ee-R-ImPi, asm:intro-wightman.
- prop:ee-oneloop: + prop:ee-R-ImPi.
- prop:ee-twoloop: + def:prelim-feynman-rules.
- prop:ee-contour: + def:ee-adler, asm:intro-wightman.
- thm:ee-ope: + prop:ee-twoloop.
- ex:ee-soft-sets (new): {thm:ee-euclid-ir}.
- App C lists are exactly the outline's.

## 8. Formulas
VF IDs used, with `%` comments at the formulas:
- Ch6: VF-CONV-12, VF-EE-1, -3, -4, -5, -6, -7, -8, -9, -10, -11, -13, -14, -15, VF-QCD-7.
- App C: VF-CONV-4, -6, VF-DY-4, VF-EE-4, -5, -7, VF-PDF-6, VF-SUD-1, VF-SUD-2.
- No T-status formula was used.
- VF-EE-13 and VF-EE-14 (status A) were re-derived: the IR count by w06_ir_degree S1–S3 and w06_ir_example; the analyticity statements by w06_analytic K1–K7.
- VF-EE-10, general-group form (status C), is quoted as literature. Baikov–Chetyrkin–Kühn 2010 is the verified location (A16); the reduction to SU(3) was checked (rg_contour N2a).

Writer-derived or writer-checked formulas, with their scripts. Logs are in `writing/work/W06/logs/` and `logs_rerun/`; all re-run in this session: 109 checks plus 13 new ones, all PASS.
- IR degree d = A + ½A_q ≥ 2, and the nine soft sets of the two-loop graph V and the hard-island case: w06_ir_degree.py, w06_ir_example.py.
- One-subtraction equivalence, (s+Q²)⁻² ≥ (2s)⁻², dispersion relation, contour formula, smearing identity and its LO example R₀[1−arctan(Δ/s)/π]: w06_analytic.py.
- Four-loop expansion of a(Q²) (5/2·b₀b₁), polynomial degrees, r₃ and r₄ in terms of d_n via two independent continuations: w06_rg_contour.py.
- Exact real and virtual closed forms, the warning factor Γ²(1−ε)/Γ(1−3ε) = c_Γ(1−π²ε²/2), quark-spectrum pole and moments 0, 4/3, 25/12, 157/60: w06_ee_oneloop.py.
- Per-diagram two-loop poles V and S₁+S₂ (not in VF), Ward identity, exact r₁ and r₂: w06_twoloop_diagrams.py.
- Cutting identity, term by term and analytically; Î(1,1,1,1,1) = 6ζ₃: w06_twoloop_cut.py.
- OPE coefficients C_q = 2e_q², C_G = e_q²/12, m_q² term −N_c e_q² m²/(2π²Q²), and the Adler-function OPE coefficients 48π² and 2π² (not in VF): w06_ope_coeffs.py; cross-checked against Colangelo–Khodjamirian eq. (45), which I read in the arXiv text this session.
- r₃ numerics, singlet coefficient −1.2395, d₃ = 6.371, 2.593, −0.719, (π²/3)b₀² = 16.655, 14.279, 12.086: w06_pi2_table.py, rg_contour N1–N5.
- α_s(20 GeV) = 0.1533 (matches the VF-QCD-7 table), and the series terms 0.0488, 0.0034, −0.0015, of which the π² part is −0.0014: w06_numeric_example.py.
- App C: e^{εγ}c_Γ and Γ(1−ε)c_Γ expansions, the S_ε comparison, the form-factor reduction F = ig₀²C_F[2sJ(1,1,1)+(7−D)J(0,1,1)], tensor formula A_t (m ≤ 4), IBP, phase spaces, the four D-dimensional kernels and their n-independence, and the +P_qg shift: w06_appC_checks.py, w06_twoloop_cut.py, w06_twoloop_diagrams.py, w06_ee_oneloop.py.

## 9. Verification items
- No 「本书新结果」 is printed. The cutting identity and the route to finite R are printed as 「本书给出的推导」 with novelty not claimed (N24/K4).
- The E29 history sentence follows the verified printable version: GKL 1988 was incorrect; it was corrected in 1991 by Surguladze–Samuel and by GKL; this is 「附录~Q 第~20~条」 (LA-6).
- No new candidate errata.

## 10. Citations
- 63 keys in Ch6 and 6 in App C.
- New since the earlier draft: Adler1974, Kinoshita1962, LeeNauenberg1964, Frye:2018xjj, EllisStirlingWebber1996, ChetyrkinKuhnKwiatkowski1996, BreitenlohnerMaison1977a, Symanzik1973, KinoshitaUkawa1976, ChetyrkinTkachov1981, Tkachov1981, MochVermaserenVogt2005, ParticleDataGroup:2024cfk.
  - Each is supported by REFS_NOTES/SURVEY entries; some only at [abs] level, and they are used accordingly (e.g. Symanzik and Kinoshita–Ukawa only as "early systematic analyses of IR singularities of massless amplitudes"; Frye only for "one-sided sums suffice but need forward scattering", per A23).
- Bib additions (LA-14), with texkeys and DOIs re-checked on INSPIRE and the title on Crossref in this session: Gorishnii:1988bc (PLB 212 (1988) 238), Baikov:2010je (PRL 104 (2010) 132004), Furry:1937zz (PR 51 (1937) 125), Colangelo:2000dp (hep-ph/0010175, Handbook of QCD vol. 3).
- Printed locations:
  - Colangelo:2000dp eq. (45): verified in the arXiv text, with the same correlator definition as VF-CONV-12.
  - Collins1984 §12.8 (with the verified English quote) and IzubuchiEtAl2018 Sec. II: per A09.
  - ParticleDataGroup:2024cfk eq. (9.25): per VF-QCD-7.
- Collins2011 is cited without a location in rem:appC-Seps, because the §3.3.2 location in VF-CONV-4 is second-hand (LA-7).
- Attributions follow A16: CKT and DS for MS-bar r₂; Celmaster–Gonsalves in the MOM scheme; BCK 2010 for the general group. The Radyushkin1996 trap is avoided by citing KrasnikovPivovarov1982 and KataevStarshenko1995.
- No 「文献待补」, no 「位置待核实」, no preprints cited.

## 11. Figures
- fig:ee-oneloop (from research/tikz2), fig:ee-pi-plane (figures/figset_A) and fig:ee-cutsum-disc (figures/figset_B) are copied verbatim from writing/packs/W06/figblocks.tex (11 Oct, 13:00). I checked programmatically that each block is identical to the pack.
- Only the positions of the blocks were changed, after a placement experiment, so that LaTeX prints them in the text flow instead of on half-empty pages of their own: fig:ee-oneloop now follows ex:ee-quark-spectrum, and fig:ee-cutsum-disc follows the r₃ paragraph, preceded by the paragraph that introduces it. Each figure is referenced in the text.
- No figure errors found; the captions are consistent with the text (Furry remark included).
- The flow chart required at the start of sec:ee-theorem is the writer's own unnumbered TikZ. It was redrawn with wider nodes and a dashed edge from the O(α_s) computations to cor:ee-cuts.

## 12. Boxes and tables
- The 「本章证明了什么／没有证明什么」 box is right after the opening and matches the outline, with "微扰 R(s) 的逐点意义" added under 没有证明.
- No correspondence table or status table is required for Ch6 or App C.

## 13. Deviations, and spec issues found
1. **Page budget.** Ch6 runs to about 19.6 pp against an LA-8 maximum of 16.8 pp.
   - Why: 24 canonical statements with complete proofs of all [R] statements (the IR count, the RG argument, the polynomial-continuation proof, real/virtual closed forms, the exact cutting identity), three required figures (two large), the required flow chart and the worked examples.
   - Already done: the two half-empty figure pages were eliminated, saving about 0.8 pp.
   - If a cap is imposed, the permitted cuts are: ex:ee-soft-sets (about 0.25 pp), the numerical sentence in ex:ee-pi2, the per-diagram pole display in the prop:ee-twoloop sketch (could go to App G), the m_q-term detail in the thm:ee-ope sketch, the roadmap sentence. Together about 0.8–1 pp. Proofs of [R] statements may not be shortened (LA-8).
2. The `\uses` additions listed in item 7.
3. Non-perturbative lines added to the hadron-level R_def statements prop:ee-adler-dispersion and prop:ee-contour (§4.4(6)).
4. prop:ee-analytic(b): the outline's "⟺ the Adler function is finite at one Euclidean point" is made precise as convergence of the dispersive integral Q²∫R/(s+Q²)². With N subtractions the derivative of Π always exists, so the outline's wording is imprecise.
5. cor:ee-cuts status paragraph: it says the error-type classification does not apply, because the gap is the proof of an identity, not a power-counting estimate. The earlier "% errtype: E-S" was removed.
6. thm:ee-ope states the leading coefficients C_q, C_G and the m_q² term (writer-derived and checked; item 8).
7. The general-group r₂ is cited to Baikov:2010je (A16), with CKT, DS and CG cited for the SU(3) value.

Spec issues found:
- FINAL_OUTLINE rem:appC-Seps cites "(VF-CONV-3)" for scheme-independence of cross sections; it should be VF-CONV-4.
- The imprecision in item 4.

## 14. Open items for the lead author
See open_items.


## open_items

1. Page budget: Ch6 is about 19.6 pp of content (20 pp to the bibliography) against 14 pp (LA-8 maximum 16.8 pp). Please decide whether to accept it or to cap; if capping, the permitted cuts are listed in report item 13.1 and save about 0.8–1 pp. App C (about 3.6 pp) is within tolerance.
2. App G writer (W29): prop:ee-twoloop's proof sketch ends with 「完整论证见\cref{sec:appG-ee}」. sec:appG-ee should contain the diagram-by-diagram two-loop details (traces, topology (1,1,1,1,1)/(2,1,1,0,1)/(1,2,0,1,1), IBP reduction, per-diagram poles V and S1+S2 as printed in Ch6).
3. App Q writer (W30): row 20 (E29) should match the Ch6 history sentence. GKL PLB 212 (1988) 238 (key Gorishnii:1988bc, added in ch06_ee.bib-additions) was corrected by Surguladze–Samuel PRL 66 (1991) 560 and GKL PLB 259 (1991) 144. Ch6 cites \cref{sec:appQ-errata}, because tab:appQ-errata-b is not in the registry.
4. Ch7 writer (W07): thm:ee-ope's status paragraph says the full OPE-status discussion is repeated at thm:dis-ope and refers back here; please keep these consistent (A09 wording). Ch24 rem:front-ope-qcd-status is cited as a forward pointer.
5. Integrator: merge chapters/ch06_ee.bib-additions (Gorishnii:1988bc, Baikov:2010je, Furry:1937zz, Colangelo:2000dp; all re-verified on INSPIRE/Crossref on 2026-10-14). The positions of the figure blocks in ch06 were tuned so that both large figures print in the text flow; if a figure re-sync changes a block's height, the placement may need re-checking (the blocks themselves are verbatim).
6. Spec fix suggestion: FINAL_OUTLINE_v2 rem:appC-Seps cites '(VF-CONV-3)' where VF-CONV-4 is meant. The prop:ee-analytic(b) wording 'Adler function finite at one Euclidean point' should read 'the one-subtracted dispersive integral for the Adler function converges at one Euclidean point', as implemented in the unit.
7. Cross-unit consistency to confirm at review: Ch3 rem:prelim-cutting-dr ([A]) and ex:prelim-vacpol; Ch2 prop:qcd-superficial-degree ([R, R_def]); and Ch4 rem:ir-euclid-corners are used as stated in Ch6 (the IR count d=A+A_q/2 and the zero-momentum Landau solutions).

