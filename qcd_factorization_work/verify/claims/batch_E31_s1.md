# Verification batch E31–E36 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims E31–E36 of `verify/CLAIMS.md` (sources: `research/survey/SURVEY.md` item 8;
`spec/FINAL_OUTLINE.md` lem:dy-fsi; `research/critic/REVIEW.md` §6, §10 c2; `research/c_dis/DERIVATION.md` §11;
`frontier/others/OTHERS.md` App. A, §4.1–4.3, §4.7, §5.2, §6, §7, §9.2, §9.5; `refdoc/REFDOC_ANALYSIS.md` ERR-M30).

## 0. Method and sources

* **Primary literature was downloaded independently** (untrusted data, read as text or rendered pages; nothing executed from it except
  LaTeX compiles with `-no-shell-escape` to obtain equation numbers).
  * Collins, *Foundations of Perturbative QCD*, open-access reissue (CUP 2023, doi:10.1017/9781009401845): chapter 14 PDF
    (pp. 540–572) and the full-book PDF (640 pp., PDF creation date 2013-01-16; copyright page "First published 2011, Reissued as OA 2023").
    The whole book text was searched.
  * BBDM: Bardeen–Buras–Duke–Muta, FERMILAB-Pub-78/42-THY (= PRD 18 (1978) 3998), INSPIRE-hosted scan; pp. 17, 18, 27, 28 rendered as images.
  * Buras, FERMILAB-Pub-79/17-THY (= RMP 52 (1980) 199), INSPIRE-hosted scan; p. 33 rendered.
  * Floratos–Ross–Sachrajda NPB 152 (1979) 493, KEK scan (text only).
  * Vermaseren–Vogt–Moch arXiv:hep-ph/0504242 (source); Blümlein–Marquard–Schneider–Schönwald arXiv:2208.14325 (source).
  * DGOPS arXiv:1510.08696 (source).
  * For E33: arXiv sources/abstracts of every revised version: 0901.0722 v1–v3 (compiled v1), 0903.1126, hep-ph/9407339v2 (file `erratum.tex`),
    hep-ph/9709499 v1/v2 (PDFs, figure pages rendered), 1912.09370 v1/v2, 2109.03665 v2/v3, 1605.02737 v2/v3, 1412.0671 v1/v4,
    hep-th/0002245 (BBH review); arXiv API comments for 2112.07680, 2204.03856, 1511.06737, 2204.11898, 1911.12040, 1111.0910, 1312.0058, 1708.03528.
  * For E34: 2009.06779v2, 2306.09495v3, 0710.4330v1 (only version), 2304.06161v1, hep-ph/9603204, hep-ph/9507271, 0812.3416, 1309.7644, 1305.1924.
  * For E35: 2111.01170v2 (= PRD version; compiled for equation numbers), 2006.07377v2 (= JHEP final; compiled), 2308.00025 v2 (≈ EPJC) and v4.
  * For E36: 1801.01138v2, 1405.2080v1, 1601.04695v3 (source + arXiv PDF), 1507.01652v2, and three citing papers (2607.14259, 2207.06507, 2307.02521).
* **Not accessible** (no circumvention attempted): CSS 1988 NPB 308 (1988) 833 (ScienceDirect 403; no KEK scan; CERN CDS behind a bot check);
  the published journal texts of the paywalled errata (PRD 34 (1986) 3932, NPB 213 (1983) 545, PLB 316 (1993) 633, ZPC 42 (1989) 504, NPB 139 (1978) 545);
  Springer pages of JHEP errata (client challenge). Where I relied on arXiv revisions instead of the erratum text, this is said.
* INSPIRE API: publication data and erratum records for all papers; citing papers of SYZ 2018 (36) and Borden–Kovchegov 2023 (43).
* **My own scripts** (in `verify/claims/batch_E31_s1_scripts/`, run with `python3 -I`, outputs saved as `*.out.txt`):
  `e32_moments.py`, `e34_helicity.py`, `e35_yukawa.py`, `e35_roots.py`. The project script `frontier/others/scripts/s2_crs_yukawa_pdf.py`
  was re-run from a scratch copy (10/10 PASS; output `rerun_project_s2_crs_yukawa_pdf.out.txt`).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E31 | **confirmed** (as a quotation/attribution only) | Print it as Collins's own assessment. Collins nowhere identifies the "errors" (CSS 1988 is cited only on pp. 553, 558, 560), and CSS 1988 was not accessible. Do not list or characterise specific errors of CSS 1988. The improvements Collins does describe can be named (sec. 2). | The quotation is Collins 2011 p. 553. No published list of the corrected errors was found. |
| E32 | **refuted** as an erratum (the correct formula is confirmed) | Drop the "commonly quoted variant" sentence: no printed source exists in BBDM, Buras RMP, FRS, VVM or Blümlein et al. 2022, and the critic's own script calls the variant `misremembered`. Print the correct C^{q,(1)}_{2,n} with its sources and the Adler check (which BBDM already state). | Correct form: BBDM eq. (3.9) (MS; drop the γ̃(ln4π−γ_E) term for MS-bar), Adler sum rule "exactly satisfied" in BBDM eq. (4.10); Buras eq. (2.96); VVM eq. (A.3); Blümlein et al. 2022. |
| E33 | **confirmed** (all 18 errata exist); contents now examined for 13 | **OTHERS §4.3 quotes the pre-erratum DHYZ conclusion. The erratum reverses it: the terms "cancel after summing over colors".** Other errata do not affect formulas we quote (table in sec. 4). Three further errata in our material are missing from the list: Erdoğan 2014, Surguladze–Samuel 1991, Buffing–Diehl–Kasemets 2018. Side finding: the dipole formula is eq. (7), not "(2)", of Becher–Neubert 2009. | Published errata (INSPIRE); contents read from the arXiv revisions. |
| E34 | **confirmed** (all four reports are accurate) | (i) Sharpen: the disagreement concerns the subleading logs (k = 5 at three loops; the NLL series αα_s^nL^{2n+1}) of Akhoury–Wang–Yakovlev 2001 and Anastasiou–Penin 2020. (iii) Add that BC traced the ζ(3) mismatch to the cutoff, and that later BC work ("composite conformal dipole") reports agreement with NLO BFKL. (iv) BER themselves quote only "z = 3.66". 3.66394 = √((17+√97)/2) is the analytic value of BER's pure-glue formula (first given by Kovchegov–Pitonyak–Sievert 2017). Verified: four-loop coefficients 496 (BK) vs 504 (BER) in ā⁴/ω⁷. | All four are the papers' own statements. |
| E35 | **confirmed**, one numerical correction | At μ = 0.8 GeV the PDF is negative for **ξ ∈ (0.2640, 1)**, not "[0.28, 0.98]" (that range comes from the project script's 0.02 grid). f > 0 for all ξ iff μ > μ_* = 1.699 GeV. The bare-positivity step is in CFH §2, right after the operator definition (JHEP eq. (2.2)), and it is used in §3.1. | CRS PRD 105 (2022) 076010 eqs. (55)–(59), Sec. VI, Sec. VIII B; CFGH EPJC 84 (2024) 335 (Q² ≳ 5 GeV²). |
| E36 | **confirmed**, wording to refine | Gaunt's claim has two parts: (a) the CSS cancellation *argument* fails at two S–S Glauber gluons for E_T; (b) he *suggests* that factorization fails at LP for MPI-sensitive observables. SYZ contradict only the pure-Glauber part, and agree that violation can arise from soft emission off the rungs. "The claims survive for multi-differential observables" should read: RS's general statement (any observable constraining Δp_⊥) is not contradicted outside SYZ's scope. "Disputed" means no rebuttal of SYZ was found. | SYZ PRD 97 (2018) 096017 abstract and Sec. 3.2; RS §11.1 (eq. (11.13) and the paragraph after it); Gaunt JHEP 07 (2014) 110; Zeng JHEP 10 (2015) 189. |

---

## 2. E31 — CSS 1988 "with correction of errors" (Collins 2011 §14.4, p. 553)

**Quotation (verified verbatim, OA reissue p. 553, first paragraph of §14.4 "Factorization for Drell-Yan"):**
> "For the general treatment of the Glauber region, I will follow the proof given by Collins, Soper, and Sterman (1988), but with some
> important improvements and with correction of errors. That reference supersedes earlier work (Bodwin, 1985; Collins, Soper, and Sterman, 1985a)."

The TOC of the reissue puts §14.4 at p. 553. The reissue PDF is the 2013 production file, and its index gives "Drell-Yan process … factorization, 553–562".
I did not see a 2011 printing; standard reprint practice keeps the pagination.

**Bibliographic identification (Collins's bibliography, pp. 606 and 608):** "Bodwin G. T. (1985). Factorization of the Drell-Yan cross-section
in perturbation theory. Phys. Rev. D31, 2616–2642. Erratum: D34, 3932 (1986)"; "Collins J. C., Soper D. E., Sterman G. (1985a). Factorization
for short distance hadron-hadron scattering. Nucl. Phys. B261, 104–142"; "(1988). Soft gluons and factorization. Nucl. Phys. B308, 833–856".
These match the claim's literature list. INSPIRE agrees (Bodwin:1984hc with erratum record; Collins:1985ue; Collins:1988ig, report ITP-SB-87-69).

**"Identify the errors corrected" (recipe) — result: they are not identified anywhere in the book.**
A search of the full text shows CSS 1988 is cited exactly three times: p. 553 (above), p. 558 and p. 560. None of the three names an error.
The *improvements* Collins describes (none labelled an error) are:
1. p. 558: the remainder factor R is independent of the cut placement V of the soft vertices. "A proof of this result (CSS 1988) can be made by
   examining x⁻-ordered perturbation theory for R … Instead I will show here an argument that uses commutators for the gluon field": the fields are
   at space-like separation and commute in Feynman gauge.
2. p. 560, §14.4.5: "the treatment of the Glauber region was originally formulated (CSS 1988) only in the context of situations using integrated parton
   densities … In fact, the argument works equally well for the TMD case."
3. pp. 560–561, §14.4.6: "there is one step that needs enhancement … cancellation of the soft factor". Drell–Yan gives past-pointing Wilson lines,
   and T invariance (§13.17.5) equates them with future-pointing ones. Related: §14.4.1 step 5 uses a Grammer–Yennie approximant with past-pointing
   Wilson lines, compatible with the deformation "away from initial-state singularities".

DGOPS 2016 (arXiv:1510.08696, §2 "Approximations for soft gluons") adds two technical differences. CSS 1988 used l̃ = (0, l⁻, 0_T), i.e. δ = 0 in
Collins's §10.4.2 approximant. CSS 1988 §3.2 neglected l_T in A by "a specific routing of loop momenta". DGOPS say they "revisit and clarify some
subtle issues in the single Drell-Yan case". They do not call these errors either.

**Verdict: confirmed as an attribution.** The monograph may print, attributed to Collins, that §14.4 follows CSS 1988 "with some important improvements
and with correction of errors" and that CSS 1988 supersedes Bodwin 1985 and CSS 1985a. FINAL_OUTLINE's paraphrase 「Collins (2011) §14.4 在 CSS 1988
基础上改进并纠正了若干错误」 is acceptable only if attributed ("据 Collins 所述"). It must not imply that we identified or checked any error of CSS 1988.

---

## 3. E32 — one-loop moments C^{q,(1)}_{2,n} and the "commonly quoted variant"

**Independent computation** (`e32_moments.py`, normalisation a_s = α_s/4π, S_k ≡ S_k(n)):
* x-space input: VVM eq. (4.3), c^{(1)}_{2,ns}(x) = C_F{4D₁ − 3D₀ − (9+4ζ₂)δ(1−x) − 2(1+x)(L₁−L₀) − 4L₀/(1−x) + 6 + 4x}.
  Its Mellin moments were computed numerically (40 digits) for n = 1…12 and compared with the closed form
  **C_F[2S₁² − 2S₂ + 3S₁ − 2S₁/(n(n+1)) + 3/n + 4/(n+1) + 2/n² − 9]**. Worst residual 4×10⁻⁴⁰. Values/C_F: 0, 1/3, 29/12, 91/20, 589/90, … .
* Non-integer n (0.7, 1.5, 2.25, 5.5, 13.3), using the continuation S₁ = ψ(n+1)+γ_E, S₂ = ζ₂ − ψ′(n+1): residuals ≤ 10⁻²⁹.
* VVM eq. (A.3), C_F(9(S₁−1) + 2γ_qq(S₁,₁ + 2S₁ − S₂) − 7(N₋+1)S₁) with γ_qq = N₊+N₋, equals the closed form exactly for n = 1…30, odd n included.
* Large n: the closed form − C_F[2ln²N̄ + 3lnN̄ − 9 − 2ζ₂] → 0 like ln n/n (0.034, 4.6×10⁻⁴, 5.9×10⁻⁶ at n = 10³, 10⁵, 10⁷).
* **n = 1: closed form = 0 (Adler); variant (2/(n+1) + 1/n²) = −2C_F = −8/3.** The difference is C_F[2/(n+1) + 1/n²].
  Cross-checks at n = 1: c₂ − c_L = −2C_F a_s = −(2/3)α_s/π (Bjorken sum rule for F₁); c₃ = c₂ − 2C_F(1+x) gives −3C_F a_s = −α_s/π (GLS).
  Both agree with BBDM eqs. (4.11), (4.12).
* The variant is not any other standard one-loop moment: it differs from c₂ − c_L and from c₃ for n = 1…10. It is what one gets by doubling the α_s/2π form
  term by term but leaving "2/(n+1) + 1/n²" undoubled. That points to a normalisation slip.

**Literature (read, not recalled):**
* **BBDM preprint p. 17, eq. (3.9)**: B^{NS}_{2,n} = C₂(R){3Σ1/j − 4Σ1/j² − (2/(n(n+1)))Σ1/j + 4Σ_s(1/s)Σ_{j≤s}1/j + 3/n + 4/(n+1) + 2/n² − 9 +
  γ̃₀ⁿ(ln4π − γ_E)}, with C_{2,n} = 1 + (ḡ²/16π²)B_{2,n}. Since 4S₁,₁ = 2(S₁² + S₂), this is exactly the closed form plus the MS→MS-bar term.
  p. 27, eq. (4.7): C^{ν̄−ν}_{2,n} = C^{NS}_{2,n} for odd n. p. 28: **"the Adler sum rule (4.10) is exactly satisfied"**. So the original source states the n = 1 check itself.
* **Buras preprint p. 33, eq. (2.96)**: the same expression with 3/n + 4/(n+1) + 2/n² − 9.
* FRS NPB 152 (1979), eqs. (4.9)–(4.11): "agree with those of Bardeen et al." (text only; formula not rendered).
* VVM eq. (A.3) as above. Blümlein et al. 2022 (arXiv:2208.14325) c^{(1,0)}_{F2,q} = C_F{(2+5N−2N²−9N³)/(N²(1+N)) + (−2+3N+3N²)/(N(1+N))S₁ + 2S₁² − 2S₂},
  which is algebraically identical to the closed form.
* Web searches for the variant string found nothing. The project's `research/critic/checks/c2_coeff_consistency.py` names the variant `misremembered(n)`.

**Verdict: refuted as an erratum.** No erroneous published formula is identified, and every primary source checked prints the correct form; the claim itself says
"source unspecified". The mathematics of the correct statement is **confirmed**. Print: C^{q,(1)}_{2,n} = C_F[2S₁² − 2S₂ + 3S₁ − 2S₁/(n(n+1)) + 3/n + 4/(n+1)
+ 2/n² − 9] in a_s = α_s/4π (= 2C^q_{2,N} of c_dis in α_s/2π). It vanishes at n = 1, as required by the Adler sum rule and as already noted by BBDM (1978).
Cite BBDM eq. (3.9) (MS-bar after dropping γ̃(ln4π−γ_E)) and eq. (4.10), plus VVM (A.3). Do not mention a "commonly quoted variant".

---

## 4. E33 — published errata whose content was not examined

All 18 erratum records exist on INSPIRE with exactly the references in the claim. FRS NPB 152 (1979) has no erratum record; the "Floratos et al. (+ erratum)" item is
FRS NPB 129 (1977) 66 [NPB 139 (1978) 545]. Contents examined:

| paper | erratum | content (how examined) | used in our material? / action |
|---|---|---|---|
| Bodwin PRD 31 (1985) 2616 | PRD 34 (1986) 3932 | not accessible (APS; no arXiv) | abstract level only. Cite with erratum. |
| Collins–Soper NPB 193 (1981) 381 | NPB 213 (1983) 545 | not accessible (also listed in Collins 2011's bibliography) | historical statement only |
| Collins PRD 57 (1998) 3051 | PRD 61 (2000) 019902 | arXiv v2 (1999-09-06, "Two figures corrected"); text identical apart from the date. **Fig. 1** (leading regions for diffractive DIS) and **Fig. 5** (soft gluon between proton and jet subgraphs): in the corrected figures the collinear subgraph A emits further target-collinear final-state lines besides p′ (rendered both versions). | text quotes (thm:break-ddis). `tikz3/fig_diffraction` is schematic and not affected. Any region diagram after Collins's Fig. 1 must show the extra lines. |
| BBL PRD 51 (1995) 1125 | PRD 55 (1997) 5853 | `erratum.tex` in arXiv v2: spin-flip Fock states have probability ~v³ ("amplitude of order vⁿ" → "probability of order v²ⁿ"; odd powers of v allowed). Error estimates O(v⁴Γ)→O(v³Γ) in (3.1), (4.1a,b), (4.3a,b); O(v³σ) in (6.8a,b), (6.9a,b). Typos: (3.19a,b) prefactor √(3N_c/2π); (5.4) last colour matrix T^a_{i′j′}; (5.5) coefficient 4/(N_c²−1); (A16), (A25) α_s(2M). | VF-NRQ-1…4 not affected. No BBL error estimate is quoted; if one is, use v³. |
| Becher–Neubert PRL 102 (2009) 162001 | PRL 111 (2013) 199905 | arXiv v3 (2013-10-22, "additional term in (12)"): eq. (12), the relation to Catani's H^{(2)} for ≥4 partons, gains −(if^{abc}/32ε)Σ_{(i,j,k)}T_i^aT_j^bT_k^c(γ₀^i/C_i − γ₀^j/C_j) ln(−s_ij/−s_jk) ln(−s_ki/−s_ij). | Not affecting the dipole formula. **Side finding:** in v1–v3 the dipole formula is **eq. (7)**; eq. (2) is Catani's I^{(1)}, I^{(2)} display (compiled v1; counted v3). VF-SUD-5 and thm:sudakov-ir-poles cite "eq. (2)": fix to (7). VF-SUD-5's ordered-pair reading agrees with BN's eq. (10), Σ_{(i,j)}T_i·T_j = −ΣC_i (v2/v3). |
| Henneaux PLB 313 (1993) 35 | PLB 316 (1993) 633 | not accessible (arXiv v1 only; the BBH review hep-th/0002245 cites the paper without mentioning the erratum) | used as a hypothesis source (VF-FRO-15, OTHERS §8.2). Read the erratum before citing a specific statement; otherwise cite BBH 2000 for the theorem. |
| Ebert–Gao–Stewart JHEP 06 (2022) 007 | JHEP 07 (2023) 096 | arXiv v3: "fixing typos and with complex C^(1) [JHEP erratum version]" | abstract level. Any printed NLP hard coefficient must be the complex one. |
| Rodini–Vladimirov JHEP 08 (2022) 031 | JHEP 12 (2022) 048 | arXiv v2 "misprints corrected"; v3 (2025) "corrected typos in Eq. C.4/5" | abstract level |
| Kovchegov–Pitonyak–Sievert JHEP 01 (2016) 072 | JHEP 10 (2016) 148 | arXiv v3 (2016-07) "more corrections included" | literature level only |
| Cougoulic et al. JHEP 07 (2022) 095 | JHEP 09 (2024) 052 | arXiv v4 (2024-08): "minor corrections in intermediate steps without changes to the final results" | literature level only |
| **Dixon–Herrmann–Yan–Zhu JHEP 05 (2020) 135** | JHEP 06 (2024) 143 | arXiv v2 (2024-05), diffed against v1. The normalisation ξ_ε = 1+ε²ζ₂ "was mistakenly omitted" in **eq. (3.12)** (two-loop tripole soft factor). Consequences: 30ζ₄→15ζ₄, iπ³/3→iπ³/6, −2ζ₂→−ζ₂ in the soft-collinear terms, and **the conclusion is reversed**. v1: "factorization-violating terms survive at the level of the cross section". v2: they "cancel at the level of the cross section", and "at … O(α_s³) there is no potential factorization violation visible in the soft-collinear limit". New abstract: "…potentially dangerous factorization-violating terms can arise, **but they cancel after summing over colors**." | **OTHERS §4.3 quotes the v1 abstract. It must be corrected**, and DHYZ must not be cited as evidence of cross-section-level violation. |
| Forshaw–Holguin JHEP 12 (2021) 084 | JHEP 04 (2024) 097 | arXiv v3 (2024-03) diffed against v2. v2 predicted CVLs α_s⁵L² in the cumulative W/Z/H p_T. v3: for the **vector-sum p_T**, momentum conservation (the CSS proof) forces ln w = 0, so there are **no CVLs**. A scalar-sum p_T may have α_s⁵L²(ln w)⁴. "all observables" → "almost all" in the body; CVLs below α_sⁿL^{2n−4} carry an O(1) factor that may vanish. | OTHERS §4.4 already says "almost all". If FH is cited for DY/W/Z q_T, use the corrected statement. |
| Becher–Neubert–Rothen–Shao JHEP 11 (2016) 019 | JHEP 05 (2017) 154 | arXiv v3 vs v2: signs of V_m, R_m (one-loop anomalous dimension, "(5.11)") and of the preceding real/virtual terms flipped; S₂^{(2)}, S₂^{(3)} get 1/2!, 1/3!. §2 (factorization formula, RGEs) unchanged apart from removed highlighting. | VF-FRO-14 and OTHERS §11.1 use §2 only, so they are not affected. If V_m, R_m are ever printed, use the v3 signs. |
| Bertone et al. JHEP 03 (2020) 135 | JHEP 08 (2022) 108 | arXiv v3: overall normalisation of eqs. (C.18)–(C.20) changed | abstract level |
| Diehl–Ostermeier–Schäfer JHEP 03 (2012) 089 | JHEP 03 (2016) 001 | arXiv v3 "small corrections as published in erratum; list of changes at end" (list not examined line by line) | abstract level and DGOPS pointers |
| Kramer–Lampe ZPC 34 (1987) 497 | ZPC 42 (1989) 504 | not accessible | c_ee reference list only |
| Penin PLB 745 (2015) 69 | PLB 751 (2015) 596; PLB 771 (2017) 633 | arXiv v4 (2017-05, "asymptotic formula corrected, conclusions unchanged"). The v1 abstract's claim that the power-suppressed term "dominates the amplitudes at extremely high energies" is removed. | mentioned only as a precursor ("Penin and Liu–Penin"). Do not quote Penin's asymptotic claim. |
| FRS NPB 129 (1977) 66 | NPB 139 (1978) 545 | not accessible | historical citation only |

**Errata present in our material but missing from E33's list:** Erdoğan PRD 89 (2014) 085016 [Erratum PRD 90 (2014) 089902; arXiv v2 "Figure 6 corrected"]
(OTHERS §1.6); Surguladze–Samuel PRL 66 (1991) 560 [Erratum ibid. 2416] (c_ee §12); Buffing–Diehl–Kasemets JHEP 01 (2018) 044 [Erratum JHEP 07 (2021) 046;
arXiv v3 "added erratum (main body of paper unchanged)"] (OTHERS §10).

**Verdict: confirmed** (existence and bibliographic data). The rule "use the corrected version" needs the DHYZ fix above.

---

## 5. E34 — reported disagreements (NLP, small x)

* **(i) Liu–Mecaj–Neubert–Wang, JHEP 01 (2021) 077 (arXiv:2009.06779v2 = journal version).** Abstract: "…predict the large logarithms of order αα_s²L^k in the three-loop
  decay amplitude, where L = ln(−M_h²/m_b²) and k = 6,5,4,3. We find perfect agreement with existing numerical results for the amplitude and analytical results for the
  three-loop contributions involving a massless quark loop. On the other hand, we disagree with the results of previous attempts to predict the series of subleading
  logarithms ∼αα_s^nL^{2n+1}." Sec. 6 identifies those attempts as Akhoury–Wang–Yakovlev 2001 and, for gg→h, Anastasiou–Penin 2020. The disputed coefficient is the
  C_F²α_s²L⁵ term (theirs −C_F/10 vs LMNW −3C_F/20). For gg→h, LMNW give (C_A−C_F)/640·(11C_A/9 − C_F − 10T_Fn_b/3), and the numerical authors (Czakon–Niggetiedt)
  confirmed it by private communication. Sec. 7 states the same. **Accurate.**
* **(ii) Rodini–Vladimirov, PRD 110 (2024) 034009 (arXiv:2306.09495v3).** Abstract: "We found several differences with earlier derivations, which are due to accounting
  for nontrivial kinematics of the quark-gluon interference terms." The body adds that they agree on all comparable terms, and that the overlooked effects
  (Mulders–Tangerman, Bacchetta et al. 2007, Ebert–Gao–Stewart 2022) come from assuming strictly positive collinear momenta. **Accurate.**
* **(iii) Balitsky–Chirilli, PRD 77 (2008) 014019 (arXiv:0710.4330v1, the only arXiv version; journal text not seen).** Sec. VI ("Comparison to NLO BFKL"): the
  eigenvalue "coincides with Eq. (eigenvalue) up to the extra term 2ζ(3)", i.e. an extra (α_s²N_c²/4π²)ζ(3) Tr U_xU_y†, "which contradicts the requirement
  d/dη U_xU_y† = 0 at x = y. A possible reason for the disagreement is the connection between the matrix element of the color dipole with a rigid cutoff α < σ and
  the cutoff by energy s". Sec. VIII (Conclusions): "agrees with the forward NLO BFKL kernel up to a term proportional α_s²ζ(3) times the original dipole. We think
  that the difference could be due to different definitions of the cutoff in the longitudinal momenta." **Accurate.** For printing, add the later development stated
  by Balitsky–Chirilli PRD 88 (2013) 111501 (arXiv:1309.7644): the rigid cutoff violates conformal invariance, an O(α_s) counterterm defines the "composite conformal
  dipole" (NPB 822 (2009)), and its evolution "is Möbius invariant and agrees with NLO BFKL kernel" (said there in the N = 4 SYM context).
* **(iv) Borden–Kovchegov, PRD 108 (2023) 014001 (arXiv:2304.06161) vs BER.** Read: abstract, Secs. on the anomalous dimension and the BER comparison. Independent
  checks (`e34_helicity.py`, ā = α_sN_c/2π):
  * BER's pure-glue Δγ_GG re-derived from **BER Z. Phys. C72 (1996) 627, eq. (4.8)**, with F₈ = Ng²∂_ω ln(e^{z²/4}D_p(z)), p = 2C_A/N = 2, D₂ = (z²−1)e^{−z²/4},
    M₀ = 4N, G₀ = N. The square-root argument becomes exactly 1 − (16ā/ω²)(1−3ā/ω²)/(1−ā/ω²), as BK transcribe it.
  * Expansions: BK Δγ_GG = 4ā/ω + 8ā²/ω³ + 56ā³/ω⁵ + **496**ā⁴/ω⁷ + 4824ā⁵/ω⁹; BER: 4, 8, 56, **504**, 4920. They agree through three loops and differ from four
    loops on, as BK state.
  * Intercepts: BK √u with u³ − 256u + 1024 = 0 gives **3.660744√ā**, equal to their closed form (4/3^{1/3})√(Re[(−9+i√111)^{1/3}]). BER: u² − 17u + 48 = 0 gives
    √((17+√97)/2) = **3.663936√ā**. Relative difference 0.087%.
  * Attribution detail: BER themselves print only "the pure gluonic case would have given z = 3.66" (singlet with n_f = 4: 3.45). 3.66394 is BK's (and earlier
    Kovchegov–Pitonyak–Sievert, PRD 95 (2017) 014033) analytic evaluation of BER's equations. BER references for the bib: Bartels–Ermolaev–Ryskin, Z. Phys. C70 (1996) 273
    [hep-ph/9507271] (non-singlet) and Z. Phys. C72 (1996) 627 [hep-ph/9603204] (singlet; eq. (4.8)).
  * Status 2026: still open. No four-loop fixed-order computation found among the 43 papers citing BK 2023. Ermolaev, Phys. Atom. Nucl. 87 (2024) 244, writes that BER
    "has recently been confirmed, except for a very small discrepancy". Print no verdict.

**Verdict: confirmed.**

---

## 6. E35 — positivity of MS-bar PDFs; Yukawa counterexample

* **CRS (arXiv:2111.01170v2 = PRD 105 (2022) 076010; compiled for numbering).** Abstract: CFH's derivation's "primary failure is in the apparently uncontroversial statement
  that bare pdfs are always positive … Divergent UV contributions are regulated and are positive when n < 4, but can and often do become negative after analytic
  continuation to n > 4." Sec. VI ("Failure of an argument for positivity of MS-bar pdfs"): there is no ε for which both Z^B and the bare pdf are positive, and "at least
  one of items 1–3 must be false" (bare factorization; positivity of bare pdfs; positivity of partonic cross sections). Equation numbers verified: (55) MS-bar pdf,
  (56) Δ(ξ), (57) counterterm −a_λ(1−ξ)S_ε/ε, (58) DR integral, (59) cutoff form. Sec. VIII B is "Systematics of why the pdf becomes negative".
* **CFH (arXiv:2006.07377v2 = JHEP 11 (2020) 129; compiled).** The bare-positivity step is in §2, right after the operator definition (arXiv eq. (2), JHEP eq. (2.2)), p. 4:
  "It can be shown (see e.g. Sect. 6.7 of Ref. [Collins 2011]) that the expression Eq. (2) is a number density, and as such before subtraction of divergences it is
  positive." It is used in the p. 6 principle "If all contributions which are factored away from the partonic cross section and into the PDF remain positive, then the
  latter also stays positive" (CRS quote this as "p. 5" of the journal). In §3.1.1 (p. 15) and §3.1.2 (p. 19): "because the bare PDF of Eq. (2) is a probability density,
  the three factors which are convoluted in Eq. (50) are all separately positive when ε → 0⁻".
* **Independent derivation** (`e35_yukawa.py`). From the operator definition with one scalar in the intermediate state, the spin trace is
  (1/2)Tr[(P̸+m_p)(k̸+m_q)γ⁺(k̸+m_q)] = 2P⁺[(m_q+ξm_p)² + k_T²], with k² − m_q² = −(k_T²+Δ)/(1−ξ) (sympy, explicit Dirac matrices). Hence
  f(ξ) = λ²(1−ξ)/(2(2π)^{D−1}) μ^{2ε}∫d^{D−2}k_T [k_T²+(m_q+ξm_p)²]/(k_T²+Δ)². DR + MS-bar gives exactly a_λ(1−ξ)[ln(μ²/Δ) − 1 + (m_q+ξm_p)²/Δ], with pole
  a_λ(1−ξ)S_ε/ε. The k_T < μ cutoff form differs by O(m²/μ²): 3.1×10⁻³ at 30 GeV and 2.8×10⁻⁴ at 100 GeV for the bracket.
* **Sign structure** (m_q, m_p, m_s = 0.3, 1.0, 1.5 GeV; bisection, `e35_roots.py`). The sign change in ξ is at 0.0851 (μ = 0.5), **0.2640 (μ = 0.8)**, 0.4088 (1.0),
  **0.5674 (1.2)**, 0.8229 (1.5), 0.9921 (1.69). f < 0 for all larger ξ up to ξ → 1. There is no sign change for μ ≥ 1.70 GeV. μ_* = m_s exp{½[1 − (m_q+m_p)²/m_s²]}
  = **1.69878 GeV**. The threshold μ₀(ξ) rises monotonically from m_q = 0.3 GeV (ξ→0) to μ_* (ξ→1), so f(ξ;μ) > 0 for all ξ iff μ > μ_*. The project script prints
  "[0.28, 0.98]" because its grid is `linspace(0.02, 0.98, 49)`. The true region at 0.8 GeV is (0.264, 1).
* **CFGH (arXiv:2308.00025; v2 ≈ EPJC 84 (2024) 335, v4 2026).** Both versions: "PDFs always turn positive at high enough scale … and, correspondingly, turn negative
  at a low enough scale, as pointed out in [CRS]. However, the value of this scale is set by non-perturbative physics"; "can be very conservatively estimated to be
  Q² ≳ 5 GeV²" (α_s/2π·C_gg < 1 at x ∼ 0.3 ⇒ α_s ≲ 0.2). v4 corrects the argument for Eq. (44), Eqs. (46)–(47) and Fig. 1 "with unchanged conclusion".

**Verdict: confirmed with the interval corrected.** The grades [V] (all-μ positivity as a general theorem) and [P] (positivity above a non-perturbative scale) are appropriate.

---

## 7. E36 — Gaunt / Rothstein–Stewart vs Schwartz–Yan–Zhu

* **Gaunt 2014 (arXiv:1405.2080v1), abstract:** "for hadronic transverse energy E_T … the classic CSS argument for the cancellation of Glauber gluons breaks down at
  the level of two Glauber gluons exchanged between the spectators … we suggest that this failure … corresponds to a failure of the 'standard' factorisation formula …
  at leading power … MPI sensitive observables … beam thrust B⁺_{a,b} and transverse thrust." The conclusions say the same ("we argued").
* **Rothstein–Stewart 2016 (arXiv:1601.04695v3), §11.1 "Spectator-Spectator":** eq. (11.13) shows that the S–S phase cancels when the Δp_⊥ integral is unrestricted
  (checked in the arXiv PDF). Then: "Assuming that the measurement restricts the Δp_⊥ ∼ Q*, then these spectator-spectator scattering Glauber exchange diagrams will not
  cancel out. In this case the measurement spoils the factorization of the perturbative n- and n̄-collinear initial state beam radiation, but only starting at O(α_s⁴)
  … for event shape observable such as beam thrust, transverse thrust, and E_T … first discussed in [Gaunt] … computed numerically for a double spin asymmetry beam
  thrust observable … [Zeng] … it applies to any observable where Δp_⊥ is constrained, including for example beam thrust without the spin asymmetries." RS also note that
  this alone does not explain the underlying-event sensitivity, and that it enters only at N⁴LL.
* **SYZ 2018 (arXiv:1801.01138v2), abstract:** "for pure Glauber ladder graphs, all amplitude-level factorization violating effects completely cancel at cross section
  level for any single-scale observable (such as hadronic transverse energy or beam thrust). This result disproves previous claims that these pure Glauber graphs are
  factorization-violating." Intro: Gaunt and RS argued for violation "by diagrams with pure Glauber gluon exchange"; the result holds "integrated over the kinematic
  variables other than a single infrared-safe observable". Scope: "Our argument does not apply to doubly-differential observables, like those studied in [Zeng]."
  §3.2 "All-orders Glauber cancellation": "the cancellation we found persists to all orders". Corollary: the leading violation needs the Lipatov vertex (real soft
  radiation; connection with the underlying event).
* **Zeng 2015 (arXiv:1507.01652v2), abstract:** a QCD-with-scalar-quarks counterexample to any factorization with decoupled collinear sectors in DY with jet vetoes/beam
  thrust. It shows a non-zero leading-power spin asymmetry from S–S Glauber exchange.
* **Later literature (INSPIRE, 36 citing papers):** no rebuttal of SYZ found. Bijl–Niedenzu–Waalewijn 2023 cite SYZ approvingly ("for single-scale observables such
  contributions necessarily involve a Lipatov vertex"). Barcaro–Gao–Gaunt–Pathak 2026 list Gaunt 2014 and SYZ 2018 together among works where "factorization violation
  has been established", without discussing the conflict.

**Verdict: confirmed**, with this wording: "Gaunt (2014) found that the CSS cancellation argument fails at the level of two S–S Glauber gluons for E_T and suggested
LP factorization failure for MPI-sensitive observables. RS (2016, §11.1) state that S–S Glauber exchange spoils factorization from O(α_s⁴) for observables constraining
Δp_⊥ (beam thrust, transverse thrust, E_T). SYZ (2018) argue to all orders that pure Glauber ladders cancel for every IR-safe single-scale observable, 'disproving' the
pure-Glauber claims; violation then requires soft emission off the rungs. SYZ's argument excludes doubly-differential observables, where neither RS's general statement
nor Zeng's model result is contradicted. Standard factorization for MPI-sensitive observables remains [C]."
Related note on R-M30 / ERR-M30: "MPI-sensitive observables remain non-factorizing" overstates the case. Keep [C] (OTHERS §4.7).

---

## 8. Side findings (for the integrator)

1. **OTHERS §4.3 (DHYZ 2020):** replace the v1-abstract quote by the erratum conclusion (sec. 4).
2. **VF-SUD-5 / thm:sudakov-ir-poles:** the Becher–Neubert PRL dipole formula is eq. (7) (arXiv v1–v3 numbering), not eq. (2).
3. **OTHERS §7 / CLAIMS E35:** "negative for ξ ∈ [0.28, 0.98] at μ = 0.8 GeV" → "negative for ξ > 0.264 (up to ξ → 1)".
4. **E32:** the "variant" exists only in our critic's check script; remove it from REVIEW §6/§10 text intended for print.
5. **E34(iii):** add the composite-conformal-dipole follow-up whenever the ζ(3) mismatch is printed.
