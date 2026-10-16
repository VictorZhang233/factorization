# Verification batch A12–A22 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are attributions (who said what, where). For each one I opened the cited
source myself wherever it was reachable, and I recomputed the formulas that the attributions carry.

## 0. Method and sources

* **Downloads.** Each download went into its own directory under the session scratchpad `a12v2/dl/…`. They were read as text only
  (`pdftotext -layout`), and the pages that carry a formula or a quote were also rendered to PNG and inspected.
  * **Collins, *Foundations of perturbative QCD*,** OA reissue, Cambridge Core chapter PDFs: front matter, ch. 2, 3, 5, 10, 11, 13, 14 and 15, App. A and the references.
    The front matter of *Renormalization* (OA) was also read.
  * **arXiv:** 1507.00047 (ADG), 1309.6521v3 (Caron-Huot), hep-ph/0409313 (CSS review), 2304.03302 (TMD Handbook), 1810.10022 (Frye et al.),
    1812.06468, 1812.04247, hep-ph/9607206 (Indumathi), 2308.16807, 1001.3606 (BCK), 2002.01223 (Waldschmidt), hep-ph/0403192 (MVV),
    0807.0323 (BCR, LaTeX source), 2103.03270 (BPV), 1112.4405 (CdFR), 1206.6363 (FSS), 2408.03019 (GHMMS), hep-ph/9709499 (Collins 1998),
    1001.2977 (RM), hep-ph/0604094 (FKS 2006), 0808.1269 (FKS 2008), 0902.0477 (Keates–Seymour), 2107.01212 (BNS), 1206.3955 (CDF),
    hep-ph/9808371 (MRST), hep-ph/9605210 (Klasen–Kramer 1996), hep-ph/9805369, 0805.2809 (H1), 0904.1092 (ZEUS), 1012.4355,
    hep-ph/9603249 (Ji), hep-ph/9907495 (BKM), hep-ph/0109045 (BPS 2002, LaTeX source), hep-ph/9407339 (BBL).
  * **Preprint scans:**
    * Fermilab: BBDM 1978 (FERMILAB-Pub-78/42-THY).
    * INSPIRE files: Dine–Sapirstein 1979 (SLAC-PUB-2332) and Lepage–Brodsky 1980 (SLAC-PUB-2478).
    * archive.org, Digital Library of India scan: Titchmarsh, *The Theory of Functions*, 2nd ed. (1939).
    * PDG 2024 review, "Cross-section formulae for specific processes".
  * **BM II** (CMP 52 (1977) 55, Project Euclid scan). A fresh download was blocked (Incapsula), so I used the copy that the
    interrupted first attempt of this same batch had downloaded earlier in this session. I checked its header and pagination: it is the
    genuine CMP 52, 55–75 scan.
  * **Not accessible**, and not circumvented:
    * APS full texts: Grammer–Yennie 1973, AM-type PRD/PRL texts.
    * ScienceDirect (Cloudflare).
    * CERN CDS (bot challenge).
    * Springer ZPC (DFLM, FP).
    * Boas, *Entire Functions* (lending only).
    * The books of Ellis–Stirling–Webber and Peskin–Schroeder.
* **INSPIRE API** for every bibliographic item and abstract (helper `insp.py`); Crossref for the two Collins OA DOIs.
* **My scripts** are in `verify/claims/batch_A12_s1_scripts/`; run each with `python3 -I`.

  | script | what it checks |
  |---|---|
  | `a15_bbdm.py` | BBDM eq. (3.9) against the c_dis Mellin moments |
  | `a16_r2.py` | r₂ in MS and MS-bar |
  | `a18_qqbar_gg.py` | independent numerical computation of the spin- and colour-averaged \|M\|²(qq̄→gg) |
  | `a20_sll.py` | the first super-leading log, recomputed from BNS eqs. (14) and (19) |
  | `pg.py` | page extractor for the Collins chapters |
  | `insp.py` | INSPIRE query helper |

* **Project script re-run:** `research/c_tmd/scripts/sivers_spectator.py` prints "Spectator-model checks: PASS".

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| A12 | **confirmed** | Read in full, not only the abstract. Cite Caron-Huot §4.3, eq. (4.28), with his wording "appears to rule out". Add Aybat–Dixon–Sterman 2006 for the two-loop statement and Henn–Mistlberger 2016 as an independent check of ADG. | yes (attribution) |
| A13 | **confirmed** | All pages and quotes are correct. p. 571 prints a typo, "One of notable notable exception is Nayak, Qiu, and Sterman (2005)", so quote only "notable exception", or add [sic]. "relative lack of detailed proofs" is on p. 571. The §14.6 m²/Q²×1/ε term is a possibility Collins raises ("One can imagine…"), not a shown result. | yes |
| A14 | **confirmed** | Every abstract and text quote is verbatim. Di'Lieto et al. call the agreement "fortuitous". Frye et al. say "often requires" (§8); "generically" appears in their abstract. | yes |
| A15 | **confirmed, with corrections** | The O(α_s) F_L coefficient is first due to Zee–Wilczek–Treiman 1974. BBDM cite ZWT, Calvo, Nanopoulos–Ross and Hinchliffe–Llewellyn Smith for it. AM 1978 is the x-space "Altarelli–Martinelli equation". The DIS scheme starts with AEM NPB 143 (1978) 521 [Erratum NPB 146 (1978) 544] as well as AEM 1979. The DFLM gluon is "the convention first introduced by DFLM" (Klasen–Kramer 1996); the DFLM text itself was not seen. Add the HvNM erratum NPB 644 (2002) 403. BBDM has now been opened: eq. (3.9) is identical to c_dis. Its Bjorken sum rule reads 1−8/((33−2f)ln), not 2[…]. Drop "ESW (4.80)" unless checked. | yes |
| A16 | **confirmed, with one correction** | BM II does **not** spell out non-abelian gauge theory with ghosts. It names "Yang-Mills field + fermions without axial coupling" and "certain non-abelian gauge theories" only as examples, under assumed Ward identities. r₂ is confirmed (DS 1979 eq. (11); BCK 2010 general group). CG 1980 quote −0.94 in the MOM scheme and state agreement. ESW H(ε) remains unverified. | yes |
| A17 | **confirmed** | Titchmarsh 2nd ed. §5.81 (p. 186) states the weaker form: type k<π in the whole half-plane. The sharper form of Theorem 7.6 matches Boas Thm 9.2.1, which I know only through Waldschmidt. Add the Catani–Seymour erratum NPB 510 (1998) 503. MVV (2.7) and (3.4) are verified. | yes |
| A18 | **confirmed, with one caveat** | Collins himself says his approximant generalizes GY and differs from GY's K term (pp. 118, 345, 421). The GY K-photon ∝ k_μk_ν, but **do not print** the k↔−k-symmetrized b_k of c_wilson §6.1 as "the original GY". Indumathi (Ann. Phys. 263 (1998) 310) says that form is "a slight modification … with respect to the original definition of GY for p_f≠p_i". The qq̄→gg formula is verified independently (numerics plus PDG eq. (51.9)). All Collins page numbers are correct. | yes |
| A19 | **confirmed** | BCR eq. (SivBM2-s-pl) is read in the source and the vertex conventions give e_qe_s=−e_c². "Lensing": cite Burkardt PRD 66 (2002) 114005 and NPA 735 (2004) 185. The κ-relation refs in BCR are **Burkardt–Hwang** PRD 69 (2004) 074032 and Lu–Schmidt PRD 75 (2007) 073008. The u-quark Sivers sign is negative (BCR 2008; BPV 2021). | yes |
| A20 | **confirmed, with a mandatory correction to item (4)** | FKS 2006 eq. (3.24), coefficient (3N²−4)/480, is for an out-of-gap gluon on **one side (y>0)**. The full first SLL for qq→qq is −σ₀(2α_s/π)⁴ln⁵(Q/Q₀)π²Y(3N²−4)/**240**: FKS 2008 eq. (2.22), Keates–Seymour 2009 eq. (3.2), and my recomputation from BNS eqs. (14) and (19). The phrase "contrary to earlier statements" is not a BNS quote. The BNS equations for 2→1 and 2→0 are (22) and (23); for 2→0 their explicit case is qq̄→V. | yes |
| A21 | **confirmed** | The LB normalization is verified (LB 1980, eq. (2.24a)): ∫φ_π = f_π/(2√N_c) with LB's f_π≈93 MeV. With f_π≈130 MeV write F_π/(2√N_c). FGOC/DR/BT/MNP are NLO **hard-scattering** references, not the two-loop ERBL kernel. ILS abstracts state dominance, not 1/Q⁴; for the 1/Q⁴ scaling cite BKM 2000 eq. (25). | yes |
| A22 | **confirmed** | PRD 66 054005 and PRD 67 071502 verified; the BPS footnote is read in the source. Comment PRD 72 098501 and reply PRD 72 098502 exist ("We disagree with their criticisms"). The BBL convention D=∂+igA (p. 9) and M = pole mass are verified. Add the BBL erratum PRD 55 (1997) 5853. | yes |

---------------------------------------------------------------------------------------------------------------------

## 2. A12 — dipole formula beyond two loops

**ADG, PRL 117 (2016) 172002, arXiv:1507.00047v2.** I read the full text.

* After eq. (4): "Equation (4) is known as the dipole formula, and captures the entirety of the soft anomalous dimension matrix up to two loops."
* Eq. (7) is the most general three-loop correction Δ_n^(3), with C = ζ₅ + 2ζ₂ζ₃ and F(z) = L₁₀₁₀₁(z) + 2ζ₂[L₀₀₁(z) + L₁₀₀(z)] (eqs. (13)–(14)).
* Abstract: "non-dipole corrections appear already for three coloured partons, where the correction is a constant without kinematic
  dependence. Kinematic dependence appears only through conformally-invariant cross ratios for four coloured partons or more…
  thereby preserving strict collinear factorization properties". See also Δ_Sp^(3) in eq. (17).
* In the Regge limit Δ₄^(3) tends to a constant: "the dipole formula alone is consistent with predictions from the Regge limit through
  NNLL at O(α_s³)".

**Independent confirmation.** Henn–Mistlberger, PRL 117 (2016) 171601 (INSPIRE abstract): the full-colour three-loop four-gluon N=4 amplitude
"provides an independent check of a recent result for three-loop corrections to the soft anomalous dimension".

**Two loops.** Aybat–Dixon–Sterman, PRD 74 (2006) 074004 (ADG ref. [17]).

**Caron-Huot, JHEP 05 (2015) 093 (arXiv v3).** The relevant section is §4.3, "Implications for infrared divergences", pp. 34–36.
* "at four loops, we do find a 1/ε pole in eq. (4.19), in contradistinction with the dipole formula prediction, and signaling a
  nontrivial contribution to the four loop soft anomalous dimension". The Regge limit of the four-loop soft anomalous dimension is
  eq. (4.28), ∝ ζ₃C_A[T_t²,[T_t²,T_s²]]log³|s/t|.
* "this appears to rule out the dipole conjecture starting from four loops". The effect is "delayed to four loops, contrary to two or
  three as the argument would naively suggest".
* The analysis covers the signature-even NLL amplitude only.

This is consistent with ADG, whose three-loop non-dipole term has no Regge logarithms.

**Verdict: confirmed.** "Dipole formula beyond two loops: [V]" is correct: an explicit non-zero three-loop correction is computed and has been
checked independently. Two refinements:
* The dipole formula with Casimir scaling is also modified for two legs at four loops by quartic Casimirs; ADG mention this possibility.
* Cite Caron-Huot as §4.3, eq. (4.28), "appears to rule out".

## 3. A13 — Collins 2011: pages, quotes, conventions

**Status of the book.** Front matter of the OA PDF: "This title, first published in 2011, has been reissued as an Open Access publication";
"DOI: 10.1017/9781009401845"; "First published 2011 / Reissued as OA 2023". Crossref lists edition-number 1, published 2023-07-13.

For *Renormalization* the imprint reads "First published 1984 … Reissued as OA 2023", DOI 10.1017/9781009401807. The back-cover blurb
says "first published in 1986"; that is the paperback year, so cite 1984.

INSPIRE attaches the OA DOI to the 2011 record. **"Not a new edition": confirmed.**

| item | location checked | result |
|---|---|---|
| §5.4.3 (devil's advocate; ELOP p. 48 quote) | p. 110 | verbatim. "would be rewarded by not finding a published explicit and complete proof. Textbook treatments, when examined closely, are incomplete"; ELOP: "A proper proof needs the use of topology; . . . We shall be content with plausibility arguments." Exercise 5.3 (***) on p. 159. |
| §11.3.2 (K gluons "glossed over"; Labastida–Sterman; Collins–Rogers 2008) | p. 407 | verbatim |
| BRST argument, eqs. (11.11)–(11.18) | pp. 408–410 | correct. The gap quote on p. 410 is verbatim as printed in OTHERS §8.1. |
| triangular mixing (11.20) | p. 412 | correct, with Hamberg–van Neerven 1992 and Collins–Scalise 1994 |
| §14.4 (CSS 1988 "with some important improvements and with correction of errors"; supersedes Bodwin 1985 and CSS 1985a) | p. 553 | verbatim |
| §14.4.6 (T-invariance, §13.17.5; unitarity, §12.8.6) | pp. 560–561 | correct |
| §14.4.7 BBL phases ("their effects do not break factorization; rather they get moved into the parton densities") | p. 561 | verbatim |
| §14.4.8 "Issues remaining" (graduated-rapidity exchange; incomplete leading regions, Labastida–Sterman; "The current versions of genuine proofs are evidently formidable") | pp. 561–562 | verbatim |
| §14.6 (masses; (14.42) m²/Q²×1/ε; "this is a bad idea") | pp. 569–570 | verbatim. Caution: Collins writes "One can imagine a divergence proportional to (14.42)" and "factorization by itself does not imply that all IR divergences cancel, but only those that are leading power in Q". This is a danger he points out (perhaps not for DY), not a demonstrated result. |
| §14.7 ("depended quite essentially on the cross section being completely inclusive") | p. 570 | verbatim |
| §14.7 ("relative lack of detailed proofs…"; NQS; TMD factorization "appear to fail", CQ 2007, RM 2010) | p. 571 | verbatim, **but** the printed sentence is "One of notable notable exception is Nayak, Qiu, and Sterman (2005)." I confirmed this by rendering the page. SURVEY's "One notable exception is …" silently corrects the typo. |
| §15.9 ("I have not been able to penetrate the SCET literature to properly understand its rationale") | p. 580 | verbatim |
| §13.15.2 (MOS, NSY, JMY 2005 "ignored important quark polarization effects"; JMY 2004) | p. 528 | verbatim |
| §13.17.1–13.17.5 | pp. 534–536 | correct; (13.124) is the sign reversal |
| eq. (2.2) | p. 9 | D_μψ₀ = (∂_μ + ig₀t^αA^α_(0)μ)ψ₀; the Wilson line in (13.40) is P e^{−ig₀∫n·A} |
| eq. (13.35a,b) | p. 495 | S̃(b_T) = ∫d^{2−2ε}k_T e^{+ik_T·b_T}S(k_T); "The normalizations differ from those in Collins and Soper (1982b)" |

Collins–Rogers, PRD 87 (2013) 034018 (Collins:2012uy) is bibliographically correct. The Collins 2011 locations it quotes all exist:
§3.3.2 "Quark-gluon vertex" (p. 47), §10.8 (p. 359), §10.11.1 (p. 379), §10.12.3 (p. 391), (13.106) (p. 529), (14.31) (p. 563).

**Verdict: confirmed**, with the typo and phrasing cautions above.

## 4. A14 — history of DY factorization and higher twist

All of these were checked against INSPIRE (publisher) abstracts unless stated otherwise.

* **BBL 1981**, PRL 47 1799: "initial-state interactions violate the usual QCD factorization predictions for massive lepton-pair production in leading twist" ✓.
* **BBL 1989**, PRD 39 3287: "can invalidate the parton-model (factorized) form of the cross section unless the beam energy is greater than a scale that grows with the length of the target"; ⟨q_T²⟩ ∝ target length ✓.
* **Bodwin 1985**, PRD 31 2616 [Erratum PRD 34 (1986) 3932]: "detailed one- and two-loop examples … this factorization program can be implemented to all orders" ✓. The erratum is listed on INSPIRE; its content was not examined.
* **Lindsay–Ross–Sachrajda**, PLB 117 (1982) 105 and NPB 214 (1983) 61: "the sum of all these non-factorising terms is zero" ✓.
* **Brandt–Frenkel–Taylor**, NPB 312 (1989) 589: verified to two loops in an eikonal "meson" model ✓.
* **DFT**, NPB 168 (1980) 93: "two quarks (with non-zero mass, and colour averaged) in the initial state … non-leading infrared divergences coming from two soft gluons do not cancel" ✓.
* **Di'Lieto–Gendron–Halliday–Sachrajda**, NPB 183 (1981) 223: "We agree … that in two loops the single logarithmic divergence does not cancel … However, this agreement is fortuitous since we disagree with several of the intermediate results" ✓.
* **Andrási et al.**, NPB 182 (1981) 104: "Bloch-Nordsieck inclusive cross sections are not in general infrared finite in non-abelian gauge theories" ✓.
* **FGT**, NPB 233 (1984) 307: finite to O(g⁴) "except for terms which are power-suppressed at high energies"; O(g⁶); all orders under a generalized unitarity assumption ✓.
* **CCM**, NPB 264 (1986) 588: non-cancelling terms "in general of higher twist type" ✓.
* **CSS 1989 §10.2** (hep-ph/0409313, text): "At two loops, noncancelling divergences occur at the level m⁴/s² in the Drell-Yan process", citing [43] DFT/FGT/BFT and [44] Di'Lieto et al. ✓.
* **BRS**, NPB 244 (1984) 221: scalar-quark model, one loop, "factorization … holds at order m²/s, but fails at order m⁴/s²" ✓.
* **Frye et al.**, PRD 99 (2019) 056015 (text): abstract "one need only sum over initial or final states … the cancellation generically requires the inclusion of the forward scattering process"; §8 item 2 "IR finiteness often requires the inclusion of forward scattering and the interference between disconnected and connected Feynman diagrams" ✓.
* **CSS 1986**, NPB 263 37: "an analysis at all orders of perturbation theory is needed to reliably establish this conjecture" ✓.
* **TMD Handbook** §2.11.4 (arXiv v1, p. 96): "The first process where TMD factorization was proven is back-to-back hadron production in e⁺e⁻ annihilation [88]", where [88] = CS NPB 193 (1981) 381. INSPIRE lists the erratum NPB 213 (1983) 545. The Handbook has no journal version, so cite arXiv:2304.03302 ✓.

**Verdict: confirmed.**

## 5. A15 — DIS/DY attributions

* **BBDM**, PRD 18 (1978) 3998. Opened now (Fermilab preprint FERMILAB-Pub-78/42-THY).
  * Eq. (3.9): B₂,ₙ^NS = C₂(R){3S₁ − 4S₂ − 2S₁/(n(n+1)) + 4Σ_s S₁(s)/s + 3/n + 4/(n+1) + 2/n² − 9 + γ̃₀ⁿ(ln4π − γ_E)}.
  * Eq. (3.8): C_L,n = (ḡ²/16π²)C₂(R)·4/(n+1), "well known", citing refs. 11–14 = Calvo PRD 15 (1977) 730, **Zee–Wilczek–Treiman PRD 10 (1974) 2881**, Nanopoulos–Ross PLB 58 (1975) 105, Hinchliffe–Llewellyn Smith NPB 128 (1977) 93.
  * `a15_bbdm.py`: B₂,ₙ without the ln4π term equals 2·C^q_{2,N}(c_dis) exactly for N=1…20, and γ̃₀ⁿ = −2P_qq,N/C_F (the MS→MS-bar shift).
  * Sum rules (4.10)–(4.12): Adler = 2 exactly; Bjorken ∫dx[F₁^ν̄p − F₁^νp] = 1 − 8/((33−2f)ln(Q²/Λ²)). c_dis writes "2[…]", attributed to Muta's Tokyo report. In the standard normalization (Adler = 2, F₂ = 2xF₁) the right-hand side is 1·[…]. The relative correction −(2/3)α_s/π is the same either way.
* **F_L at O(α_s).**
  * H1 PLB 665 (2008) [0805.2809] cites "Zee, Wilczek and Treiman, PRD 10 (1974) 2881; Altarelli and Martinelli, PLB 76 (1978) 89" for the QCD F_L.
  * ZEUS [0904.1092] cites AM for the gluon sensitivity.
  * hep-ph/9805369 calls eq. (22), F_L = (α_s/4π)x²∫dz/z³[(16/3)F₂ + 8Σe_i²(1−x/z)zg], the "Altarelli–Martinelli equation". I derived this algebraically from C_L^q = 2C_Fz and C_L^g = 4T_Fz(1−z).
  * The ZWT abstract: "The last section of the paper deals with deviations from the Callan-Gross relation".
  * **Correction:** attribute the O(α_s) longitudinal coefficient to ZWT 1974 (moments; see also Calvo, Nanopoulos–Ross, Hinchliffe–Llewellyn Smith), and the x-space formula to AM 1978. The AM abstract itself is about jet p_⊥ and mentions σ_L/σ_T only in passing; the AM text was not accessible.
* **DIS scheme.**
  * AEM NPB 157 (1979) 461, abstract: results "expressed in terms of parton densities derived from leptonproduction".
  * AEM NPB 143 (1978) 521 [Erratum NPB 146 (1978) 544], abstract: "The question of a convenient definition of effective parton densities appropriate at this level of accuracy is discussed".
  * Klasen–Kramer PLB 386 (1996) 384 cite both AEM papers for the DIS scheme and state: "the convention has been adopted to require the momentum sum rule to be preserved … one completes the definition by requiring the condition on the second moment to be valid for all moments. This convention was first introduced by Diemoz et al." MRST (hep-ph/9808371) cite DFLM for "the so-called DIS scheme" and give the same g^DIS as c_dis §10.
  * The DFLM text itself (ZPC 39 (1988) 21; CERN-TH-4751) was not accessible, so cite it as "first introduced by DFLM (see Klasen–Kramer 1996)".
* **AEM worked in the DIS scheme:** ✓ (abstracts above). The MS-bar presentation came later (FP ZPC 11 (1982) 293, abstract: "presented in a common factorization scheme").
* **HvNM**, NPB 359 (1991) 343, abstract: "complete calculation of the order α_s² correction in the MS scheme … All channels … included now" ✓. **Erratum NPB 644 (2002) 403** (INSPIRE) must be added.
* **ESW (4.80)** and **ESW Ch. 4**: not accessible. Keep these as unverified textbook pointers, without equation numbers.

**Verdict: confirmed, with the corrections listed.**

## 6. A16 — e⁺e⁻ attributions

* **Poggio–Quinn**, PRD 14 (1976) 578, abstract: "a simple proof that all Green's functions for nonexceptional Euclidean momenta in any renormalizable (but not superrenormalizable) field theory containing zero-mass particles are infrared finite" ✓.
* **Rigorous framework.**
  * Lowenstein–Zimmermann, CMP 44 (1975) 73: power counting with massless propagators, "infrared convergence conditions" ✓.
  * Lowenstein, CMP 47 (1976) 53: Green functions as tempered distributions for "a wide class of theories with zero-mass propagators" ✓.
  * BM, CMP 52 (1977) 39: "existence of Green's functions to all orders … for theories of massless particles without super-renormalizable couplings" ✓.
  * BM, CMP 52 (1977) 55 ("II"): mixed massless and massive, IR degree Ω ≥ 4 ✓.
  * Note that CMP 52 (1977) 11 is "Dimensional renormalization and the action principle", not part of the massless series. Cite by title rather than "I–III".
* **BM II gauge scope** (text read). The paper never mentions ghosts. Gauge theories appear only as examples:
  * p. 57: IR subtractions cancel "if there is some symmetry principle at work which forbids the corresponding counterterms … and dimensional regularization respects this symmetry (examples are: QED, Yang-Mills field + fermions without axial coupling)".
  * §6, pp. 73–74: "Relevant examples are QED, the Goldstone model and certain non-abelian gauge theories", under the stated *assumptions* that the Ward identities hold at tree level, are respected by DR, and imply vanishing massless vertex functions at zero momenta.
  * **So "BM II spells out the hypotheses for non-abelian gauge theory with ghosts" is not correct.** Print instead: "BM II covers gauge theories (e.g. Yang–Mills with vector-like fermions) under the assumption that the Ward/Slavnov–Taylor identities are respected by dimensional regularization".
* **r₂** (`a16_r2.py`):
  * From BCK 2010 (PRL 104, 132004), d₂ = −(3/32)C_F² + C_FT_f(ζ₃ − 11/8) + C_FC_A(123/32 − 11ζ₃/4), with T_f = Tn_f, a_s = α_s/π and μ² = Q². This is exactly the c_ee general-group formula.
  * For SU(3): r₂ = 365/24 − 11ζ₃ + (2ζ₃/3 − 11/12)n_f = **1.985707 − 0.115295 n_f** ✓.
  * Dine–Sapirstein (SLAC-PUB-2332) eq. (11): "(1.98 − .115 N_f) MS-bar" and "(7.35 − .442 N_f) MS". My MS value is 7.3587 − 0.4409 n_f, consistent within DS's rounding.
  * CKT 1979, abstract: "evaluated within the minimal subtraction scheme"; the number is not visible.
  * Celmaster–Gonsalves 1980, abstract: R = 3Σe²{1 + α_s/π − 0.94(α_s/π)² …} with **momentum-space-subtracted** α_s (five flavours); "Our result agrees with that of Dine and Sapirstein, and Chetyrkin, Kataev, and Tkachov". When citing CG for the MS-bar number, say that they worked in the MOM scheme.
* **ESW H(ε):** not accessible, so it remains unverified.

**Verdict: confirmed, with the BM II correction.**

## 7. A17 — c_pdf attributions

* **Waldschmidt** (arXiv:2002.01223, text): Carlson's theorem ("no nonzero entire function f of exponential type < π satisfying f(ℕ) = {0}") with "(Titchmarsh, 1939, §5.81) … (Boas, 1954, Th. 9.2.1)" ✓.
* **Titchmarsh, 2nd ed. (1939)**, read directly (DLI scan, p. 186): "5.81. If f(z) is regular and of the form O(e^{k|z|}), where k<π, for R(z) ≥ 0, and f(z) = 0 for z = 0, 1, 2, 3,…, then f(z) = 0 identically". §5.8 attributes it to "Carlson … In an Upsala thesis (1914)".
  * Titchmarsh's hypothesis (type < π in the whole half-plane) is **stronger** than that of c_pdf's Theorem 7.6, which allows finite type in the half-plane and type < π only on the imaginary axis.
  * Cite Titchmarsh §5.81 for the weaker form. Cite Boas Thm 9.2.1, via Waldschmidt (not seen), for the sharper form.
  * The monograph's applications only need Prop. 7.7, which c_pdf proves, so nothing depends on this.
* **INSPIRE, all correct:**
  * CS NPB 194 (1982) 445; AP NPB 126 (1977) 298; GW PRD 8 3633 and PRD 9 980; GP PRD 9 416.
  * CFP NPB 175 (1980) 27; Jaffe NPB 229 (1983) 205; Joglekar–Lee Ann. Phys. 97 (1976) 160.
  * Gribov–Lipatov Sov. J. Nucl. Phys. 15 438; Dokshitzer JETP 46 641.
  * Catani–Seymour NPB 485 (1997) 291, **plus Erratum NPB 510 (1998) 503**.
* **MVV** (hep-ph/0403192): eq. (2.7) γ = −∫x^{N−1}P, "in the older literature an additional factor of two is often included in Eq. (2.7)". Eq. (3.4): γ_ns^(0) = C_F(2(N₋ + N₊)S₁ − 3) = C_F(2(S₁(N−1) + S₁(N+1)) − 3), with a_s = α_s/4π. Relative to the α_s/2π normalization, γ_MVV^(0) = −2γ_ours, using S₁(N−1) + S₁(N+1) = 2S₁ − 1/(N(N+1)) ✓.
* **ESW Ch. 4:** not accessible.

**Verdict: confirmed**, with the Titchmarsh nuance and the CS erratum.

## 8. A18 — c_wilson attributions

* **Grammer–Yennie 1973.** The original is not accessible (APS, Cloudflare). What I could establish:
  * GY abstract (INSPIRE/APS): the K-polarization sum "resembles a gauge transformation".
  * Collins 2011, p. 118 (§5.5.6): "This method was obtained by generalizing the argument of Grammer and Yennie (1973)".
  * Collins 2011, p. 345 (§10.6): "their approximator (in their K term) differs significantly in form from what we wrote … the original Grammer-Yennie approach would use no approximation of k_AS on the A subgraph, and would have a more complicated non-linear function in place of our denominator k_AS·n₁".
  * Collins 2011, p. 421 (§11.9.3): "as in the original Grammer-Yennie paper".
  * Secondary forms: Sen–Indumathi–Choudhury, eqs. (7)–(9), and Indumathi (hep-ph/9607206; Ann. Phys. 263 (1998) 310), eqs. (11)–(12), write K = b k_μk_ν with b = ½[(2p_f−k)·(2p_i−k)/(((p_f−k)²−m²)((p_i−k)²−m²)) + (k↔−k)]. **But Indumathi, footnote 1:** "Note a slight modification in b with respect to the original definition of GY for p_f ≠ p_i; this is needed in order to remove logarithmic sub-divergences that occur at T ≠ 0."
  * 2308.16807, eq. (3.19), uses an unsymmetrized form.
  * Conclusion: "GY K ∝ k_μk_ν (pure gauge, symmetric in μν); the one-sided k_μw_ν/(k·w ∓ i0) is Collins' generalization" is supported. The explicit k-symmetrized b_k of c_wilson §6.1 must **not** be labelled "original GY".
* **qq̄→gg.**
  * CKR, PLB 70 (1977) 234, abstract: "Not only quark-quark scattering but all contributions in lowest order are considered" ✓.
  * `a18_qqbar_gg.py`: an independent numerical computation (explicit Dirac and SU(3) matrices, physical polarizations, the s-channel sign fixed uniquely by the Ward identity) gives \|M̄\|²/g⁴ = (32/27)(t²+u²)/(tu) − (8/3)(t²+u²)/s². The ratio is 1 to 10⁻¹⁵ at three angles.
  * This equals PDG RPP 2024 eq. (51.9) after converting dσ/dΩ = \|M̄\|²/(64π²s). The ESW Tab. 7.1 entry itself was not seen.
  * PS §6.1 was not seen.
* **Weinberg**, Phys. Rev. 140 (1965) B516, "Infrared photons and gravitons" ✓.
* **Collins page numbers:** §10.3 p. 321, §10.8 p. 359, eqs. (11.4)–(11.6) p. 402, §11.4 p. 411, §11.9 p. 416, BRST pp. 407–411 — **all correct**.

**Verdict: confirmed, with the GY caveat.**

## 9. A19 — TMD and Sivers attributions

* **Ji–Yuan**, PLB 543 (2002) 66: "a gauge link involving the gauge potential at the spatial infinity" ✓.
* **BJY**, NPB 656 (2003) 165: "a transverse gauge link … from transverse components of the gauge potential at the light-cone infinity" ✓.
* **BCR 2008** (0807.0323, LaTeX source):
  * Eikonal vertex −ie_c n₋^ρ, propagator i/(−l⁺+iε) (SIDIS), diquark vertex Γ_s^ρ = ie_c(2P−2p+l)^ρ.
  * Eq. (SivBM2-s-pl): f_1T^⊥ = −(g_s²/4)(Me_c²/(2π)⁴)(m+xM)(1−x)/(p_T²[L_s²(m²)+p_T²]) log((L_s²+p_T²)/L_s²).
  * e_c² → 4πC_Fα_s, citing BHS.
  * The DY cutting rule gives the opposite sign.
  * This matches c_tmd's formula exactly with e_q = −e_c and e_s = e_c ✓. The project script re-run gives PASS.
* **Lensing and κ-relation.** BCR eq. (Sivers-kappa), ∫(1−x)f_1T^⊥q = −(3/2)MC_Fα_sκ^q, "generalize[s] the findings of" [Burkardt:2003je] = **Burkardt & Hwang**, PRD 69 (2004) 074032, and [Lu:2006kt] = Lu & Schmidt, PRD 75 (2007) 073008. The lensing picture itself is Burkardt PRD 66 (2002) 114005 and NPA 735 (2004) 185 ("Chromodynamic lensing … the correlation between the sign of the anomalous magnetic moment and the sign of the Sivers asymmetry").
* **u-quark sign.** BCR: "According to the Trento conventions … Since the Sivers function for the up (down) quark is negative (positive)", in agreement in sign with the Anselmino et al. 2008 and Collins et al. 2005 parametrizations. BPV 2021 (JHEP 05 (2021) 151): "confirm the sign of Sivers function for u and d quarks"; the u function "turns positive at large-x" in their fit ✓.
* **T-odd FF universality.** Collins–Metz, PRL 93 (2004) 252001: universality between e⁺e⁻, SIDIS and DY, modified only by time reversal of the DY parton densities. Meissner–Metz, PRL 102 (2009) 172003: "partonic pole matrix elements vanish … additional strong evidence for the universality of transverse momentum dependent fragmentation functions" ✓.

**Verdict: confirmed**; refine the lensing references.

## 10. A20 — Glauber and SLL literature

1. **CdFR**, JHEP 07 (2012) 026.
   * P^(1,R) "is strictly factorized" (after eq. (178)).
   * Δ_P^(2) "gives a vanishing contribution to P^(2,R) … with n ≤ 4 QCD partons … we have to consider … n ≥ 5".
   * §8: "may invalidate the factorization theorem of mass singularities starting at the N³LO … An explicit quantitative proof of such a cancellation would represent a highly non-trivial check". They identify "a sole additional partonic configuration" that *can* cancel.
   * FSS, JHEP 11 (2012) 066: two-loop term zero on QCD tree amplitudes (eq. (5.9)); "For pure QCD processes, factorization is violated at the three-loop level"; two loops only for EW phase differences.
   * GHMMS, JHEP 01 (2025) 090: "appear to cancel at the level of cross sections in pure QCD up to NNLO" ✓.
2. **Collins 1998** §III D (hep-ph/9709499v2; PRD 57 (1998) 3051 [Erratum PRD 61 (2000) 019902]): "Precisely because A contains both initial- and final-state interactions, there are nearby poles in both the upper and lower half-planes, and we cannot deform the r⁻ contour … Instead, we appeal to a deformation of the other longitudinal momentum component r⁺" ✓.
3. **RM**, PRD 81 (2010) 094006.
   * Abstract: "a specific calculation for a double spin asymmetry in a spectator model with a non-Abelian gauge field".
   * The unpolarized case is only indicated: "An example of the type of graph which can produce a violation of generalized TMD-factorization in the unpolarized cross section is shown in Fig. 11".
   * The abelian two-gluon graphs violate standard factorization (§IV B) and can be absorbed into Wilson loops (generalized factorization) ✓.
4. **SLL coefficient — correction needed.**
   * FKS 2006 eq. (3.24) is −σ₀(2α_s/π)⁴ln⁵(Q/Q₀)π²Y(3N²−4)/480 (eq. (3.22) is only the order estimate), "for a single emission outside of the gap (with y>0)".
   * FKS 2008 (JHEP 09 (2008) 128) eq. (2.22) gives σ₁ = −σ₀(2α_s/π)⁴ln⁵(Q/Q₀)π²Y(3N²−4)/**240** and states: "we obtain the result in equation (3.24) of [7] (up to a factor of two, since the result there is for an out-of-gap gluon with y>0…)".
   * Keates–Seymour (JHEP 04 (2009) 040) eq. (3.2) agrees, with 240.
   * **Independent recomputation** (`a20_sll.py`): BNS eq. (14), with C_rn^(O) from eq. (19) and J₂ = J₄₃/2 = ΔY (full gap width, which equals FKS's Y: "the size of the rapidity region over which emission … is vetoed"), gives −(3N_c²−4)/240.
   * The same code reproduces the n = 0, 1, 2 terms of BNS eq. (21) (singlet) exactly.
   * So the printed "first SLL … /480" must carry "(out-of-gap gluon on one side, y>0)", or the total /240 must be printed instead.
   * **BNS**, PRL 127 (2021) 212002:
     * SLLs α_s^{n+3}L^{2n+3} (eqs. (13), (14)).
     * 2→1 "start at four-loop order" (eq. (23)); 2→0 (qq̄→V, eq. (22)) "start at 5-loop order, one order higher".
     * "In the literature [2, 7], it has been stated that SLLs only arise when there are at least two colored partons in the final state, but as we have shown…".
     * Higgs with a jet veto appears only as "relevant e.g. to" (gluon-induced results are deferred to their ref. [20]).
     * "contrary to earlier statements" is a paraphrase; drop the quotation marks.
5. **CDF**, PRD 86 (2012) 032009: "the observation of a breakdown of QCD factorization, expressed as a suppression by a factor of O(10) of the diffractive structure function (DSF) measured in dijet production relative to that derived from … DDIS at HERA". The CDF 2000 abstract quotes no factor ✓.
6. **H1 and ZEUS photoproduction.**
   * H1, EPJC 51 (2007) 549: "the predicted dijet cross section has to be multiplied by a factor of approximately 0.5 for both direct and resolved photon interactions".
   * The ZEUS EPJC 55 (2008) 177 abstract states no suppression.
   * Klasen–Kramer, MPLA 23 (2008) 1885: global factors of 0.42 (H1) and 0.71 (ZEUS), or resolved-only suppression ≈ 3 fits all data.
   * Collins 1998 conclusions: the proof "would appear to apply also to direct photo-production". "Open tension" is correct.

**Verdict: confirmed, with the mandatory change to item 4.**

## 11. A21 — exclusive processes

* **PRL 84 (2000) 2589** = Frankfurt–Polyakov–Strikman–Vanderhaeghen, "Hard exclusive electroproduction of decuplet baryons in the large N_c limit".
* **PRD 60 (1999) 014010** = Frankfurt–Pobylitsa–Polyakov–Strikman. Abstract: π⁺ asymmetry "dominated at small t by the contribution of the pion pole in the isovector SPD Ẽ as required by PCAC" ✓.
* **LO factorization:**
  * LB PLB 87 (1979) 359 and PRD 22 (1980) 2157 ("We prove that these reactions are dominated by quark and gluon subprocesses at short distances").
  * ER PLB 94 (1980) 245 ("all-orders, all-logarithms proof").
  * DM PLB 90 (1980) 159 and PRD 21 (1980) 1636.
  * FJ PRL 43 (1979) 246 (asymptotic normalized behaviour) ✓.
* **NLO:**
  * FGOC NPB 186 (1981) 429 (O(α_s²) corrections to F_π).
  * DR Sov. J. Nucl. Phys. 34 (1981) 293.
  * BT PRD 35 (1987) 2255 ("to resolve the discrepancies between three previous calculations").
  * MNP PRD 60 (1999) 074004.
  * These are NLO **hard-scattering** results, not the two-loop ERBL evolution kernel.
* **LB normalization** (SLAC-PUB-2478, p. 24, eq. (2.24a)): a₀ = 6∫[dx]φ_π = (3/√n_c)f_π with ⟨0\|J_W^μ\|π⁺⟩ = √2 f_π p^μ and f_π ≃ 93 MeV, i.e. ∫φ = f_π/(2√N_c) in LB's normalization ✓. This equals F_π/(2√N_c) in c_exclusive's notation (f_π ≈ 130 MeV).
* **Soft overlap 1/Q⁴.**
  * ILS PRL 52 (1984) 1080 and NPB 317 (1989) 526 assert soft dominance at accessible Q² but state no power in their abstracts.
  * BKM PRD 61 (2000) 073004, eq. (25): the LCSR soft end-point term enters at O(1/Q⁴) ("to the 1/Q⁴ accuracy both soft and hard contributions have to be taken into account"). Cite BKM for the scaling.
* **Ji**, PRL 78 (1997) 610, eq. (13): J_{q,g} = ½[A_{q,g}(0) + B_{q,g}(0)] ✓.
* **Collins–Freund v2** (2 Jul 1998): "Improved treatement of 'endpoint/breakpoint' regions. Corrected references to earlier work" ✓.

**Verdict: confirmed.**

## 12. A22 — SCET, NRQCD and BBNS

* **PRD 66 (2002) 054005** = BPS, "Power counting in the soft collinear effective theory". **PRD 67 (2003) 071502** = BPS, "Factorization and endpoint singularities in heavy to light decays" ✓.
* **BPS 2002 footnote** (hep-ph/0109045 source): "If Ū_R is independent of x, the collinear transformations are given in Ref. [cbis] … This global reparameterization invariance fixes the collinear action, except for the way in which i n·D appears". Here [cbis] = Bauer–Stewart, PLB 516 (2001) 134. MMPS (PLB 539 (2002) 59, April 2002) is not cited in the paper ✓.
* **BBNS comment** PRD 72 (2005) 098501 (hep-ph/0411171). **BPRS reply** PRD 72 (2005) 098502 (hep-ph/0502094): "This serves as a reply … We disagree with their criticisms" ✓. Report without a verdict.
* **BBL** (hep-ph/9407339; PRD 51 (1995) 1125, **Erratum PRD 55 (1997) 5853**):
  * "The gauge-covariant derivative is D^μ = ∂^μ + igA^μ" (p. 9).
  * δL_bilinear (2.5) contains gE and gB with E^i = G^{0i}, B^i = ½ε^{ijk}G^{jk} and c_i = 1 + O(α_s). With g_BBL = −g_CONTEXT (same A), every explicit gE and gB flips sign, so the c₂, c₃, c₄ terms flip sign when transcribed.
  * M is the heavy-quark mass, identified with the perturbative pole mass (M = M_pole(1 + O(α_s²)) in power-divergence-subtracting schemes; App. B: "M is the perturbative pole mass").
  * Decays: §II.F, eq. (2.14), 2Im f_n/M^{d_n−4}, and §II.G (EM). Production: §VI.A ✓.

**Verdict: confirmed.**
