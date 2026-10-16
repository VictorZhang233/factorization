# Verification batch R-M19 – R-M29 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All eleven claims are of kind `correction_of_reference_doc` (source: `refdoc/REFDOC_ANALYSIS.md` ERR-M19 … ERR-M29).
Criterion: a correction is confirmed only if the physics statement our monograph would print is correct. The reference is not citable (REFDOC S62), so page locators are checked but a locator slip alone does not refute a claim.

## 0. Method and sources

* **Reference document.** I read `refdoc/refdoc.txt` (form feed = PDF page = printed page). Pages read in full: 7–8 (Def. 1.1), 63, 72–76, 83–84, 88–89, 93, 103, 107–111 (Note C.37, Lemma C.36–C.42, Rem. C.45), 117–122 (Ass. C.56, C.57, Lemma C.63–C.64 with proof), 127, 143, 147, 149–153 (Lemma D.38, (D.22), Ass. D.41, D.43), 174–175 (Note E.11), 214–216 (Prop. E.46), 223–226 (Rem. E.52, Tables 7–8), and the bibliography entries [46]–[63], [99]–[126].
* **Primary literature.** The arXiv e-print sources (LaTeX) were downloaded into a scratch directory and read as text. Collins–Scalise is a PostScript scan, so its arXiv PDF was converted with `pdftotext`. All bibliographic data below were checked with the INSPIRE API.
  * Nayak–Qiu–Sterman (NQS): hep-ph/0501235 = PLB 613 (2005) 45; hep-ph/0509021 = PRD 72 (2005) 114012; hep-ph/0608066 = PRD 74 (2006) 074007. The INSPIRE abstract of NQS PRL 99 (2007) 212001 was also read.
  * Catani–de Florian–Rodrigo (CdFR), 1112.4405 = JHEP 07 (2012) 026.
  * Forshaw–Seymour–Siódmok (FSS), 1206.6363 = JHEP 11 (2012) 066.
  * Guan–Herzog–Ma–Mistlberger–Suresh (GHMMS), 2408.03019 = JHEP 01 (2025) 090. Its title is "Splitting amplitudes at N³LO in QCD".
  * Henn–Ma–Xu–Yan–Zhang–Zhu, 2406.14604 = PRD 112 (2025) 076003.
  * Beneke–Buchalla–Neubert–Sachrajda (BBNS): hep-ph/9905312 = PRL 83 (1999) 1914; hep-ph/0006124 = NPB 591 (2000) 313; hep-ph/0104110 = NPB 606 (2001) 245.
  * Chay–Kim, hep-ph/0301262 = NPB 680 (2004) 302 [INSPIRE Chay:2003ju].
  * Bauer–Pirjol–Rothstein–Stewart (BPRS), hep-ph/0401188 = PRD 70 (2004) 054015.
  * Bauer–Pirjol–Stewart (BPS), hep-ph/0211069 = PRD 67 (2003) 071502.
  * Beneke–Feldmann (BF), hep-ph/0311335 = NPB 685 (2004) 249.
  * Bodwin–Braaten–Lepage (BBL), hep-ph/9407339 = PRD 51 (1995) 1125, with erratum PRD 55 (1997) 5853.
  * Kang–Qiu–Sterman (KQS), 1109.1520 = PRL 108 (2012) 102002.
  * Kang–Ma–Qiu–Sterman (KMQS), 1401.0923 = PRD 90 (2014) 034006.
  * Fleming–Leibovich–Mehen–Rothstein (FLMR), 1207.2578 = PRD 86 (2012) 094012.
  * Becher–Hager–Jaskiewicz–Neubert–Schwienbacher (BHJNS), 2408.10308 = PRL 134 (2025) 061901.
  * Collins–Scalise, hep-ph/9403231 = PRD 50 (1994) 4117.
  * Falcioni–Herzog, 2203.11181 = JHEP 05 (2022) 177.
  * Gehrmann–von Manteuffel–Yang, 2302.00022 = JHEP 04 (2023) 041.
  * Hollands, 0705.3340 = RMP 20 (2008) 1033.
  * Aybat–Rogers, 1101.5057 = PRD 83 (2011) 114042.
  * Kraus, hep-th/9709154 = Ann. Phys. 262 (1998) 155.
  * Grassi–Hurth–Steinhauser (GHS), hep-ph/9907426 = Ann. Phys. 288 (2001) 197.
  * Dybalski, hep-th/0412226 = LMP 72 (2005) 27.
  * Kisselev–Petrov, hep-ph/0502122 = PRD 71 (2005).
* **Abstract-only sources (paywalled).** I read only the INSPIRE abstracts of the following:
  * Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135
  * Joglekar, Ann. Phys. 108 (1977) 233 and 109 (1977) 210
  * Breitenlohner–Maison, CMP 52 (1977) 11, 39, 55
  * Hamberg–van Neerven, NPB 379 (1992) 143 (bibliographic data only)
  * Piguet–Sorella, LNP m28 (1995) (bibliographic data only)

  Project Euclid blocked the full BM text (HTTP Incapsula block).
* **Scripts.** All are in `verify/claims/batch_R-M19_s1_scripts/` and run with `python3 -I`; each output is saved as `*.out.txt`. The scripts written for this verification are prefixed `v2_`. The same directory holds three scripts from an earlier, interrupted attempt (`m19_*`, `m20_*`, `m25_*`). I did not rely on them; my `v2_` re-derivations are independent and agree with them.
  * `v2_rm19_nqs_pole.py`: Lorentz invariance and rest-frame reduction of the NQS pole.
  * `v2_rm20_colour.py`: SU(3) colour algebra behind CdFR §6.2 and FSS §5. It checks:
    * the operator identity and hermiticity;
    * CdFR (2partcorrcan) for q→qg, g→gg and g→qq̄;
    * CdFR (2partticharge);
    * the n = 5 operator and its expectation values on real and complex colour vectors.
  * `v2_rm24_zero_momentum_ir.py`: the Collins–Scalise mechanism, i.e. the 1/p² enhancement from a zero-momentum insertion.
  * `v2_rm25_spectrum.py`: the ω-support used in Lemma C.64, Nπ thresholds and the chiral limit.
  * `v2_rm27_selfenergy.py`: the self-energy eikonal factor of space-like and time-like Wilson lines, the divergence, a finite-length regulator, and the cancellation in (D.22).
  * `v2_rm28_taylor_sti.py`: momentum-space Taylor subtraction breaks transversality (the simplest Slavnov–Taylor identity) by local non-invariant terms.

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| R-M19 | **confirmed** | None. Precision: NQS take the Wilson-line direction l light-like, not time-like as the reference says. At NNLO the pole does not depend on l. | Yes. NQS PLB 2005 (abstract, eqs. (gn),(gn1)); NQS PRD 2005 §5 (eq. (IIIdivergence)); NQS PRD 2006 (all orders in v). |
| R-M20 | **refuted as worded** (components verified) | Do not print that the reference's two-loop statement is "wrong". It holds for unpolarized pure-QCD cross sections: FSS, with one step unproven; Henn et al. for the finite terms in N=4 SYM. It fails beyond pure QCD (EW phases), and the reason is the reality of tree-level colour vectors, not the colour sum. The CdFR, FSS and GHMMS statements in the claim are correct. "Mass singularities possibly from N³LO" is CdFR's statement, not FSS's. | Yes. CdFR §6.2–6.4; FSS abstract and §5–6; Henn et al. 2025; GHMMS introduction. |
| R-M21 | **confirmed, with precisions** | BBNS's two-loop infrared analysis is for B → Dπ (heavy–light) only, and BBNS say it is not an all-order proof. "Theorem-level" for the B→π form factor means an all-order SCET argument, i.e. our [A]. The Chay–Kim reference is Chay:2003ju = NPB 680 (2004) 302, not refs_merged.bib's Chay:2004zn. | Yes. BBNS 2000/2001; Chay–Kim 2004; BPRS 2004; BPS 2003; BF 2004. |
| R-M22 | **confirmed, with precision** | BBL's condition is momentum transfer Q² ≳ M², all orders in v. NRQCD factorization of the fragmentation functions remains a conjecture (KMQS say so explicitly). | Yes. BBL §VI.A; KQS 2012; KMQS 2014; FLMR 2012. |
| R-M23 | **confirmed** | None. Keep [V] for strict amplitude-level collinear factorization and [C] for PDF factorization of gap cross sections. | Yes. BHJNS 2025 ("does not amount to a proof"); FKS 2006; BNS 2021; BNSS 2023. |
| R-M24 | **confirmed, with precision** | The explicit forward counterexample (Collins–Scalise) is for a BRST-exact alien operator. For EOM operators the forward on-shell massless case is simply *not covered* by the proof; do not claim it fails. | Yes. Collins–Scalise 1994; Hamberg–van Neerven 1992. |
| R-M25 | **confirmed, with precision** | With m_u ≠ m_d and no QED, (W2) literally holds for the *lightest* nucleon. It fails for a neutron target, because p and n are two discrete levels below the Nπ threshold. Fix: impose the spectral condition in the target's flavour superselection sector. | Elementary; standard facts. |
| R-M26 | **confirmed, as a literature omission only** | It is *not* established that these works discharge Ass. C.24 or (B1)(B2). Keep both as assumptions until the scope is verified. Anikin–Zav'yalov's theory class remains UNVERIFIED (consistent with claim A09). | The omission concerns the reference; the sources exist (data verified on INSPIRE). |
| R-M27 | **confirmed** | None. | Yes. Aybat–Rogers 2011 ("very badly divergent … must be excluded"); project `research/c_tmd`. |
| R-M28 | **confirmed, with precision** | Say: "not a finite renormalization *in the sense of finite redefinitions of couplings and fields*; the relating finite counterterms include non-invariant ones". In the general (Hepp–Zimmermann) sense, MS-bar does differ from BPHZ(L) by finite local counterterms. | Yes. Algebraic renormalization: Piguet–Sorella 1995; Kraus 1998; GHS 2001; BM 1977. |
| R-M29 | **confirmed** | None. E.34 is Drell–Yan-specific (Glauber-window rewriting) but not part of the cancellation mechanism itself. | A statement about the reference's internal bookkeeping. |

---

## 2. R-M19: the NQS gauge completion is necessary at NNLO

**Reference (p. 76).** Fig. 49 caption: "…在色八重态算符补上伸向无穷远的 Wilson 线之后，这类交换产生的红外极点可以被矩阵元吸收". Text after Conj. 12.5: "Nayak、Qiu 与 Sterman [60] 在 NNLO（两圈）验证了…红外发散可以被吸收，前提是色八重态算符 O_n^H 被修改为包含连接到无穷远的类时 Wilson 线（以保证规范不变性）；**这些 Wilson 线在 NNLO 不改变数值结果**，但在更高阶可能产生非平凡的贡献。" [60] = NQS PRD 72 (2005) 114012.

**Literature.**
* NQS PLB, abstract: "We find uncanceled infrared poles at NNLO that are not matched by conventional NRQCD matrix elements. We show, however, that gauge invariance and factorization require that conventional NRQCD production operators be modified to include nonabelian phases or Wilson lines. With appropriately modified operators, factorization is restored at NNLO. We also argue that, in the absence of special cancellations, infrared poles at yet higher orders may require the inclusion of additional nonlocal operators, not present in the NRQCD expansion in relative velocity."
* NQS PLB §3: "the replacement … isn't really necessary if gauge dependence … is infrared safe … although gauge dependence is certainly free of infrared singularities at next-to-leading order, at NNLO this is no longer the case". §3 also fixes "l as a lightlike vector in the minus direction".
* NQS PLB §5 gives eq. (gn): Σ^(2) = α_s² (4/3ε)[(P·q)²/P⁴ − q²/P²]. Eq. (gn1) is its rest-frame form, α_s² (4/3ε) q⃗²/(4m_c²) = α_s² (1/3ε) v⃗²/4. The same section says: "when defined according to its gauge-completed form …, each octet NRQCD matrix element itself generates precisely the same pole terms … the NNLO correction is independent of the direction l".
* NQS PRD §5 ("Summary of results"): "Only diagram III provides a noncancelling pole, 2 Re III = −α_s² (1/3ε) v⃗²/4 … the gauge-completion of NRQCD matrix elements appears to be necessary … Conventional matrix elements simply will not match the infrared poles". The same section adds: "we can confidently conclude that the modification of the matrix element is necessary for matching at NNLO, at least in Feynman gauge".
* NQS PRD 74 (2006) 074007, abstract: the NNLO infrared singularities are "consistent with NRQCD factorization to all orders in … v. This factorization requires the gauge-completed matrix elements".

**Computation** (`v2_rm19_nqs_pole.py`).
* The bracket [(P·q)²/P⁴ − q²/P²] is Lorentz invariant: the difference between the boosted and rest-frame values is exactly 0.
* In the pair rest frame it equals q⃗²/(4(m²+q⃗²)).
* Hence Σ = α_s² v²/(12ε) + O(v⁴) with v = 2|q⃗|/m (the relative velocity), identical to (gn1).

**Assessment.** The pole is an uncancelled NNLO pole of order α_s²v²/ε. It is absent from the conventional operators and generated by the Wilson lines, so the Wilson lines are necessary and not numerically inert. The reference misreports its own source [60]. Precision: the reference says "time-like" lines, but NQS use a light-like l, and the NNLO coefficient does not depend on l.

**Verdict: confirmed.**

## 3. R-M20: the two-loop phase-cancellation statement

**Reference (p. 73, Rem. 12.2).** "对单圈与两圈的截面，这些相位项在对色求和后相消（单圈的 iπ 项在 |M|² 中消失）。Forshaw、Seymour 与 Siodmok [55] 指出，对于限制了末态辐射的可观测量…这些效应在更高阶不能相消，产生…超领头对数，它在 α_s⁴L⁵ 阶首次出现 [56]…对完全单举的喷注截面，是否在某一高阶出现破坏，目前没有定论。" The reference's own refs are [54] = CdFR and [55] = FSS.

**Literature.**
* **CdFR §6.2.**
  * P^(1,R) is strictly factorized. The breaking terms "are antihermitian and, therefore, they cancel" (eqs. (mp1two)–(itp1expl)).
  * At two loops, Δ̃_C^(2) "has a hermitian component that leads to the operator Δ̃_P^(2)". Eq. (wd2til) gives it as ∝ π f_abc T_i^a T_j^b T_k^c.
  * Δ̃_P^(2) "gives a vanishing contribution to P^(2,R) … with n ≤ 4 QCD partons … we have to consider … n ≥ 5". For n = 4 this follows from (wd2til4)+(2partcorrcan).
  * For n = 5 it "produces a non-vanishing factorization breaking contribution" (eq. (wd2til5)).
* **CdFR Summary.** "strict factorization is certainly violated in the SL collinear limit of two-loop squared amplitudes for parton–parton hard scattering with at least three final-state partons".
* **CdFR abstract and §6.4.** The violation has implications for logarithmically enhanced terms from NNLO, and "on various factorization issues of mass singularities (starting from the N³LO)".
* **FSS abstract.** "For pure QCD processes, factorization is violated at the three-loop level … Beyond QCD, factorization may be violated at the two-loop level provided that the hard subprocess contains matrix element contributions with phase differences between different colour topologies."
* **FSS §5.**
  * The commutator term's "expectation value on a QCD tree amplitude … is zero". The argument: T_i·T_j is real in natural bases, so the commutator is imaginary-antisymmetric, while the hard matrix is real-symmetric.
  * The caveat: the "second line" terms "are not yet proven to factorize".
  * The term is non-zero only for "certain electroweak processes" (s-channel W/Z interfering with t-channel exchange).
* **FSS §6.** The three-loop structure (eq. (3loopguess)). FSS also say the results "do not imply any mis-cancellation of the singularities of cross sections in hadron–hadron collisions" (colourless hadrons), and that they expect cancellation in inclusive observables.
* **Henn et al. (PRD 112 (2025) 076003).** In N=4 SYM, the two-loop factorization-violating terms (including the finite parts) "cancel at the level of color summed squared amplitudes". The authors conjecture that the QCD tripole terms are identical.
* **GHMMS, Introduction.** "While such factorization violating effects appear to cancel at the level of cross sections in pure QCD up to NNLO, their impact at higher orders is still an open question [Forshaw:2012bi, Henn:2024qjq]". This is a literature summary, not a GHMMS result.

**Computation** (`v2_rm20_colour.py`, SU(3), explicit tensor-product representation).
* **A.** f_abc T_i^aT_j^bT_k^c = −i[T_i·T_j, T_i·T_k] holds and the operator is Hermitian, for all 60 ordered triples (n = 5; error 2·10⁻¹⁶).
* **B.** CdFR (2partcorrcan), Sp0† f_abc T_1^a T_2^b Sp0 = 0, holds for q→qg, g→gg and g→qq̄ (≤ 8·10⁻¹⁷).
* **C.** CdFR (2partticharge) holds: T_(g)q = (C_A/2C_F)T_q, T_(q)q = (1−C_A/2C_F)T_q, T_(g)g = T_g/2, T_(q)g = (T_g+d_g)/2 (≤ 1·10⁻¹⁶).
* **D.** n = 5, with a collinear q g pair and reduced process q q̄ q′ q̄′:
  * Sp0† f T_2T_3T_4 Sp0 = (C_A/2C_F)·C_F·f T_P T_3 T_4 exactly. It is a non-zero Hermitian operator, which in the real (trace-basis-derived) orthonormal basis is purely imaginary antisymmetric (entries ±1.0607i).
  * ⟨M|F|M⟩ = 0 for relatively real colour vectors.
  * ⟨M|F|M⟩ ≠ 0 (e.g. −2.12 for a relative phase π/2) for complex ones.

  This reproduces both CdFR (non-vanishing in general) and FSS (vanishing for pure-QCD trees).

**Assessment.** Every literature component of the claim is correct: CdFR's Hermitian operator for ≥ 5 partons; FSS's three-loop onset in pure QCD and two-loop onset with EW phases; GHMMS's "appear to cancel up to NNLO". But these same facts show that the reference's sentence is right for unpolarized pure-QCD cross sections, modulo FSS's unproven input. The R4 reading note E4 had classified it as "needs qualification", and that is the accurate classification. The headline "the two-loop phase cancellation claim is wrong" would mislead a reader into thinking that pure-QCD two-loop cross sections violate factorization, which neither FSS, Henn et al. nor GHMMS say. Two further points:
* "Mass singularities possibly from N³LO" is CdFR's statement. FSS argue that hadron-level singularities are unaffected.
* The order counting differs between sources. A two-loop P^(2) on a 2→3 process is NNLO for three-jet observables but N³LO for 2→2 Born processes.

**Verdict: refuted as worded.** The printable corrected statement is in the structured output.

## 4. R-M21: BBNS / B → ππ / B → π status

**Reference.**
* p. 72 (c): "B → ππ：BBNS 的 QCD 因子化在 O(αs) 与领头幂次上成立 [48]；湮灭贡献与扭度 3 的'手征增强'贡献有端点发散…属于 C 级。" [48] = BBNS PRL 83 (1999) 1914.
* p. 72 (b) describes the SCET form-factor structure (soft overlap ξ_π plus hard spectator) correctly.
* p. 84, Table 1, nevertheless lumps "B → π、B → ππ | … | C | 端点发散".

**Literature.**
* BBNS NPB 591 (2000) §2.2: "The factorization formula allows us to compute radiative corrections to this result to all orders in α_s. Further corrections are suppressed by powers of Λ/m_b".
* BBNS NPB 591 §5 ("B→Dπ: Factorization in higher orders"): "we analyze in detail the infrared singularities for B̄_d→D⁺π⁻ decays at two-loop order … Some of the arguments … have straightforward extensions to all orders, but the following does not accomplish an all-order 'proof'". For light–light final states: "We plan to return to the extension of the factorization proof to light-light final states".
* BBNS NPB 606 (2001) §1: "a rigorous QCD factorization formula holds for the two-body decays B→M1M2, if … M2 … is a light meson", with results "at next-to-leading order in α_s and to leading power".
* Chay–Kim (NPB 680 (2004) 302; INSPIRE Chay:2003ju; refs_merged.bib's Chay:2004zn is "Soft Wilson lines in SCET", a different paper), abstract: "…at leading order in soft-collinear effective theory, and show that the decay amplitudes are factorized to all orders in α_s."
* BPRS abstract: "Using the soft-collinear effective theory we derive the factorization theorem for the decays B→M1M2 … at leading order in Λ/E_M and Λ/m_b … We argue that cc̄ penguins could give long-distance effects at leading order."
* BPS abstract: "We prove a factorization theorem for heavy-to-light form factors."
* BF abstract: "…show that the previously conjectured factorization formula is valid to all orders in perturbation theory … naive factorization … into collinear and soft matrix elements may be invalidated by divergences in convolution integrals … we circumvent the explicit regularization of endpoint divergences by a definition of the universal form factors".

**Assessment.** "Holds at O(α_s)" conflates the order of the explicit computation with the domain of validity. BBNS claim leading-power validity to all orders, with all-order arguments, and SCET leading-power derivations exist. For the B → π form factor, the decomposition into soft overlap plus hard spectator is an all-order SCET statement; only the further factorization of ξ_π fails. Two precisions:
1. The two-loop infrared analysis is for the heavy–light case, and BBNS explicitly deny it is an all-order proof.
2. BPRS's charming-penguin caveat means LP factorization for penguin modes is argued, not proved.

The grades proposed in REFDOC are consistent with the sources: [A] for the LP form-factor factorization and [P] for `prop:heavy-qcdf-lp`.

**Verdict: confirmed, with precisions.**

## 5. R-M22: Conj. 12.5 is not BBL's conjecture

**Reference (p. 76).** "猜想 12.5（NRQCD 产生因子化）(12.5) 在 p_T ≫ m_Q 或 √s ≫ m_Q 时，对任意阶的 αs 与领头的速度幂次成立。"

**Literature.**
* BBL §VI (production): "a general factorization formula for computing inclusive heavy-quarkonium production rates in high-energy processes that involve a momentum transfer Q² that is of order M² or larger". The formula is σ(H) = Σ_n F_n/M^{d_n−4}⟨0|O_n^H|0⟩, a sum organized by v-scaling.
* BBL, on hadron collisions: "we will merely assume that the Glauber divergences cancel … Given these assumptions, the factored form … holds to all orders in perturbation theory."
* BBL abstract: "processes involving momentum transfers of order M or larger".
* KQS abstract: a perturbative QCD factorization formalism "which includes both the leading power (LP) and next-to-leading power (NLP) contributions to the cross section in the m_Q²/p_T² expansion".
* KMQS: "We demonstrate that both LP and NLP contributions can be factorized … universal non-perturbative fragmentation functions". On the input fragmentation functions: "there is as yet no formal proof for the NRQCD factorization … a reasonable conjecture".
* FLMR: "In the limit p_⊥ ≫ m_Q short distance production can be thought of as the fragmentation of a pair of partons … We derive an all order factorization theorem … in terms of double parton fragmentation functions".

**Assessment.** BBL's conjecture covers all inclusive production with momentum transfer ≳ M and is organized order by order in v. It is neither restricted to p_T ≫ m_Q nor truncated at leading velocity power. At p_T ≫ m_Q the established structure is two-step: LP single-parton plus NLP pair fragmentation, then NRQCD for the fragmentation functions, which remains conjectural.

**Verdict: confirmed, with precision.**

## 6. R-M23: gap observables should be graded [C], not D

**Reference.**
* p. 73: "这类可观测量的标准共线因子化是失效的".
* p. 84 lists "间隙/非全局可观测量（pp）| — | D | 超领头对数、相干性破坏".
* Def. 1.1 defines D as "被证明破坏：存在显式的反例或一般性的破坏机制".

**Literature.**
* BHJNS abstract: "…we identify three-loop contributions from perturbative active-active Glauber-gluon exchanges with the right structure to render the cross section consistent with PDF factorization below the gap veto scale."
* BHJNS text: "While our analysis does not amount to a proof of PDF factorization, it demonstrates that the breaking of collinear factorization does not necessarily translate into a breaking of PDF factorization", and "at least up to three-loop order, the perturbative part of W_m is consistent with PDF factorization."
* SLL tower α_s^n L^{n+1}, n ≥ 4: FKS 2006, as quoted in FSS §1.
* SLL resummation: Becher–Neubert–Shao, PRL 127 (2021) 212002; BNSS, JHEP 12 (2023) 116.

**Assessment.** Amplitude-level strict collinear factorization is violated [V]. SLLs exist and are resummed. PDF factorization of gap cross sections is open, with explicit evidence for restoration. "Proven violated" is therefore an over-grading, and [C] is correct.

**Verdict: confirmed.**

## 7. R-M24: alien operators and the forward on-shell caveat

**Reference.**
* Lemma C.41(a), p. 109: "…故经 LSZ 约化后，EOM 算符在在壳的部分子态之间（**包括前向**）的矩阵元为零".
* Lemma C.41(b): BRST-exact operators vanish between physical states; "在微扰论中，对横向胶子与夸克的在壳外态，这由 BRST Ward 恒等式与 LSZ 约化直接得到".
* Inconsistently, Note C.37 (p. 107) concedes that forward kinematics (p, −p) is exceptional and needs extra infrared analysis.

**Literature (Collins–Scalise, full text).**
* Abstract: "the problems arise because of subtle infra-red singularities that appear when gluonic matrix elements are taken on-shell at zero momentum transfer".
* §1: "the one-loop gluonic matrix element of the alien operator fails to vanish at zero momentum transfer … it is a quadratic divergence in the proof that the matrix element vanishes … The problem arises when one considers matrix elements in an off-shell gluon state and then takes the gluon on-shell."
* §4.4: "This Green function has a manifest factor of zero when put on shell, but the zero is compensated by a quadratic infra-red divergence present only when the matrix element of the ancestor operator is evaluated at zero momentum transfer … there is, in fact, a 1/p² divergence which cancels against the inverse of the ghost propagator".
* §5: "Taking the momentum transfer to zero too soon introduces spurious infra-red divergences which cancel factors of zero on which the proof relies … keep the momentum transfer arbitrary … With this procedure, the Joglekar–Lee theorem should apply". CS add a caveat from Harris–Smith at non-zero momentum transfer.
* The counterexample operator is the gauge-variant part of θ^{μν}, which is BRST-exact up to the trivial equation of motion.
* Hamberg–van Neerven's apparent non-triangular mixing is the motivating puzzle.
* Falcioni–Herzog and Gehrmann–von Manteuffel–Yang work with off-shell operator matrix elements and explicit gauge-variant counterterms. GvMY note that on-shell external states avoid the mixing in renormalization, but that massless on-shell operator matrix elements are scaleless in DR.

**Computation** (`v2_rm24_zero_momentum_ir.py`). This illustrates the mechanism.
* A zero-momentum insertion doubles a propagator. Then (−p²)·G(2,1) = −1/ε + ln(−p²) + γ_E + O(ε), which does not vanish as p² → 0.
* By contrast, (−p²)·G(1,1) → 0.

**Assessment.** The vanishing of alien matrix elements is proved only off-forward or with IR-regulated legs. An explicit forward counterexample exists for a BRST-exact alien operator. For EOM operators the contact-term argument presupposes infrared regularity that is not established in forward massless kinematics. The claim's "vanish only off-forward / IR-regulated" must be read as "proved only", not as an asserted failure for EOM operators.

**Verdict: confirmed, with precision.**

## 8. R-M25: the spectral assumption (W2)

**Reference (pp. 118–121).**
* (W2): "该扇区中能动量的联合谱包含于 {p² = M²} ∪ {p² ≥ M_1²}，M_1 > M > 0：M 是该扇区的最低质量（核子），并且是孤立的".
* Proof of Lemma C.64, the only use of (W2): "由 (W2)，对易子的 Fourier 变换只在 (P ± q)² ≥ M² 时非零，即 |ω| ≥ 1". The elastic point at ω = 1 uses one-particle states, not isolation.
* The reference never mentions Haag–Ruelle.
* App. C uses massless quarks: Thm C.35 "n_f 味无质量夸克"; Rem. C.62 (p. 120) "无质量极限下…"; p. 106 "胶子（以及手征极限下的轻夸克）无质量".

**Computation** (`v2_rm25_spectrum.py`).
* (P+q)² − M² = Q²(ω−1) and (P−q)² − M² = −Q²(ω+1). So only the lower bound is used.
* With a massless pion, s(N + π(k)) = (k + √(M²+k²))², which starts at s = M²: there is no gap.
* PDG masses: M_n − M_p = 1.293 MeV, while the lowest Nπ threshold is 1073.25 MeV. Both nucleons are therefore discrete B=1 levels.

**Literature.** Dybalski (LMP 72 (2005) 27, §1): the Haag–Ruelle requirements "are ensured if the mass m is an isolated eigenvalue of the mass operator … if the mass … is an embedded eigenvalue then it seems difficult to meet the requirement".

**Assessment.**
* (W2) is false in the chiral limit.
* With isospin breaking, (W2) cannot hold for the neutron as target. Precision: with m_u ≠ m_d and no QED it holds literally for the lightest nucleon.
* With dynamical QED, isolation fails in every sector.
* Lemma C.64 needs only spec ⊂ {p² ≥ M²}. The correct sector is the target's flavour superselection sector: J is flavour-diagonal, so J|P⟩ stays in that sector.
* Isolation matters only for the standard Haag–Ruelle construction.

**Verdict: confirmed, with precision.**

## 9. R-M26: the literature behind the "no verbatim proof" assertions was not discussed

**Reference.**
* p. 83 (§15 summary): "余项在动量空间中的幂次估计（Zimmermann 坐标空间定理的动量空间形式，文献中没有逐字的证明）被列为输入假设 C.24".
* p. 88: "…在文献中没有逐字的证明（注 C.9）"; p. 89 (Fig. 54 caption) likewise.
* p. 93: "我们没有找到它在文献中逐字的证明，因此把它列为输入（假设 C.24）".
* p. 103: "对冻结 q 的森林和，我们没有找到逐字的证明，所以把结论列为假设 C.24".
* p. 111, Rem. C.45, on (B1): "我们没有找到对 OPE 中出现的全部（规范变的）算符基逐字陈述的定理".
* p. 127 (Table 2): "…改写，文献中没有逐字的证明".
* Bibliography: [116] Anikin–Zavialov, cited once (p. 117) for "Christ–Hasslacher–Mueller 与 Brandt–Preparata 的光锥展开在动量空间中的形式".
* Zav'yalov 1990, Joglekar 1977 I+II and Hollands 2008 are absent. The reference cites other Hollands papers ([90]–[92], [121]) and only Joglekar–Lee 1976 [106].

**Literature.**
* Anikin–Zav'yalov, INSPIRE abstract: "Short-distance and light-cone expansions for T-ordered products of currents are derived in the framework of the arbitrary order of the perturbation theory."
* Joglekar I, abstract: "…the operator product expansions in gauge theories in detail … which operators appear in the operator product expansion of, say two currents".
* Joglekar II, abstract: "We study the operator product expansion of two gauge-invariant currents. We discuss the operators that may appear in the expansion … hadronic physical matrix elements [of gauge-variant operators] either vanish or cannot be isolated".
* Hollands 2008 (full text). Abstract: "we can prove that the operator product expansion closes on the space of gauge invariant operators". §4 gives the BRST-cohomology argument. §5.1: "we have considered only pure Yang-Mills theory".
* Kisselev–Petrov (PRD 71 (2005)): "The light-cone OPE for the scalar theory was studied in [Zavialov 1979, 1990, 2004]".

**Assessment.** As a literature-omission correction this holds. The physics consequence does not follow: these works have not been shown to establish the frozen-q momentum-space remainder of C.24 for the relevant theory class. Anikin–Zav'yalov's theory class and remainder form are unverified; Joglekar is known only from abstracts; Hollands is pure YM with a position-space algebraic OPE. C.24 and (B1)(B2) must stay as assumptions until this is checked.

**Verdict: confirmed, as an omission only.**

## 10. R-M27: self-energies of space-like regulator lines

**Reference.**
* p. 63, Fig. 39: "(c)(d) 两端在同一条线上的图正比于 n(y_A)²：对类光线它们为零，对非类光线则不为零，必须保留".
* p. 143: "（对定义 D.21 的类空方向，n_A·n_A = −2e^{−2y_A} ≠ 0…这类指派的减除项给出软因子中 Wilson 线的自能型项（图 39(c)(d)）…但其全空间积分是快度正规化方案中**不可缺少的有限项**".

**Computation** (`v2_rm27_selfenergy.py`, n_A = (1, −e^{−2y_A}, 0_T)).
* n_A·k = −√2 k_T e^{−y_A} sinh(y − y_A), which is zero at y = y_A.
* n_A²/(n_A·k)² = −1/(k_T² sinh²(y−y_A)) exactly. The amplitude–conjugate product 1/[(x+i0)(x−i0)] is a pinch.
* The excised integral is ∫_{|u|>η} du/sinh²u ≈ 2/η: 18.07, 198.0, 1998.0, 19998 for η = 10⁻¹…10⁻⁴.
* A finite-length regulator gives ∫dx |(e^{iLx}−1)/x|² = 2πL to 10⁻⁵, i.e. a length divergence.
* For time-like lines the integral is ∫dy/cosh² = 2, which is finite.
* In (D.22), arbitrary per-line self-energy terms σ(y) cancel identically: ln f̃_A = ln f̃_B = 0 for the self-energy part.

**Literature.** Aybat–Rogers (PRD 83 (2011) 114042, eq. (soft)) use the same space-like n_A, n_B: "The soft factor contains Wilson line self-interaction (S.I.) divergences that are very badly divergent … They must therefore be excluded … all Wilson line self-energy contributions will cancel in the final definitions." The project's `research/c_tmd/DERIVATION.md` §3.2–3.6 agrees.

**Verdict: confirmed.**

## 11. R-M28: MS-bar versus BPHZ(L) in non-abelian gauge theory

**Reference.** (U1) of Ass. D.41, p. 152: "…无质量的线用 BPHZL 的辅助质量或 Euclid 减除点…到 MS 的转换是有限重整化（耦合常数与场的有限重新定义）". Yet the discussion of (Z2) of Ass. D.43 (p. 153) concedes that a gluon mass "在非阿贝尔理论中破坏 Ward 恒等式".

**Literature.**
* Kraus (BPHZL, all orders in a non-abelian theory), eq. (defren): Γ = Γ_ren + Γ_inv + Γ_break. "The non-invariant field polynomials Γ_break are used to remove the breakings of the symmetries, which have been introduced by an implicit scheme dependent adjustment of finite counterterms in the subtraction procedure"; the BPHZL breakings Δ_brs are absorbed by "local contributions of Γ_break".
* GHS §1: "the subtraction of ultra-violet divergences … leads to non-invariant Green functions … One introduces, order by order, finite non-invariant local counterterms which restore the symmetry relations (provided there are no anomalies)". Also: "Dimensional Regularization preserves gauge symmetries (up to the γ5 problem)".
* BM 1977, abstract: DR is "defined in such a way that the renormalized action principle holds … minimal, additive renormalization … derivation of Ward–Takahashi identities". The full text was not accessible.

**Computation** (`v2_rm28_taylor_sti.py`, illustration).
* The degree-2 Taylor polynomial, at a Euclidean point p0 = (0,0,0,m), of the transverse structure (p²δ^{μν} − p^μp^ν) ln p² is not transverse. For example, p_μT^{μ1} = p₁(m² − 2mp₄ + p²).
* It also contains a constant mass-like term diag(m², m², m², 0).
* So Π_R = Π_DR − T Π_DR violates p_μΠ^{μν} = 0 by local polynomials that cannot come from finite redefinitions of couplings and fields: no mass term arises that way, and the longitudinal part is fixed by the Slavnov–Taylor identity.
* Contrast: zero-momentum Taylor subtraction of an analytic transverse amplitude (massive QED loop) stays transverse.

**Verdict: confirmed, with precision on "finite renormalization".**

## 12. R-M29: the Glauber-specific content of (H1)(H2)

**Reference.**
* Table 8 caption (p. 225): "'输入'是从附录 D 继承…它们与 Glauber 区无关，对 DIS 与 e⁺e⁻ → hX 同样需要".
* p. 226: "专属于 Glauber 区的剩余未证明内容，被压缩为假设 E.33 的 (c)、假设 E.44 的 (a)–(d) 以及一般软子图的假设 E.33(a)(b)；其余假设（假设 E.18与E.34 与附录 D 的输入）是技术性的或与 DIS、e⁺e⁻ → hX 的因子化证明共有".

The same document, however, says the following.
* Prop. E.46(a), step 2: the n·K_i = 0 distributional mismatch "正是单个割线图中的 Glauber 问题". The check that "(c) 的定域项连同 (1 − T_R) 的误差恰好补足第一步中外线端点项在 n·K_i = 0 处的分布贡献…包含在附录 D 对改写形式所假设的 (H1)(H2) 中".
* Prop. E.46(c): the SA/AS localized spectator endpoints. "区域 R 中的定域项与区域 R′ 的软极限之间的重叠…我们没有证明二者在 U_R 上逐项一致，这一点属于命题 D.32 所假设的 (H1)(H2)".
* Note E.11(5): for SS lines "(H1) 不能逐图成立…对这两类被积函数的 (H1)(H2) 是附录 D 的输入".
* Prop. D.32: (H1)(H2) for the rewritten F̃_{G,R0}, "这是假设 D.14 在 Drell–Yan 中所取的形式；F_G 本身在实空间上被 Glauber 夹点卡住".
* Table 8's own rows assign the n·K = 0 check and the SA/AS allocation to "(H1)(H2)".
* Rem. E.52(1) notes the check matters for the direction of the TMD Wilson lines but not for collinear PDFs.

**Assessment.** These (H1)(H2) instances refer to constructions that exist only in Drell–Yan: the r_R-rewritten and spectator-family-summed integrands. Their content is the Glauber problem. Calling them "unrelated to the Glauber region, equally needed for DIS" contradicts the reference's own Prop. E.46 and Note E.11. E.34 (the fibre-integral envelope of the Glauber-window rewriting) is Drell–Yan-specific as well, though not part of the cancellation mechanism.

**Verdict: confirmed.**
