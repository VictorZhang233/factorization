# Verification batch E25–E30 (stage 1, independent verifier)

Date: 2026-10-10. Default stance: skeptical. Claims E25–E30 of `verify/CLAIMS.md` (sources: `research/c_scet/DERIVATION.md` §6 items 15, 17;
`research/c_wilson/DERIVATION.md` §2.7, §6.2; `research/c_ee/DERIVATION.md` §6, §8, §10; `research/survey/SURVEY.md` item 11;
`research/critic/REVIEW.md` misconception 12; `spec/VERIFIED_FORMULAS.md` VF-BQ-4, VF-WL-10, VF-EE-12).

## 0. Method and sources

**Primary literature, downloaded independently** (treated as untrusted data and read as text; LaTeX sources were compiled with
`latex -no-shell-escape` in separate build directories only to get the printed equation numbers):

* BPS 2002: arXiv:hep-ph/0109045v2 (arXiv comment: "journal version" = PRD 65 (2002) 054022). The compiled labels (revtex4) give (Lcg) = **eq. (24)**,
  (Dc) = eq. (17), (Dus) = eq. (18), (Lcq) = eq. (25), (Lcgfree) = eq. (39). An independent count with my `eqcount.py` gives the same numbers.
* BBNS 2001: arXiv:hep-ph/0104110v1. This is the only arXiv version (NPB 606 (2001) 245). Compiled: (XHparam) = **eq. (71)**, (XAparam) = eq. (72),
  (ai) = eq. (46), (Xdef) = eq. (59).
* BN 2003: arXiv:hep-ph/0308039v2 (comment: "typos and errors in data tables corrected; version to appear in Nuclear Physics B"; NPB 675 (2003) 333).
  Compiled: (XHparam) = **eq. (63)**, (fact) = eq. (2); the unlabelled a_i^p(M_1M_2) formula is **eq. (35)** (I added a label in a copy and compiled).
  The Elsevier journal pages of both papers returned HTTP 403, so **the journal typesetting was not seen**.
* Collins, *Foundations of Perturbative QCD*. Open-access reissue (Cambridge 2023, doi:10.1017/9781009401845; per the author's errata its content
  is that of the November 2013 paperback). I downloaded the chapter PDFs for chs. 2, 3, 4, 7, 11 and 13 from Cambridge Core and rendered
  p. 43 (Fig. 3.1), p. 236 (Fig. 7.10) and p. 402 (eqs. (11.4)–(11.6)) as images.
* Collins's errata list. The current version is "Errata and updates for 'Foundations of Perturbative QCD'", John Collins, dated 22 May 2026, 10 pp.,
  https://www.cantab.net/users/johncollins/qcdbook/qcd-errata.pdf. It is linked from https://www.cantab.net/users/johncollins/qcdbook/ (the old
  psu.edu pages now redirect there). Its Sec. 3 is "Corrections and updates relative to published paperback edition of November 2013", with the running
  head "CORRECTIONS AND UPDATES TO NOV. 2013 PRINTING". Wayback copies dated 2012-07-12 and 2013-06-26 do **not** yet contain the Fig. 7.10 or
  (11.4)–(11.6) items.
* Sterman–Weinberg, PRL 39 (1977) 1436. The APS full text returned HTTP 403, and Semantic Scholar lists it as closed access, so **the original text
  was not read**. Secondary sources read instead:
  * Nandi & Wada, preprint COO-1545-255 (OSTI 6091728; published as PRD 21 (1980) 76). Page 9 was rendered.
  * Chay & Ellis, arXiv:hep-ph/9607464 (= PRD 55 (1997) 2728), source.
  * Ali & Kramer, arXiv:1012.2288 (= EPJ H 36 (2011) 245), source.
  * Stagnitto, arXiv:2508.14700, source.
  * Sterman, TASI lectures hep-ph/9606312 and hep-ph/0412013, sources.
* E29: INSPIRE records and abstracts of Gorishny–Kataev–Larin PLB 212 (1988) 238, Gorishny–Kataev–Larin PLB 259 (1991) 144, and
  Surguladze–Samuel PRL 66 (1991) 560 [Erratum ibid. 2416]. LaTeX sources of Chetyrkin–Kühn–Kwiatkowski, Phys. Rept. 277 (1996) 189
  (hep-ph/9503396), Baikov–Chetyrkin–Kühn PRL 101 (2008) 012002 (0801.1821), and Baikov–Chetyrkin–Kühn–Rittinger PLB 714 (2012) 62 (1206.1288).
* E30: LaTeX sources of the following, plus Collins 2011 ch. 13, §13.17.
  * Collins hep-ph/0204004 (= PLB 536 (2002) 43). Compiled: eqs. (1)–(4).
  * Collins hep-ph/9208213v2 (= NPB 396 (1993) 161). Its header says "Add appendix on time-reversal argument, as in journal".
  * Brodsky–Hwang–Schmidt hep-ph/0201296 (= PLB 530 (2002) 99).
  * Boer–Mulders–Pijlman hep-ph/0303034 (= NPB 667 (2003) 201).

**My own scripts** are in `verify/claims/batch_E25_s1_scripts/` (run with `python3 -I`); outputs are saved as `*.out.txt`:
`eqcount.py`, `e25_ghost_gauge.py`, `e28_sw_independent.py`, `e29_r3_check.py`, `e30_pt_signs.py`.
I also re-ran two project scripts from scratch copies: `research/c_ee/sw_jets.py` (**6/6 PASS**, log `sw_jets_rerun.log`) and
`research/c_tmd/scripts/sivers_symmetry.py` with its dependency `sivers_spectator.py` (**PASS**, log `sivers_symmetry_rerun.log`).

## 1. Summary

| id | verdict | what must change before printing | already in the literature? |
|---|---|---|---|
| E25 | **confirmed** | Gauge-fixing and ghost terms are each usoft invariant; only their **sum** is BRST invariant. Cite BPS eq. (24) and the text after it. | No published correction found. The facts are standard background-field/BRST properties. |
| E26 | **confirmed** (arXiv versions) | BN 2003's misprinted sentence is about **X_A** (eq. (63), "and similarly for X_H"), not X_H. Give the locations: BBNS after eq. (71), BN after eq. (63). The notation remark is a caution, not an erratum: both papers label V by the emitted meson. | No erratum listed on INSPIRE. Journal typesetting not checked. |
| E27 | **confirmed** | Fig. 7.10: the errata reverse the sign of the **gluon**-pdf vertex to the right of the cut (g_0 n^μ f_{kαj} → −g_0 n^μ f_{kαj}). The quark-pdf vertices −ig_0n^μt_α (left) and +ig_0n^μt_α (right) were printed correctly and are unchanged. | Yes, in the author's errata list (Sec. 3). The sign convention of g is stated in the book itself. |
| E28 | **confirmed** as physics; **not an erratum of SW** | The ln 2ε form with ε a fraction of the total energy is SW's own result, as quoted by three secondary sources. I found no printed full O(α_s) formula that writes ln ε with total-energy ε, so "common form" is unsubstantiated. Print it as a convention remark, not as an erratum. | Yes: Nandi–Wada 1979/80, Chay–Ellis 1997 eq. (11), Ali–Kramer 2011. |
| E29 | **confirmed** | None. The singlet term is (Σe_q)²(55/72 − 5ζ₃/3)a³ = 3Σe_q²·η·(−1.2395)a³. | Yes: GKL 1991, SS 1991 (+ erratum), CKK 1996, BCK 2008, BCKR 2012. |
| E30 | **confirmed** | Collins 2002 writes the sign reversal explicitly only for f_1T^⊥ (eq. (3)). For h_1^⊥ it says only that the T argument fails, so the function is allowed. The explicit "h_1^⊥ reverses sign" is in Collins 2011 §13.17.2 and Boer–Mulders–Pijlman 2003. Both attribute the sign change to Collins 2002. | Yes: Collins 2002; Collins 2011 eq. (13.124), §13.17.2; BMP 2003. |

---

## 2. E25 — BPS 2002: the ghost term is not collinear-gauge invariant

**Published text** (arXiv:hep-ph/0109045v2 = journal version; eq. (24) = label `Lcg`):

$$\mathcal L_c^{(g)}=\frac1{2g^2}{\rm tr}\Big\{\big[i\mathcal D^\mu+gA_{n,q}^\mu,\,i\mathcal D^\nu+gA_{n,q'}^\nu\big]\Big\}^2
+2\,{\rm tr}\Big\{\bar c_{n,p'}\big[i\mathcal D_\mu,\big[i\mathcal D^\mu+gA^\mu_{n,q},c_{n,p}\big]\big]\Big\}
+\frac1\alpha{\rm tr}\Big\{[i\mathcal D_\mu,A^\mu_{n,q}]\Big\}^2 ,\qquad(24)$$

with $i\mathcal D^\mu\equiv\frac{n^\mu}2\bar{\mathcal P}+\mathcal P_\perp^\mu+\frac{\bar n^\mu}2in\!\cdot\!D$ (eq. (17)) and $iD^\mu=i\partial^\mu+gA^\mu_{us}$ (eq. (18)).
The text directly after eq. (24) reads:
> "The first two terms in Eq. (24) are invariant under collinear gauge transformations, while the last is the gauge fixing term with parameter α.
> Furthermore, the complete collinear Lagrangian is invariant under usoft gauge transformations, including the 1/α gauge fixing term. This complies
> with the notion of the usoft gluon as a background field."

The "first two terms" are the field-strength term and the ghost term. In the LaTeX source the ghost rows of Table I (collinear:
$c\to\mathcal U_Q c\,\mathcal U^\dagger$; usoft: $V_{us}cV_{us}^\dagger$) are commented out, so the printed table gives no ghost transformation at all. The decoupling
section uses $c_{n,p}=Yc^{(0)}_{n,p}Y^\dagger$ and $i\mathcal D+gA=Y(i\mathcal D_{(0)}+gA^{(0)})Y^\dagger$ (text after eq. (39)).

**Analytic check.** Let $\Pi^\mu=i\mathcal D^\mu+gA^\mu$. Under a collinear transformation (Table I) $\Pi^\mu\to U\Pi^\mu U^\dagger$, while $i\mathcal D^\mu$ is unchanged.
Infinitesimally, with $U=1+i\omega$, $\delta A^\mu=-\frac ig[\Pi^\mu,\omega]$.

* *Ghosts in the adjoint* (the commented-out row). By the Jacobi identity and cyclicity,
  $\delta\mathcal L_{gh}=2\,{\rm tr}\big(\bar c\,[[i\mathcal D_\mu,i\omega],[\Pi^\mu,c]]\big)$, with $[i\mathcal D_\mu,i\omega]=-\partial_\mu\omega+ig[B_\mu,\omega]$.
  This is $O(\lambda^0)$ in SCET counting, because ω carries collinear label momenta.
* *Ghosts inert.* Then $\delta\mathcal L_{gh}=2\,{\rm tr}\big(\bar c\,[i\mathcal D_\mu,[[i\omega,\Pi^\mu],c]]\big)$.

In both cases $\delta\mathcal L_{gh}$ is linear in $\bar c$ with no derivative acting on $\bar c$. Invariance of the action for all $\bar c$ would therefore require its
coefficient to vanish identically, and it does not. Already for $A=B=0$ the coefficient is $\propto[\partial_\mu\omega,\partial^\mu c]$, which is nonzero for a
non-abelian group. So the ghost term is not collinear-gauge invariant under either assignment. This is what one expects: the ghost operator is the
Faddeev–Popov operator of the gauge-fixing function $G=[i\mathcal D_\mu,A^\mu]$, and that function is designed to break exactly the collinear invariance.

* The field-strength term is invariant because $[\Pi^\mu,\Pi^\nu]\to U[\Pi^\mu,\Pi^\nu]U^\dagger$.
* Under a usoft transformation, $i\mathcal D\to Vi\mathcal D V^\dagger$ (V depends only on the multipole coordinate), $A\to VAV^\dagger$ and $c,\bar c\to V(\cdot)V^\dagger$.
  All three terms transform by conjugation, so their traces are invariant.
* BRST: take $sA^\mu=-\frac ig[\Pi^\mu,c]$ and $sc=icc$, so that $s^2A=0$ (by the derivation $s[\Pi,c]=[\Pi,sc-icc]$), and $s\bar c=\lambda G$.
  Then $\mathcal L_{gh}=2ig\,{\rm tr}(\bar c\,sG)$ and
  $s(\mathcal L_{gf}+\mathcal L_{gh})=(\tfrac2\alpha+2ig\lambda){\rm tr}(G\,sG)-2ig\,{\rm tr}(\bar c\,s^2G)$, which vanishes for $\lambda=\frac{i}{\alpha g}$.
  Each term alone is not invariant, and $s\mathcal L_F=0$.

**Numerical check** (`e25_ghost_gauge.py`). I use a continuum representation of the LO SCET structure: label and residual derivatives are combined into
full derivatives on the collinear fields, and the usoft field enters only as $B^\mu=\frac{\bar n^\mu}2 b$ with $b=n\!\cdot\!A_{us}$ depending on $\bar n\!\cdot\!x$ only, so that
$\bar n\!\cdot\!\partial b=\partial_\perp b=0$. The setup is SU(2) with random quadratic fields, an explicit Grassmann algebra for $c,\bar c$ and the BRST parameter, and
exact degree-2 jets. Results for three random trials (all as expected; nonzero entries are O(1–60) against Lagrangian terms of size 40–85, zeros are below 1e-12):

| quantity | result |
|---|---|
| collinear δL_F | 0 |
| collinear δL_gh (ghosts adjoint) | **nonzero** (11, 16, 38) |
| collinear δL_gh (ghosts inert) | **nonzero** (15, 25, 59) |
| collinear δL_gh with A = B = 0 | **nonzero** (3.8, 16, 4.2) |
| collinear δL_gf | nonzero |
| usoft δL_F, δL_gh, δL_gf | 0, 0, 0 |
| BRST s L_F | 0 |
| BRST s L_gf alone, s L_gh alone | nonzero, equal and opposite |
| BRST s(L_gf + L_gh) | **0** |
| s²A = 0 with sc = icc; negative control sc = −icc | 0; nonzero |

**Verdict: confirmed.** One precision point: "gauge-fixing and ghost terms are … BRST invariant" must be read as "their **sum** is BRST invariant (each alone is
not); the whole $\mathcal L_c^{(g)}$ is BRST invariant". Usoft covariance (invariance with $c,\bar c\to V_{us}cV_{us}^\dagger$) holds term by term. That is what the
decoupling proof uses, and BPS themselves stress that "the derivative in the 1/α gauge fixing term … is covariant with respect to the usoft $n\cdot A_{us}$ background
field". **Literature:** INSPIRE lists no erratum for PRD 65 054022. I found no published correction of this sentence; BFPRS 2002 (hep-ph/0202088) and
Becher–Broggio–Ferroglia 2015 (arXiv:1410.1892) do not repeat it.

---

## 3. E26 — BBNS 2001 / BN 2003: "m_M" must read m_B

**BBNS 2001** (hep-ph/0104110v1):
> eq. (71): $X_H=(1+\varrho_He^{i\varphi_H})\ln\frac{m_B}{\Lambda_h};\ \varrho_H\le1$ — "with an arbitrary phase φ_H, which may be caused by soft rescattering. In other words,
> we assign a 100% uncertainty to the ``default value'' $X_H=\ln(m_M/\Lambda_h)\approx2.4$."

The same paper elsewhere has the correct form: "(using central values for all input parameters and setting $X_H=\ln(m_B/\Lambda_h)\approx 2.4$)"; after eq. (72),
"default value $X_A=\ln(m_B/\Lambda_h)$"; and "fixed at the default value $X_H=X_A=\ln(m_B/\Lambda_h)$". It also states $\Lambda_h=0.5$ GeV ("$\mu_h=\sqrt{\Lambda_h\mu}$ with
$\Lambda_h=0.5$ GeV").

**BN 2003** (hep-ph/0308039v2):
> eq. (63): $X_A=(1+\varrho_Ae^{i\varphi_A})\ln\frac{m_B}{\Lambda_h};\ \varrho_A\le1,\ \Lambda_h=0.5$ GeV, "and similarly for $X_H$. Here φ_A is an arbitrary strong-interaction
> phase … In other words, we assign a 100% uncertainty to the ``default value'' $X_A=\ln(m_M/\Lambda_h)\approx2.4$."

The default value can only be $\ln(m_B/\Lambda_h)$: $\ln(5.279/0.5)=2.357\approx2.4$, whereas any light-meson mass gives a negative or zero logarithm
($\ln(m_\pi/0.5)=-1.27$, $\ln(m_K/0.5)\approx-0.01$). So $m_M\to m_B$ in both sentences. **Correction to the claim:** in BN 2003 the misprinted sentence concerns
$X_A$ (with $X_H$ treated "similarly"), not $X_H$.

**Notation part.** BN 2003, text after eq. (2): "Whenever the spectator antiquark line goes from the $\bar B$ meson to one of the final-state mesons we call this meson
$M_1$ and the other one $M_2$." Eq. (35) reads
$a_i^p(M_1M_2)=(C_i+\frac{C_{i\pm1}}{N_c})N_i(M_2)+\frac{C_{i\pm1}}{N_c}\frac{C_F\alpha_s}{4\pi}[V_i(M_2)+\frac{4\pi^2}{N_c}H_i(M_1M_2)]+P_i^p(M_2)$, so V refers to the emitted
meson $M_2$. BBNS 2001 eq. (46) is πK-specific:
* $a_{1,I},a_{4,I},a_{10,I}$ carry $V_K$ and $H_{K\pi}$;
* $a_{2,I},a_{3,I},a_{9,I}$ carry $V_\pi$ and $H_{\pi K}$;
* $a_{5},a_{7}$ carry $-V'_\pi$;
* BBNS's own notation is $H_{M_2M_1}$, i.e. the emitted meson first.

The two papers are consistent: both label V by the emitted meson. The remark is a transcription caution, not an erratum.

**Verdict: confirmed (typo; arXiv versions).** BBNS v1 is the only arXiv version. BN v2 is the "version to appear in NPB", and the misprint survived its typo pass.
The Elsevier typesetting could not be checked. INSPIRE lists no erratum for either paper.

---

## 4. E27 — Collins 2011: errata to Fig. 7.10 and eqs. (11.4)–(11.6); sign of g

**Errata list** (22 May 2026 version, Sec. 3, which "appl[ies] to both editions"):
> "In Fig. 7.10, there should be a reversal of the sign of the Feynman rule for the gluon-to-Wilson-line coupling to the right of the final-state cut in the gluon pdf.
> That is, Fig. 7.10 should be modified to:" — Quark pdf, bare fields: $-ig_0n^\mu(t_\alpha)_{kj}$ | $ig_0n^\mu(t_\alpha)_{kj}$; renorm.: $-ig_0Z_3^{1/2}n^\mu(t_\alpha)_{kj}$ |
> $ig_0Z_3^{1/2}n^\mu(t_\alpha)_{kj}$; Gluon pdf, bare: $g_0n^\mu f_{k\alpha j}$ | $-g_0n^\mu f_{k\alpha j}$; renorm.: $g_0Z_3^{1/2}n^\mu f_{k\alpha j}$ | $-g_0Z_3^{1/2}n^\mu f_{k\alpha j}$.
>
> "P. 402: In Eqs. (11.4)–(11.6), subscript Lorentz indices should be replace[d] by superscripts, and vice versa", giving
> $H\cdot C=H^{\mu_1\ldots\mu_N}\prod_jg_{\mu_j\nu_j}C^{\nu_1\ldots\nu_N}$ (11.4); $g_{\mu_j\nu_j}=K_{\mu_j\nu_j}+G_{\mu_j\nu_j}$ (11.5);
> $K_{\mu_j\nu_j}=\frac{k_{j\mu_j}w_{2\nu_j}}{k_j\cdot w_2-i0}$, $G_{\mu_j\nu_j}=g_{\mu_j\nu_j}-\frac{k_{j\mu_j}w_{2\nu_j}}{k_j\cdot w_2-i0}$ (11.6), "$k_j$ … the momentum of gluon $j$ flowing into $H$",
> "$w_2$ projects onto plus components of momentum: $w_2=(0,1,0_T)$".

**Printed book** (OA reissue = Nov. 2013 content, rendered pages):
* Fig. 7.10, p. 236. Quark pdf: $-ig_0n^\mu(t_\alpha)_{kj}$ (left) and $ig_0n^\mu(t_\alpha)_{kj}$ (right). Gluon pdf: $g_0n^\mu f_{k\alpha j}$ on **both** sides; the caption gives
  $(T_\alpha)_{kj}=if_{k\alpha j}$.
* p. 402: $H\cdot C=H_{\mu_1\ldots\mu_N}\prod g^{\mu_j\nu_j}C_{\nu_1\ldots\nu_N}$ and $K^{\mu_j\nu_j}=k_j^{\mu_j}w_2^{\nu_j}/(k_j\cdot w_2-i0)$, inconsistent with the following sentence
  "the largest term … has $\mu_j=-,\ \nu_j=+$".

The corrected entries are consistent. With $(T_\alpha)_{kj}=if_{k\alpha j}$, the quark pattern $\mp ig_0n^\mu T_\alpha$ gives $g_0n^\mu f_{k\alpha j}$ on the left and $-g_0n^\mu f_{k\alpha j}$ on the
right, as hermitian conjugation on the conjugate side requires.

**Sign of g.** Collins eq. (2.2) is $D_\mu\psi_0=(\partial_\mu+ig_0t^\alpha A^\alpha_{(0)\mu})\psi_0$ and eq. (2.3) is $G=\partial A-\partial A-g_0fAA$. Eq. (3.14) has $\mathcal L_{b.i.}=-g\mu^\epsilon\bar\psi t^\alpha\slashed A^\alpha\psi+\dots$, and
Fig. 3.1 (p. 43) gives the quark–gluon vertex $-ig\mu^\epsilon(t^\alpha)_{ab}\gamma^\mu$. Against Peskin–Schroeder's $+ig\gamma^\mu t^a$ (with $D=\partial-igA$), this means
$g_{\rm Collins}=-g$. Consistently, eq. (13.40) reads $W(x;\infty,n)=P\,e^{-ig_0\int_0^\infty d\lambda\,n\cdot A(x+\lambda n)}$, and the caption of Fig. 7.10 says the vertex sign "corresponds to the
sign of the coupling in our Lagrangian, whose Feynman rules are in Fig. 3.1".

**i0 and orientation.** With $k$ flowing into $H$, an attachment to the outgoing struck quark gives $1/[(p_f-k)^2+i0]\propto1/(k^+-i0)$. This is the $-i0$ of the
future-pointing eikonal line ($-i/(n\cdot K-i0)$; c_wilson §2.3). It is consistent with Collins (7.51), whose Wilson line on the left of the cut has $i/(k^++\dots+i0)$ for momenta
directed **into** the bubble, i.e. out of a future-pointing line.

**Verdict: confirmed, with one precision fix.** The claim describes the corrected Fig. 7.10 only through its quark entries. The erratum actually changes the **gluon-pdf**
vertex to the right of the cut; the quark entries were already correct. Everything else checks out: the index interchange, $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-i0)$, DIS
future-pointing, $D=\partial+igA$ (eq. (2.2)) and $g_{\rm Collins}=-g$. The c_wilson table row ("quark pdf … as corrected in his errata") is correct in content but
should not suggest that the quark rules were corrected.

---

## 5. E28 — Sterman–Weinberg: ln 2ε versus ln ε

**Definition and SW's own form (secondary sources; SW's text inaccessible):**
* Nandi & Wada (COO-1545-255 = PRD 21 (1980) 76), p. 3: "Following Ref. 1 [SW], we consider the 2-jet cross section σ(E,θ,ε,δ) defined as the cross section for all
  e+e− annihilation events in which (1 − ε) fraction of the total e+e− energy E is emitted in a pair of oppositely directed cones of opening angle 2δ."
  Their p. 9 (rendered), eq. (23):
  $\frac{d\sigma^{2\text{-jet}}}{d\cos\theta}=\sigma_0\frac38[1-\frac{4\alpha_s}{3\pi}\{(3+4\ln2\epsilon)\ln\delta+\frac{\pi^2}3-\frac52\}](1+\cos^2\theta)$, followed by "We note that this is in
  agreement with the expression (6) in Ref. 1." Their footnote 7 records a private communication with Weinberg.
* Chay & Ellis (PRD 55 (1997) 2728), eq. (11): "a fraction (1−ε) of the total energy …":
  $\frac{d\sigma}{d\Omega}=(\frac{d\sigma}{d\Omega})_B[1-\frac{4\alpha_s}{3\pi}\{(3+4\ln2\epsilon)\ln\delta+\frac{\pi^2}3-\frac52\}+O(\epsilon,\delta)]$.
* Ali & Kramer (EPJ H 36 (2011) 245): "having all but a fraction ε of the total c.m. energy",
  $\sigma_{2\text{-jet}}=\sigma_0[1+C_F\frac{\alpha_s}\pi(-4\ln2\epsilon\ln\delta-3\ln\delta-\frac{\pi^2}3+\frac52+O(\epsilon)+O(\delta))]$.

All three agree: SW's own result has $\ln 2\epsilon$ with ε a fraction of the **total** energy, so **SW 1977 is not in error**.
Double-log versions with $\ln(1/\epsilon)$ (Stagnitto arXiv:2508.14700 eq. (SWxs2jet); Ali–Kramer's LL formula) are correct at their stated accuracy.
I did **not** find a printed full $O(\alpha_s)$ bracket with "$4\ln\delta\ln\epsilon$" and total-energy ε. The "4 ln δ ln ε" in c_ee §8/§10 refers to "the form quoted in the task",
i.e. our own outline.

**Independent numerics** (`e28_sw_independent.py`, written from scratch). The setup:
* Two-jet condition: (a) some $\theta_{ij}\le2\delta$, or (b) some $x_k\le2\epsilon$ together with $\pi-\theta_{ij}\le2\delta$ for the other pair. I re-derived this
  from the cone geometry: $-\hat p_k$ lies on the arc between $\hat p_i$ and $\hat p_j$, and two partons outside the cones are impossible.
* Variables $a=y_{13}$, $b=y_{23}$. All boundaries are linear or quadratic in $b$, so the $b$-integral is done analytically between breakpoints.
* The $a$-integral uses adaptive QUADPACK in $\ln a$. The panel edges must include the integrand jumps at $a=2\epsilon$ and $a=1-2\epsilon$; without them QUADPACK
  misses the jump and errs by about 1e-3.
* A Monte Carlo cross-check of the region logic at (0.05, 0.25) gives 20.155 ± 0.12 against 20.149.

Quantity tabulated: $c_{2j}=(\sigma_{2j}/\sigma_0-1)/(C_F\alpha_s/\pi)=\frac34-\frac12I_{3j}$.

| (ε, δ) | numeric | ln 2ε form | ln ε form |
|---|---|---|---|
| (1e-2, 0.1) | −29.92160 | −29.91318 | −36.297 |
| (1e-3, 0.03) | −77.44117 | −77.43773 | −87.160 |
| (1e-4, 0.01) | −143.86726 | −143.86685 | −156.635 |
| (1e-5, 0.005) | −214.20123 | −214.20139 | −228.891 |
| **(1e-6, 0.003)** | **−288.281051** | **−288.281180** | **−304.3875** |

The (1e-6, 0.003) numeric value is stable to 1e-8 under panel changes. My $I_{3j}$ values agree to 10 digits with the re-run project script, which uses
different variables, $(x_3,v)$: 289.2345205689, 374.0616812118, 578.0621017028. Rounded, the claimed numbers are reproduced: −288.2811, −288.2812, −304.39.
The two forms differ by exactly $4\ln2\,|\ln\delta|=16.1064$ at δ = 0.003. The residual $1.3\times10^{-4}$ is consistent with $O(\epsilon\ln d,\,d\ln\epsilon)$.

**Verdict: confirmed as a physics statement**: the ln 2ε formula with total-energy ε, the beam-energy rewriting, the size of the error, and the numbers.
It is **not an erratum of Sterman–Weinberg**, and the "common form" is unsubstantiated. It should be printed as a convention remark, which is what VF-EE-12
already does, unless a printed source of the wrong full formula is cited.

---

## 6. E29 — GKL 1988 O(α_s³) R-ratio, later corrected

* GKL, PLB 212 (1988) 238, INSPIRE abstract: "The obtained correction is large. For example at √s ≃ 34 GeV in the MS scheme it is about 2.5 times larger than the previous
  O(α_s²) term."
* Surguladze–Samuel, PRL 66 (1991) 560 [Erratum ibid. 2416; INSPIRE lists the erratum], abstract: "The result differs from a previous calculation and is much smaller."
* GKL, PLB 259 (1991) 144, abstract: "total analytical reevaluation … for five active flavors … $R(s)=\frac{11}3[1+\alpha_s/\pi+1.409(\alpha_s/\pi)^2-12.805(\alpha_s/\pi)^3]$."
* Chetyrkin–Kühn–Kwiatkowski, Phys. Rept. 277 (1996) 189, Sec. "Massless limit": "The initial calculation of the O(α_s³) term described in [GKL 1988] was later corrected by
  two groups [GKL 1991, Surguladze–Samuel 1991]". Their eq. (ns1) gives the analytic non-singlet coefficient and eq. (ns2) gives "−6.6369 − 1.2001 n_f − 0.0052 n_f²"
  (source comment: −6.63693554 − 1.200134058 n_f − 0.00517835519 n_f²).
  Their singlet term is $R_{11}=(\sum_fv_f)^2(\alpha_s/\pi)^3(-1.2395)$, with $r^V_S=\frac13(\frac{\alpha_s}{4\pi})^3(\frac{d_{abc}}4)^2[\frac{176}3-128\zeta_3]$.
* BCK 2008, eq. (R_numerical_nl): $(-6.63694-1.20013n_f-0.00518n_f^2)a_s^3$ (non-singlet).
* BCKR 2012, eq. (Rqcd): $+(\sum_fq_f)^2\{a_s^3(\frac{55}{72}-\frac53\zeta_3)+\dots\}$; numerically $-(\sum q_f)^2\,1.2395\,a_s^3$.

**My check** (`e29_r3_check.py`, sympy):
* From CKK (ns1): $r_3^{NS}=-6.636936-1.200134n_f-0.005178n_f^2$.
* The $\pi^2$ part equals $-\frac{\pi^2}3b_0^2$ with $b_0=(11-\frac23n_f)/4$; the Adler coefficient is $d_3=18.2427-4.2158n_f+0.0862n_f^2$.
* $\frac{55}{72}-\frac53\zeta_3=-1.239539$. This equals $d_R\cdot\frac{d^{abc}d^{abc}}{d_R}(\frac{11}{192}-\frac{\zeta_3}8)$ with $d^{abc}d^{abc}=40/3$, and also equals CKK's
  normalization (exact symbolic equality).
* With $\eta=(\sum e_q)^2/(3\sum e_q^2)$ (= 0, 2/15, 1/33 for $n_f$ = 3, 4, 5), the total $a^3$ coefficients are −10.2839, −11.6856, **−12.8046**. GKL 1991 gives −12.805 for
  $n_f=5$; BCKR give −11.686 for $n_f=4$.
* Normalization: $3\sum e_q^2\cdot\eta\cdot c=(\sum e_q)^2c$, so $c=55/72-5\zeta_3/3$ is correct as the coefficient of η.

**Verdict: confirmed.** The "recalled; verify" status can be dropped. Cite GKL 1991, Surguladze–Samuel 1991 (+ erratum), and CKK 1996 for the history.

---

## 7. E30 — Collins 1993 T-odd argument invalidated by the Wilson line (Collins 2002, after BHS 2002)

* **Collins 1993** (hep-ph/9208213v2 = NPB 396 (1993) 161, appendix "as in journal"): "Sivers suggested … However, as we will now show, such an asymmetry is prohibited because
  QCD is time-reversal invariant." The PT argument on the operator without a Wilson line concludes $\hat f(LR)=\hat f(RL)=0$, which "contradicts Sivers' suggestion". The
  main text notes that the gauge-invariance subtleties (the path-ordered exponential) were ignored.
* **BHS 2002** (PLB 530 (2002) 99), abstract: "final-state interactions from gluon exchange between the outgoing quark and the target spectator system lead to single-spin
  asymmetries in deep inelastic lepton-proton scattering at leading twist".
* **Collins 2002** (PLB 536 (2002) 43). The abstract opens "Recently, Brodsky, Hwang and Schmidt have proposed a new mechanism …" and continues "An earlier proof that the Sivers
  asymmetry vanishes because of time-reversal invariance is invalidated by the path-ordered exponential of the gluon field in the operator definition of parton densities.
  Instead, the time-reversal argument shows that the Sivers asymmetry is reversed in sign in hadron-induced hard processes (e.g., Drell-Yan)".
  * Eq. (2): $P(x,k_T,s_T,\zeta)|_{\rm future\ W}=P(x,k_T,-s_T,\zeta)|_{\rm past\ W}$.
  * Eq. (3): $f^\perp_{1T}(x,k_T,\zeta)|_{\rm DIS}=-f^\perp_{1T}(x,k_T,\zeta)|_{\rm DY}$.
  * Sec. "Unpolarized Drell-Yan": "The failure of the time-reversal argument applies to more than the Sivers asymmetry. There is also the possibility of a nonzero transversity
    of a quark in an unpolarized hadron … $h_1^\perp$". It is defined in eq. (4) with past-pointing lines. **No explicit sign-reversal equation is given for $h_1^\perp$.**
* **Collins 2011** §13.17: "there is a change of sign between SIDIS and DY (Collins, 2002) for the T-odd functions, i.e., for the Sivers and Boer-Mulders functions". Eq. (13.124)
  is $f^\perp_{1T,\rm SIDIS}=-f^\perp_{1T,\rm DY}$, and §13.17.2 says the Boer–Mulders function "therefore also reverses sign between SIDIS and Drell-Yan".
  **BMP 2003** (NPB 667 (2003) 201): $f_{1T}^\perp$ and $h_1^\perp$ are T-odd, and "they appear with different signs in SIDIS and DY [Collins-02]".

**Checks.**
* Re-run of `sivers_symmetry.py`: PASS. Its ingredients are the PT Dirac identities, PT flipping S at fixed P, the b-space form, and the spectator model with
  ratio DY/SIDIS = −1.000000 at three points, matching Bacchetta–Conti–Radici with $e_qe_s=-e_c^2$.
* My own `e30_pt_signs.py` (Weyl representation, $P_T$ solved from $P_T^{-1}\gamma^{\mu*}P_T=\gamma^\mu$): PT sign +1 for $\gamma^+$, −1 for $\gamma^+\gamma_5$ and for
  $\gamma^+\gamma^j\gamma_5$, so $h_1^\perp$ is PT-odd. The eikonal phase gives $\int{\rm Im}\frac1{l-i0}f=+\pi f(0)$ and $\int{\rm Im}\frac1{l+i0}f=-\pi f(0)$.

**Verdict: confirmed.** "Likewise $h_1^\perp$" is correct physics, but Collins 2002 only implies it; cite Collins 2011 §13.17.2 and BMP 2003 for the explicit statement.
The relations hold given TMD factorization with future-pointing staples (SIDIS) and past-pointing staples (DY). They are an [R] consequence of PT invariance and the
operator definitions.

---

## 8. Files

* `verify/claims/batch_E25_s1_scripts/eqcount.py`: equation counter used to cross-check compiled equation numbers. It drops macro-definition lines; a label on a
  `\nonumber` eqnarray row takes the next printed number.
* `e25_ghost_gauge.py` / `.out.txt`: E25 gauge and BRST checks (3 trials, ALL PASS).
* `e28_sw_independent.py` / `.out.txt`: E28 Sterman–Weinberg numerics (the adaptive pass at the end is the authoritative one).
* `e29_r3_check.py` / `.out.txt`: E29 coefficients.
* `e30_pt_signs.py` / `.out.txt`: E30 PT signs.
* `sw_jets_rerun.log`, `sivers_symmetry_rerun.log`: re-runs of the project scripts.
