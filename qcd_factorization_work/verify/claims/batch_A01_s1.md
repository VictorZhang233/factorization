# Verification batch A01 – A11 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are of kind `attribution`.
Criterion: an attribution is confirmed only if the cited source really contains the attributed content (checked in the paper itself), and a "first"/"no paper exists" statement only if targeted INSPIRE searches find no counter-example. Several claims are bundles of sub-claims. A bundle is graded **refuted** if at least one sub-claim that would be printed is factually wrong. The corrected bundle is then given in full. A bundle is graded **confirmed** if every sub-claim holds, possibly after precisions or qualifiers that are spelled out.

## 0. Method and sources

* **Downloads.** All arXiv sources were fetched fresh from `arxiv.org/e-print` into the session scratchpad (each in its own directory) and read as text. Arabic equation numbers were checked on the arXiv PDFs where the TeX uses macros. Bibliographic data come from the INSPIRE API, cross-checked with Crossref and the arXiv API where noted. Journal-only sources that were read:
  * APPB 53 (2022) 4-A2: journal PDF from actaphys.uj.edu.pl.
  * Vladimirov JHEP 04 (2018) 045: SCOAP3 copy via INSPIRE.
  * Collins, *Renormalization* (1984), ch. 12, and Collins, *Foundations of Perturbative QCD* (2011), ch. 14: open-access 2023 chapter PDFs on Cambridge Core.
  * Habilitation documents of Y. Liu: public BIP of the Jagiellonian University (habilitacje.bip.uj.edu.pl). Only professional data are used.
* **Scripts** in `verify/claims/batch_A01_s1_scripts/` (Python run with `python3 -I`):
  * `fetch_arxiv.sh`: source download helper.
  * `inspire_search.py`, `inspire_before.py`: INSPIRE queries, the second with a local cut-off on the earliest date.
  * `a02_inspire_counts.py`: BAI vs name search and affiliation history.
  * `eqcount.py`: rough equation counter for TeX sources.
  * `a05_cH_numeric.py` (+ `.log`): numerical values of c_H and N_m.
  * `run_checks.sh` (+ `run_checks.log`): re-runs all bibliographic and absence searches used below (33 INSPIRE queries).
* **Sources read in the relevant sections**, by claim:
  * A01: arXiv:2008.03886, 2004.03543, 1911.03840 (metadata).
  * A03: arXiv:1910.11415, 1911.03840, 2005.14572, 2003.06063, 2102.01101, 2305.04416, 2403.06787, 1811.00026, 1901.03685, 1405.7640, 2312.05957.
  * A04: APPB lecture notes (full text searched; §3.3, §4 intro, §4.4, §6, App. D, E and the reference list read); arXiv:2002.07527, 2201.08401, 2304.14440, 0808.2665, 1801.05930, 2311.06907, 1807.07528, 2102.07248; JHEP version of 1707.07606.
  * A05: arXiv:2601.12189 (§5), 1801.03917, 1404.6860, 1404.6680, 1706.08962, 1707.07152, 1707.03107, 2004.01043, 2004.03543 (§III), 2305.04416, 2402.06725.
  * A06: arXiv:2410.05141, 2410.12910, 1806.00808, 1811.10267, 1510.08696, plus abstracts of the remaining hits.
  * A07: arXiv:2401.08012, 2609.20545, 2308.04270.
  * A08: arXiv:2007.04085, 2011.10368.
  * A09: arXiv:0705.3340 (§5.1), 1603.08012 (§1), 1105.3375 (Thm., eq. (7)); Collins 1984 §12.8.
  * A10: hep-ph/9711391, 1410.1892 (ch. 2), 1111.2589, 1809.04325, 2211.14845, 2407.13738, 2408.10308.
  * A11: arXiv:0811.0246 (PDF), 1601.04695 (PDF: §5.1, §9, §10, §11); Collins 2011 §14.4.5.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| A01 | **confirmed** | LAMET line 89: write "Ji, Liu, Schäfer, Wang, Yang, Zhang, Zhao, NPB 964 (2021) 115311". `lamet.bib` (key Ji:2020brr) is already correct. Line 101 (PLB 811: Ji, Liu, Liu) is correct. | Metadata (INSPIRE, Crossref, arXiv agree). |
| A02 | **confirmed, with precisions** | (i) The INSPIRE author profile gives Jagiellonian "start_date 2020". The primary source (habilitation summary, Aug 2023) gives a postdoc internship in 2021 and *adiunkt* since 2021. Paper affiliations first show Jagiellonian in 2021. Print "since 2021". (ii) "Habilitation 2023" = the habilitation application/summary dated Aug 2023; the conferral date was not found. (iii) No authoritative Chinese name was found: delete 刘义壮 (LAMET l. 9, twice) and 刘一壮 (YZLIU l. 857, FINAL_OUTLINE l. 137). spec_v2 contains neither. | INSPIRE author 1981577; ORCID 0000-0002-0897-1165; UJ habilitation BIP. |
| A03 | **confirmed, with mandatory qualifiers** | I.5: write "first lattice calculation of S_I (LPC 2020, their own claim); first lattice CS kernel: Shanahan–Wagman–Zhao 2020 (quenched)". C2: cite Gao–Lee–Mukherjee–Shugert–Zhao 2021 (NLL threshold resummation of the *pseudo-PDF/SDF* coefficient; origin of the qPDF threshold logs). A5: cite the ESZ 2018 non-perturbative soft mismatch factor g^S_q as precursor. A3: cusp-angle analyticity goes back to Korchemsky–Radyushkin 1987, so drop "first" or say "to our knowledge". D1 and LAMET §11: add O(1/N), Bjorken limit of a *forward* matrix element, λ ∈ iℝ≥0; cite BBK 1998 (all-power, convergent OPE of a vacuum correlator in the 2D O(N) σ model at NLO in 1/N). A6: keep "in the exponential regulator". | Each "first" is the authors' own claim (JLL 2019; Liu 2024 §1; LPC 2020) or survives our searches. |
| A04 | **refuted** (one misattribution; 9 of 10 items verified) | (iv) The "not presented beyond one loop" remark in APPB §4.4 is about Ref. [47] = **Collins, IJMPCS 4 (2011) 85 [Collins:2011ca]**, not Collins–Soper 1981. APPB's criticism of CS 1981 itself is a different one (App. D: a heuristic IR-safety argument with a loophole for linear divergences). (ii) Vladimirov–Schäfer 2020: an SCET_II derivation with a one-loop check, not a "one-loop" result. (v) Ji:2018hvs has five authors (…, Zhang, Zhao). Cite the "open question" quote from the JHEP version (p. 32); it is not in arXiv v2. | APPB 53 (2022) 4-A2; PRD 101 (2020) 074517; JHEP 04 (2018) 045. |
| A05 | **confirmed, with precisions** | (iii) BCK *argue* all-order equality and *compute* 3 loops (quark) / 2 loops (gluon). (iv) Radyushkin 1983 is now verified at abstract level ("On spectral properties of parton correlation functions and multiparton wave functions"); drop "recall". (v) JLS *extracted* c_a, c_H by matching to the exact NNLO kernel (c_H partly analytically, App. F); "fitted" is inaccurate. (vi) Avkhadiev–Shanahan–Wagman–**Zhao** (four authors). | Each item is located verbatim in the source (§5 below). |
| A06 | **refuted** (2 of 11 absence claims false) | (3) **False**: the N³LO non-singlet matching for the Wilson-line quark correlator exists: Cheng–Huang–Li–Li–Ma, PRL 134 (2025) 251902 [arXiv:2410.05141]. Ji–Liu–Su–Zhang, JHEP 03 (2025) 045, cite it as "the three-loop result [of the quasi-PDF matching kernel] in Mellin space". (4) **False as stated**: Rossi–Testa, PRD 98 (2018) 054028, call the counter-arguments of [Ji:2017rah] "untenable". Their PoS Confinement2018 092 concedes individual moments but maintains the obstruction for the full PDF. Replies: KOZ 2018; Radyushkin PLB 788 (2019) 380. All other items survive the searches. | See §7. |
| A07 | **confirmed** | "Braun 2024" = Braun–Koller–Schoenleber. Su et al. cite BKS only in a list and do not discuss its result. Neither paper says the other is wrong. | BKS PRD 109 (2024) 074510; Su et al. arXiv:2609.20545; Braun JHEP 10 (2023) 134. |
| A08 | **confirmed** | CLAIMS.md gives a wrong title for Collins 2020. The real title is "A new and complete proof of the Landau condition for pinch singularities of Feynman graphs and other integrals" (39 pp., 10 figs, v1 only). | arXiv/INSPIRE/Crossref: no journal version of 2007.04085 or 2011.10368. |
| A09 | **confirmed** | Hollands 2008 is **Rev. Math. Phys.** 20 (2008) 1033 ("RMP" is ambiguous). Quote Collins 1984 §12.8 (p. 321) exactly. | Collins 1984; Hollands 2008 §5.1; FH 2016 Thms 1–2; HK 2012 eq. (7); HHK 2016. |
| A10 | **confirmed** | The 2022 on-shell-expansion paper is Gardi–Herzog–Jones–Ma–**Schlenk**. | §11. |
| A11 | **refuted** (one item false) | (3) **False**: RS §10.1–10.3 treat the n–n̄ production current explicitly. Fig. 29: "an e⁺e⁻ annihilation current with a soft or Glauber loop". Text: Glauber exchange as "amplitude level rescattering phases, even for e⁺e⁻ annihilating into just final state strongly interacting particles". RS also state that for n–n̄ production "the result at any order … should be the same in the theories with or without … Glauber". Items (1), (2), (4), (5) verified. | RS JHEP 08 (2016) 025; AS PLB 671 (2009) 46; Collins 2011 §14.4.5. |

---

## 2. A01 — author list of NPB 964 (2021) 115311

* **INSPIRE** (arxiv:2008.03886, texkey Ji:2020brr): Ji, Xiangdong; Liu, Yizhuang; Schäfer, Andreas; Wang, Wei; Yang, Yi-Bo; Zhang, Jian-Hui; Zhao, Yong.
* **Crossref and the arXiv API** give the same seven authors in the same order.
* **RMP 93 (2021) 035005** (arXiv:2004.03543): Ji, Yu-Sheng Liu, Yizhuang Liu, Zhang, Zhao (arXiv and INSPIRE order; Crossref lists Yizhuang Liu before Yu-Sheng Liu). The surname string "Ji, Liu, Liu, Zhang, Zhao" is the RMP's. The RMP has exactly five authors, so "et al." fits neither paper.
* **PLB 811 (2020) 135946** (arXiv:1911.03840): Ji, Yizhuang Liu, Yu-Sheng Liu. LAMET line 101 is correct.
* `frontier/lamet/lamet.bib` entry Ji:2020brr already has the correct seven authors. Only the prose on LAMET line 89 is wrong.

**Verdict: confirmed.**

## 3. A02 — identity of Yizhuang Liu

* **INSPIRE author 1981577.** Name "Liu, Yizhuang"; ORCID 0000-0002-0897-1165; BAI Y.Liu.90. One position: Jagiellonian U., `start_date 2020`, current. The record also holds institutional e-mail addresses; they are not reproduced here.
* **ORCID** public record: given name Yizhuang, family name Liu, no other names, no education or employment entries.
* **Counts** (`a02_inspire_counts.py`):
  * `a Y.Liu.90`: 73 records, earliest 2014-07-01, latest 2026-09-17.
  * `a "Liu, Yizhuang"` (quoted): 72 records, all among the 73.
  * The only extra BAI record is Liu:2022nnk (APPB lecture notes, author string "Liu, Y.").
  * The unquoted name search returns 3205 records, so the quotes matter.
  * Stubs Y.Liu.28, .38, .68 carry the name "Liu, Yizhuang" but hold detector/heavy-ion, accelerator/medical and mathematics papers.
* **Career** (habilitation summary "Dane osobowe i podsumowanie osiągnięć zawodowych", Aug 2023; professional data only):
  * B.Sc. (licencjat), USTC, 1.07.2012.
  * Ph.D., SUNY Stony Brook, 18.08.2018; promotor I. Zahed; thesis "Non-perturbative studies in QCD".
  * 2018–2020 postdoc at TDLI Shanghai; 2020–2021 postdoc at Regensburg; 2021 postdoctoral internship at UJ; 2021–present adiunkt at UJ.
  * Series [H1]–[H7]: PRD 105 (2022) 076014; NPB 964 (2021) 115311; PRL 125 (2020) 192001; RMP 93 (2021) 035005; PLB 811 (2020) 135946; NPB 955 (2020) 115054; JHEP 08 (2023) 037. These are exactly YZLIU's keys.
  * Polish title of the series: "Sformułowanie rozkładu partonów w przestrzeni euklidesowej: faktoryzacja, ewolucja i zastosowanie na sieci".
  * Awards: Silsbee Prize 2016; Rector's Award UJ 2022.
  * INSPIRE paper affiliations of Y.Liu.90 agree: Stony Brook 2014–18; TDLI/SJTU 2018–20; Regensburg 2020–21; Jagiellonian from 2021.
* **Discrepancy.** The INSPIRE profile says Jagiellonian from 2020. The primary source and the paper affiliations say 2021. Print 2021.
* **Habilitation date.** The summary is dated August 2023. The conferral date was not found (UJ news only lists a 2021 seminar).
* **Chinese name.** No authoritative source was found:
  * none in the habilitation documents, INSPIRE (no `native_name`), ORCID, or the IHEP lattice-school participant list;
  * web searches for 刘义壮 and 刘一壮 together with TDLI/LaMET give no hit tied to this person.
  * Both renderings remain UNVERIFIED and must be deleted. `grep` shows them only in LAMET.md l. 9 (刘义壮, twice), YZLIU.md l. 857 and FINAL_OUTLINE.md l. 137 (刘一壮), plus CLAIMS.md. spec_v2 contains neither.

**Verdict: confirmed** (with the precisions above).

## 4. A03 — Liu-programme priority claims

Each item was checked against the source's own novelty statement, then searched on INSPIRE (fulltext and title) for earlier work.

* **I.5 (conflict) — confirmed.**
  * SWZ, arXiv:2003.06063 (submitted 2020-03-12; PRD 102 (2020) 014511), abstract: "This work presents the first exploratory determination of the Collins-Soper kernel using the lattice formulation of QCD. In a quenched calculation, the N_f = 0 kernel …".
  * LPC, arXiv:2005.14572 (2020-05-29; PRL 125 (2020) 192001) itself claims only: "In this paper we present the first lattice QCD calculation of the intrinsic soft function S_I … [the CS kernel] we will calculate it as a by-product. Our result is consistent with that of quenched lattice calculations of TMDPDFs [Shanahan:2020zxr]."
  * LPC used a 2+1-flavour CLS ensemble; they mention "partially quenching effect". A narrower "first dynamical CS kernel" is not claimed by LPC and should not be printed.
* **A1 (time-independent soft factor) — confirmed.**
  * JLL, arXiv:1910.11415: "Recently, there have been attempts to formulate the soft function on lattice [Ji:2014hxa, Ji:2018hvs, Ebert:2019okf], however, the suggested Euclidean quantities so far cannot be used in actual TMD factorization." They then present the HQET form-factor representation.
  * On the bent soft functions, JLL write: "the cusp anomalous dimension of the bent soft functions in Ref. [Ji:2014hxa, Ebert:2019okf] coincide with S_I at one-loop level, in general it is different beyond one-loop order".
  * ESZ 1901.03685 introduced the "bent" quasi soft function "and discuss potential issues at higher orders".
  * INSPIRE fulltext search ("soft function" + "lattice QCD" + "form factor", 61 hits before 2019-10-25) and the "soft factor"/"Euclidean"/"heavy quark" searches found no earlier time-independent representation.
* **A3 (continuation framework, Table 2) — confirmed in weakened form.** The APPB makes no explicit priority claim. Precedents:
  * Korchemsky–Radyushkin NPB 283 (1987) 342: "the analyticity properties of Γ_cusp with respect to γ are investigated" (cusp-angle analyticity of the anomalous dimension).
  * Collins–Metz 2004 and Collins 2011: universality via contour deformation.
  * No earlier systematic classification of off-light-cone *TMD* soft functions (b⊥-separated, all time orderings, Table 2) was found. Print without "first", or with "to our knowledge", citing KR 1987 for the angle analyticity.
* **A5 (S_I and 𝒟 = 2𝒟₁ − 𝒟₂) — confirmed with a precursor.** JLL NPB: S_I = S₂/(S₁S₁) "is called the intrinsic soft function … S_I is scheme independent", S_I = e^{−𝒟}, and "we obtain the relation 2𝒟₁ − 𝒟₂ = 𝒟". Precursor: ESZ, PRD 99 (2019) 034505 (arXiv:1811.00026) "define g^S_q(b_T, μ) as the mismatch of the lightlike and quasi soft factors, which we allow to be nonperturbative". The novelty is an operator-defined, rapidity-scheme-independent, Euclidean-computable object. This qualifier must be printed together with the ESZ precursor.
* **A6 (time ordering, exponential regulator) — confirmed with its qualifier.** Liu 2023 frames the earlier statements as claims based on space-like separations (Collins–Metz 2004, Collins 2011, ESV 2016) or as assumptions (Vladimirov 2016/2017, 2020). The INSPIRE search of papers citing the exponential-regulator paper (recid 1441208) with "time ordering" + "soft factor" found no earlier all-order argument. Keep "in the exponential regulator" and "to our knowledge".
* **B1 (quasi-TMD matching, single-line power counting) — confirmed.**
  * Earlier matchings: ESZ 2018/2019, with an undetermined g^S_q or a bent soft function.
  * JLL PLB (Nov 2019) is the first with a Euclidean-computable soft factor. VS 2020 (Feb 2020) is later.
  * The single-line power counting is APPB eqs. (54)–(68).
* **C2 (threshold factorization) — confirmed with a mandatory citation.**
  * Gao–Lee–Mukherjee–Shugert–Zhao, PRD 103 (2021) 094504 (arXiv:2102.01101, Feb 2021) analysed the origin of the threshold logarithms in qPDF and pPDF. They resummed them at NLL in Mellin space for the *spatial correlator/pseudo-PDF* coefficient with "the form motivated by the standard threshold resummation formulas". For the qPDF they state the resummed kernel "is beyond the scope of this work".
  * JLS 2023 (arXiv:2305.04416) cite them ("it is known [Xiong:2013bka, Gao:2021hxl] …"). JLS give the first *derived* threshold factorization C → H·J of the momentum-space quasi-PDF kernel, with full RG resummation and the universality of the heavy–light Sudakov kernel.
  * "First … of LaMET (quasi-PDF) kernels" is correct only with GLMSZ cited.
* **D1 (2D GN) — confirmed with precedents.**
  * Liu 2024 §1: "To our knowledge, this type of expansions in the Bjorken limit … has never been analytically worked out in 2D QFTs with marginal UV limits … (expansions in the Euclidean high-virtuality limit −p² → +∞ for vacuum correlators have been worked out many years ago for the O(N) non-linear sigma model in [Beneke:1998eq] and for the large-N Gross Neveu recently in [Marino:2024uco])".
  * BBK, PLB 443 (1998) 308, abstract: OPE of the σ-model self-energy "to all orders in the coupling and the large momentum, and to next-to-leading order in 1/N … We also find that the OPE converges for sufficiently large external momentum".
  * Convergence theorem: abstract "for any 0 < z² < ∞ and any λ ∈ iR≥0"; §5 states it for ℰ(z²m², iλ), λ ≥ 0, i.e. imaginary Ioffe time. "F₂, F₃ … can be shown in similar ways".
* **LAMET §11 ("the only places … non-perturbatively and to all powers") — confirmed only if narrowed.**
  * True for forward (hadronic) Bjorken-limit expansions, at O(1/N) (non-perturbative in the coupling only), in a marginal 2D model.
  * The all-power, convergent vacuum OPE of BBK 1998 is also 2D and must be mentioned.
  * The wording "non-perturbatively" without "at O(1/N)" overstates the result.

**Verdict: confirmed, with the qualifiers above.** No item is contradicted by an earlier paper once these qualifiers are printed. Without the GLMSZ, ESZ and BBK citations, items C2, A5 and D1 / LAMET §11 would be misleading.

## 5. A04 — Liu-programme proof-status attributions

Item by item:

* **(i) — verified verbatim.**
  * APPB §6: "We should also mention that all the proofs in the paper, except the ones for the analyticity, follow the typical rigorous standards in the TMD factorization literature. To promote all these 'physical proofs' to fully mathematically consistent proofs at the level of those works for UV renormalization remains to be an important but difficult task …"
  * PLB (arXiv:1911.03840): "Here we provide a sketch of mathematical proof for Eq. (factorization), leaving details to a future publication".
* **(ii) — verified with one precision.**
  * ESSZ (JHEP 04 (2022) 178): "prove a factorization relation between these quantities to all orders in α_s … no mixing between various quark flavors or gluons".
  * dRV PRD 108 (2023) 114009: NNLO coefficient function. JLS 2023: NNLO heavy–light Sudakov factor. JLS's own note says dRV's two-loop result "agrees with the result we found here".
  * **Precision:** VS 2020 "Using soft collinear effective field theory, we derive the factorization theorem for the quasi-TMD operator. We check the factorization theorem at one-loop level". This is an SCET_II derivation plus a one-loop check, not merely a one-loop result.
* **(iii) — verified.** The renormalizability proofs are JZZ (Ji, Zhang, Zhao), GJS (Green, Jansen, Steffens) and IMQY (Ishikawa, Ma, Qiu, Yoshida). Liu is not an author.
* **(iv) — WRONG ATTRIBUTION.**
  * APPB §4.4: "In early 1980s, Collins and Soper have developed a diagrammatic technic … When applied to the off-lightcone soft functions, it was claimed in **Ref. [47]** that collinear modes … are power-suppressed … However, a detailed explanation regarding how the collinear modes were suppressed to the extent that were sufficient to kill all the rapidity divergences beyond one-loop level is not presented."
  * APPB reference [47] = "J. Collins, «New Definition of TMD Parton Densities», Int. J. Mod. Phys.: Conf. Ser. 4, 85 (2011)" = Collins:2011ca (arXiv:1107.4123).
  * APPB's criticism of Collins–Soper 1981 itself is a different one (App. D): "We first show the heuristic argument made in Ref. [1] and point out the loophole caused by linear divergence".
  * The next sentence of §4.4 is correct as attributed: "The nature of the rapidity divergence has also been studied in Ref. [19] [Vladimirov JHEP 1804 045] using the conformal transformation method. It was claimed that the rapidity divergence can be mapped to UV divergences for Wilson-line cusps, thus can be factorized".
  * Vladimirov's quote is in the **published** version, JHEP 04 (2018) 045, p. 32 (conclusions): "the factorization of rapidity divergences for SIDIS soft factor remains the open question". It is absent from arXiv:1707.07606v2, as Liu 2023 notes ("in the published version").
* **(v) — verified.**
  * Collins, PoS LC2008 028 (arXiv:0808.2665): "I therefore propose to redefine the unintegrated parton density … Matrix element(L) / √(Wilson loop (2L))".
  * Ji:2018hvs (arXiv:1801.05930) introduces the same subtraction.
  * JLL cite both: "subtract them from the beginning … with rectangular Wilson loop [Collins:2008ht, Ji:2018hvs]".
  * Ji:2018hvs has five authors: Ji, Jin, Yuan, Zhang, Zhao. "Ji–Jin–Yuan–Zhang" omits Zhao.
* **(vi) — verified.**
  * APPB §3.3: the static potential "suffers from spurious IR divergences starting at the α_s⁴ order", and for quasi-TMDs "Beyond three-loops, they cause power divergences".
  * APPB §4 overview: "starting from the 3-loop level".
  * The wording is inconsistent, so do not print an exact loop order.
* **(vii) — verified.** Liu–Su (arXiv:2311.06907) eq. (2.52): "Here we propose a conjecture that the amplitude N_m … is the same as that for the linear divergence or the heavy-quark pole mass even beyond large β₀ limit", giving N_m = 0.622 … 0.524 for n_f = 0 … 5. The large-β₀ value C_F e^{5/6}/π = 0.976565 was re-computed (`a05_cH_numeric.log`).
* **(viii) — verified.**
  * Liu 2023 §4: rigorous coordinate-space analyticity of DR correlators remains to be proven, "But the author believes in it".
  * App. C on DY = SIDIS: the light-front argument "can only be regarded as heuristic", followed by an alternative deformation argument. Line 504: "the method based on coordinate-space analyticity can not be used to establish this identity".
  * So [A] (conditional) for the theorem and [P] for DY = SIDIS are consistent with the source. These grades are our own.
* **(ix) — verified.** Liu 2024 §1: "the specific structure of the QCD Bjorken limit commonly called 'collinear factorization', strictly speaking, has no exact derivation up to now".
* **(x) — verified.**
  * The word "super-renormalizable" does not occur in Ji:2018waw (arXiv:1807.07528); the paper says "No such renormalization is needed for spinor QCD".
  * Liu:2021evw: arXiv v1 (2021-02-14) only, no journal reference on arXiv or INSPIRE.

**Verdict: refuted** (item (iv) is a misattribution). The corrected bundle is given in the structured output.

## 6. A05 — LaMET attributions

* **(i) — verified.**
  * JLS 2026 (arXiv:2601.12189) §5, "Exponential decay of space-like correlators from locality": the bound "can be proved using conformal mapping and Jensen's formula as discussed in Ref. [Fredenhagen:1984bz]". Fredenhagen, "A remark on the cluster theorem", CMP 97 (1985) 461.
  * §5.3: "The above can be proven to all orders in perturbation theory in φ³ or φ⁴, using parametric representations and properties of graph polynomials".
  * "Thm 7.1" is LAMET's own numbering; in JLS this is §5.
* **(ii) — verified.**
  * IJJSZ (arXiv:1801.03917) §I: "Our approach is based on the operator product expansion (OPE) … has been proven for scalar field theory … and is widely assumed to hold for any renormalizable quantum field theory including QCD".
  * Ma–Qiu, arXiv:1404.6860 (Apr 2014), published as PRD 98 (2018) 074021.
  * RMP §III: "An all-order factorization proof … was first given with a diagrammatical approach [Ma:2014jla] … While the proof is only for perturbative free quark states, the factorization formulas are widely believed to be true nonperturbatively as well."
  * Ji 2014 (Sci. China 57 (2014) 1407): "In fact the factorization in terms of Feynman diagrams can be proved order by order as in the renormalization program." No proof is given there.
* **(iii) — verified.**
  * JZZ: "Note that the above arguments are valid independent of whether the heavy quark field in the HQET Lagrangian is defined by a timelike or spacelike vector", i.e. the space-like extension is asserted.
  * IMQY §4: "We only concentrated on overall divergences but not on subdivergences, because subdivergences can be taken care by forest subtraction … The change of divergence indexes discussed here are only for superficial divergence."
  * BCK (JHEP 07 (2020) 161): "We **argue** that the renormalization factors … at space-like and time-like separations … coincide to all orders … calculate … to three- and two-loop accuracy".
* **(iv) — verified at abstract level.** Radyushkin, PLB 131 (1983) 179, "On Spectral Properties of Parton Correlation Functions and Multiparton Wave Functions": "Using a parametric representation for Feynman integrals it is demonstrated that the functions F(x₁,…,x_k), ψ(x₁,…,x_k) … have the spectral properties necessary for their parton interpretation."
* **(v) — verified.**
  * JLS 2023: the factorization predicts the threshold limit "up to two unknown constants c_a and c_H … it allows us to extract the two unknown constants"; "There are 41 non-vanishing terms, all of them are consistent with the exact results".
  * c_H = 0.0725 C_F² − 0.0840 C_F C_A + 0.1453 C_F n_f T_F (re-computed: 0.072518, −0.084043, 0.145307). The C_F C_A and C_F² terms are extracted analytically in their App. F.
  * Agreement with dRV is stated in their final note.
  * "Fitted" is inaccurate; "extracted" is correct.
* **(vi) — verified.** Avkhadiev, Shanahan, Wagman, **Zhao**, PRL 132 (2024) 231901: "This is the first such determination with systematic control of quark mass, operator mixing, and discretization effects."

**Verdict: confirmed** (with the precisions).

## 7. A06 — literature-absence claims and unrefereed preprints

The searches are re-run by `run_checks.sh`.

* **(1) No Zimmermann-level OPE for Wilson-line operators — holds.** Title search on OPE + Wilson line/nonlocal/quasi/gauge link/light-ray since 2010 finds 10 hits: light-ray OPE in CFT, BCK non-local condensate, moments of GPDs, and similar; no proof.
* **(2) No dedicated quasi-TMD Glauber analysis — holds.** No title hit. The 10 fulltext hits (quasi-TMD + Glauber) only mention Glauber modes.
* **(3) No N³LO quasi-PDF kernel — FALSE.**
  * Cheng, Huang, Li, Li, Ma, PRL 134 (2025) 251902 (arXiv:2410.05141, Oct 2024): "We present the first complete next-to-next-to-next-to-leading-order calculation of the matching coefficients that link unpolarized flavor nonsinglet PDFs with lattice QCD computable correlation functions".
  * The operator is ψ̄(ξ)γ^ν Φ(ξ,0) ψ(0) with a straight link, "which has been utilized to define quasi-PDFs".
  * Ji–Liu–Su–Zhang, JHEP 03 (2025) 045, on the quasi-PDF matching kernel 𝒞: "The three-loop result in Mellin space is presented in Ref. [Cheng:2024wyu]".
  * LAMET §13 item 9 must be corrected accordingly.
* **(4) No published refutation of the resolution of the Rossi–Testa critique — FALSE as stated.**
  * Rossi–Testa, PRD 98 (2018) 054028 (June 2018, after JZZ's June 2017 response): "Many Authors (see among others [Ji:2017rah]) consider the argument about UV power divergent moments inconclusive … Both counter-arguments are, however, untenable."
  * Rossi–Testa, PoS Confinement2018 092 (Nov 2018) concede that the obstruction does "not prevent extracting single PDF moments … [Karpie:2018zaz, Ma:2017pxb]". They maintain that the full PDF cannot be obtained.
  * Replies: Karpie–Orginos–Zafeiropoulos, JHEP 11 (2018) 178; Radyushkin, PLB 788 (2019) 380 ("no contradiction between the infinite values of the yⁿ moments of Q and finite values of the xⁿ moments of f").
  * No Rossi–Testa paper after Nov 2018 was found. The correct status is "contested in 2017–2018, with published exchanges on both sides".
* **(5) The RS proof with ℒ_G never appeared — holds.** INSPIRE: only two joint Rothstein–Stewart papers after 2015 (1601.04695; vNRQCD 2018). There is no "proof of factorization" paper by them.
* **(6) No BBNS endpoint refactorization (B → ππ, πK power corrections) — holds.** Fulltext search of papers citing BBNS 2000/2001 with "refactorization" and "endpoint divergence" gives 8 hits: h → γγ, structure-dependent QED effects in exclusive/leptonic B decays (B_s → μμ, B⁻ → μν̄), B̄ → X_sγ, B_c → η_c form factors, QCDF amplitudes from flavour symmetries, one-loop matching of NLP two-jet operators. None treats BBNS annihilation or spectator power corrections.
* **(7) No all-order twist-3 SSA factorization proof — holds.** The newest work, Rein–Schlegel–Tollkühn–Vogelsang, PRL 135 (2025) 251901, demonstrates factorization "at one loop".
* **(8) No QCD-with-quarks flow-equation proof — holds; not verified exhaustively.** Found only QED (Keller–Kopper 1991), spontaneously broken SU(2) Yang–Mills (Kopper–Müller 2000, 2009), SU(2) Yang–Mills (Efremov–Guida–Kopper 2017) and pure YM (FHH 2016).
* **(9) No multilocal BRST classification — holds.** Recent "alien operator" work (Falcioni et al. 2024) concerns local twist-2 operators.
* **(10) Gordan precedent — still unchecked.** A partial check found no precedent. INSPIRE fulltext "Gordan" + Landau equations gives only Clebsch–Gordan hits. Farkas' lemma appears in arXiv:2609.18668 (2026, causal LTD) in a different role. Pre-arXiv Landau-equation literature is not fulltext-indexed.
* **(11) DGOPS — verified, as their 2015 statement.** JHEP 01 (2016) 076, intro: "To the best of our knowledge, the cancellation of Glauber gluon exchange in single hard scattering has also been established only for Drell-Yan production".
* **Unrefereed preprints — verified.** INSPIRE `publication_info` is empty, arXiv has no `journal_ref`, and Crossref finds nothing for:
  * Collins 2007.04085 (v1 only);
  * Fröb–Holland 1603.08012 (v2, Jan 2021);
  * Beneke–Schnubel–Szafron 2608.25502 (v1; "Next-to-leading power endpoint DIS and PDF factorization");
  * Gamberg et al. 2211.13209 (v2);
  * Bodwin et al. 2512.11647 (v3, July 2026).

**Verdict: refuted** (items 3 and 4).

## 8. A07 — GPDs at x = ±ξ

* **Braun–Koller–Schoenleber, PRD 109 (2024) 074510.**
  * Abstract: corrections at x = ±ξ "are suppressed by the first power of the hard scale only … come from soft momenta and have nothing to do with the known UV renormalon".
  * Conclusions: "the limits x → ξ and (vP) → ∞ do not commute … the 1/(vP)¹ power correction in qGPDs at x = ξ is unrelated to the UV renormalon … it is generated by the discontinuity of the x-derivative of the quark GPD at x = ξ".
* **Su–Ji–Liu–Zhang, arXiv:2609.20545.**
  * Eq. (qlog): the logarithm ln(4P_z²(x±ξ)²/μ²) comes multiplied by |x±ξ|/(y±ξ).
  * "there is no leading-twist contribution from the soft scales"; "potential soft contributions near x = ±ξ are power suppressed".
  * Four data sets: ETMC20, ETMC21, MSULat23, ETMC25.
  * Regulator hierarchy: "ε₂ ≪ |ε₁| → 0 … Other limits … are divergent".
  * "may arise from regulator-related numerical artifacts".
  * Braun 2023 and BKS 2024 appear only in a citation list in their introduction. Their "difficulties" paragraph cites Holligan 2025 and the lattice discontinuities, not BKS.
* **Braun, JHEP 10 (2023) 134:** the kinematic twist-3 terms "are logarithmically enhanced … and are discontinuous at the kinematic points x = ±ξ".
* "Not strictly contradictory" is correct: both papers find the soft contributions power-suppressed, and BKS quantify the leading term as first-power.

**Verdict: confirmed.**

## 9. A08 — Collins 2020 and Mühlbauer 2020

* arXiv:2007.04085: v1 only (2020-07-08), "39 pages, 10 figures". Title: "A new and complete proof of the Landau condition for pinch singularities of Feynman graphs and other integrals". No journal on INSPIRE, arXiv or Crossref.
* Theorem 1 (`thm:main.contour`) has restrictions (a) and (b). Eq. (restrict) = (8.15), in §VIII B. Collins writes: "The theorem may well be true without these extra restrictions … the proof that we will give only applies when the restrictions are valid" and "A more general proof (or counterexample) would be obviously be useful".
* arXiv:2011.10368 (Mühlbauer): v1 only; the abstract includes "singularities of the second type".
* The OTHERS §1.2/§1.7 grades and FINAL_OUTLINE §0.9 item 4 ("Not adopted (D3…)") are as stated.

**Verdict: confirmed** (fix the title in CLAIMS.md).

## 10. A09 — rigour status of the OPE

* **Zimmermann**, Ann. Phys. 77 (1973) 570: "renormalizable interactions of a scalar field".
* **Collins 1984, §12.8, p. 321** (OA edition): "This expansion is proved in a gauge theory the same way as in any other theory."
* **IJJSZ:** "widely assumed …".
* **Hollands, Rev. Math. Phys. 20 (2008) 1033.** Abstract: "the operator product expansion closes on the space of gauge invariant operators". §5.1 "Matter fields, anomalies": "In this paper, we have considered only pure Yang-Mills theory for simplicity … chiral fermions".
* **Fröb–Holland, arXiv:1603.08012v2 (unpublished).**
  * Thm 1: existence "for an arbitrary massless, superficially renormalisable theory".
  * Thm 2: the Ward identity holds "if … H^{1,4}_{E(4)}(s|d) = 0", which holds "for pure Yang-Mills theories — but not, for instance, in the presence of chiral fermions in non-real representations".
  * The bounds are from FHH, J. Math. Phys. 57 (2016) 122301 (pure YM).
* **Convergence:** Hollands–Kopper, CMP 313 (2012) 257, massive φ⁴₄. The theorem's remainder bound is eq. (7) (counted on the source). Holland–Hollands–Kopper, CMP 342 (2016) 385, massless.
* **Anikin–Zav'yalov**, Ann. Phys. 116 (1978) 135: the abstract does not specify the theory class, so it stays UNVERIFIED.

**Verdict: confirmed.**

## 11. A10 — method of regions

* **Smirnov**, CMP 134 (1990) 109: expansions in limits of large momenta and masses "are proved" (abstract). The Euclidean character is from Jantzen 2011 §1: "Euclidean-type limits … through the agreement with existing and proven expansions by subgraphs".
* **Jantzen**, JHEP 12 (2011) 076: the formalism holds under conditions 1–4, including commuting expansions and absolute convergence of the expansions over the whole domain. It also needs the exchange of the series summations. §6 is "Example: Sudakov form factor" with a massive exchange and an off-shell leg.
* **SSS**, EPJC 79 (2019) 136, summary: "We proved our prescriptions for the contribution of the leading order for each essential facet. We proved our prescriptions in the general order in the simple situation with one essential facet."
* **GHJMS**, JHEP 07 (2023) 197: five authors, including **Schlenk**. They prove commutativity of multiple on-shell expansions for regions where every soft subgraph connects two jets.
* **GHJM**, JHEP 08 (2024) 127: from three loops, pinches in parameter space require "new regions … facets of the dissected polytope".
* **BHJNS**, PRL 134 (2025) 061901: a "hidden" three-loop active–active Glauber region; "we were unable to find this region using Asy2.1".
* **Beneke–Smirnov**, NPB 522 (1998) 321: threshold expansion only. Their examples are γ* → Q̄Q near threshold and two-loop threshold diagrams. The word "Sudakov" does not occur.
* **BBF**, LNP 896, §2.2 "The Sudakov Problem": massless one-loop vertex with L² ∼ P² ≪ Q². §2.3: massive Sudakov problem and the collinear anomaly.

**Verdict: confirmed.**

## 12. A11 — Glauber attributions

* **(1) — verified.**
  * Aybat–Sterman, PLB 671 (2009) 46, eq. (14): M^(Sub) ∝ Ψ_f × exp[i(α/2π)∫d²q⊥/q⊥² (e^{ib·q⊥} − 1)], "in which the phase is explicit".
  * RS: eq. (9.1) is the phase φ(b⊥) as the Fourier transform of the 1/q⊥² potential; eqs. (9.18)–(9.19) give G̃ = e^{iφ}; eqs. (11.12)–(11.13) give the S–S phase, which cancels after ∫d²Δp⊥.
* **(2) — verified.**
  * RS: "taken alone it is far from a proof of factorization, even in the abelian case".
  * A–A Glauber = soft zero-bin: RS §12 states that "the zero bin subtraction of soft or collinear loops involving these Wilson lines are exactly equal to the contribution from a corresponding set of Glauber graphs" (1 and 2 loops).
* **(3) — FALSE.**
  * RS §10.1 (eq. (10.1) current, n–n̄ production): "with the SCET operators we can still choose to treat the Glauber exchange as specific non-vanishing contributions which describe amplitude level rescattering phases, even for e⁺e⁻ annihilating into just final state strongly interacting particles".
  * Fig. 29: "Single soft emission graphs for an e⁺e⁻ annihilation current with a soft or Glauber loop".
  * SCET_I: "for all cases in SCET_I the Glauber graphs … do not contribute … the (iπ) factors are carried by the ultrasoft diagrams".
  * §10.3: "the result at any order for the n-n̄ production graphs should be the same in the theories with or without the inclusion of Glauber gluon exchange".
  * The rule "Ultrasoft Wilson line directions in SCET_I are determined by the physical directions since their diagrams do not have subtractions" is verified (RS §4).
* **(4) — verified.** RS §5.1, after the BPS redefinition: "only the adjoint lines Y_n and Y_n̄ appear in this Lagrangian". The n–n̄ Glauber operators survive.
* **(5) — verified.** Collins 2011 §14.4.5 (p. 560 of the OA edition): "the treatment of the Glauber region was originally formulated (CSS 1988) only in the context of … integrated parton densities … In fact, the argument works equally well for the TMD case."

**Verdict: refuted** (item 3). Corrected item (3): RS discuss the e⁺e⁻ (n–n̄ production) current at one and two loops. Glauber phases there are either explicit (SCET_II, equal to the soft zero-bin) or carried by ultrasoft graphs (SCET_I). RS expect the same at any order but give no all-order proof. For e⁺e⁻ event shapes, cite the contour-deformation argument (Collins 2011), and RS only as supporting one- and two-loop evidence.
