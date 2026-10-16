# Verification batch A23–A28 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. All six claims are of kind `attribution`.
For each attributed statement I tried to read the cited source itself. Where only the abstract was reachable,
that is said explicitly ("abstract level"). Bibliographic data were checked on INSPIRE (REST API) and on
Crossref; preprint status was checked on arXiv (API listing: versions, journal-ref) and INSPIRE.
Two small computations were re-done from scratch (items A23-19/20, A24-9).

## 0. Method and sources

**Scripts and logs** (all in `verify/claims/batch_A23_s1_scripts/`; run with `python3 -I`; downloads go to a
separate scratch directory passed as an argument):
* `inspire_fetch.py OUTDIR` — 86 INSPIRE queries (one per reference of A23–A28); every query returned exactly one
  record (the one author/title query for Graudenz was replaced by the journal query). Summary of all records,
  with abstracts, in `inspire_fetch.log`.
* `arxiv_fetch.py OUTDIR ids…` — arXiv PDFs + API metadata of the papers read in full (list below).
* `a23_item20_gluon_average.py` (PASS) — own D-dimensional Dirac-trace routine (perfect-matching recursion,
  index loops = D), γ*g → q q̄ in D = 4−2ε, Ward identity checked, own two-body phase space, MS-bar
  subtraction; done with both gluon averages 1/(D−2) and 1/2. Log: `a23_item20_gluon_average.log`.
* `a23_misc_checks.py` (PASS) — Gottfried sum in the QPM; MVV normalisation of c^(1)_{2,g}; z^{n−3} = z^{1−2ε}.

**Read in full or in the relevant sections (arXiv versions unless stated):**
Aybat–Sterman 0811.0246v1 (all 5 pp.); STAR 1511.06003 (text and Fig. 4); Bury–Prokudin–Vladimirov 2012.05135
(text p. 4); Braun–Manashov–Pirnay 0909.3410 (intro, §5 end, conclusions); Cammarota et al. (JAM) 2002.08384
(intro); Liu–Mecaj–Neubert–Wang 2009.06779 (intro, §3, §7); Liu–Neubert 1912.08818 (§5.2); Beneke–Schnubel–Szafron
2608.25502v1 (abstract, §7 Conclusion); Collins 1993 hep-ph/9208213v2 (§2 and Appendix); Lambertsen–Vogelsang
1605.02625 (§1); Moch–Vermaseren–Vogt hep-ph/0403192 (§3, §4, refs.) and Vermaseren–Vogt–Moch hep-ph/0504242
(§4, App. A); Frye et al. 1810.10022 (§1, §8); Collins–Soper–Sterman review hep-ph/0409313 (end of §9, §10.1–10.2);
Mondejar–Pineda 0901.3113 (§1); Geyer–Robaschik–Müller hep-ph/9406259 (§1);
Lowenstein–Zimmermann–Weinstein, "Formulation of abelian gauge theories without regulators II", SLAC-PUB-1451
(= PRD 10 (1974) 2500), pp. 2–3 (scanned preprint, CERN/INSPIRE file);
Einhorn, FERMILAB-PUB-76/22-THY (= PRD 14 (1976) 3451), intro, §V, conclusions (Fermilab scan);
Collins, *Foundations of perturbative QCD* (2011; OA reissue 2023, DOI 10.1017/9781009401845): chapter list
(Crossref chapter records .001–.020), ch. 12 pp. 435–437 and 461 (eqs. (12.35)–(12.40), (12.73)), section
headings of ch. 5, 10, 11, 13, 14 (Cambridge Core OA chapter PDFs).

**Not accessible:** Anikin–Zav'yalov Ann. Phys. 116 (1978) full text (ScienceDirect 403); CSS 1986, DFT 1980,
Di'Lieto et al. 1981, FGT 1984, CCG 1976, Christ–Lee 1966 full texts (used at abstract level; DFT/FGT also through the
CSS 1989 review text).

## 1. Summary

| id | verdict | what must change before printing |
|---|---|---|
| A23 | **confirmed** (item-by-item status in §2) | 19 items verified, item 2 answered in the negative (LZ 1975 does **not** cover gauge-fixed QCD), item 1 verified only at abstract level (**theory class still OPEN**). Corrections: item 7 ⇒ heavy-quark pairs in hadron collisions are [C] (CSS call it a "conjecture"); item 9 ⇒ the power-suppression statement comes from CSS 1989 §10.2 (non-cancellation at the level m⁴/s²) and FGT 1984, not from DFT/DGHS themselves; item 21 ⇒ the QCD DIS proof is Collins ch. 8–**11** (§§11.3, 11.9), not ch. 8–10. |
| A24 | **confirmed**, with refinements | (6): Bjorken scaling in DIS in the 't Hooft model is Einhorn's result; CCG constructed the current amplitudes and the e⁺e⁻/vacuum-polarisation part. Einhorn's published title differs from INSPIRE and from our bib entry. (2): Collins–Metz *argue* universality; Meissner–Metz give "additional strong evidence". (4): primary sources for the O(α_s²) Lam–Tung violation are Mirkes 1992 and Mirkes–Ohnemus 1995. "Recalled" journal data (CCG, Einhorn, Burkardt–Koike) are now verified. |
| A25 | **confirmed**, one wording fix | Bodwin et al. 2020 identified "the sources of **some** of these differences", not all. Gamberg et al. is still unpublished (arXiv v2, 2023; no journal-ref on arXiv or INSPIRE). |
| A26 | **confirmed** | All five conflicts exist as described; the lead-author resolutions are recorded in spec_v2 (§5 below) and agree with the CONTEXT tag definitions. |
| A27 | **confirmed**, with corrections | STAR's χ² values come from the fit to the **W±** asymmetries only (not Z). BPV: the same-sign fit "does exhibit tensions between DY and SIDIS data sets". The BMP–Kang–Qiu disagreement was reconciled in 2012 (Kang–Qiu PLB 713 (2012) 273; Schäfer–Zhou PRD 85 (2012) 117501; BMP erratum PRD 86 (2012) 119902). JAM 2020 say their analysis "further indicates a resolution" of the sign mismatch. |
| A28 | **confirmed**, with precision notes | LMNW prove the first refactorization condition in §3.1 (eq. (3.5)) and the second in §3.2 (eqs. (3.12)–(3.14)). In LN 2020 they were verified at NLO and conjectured to all orders. BSS 2026 is v1 only, unrefereed. "[R] by explicit examples" means: shown in specific processes, not a general theorem. |

## 2. A23 — REVIEW §11 "verify" list (21 items)

Status key: **V** verified (source read); **V-abs** verified at abstract level; **ANS** question answered;
**OPEN** not decidable from accessible sources; **CORR** verified after a correction.

| # | REVIEW item | status | evidence and the statement that may be printed |
|---|---|---|---|
| 1 | Anikin–Zav'yalov, Ann. Phys. 116 (1978) 135: light-cone expansion proof in renormalized PT | V-abs / **OPEN (scope)** | Data: Ann. Phys. 116 (1978) 135–166 (INSPIRE, Crossref). Abstract: "Short-distance and light-cone expansions for T-ordered products of currents are derived in the framework of the arbitrary order of the perturbation theory." Which theories are covered (scalar only? gauge theories?) could not be checked: the full text is inaccessible. Geyer–Robaschik–Müller (hep-ph/9406259, §1) display the A–Z light-ray expansion "for a toy model with scalar fields". Zav'yalov revisited the problem in TMP 138 (2004) 370. **Print:** "derived to arbitrary order of renormalized perturbation theory (Anikin–Zav'yalov 1978)". Do not cite it as a proof for QCD; the open scope question is also N13(iii)/R-M26. |
| 2 | Lowenstein–Zimmermann, NPB 86 (1975) 77: does BPHZL cover IR finiteness of off-shell Green functions in gauge-fixed QCD? | **ANS: no** | Data: NPB 86 (1975) 77–103. Abstract: the scheme "is first developed for the massless A⁴ model and then applied to the Goldstone and pre-Higgs models". In the classification of the same authors (Lowenstein–Zimmermann–Weinstein, PRD 10 (1974) 2500, preprint pp. 2–3), the "pre-Higgs model" is an **abelian** vector meson with an explicit mass, coupled to a complex scalar (v ≠ 0, δ = 0, m₀ ≠ 0). There is no non-abelian gauge field and no Faddeev–Popov ghost. **Print:** LZ 1975 (NPB 86) is the BPHZL scheme for massless scalar and abelian vector-meson models. The companion CMP 44 (1975) 73 is the general IR+UV power-counting theorem. Neither is a QCD statement. |
| 3 | Frye et al., PRD 99 (2019) 056015: KLN, forward/disconnected | V | §8 "Summary and Conclusions", points 1–2: "One never needs to sum over initial and final states to achieve IR finiteness…"; "IR finiteness often requires the inclusion of forward scattering and the interference between disconnected and connected Feynman diagrams." |
| 4 | Gaunt, JHEP 07 (2014) 110: exact claim | V-abs | Abstract: "for hadronic transverse energy E_T … the classic CSS argument for the cancellation of Glauber gluons breaks down at the level of two Glauber gluons exchanged between the spectators" (shown); "we suggest that this failure … corresponds to a failure of the 'standard' factorisation formula … at leading power", also for "MPI sensitive observables", e.g. beam thrust B⁺_{a,b} and transverse thrust (suggested). The dispute with SYZ 2018 is E36 (confirmed in batch_E31_s1). |
| 5 | Aybat–Sterman, PLB 671 (2009) 46: scope with coloured final states | V (full text) | **Scope.** Weighted transition probabilities (parton distributions) with an incoming parton and an incoming Wilson line Φ_β(0,−∞). An IR-safe weight S(N) may select final states with jets or heavy coloured particles. The paper "outline[s] arguments"; it is not a complete proof. Assumed or deferred steps: the factorization of β-jet spectators ("We will assume this result here, and review details … elsewhere [16, 'in preparation']"; that paper never appeared on INSPIRE) and the collinear subtractions ("We shall assume …"). One transverse scale m is assumed; multiple scales are only sketched. Glauber "pinch" is replaced in the hybrid LCOPT form by "a mismatch between the directions of the deformations for initial and final states". The phases cancel only after the inclusive sum over final states, and only "so long as the weight S(N) is chosen so that radiation of this scale [energies ~m²/Q] is summed inclusively in all directions". With a wide-angle energy veto E₀, non-cancelling logs of E₀/Q are expected, and at high orders phase effects (cf. FKS SLLs). Explicit abelian phase: their eq. (14). |
| 6 | FSS, JHEP 11 (2012) 066: order of collinear-factorization breaking | V-abs | Abstract: for non-inclusive observables in hadron–hadron collisions, "For pure QCD processes, factorization is violated at the three-loop level", "driven by the non-commutation of Coulomb/Glauber gluon exchanges with other soft exchanges". Beyond QCD it "may be violated at the two-loop level" if the hard process has phase differences between colour topologies. |
| 7 | CSS, NPB 263 (1986) 37: completeness of the Glauber argument ([A]/[C] in B13) | V-abs ⇒ **[C]** | Data: NPB 263 (1986) 37–60. The abstract considers "several low-order graphs" and "argue[s]" that the standard factorization formula applies, then: "We emphasize that an analysis at all orders of perturbation theory is needed to reliably establish this conjecture." The heavy-quark-pair entry of B13 is therefore [C], as in SURVEY item 9 and `conj:dy-coloured-final`. |
| 8 | Collins, PRD 58 (1998) 094002: "error suppressed uniformly in m/Q" | V-abs | Exact wording: "The power-suppressed corrections to the factorization formula are uniformly suppressed by a power of Λ/Q, independently of the size of heavy quark masses, M, relative to Q." Also: "Although the proof is explicitly given for deep-inelastic scattering, the methods apply more generally". |
| 9 | DFT 1980 / Di'Lieto et al. 1981: power suppression for DY | V (via CSS review) | DFT (NPB 168 (1980) 93–110, abstract): with "two quarks (with non-zero mass, and colour averaged) in the initial state", "non-leading infrared divergences coming from two soft gluons do not cancel". DGHS (NPB 183 (1981) 223–250, abstract): in two loops "the single logarithmic divergence does not cancel in the colour averaged cross section"; agreement with DFT "fortuitous" (intermediate results differ). **Precise power statement** (CSS 1989 review, hep-ph/0409313, end of §9 and §10.2, citing DFT, FGT 1984, BFT 1989, DGHS): two-loop calculations "show that infrared divergences cancel at leading power (although not at higher twist)", and "At two loops, noncancelling divergences occur at the level m⁴/s² in the Drell–Yan process"; factorization is respected at m²/s. FGT 1984 (NPB 233, 307, abstract): the BN cross section for q q̄ annihilation is "infrared finite [to O(g⁴)], except for terms which are power-suppressed at high energies", with the argument extended to g⁶ and, "assuming a generalized unitarity principle", to all orders. |
| 10 | Beneke–Braun, NPB 454 (1995) 253: no 1/Q renormalon in DY | V-abs | Abstract: the leading IR-renormalon divergence of the resummed DY cross section "is cancelled by higher-order perturbative contributions in the exponent". "From this evidence", higher-twist corrections to the hard cross section "should therefore intervene only at order Λ²/(Q²(1−z)²) in the entire perturbative domain Q(1−z) > Λ". This is renormalon evidence near threshold, not a proof (consistent with REVIEW C11 "suggest but do not prove"). |
| 11 | BNRS 2016 / BNS 2021: data and status | V | BNRS: JHEP 11 (2016) 019 [Erratum JHEP 05 (2017) 154], factorization theorems for cone-jet cross sections with RG resummation of NGLs and a two-loop check. BNS: PRL 127 (2021) 212002, "the all-order structure of these 'super-leading logarithms' for generic 2→l scattering processes at hadron colliders" and closed-form resummation. Grades as in VF (A20 for the loop orders). |
| 12 | Mankiewicz–Piller 2000 | V | PRD 61 (2000) 074013 (hep-ph/9905287). Verified with full text in batch_E19_s1 (E21) and batch_R-M8_s1. Abstract: "QCD factorization cannot be applied as shown explicitly in a leading order calculation". |
| 13 | Ebert–Michel–Stewart–Sun 2022 | V-abs | JHEP 07 (2022) 129. They compute the cumulative k_T ≤ k_T^cut integral of TMD PDFs in terms of collinear PDFs, "correcting the naive picture where the TMD PDF integrates to a collinear PDF" (percent-level corrections for scales near k_T^cut). |
| 14 | Braun–Vladimirov–Zhang 2019 | V | PRD 99 (2019) 014013. Endpoint scaling Λ²/(x²(1−x)P_z²) verified in batch_E01_s1 (E03); the (cR) erratum does not affect it. |
| 15 | Korchemsky–Sterman 1999 | V-abs | NPB 555 (1999) 335–351. Differential thrust and heavy-mass distributions in the two-jet limit are convolutions of non-perturbative shape functions with resummed perturbative cross sections; "They organize all power corrections of the form 1/(eQ)ⁿ". |
| 16 | Shifman 2000 (hep-ph/0009131) | V | "Quark–hadron duality", in *At the Frontier of Particle Physics / Handbook of QCD*, vol. 3, eds. M. Shifman (and B. Ioffe), World Scientific 2001, pp. 1447–1494, DOI 10.1142/9789812810458_0032 (INSPIRE + Crossref). The bib entry `Shifman2000` agrees. |
| 17 | Graudenz 1994: NLO SIDIS | V-abs | NPB 432 (1994) 351–376 (hep-ph/9406274). Finite NLO one-particle-inclusive DIS cross section, with the collinear target-fragmentation divergence absorbed into fracture functions. |
| 18 | page data | V | INSPIRE and Crossref agree: Li–Sterman NPB 381 (1992) 129–140; Soffer PRL 74 (1995) 1292–1294; Labastida–Sterman NPB 254 (1985) 425–440; Kodaira NPB 165 (1980) 129–140; Christ–Lee Phys. Rev. 143 (1966) 1310–1321. |
| 19 | z^{1−2ε} in the D-dimensional FF (Collins ch. 12) | V | Collins 2011 §12.4.3–12.4.4: integrated FF (12.38) (scalar) and (12.40) (Dirac) carry the prefactor **z^{n−3}**, n = 4−2ε, i.e. z^{1−2ε}. Collins: "The factor z^{n−3} is perhaps unexpected … It arises from the normalization of the hadron state, and then from the change of variable from the parton to the hadron frame." Used explicitly in (12.73) (g²μ^{2ε}z^{1−2ε}/(N_{c,g}(2−2ε)(2π)^{4−2ε})). |
| 20 | gluon D-dim average behind the standard MS-bar C_g, Δ_qg (D5) | V (own computation) | Own computation (`a23_item20_gluon_average.py`; traces agree with c_dis §6, Ward identity 0). With the 1/(D−2) = 1/[2(1−ε)] average, the MS-bar remainder is exactly C_g = T_F[(z²+(1−z)²) ln((1−z)/z) − 1 + 8z(1−z)]. This equals MVV hep-ph/0504242 eq. (4.4), the first-order result attributed there to BBDM 1978 (normalisation conversion: `a23_misc_checks.py`). With a 1/2 average: C_g → C_g + T_F[z²+(1−z)²]. The pole −(2/ε)P_qg and C_L^g are unchanged. The same 1/(D−2) average (MS-bar gluon PDF, CDR) underlies Δ_qg; the shift cancels in Δ_qg − C_g (one collinear pole each), as REVIEW D5 says. Collins also averages over (2−2ε) gluon polarisations (eq. (12.73)). |
| 21 | Collins (2011) chapter numbers | **CORR** | Crossref chapter records: 1 Introduction (1–7); 2 Why QCD? (8–35); 3 Basics of QCD (36–68); 4 Infra-red safety and non-safety (69–86); 5 Libby–Sterman analysis and power-counting (87–160); 6 Parton model to parton theory: simple model theories (161–212); 7 Parton theory: further developments (213–242); 8 Factorization for DIS, mostly in simple field theories (243–283); 9 Corrections to the parton model in QCD (284–312); 10 Factorization and subtractions (313–397); 11 DIS and related processes in QCD (398–425); 12 Fragmentation functions: e⁺e⁻ annihilation to hadrons, and SIDIS (426–478); 13 TMD factorization (479–539); 14 Inclusive processes in hadron–hadron collisions (540–572); 15 Introduction to more advanced topics (573–581). REVIEW's ch. 5 (Landau criterion §5.1.4, reduced graphs §5.2, power counting §5.5/5.8, leading regions §5.9), ch. 12–13 (SIA/SIDIS, FF definition), ch. 14 (DY; Glauber example §14.3, DY factorization §14.4, TMD DY §14.5), and ch. 10, 13–14 (TMD) are correct. **B10 is not:** "ch. 8–10 (regions; Ward identities; …)". The QCD DIS proof is in ch. 11: §11.3 "Factorization for DIS" (11.3.1 abelian, 11.3.2 non-abelian gluon) and §11.9 "Ward identities to convert K gluons to Wilson line". Ch. 10 has only the Sudakov-form-factor version (§10.8.3 "Elements of diagrammatic Ward identities"). Print **ch. 8–11**. |

The introductory cross-references of the claim are correct as follows. Mankiewicz–Piller → E21 (verified).
Gaunt/SYZ → E36 (verified). BVZ → E03 (verified). Aybat–Sterman → R-M32 has no stage-1 report yet, but my reading of
AS 2009 (item 5) supports R-M32's description of the method: hybrid LCOPT, Glauber pinch replaced by a
mismatch of deformation directions, phases cancelled after the inclusive final-state sum.

## 3. A24 — misconception-box attributions

1. **Collins 1993 → Collins 2002 after BHS 2002. V (full text of Collins 1993).** Collins 1993 (NPB 396 (1993)
   161–182, hep-ph/9208213, §2 and Appendix): Sivers' asymmetry "is prohibited because QCD is time-reversal invariant.
   This is shown in the appendix". The Appendix proof uses PT and hermiticity to show f̂(LR) = f̂(RL) = 0. Collins 2002
   (PLB 536 (2002) 43–48), abstract: BHS's mechanism is a Sivers asymmetry. "An earlier proof that the Sivers asymmetry
   vanishes because of time-reversal invariance is invalidated by the path-ordered exponential…", and "the time-reversal
   argument shows that the Sivers asymmetry is reversed in sign in hadron-induced hard processes (e.g., Drell–Yan)".
   BHS: PLB 530 (2002) 99–107.
2. **T-odd FF universality. V-abs.** Collins–Metz, PRL 93 (2004) 252001: Wilson-line directions are consistent with
   factorization and give universality between e⁺e⁻, SIDIS and DY. Only a T-transformation of the soft function and the
   parton densities enters for DY, so T-odd *parton densities* reverse sign and fragmentation functions do not.
   Meissner–Metz, PRL 102 (2009) 172003: the partonic pole matrix elements for fragmentation vanish, which "gives
   additional strong evidence for the universality of transverse momentum dependent fragmentation functions".
   Print: "universality argued by CM 2004, further supported by MM 2009".
3. **Transverse links. V-abs.** Ji–Yuan, PLB 543 (2002) 66–72 (light-cone-gauge link at spatial infinity reproduces the
   BHS FSI). Belitsky–Ji–Yuan, NPB 656 (2003) 165–198 ("a transverse gauge link … indispensable for restoration of the
   gauge invariance of parton distributions in the light-cone gauge").
4. **Lam–Tung violated at O(α_s²). V.** Lam–Tung, PRD 21 (1980) 2712: "not subject to any first-order QCD
   modification". Lambertsen–Vogelsang, PRD 93 (2016) 114013, §1: the NLO corrections "first … derived in Refs.
   [24, 25]" (Mirkes NPB 387 (1992) 3; Mirkes–Ohnemus PRD 51 (1995) 4891) "suggest overall modest O(α_s²) effects …
   so that also the Lam–Tung relation, although found to be violated at NLO, still holds to fairly good approximation".
   At q_T ≠ 0, O(α_s²) is NLO. Print with Mirkes 1992 and Mirkes–Ohnemus 1995 as primary sources.
5. **DFT 1980, DGHS 1981. V-abs.** See A23 item 9. Two-loop non-cancellation, massive colour-averaged initial quarks.
6. **'t Hooft-model scaling. V (Einhorn) / V-abs (CCG).** Journal data were recalled and are now verified:
   CCG PRD 13 (1976) 1649–1669 and Einhorn PRD 14 (1976) 3451–3471. Einhorn's **published title** (Crossref) is
   "Confinement, form factors, and deep-inelastic scattering in two-dimensional quantum chromodynamics". INSPIRE and our
   bib entry `Einhorn1976` carry the preprint title "Form-Factors and Deep Inelastic Scattering in Two-Dimensional QCD".
   Fix the bib (REFS policy: publisher titles). Einhorn (preprint §V): "Because the theory is superrenormalizable,
   one expects to find exact scaling, and this will be borne out by explicit calculations". The abstract adds that the sum
   over hadronic final states "reproduces the parton model precisely". CCG's abstract covers current amplitudes, asymptotic
   freedom and the quark mass as scale of mass corrections. Mondejar–Pineda (0901.3113, §1) credit CCG and Einhorn for
   "the vacuum polarization and for DIS off a meson", respectively. **Print:** DIS scaling and parton model in the
   't Hooft model: Einhorn 1976, building on CCG 1976. Caveat for "[R] in that model" statements about power
   corrections: Mondejar–Pineda (PRL 101 (2008) 152002; PRD 79 (2009)) find a violation of the OPE at NLO in 1/Q² in this
   model. Leading-twist scaling is unaffected.
7. **Burkardt–Koike δ(x). V-abs** (data recalled, now verified: NPB 632 (2002) 311–329, hep-ph/0111343). A δ(x) term in
   h_L (and h_L³) for a one-loop dressed massive quark, and also in e(x, Q²), "but not in g_T(x,Q²), to this order".
   This is a perturbative quark-target result.
8. **P⁺_NS − P⁻_NS at NLO ∝ C_F(C_F − C_A/2). V.** MVV hep-ph/0403192 eqs. (4.6)–(4.7): P^(1)−_ns = P^(1)+_ns +
   16C_F(C_F − C_A/2){p_qq(−x)[ζ₂ + 2H_{−1,0} − H_{0,0}] − 2(1−x) − (1+x)H₀} (a_s = α_s/4π). They are quoted "[3, 8]",
   [8] = Curci–Furmanski–Petronzio NPB 175 (1980) 27–92 (the x-space kernels; the N-space γ^(1)± are from [4, 6] =
   Floratos–Ross–Sachrajda NPB 129 (1977) 66 [Erratum NPB 139 (1978) 545] and González-Arroyo–López–Ynduráin 1979).
   Independent re-coding: batch_R-M8_s1 (R-M10).
9. **Gottfried/NMC. V-abs.** NMC PRL 66 (1991) 2712: S_G = 0.240 ± 0.016, "below the quark-parton-model expectation of
   1/3". Reevaluation, PRD 50 (1994) R1: still below 1/3. In the QPM with isospin symmetry,
   S_G = 1/3 + (2/3)∫(ū − d̄)dx (`a23_misc_checks.py`), so 1/3 requires ū = d̄. The original sum rule is Gottfried
   PRL 18 (1967) 1174 (nonrelativistic quark model).
10. **Christ–Lee 1966. V-abs.** Phys. Rev. 143 (1966) 1310–1321. The abstract is about the C/T-noninvariant effects in
    l±N → l±Γ. The specific "no single target-spin asymmetry at one-photon exchange" statement was not read in the
    full text.

## 4. A25 — quarkonium, EW and DPS (abstract level; preprint status checked)

* **NQS 2005–06. V-abs.** PLB 613 (2005) 45–51: "uncanceled infrared poles at NNLO that are not matched by
  conventional NRQCD matrix elements"; Wilson lines restore factorization "at NNLO"; "in the absence of special
  cancellations, infrared poles at yet higher orders may require … additional nonlocal operators". PRD 72 (2005)
  114012 (NNLO calculation, to v²). PRD 74 (2006) 074007: "consistent with NRQCD factorization to all orders in the heavy
  quark relative velocity v", octet → singlet. Grade [P] is correct.
* **Bodwin–Chung–Ee–Kim–Lee 2020. V-abs, wording fix.** PRD 101 (2020) 096011 (1910.05497). Wilson-line-direction
  independence of the IR divergences: "We find this to be the case". "The results … differ in some respects from those
  of … Nayak, Qiu, and Sterman … **We have identified the sources of some of these differences.**" Both are consistent with
  NRQCD factorization; "the general principle … has yet to be revealed". Replace "(sources identified)" by "the sources of
  some of the differences were identified".
* **η_c. V-abs.** BHK PRL 114 (2015) 092004 (title: "… challenges nonrelativistic-QCD factorization"; NLO NRQCD
  "greatly overshoot[s]" LHCb when LDMEs from J/ψ fits are converted by HQSS). Han–Ma–Meng–Shao–Chao PRL 114 (2015)
  092005 (the bound is consistent with their J/ψ fits). Zhang–Sun–Sang–Li PRL 114 (2015) 092006 (good description of η_c
  and J/ψ data).
* **CCC 2000. V-abs.** PRL 84 (2000) 4810–4813: initial states "carry a definite nonabelian flavor", so the EW
  corrections to inclusive TeV-scale cross sections have "Bloch–Nordsieck violating double logs", analysed for e⁺e⁻ →
  hadrons. [V] is correct.
* **BERV 2019. V-abs.** PRD 100 (2019) 096008: for observables measuring the weak charge of final states, LP
  non-factorizable EW corrections; "factorization-violating logarithms, which start at order α_s²α_W²log⁴(Q²/M_W²)". [V]
  as computed.
* **DGOPS 2016. V-abs.** JHEP 01 (2016) 076: Glauber cancellation "at all orders for double Drell–Yan … both for the
  integrated cross section and for the cross section differential in the transverse boson momenta". [A] is correct.
* **EGS 2022. V-abs.** JHEP 06 (2022) 007 [Erratum JHEP 07 (2023) 096]: "Working under the assumption that leading
  power Glauber interactions do not spoil factorization at this order". [A](cond.: Glauber) is correct.
* **Gamberg–Kang–Shao–Terry–Zhao. V.** arXiv:2211.13209: latest v2 (2023-02-14), no journal-ref (arXiv API). INSPIRE
  record 2514090 has no publication info. The † (unrefereed) is correct as of 2026-10-10.

## 5. A26 — grade conflicts between our materials (internal check)

| # | conflict (verified in the files) | resolution recorded in spec_v2 | assessment |
|---|---|---|---|
| 1 | OTHERS §2.7 table: QCD with quarks "[R] in PT via classical results". OTHERS §1.2/§1.7: Collins 2020 Thm 1 "[R]†". FINAL_OUTLINE §0.9 item 4: "**Not adopted** (D3…)". | FINAL_OUTLINE_v2 §0.8: D3 binding (`thm:dis-ope` [A]); MD14: `thm:front-collins-pinch` [A] (preprint-only proof). REFS_NOTES_v2 A09: the OTHERS grade is "not adopted". | Correct. No self-contained proof of the gauge-invariant OPE for QCD with quarks exists (OTHERS itself says so), so [A] fits the CONTEXT definition. Collins' Thm 1 is complete but unrefereed and needs hypotheses (a)(b). [A] is conservative and consistent. |
| 2 | YZLIU §3.E2: "Grade: [R]-level … at the same standard as the renormalization of HQET". LAMET §3.2 Thm 3.1: "Grade [A]", with N1–N3 [A] in §4.5 ("asserted for space-like n"). | Ch22 `prop:lattice-renormalizability` [A] "(v1 label and tag)", status lists the asserted space-like extension (`asm:lamet-aux-renorm`) and the superficial-degree counting. | Correct. Both gaps named by LAMET are real (JZZ's space-like statement is "asserted"; IMQY count superficial degrees). [R] is not justified. |
| 3 | LAMET table row 18 and §6.1: "[R]_{2L} (41 terms, two constants fitted)". YZLIU C2: "[P] for the explicit NNLO verification". | Ch23 `thm:yzliu-threshold` [A]; `prop:yzliu-threshold-nnlo` [P]. | Correct. Two constants (c_a, c_H) are *extracted* from the comparison. A finite-order check with fitted constants is [P] by definition; only c_H has an independent cross-check (dRV 2023). |
| 4 | OTHERS Prop. 1.2 (Gordan) "[R]". v1/v2 outline: `lem:appD-gordan` "(数学，无标签)". | Kept untagged (pure mathematics); Ch24 adds `lem:front-min-norm` (constructive proof) [PENDING-VERIFY: N02]. | Not a physics conflict: a pure-math lemma is untagged by the outline's convention. Gordan's theorem itself is classical. N02 is confirmed in batch_N01_s1. |
| 5 | REFDOC_ANALYSIS §0 item 1 and ERR-S1: the residual −¼C_Aχ²T_A·T_B is "the reference's main justification for grading DY B′ rather than B". REFDOC line 139 also ties B′ to App. E assumptions. | REFDOC table (line 1051): "B′" ↦ [A] plus a mandatory 「地位与缺口」 paragraph naming the `asm:appO-*` items. `thm:dy-factorization` [A] with a four-layer status (FINAL_OUTLINE_v2 §0.9). | Correct. The residual is an artefact of the strict truncation (N01 computation confirmed in batch_N01_s1; the result is in Meggiolaro 1997). Without it, B′ has no separate content beyond the named App. E/O assumptions. |

## 6. A27 — Sivers experimental status, twist-3 evolution, Collins 1998

* **COMPASS 2017. V-abs.** PRL 119 (2017) 112002 (APS abstract): "Within the experimental uncertainties, the observed
  sign of the Sivers asymmetry is found to be consistent with" the sign change. Keep the hedge.
* **COMPASS 2024. V-abs.** PRL 133 (2024) 071902, final 2015+2018 data: "consistent with the fundamental QCD prediction
  of a sign change of naive time-reversal-odd TMD PDFs".
* **STAR 2016. V, with a correction.** PRL 116 (2016) 132301 (1511.06003). Data from 2011, 25 pb⁻¹. "A combined fit on
  **W⁺ and W⁻** asymmetries, A_N(y_W), to the theoretical prediction in the KQ model (no TMD evolution) … gives a
  χ²/ndf = 7.4/6 assuming a sign-change … and a χ²/ndf = 19.6/6 otherwise. The current data thus favor theoretical models
  that include a change of sign … if TMD evolution effects are small." The Z⁰ sample (50 events) is not part of that fit.
  Write "STAR W± (2011 data)" for the χ² statement.
* **BPV 2021. V, with an addition.** PRL 126 (2021) 112002 (2012.05135), p. 4: "The resulting fit does exhibit tensions
  between DY and SIDIS data sets, however, the fit has χ²/N_pt = 1.0 and cannot exclude the same sign of Sivers functions
  in DY and SIDIS. The sign of the sea-quark Sivers function plays here the central role."
* **EKT 2021. V-abs.** JHEP 01 (2021) 126: "tension arises when trying to describe the spin asymmetries of W/Z bosons
  at RHIC".
* Verdict "consistent, not decisive": supported.
* **BMP 2009 vs Kang–Qiu 2009. V, with an addition.** BMP (PRD 80 (2009) 114002 [Erratum PRD 86 (2012) 119902]):
  "Our results do not agree with the recent calculations…". In the text the comparison is explicitly with Kang–Qiu
  ("Ref. [27]", PRD 79 (2009) 016003): "two terms where we disagree, and their origin could be identified". The
  disagreement was later reconciled. Kang–Qiu, PLB 713 (2012) 273 (abstract): they "identify the sources that are
  responsible for the differences, and are able to reconcile the results from various groups". See also Schäfer–Zhou PRD 85
  (2012) 117501. Print both the 2009 disagreement and its 2012 reconciliation. This also gives FINAL_OUTLINE's "resolved"
  a citation.
* **Sign mismatch. V.** Kang–Qiu–Vogelsang–Yuan, PRD 83 (2011) 094001: the k_⊥-moment of the Sivers function has
  "opposite sign from that of T_{q,F}(x,x)". JAM 2020 (Cammarota et al., PRD 102 (2020) 054002, §1): describing both
  A_SIDIS^Siv and A_N^h "further indicates a resolution to the 'sign-mismatch' puzzle". In their fit the Qiu–Sterman term
  in A_N is negligible and the Collins-type term dominant. "Addressed by" is fair; "indicates a resolution" is their own
  wording.
* **Collins 1998.** See A23 item 8 (exact quote).

## 7. A28 — NLP endpoint factorization

* **Endpoint divergences generic; MS-bar of individual functions insufficient. V-abs.** LN 2020 (JHEP 04 (2020) 033)
  abstract: endpoint-divergent convolutions "indicate an unexpected failure of dimensional regularization and the MS-bar
  subtraction scheme". BBJV 2020 (JHEP 07 (2020) 078) abstract: "Factorization holds only before the dimensional regulator
  is removed, due to a divergent convolution when the collinear and soft functions are first expanded around d = 4".
  Read "[R] (explicit examples)" as: rigorously exhibited in specific processes, not a general theorem.
* **h → γγ (b loop). V.** LN 2020 §5.2, eqs. (54)–(55): "Our explicit expression[s] … confirm that these relations
  indeed hold at NLO in α_s … these relations must hold to all orders …, and it would be desirable to derive them
  rigorously from SCET." LMNW 2021 (JHEP 01 (2021) 077), §3 "SCET derivation of the refactorization conditions". First
  condition: §3.1, eq. (3.5). Second: §3.2, eqs. (3.12)–(3.14), contour wrapped around the soft-function cut, (3.14) =
  discontinuity of S^(0), "This proves the second refactorization condition in (2.7)". §7: "We have proved two D-dimensional
  refactorization conditions". "Proven within SCET, so resting on SCET's assumptions" and [A] are correct. The claim's
  "(3.12)–(3.14)" covers only the second condition.
* **gg → h (LNSW 2023, JHEP 06 (2023) 183). V-abs.** RBS scheme, "factorization theorem free of endpoint divergences",
  three-loop α_s³lnᵏ (k = 6…3), first three towers resummed. [A].
* **Threshold DY at NLP (BBJV). V-abs** (quote above). [P] (bare, d-dimensional) is correct.
* **LL resummation, Beneke et al. 2019–2022. V-abs.** DY JHEP 03 (2019) 043; gg→H JHEP 01 (2020) 094; off-diagonal
  DIS JHEP 10 (2020) 196 (LL bootstrapped from d-dimensional consistency and the then-conjectured soft-quark Sudakov
  exponentiation, which they derive); "gluon thrust" JHEP 07 (2022) 144 ("first resummation of the endpoint-divergent
  SCET_I observables at the leading logarithmic accuracy"). [A] at LL only.
* **BSS 2026. V.** arXiv:2608.25502, v1 only (2026-08-26), no journal-ref (arXiv); INSPIRE 3196336 unpublished. §7: at
  LP the threshold PDFs coincide with the ξ → 1 limit of MS-bar PDFs and MS-bar renormalization commutes with the endpoint
  limit. At NLP the PDF becomes a two-scale object (abstract). LL resummation in d-dimensional MS-bar and in a
  refactorization "endpoint scheme". The scheme relation is "provided (to double-logarithmic accuracy) in the present
  work". NLL is announced as forthcoming. [A]† (LL) is correct.
* **Bodwin et al. V-abs.** PRD 104 (2021) 016010 (confirms the LMNW(F) conjecture for the soft-quark-function
  renormalization at O(α_s); analyticity by light-cone PT). PRD 104 (2021) 116025 (a soft-subtracted radiative jet function
  is needed; non-local renormalization). PRD 109 (2024) 056020 (gauge-invariance violations of position-space SCET
  Lagrangians, repaired by EOM terms). arXiv:2512.11647 (v3, 2026-07-03, unpublished; "hidden self-energy
  contributions"). "Scrutinize individual ingredients" is a fair summary.

## 8. Items for stage 2 and for the spec patch

1. A23-1 stays OPEN on scope (theory class of Anikin–Zav'yalov). Keep the hedge in REFS_NOTES_v2 A09 until the full text
   or Zav'yalov 1990 is read.
2. Bib fix: `Einhorn1976` title → "Confinement, form factors, and deep-inelastic scattering in two-dimensional quantum
   chromodynamics" (Crossref); pages 3451–3471. `CallanCooteGross1976`: pages 1649–1669.
3. B10 pointer: Collins 2011 ch. 8–11 (§§10.1–10.8, 11.3, 11.9).
4. A27: add Kang–Qiu PLB 713 (2012) 273 (and Schäfer–Zhou PRD 85 (2012) 117501) as the reconciliation of the
   twist-3 evolution dispute; restrict the STAR χ² sentence to W±.
5. A25: "sources of some of these differences".
6. A24-6: if the monograph keeps "[R] in that model" for the 't Hooft model (`prop:power-thooft-model`), limit it to
   leading-twist scaling. Mondejar–Pineda (PRL 101 (2008) 152002) report an OPE breakdown at NLO in 1/Q² in the same
   model. This was read at the level of their 2009 introduction only; check it before printing.
