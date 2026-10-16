# VERIFIED_FORMULAS_v2 — formulas verified for the monograph (spec v2)

The monograph is 《QCD 因子化定理：严格证明、全阶论证与适用边界》. This file was assembled on 2026-10-10 by the spec-v2 writer-spec/figures/bibliography drafter (current revision **v2.1**, same day: VF-EXC-14, VF-FRO-17, pending register keyed to `verify/CLAIMS.md` — see CHANGELOG). It **supersedes** `spec/VERIFIED_FORMULAS.md` (v1): it contains every v1 entry (IDs unchanged), the group **VF-REF** of the reference-document analysis (refdoc S54), the new group **VF-QCD** for Ch2, and the frontier groups **VF-LAM** (Ch22), **VF-YZL** (Ch23) and **VF-FRO** (Ch24 and others).

## How to use this file

**Writers copy formulas from this file.** Each entry gives the exact LaTeX in the binding conventions (`CONTEXT.md`, completed by `WRITER_SPEC_v2.md` §3), its verification status, the path of the source that verified it, and the labels that use it. The IDs `VF-<GROUP>-<n>` are cited in FINAL_OUTLINE_v2 and in the figure captions of FIGURES_INDEX_v2.

**If a formula you need is not here:** derive it yourself, mark it "writer-derived" in your final report, and list the check you made (limit, sum rule, numerical test, script). Never copy a formula from memory or from a paper with different conventions without converting it and saying so (WRITER_SPEC_v2 §6.4; the known traps are rows 4, 8, 30, 31, 40, 42, 44, 45 of the notation table).

**Status codes**

| code | meaning |
|---|---|
| **V** | derived and checked with scripts (exact algebra or high-precision numerics) in the binding conventions, by a research agent, a frontier agent, a refdoc reader or the spec-v2 drafter (the script is named) |
| **VL** | as V, and also compared with the literature value after an explicit conversion (the source was read) |
| **A** | re-derived by hand (architect, spec audit, refdoc synthesizer or spec-v2 drafter) and consistent with the agents where they overlap, but not script-checked |
| **C** | general-group or general form recalled; only a special case or a consistency relation is verified |
| **TR** | (new in v2) transcribed from a source that a frontier agent read in full (rendered page checked) and converted to the binding conventions; no independent derivation or script check. A writer may quote it as the source's result with the citation; if it is used as a step of a derivation in our text, re-derive it or hedge it 「（据原文，待核实）」 |
| **T** | to verify — preliminary, recalled, or convention-dependent. Re-derive or cross-check it, and mark it in the text if the check cannot be completed |

**Flag (retired in v2.3).** Revision v2.2 appended a pending flag to the status of entries that supported a claimed literature erratum, a candidate 「本书新结果」, or an App M/N/O statement affected by the proof extensions X1–X3. The verify patch v2.3 (2026-10-11) resolved every flag: the outcome is now written in the status of each such entry and in the register at the end of this file (a record of outcomes). Entries whose claim was refuted were corrected (VF-LAM-9, VF-REF-12) or are marked "not printed".

**Source abbreviations**
- `c_x §k` = `research/c_x/DERIVATION.md` §k; logs in `research/c_x/logs/`.
- `critic cN` = `research/critic/REVIEW.md` §10 (scripts in `research/critic/checks/`); `BP` = `research/architect/BLUEPRINT.md`.
- `R1`…`R8` = `refdoc/notes/R*.md` with scripts in `refdoc/work_R*/`; `SYN` = `refdoc/work_SYN/`.
- `LAMET sN` = `frontier/lamet/scripts/sN_*.py` (logs `frontier/lamet/logs/`, 190/190 pass); `LAMET §k` = `frontier/lamet/LAMET.md` §k.
- `YZLIU <script>` = `frontier/yzliu/scripts/<script>.py`; `YZLIU §k` = `frontier/yzliu/YZLIU.md`.
- `OTHERS sN` = `frontier/others/scripts/sN_*.py` (36/36 pass); `OTHERS §k` = `frontier/others/OTHERS.md`.
- `v2-check Qn` = `spec_v2/checks/vf_v2_checks.py`, check Qn (log `spec_v2/checks/vf_v2_checks.log`, 36/36 pass).
- Check IDs in square brackets (e.g. [SS3e]) are the agents' script check labels.

**Chapter references.** The v1 entries below are copied verbatim except for three chapter numbers converted to v2 (VF-CONV-20, VF-CONV-22, VF-PDF-10). All "Used in" lines list **labels**, which are unchanged in v2 even where a statement moved to another chapter (WRITER_SPEC_v2 §5.3).

Common notation:
- $a_s$ denotes whichever expansion parameter the entry states; in VF-LAM and VF-YZL, $a\equiv\alpha_sC_F/(2\pi)$ unless stated.
- $L$ is defined in each entry. In VF-LAM/VF-YZL: $L_z=\ln(-z^2\mu^2e^{2\gamma_E}/4)$ (coordinate), $L_\zeta=\ln(\zeta_z/\mu^2)$ with $\zeta_z=(2xP^z)^2=4p_z^2$, $\ell_p=-L_\zeta$, $L_b=\ln(\mu^2b_T^2/b_0^2)$.
- $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$; $S_k\equiv S_k(N)=\sum_{j=1}^Nj^{-k}$, $S_1(N)=\psi(N+1)+\gamma_E$, $S_2(N)=\zeta_2-\psi'(N+1)$; $\bar N=Ne^{\gamma_E}$.

**Group index**

| group | content | entries | units |
|---|---|---|---|
| CONV | conventions | 24 | all |
| EE | $e^+e^-$ total cross section | 15 | Ch6 |
| SUD | Sudakov form factor | 5 | Ch5 |
| REG | Landau, power counting, regions | 14 | Ch4, App D/E |
| WL | Wilson lines, eikonal and Ward identities, Glauber phase | 13 | Ch3, Ch9, App B/F |
| DIS | DIS at one loop | 14 | Ch7, Ch10, App G |
| PDF | operator definitions, one loop, DGLAP | 15 | Ch8, App K/L |
| DY | Drell–Yan at one loop | 14 | Ch12 |
| THR | threshold | 3 | Ch13 |
| TMD | TMD factorization | 10 | Ch14 |
| SCET | SCET, thrust | 16 | Ch15, Ch16 |
| NRQ | NRQCD | 4 | Ch20 |
| BQ | $B$ decays | 6 | Ch20 |
| EXC | hard exclusive processes | 13 + 1 (VF-EXC-14 in Part B, v2.1) | Ch19 |
| POL | polarized DIS | 3 | Ch7, Ch11 |
| GLA | Glauber region and breaking | 13 | Ch12, Ch18, App O |
| MISC | miscellaneous | 5 | App K, Ch11, Ch17 |
| **QCD** (new) | QCD basics: colour algebra, field strength, renormalization constants, $\beta$, running coupling | 9 | Ch2 |
| **REF** (new) | refdoc S54: OPE segment, triangle, Glauber direction, eikonal box, weights, … | 19 | Ch4–Ch9, Ch12, Ch14, Ch18, Ch19, App M/N/O |
| **LAM** (new) | LaMET: definitions, renormalization, kernels, TMC, power corrections, threshold, quasi-TMD, Fourier step | 20 (VF-LAM-19 new in v2.3) | Ch22 (Ch23) |
| **YZL** (new) | Yizhuang Liu et al.: soft functions, $S_I$, analyticity, quasi-TMD, heavy–light kernel, renormalons, models | 17 (VF-YZL-17 new in v2.3) | Ch23 |
| **FRO** (new) | other frontier results: Landau/Gordan, OPE convergence, regions, Glauber EFT, SLL, NLP, positivity, LUXqed, BK, DPS, NGL, small-$x$ helicity | 17 | Ch24 (and Ch4, Ch8, Ch12, Ch16–Ch18, Ch21) |

---------------------------------------------------------------------------------------------------

# Part A — spec v1 entries (verbatim, IDs unchanged)

## CONV — conventions (23 entries)

### VF-CONV-1 — 光锥坐标与光锥矢量
$$v^\pm=\frac{v^0\pm v^3}{\sqrt2},\qquad v\cdot w=v^+w^-+v^-w^+-\mathbf v_T\cdot\mathbf w_T,\qquad n_A=(1^+,0^-,\mathbf 0_T),\ n_A\cdot v=v^-;\quad n_B=(0^+,1^-,\mathbf 0_T),\ n_B\cdot v=v^+ .$$
$n_B$ is Collins' $w_2$. The PDF Wilson line of hadron $A$ (moving along $+z$) runs along $n_B$ and contains $n_B\cdot A=A^+$.
- **Status:** V.
- **Source:** CONTEXT.md; c_wilson §1 (C4); c_glauber §0.2.
- **Used in:** `def:prelim-lightfront` and throughout.

### VF-CONV-2 — QCD 拉氏量与规范变换
$$\mathcal L=-\tfrac14G^a_{\mu\nu}G^{a\mu\nu}+\sum_q\bar\psi_q(i\slashed D-m_q)\psi_q-\frac1{2\xi}(\partial\cdot A^a)^2+\bar c^a(-\partial^\mu D^{ac}_\mu)c^c,$$
$$D_\mu=\partial_\mu-igA^a_\mu t^a,\quad (D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c,\quad G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu,$$
$$\psi\to U\psi,\qquad A_\mu\to UA_\mu U^{-1}-\frac ig(\partial_\mu U)U^{-1},\qquad {\rm Tr}(t^at^b)=\tfrac12\delta^{ab}.$$
- **Status:** V.
- **Source:** CONTEXT.md; c_pdf §1.
- **Used in:** `def:prelim-qcd`.

### VF-CONV-3 — Feynman 规则（协变规范）
- Quark propagator $\dfrac{i(\slashed p+m)}{p^2-m^2+i0}$.
- Gluon propagator $\dfrac{-i}{k^2+i0}\Big[g^{\mu\nu}-(1-\xi_g)\dfrac{k^\mu k^\nu}{k^2}\Big]\delta^{ab}$.
- Ghost propagator $\dfrac{i\delta^{ab}}{p^2+i0}$ (as Peskin–Schroeder ch. 16).
- Quark–gluon vertex $ig\gamma^\mu t^a$.
- Three-gluon vertex (all momenta incoming, $(k,\mu,a),(p,\nu,b),(q,\rho,c)$): $gf^{abc}[g^{\mu\nu}(k-p)^\rho+g^{\nu\rho}(p-q)^\mu+g^{\rho\mu}(q-k)^\nu]$.
- Ghost vertex $-gf^{abc}p^\mu$, where $p$ is the outgoing-ghost momentum.
- Four-gluon vertex: as Peskin–Schroeder.

Checks: the three-gluon vertex was checked against $i\mathcal L_{\rm int}$ by plane waves. Ward identities fail with the opposite sign, and the $q\bar q\to gg$ cross section is reproduced (VF-WL-9).
- **Status:** V.
- **Source:** c_pdf §1 (s5); c_wilson §5.
- **Used in:** `def:prelim-feynman-rules`.

### VF-CONV-4 — $\overline{\rm MS}$ 与 $S_\varepsilon$
$$g_0^2=4\pi\alpha_s(\mu)\,\mu^{2\varepsilon}\,S_\varepsilon^{-1}Z_g^2,\qquad S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}\quad(\text{binding}),\qquad D=4-2\varepsilon .$$
Collins 2011 uses $S_\varepsilon^{\rm C}=(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$, and
$$\frac{S_\varepsilon}{S^{\rm C}_\varepsilon}=e^{-\varepsilon\gamma_E}\Gamma(1-\varepsilon)=1+\frac{\pi^2}{12}\varepsilon^2+O(\varepsilon^3).$$
The two conventions differ in finite constants wherever $1/\varepsilon^2$ poles are subtracted (TMD $\tilde C$, $\mathcal H$: VF-TMD-5). Bare scale: $g_0^2=4\pi\alpha_s\mu_0^{2\varepsilon}$ (c_ee notation $\mu_0$).
- **Status:** V (binding definition). The ratio was derived by the spec synthesizer and re-derived in `research/c_tmd/DERIVATION.md` §1 item 3. The Collins 2011 section number (§3.3.2) is quoted from Collins–Rogers 2013 (c_tmd §0), not read in the book: cite it as 「Collins 2011 第~3.3.2~节（据 Collins–Rogers 2013）」.
- **Source:** CONTEXT.md; c_dis §1.2; c_ee §1; c_tmd logs.
- **Used in:** `def:prelim-msbar`, `rem:appC-Seps`, `rem:tmd-scheme-constants`.

### VF-CONV-5 — $\beta$ 函数
$$\mu^2\frac{d\alpha_s}{d\mu^2}=-\frac{\beta_0}{4\pi}\alpha_s^2-\frac{\beta_1}{(4\pi)^2}\alpha_s^3-\dots,\qquad \beta_0=\tfrac{11}3C_A-\tfrac43T_Fn_f,\qquad \beta_1=\tfrac{34}3C_A^2-4C_FT_Fn_f-\tfrac{20}3C_AT_Fn_f .$$
In $D$ dimensions, $\mu^2d\alpha_s/d\mu^2=-\varepsilon\alpha_s+\beta(\alpha_s)$.
- **Status:** V for $\beta_0$ (CONTEXT.md; $\delta Z_3$ re-derived in c_pdf, VF-PDF-14). **T** for $\beta_1$, which is quoted from the literature (`Caswell1974`, `Jones1974`) and was not re-derived.
- **v2 note:** the reduction of the group form of $\beta_1$ to the SU(3) value $102-\frac{38}3n_f$ is verified (spec_v2 v2-check Q4b); the group form itself is still quoted, so the status of $\beta_1$ stays **T** (see VF-QCD-5 for $\beta_2$ and the higher coefficients).
- **Used in:** `prop:prelim-beta`.

### VF-CONV-6 — CDR 中的胶子极化平均
The average over polarizations of an external gluon is $\dfrac1{D-2}=\dfrac1{2(1-\varepsilon)}$, together with the colour average $\frac1{N_c^2-1}$. This is part of the $\overline{\rm MS}$ convention for gluon targets. Averaging over 2 polarizations instead gives
$$C_2^g\to C_2^g+P_{qg},\qquad \Delta_{qg}\to\Delta_{qg}+P_{qg}.$$
- **Status:** V.
- **Source:** c_dis §1.2, §13; c_dy §1.3, §3.10.
- **Used in:** `def:pdf-gluon`, `prop:disall-nlo`, `prop:dy-nlo`.

### VF-CONV-7 — 加号分布与乘积约定
$$\int_0^1dz\,[g(z)]_+h(z)=\int_0^1dz\,g(z)[h(z)-h(1)],\qquad \mathcal D_k(z)=\Big[\frac{\ln^k(1-z)}{1-z}\Big]_+ ,$$
$$g(z)\mathcal D_k\equiv g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)\quad(\text{product convention}),$$
$$C_F\Big[\frac{1+z^2}{1-z}\Big]_+=C_F\Big[\frac{1+z^2}{(1-z)_+}+\frac32\delta(1-z)\Big],\qquad \Big[\frac{2z}{1-z}\Big]_+=\frac{2z}{(1-z)_+}+2\delta(1-z),\qquad \Big[\frac{z}{1-z}\Big]_+=z\Big[\frac1{1-z}\Big]_++\delta(1-z).$$
- **Status:** V.
- **Source:** CONTEXT.md; c_pdf §1; c_dy §0; critic c1.
- **Used in:** `def:prelim-plus`.

### VF-CONV-8 — 加号分布的 Mellin 矩
$$\int_0^1z^{N-1}\mathcal D_0=-S_1(N-1)\xrightarrow{N\to\infty}-\ln\bar N,\qquad \int_0^1z^{N-1}\mathcal D_1=\tfrac12\big[S_1^2(N-1)+S_2(N-1)\big]\xrightarrow{N\to\infty}\tfrac12(\ln^2\bar N+\zeta_2).$$
- **Status:** V.
- **Source:** critic c6; c_dy §3.7.
- **Used in:** `lem:prelim-mellin`, `lem:appA-mellin-table`.

### VF-CONV-9 — Wilson 线与 Fourier 约定
$$W[b,a]=P\exp\Big(ig\!\int_a^b\!dz^\mu A^a_\mu(z)t^a\Big),\qquad W[b,a]\to U(b)W[b,a]U^\dagger(a),\qquad \frac{d}{ds}W(s)=ig\,\dot z\cdot A(z(s))\,W(s),$$
with later points (closer to $b$) to the left. Further:
- composition $W[c,b]W[b,a]=W[c,a]$; retracing $W[b,a]W[a,b]=1$;
- adjoint line $W^{(A)}_{ab}[b,a]=2{\rm Tr}[t^aW[b,a]t^bW[a,b]]$;
- Fourier convention $A_\mu(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ik\cdot x}\tilde A_\mu(k)$, with $k$ flowing **into** the line;
- adiabatic regulator: the $j$-th eikonal denominator from the infinite end carries $\pm ij\epsilon$.
- **Status:** V (numerical SU(2)/SU(3) checks).
- **Source:** c_pdf §1, §2.4; c_wilson §1 (C1–C3).
- **Used in:** `def:prelim-wilson`, `prop:prelim-wilson-covariance`.

### VF-CONV-10 — $\gamma_5$、$\epsilon$ 张量与横向张量
$$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,\qquad \epsilon^{0123}=+1,\qquad {\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma},$$
$$g_\perp^{\mu\nu}=g^{\mu\nu}-n_A^\mu n_B^\nu-n_B^\mu n_A^\nu,\qquad \epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}n_{A\rho}n_{B\sigma},\qquad \epsilon_\perp^{12}=+1 .$$
In DR: HVBM with Larin's finite renormalization (VF-POL-1, App I). VGG 1999 use $\varepsilon_{0123}=+1$, which is the opposite sign.
- **Status:** V (all 256 index sets; s1, s7).
- **Source:** c_exclusive §1 (its $\bar n$ is our $n_A$, its $n$ is our $n_B$).
- **Used in:** `def:prelim-gamma5`, `def:appI-hvbm`, `prop:excl-dvcs-lo`.

### VF-CONV-11 — TMD 的 Fourier 约定
$$\tilde f(x,b_T)=\int d^{2-2\varepsilon}k_T\,e^{-ik_T\cdot b_T}f(x,k_T),\qquad b_0=2e^{-\gamma_E},\qquad \mu_b=b_0/b_T,$$
$$\delta^{(2)}(q_T-k_{AT}-k_{BT})\ \Rightarrow\ \int\frac{d^2b_T}{(2\pi)^2}e^{iq_T\cdot b_T}\tilde f_A(b_T)\tilde f_B(b_T).$$
Operator form: $\tilde f^{\rm unsub}(x,b_T)=\int\frac{dw^-}{4\pi}e^{-ixP^+w^-}\langle P|\bar\psi(w)\gamma^+\mathcal W_{\rm staple}\psi(0)|P\rangle$ with $w=(0^+,w^-,b_T)$.
- **Status:** V. Convention: CONTEXT.md; cross-section form: BP T11.10; operator form: `research/c_tmd/DERIVATION.md` §2.1, which follows Aybat–Rogers 2011 eqs. (11), (27): $f(x,k_T)=\int\frac{d^{2-2\varepsilon}b_T}{(2\pi)^{2-2\varepsilon}}e^{+ik_T\cdot b_T}\tilde f(x,b_T)$, i.e. the **same** forward convention $e^{-ik_T\cdot b_T}$ as CONTEXT for TMD PDFs (spec audit re-derived the sign chain). **Caution:** Collins 2011 eq. (13.35) defines the soft factor and the TMD *fragmentation* functions with $e^{+ik_T\cdot b_T}$ (survey §0.3, read in the book); convert explicitly for TMD FFs and for every $b$-odd (T-odd, spin) structure.
- **Used in:** `def:tmd-unsub`, `thm:tmd-factorization`.

### VF-CONV-12 — 真空极化与 $R$
$$\Pi^{\mu\nu}(q)=i\!\int\! d^4x\,e^{iq\cdot x}\langle0|T\,j^\mu(x)j^\nu(0)|0\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\,\Pi(q^2),\qquad j^\mu=\sum_qe_q\bar q\gamma^\mu q,$$
$$\int d^4x\,e^{iq\cdot x}\langle0|j^\mu(x)j^\nu(0)|0\rangle=2\,{\rm Im}\,\Pi^{\mu\nu}(q)\ (q^0>0),\qquad \sigma=\frac{16\pi^2\alpha^2}{s}{\rm Im}\,\Pi(s+i0),\qquad R(s)=12\pi\,{\rm Im}\,\Pi(s+i0),$$
$$\sigma_{\mu\mu}=\frac{4\pi\alpha^2}{3s},\qquad L_{\mu\nu}(q^\mu q^\nu-q^2g^{\mu\nu})=s^2,\qquad \Pi_{\rm PS}=-e^2\Pi .$$
- **Status:** V.
- **Source:** c_ee §1 (1.1)–(1.3); BP §0.4(4).
- **Used in:** `prop:prelim-optical`, `def:ee-R`, `prop:ee-R-ImPi`.

### VF-CONV-13 — 强子张量与结构函数
$$W^{\mu\nu}=\frac1{4\pi}\int d^4z\,e^{iq\cdot z}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle=\Big(-g^{\mu\nu}+\frac{q^\mu q^\nu}{q^2}\Big)F_1+\frac{\tilde P^\mu\tilde P^\nu}{P\cdot q}F_2,\qquad \tilde P=P-\frac{P\cdot q}{q^2}q,$$
$$Q^2=-q^2,\quad x=\frac{Q^2}{2P\cdot q},\qquad F_L=\Big(1+\frac{4M^2x^2}{Q^2}\Big)F_2-2xF_1\ \xrightarrow{M\to0}\ F_2-2xF_1,$$
with spin averaging and $\langle P'|P\rangle=(2\pi)^32E\,\delta^3(\vec P'-\vec P)$. The $1/(4\pi)$ reproduces $F_2=\sum_qe_q^2x(q+\bar q)$. Positivity: $\epsilon_T\epsilon_TW=F_1\ge0$ and $2x\,\epsilon_L\epsilon_LW=F_L\ge0$.
- **Status:** V.
- **Source:** c_dis §1.1, §2; critic c7; BP §0.4(2).
- **Used in:** `def:dis-kinematics`, `prop:dis-W-structure`, `ex:intro-handbag`.

### VF-CONV-14 — 前向 Compton 振幅、交叉与色散关系
$$T^{\mu\nu}=i\!\int\! d^4z\,e^{iq\cdot z}\langle P|T\,j^\mu(z)j^\nu(0)|P\rangle,\qquad \omega=\frac{2P\cdot q}{Q^2}=\frac1x,\qquad {\rm Im}\,T_i(\omega+i0)=2\pi F_i\ (\omega>1),$$
$$T_1(-\omega)=T_1(\omega),\qquad T_2(-\omega)=-T_2(\omega),\qquad T_2=\sum_{n=2,4,\dots}4\omega^{n-1}\!\int_0^1\!dx\,x^{n-2}F_2,\qquad T_1-T_1(0)=\sum_{n=2,4,\dots}4\omega^{n}\!\int_0^1\!dx\,x^{n-1}F_1,$$
$$\text{free quark: }F_2=e_q^2\delta(1-x)\ \Rightarrow\ T_2=\frac{4e_q^2\,\omega}{1-\omega^2}.$$
- **Status:** A (BP §0.4(3), §18.3, S5). Consistent with the c_dis OPE check: the Taylor coefficients of the partonic $T^{\mu\nu}$ equal the moments exactly in $\varepsilon$ (VF-DIS-13).
- **Used in:** `def:dis-compton`, `prop:dis-compton-analytic`, `prop:dis-dispersion`.

### VF-CONV-15 — 扭度 2 算符及其约化矩阵元
$$O_q^{\mu_1\cdots\mu_n}=\mathcal S\,\bar\psi\gamma^{\mu_1}iD^{\mu_2}\cdots iD^{\mu_n}\psi-{\rm traces},\qquad O_g^{\mu_1\cdots\mu_n}=\mathcal S\,G^{\mu_1\alpha}iD^{\mu_2}\cdots iD^{\mu_{n-1}}G_\alpha{}^{\mu_n}-{\rm traces},$$
$$\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}\big(P^{\mu_1}\cdots P^{\mu_n}-{\rm traces}\big),\qquad O_g^{+\cdots+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}\ \ (\langle g|O_g^{+\cdots+}|g\rangle=2(k^+)^n).$$
- **Status:** V.
- **Source:** BP §0.4(6); c_pdf §5.2.
- **Used in:** `def:dis-twist`, `thm:dis-ope`.

### VF-CONV-16 — 反常维度约定与词典
$$\gamma_{ij}(N)=\int_0^1dz\,z^{N-1}P_{ij}(z),\qquad \frac{dA^{(n)}_i}{d\ln\mu^2}=\sum_j\Gamma_{ij}A^{(n)}_j,\quad \Gamma_{ij}=\frac{\alpha_s}{2\pi}\gamma_{ij}(n)+O(\alpha_s^2),\qquad \frac{dC^{(n)}_{a,j}}{d\ln\mu^2}=-\sum_iC^{(n)}_{a,i}\Gamma_{ij},$$
$$\gamma^{(0)}_{\rm MVV}(N)=-2\gamma_{qq}(N)\ (a_s=\tfrac{\alpha_s}{4\pi}),\qquad \gamma_O^{\rm GW}=-\frac{\alpha_s}{\pi}\gamma_{qq}(N)=\frac{\alpha_s}{2\pi}C_F\Big[1-\frac2{N(N+1)}+4\sum_{j=2}^N\frac1j\Big]\ (\mu\,dO/d\mu=-\gamma_OO).$$
- **Status:** VL (MVV eqs. (2.6), (2.7), (3.4) read).
- **Source:** c_pdf §4.4; BP §0.4(7).
- **Used in:** `prop:dis-ope-rg`, `prop:pdf-lo-kernels`.

### VF-CONV-17 — 碎裂函数的定义
$$d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}_c{\rm Tr}_D\Big[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle\Big],\qquad w=(0^+,w^-,\mathbf 0_T),\ z=\frac{p_h^+}{k^+},$$
in the **hadron frame** $\mathbf p_{h,T}=0$, with future-pointing lines along $n_B$. Equivalent parton-frame form: prefactor $\frac1{4N_cz}$ together with an explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$. Free quark: $d_{q/q}=\delta(1-z)$.

**Audit correction (2026-10-10).** The first version of this entry printed the parton-frame prefactor $\frac1{4N_cz}$ together with the hadron frame. That is off by $z^{-2}$ in four dimensions; the free-quark check cannot see it. Reason: the hadron frame is reached by a transverse boost, under which the parton's transverse momentum is $k_T=-p_{hT}/z$, so $d^{2-2\varepsilon}p_{hT}=z^{2-2\varepsilon}d^{2-2\varepsilon}k_T$, and $\frac1z\cdot z^{2-2\varepsilon}=z^{1-2\varepsilon}=z^{d-3}$. Check: at $O(\alpha_s)$ in $A^+=0$ gauge with $h=q$, $X=g$, the definition must give $d^{(1)}_{q/q}=\frac{\alpha_s}{2\pi}C_F\frac{1+z^2}{1-z}\int\frac{dl_T^2}{l_T^2}$ ($z<1$), the LO time-like kernel; the wrong prefactor gives $z^{-2}$ times this. For massless partons in pure DR the bare partonic FF is $\delta(1-z)$ whatever the prefactor, so the $\overline{\rm MS}$ partonic coefficient functions are unaffected; the $z^{-2\varepsilon}$ fixes the scheme of the hadron-level definition.
- **Status:** A (frame-change Jacobian derived by the spec audit; $O(\alpha_s)$ number-density check of `refdoc` reader R1, `check_ff_norm.py`, re-run by the refdoc synthesizer — REFDOC_ANALYSIS §2.4 OUR-1, S9; agrees with the $z^{1-2\varepsilon}=z^{d-3}$ recalled by the critic, D4, and attributed to Collins–Soper 1982 and Collins 2011 ch. 12 — section number to verify).
- **Used in:** `def:pdf-ff`.

### VF-CONV-18 — cusp 与 Collins–Soper 核的归一化
$$\Gamma_{\rm cusp}=\frac{C_F\alpha_s}{\pi}+O(\alpha_s^2),\qquad \gamma_K=2\Gamma_{\rm cusp},\qquad \frac{d\tilde K}{d\ln\mu}=-\gamma_K,\qquad \gamma_q(\alpha_s;\zeta/\mu^2)=\gamma_q(\alpha_s;1)-\tfrac12\gamma_K\ln\frac{\zeta}{\mu^2}.$$
- **Status:** V.
- **Source:** BP §0.4(9); critic c7.
- **Used in:** `def:sudakov-cusp`, `prop:tmd-evolution`.

### VF-CONV-19 — 区域标度与幂次计数单位
$\lambda=m/Q$. The scalings, in $(k^+,k^-,k_T)$, are:
- hard $Q(1,1,1)$;
- $A$-collinear $Q(1,\lambda^2,\lambda)$;
- $B$-collinear $Q(\lambda^2,1,\lambda)$;
- soft $Q(\lambda,\lambda,\lambda)$;
- ultrasoft $Q(\lambda^2,\lambda^2,\lambda^2)$;
- Glauber $|k^+k^-|\ll k_T^2$, typically $Q(\lambda^2,\lambda^2,\lambda)$.

Sterman's $\omega$ is the power of $\lambda_S=\lambda^2$. Libby–Sterman's "soft" is ultrasoft here.
- **Status:** V.
- **Source:** c_regions §2.1, §2.6.
- **Used in:** `def:ir-scalings`. See also VF-REG-7.

### VF-CONV-20 — 事件形状的分布约定
Star distributions:
- jet (reference $\mu^2$): $\int_0^{\mu^2}dp^2[\frac{\ln^k(p^2/\mu^2)}{p^2}]_*f=\int_0^{\mu^2}dp^2\frac{\ln^k(p^2/\mu^2)}{p^2}[f(p^2)-f(0)]$;
- $\mu^{2\varepsilon}(p^2)^{-1-\varepsilon}=-\frac{\delta(p^2)}\varepsilon+\sum_k\frac{(-\varepsilon)^k}{k!}[\frac{\ln^k(p^2/\mu^2)}{p^2}]_*$;
- soft: $\mu^{2\varepsilon}k^{-1-2\varepsilon}=-\frac{\delta(k)}{2\varepsilon}+\sum_k\frac{(-2\varepsilon)^k}{k!}[\frac{\ln^k(k/\mu)}{k}]_*$.

$\tau$-space plus distributions subtract at $\tau=0$: $\int_0^1[g]_+h=\int_0^1g(h-h(0))$.
- **Status:** V.
- **Source:** c_scet §1.
- **Used in:** Ch15 `scet`, Ch16 `jets` (v1: Ch14, Ch15).

### VF-CONV-21 — Laplace 变换（Becher–Schwartz 约定）
$$\tilde t(\nu)=\int_0^\infty d\tau\,e^{-\nu\tau}\frac1{\sigma_0}\frac{d\sigma}{d\tau},\quad s=\frac1{e^{\gamma_E}\nu},\quad L_Q=\ln\frac{Q^2}{\mu^2},\ L_J=\ln\frac{sQ^2}{\mu^2},\ L_S=\ln\frac{sQ}{\mu},\quad \ell=\ln(\nu e^{\gamma_E}),\ L_J=L_Q-\ell,\ L_S=\tfrac12L_Q-\ell .$$
- **Status:** VL (BS 2008 read).
- **Source:** c_scet §1.
- **Used in:** `prop:scet-thrust-oneloop`, `prop:scet-ll`.

### VF-CONV-22 — SCET 光锥矢量
$$n=(1,0,0,1),\quad \bar n=(1,0,0,-1),\quad n\cdot\bar n=2,\quad p^\mu=\bar n\!\cdot\!p\frac{n^\mu}2+n\!\cdot\!p\frac{\bar n^\mu}2+p_\perp^\mu,\quad \bar n\!\cdot\!p=\sqrt2p^+,\ n\!\cdot\!p=\sqrt2p^- .$$
Scalings are written for $(\bar n\cdot p,n\cdot p,p_\perp)$. Rothstein–Stewart and the blueprint use the swapped order.
- **Status:** V.
- **Source:** c_scet §1; critic c7.
- **Used in:** Ch15 `scet` only (v1: Ch14).

### VF-CONV-23 — cusp 反常维度
$$\Gamma_{\rm cusp}=\sum_{n\ge0}\Big(\frac{\alpha_s}{4\pi}\Big)^{n+1}\Gamma_n,\qquad \Gamma_0=4C_F,\qquad \Gamma_1=4C_F\Big[\Big(\frac{67}9-\frac{\pi^2}3\Big)C_A-\frac{20}9T_Fn_f\Big].$$
The Becher–Schwartz arXiv source prints a spurious $C_F$ inside the bracket of $\Gamma_1$.
One-loop cusp of two time-like Wilson lines with Minkowskian cusp angle $\beta$: $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$.
- **Status:**
  - $\Gamma_0$: VL (BS 2008 App. B read);
  - $\Gamma_1$: VL (BS read, corrected against `KorchemskyRadyushkin1987`; c_scet §6 item 10);
  - $\Gamma(\beta)$: **V**. (i) `research/c_tmd/DERIVATION.md` §3.5 (R4): the UV pole of the one-loop soft factor with two time-like lines of rapidity difference $Y$ is $-\frac{\alpha_sC_F}\pi\frac{Y\coth Y-1}\varepsilon$, i.e. two cusps of angle $\beta=Y$ with this anomalous dimension each (rapidity integrals analytic + numeric). (ii) Spec-audit check (`scratchpad/audit/checks1.py`): the exchange graph is governed by $\int_0^1\frac{dx}{1-4x(1-x)\cos^2(\theta/2)}=\frac{\pi-\theta}{\sin\theta}$, which gives the $\gamma\cot\gamma$ structure ($\gamma=\pi-\theta\to i\beta$); the $-1$ is the Wilson-line self-energy, fixed by $\Gamma(0)=0$; $\beta\coth\beta\to|\beta|$ reproduces the light-like normalization $\Gamma_{\rm cusp}=\alpha_sC_F/\pi$. Note: this is the cusp **including** the self-energies of both lines; Becher–Neubert's massive-parton formalism writes $\beta\coth\beta$ alone and puts the $-1$ into $\gamma^Q$.
- **Used in:** `def:sudakov-cusp`, `prop:appB-cusp-oneloop`.

### VF-CONV-24 — Larin 方案中 $\gamma^\mu\gamma_5$ 的替换（本书约定下的符号）
$$\gamma^\mu\gamma_5=-\frac i6\,\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma\qquad(\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3,\ \epsilon^{0123}=+1).$$
The form $\gamma_\mu\gamma_5=\frac i6\epsilon_{\mu\nu\rho\sigma}\gamma^\nu\gamma^\rho\gamma^\sigma$ found in the literature holds with $\epsilon_{0123}=+1$, i.e. $\epsilon^{0123}=-1$. Copying it with the binding $\epsilon^{0123}=+1$ gives the wrong overall sign.
- **Status:** V (spec audit: explicit $4\times4$ Dirac matrices, all $\mu$, both forms; `scratchpad/audit/checks1.py`, `checks2.py`).
- **Used in:** `prop:appI-larin`, `def:appI-hvbm`.

---------------------------------------------------------------------------------------------------

## EE — $e^+e^-$ total cross section

Notation: $a=\alpha_s/\pi$, $L=\ln(-q^2/\mu^2)$, $\ell=\ln(s/\mu^2)$, $c_\Gamma=\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)$.

### VF-EE-1 — Born
$$\sigma_0=\frac{4\pi\alpha^2}{3s}N_c\sum_qe_q^2,\qquad R_0=N_c\sum_qe_q^2 .$$
- **Status:** V.
- **Source:** c_ee §0 row 1.
- **Used in:** `def:ee-R`.

### VF-EE-2 — (not used)

### VF-EE-3 — 单圈流关联函数
$$\Pi_0=N_ce_q^2\frac{2(D-2)}{D-1}\frac{G(1,1)}{(4\pi)^{D/2}}(-q^2-i0)^{-\varepsilon},\qquad \Pi_0^{\overline{\rm MS}}=\frac{N_ce_q^2}{12\pi^2}\Big(\frac53-L\Big),\qquad {\rm Im}\,\Pi_0(s+i0)=\frac{N_ce_q^2}{12\pi}.$$
The imaginary part from $L\to\ell-i\pi$ and from the two-particle cut agree exactly in $\varepsilon$.
- **Status:** V (A5).
- **Source:** c_ee §2.
- **Used in:** `prop:prelim-optical`, `ex:prelim-vacpol`.

### VF-EE-4 — 单圈夸克形状因子（类时）
$$F^{(1)}(q^2)=-\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu_0^2}{-q^2-i0}\Big)^{\varepsilon}c_\Gamma\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)},\qquad F^{(1)}\overset{\overline{\rm MS}}=\frac{\alpha_sC_F}{4\pi}\Big[-\frac2{\varepsilon^2}+\frac{2L-3}{\varepsilon}-L^2+3L-8+\zeta_2+O(\varepsilon)\Big],$$
$${\rm Im}\,F^{(1)}(s+i0)=\frac{\alpha_sC_F}{4\pi}\Big[-\frac{2\pi}\varepsilon+2\pi\ell-3\pi\Big],\qquad 2{\rm Re}\,F^{(1)}=\frac{\alpha_sC_F}{2\pi}\Big[-\frac2{\varepsilon^2}+\frac{2\ell-3}{\varepsilon}-\ell^2+3\ell-8+\zeta_2+\pi^2\Big].$$
- **Status:** V (B0–B6).
- **Source:** c_ee §3.1 (3.1)–(3.3).
- **Used in:** `prop:ee-oneloop`, `prop:sudakov-coulomb`.

### VF-EE-5 — 实辐射 $\gamma^*\to q\bar qg$
With $y_{ij}=2p_i\cdot p_j/s$:
$$-g_{\mu\nu}\sum M^\mu M^{\nu*}=8(1-\varepsilon)g_0^2C_FN_ce_q^2\Big[(1-\varepsilon)\Big(\frac{y_{13}}{y_{23}}+\frac{y_{23}}{y_{13}}\Big)+\frac{2y_{12}}{y_{13}y_{23}}-2\varepsilon\Big],\qquad d\Phi_3=\frac{(4\pi)^{2\varepsilon-3}s^{1-2\varepsilon}}{2\Gamma(2-2\varepsilon)}dy_{13}dy_{23}(y_{12}y_{13}y_{23})^{-\varepsilon},$$
$$\frac{\rho_R}{\rho_0}=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}\frac{2(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)\Gamma(1-\varepsilon)^2}{\varepsilon^2(1-3\varepsilon)(2-3\varepsilon)\Gamma(1-3\varepsilon)}=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}c_\Gamma\Big[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2+O(\varepsilon)\Big];$$
In 4D: $\frac1{\sigma_0}\frac{d\sigma}{dx_1dx_2}=\frac{C_F\alpha_s}{2\pi}\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$.

**Warning:** the separate real and virtual constants depend on the common normalization. The two $\Gamma$-prefactors differ by $1-\frac{\pi^2}2\varepsilon^2$; only the sum is normalization independent.
- **Status:** V (C1–C5).
- **Source:** c_ee §3.2 (3.4)–(3.6).
- **Used in:** `prop:ee-oneloop`, `ex:ir-real-emission`.

### VF-EE-6 — $O(\alpha_s)$ 的 $R$
$$\frac{\rho_R+\rho_V}{\rho_0}=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}{s}\Big)^{\varepsilon}\Big[\frac32+O(\varepsilon)\Big]\ \Rightarrow\ R=R_0\Big(1+\frac{3C_F}4\frac{\alpha_s}\pi\Big)=R_0\Big(1+\frac{\alpha_s}\pi\Big).$$
- **Status:** V (D1–D4).
- **Source:** c_ee §3.3 (3.7).
- **Used in:** `prop:ee-oneloop`.

### VF-EE-7 — 欧氏两圈关联函数
$$\Pi^{(1)}_{\rm bare}=N_ce_q^2C_F\frac{g_0^2(Q^2)^{-2\varepsilon}}{(4\pi)^D}\big[r_1G(1,1)^2+r_2G(1,1)G(1{+}\varepsilon,1)\big],\quad r_1=-\frac{4(1-\varepsilon)(2-\varepsilon+2\varepsilon^2)}{\varepsilon(3-2\varepsilon)},\quad r_2=\frac{16(1-\varepsilon)(1-2\varepsilon)(2-2\varepsilon+\varepsilon^2)}{\varepsilon(3-2\varepsilon)(2-3\varepsilon)},$$
$$G(1{+}\varepsilon,1)=\frac{\Gamma(2\varepsilon)\Gamma(1-2\varepsilon)\Gamma(1-\varepsilon)}{\Gamma(1+\varepsilon)\Gamma(2-3\varepsilon)},\qquad Q^2=-q^2-i0,\qquad \hat I(1,1,1,1,1)=6\zeta_3+O(\varepsilon),$$
$$\Pi_{\overline{\rm MS}}(q^2)=\frac{N_ce_q^2}{12\pi^2}\Big[\frac53-L+\frac{\alpha_s}\pi\frac{3C_F}4\Big(\frac{55}{12}-4\zeta_3-L\Big)\Big]+O(\alpha_s^2),\qquad D(Q^2)=N_ce_q^2\Big(1+\frac{3C_F}4\frac{\alpha_s}\pi\Big).$$
The constants $\frac53$ and $\frac{55}{12}-4\zeta_3$ are scheme dependent (contact terms).
- **Status:** V (transversality, IBP; P0–P5, T2).
- **Source:** c_ee §4.1–4.3 (4.1)–(4.5).
- **Used in:** `prop:ee-twoloop`, `lem:appC-ibp`.

### VF-EE-8 — 精确到 $\varepsilon$ 的切割恒等式
$$2(D-1)\,s\,{\rm Im}\,\Pi^{(1)}_{\rm bare}(s+i0)=\rho_V+\rho_R$$
This holds term by term: $r_1G_{11}^2\leftrightarrow\rho_V$ and $r_2G_{11}G_{1+\varepsilon,1}\leftrightarrow\rho_R$.
- **Status:** V (proved analytically by reflection formulas; 30 digits at 5 values of $\varepsilon$; C1, X1).
- **Source:** c_ee §4.4 (4.6).
- **Used in:** `prop:ee-cutting-exact`, `rem:prelim-cutting-dr`.

### VF-EE-9 — 重整化群结构、围道公式与 $\pi^2$ 项
$$\mu^2\frac{d\Pi}{d\mu^2}=\frac{N_c\sum e_q^2}{12\pi^2}(1+a+\dots)\ (q\text{-independent}),\qquad D(Q^2)\equiv-12\pi^2Q^2\frac{d\Pi(-Q^2)}{dQ^2}=R_0\,d(a(Q^2)),\qquad R(s)=\frac1{2\pi}\int_{-\pi}^{\pi}d\theta\,D(se^{i\theta}),$$
$$r_1=d_1,\quad r_2=d_2,\quad r_3=d_3-\frac{\pi^2}3b_0^2d_1,\quad r_4=d_4-\pi^2\Big(b_0^2d_2+\frac56b_0b_1d_1\Big),\qquad b_0=\frac{\beta_0}4,\ b_1=\frac{\beta_1}{16},\ \mu^2\frac{da}{d\mu^2}=-b_0a^2-b_1a^3 .$$
At order $a^n$, $\Pi_{\overline{\rm MS}}$ is a polynomial in $L$ of degree $\max(1,n)$, and $R^{(n)}$ is a polynomial of degree $\le n-1$ in $\ln(s/\mu^2)$. For SU(3), $\frac{\pi^2}3b_0^2=16.66,14.28,12.09$ for $n_f=3,4,5$.
- **Status:** V (G1–G4, two independent continuations).
- **Source:** c_ee §6.
- **Used in:** `prop:ee-adler-rg`, `cor:ee-R-alphas`, `prop:ee-contour`, `ex:ee-pi2`.

### VF-EE-10 — $R$ 的 $O(a^2)$ 系数
$$R=R_0\big[1+a+r_2a^2+\dots\big],\qquad r_2^{\rm SU(3)}=\frac{365}{24}-11\zeta_3-n_f\Big(\frac{11}{12}-\frac23\zeta_3\Big)=1.9857-0.1153\,n_f\quad(\overline{\rm MS},\ \mu^2=s,\ a=\alpha_s(s)/\pi).$$
General group:
$$R=R_0\Big[1+\tfrac34C_Fa+a^2\Big(-\tfrac{3}{32}C_F^2+C_FC_A\big(\tfrac{123}{32}-\tfrac{11}4\zeta_3\big)+C_FT_Fn_f\big(-\tfrac{11}8+\zeta_3\big)\Big)+\dots\Big]$$
- **Status:** V for SU(3) (critic c4). **C** for the general-group form: it reproduces the verified SU(3) value, but the agent did not read the originals.
- **Literature:** `ChetyrkinKataevTkachov1979`, `DineSapirstein1979`, `CelmasterGonsalves1980a`. Values at $a^3$, $a^4$ are quoted as literature only.
- **Used in:** `cor:ee-R-alphas`.

### VF-EE-11 — KLN：排他部分与夸克能谱
$$\frac{\sigma(q\bar q)^{(1)}}{\sigma_0}=N_\varepsilon\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\pi^2\Big],\qquad \frac{\sigma(q\bar qg)}{\sigma_0}=N_\varepsilon\Big[\frac2{\varepsilon^2}+\frac3\varepsilon+\frac{19}2-\pi^2\Big],\qquad N_\varepsilon=\frac{\alpha_sC_F}{2\pi}\Big(\frac{4\pi\mu_0^2}s\Big)^{\varepsilon}c_\Gamma,$$
$$\frac1{\sigma_0}\frac{d\sigma}{dx}\Big|_{\rm pole}=-\frac1\varepsilon\frac{\alpha_s}{2\pi}P_{qq}(x).$$
The moments $n=0..3$ of the $1/\varepsilon$ coefficient are $0,\frac43,\frac{25}{12},\frac{157}{60}$ (times $C_F$).
- **Status:** V (E1–E4).
- **Source:** c_ee §7.
- **Used in:** `ex:ee-quark-spectrum`, `rem:coll-sia-nlo`.

### VF-EE-12 — Sterman–Weinberg 两喷注截面
$$\sigma_{2j}=\sigma_0\Big\{1-\frac{C_F\alpha_s}\pi\Big[4\ln\delta\ln2\epsilon+3\ln\delta+\frac{\pi^2}3-\frac52\Big]\Big\},\qquad \epsilon<\delta\ll1,$$
where $\epsilon$ is the energy fraction of the **total** energy $\sqrt s$. With a fraction $\epsilon'$ of the beam energy the log reads $4\ln\delta\ln\epsilon'$. The formula does not apply for $\epsilon\gg\delta$.
- **Status:** V (S1–S6, exact numerics).
- **Source:** c_ee §8.
- **Used in:** `prop:jets-sw`, `ex:jets-sw`.

### VF-EE-13 — 软子集的红外度
For a soft subset $S$ attached $A$ times to non-soft lines, $A_q$ of which are quark ends: $d=A+\frac12A_q\ge2$.
Euclidean IR finiteness at non-exceptional momenta then follows from the convergence theorems (`PoggioQuinn1976`, `LowensteinZimmermann1975`, `BreitenlohnerMaison1977a`).
- **Status:** A (BP S3). The writer re-derives the counting.
- **Used in:** `thm:ee-euclid-ir`.

### VF-EE-14 — Adler 函数的色散表示与抹平恒等式
$$D(Q^2)=Q^2\int_0^\infty ds\,\frac{R(s)}{(s+Q^2)^2},\qquad \bar R(s,\Delta)\equiv\frac\Delta\pi\int_0^\infty ds'\frac{R(s')}{(s'-s)^2+\Delta^2}=\frac{12\pi}{2i}\big[\Pi(s+i\Delta)-\Pi(s-i\Delta)\big].$$
Check: a constant $R$ gives $D=R$.
- **Status:** A (BP §18.3).
- **Used in:** `prop:ee-adler-dispersion`, `prop:ee-smearing`.

### VF-EE-15 — 无质量传播子型图的单标度结构
Every bare $(n{+}1)$-loop contribution to $\Pi$ equals $c_n(\varepsilon)(\mu_0^2)^{n\varepsilon}(-q^2-i0)^{-(n+1)\varepsilon}$, with $c_n$ meromorphic in $\varepsilon$.
- **Status:** V (dimensional analysis; explicit at one and two loops).
- **Source:** c_ee §5 item 2.
- **Used in:** `lem:ee-single-scale`.

---------------------------------------------------------------------------------------------------

## SUD — Sudakov form factor

### VF-SUD-1 — 单圈形状因子（精确到 $\varepsilon$）
$$F(Q^2)=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\frac{e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)}{\Gamma(1-2\varepsilon)}\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]=1+\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+\varepsilon\Big(-16+\frac32\zeta_2+\frac{14}3\zeta_3\Big)+O(\varepsilon^2)\Big]$$
Here $Q^2=-q^2>0$ (spacelike). All poles are infrared ($Z_1=Z_2$; external self-energies are scaleless).
- **Status:** VL. Derived independently by c_dis, c_ee, c_dy and c_scet; equal to MVV 2005 through $\varepsilon^4$ (c_dy §6.3).
- **Source:** c_dis §4 (boxed); c_scet §0 row 7.
- **Used in:** `prop:sudakov-oneloop`, `sec:appC-formfactor`.

### VF-SUD-2 — 类时延拓与 $\pi^2$ 增强
$(\mu^2/Q^2)^\varepsilon\to(\mu^2/s)^\varepsilon e^{i\pi\varepsilon}$, and
$$2{\rm Re}\,F^{(1)}(s+i0)=\frac{\alpha_sC_F}{2\pi}\Big(\frac{\mu^2}s\Big)^{\varepsilon}\cos(\pi\varepsilon)f(\varepsilon),\qquad f=-K_v\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}.$$
At one loop the timelike value exceeds the spacelike one by $\frac{\alpha_sC_F}{2\pi}\pi^2$. In DY, the $\delta(1-z)$ coefficient decomposes as $\frac{2\pi^2}3=-\frac{\pi^2}2(K_r)+\frac{\pi^2}6(K_v)+\pi^2(\cos\pi\varepsilon)$.
- **Status:** V.
- **Source:** c_ee §3.1 (B6); c_dy §3.4–3.5 (`plus_trap.py`).
- **Used in:** `prop:sudakov-oneloop`, `cor:sudakov-exponentiation`, `prop:dy-nlo`.

### VF-SUD-3 — $K+G$ 的单圈内容
$$\frac{\partial\ln F}{\partial\ln Q^2}=\frac12\big[K(\varepsilon,\alpha_s)+G(Q^2/\mu^2,\alpha_s,\varepsilon)\big],\qquad K=\frac{\alpha_sC_F}{4\pi}\frac4\varepsilon,\qquad G=\frac{\alpha_sC_F}{2\pi}\Big(3+2\ln\frac{\mu^2}{Q^2}\Big),\qquad \mu\frac{dG}{d\mu}=-\mu\frac{dK}{d\mu}=\gamma_K=\frac{2C_F\alpha_s}\pi .$$
- **Status:** V (critic c7; pole and log terms only).
- **Used in:** `prop:sudakov-kg`.

### VF-SUD-4 — 双对数系数
$$\delta F_{\rm LL}=-\frac\alpha{2\pi}\ln\frac{Q^2}{P_1^2}\ln\frac{Q^2}{P_2^2}\ (\text{off-shell}),\qquad \delta F_{\rm LL}=-\frac\alpha{4\pi}\ln^2\frac{Q^2}{M^2}\ (\text{massive photon}).$$
In QCD, $\alpha\to C_F\alpha_s$.
- **Status:** VL (agrees with Sudakov's and Jackiw's coefficients as quoted in `Collins:1989bt`).
- **Source:** c_regions R6.
- **Used in:** `ex:sudakov-ll`.

### VF-SUD-5 — 多腿振幅红外极点：偶极子公式的归一化
$$\boldsymbol\Gamma=\sum_{(i,j)}\frac{\mathbf T_i\cdot\mathbf T_j}2\,\gamma_{\rm cusp}(\alpha_s)\ln\frac{\mu^2}{-s_{ij}}+\sum_i\gamma^i(\alpha_s),\qquad s_{ij}=2\sigma_{ij}p_i\cdot p_j+i0,$$
where $(i,j)$ runs over **ordered** pairs with $i\ne j$ (each unordered pair twice), $\sigma_{ij}=+1$ if $i,j$ are both incoming or both outgoing and $-1$ otherwise, $\gamma_{\rm cusp}=4\frac{\alpha_s}{4\pi}+\dots$ is Casimir-stripped ($\Gamma^F_{\rm cusp}=C_F\gamma_{\rm cusp}$), $\gamma^q=-3C_F\frac{\alpha_s}{4\pi}+\dots$, and $\frac{d}{d\ln\mu}|\mathcal M_{\rm fin}\rangle=\boldsymbol\Gamma|\mathcal M_{\rm fin}\rangle$.
Check: for the quark form factor ($\mathbf T_1\cdot\mathbf T_2=-C_F$) this gives $\frac{d\ln C_V}{d\ln\mu}=C_F\gamma_{\rm cusp}\ln\frac{-q^2}{\mu^2}+2\gamma^q=\frac{C_F\alpha_s}{4\pi}(4L-6)$, exactly the derivative of VF-SCET-8.
- **Status:** V-consistency (spec audit: the ordered-pair reading is the one consistent with VF-SCET-8). The writer still cites `Becher:2009cu` eq. (2) for the general form; whether the source writes the sum over ordered pairs with $\frac12$ or over unordered pairs without it is immaterial.
- **Used in:** `thm:sudakov-ir-poles`.

---------------------------------------------------------------------------------------------------

## REG — Landau equations, power counting, method of regions

### VF-REG-1 — Feynman 参数表示
$$I(p)=\int\prod_{l=1}^{L}\frac{d^Dk_l}{i\pi^{D/2}}\prod_{j=1}^{N}\frac{1}{(-D_j-i0)^{\nu_j}}=\frac{\Gamma(\nu-LD/2)}{\prod_j\Gamma(\nu_j)}\int_{\mathbb R_+^N}\prod_jd\alpha_j\,\alpha_j^{\nu_j-1}\delta\Big(1-\sum_{j\in\sigma}\alpha_j\Big)\frac{\mathcal U^{\nu-(L+1)D/2}}{(\mathcal F-i0)^{\nu-LD/2}},$$
with $D_j=q_j^2-m_j^2$, $\mathcal D(\alpha,k)=\sum_j\alpha_j(m_j^2-q_j^2)$, $\mathcal U=\det A$ and $\mathcal F=\mathcal U\mathcal D(\alpha,k_c)$. The homogeneity degrees of $\mathcal U$ and $\mathcal F$ are $L$ and $L+1$.
- **Status:** V.
- **Source:** c_regions §1.1.
- **Used in:** `def:ir-landau-setup`.

### VF-REG-2 — 参数空间的围道形变
$$z_j=\alpha_j\Big[1-i\tau\eta\Big(\partial_j\mathcal F-\sum_k\alpha_k\partial_k\mathcal F\Big)\Big],\qquad {\rm Im}\,\mathcal F(z)=-\tau\eta V+O(\eta^3),\qquad V=\sum_j\alpha_j(\partial_j\mathcal F)^2-c^2\ge0 .$$
- **Status:** V (L2 symbolic, L6 numeric).
- **Source:** c_regions §1.2 (Theorem L1).
- **Used in:** `thm:ir-landau-alpha`.

### VF-REG-3 — 包络恒等式与动量空间判据
$$\frac{\partial(\mathcal F/\mathcal U)}{\partial\alpha_j}=-D_j(k_c),\qquad \frac{\mathcal F}{\mathcal U}=\sum_j\alpha_j(m_j^2-q_j^2)\Big|_{k_c}.$$
Momentum space: if no $\alpha\in\mathbb R^S_{\ge0}\setminus\{0\}$ satisfies $\sum_{j\in S}\alpha_ju_j=0$, with $u_j=\partial D_j/\partial k$, then a local deformation $k\to k+i\eta\chi v$ exists, with
$$D_j(k+i\eta\chi v)=D_j(k)-\eta^2\chi^2(v'_j)^2+2i\eta\chi\,q_j\cdot v'_j .$$
- **Status:** V (L1, L5).
- **Source:** c_regions §1.3–1.4 (L2, L3).
- **Used in:** `lem:ir-envelope`, `thm:ir-landau-momentum`, `lem:appD-gordan`.

### VF-REG-4 — 单圈无质量顶点的 Landau 集
$\mathcal F=-Q^2\alpha_1\alpha_2$. The Landau set consists of:
- the closed edges $\{\alpha_2=0\}$ (collinear to $p_1$, $k=xp_1$) and $\{\alpha_1=0\}$ (collinear to $p_2$);
- the soft corner $k=0$;
- the edge $\{\alpha_0=0\}$, but only at $Q^2=0$.

Caveat: the massless self-energy has a momentum-space pinch without a parameter pinch (Collins 2020 App. D1).
- **Status:** V (L3a, L4).
- **Source:** c_regions §1.6, §1.8.
- **Used in:** `ex:ir-vertex`, `lem:ir-envelope`.

### VF-REG-5 — 无质量箱图的 Landau 集
The Landau set is the 4 edges $(01),(12),(23),(30)$ plus the 4 corners. The edges $(02)$ and $(13)$ belong to it only at $s=0$ or $t=0$.
- **Status:** V (L3e).
- **Source:** c_regions §1.7.

### VF-REG-6 — 顶点共线区的 $k^-$ 积分
$$\int dk^-\frac1{D_0D_1D_2}=\frac{2\pi i}{2p_1^+}\frac{1}{k_T^2\,\big(xQ^2-k_T^2/(1-x)\big)}$$
The poles pinch $k^-=0$ from opposite sides, and the remaining $\int d^2k_T/k_T^2$ is logarithmic.
- **Status:** V (C1–C5).
- **Source:** c_regions §2.2 (P1).
- **Used in:** `ex:ir-vertex`.

### VF-REG-7 — 程函近似的误差
Glauber, soft and ultrasoft exchanges all scale as $\lambda^0$. The eikonal error is $O(\lambda)$ for soft, $O(\lambda^2)$ for ultrasoft and $O(1)$ for Glauber exchanges. In the Glauber region, $(p_A+k)^2\simeq2p_A^+k^--2p_{A,T}\cdot k_T-k_T^2$.
- **Status:** V (P1, P3, P6).
- **Source:** c_regions §2.6.
- **Used in:** `def:ir-scalings`, `def:ir-glauber`.

### VF-REG-8 — 约化图的超表观红外发散度（Feynman 规范，Sterman 单位）
$$\omega(R)=\sum_J\tfrac12\big(f^g_J+t_J+2u_J+2f^b_J-e_J\big)+\tfrac12\sum_Js^q_J+b_{S\to H}+\tfrac32f_{S\to H}.$$
Check table (P7):

| configuration | $\omega$ |
|---|---|
| Sudakov soft and collinear | 0 |
| transverse gluon into $H$ | $\frac12$ |
| "−" gluon into $H$ | 1 |
| extra $q\bar q$ pair into $H$ | 1 |
| soft quark exchange | 1 |
| soft gluon into $H$ | 1 |
| soft quark into $H$ | 2 |
| gluon jet with only scalar gluons | $-\frac12$ (super-leading) |

Feynman-gauge K dominance: $J\cdot H=(J^+/k^+)(k\cdot H)+O(\lambda^2)$ (P5).
- **Status:** V. Agrees with Sterman TASI'95 eq. (64) and with BP P3.9 once the bad-component term is added.
- **Source:** c_regions §2.4 (P2).
- **Used in:** `prop:ir-power-counting`, `prop:appE-degree`, `ex:ir-k-dominance`.

### VF-REG-9 — 单圈 Glauber 钳夹判据
For the vertex, each light-cone integral has one pole in the Glauber region: not trapped. For an incoming and an outgoing $A$-collinear line, the poles are $k^-=-k_T^2/(2p_A^+)+i0$ and $k^-=k_T^2/(2p_{A'}^+)-i0$, which pinch. The exact integral is finite,
$$\frac{2\pi i}{2k_T^2(p_A^++p_{A'}^+)},$$
whereas the eikonal version diverges.
- **Status:** V.
- **Source:** c_regions §2.6.
- **Used in:** `prop:ir-glauber-trapping`.

### VF-REG-10 — 离壳 Sudakov 三角形的区域展开
Each region is to be multiplied by $1/Q^2$:
$$H=\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)},\quad C_{1,2}=-\Big(\frac{\mu^2}{P^2}\Big)^{\varepsilon}e^{\varepsilon\gamma_E}\frac{\Gamma(1+\varepsilon)\Gamma^2(-\varepsilon)}{\Gamma(1-2\varepsilon)},\quad S=-\Big(\frac{\mu^2Q^2}{P^4}\Big)^{\varepsilon}e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma(\varepsilon)\Gamma(-\varepsilon),$$
$$H+C_1+C_2+S=\frac1{Q^2}\Big[\ln^2\frac{Q^2}{P^2}+\frac{\pi^2}3\Big]+O(\varepsilon),$$
$$Q^2I=L^2+\frac{\pi^2}3+t\Big(2L^2+4L-4+\frac{2\pi^2}3\Big)+t^2\big(6L^2+14L-11+2\pi^2\big)+O(t^3L^2),\qquad L=\ln t,\ t=P^2/Q^2 .$$
The on-shell massless form factor equals its hard region (c_regions §3.7).
- **Status:** VL (BBF 2015 eqs. (2.39)–(2.44); Usyukina–Davydychev).
- **Source:** c_regions §3.2 (R1–R3).
- **Used in:** `ex:sudakov-offshell`, `ex:sudakov-onshell-hard`.

### VF-REG-11 — 有质量交换、无质量在壳外线
Pure DR is ill-defined here. With analytic regulators,
$$H+C_1+C_2=\frac1{Q^2}\Big[\frac12\ln^2\frac{Q^2}{M^2}+\frac{\pi^2}3\Big].$$
- **Status:** VL (Jantzen 2011 eqs. (6.26)–(6.30); BBF eqs. (2.50)–(2.52)).
- **Source:** c_regions §3.5 (R4).
- **Used in:** `ex:sudakov-massive`.

### VF-REG-12 — 有质量在壳外线、无质量胶子
Pure DR suffices. At $\mu=Q$:
$$H+C_1+C_2=\frac1{Q^2}\Big[\frac1\varepsilon\ln\frac{m^2}{Q^2}-\frac12\ln^2\frac{m^2}{Q^2}-\frac{\pi^2}6\Big].$$
This corrects critic O11.
- **Status:** V (C1).
- **Source:** c_regions §3.6 (R5).
- **Used in:** `ex:sudakov-massive`.

### VF-REG-13 — 一维玩具积分与零区
$I=\int_0^\infty\frac{dk}{(k+m)(k+M)}$. With the regulator $k^{-e}$: $T_s+T_h\to\frac{\ln(M/m)}M$ and $T_sT_h=0$. With cutoffs instead, the overlap must be subtracted (zero-bin).
- **Status:** V.
- **Source:** c_regions §3.3.
- **Used in:** `ex:ir-regions-toy`.

### VF-REG-14 — 归一化注记
$q^2C_0=Q^2I$, relating the Passarino–Veltman $C_0$ to the BBF integral $I$.
- **Status:** V.
- **Source:** c_regions §3.2.
- **Used in:** `ex:sudakov-offshell`.

---------------------------------------------------------------------------------------------------

## WL — Wilson lines, eikonal and Ward identities, Grammer–Yennie, Glauber phase

### VF-WL-1 — 半无限 Wilson 线的动量空间规则
**Universal rule:**
- vertex $igt^av^\mu$;
- eikonal propagator $\dfrac{i}{v\cdot\ell+i0}$, with $\ell$ along the orientation and $\ell=0$ on the segment reaching infinity;
- colour in path order.

**Explicit forms.** Past-pointing line, $k_1$ nearest $-\infty$:
$$W^{(m)}[0,-\infty n]=\prod_j[ig\,n\cdot\tilde A(k_j)]_{\rm path\ order}\prod_{j=1}^m\frac{i}{n\cdot(k_1+\dots+k_j)+i0}.$$
Future-pointing line, $k_1$ nearest $0$:
$$W^{(m)}[\infty n,0]:\ \prod_{j=1}^m\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}.$$
Conjugate lines get the complex-conjugate rules. One-gluon terms: $W[\infty n,0]\ni gt^an^\mu\tilde A_\mu(k)/(n\cdot k-i0)$ and $W[-\infty n,0]\ni gt^an^\mu\tilde A_\mu(k)/(n\cdot k+i0)$.
- **Status:** V (1a–1c).
- **Source:** c_wilson §2.2–2.5; BP §0.4(10); c_glauber §0.2.
- **Used in:** `prop:prelim-wilson-rules`, `prop:appB-rules`.

### VF-WL-2 — 阿贝尔程函恒等式
$$\sum_{\pi\in S_m}\prod_{j=1}^m\frac1{a_{\pi(1)}+\dots+a_{\pi(j)}}=\prod_j\frac1{a_j}$$
It is exact at finite $\epsilon$ with the adiabatic regulator ($j$-th denominator $+ij\epsilon$), not with a uniform $+i\epsilon$.
- **Status:** V (2a).
- **Source:** c_wilson §3.1.
- **Used in:** `lem:prelim-eikonal-identity`.

### VF-WL-3 — 非阿贝尔：路径排序与 web
$$W^{(2)}-\tfrac12\big(W^{(1)}\big)^2=\tfrac14\sum_{r,s}[T_s,T_r]\big(E(r,s)-E(s,r)\big)\quad(\text{exact at finite }\epsilon).$$
The symmetric part obeys VF-WL-2.
- **Status:** V (2b).
- **Source:** c_wilson §3.3.
- **Used in:** `prop:sudakov-webs`, `prop:appB-webs`.

### VF-WL-4 — 洗牌恒等式
$$\sum_{\sigma\in S_m}\prod_{j=1}^m\frac1{n\cdot(k_{\sigma1}+\dots+k_{\sigma j})+i0}=\prod_{j=1}^m\frac1{n\cdot k_j+i0},$$
together with the general shuffle product of two eikonal lines.
- **Status:** V.
- **Source:** c_wilson §3.1–3.2.
- **Used in:** `lem:appB-shuffle`.

### VF-WL-5 — 程函近似
$$S(p+k)\,ig\gamma^\mu t^a\,u(p)\simeq-g\,t^a\frac{p^\mu}{p\cdot k+i0}u(p)\quad(\text{incoming quark}).$$
$m$ soft gluons give $W[0,-\infty p]$. Outgoing lines get $-i0$.
- **Status:** V (3).
- **Source:** c_wilson §4.
- **Used in:** `ex:prelim-eikonal-two`.

### VF-WL-6 — 基本 Ward 恒等式
- (W1) $S(p+k)(ig\slashed kt^a)S(p)=gt^a[S(p+k)-S(p)]$.
- (W2) On-shell ends: $\bar u(p')ig\slashed kS(p'-k)=g\bar u(p')$, $S(p+k)ig\slashed ku(p)=-gu(p)$, $\bar v(p)ig\slashed kS(-p-k)=+g\bar v(p)$, $S(-p+k)ig\slashed kv(p)=-gv(p)$.
- (W3) $q_{1\mu}V^{\mu\nu\rho}_{abc}=gf^{abc}[(q_3^2g^{\nu\rho}-q_3^\nu q_3^\rho)-(q_2^2g^{\nu\rho}-q_2^\nu q_2^\rho)]$.
- (W4) Ghost vertex: $k_\mu(-gf^{abc}p'^\mu)=-\frac g2f^{abc}(p'^2-p^2+k^2)$. This is not a pure difference.
- (W5) Eikonal: $\dfrac{n\cdot k}{(n\cdot\ell+i0)(n\cdot(\ell+k)+i0)}=\dfrac1{n\cdot\ell+i0}-\dfrac1{n\cdot(\ell+k)+i0}$.

Fermion line with on-shell ends: the sum over insertions is $g\sum_r[\text{gluon }r\text{ with }q_r+k,\ [T_K,T_r]]$, which vanishes in the abelian case.
- **Status:** V (4a; s4(a,b)).
- **Source:** c_wilson §5.1–5.2.
- **Used in:** `lem:method-ward-elementary`, `lem:method-ward-abelian`.

### VF-WL-7 — $\gamma^*\to q\bar qg$，$\epsilon\to k$
- On shell: $k_\mu\mathcal A^{\mu\nu}=0$.
- With the antiquark leg off shell: $k_\mu H^\mu=-gt^aH_0$. With the K projector this gives the first term of $W[\infty n_1,0]$.
- Check: $\sum|\mathcal M|^2=8N_cC_Fg^2\frac{x_1^2+x_2^2}{(1-x_1)(1-x_2)}$.
- **Status:** V (4b).
- **Source:** c_wilson §5.3.
- **Used in:** `prop:method-ward-tree`(a).

### VF-WL-8 — DIS：PDF Wilson 线的种子
$$k_\mu H^\mu_a=g\,t^aH_0,\qquad H_\mu\frac{k^\mu n_B^\alpha}{n_B\cdot k-i0}=W^{(1)}[\infty n_B,0]H_0,$$
$$k_{1\mu}k_{2\nu}H^{\mu\nu}_{ab}=(n_B\!\cdot\!k_1)(n_B\!\cdot\!k_2)\,g^2\Big[\frac{t^bt^a}{n_B\cdot K\,n_B\cdot k_2}+\frac{t^at^b}{n_B\cdot K\,n_B\cdot k_1}\Big]H_0=(n_B\!\cdot\!k_1)(n_B\!\cdot\!k_2)W^{(2)}_{ab}[\infty n_B,0]H_0,\qquad K=k_1+k_2 .$$
DIS gives $-i0$ (future pointing); DY gives $+i0$ (past pointing). No ghost or three-gluon graph enters at this order.
- **Status:** V (4c; s4(f), $10^{-12}$).
- **Source:** c_wilson §5.4.
- **Used in:** `prop:method-ward-tree`(b), `prop:appF-two-gluon`.

### VF-WL-9 — 非阿贝尔树图恒等式、鬼场与 $q\bar q\to gg$
$$k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{g^2f^{abc}}{Q^2}\big(k_2^2g^{\nu\sigma}-k_2^\nu k_2^\sigma\big)J_{c\sigma},\qquad J_c^\sigma=\bar v(p_2)\gamma^\sigma t^cu(p_1)\quad(q\bar q\to g^*g^*),$$
$$\sum_{\rm phys}|\mathcal A|^2=\sum_{-g,-g}|\mathcal A|^2-2\sum|\mathcal A_{\rm gh}|^2,\qquad \frac1{36}\sum_{\rm phys}|\mathcal A|^2=g^4\Big[\frac{32}{27}\frac{t^2+u^2}{tu}-\frac83\frac{t^2+u^2}{s^2}\Big].$$
For $\gamma^*\to q\bar qg^*g^*$: $k_{1\mu}\mathcal A^{\mu\nu}_{ab}=\frac{igf^{abc}}{Q^2}(k_2^\nu k_2^\sigma-k_2^2g^{\nu\sigma})\mathcal A^c_\sigma(Q)$. The Slavnov–Taylor identity holds with ghost terms (§5.6).
- **Status:** VL (`CombridgeKripfganzRanft1977`; ratio $-1=2\times10^{-13}$).
- **Source:** c_wilson §5.5–5.6.
- **Used in:** `prop:prelim-unitarity`, `thm:prelim-slavnov-taylor`, `ex:method-ward-tree`, `prop:appJ-ghost-cuts`.

### VF-WL-10 — 共线 Grammer–Yennie 分解
$$g_{\mu\nu}=K_{\mu\nu}+G_{\mu\nu},\qquad K_{\mu\nu}=\frac{k_\mu w_{2\nu}}{k\cdot w_2-i0},\ w_2=n_B,\qquad H\cdot G\cdot C=H\cdot\Big(C-\frac{C^+}{k^+}k\Big).$$
$G$ is suppressed by $\ge\lambda$: by $\lambda^2$ for an on-shell massless parent, by $\lambda$ generically. The exception is a single transverse gluon as the active parton. The $i0$ is $-i0$ for final-state attachments (DIS) and $+i0$ for initial-state ones (DY).
- **Status:** algebra V; power counting [A] (5a). Collins 2011 eqs. (11.4)–(11.6) are corrected in the errata, as flagged by c_wilson.
- **Source:** c_wilson §6.2.
- **Used in:** `def:method-collinear-approx`, `lem:method-gy`.

### VF-WL-11 — 软 Grammer–Yennie 分解
$$K_s^{\mu\nu}=\frac{k^\mu n_A^\nu}{n_A\cdot k\pm i0},$$
with $+i0$ for an incoming $A$ line and $-i0$ for an outgoing one. $G_s$ is suppressed by $\lambda|k_T|/|k^-|$ outside the Glauber region and is $O(1)$ inside it. In the Glauber region $(p_A+k)^2\simeq2p_A^+k^--2p_{A,T}\cdot k_T-k_T^2$.
- **Status:** algebra V; power counting [A] (5b).
- **Source:** c_wilson §6.3.
- **Used in:** `def:method-soft-approx`, `lem:method-soft-accuracy`, `def:ir-glauber`.

### VF-WL-12 — Glauber（Coulomb）相位与单交换积分
$$\frac1{k^-+i0}-\frac1{k^--i0}=-2\pi i\,\delta(k^-),\qquad \int_{-\infty}^{\infty}\!dk^-\frac{1}{(k^-+i0)(-k^++i0)(2k^+k^--k_T^2+i0)}=\begin{cases}0,&k^+>0,\\[2pt]-\dfrac{2\pi i}{k_T^2\,k^+},&k^+<0.\end{cases}$$
- **Status:** V (c_glauber [P3a–d]; BP E7.24).
- **Source:** c_glauber §1.4; c_wilson s6.
- **Used in:** `prop:method-glauber-oneloop`, `thm:tmd-sivers-sign`, `ex:power-sgp`.

### VF-WL-13 — 半无限 Wilson 线的 Ward 恒等式
$$\sum_{\rm insertions}=-gT_qY+g\sum_pZ_p\big(\dots[T_q,T_{p+1}]\dots\big)$$
- **Status:** V (2c).
- **Source:** c_wilson §3.5.
- **Used in:** App B, App F.

---------------------------------------------------------------------------------------------------

## DIS — deep-inelastic scattering at one loop

Normalization:
$$\frac{F_2}x=\sum_qe_q^2\Big\{q+\bar q+\frac{\alpha_s}{2\pi}\big[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g\big]\Big\},\qquad \frac{F_L}x=\sum_qe_q^2\frac{\alpha_s}{2\pi}\big[C_L^q\otimes(q+\bar q)+2C_L^g\otimes g\big].$$
The factor 2 counts the quark and the antiquark.

### VF-DIS-1 — Born（精确到 $D$ 维）
$$\frac{\hat F_2^{(0)}}z=e_q^2\delta(1-z),\qquad \hat F_L^{(0)}=0\quad\Rightarrow\quad F_2=\sum_qe_q^2x(q+\bar q),\ F_1=\tfrac12\sum_qe_q^2(q+\bar q),\ F_L=0\ (\text{LO}).$$
- **Status:** V.
- **Source:** c_dis §3.
- **Used in:** `ex:intro-handbag`.

### VF-DIS-2 — $D$ 维投影算符
$$\frac{F_L}x=\frac{8x^2}{Q^2}P_\mu P_\nu W^{\mu\nu},\qquad \frac{F_2}x=\frac1{1-\varepsilon}\Big[-g_{\mu\nu}+(3-2\varepsilon)\frac{4x^2}{Q^2}P_\mu P_\nu\Big]W^{\mu\nu}.$$
Massive target, with $\rho^2=1+4x^2M^2/Q^2$: $F_L=\rho^2F_2-2xF_1$, $F_L/x=\frac{8x^2}{Q^2\rho^2}PWP$, and $\rho^2F_2/x=[2(-gW)+(D-1)F_L/x]/(D-2)$.
- **Status:** V.
- **Source:** c_dis §2.
- **Used in:** `def:disall-breit`.

### VF-DIS-3 — 虚修正对 DIS 的贡献
$$\frac{\hat F_2^{q,\rm V}}{ze_q^2}=2F^{(1)}\delta(1-z)=\frac{\alpha_s}{2\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\Big[-\frac2{\varepsilon^2}-\frac3\varepsilon-8+\zeta_2+O(\varepsilon)\Big]\delta(1-z)$$
There is no virtual contribution to $F_L$.
- **Status:** V.
- **Source:** c_dis §4.

### VF-DIS-4 — 夸克道实辐射（精确到 $\varepsilon$）
$$R_2^q=\frac{e^{\varepsilon\gamma_E}\Gamma(-\varepsilon)}{2\Gamma(2-2\varepsilon)}z^{\varepsilon}(1-z)^{-1-\varepsilon}\big[2(1+z^2)-\varepsilon(7-2z)+\varepsilon^2\big],\qquad R_L^q=\frac{e^{\varepsilon\gamma_E}\Gamma(2-\varepsilon)}{\Gamma(2-2\varepsilon)}2z\Big(\frac z{1-z}\Big)^{\varepsilon},$$
$$R_2^q=\frac{2\delta}{\varepsilon^2}+\frac1\varepsilon\Big[-2\mathcal D_0+1+z+\frac32\delta\Big]+2\mathcal D_1-\frac32\mathcal D_0-(1+z)\ln(1-z)-\frac{1+z^2}{1-z}\ln z+3+2z+\Big(\frac72-3\zeta_2\Big)\delta+O(\varepsilon).$$
Normalization: $\hat F^{q,\rm R}_a/(ze_q^2)=\frac{\alpha_s}{2\pi}C_F(\mu^2/Q^2)^\varepsilon R_a^q$.
- **Status:** V.
- **Source:** c_dis §5.3–5.4.

### VF-DIS-5 — 光子—胶子融合（精确到 $\varepsilon$）
$$R_2^g=\frac{2e^{\varepsilon\gamma_E}\Gamma(-\varepsilon)}{\Gamma(2-2\varepsilon)}\Big(\frac z{1-z}\Big)^{\varepsilon}\frac{z^2+(1-z)^2-3\varepsilon+4\varepsilon^2-2\varepsilon^3}{(1-\varepsilon)^2},\qquad R_L^g=\frac{e^{\varepsilon\gamma_E}\Gamma(1-\varepsilon)}{\Gamma(2-2\varepsilon)}\frac{8z(1-z)}{1-\varepsilon}\Big(\frac z{1-z}\Big)^{\varepsilon},$$
$$R_2^g=-\frac2\varepsilon\big[z^2+(1-z)^2\big]+2\Big\{\big[z^2+(1-z)^2\big]\ln\frac{1-z}z-8z^2+8z-1\Big\}+O(\varepsilon).$$
Normalization: $\hat F^g_a/(ze_q^2)=\frac{\alpha_s}{2\pi}T_F(\mu^2/Q^2)^\varepsilon R_a^g$.
- **Status:** V.
- **Source:** c_dis §6.
- **Used in:** `ex:disall-gluon`.

### VF-DIS-6 — 极点结构与 $\overline{\rm MS}$ 质量因子化
$$\frac{\hat F_2^q}{ze_q^2}=\delta(1-z)+\frac{\alpha_s}{2\pi}\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\Big[-\frac1\varepsilon P_{qq}+C_2^q+O(\varepsilon)\Big],\qquad \frac{\hat F_2^g}{ze_q^2}=\frac{\alpha_s}{2\pi}\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\Big[-\frac2\varepsilon P_{qg}+2C_2^g\Big].$$
Pole bookkeeping:
- $1/\varepsilon^2$: $2-2=0$;
- $1/\varepsilon$: $-P_{qq}/C_F$, including the $\frac32\delta$ from the virtual graph;
- $\delta$ coefficient: $\frac72-3\zeta_2-8+\zeta_2=-(\frac92+\frac{\pi^2}3)$.

Partonic PDFs: VF-PDF-5. In subtraction language: $C_A\Gamma^{(1)}=f^{(1)}_{q/q}\otimes{\rm Born}=-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}$ and $C_H\Gamma^{(1)}=\frac{\alpha_s}{2\pi}C_2^q$.
- **Status:** V.
- **Source:** c_dis §7.
- **Used in:** `prop:disall-nlo`, `ex:method-dis-oneloop`.

### VF-DIS-7 — $\overline{\rm MS}$ 系数函数
At $\mu=Q$:
$$C_2^q=C_F\Big[2\mathcal D_1-\frac32\mathcal D_0-(1+z)\ln(1-z)-\frac{1+z^2}{1-z}\ln z+3+2z-\Big(\frac92+\frac{\pi^2}3\Big)\delta(1-z)\Big],$$
$$C_2^g=T_F\Big[\big(z^2+(1-z)^2\big)\ln\frac{1-z}z-8z^2+8z-1\Big],\qquad C_L^q=2C_Fz,\qquad C_L^g=4T_Fz(1-z).$$
General $\mu$: $C_2^i(z,Q^2/\mu^2)=C_2^i(z)+\ln(Q^2/\mu^2)P_{qi}(z)$. $C_L$ has no $\mu$ dependence at this order.
- **Status:** VL (cross-checked with `Vermaseren:2005qc`, `Moch:2004xu`; VF-DIS-12).
- **Source:** c_dis §0, §8.
- **Used in:** `prop:disall-nlo`, `thm:pdf-dis-xspace`.

### VF-DIS-8 — Mellin 矩（单位 $\alpha_s/2\pi$）
$$C^q_{2,N}=C_F\Big[S_1^2-S_2+\frac32S_1-\frac{S_1}{N(N+1)}+\frac3{2N}+\frac2{N+1}+\frac1{N^2}-\frac92\Big],\qquad C^g_{2,N}=T_F\Big[-\frac{N^2+N+2}{N(N+1)(N+2)}S_1+\frac1{N^2}-\frac1N+\frac6{(N+1)(N+2)}\Big],$$
$$C^q_{L,N}=\frac{2C_F}{N+1},\qquad C^g_{L,N}=\frac{4T_F}{(N+1)(N+2)},\qquad P_{qq,N}=C_F\Big[\frac32+\frac1{N(N+1)}-2S_1\Big],\qquad P_{qg,N}=T_F\frac{N^2+N+2}{N(N+1)(N+2)} .$$
Table, $N=1,\dots,8$:

| $N$ | $C^q_{2,N}/C_F$ | $C^g_{2,N}/T_F$ |
|---|---|---|
| 1 | 0 | $\frac13$ |
| 2 | $\frac16$ | $-\frac14$ |
| 3 | $\frac{29}{24}$ | $-\frac7{20}$ |
| 4 | $\frac{91}{40}$ | $-\frac{133}{360}$ |
| 5 | $\frac{589}{180}$ | $-\frac{23}{63}$ |
| 6 | $\frac{5281}{1260}$ | $-\frac{1777}{5040}$ |
| 7 | $\frac{50791}{10080}$ | $-\frac{27}{80}$ |
| 8 | $\frac{58703}{10080}$ | $-\frac{16231}{50400}$ |

MVV normalization: $c^{(1)}_{2,q}(N)=2C^q_{2,N}=C_F[2S_1^2-2S_2+3S_1-\frac{2S_1}{N(N+1)}+\frac3N+\frac4{N+1}+\frac2{N^2}-9]$. A commonly quoted variant with $\frac2{N+1}+\frac1{N^2}$ **fails** the Adler check (critic c2).
- **Status:** VL.
- **Source:** c_dis §11; critic c2.
- **Used in:** `prop:dis-c-oneloop`, `lem:appA-mellin-table`.

### VF-DIS-9 — 等价形式与 $C_1$
$$C_2^q=C_F\Big[\frac{1+z^2}{1-z}\Big(\ln\frac{1-z}z-\frac34\Big)+\frac{9+5z}4\Big]_+\ (\text{whole-bracket plus}),\qquad C_1^i=C_2^i-C_L^i .$$
- **Status:** V.
- **Source:** c_dis §8.

### VF-DIS-10 — 标度依赖
$$\frac{\partial}{\partial\ln\mu_F^2}\frac{F_2}x=O(a^2),\qquad \frac{\partial F_2}{\partial\ln\mu_R^2}=-\frac{\beta_0}2a^2\sum_qe_q^2\big[C_2^q\otimes(q+\bar q)+2C_2^g\otimes g\big],\qquad a=\frac{\alpha_s}{2\pi}.$$
$F_L$ is $\mu$-independent at $O(a)$.
- **Status:** V.
- **Source:** c_dis §9.
- **Used in:** `prop:disall-scale`.

### VF-DIS-11 — DIS 方案
$$q_i^{\rm DIS}=q_i+a\big[C_2^q\otimes q_i+C_2^g\otimes g\big],\qquad g^{\rm DIS}=g-a\big[C_2^q\otimes\Sigma+2n_fC_2^g\otimes g\big],\qquad P^{(1),\rm DIS}_{\rm NS}=P^{(1),\overline{\rm MS}}_{\rm NS}-\frac{\beta_0}2C_2^q,$$
$$P'^{(1)}=P^{(1)}+Z\otimes P^{(0)}-P^{(0)}\otimes Z-\frac{\beta_0}2Z,\qquad Z=\begin{pmatrix}C_2^q&2n_fC_2^g\\-C_2^q&-2n_fC_2^g\end{pmatrix}\ \text{in the }(\Sigma,g)\text{ basis}.$$
$C_L$ is scheme independent at $O(\alpha_s)$.
- **Status:** V. The attribution of the gluon choice to `DiemozEtAl1988` was recalled by c_dis and not re-checked: cite with "参见".
- **Source:** c_dis §10.
- **Used in:** `prop:disall-dis-scheme`, `rem:pdf-schemes`.

### VF-DIS-12 — 文献换算
$c^{(1)}_{2,\rm ns}=2C_2^q$ and $c^{(1)}_{2,g}=4n_fC_2^g$ (MVV normalization $a_s=\alpha_s/4\pi$).
- **Status:** VL.
- **Source:** c_dis §12.

### VF-DIS-13 — 单圈 OPE 检验
- The Taylor coefficients in $\omega$ of the hard-region forward Compton amplitude of an on-shell parton equal the Mellin moments of the bare cut results, **exactly in $\varepsilon$**. This holds for $N=1..8$ for the quark ($F_2$, $F_L$) and for even $N\le8$ for the gluon.
- The renormalized Wilson coefficients reproduce VF-DIS-8. The residues are $-P_{qq,N}$ and $-P_{qg,N}$, and no $1/\varepsilon^2$ survives.
- **Status:** V (`ope_check.py`, `ope_wilson.py`).
- **Source:** c_dis §11.
- **Used in:** `thm:dis-ope`, `prop:dis-wilson-partons`, `cor:disall-consistency`.

### VF-DIS-14 — Adler 与 Bjorken $\nu$ 求和规则
$C^q_{2,1}=0$, which is the Adler sum rule ($\int_0^1C_2^q=0$). From $C^q_{L,1}=C_F$ it follows that $C^q_{1,1}=C^q_{2,1}-C^q_{L,1}=-C_F$, the Bjorken $\nu$ sum rule.
- **Status:** V.
- **Source:** c_dis §11 table; critic c2.
- **Used in:** `prop:dis-c-oneloop`.

---------------------------------------------------------------------------------------------------

## PDF — operator definitions, one loop, DGLAP

### VF-PDF-1 — 自由场值与反夸克
$$f_{q/H}(\xi)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c\ \Rightarrow\ f^{(0)}_{q/q}=\delta(1-\xi),\quad f^{(0)}_{q/\bar q}=-\delta(1+\xi),$$
$$f_{\bar q}(\xi)=-f_q(-\xi).$$
The antiquark relation is equivalent to the definition with $\psi^c=C\bar\psi^{\mathsf T}$ and $W^*$. For $x>0$: $q(x)=f_q(x)$ and $\bar q(x)=-f_q(-x)$.
- **Status:** VL (`CollinsSoper1982a`; Collins 2011 §7.5).
- **Source:** c_pdf §2.1–2.2.
- **Used in:** `def:pdf-quark`, `def:pdf-antiquark`, `prop:pdf-invariance`.

### VF-PDF-2 — 胶子分布
$$f_{g/H}(\xi)=\sum_j\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_a(w)W^{(A)}_{ab}[w,0]G^{+j}_b(0)|P\rangle_c,\qquad f^{(0)}_{g/g}=\delta(1-\xi)-\delta(1+\xi),\qquad \langle k|T^{++}_g|k\rangle=2(k^+)^2 .$$
$f_g(-\xi)=-f_g(\xi)$. The index $j$ runs over $D-2$ transverse values.
- **Status:** V.
- **Source:** c_pdf §2.3; BP §0.4(5).
- **Used in:** `def:pdf-gluon`.

### VF-PDF-3 — Feynman 规范下由算符定义计算的单圈 $f_{q/q}$（胶子质量 $m$）
$$f_R=A_\varepsilon\Big[(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}+\frac{2\xi^{1-\varepsilon}}{1-\xi}\Big],\qquad A_\varepsilon=\frac{\alpha_s}{2\pi}C_Fe^{\varepsilon\gamma_E}\Gamma(\varepsilon)\Big(\frac{\mu^2}{m^2}\Big)^{\varepsilon},\qquad \frac{V_1+V_1^\dagger}{\rm tree}=-A_\varepsilon\int_0^1dx\frac{2x^{1-\varepsilon}}{1-x},$$
$$\Sigma_V(0)=-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon},\qquad \langle f^{(1)}_{\rm bare},h\rangle=A_\varepsilon\Big\{\int_0^1\!d\xi\Big[(1-\varepsilon)^2(1-\xi)\xi^{-\varepsilon}h+\frac{2\xi^{1-\varepsilon}}{1-\xi}(h-h(1))\Big]-\frac{1-\varepsilon}{2-\varepsilon}h(1)\Big\},$$
$$f^{(1)}_{q/q}(\xi;\mu)=\frac{\alpha_s}{2\pi}\Big\{P_{qq}(\xi)\ln\frac{\mu^2}{m^2}+C_F\Big[-(1-\xi)(2+\ln\xi)-\Big[\frac{2\xi\ln\xi}{1-\xi}\Big]_++\frac14\delta(1-\xi)\Big]\Big\}\quad(\text{regulator dependent}).$$
UV poles graph by graph, in units $\frac{\alpha_s}{2\pi}\frac{C_F}\varepsilon$:
- ladder: $(1-\xi)$;
- Wilson line: $[\frac{2\xi}{1-\xi}]_+$;
- self-energy: $-\frac12\delta$;
- sum: $P_{qq}/C_F$.

Quark number is conserved exactly in $\varepsilon$. The light-cone-gauge ladder alone gives the $D$-dimensional kernel $\hat P_{qq}$.
- **Status:** V (s2).
- **Source:** c_pdf §3.1–3.5.
- **Used in:** `prop:pdf-pqq-operator`, `ex:pdf-oneloop`.

### VF-PDF-4 — 重整化约定
$$f_{\rm ren}=Z\otimes f_{\rm bare},\qquad Z_{qq}(x)=\delta(1-x)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{qq}(x)+O(\alpha_s^2),\qquad \frac{dZ}{d\ln\mu^2}Z^{-1}=\frac{\alpha_s}{2\pi}P+O(\alpha_s^2).$$
The opposite convention, $f_{\rm bare}=Z'\otimes f_{\rm ren}$, has $Z'=\delta+\frac{\alpha_s}{2\pi}\frac1\varepsilon P$.
- **Status:** V.
- **Source:** c_pdf §3.5 (2a).
- **Used in:** `def:pdf-quark`, `thm:pdf-dglap`.

### VF-PDF-5 — 纯维数正规化中的部分子 PDF
$$\int\frac{d^{2-2\varepsilon}l_T}{l_T^2}=\pi^{1-\varepsilon}\Gamma(1+\varepsilon)M^{-2\varepsilon}\Big(\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}\Big)=0,\qquad f^{\rm bare}_{i/j}=\delta_{ij}\delta(1-\xi),\qquad f_{i/j}=\delta_{ij}\delta(1-\xi)-\frac{\alpha_s}{2\pi}\frac1\varepsilon P_{ij}(\xi)+O(\alpha_s^2).$$
After renormalization the surviving $\varepsilon$ is an IR pole.
- **Status:** V.
- **Source:** c_pdf §3.6; c_dis §7.
- **Used in:** `prop:pdf-partonic-dr`.

### VF-PDF-6 — $D$ 维实辐射核（CDR 平均）
$$\hat P_{qq}=C_F\Big[\frac{1+z^2}{1-z}-\varepsilon(1-z)\Big],\quad \hat P_{gq}=C_F\Big[\frac{1+(1-z)^2}z-\varepsilon z\Big],\quad \hat P_{qg}=T_F\Big[1-\frac{2z(1-z)}{1-\varepsilon}\Big],\quad \hat P_{gg}=2C_A\Big[\frac z{1-z}+\frac{1-z}z+z(1-z)\Big].$$
- **Status:** VL (Catani–Seymour 1997).
- **Source:** c_pdf §4.1.
- **Used in:** `prop:pdf-lo-kernels`, `ex:pdf-quark-in-gluon`.

### VF-PDF-7 — 领头阶分裂函数
$$P_{qq}=C_F\Big[\frac{1+z^2}{1-z}\Big]_+,\quad P_{qg}=T_F\big[z^2+(1-z)^2\big],\quad P_{gq}=C_F\frac{1+(1-z)^2}z,\quad P_{gg}=2C_A\Big[\frac z{(1-z)_+}+\frac{1-z}z+z(1-z)\Big]+\frac{\beta_0}2\delta(1-z),$$
$$\frac{d}{d\ln\mu^2}\binom\Sigma g=\frac{\alpha_s}{2\pi}\begin{pmatrix}P_{qq}&2n_fP_{qg}\\P_{gq}&P_{gg}\end{pmatrix}\otimes\binom\Sigma g .$$
Here $\frac{z}{(1-z)_+}$ means $z[\frac1{1-z}]_+$. Sum rules: $\int_0^1P_{qq}=0$; $\int_0^1z[P_{gg}+2n_fP_{qg}]=0$; $\int_0^1z[P_{qq}+P_{gq}]=0$.
- **Status:** VL (Altarelli–Parisi 1977).
- **Source:** c_pdf §4.2; critic c1.
- **Used in:** `prop:pdf-lo-kernels`.

### VF-PDF-8 — 反常维度（DGLAP 归一化）
$$\gamma_{qq}(N)=C_F\Big[\frac32+\frac1{N(N+1)}-2S_1(N)\Big],\quad \gamma_{qg}(N)=T_F\frac{N^2+N+2}{N(N+1)(N+2)},\quad \gamma_{gq}(N)=C_F\frac{N^2+N+2}{(N-1)N(N+1)},$$
$$\gamma_{gg}(N)=2C_A\Big[\frac1{N(N-1)}+\frac1{(N+1)(N+2)}-S_1(N)\Big]+\frac{\beta_0}2 .$$
Large $N$: $\gamma_{qq}\to-2C_F(\ln N+\gamma_E)+\frac32C_F$.
- **Status:** VL.
- **Source:** c_pdf §4.3; critic c1.
- **Used in:** `prop:pdf-lo-kernels`, `prop:dis-ope-rg`.

### VF-PDF-9 — $N=2$ 单态矩阵
$$\begin{pmatrix}\gamma_{qq}&2n_f\gamma_{qg}\\\gamma_{gq}&\gamma_{gg}\end{pmatrix}_{N=2}=\begin{pmatrix}-\frac43C_F&\frac23n_fT_F\\\frac43C_F&-\frac23n_fT_F\end{pmatrix}$$
The eigenvalues are $0$ and $-\frac{4C_F+2n_fT_F}3$. For SU(3), $\langle x\rangle_\Sigma\to\frac{3n_f}{16+3n_f}$. Non-singlet LO evolution: $M_n^{\rm NS}(Q^2)=M_n^{\rm NS}(Q_0^2)[\alpha_s(Q^2)/\alpha_s(Q_0^2)]^{-2\gamma_{qq}(n)/\beta_0}$.
- **Status:** VL (Gross–Wilczek 1974).
- **Source:** c_pdf §4.3 (3d, 5b).
- **Used in:** `cor:dis-scaling`, `ex:dis-n2`.

### VF-PDF-10 — 约定换算表
| convention | relation to ours |
|---|---|
| ours = ESW: $P=\frac{\alpha_s}{2\pi}P^{(0)}+\dots$ | identical |
| MVV: $a_s=\alpha_s/4\pi$, $\gamma^{(n)}=-\int x^{N-1}P^{(n)}$ | $P^{(0)}_{\rm MVV}=2P$, $\gamma^{(0)}_{\rm MVV}=-2\gamma$ |
| operator (GW/GP): $\mu\,dO_N/d\mu=-\gamma_OO_N$ | $\gamma_O=-\frac{\alpha_s}\pi\gamma(N)$ |
| local operators, App L / Ch8 (v1: Ch7): $\frac{dO}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\Gamma O$ | $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$ |
- **Status:** VL (MVV eqs. (2.6), (2.7), (3.4) read).
- **Source:** c_pdf §4.4.
- **Used in:** `prop:dis-ope-rg`, `prop:pdf-lo-kernels`.

### VF-PDF-11 — PDF 的矩 = 定域算符矩阵元
$$a_n=\int_{-1}^1d\xi\,\xi^{n-1}f_q(\xi)=\frac{\langle P|\bar\psi\gamma^+(iD^+)^{n-1}\psi|P\rangle}{2(P^+)^n}=\int_0^1dx\,x^{n-1}\big[q+(-1)^n\bar q\big],\qquad \int_0^1dx\,x^{n-1}g(x)=\frac{\langle P|O_g^{(n)}|P\rangle}{2(P^+)^n}\ (n\text{ even}).$$
Here $O_g^{(n)}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$. Left- and right-acting derivatives agree only in forward matrix elements.
- **Status:** V (s4(a)–(d)).
- **Source:** c_pdf §5.1–5.3.
- **Used in:** `thm:pdf-moments-local`, `prop:appL-bare`.

### VF-PDF-12 — 光线算符顶点的矩
$$\frac{g\,t^an^\mu\gamma^+}{2q^+}\big[\delta(\xi P^+-k_2^+)-\delta(\xi P^+-k_1^+)\big]\ \xrightarrow{\ n\text{-th moment}\ }\ \frac1{2(P^+)^n}\Big[g\,t^an^\mu\gamma^+\sum_{j=0}^{n-2}(k_2^+)^j(k_1^+)^{n-2-j}\Big],\qquad k_2=k_1+q.$$
The right-hand side is the one-gluon vertex of $\bar\psi\gamma^+(iD^+)^{n-1}\psi$. At second order one gets second divided differences. Checked for $n\le7$.
- **Status:** V (s4(b)).
- **Source:** c_pdf §5.4.
- **Used in:** `lem:pdf-wilson-moments`, `lem:appL-divided-differences`, `def:dis-twist`.

### VF-PDF-13 — 单圈矩：精确到 $\varepsilon$ 的逐图对应
| PDF graph | local-operator graph | $n$-th moment |
|---|---|---|
| ladder R1 | vertex | $A_\varepsilon\frac{(1-\varepsilon)^2}{(n-\varepsilon)(n+1-\varepsilon)}$ |
| Wilson line R2+V1 | operator–gluon graphs | $-2A_\varepsilon\sum_{i=1}^{n-1}\frac1{i+1-\varepsilon}$ |
| V2 | self-energy | $-A_\varepsilon\frac{1-\varepsilon}{2-\varepsilon}$ |

The total is $0$ for $n=1$ and $-\frac{4A_\varepsilon}{3-\varepsilon}$ for $n=2$, whose pole is $\frac{\alpha_s}{2\pi}\frac{\gamma_{qq}(2)}\varepsilon$.
- **Status:** V (s4(e)).
- **Source:** c_pdf §5.4.
- **Used in:** `thm:pdf-moments-local`, `ex:pdf-moments-exact`, `prop:appL-renormalized`.

### VF-PDF-14 — 场重整化常数与定域算符反常维度
$$\delta Z_2=-\frac{\alpha_s}{4\pi}\frac{C_F\xi_g}\varepsilon,\qquad \delta Z_3=\frac{\alpha_s}{4\pi}\frac1\varepsilon\Big[\Big(\frac{13}6-\frac{\xi_g}2\Big)C_A-\frac43T_Fn_f\Big].$$
The local operators give $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$ for $N=2,4,\dots,14$. All $\Gamma_{ij}$ are independent of the gauge parameter; the per-graph $\xi_g$ dependence is tabulated in c_pdf §6.4. At $N=2$ the columns sum to zero ($T^{++}$ is conserved).
- **Status:** VL (Peskin–Schroeder ch. 16; GW/GP).
- **Source:** c_pdf §6.
- **Used in:** `prop:pdf-local-anomalous`, `prop:prelim-beta`.

### VF-PDF-15 — 偶数矩唯一性与延拓
- **Thm 7.2.** If $x^{2k_0}g\in L^1$ and $\int_0^1x^{2k}g=0$ for all $k\ge k_0$, then $g=0$ a.e.
- **Cor 7.3.** Even moments $N\ge N_1$ determine $q+\bar q$ and $g$; odd moments determine $q-\bar q$.
- **Prop 7.5.** For $P=r+a[\frac1{1-x}]_++b\delta$ with $|r|\le C/x$: vanishing even moments imply $a=b=0$ and $r=0$.
- **Prop 7.7.** If $F$ is holomorphic for ${\rm Re}\,z>\sigma_0$ with $|F|\le C(1+|z|)^m$ and vanishes on an arithmetic progression, then $F\equiv0$.
- **Hilbert-matrix condition number:** ${\rm cond}_2\approx e^{3.5K}$.
- **Status:** V (complete proofs; s6 15/15).
- **Source:** c_pdf §7.
- **Used in:** `thm:appK-even-moments`, `cor:appK-pdf`, `prop:appK-kernels`, `prop:appK-continuation`, `rem:dis-uniqueness`.

---------------------------------------------------------------------------------------------------

## DY — Drell–Yan at one loop

Normalization:
- $\sigma_0=\dfrac{4\pi\alpha^2}{3N_cQ^2}$ and $a=\alpha_s(\mu_R)/2\pi$;
- $\hat s\,\dfrac{d\hat\sigma_{ij}}{dQ^2}=\sigma_0e_q^2\Delta_{ij}(z)$, with $z=Q^2/\hat s$ and $\tau=Q^2/s$;
- $\Delta_{qg}$ is per one quark (or antiquark) and one gluon.

### VF-DY-1 — 领头阶
$$\frac{d\sigma}{dQ^2}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_qe_q^2\int_0^1dx_1dx_2\,\delta(x_1x_2-\tau)\big[q(x_1)\bar q(x_2)+\bar q(x_1)q(x_2)\big],$$
$$\frac{d^2\sigma}{dQ^2dy}=\frac{4\pi\alpha^2}{3N_cQ^2s}\sum_qe_q^2\big[q(x_1)\bar q(x_2)+\bar q(x_1)q(x_2)\big],\qquad x_{1,2}=\sqrt\tau e^{\pm y},$$
$$\hat\sigma(q\bar q\to\ell^+\ell^-)=\frac{4\pi\alpha^2e_q^2}{3N_c\hat s}.$$
- **Status:** VL.
- **Source:** c_dy §0, §2; BP §18.3.
- **Used in:** `prop:dy-born`, `thm:tmd-factorization` ($\sigma_0$).

### VF-DY-2 — 主公式
$$\hat s\frac{d\hat\sigma}{dQ^2}=\frac{2\alpha^2}{3Q^2}\int d\Phi_{\gamma^*X}\big\langle-g_{\mu\nu}H^\mu H^{\nu*}\big\rangle,\qquad \int d\Phi_2L_{\mu\nu}=\frac1{6\pi}(q_\mu q_\nu-q^2g_{\mu\nu}),\qquad \Delta^{\rm bare}_{ij}=\frac{N_c}{2\pi e_q^2(1-\varepsilon)}\int d\Phi^{(D)}_{\gamma^*X}\langle-gHH^*\rangle .$$
- **Status:** V.
- **Source:** c_dy §1.2–1.4.
- **Used in:** `def:dy-kin`.

### VF-DY-3 — $D$ 维矩阵元
$$T_{q\bar q}=8(1-\varepsilon)\Big[(1-\varepsilon)\Big(\frac{\hat u}{\hat t}+\frac{\hat t}{\hat u}\Big)+\frac{2\hat sQ^2}{\hat t\hat u}-2\varepsilon\Big],\qquad T_{qg}=-8(1-\varepsilon)\Big[(1-\varepsilon)\Big(\frac{\hat s}{\hat t}+\frac{\hat t}{\hat s}\Big)+\frac{2\hat uQ^2}{\hat s\hat t}-2\varepsilon\Big].$$
The colour factors are $C_FN_c$ and $T_F(N_c^2-1)$ respectively.
- **Status:** V (crossing; explicit spinors to $10^{-15}$).
- **Source:** c_dy §3.1.

### VF-DY-4 — $D$ 维两体相空间
$$d\Phi_2=\frac1{8\pi}\Big(\frac{4\pi}{\hat s}\Big)^{\varepsilon}\frac{(1-z)^{1-2\varepsilon}}{\Gamma(1-\varepsilon)}[v(1-v)]^{-\varepsilon}dv .$$
- **Status:** V.
- **Source:** c_dy §3.2.
- **Used in:** `lem:appC-phase-space`.

### VF-DY-5 — 实辐射（精确到 $\varepsilon$）
With $K_r=e^{\varepsilon\gamma_E}\Gamma(1-\varepsilon)/\Gamma(1-2\varepsilon)$:
$$\Delta^R_{q\bar q}=-\frac{\alpha_s}{2\pi}\frac{2C_F}\varepsilon\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}K_r\,z^\varepsilon(1-z)^{-1-2\varepsilon}\Big[1+z^2+\frac{2\varepsilon^2(1-z)^2}{1-2\varepsilon}\Big],$$
$$\Delta^R_{qg}=-\frac{\alpha_s}{2\pi}\frac{T_F}{2\varepsilon}\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}K_r\,z^\varepsilon(1-z)^{-2\varepsilon}\frac{2(z^2+(1-z)^2)-\varepsilon(5z^2-6z+7)+\varepsilon^2(1+z)^2}{(1-\varepsilon)(1-2\varepsilon)} .$$
- **Status:** V.
- **Source:** c_dy §3.3.

### VF-DY-6 — 虚修正（类时）
With $K_v=e^{\varepsilon\gamma_E}\Gamma(1+\varepsilon)\Gamma^2(1-\varepsilon)/\Gamma(1-2\varepsilon)$:
$$F^{(1)}=\frac{\alpha_s}{4\pi}C_F\Big(\frac{\mu^2}{-q^2-i0}\Big)^{\varepsilon}f(\varepsilon),\qquad f=-K_v\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)},\qquad \Delta^V=\frac{\alpha_s}{2\pi}C_F\Big(\frac{\mu^2}{Q^2}\Big)^{\varepsilon}\cos(\pi\varepsilon)f(\varepsilon)\,\delta(1-z).$$
- **Status:** VL (MVV 2005 through $\varepsilon^4$).
- **Source:** c_dy §3.4.

### VF-DY-7 — Laurent 展开表
Units $a=\alpha_s/2\pi$, $L=\ln(\mu^2/Q^2)$:

| piece | $\varepsilon^{-2}$ | $\varepsilon^{-1}$ | $\varepsilon^0$ |
|---|---|---|---|
| real $q\bar q$ | $2C_F\delta$ | $2C_FL\delta-4C_F\mathcal D_0+2C_F(1+z)$ | $C_F(L^2-\frac{\pi^2}2)\delta-4C_FL\mathcal D_0+8C_F\mathcal D_1+2C_F(1+z)L-4C_F(1+z)\ln(1-z)-2C_F\frac{1+z^2}{1-z}\ln z$ |
| virtual | $-2C_F\delta$ | $-C_F(3+2L)\delta$ | $C_F(-L^2-3L-8+\frac{7\pi^2}6)\delta$ |
| real $qg$ | — | $-P_{qg}$ | $T_F[(z^2+(1-z)^2)\ln\frac{(1-z)^2}z+\frac{1+6z-7z^2}2]-P_{qg}L$ |

The remaining pole of real + virtual is $-\frac2\varepsilon P_{qq}$.
- **Status:** V.
- **Source:** c_dy §3.5.

### VF-DY-8 — $\overline{\rm MS}$ 系数函数
$$\Delta_{q\bar q}=\delta(1-z)+\frac{\alpha_s}{2\pi}\Big\{C_F\Big[4(1+z^2)\mathcal D_1-2\frac{1+z^2}{1-z}\ln z+\Big(\frac{2\pi^2}3-8\Big)\delta(1-z)\Big]+2P_{qq}(z)\ln\frac{Q^2}{\mu_F^2}\Big\},$$
$$\Delta_{qg}=\frac{\alpha_s}{2\pi}\Big\{T_F\Big[\big(z^2+(1-z)^2\big)\ln\frac{(1-z)^2}z+\frac12+3z-\frac72z^2\Big]+P_{qg}(z)\ln\frac{Q^2}{\mu_F^2}\Big\},$$
$$\frac{d\sigma}{dQ^2}=\frac{\sigma_0}s\sum_qe_q^2\int dx_1dx_2dz\,\delta(x_1x_2z-\tau)\Big\{[q\bar q+\bar qq]\Delta_{q\bar q}+[g(q+\bar q)+(q+\bar q)g]\Delta_{qg}\Big\}.$$
$(1+z^2)\mathcal D_1$ uses the product convention. There is no $\mu_R$ dependence at this order.
- **Status:** VL (agrees with `Duhr:2020sdp` ancillary files, including the $\mu_F$ terms).
- **Source:** c_dy §0, §6.1.
- **Used in:** `prop:dy-nlo`.

### VF-DY-9 — $\overline{\rm MS}$ 质量因子化
$$\Gamma_{ki}(x)=\delta_{ki}\delta(1-x)-\frac{\alpha_s}{2\pi}\frac1\varepsilon\Big(\frac{\mu^2}{\mu_F^2}\Big)^{\varepsilon}P_{ki}(x),\qquad \Delta_{q\bar q}=\Delta^{\rm bare}_{q\bar q}+2a\tfrac1\varepsilon\Big(\frac{\mu^2}{\mu_F^2}\Big)^{\varepsilon}P_{qq},\qquad \Delta_{qg}=\Delta^{\rm bare}_{qg}+a\tfrac1\varepsilon\Big(\frac{\mu^2}{\mu_F^2}\Big)^{\varepsilon}P_{qg}.$$
In the $qg$ channel the subtraction is $f_{\bar q/g}\otimes\hat\sigma_{q\bar q}$.
- **Status:** V.
- **Source:** c_dy §3.6.

### VF-DY-10 — DIS 方案与 PDF 的普适性
$$\Delta^{\rm DIS}_{q\bar q}=C_F\Big[\Big(1+\frac{4\pi^2}3\Big)\delta(1-z)+2(1+z^2)\mathcal D_1+3\mathcal D_0-6-4z\Big],\qquad \Delta^{\rm DIS}_{qg}=T_F\Big[(z^2+(1-z)^2)\ln(1-z)+\frac32-5z+\frac92z^2\Big],$$
$$\Delta^{\overline{\rm MS}}_{q\bar q}-2C_2^q=\Delta^{\rm DIS}_{q\bar q},\qquad \Delta^{\overline{\rm MS}}_{qg}-C_2^g=\Delta^{\rm DIS}_{qg}\quad(\text{to }10^{-30}).$$
- **Status:** V (critic c2). These are the commonly quoted DIS-scheme forms; the original AEM 1979 paper was not read.
- **Source:** c_dy §3.7.
- **Used in:** `rem:dy-dis-scheme`.

### VF-DY-11 — $\mu_F$ 无关性
$d\sigma/d\ln\mu_F^2=O(\alpha_s^2)$, exactly in Mellin space; numerically in $x$ space to $10^{-13}$.
- **Status:** V (4/4).
- **Source:** c_dy §5.
- **Used in:** `prop:dy-scale`.

### VF-DY-12 — 乘积约定与整体加号的差别
$$(1+z^2)\mathcal D_1=\Big[\frac{(1+z^2)\ln(1-z)}{1-z}\Big]_++\frac74\delta(1-z),\qquad\text{so }4C_F(1+z^2)\mathcal D_1\text{ vs. whole-term plus differ by }7C_F\,\delta(1-z).$$
Derivation: $-\int_0^1(1+z)\ln(1-z)\,dz=\frac74$. Checked by the spec synthesizer and consistent with c_dy §3.10.
- **Status:** V.
- **Used in:** `def:prelim-plus`, `prop:dy-nlo`.

### VF-DY-13 — Glauber 玩具模型（阿贝尔，eikonal 旁观者）
- **(G-i)** $\sum$ spectator–spectator exchanges $=e^{i\chi(b)}$, with $\chi(b)=-\frac{g_Ag_B}{2\pi}K_0(m|b|)$.
- **(G-ii)** The phase cancels in cross sections inclusive in the relative transverse momentum: at $O(g^2)$, $i\chi-i\chi=0$; at $O(g^4)$, $\chi^2-\frac{\chi^2}2-\frac{\chi^2}2=0$; and $|e^{i\chi}|^2=1$ to all orders.
- **(G-iii)** The spectator–spectator Glauber region is trapped.
- **(G-iv)** The active–spectator exchange is not trapped in $k^+$. It is $A$-collinear, with a past-pointing line.
- **Status:** V (25/25).
- **Source:** c_dy §7.
- **Used in:** `prop:dy-abelian-model`.

### VF-DY-14 — Mellin 矩与大 $N$
At $\mu_F=Q$:
- $N=1$: $\Delta^{(1)}_{q\bar q}=C_F(8\zeta_2-\frac72)$ and $\Delta^{(1)}_{qg}=\frac{T_F}9$;
- $N=2$: $\Delta^{(1)}_{q\bar q}=C_F(8\zeta_2+\frac{13}{18})$ and $\Delta^{(1)}_{qg}=-\frac{11}{18}T_F$;
- large $N$: $\Delta_{q\bar q,N}=1+aC_F[4\ln^2\bar N+8\zeta_2-8]+O(\ln N/N)$.
- **Status:** V (40 digits).
- **Source:** c_dy §3.7.
- **Used in:** `ex:dy-threshold`, `prop:thr-oneloop`.

---------------------------------------------------------------------------------------------------

## THR — threshold

### VF-THR-1 — 阈值指数（领头幂次）
$$\ln\Delta_N=\int_0^1dz\,\frac{z^{N-1}-1}{1-z}\Big[2\int_{\mu_F^2}^{(1-z)^2Q^2}\frac{dq^2}{q^2}A(\alpha_s(q^2))+D(\alpha_s((1-z)^2Q^2))\Big]+O(N^0),\qquad A=\frac{C_F\alpha_s}\pi+O(\alpha_s^2),\ D=O(\alpha_s^2).$$
- **Status:** V for the normalization of $A^{(1)}$, which reproduces the $8C_F\mathcal D_1$ of $\Delta_{q\bar q}$ (critic c6). The structure of the formula is literature (`Sterman1987`, `CataniTrentadue1989`).
- **Used in:** `thm:thr-refactorization`.

### VF-THR-2 — 单圈大 $N$ 检验
$\langle\mathcal D_0,z^{N-1}\rangle\to-\ln\bar N$ and $\langle\mathcal D_1,z^{N-1}\rangle\to\frac12(\ln^2\bar N+\zeta_2)$, so
$$\Delta_{q\bar q,N}=1+\frac{\alpha_s}{2\pi}C_F\big[4\ln^2\bar N+8\zeta_2-8\big]\ (\mu_F=Q).$$
- **Status:** V.
- **Source:** critic c6; c_dy §3.7.
- **Used in:** `prop:thr-oneloop`, `lem:appA-mellin-table`.

### VF-THR-3 — 与 Moch–Vogt 的比较
$g_{01}^{\rm DY}=C_F(-16+16\zeta_2+8\gamma_E^2)$ in the normalization of `Moch:2005ky`, consistent with VF-THR-2.
- **Status:** VL.
- **Source:** c_dy §6.2.
- **Used in:** `prop:thr-oneloop`.

---------------------------------------------------------------------------------------------------

## TMD — transverse-momentum-dependent factorization

**Update (spec audit, 2026-10-10).** `research/c_tmd/DERIVATION.md` now exists (written 14:07, after this file was first built). All 17 c_tmd scripts pass (`scripts/run_all.sh`; no log contains FAIL; the earlier tolerance-level FAILs are gone). Its results R1–R12 (DERIVATION §0) were checked against the arXiv sources of Aybat–Rogers 2011, Echevarria–Idilbi–Scimemi 2012, Collins–Rogers 2013, Balázs–Yuan 1997 and Bacchetta–Conti–Radici 2008. The entries below are upgraded accordingly; c_tmd result numbers R1–R12 are given in brackets. Collins 2011 equation numbers are quoted only where Collins–Rogers 2013 quote them ((13.106), (14.31), §3.3.2, §10.8, §10.11.1, §10.12.3).

### VF-TMD-1 — 单圈 Collins–Soper 核
$$\tilde K(b_T;\mu)=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}+O(\alpha_s^2),\qquad \frac{d\tilde K}{d\ln\mu}=-\gamma_K .$$
- **Status:** VL (critic c7; c_tmd [R7], DERIVATION §3.8: obtained both from the $\zeta$-derivative of the TMD and from the soft factor alone, §3.5; equal to Aybat–Rogers 2011 (B1)–(B3)).
- **Used in:** `lem:tmd-soft-oneloop`, `prop:tmd-evolution-oneloop`.

### VF-TMD-2 — $\gamma_K$
$\gamma_K=\dfrac{2\alpha_sC_F}\pi+O(\alpha_s^2)$, so that $\gamma_K=2\Gamma_{\rm cusp}$.
- **Status:** V (critic c7).
- **Used in:** `prop:tmd-evolution-oneloop`.

### VF-TMD-3 — 类时硬因子
$$\mathcal H=1+\frac{\alpha_sC_F}{2\pi}\Big[-L^2+3L-8+\frac{7\pi^2}6\Big],\qquad L=\ln\frac{Q^2}{\mu^2},\qquad \frac{d\ln\mathcal H}{d\ln\mu}=\frac{\alpha_sC_F}\pi(2L-3).$$
This is the same as VF-SCET-8 in other units.
- **Status:** VL (BP §18.3; c_scet row 8 vs BS 2008; c_tmd [R10], DERIVATION §4.2, from an independent exact-in-$\varepsilon$ form factor; equals EIS 2012 §7).
- **SIDIS (space-like) hard factor:** $\mathcal H_{\rm SIDIS}=1+\frac{\alpha_sC_F}{2\pi}[-L^2+3L-8+\frac{\pi^2}6]$ (binding $S_\varepsilon$). With Collins' $S_\varepsilon$ the constants are $-8+\pi^2$ (DY) and $-8$ (SIDIS) (c_tmd [R10]; Aybat–Rogers arXiv:1107.3973).
- **Used in:** `prop:tmd-evolution-oneloop`, `thm:tmd-factorization`.

### VF-TMD-4 — TMD 反常维度
$$\gamma_q(\alpha_s;1)=\frac32\frac{\alpha_sC_F}\pi,\qquad \gamma_F=\frac{\alpha_sC_F}\pi\Big(\frac32-l_\zeta\Big),\ l_\zeta=\ln\frac\zeta{\mu^2},\qquad 2\gamma_q-\tfrac12\gamma_K\ln\frac{\zeta_A\zeta_B}{\mu^4}=\frac{\alpha_sC_F}\pi(3-2L)\ (\zeta_A\zeta_B=Q^4).$$
- **Status:** VL (c_tmd [R6]–[R7], DERIVATION §3.8: UV counterterm $Z_FZ_2=1+aS_\varepsilon[-\frac1{\varepsilon^2}+\frac{l_\zeta-3/2}\varepsilon]$, $a=\frac{\alpha_sC_F}{2\pi}$, the same in both $S_\varepsilon$ conventions; equal to Aybat–Rogers 2011 (B1)–(B3); RG consistency with VF-TMD-3 checked for DY and SIDIS).
- **Used in:** `prop:tmd-evolution-oneloop`.

### VF-TMD-5 — 小 $b$ 系数 $\tilde C_{q/q}$ 与 $S_\varepsilon$ 方案常数
At $\mu=\mu_b$, $\zeta=\mu_b^2$:
$$\tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}\Big[(1-x)-\frac{\pi^2}{12}\delta(1-x)\Big]\ (\text{binding }S_\varepsilon),\qquad \tilde C_{q/q}=\delta(1-x)+\frac{\alpha_sC_F}{2\pi}(1-x)\ (\text{Collins }S^{\rm C}_\varepsilon).$$
Hard factor with Collins' $S_\varepsilon$: $-8+\pi^2$ instead of $-8+\frac{7\pi^2}6$. The scheme differences cancel in the cross section: $\mathcal H^{\rm bind}-\mathcal H^{\rm C}=\frac{\pi^2}6$ and $2[\tilde C^{\rm bind}-\tilde C^{\rm C}]=-\frac{\pi^2}6$.
- **Status:** VL (c_tmd [R8], DERIVATION §3.9: the binding value equals EIS 2012 §4 eq. `coeff` (standard $S_\varepsilon$); the Collins value equals Aybat–Rogers 2011 (A11), read in the arXiv source; RG check $\frac{d}{d\ln\mu}(\tilde C\otimes f)=\gamma_F\,\tilde C\otimes f$ passes).
- **Full one-loop form** (c_tmd [R8]), with $a=\frac{\alpha_sC_F}{2\pi}$, $L_b=\ln\frac{\mu^2b_T^2}{b_0^2}$, $l_\zeta=\ln\frac\zeta{\mu^2}$, $p(x)=(1+x^2)[\frac1{1-x}]_+$, $\kappa=1$ (binding), $0$ (Collins):
$$\tilde C_{q/q}=\delta(1-x)+a\Big\{-L_b\,p(x)+(1-x)+\delta(1-x)\Big[-\frac{L_b^2}2-L_bl_\zeta-\kappa\frac{\pi^2}{12}\Big]\Big\},\qquad \tilde C_{q/g}=\frac{\alpha_sT_F}{2\pi}\Big\{-L_b[x^2+(1-x)^2]+2x(1-x)\Big\},$$
$\tilde C_{q/\bar q},\tilde C_{q/q'}=O(\alpha_s^2)$. The coefficient of $L_b$ is $-p(x)$, not $-P_{qq}/C_F$ (the $\frac32\delta$ belongs to $\gamma_F$). Error term of the small-$b$ OPE: $O((mb_T)^p)$, $p>0$ (not "$O(b_Tm)$"; c_tmd §8 item 6).
- **Used in:** `prop:tmd-small-b`, `rem:tmd-scheme-constants`.

### VF-TMD-6 — $\tilde C_{q/g}$
$$\tilde C_{q/g}(x;\mu_b,\mu_b^2)=\frac{\alpha_sT_F}{2\pi}2x(1-x).$$
The pole is $-\frac1\varepsilon P_{qg}/T_F$, IR, matching the PDF. The $D$-dimensional kernel is $F_{q/g}=1-\frac{2x(1-x)}{1-\varepsilon}$.
- **Status:** VL (c_tmd [R8], `quark_in_gluon.py`, gluon polarizations averaged over $D-2$; equal to Aybat–Rogers 2011 (A10)).
- **Used in:** `prop:tmd-small-b`.

### VF-TMD-7 — 小 $q_T$ 渐近行为与 CSS 系数
$$A^{(1)}=C_F,\qquad B^{(1)}=-\frac32C_F\quad(\text{expansion in }\alpha_s/\pi,\ C_1=b_0,\ C_2=1),\qquad C^{(1)}_{qq}=\frac{\alpha_s}\pi\Big[\frac{C_F}2(1-z)+C_F\Big(\frac{\pi^2}4-2\Big)\delta(1-z)\Big].$$
The $O(\alpha_s)$ CSS expansion reproduces the exact small-$q_T$ asymptotics: the ratio tends to $1$, while with $B^{(1)}=0$ it would be $0.896$ at $q_T/Q=10^{-3}$.
- **Status:** VL (c_tmd [R11], DERIVATION §5: symbolic `css_expansion.py`; numerical comparison with the exact $O(\alpha_s)$ matrix elements, ratio $\to1$ with deviation $\sim q_T^2/Q^2$, both channels; Balázs–Yuan 1997 App., read in the source). Also $C^{(1)}_{qg}=\frac{\alpha_s}\pi T_Fz(1-z)$. $C^{(1)}_{qq}$ is identical in both $S_\varepsilon$ conventions (it equals $\tilde C_{q/q}+\frac12\mathcal H^{(1)}\delta$).
- **Used in:** `def:tmd-kin`, `rem:tmd-scheme-constants`, `ex:tmd-qt-asymptotics`.

### VF-TMD-8 — 软因子快度积分、$\delta$ 正规子与 Sivers 模型
- Soft factor with non-light-like lines: $\tilde S^{(1)}_{\rm bare}=\frac{\alpha_sC_F}\pi S_\varepsilon(Y\coth Y-\sigma)A(\varepsilon)$, $Y=y_A-y_B$, with $\sigma=1$ (time-like lines, self-energies included) or $\sigma=0$ (space-like lines, "no S.I."); renormalized $-\frac{\alpha_sC_F}\pi(Y\coth Y-\sigma)L_b$. The time-like and the space-like (principal-value) rapidity integrals both give $4(Y\coth Y-\sigma)$. For $\sigma=1$ the UV pole is two cusps with the one-loop cusp anomalous dimension of VF-CONV-23.
- $\delta$ regulator: the soft integral gives $\ln\frac{l_T^2}{2\delta^+\delta^-}$, and the combination gives $\ln(\zeta/k_T^2)$ with $\zeta=2(p^+)^2\delta^-/\delta^+$.
- Spectator model (point-like scalar diquark): $f_{1T}^{\perp\,\rm SIDIS}=\frac{g^2e_qe_s}{4(2\pi)^4}\frac{M(m+xM)(1-x)}{k_T^2(k_T^2+L^2)}\ln\frac{k_T^2+L^2}{L^2}=-f_{1T}^{\perp\,\rm DY}$, $L^2=x\lambda^2+(1-x)m^2-x(1-x)M^2$; negative for an attractive final-state interaction ($e_qe_s<0$; QCD singlet $e_qe_s\to-4\pi C_F\alpha_s$) in the Trento convention (`BacchettaEtAl2004`).
- **Status:** V/VL. Soft factor: c_tmd [R4] (analytic + numeric rapidity integrals). $\delta$ regulator: c_tmd [R9], equal to Collins–Rogers 2013 eq. (zetaA). Spectator model: c_tmd [R12] (full Dirac traces numerically; closed forms to $10^{-10}$; DY/SIDIS $=-1$ to $10^{-12}$), equal to Bacchetta–Conti–Radici 2008 eq. (SivBM2-s-pl) with $e_qe_s=-e_c^2$. That the *phenomenological* $f_{1T}^{\perp u}$ is negative is recalled, not verified.
- **Used in:** `lem:tmd-soft-oneloop`, `rem:tmd-schemes`, `thm:tmd-sivers-sign`, `ex:tmd-sivers-model`.

### VF-TMD-9 — $\zeta$ 的归一化、极限次序与正规子 Wilson 线的方向
$$\zeta_A=M_A^2x_A^2e^{2(y_P-y_n)}=2(x_AP_A^+)^2e^{-2y_n},\qquad \zeta_B=2(x_BP_B^-)^2e^{2y_n},\qquad \zeta_A\zeta_B=Q^4\ \text{(leading power)}.$$
- Aybat–Rogers 2011 eq. (3) prints a spurious factor 2 in $\zeta$; their one-loop results agree with ours only without it. Do not copy that equation.
- **Order of limits** in `def:tmd-collins`: first the light-like limit $y_B\to-\infty$ at fixed $\varepsilon$, then $\overline{\rm MS}$ renormalization, then $\varepsilon\to0$. In the other order the non-light-like vertex graph leaves $\ln^2(\Lambda_B^2/\mu^2)$ terms (c_tmd §3.4; Collins–Rogers 2013 §3, citing Collins 2011 §10.8, §10.11.1).
- **Regulator lines are space-like** (Collins 2011; Aybat–Rogers 2011). With time-like past-pointing lines the path-ordered operator is anti-time-ordered, and the PT argument of `thm:tmd-sivers-sign` fails at finite rapidity: the real part of the one-loop vertex differs by $2\pi^2\frac{\alpha_sC_F}{4\pi}$ (c_tmd §3.4, §6.2). All such terms vanish in the light-like limit.
- **Status:** V (c_tmd §1 item 4, §2.3, §3.4, §8 items 3–5).
- **Used in:** `def:tmd-collins`, `thm:tmd-sivers-sign`, `ex:tmd-oneloop`.

### VF-TMD-10 — 小 $q_T$ 的 $O(\alpha_s)$ 渐近式（CSS 展开的检验）
$$\frac{d\sigma}{dQ^2dy\,dq_T^2}\Big|_{q_T\ll Q}=\frac{\sigma_0}{s}\frac{\alpha_s}{2\pi}\frac1{q_T^2}\Big\{\Big[2A^{(1)}\ln\frac{Q^2}{q_T^2}+2B^{(1)}\Big]q(x_A)\bar q(x_B)+(P_{qq}\otimes q)(x_A)\bar q(x_B)+q(x_A)(P_{qq}\otimes\bar q)(x_B)+(P_{qg}\otimes g)(x_A)\bar q(x_B)+\dots\Big\}+O\Big(\frac{\alpha_s}{Q^2}\Big),$$
with $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$ (VF-DY normalization; c_tmd writes $\sigma_0/s$ as one symbol), $A^{(1)}=C_F$, $B^{(1)}=-\frac32C_F$ in units $\alpha_s/\pi$ (VF-TMD-7). Fourier identities: ${\rm FT}[L]=-\frac1{\pi q_T^2}$, ${\rm FT}[L^2]=-\frac2\pi\frac{\ln(Q^2/q_T^2)}{q_T^2}$, $L=\ln(Q^2b^2/b_0^2)$, ${\rm FT}[g]=\int\frac{d^2b}{(2\pi)^2}e^{iq_T\cdot b}g$.
- **Status:** V (c_tmd [R11], DERIVATION §5.3; exact matrix elements vs expansion, ratio $1.0000000$ at $q_T/Q=10^{-4}$; altering $A^{(1)}$ or $B^{(1)}$ destroys the agreement).
- **Used in:** `def:tmd-kin`, `ex:tmd-qt-asymptotics`.

---------------------------------------------------------------------------------------------------

## SCET — soft-collinear effective theory, thrust

Here $a=C_F\alpha_s/(4\pi)$, and scalings are written for $(\bar n\cdot p,n\cdot p,p_\perp)$. The source is c_scet (171/171 checks); "(read)" means the agent read the original arXiv source.

### VF-SCET-1 — 模式
| mode | scaling $(\bar n\!\cdot\!p,n\!\cdot\!p,p_\perp)/Q$ |
|---|---|
| hard | $(1,1,1)$ |
| $n$-collinear | $(1,\lambda^2,\lambda)$ |
| $\bar n$-collinear | $(\lambda^2,1,\lambda)$ |
| usoft | $(\lambda^2,\lambda^2,\lambda^2)$ |
| soft | $(\lambda,\lambda,\lambda)$ |
| hard-collinear | $(1,\lambda,\lambda^{1/2})$ |
| Glauber $n\bar n$ | $(\lambda^2,\lambda^2,\lambda)$ |
| Glauber $ns$ | $(\lambda,\lambda^2,\lambda)$ |
| Glauber $\bar ns$ | $(\lambda^2,\lambda,\lambda)$ |
- **Status:** VL (Rothstein–Stewart Table 1, with the first two entries swapped).
- **Used in:** `def:scet-modes`.

### VF-SCET-2 — 场的标度
$\xi_n\sim\lambda$, $(\bar n\!\cdot\!A_n,n\!\cdot\!A_n,A_{n\perp})\sim(1,\lambda^2,\lambda)$, $A_{us}\sim\lambda^2$, $q_{us}\sim\lambda^3$, $A_s\sim\lambda$, $q_s\sim\lambda^{3/2}$.
- **Status:** VL.
- **Used in:** `prop:scet-scalings`.

### VF-SCET-3 — 领头阶共线夸克拉氏量
$$\mathcal L^{(0)}_{\xi\xi}=\bar\xi_n\Big[in\!\cdot\!D+i\slashed D_{\perp c}\frac1{i\bar n\!\cdot\!D_c}i\slashed D_{\perp c}\Big]\frac{\bar{\slashed n}}2\xi_n,\qquad in\!\cdot\!D=in\!\cdot\!\partial+gn\!\cdot\!A_n+gn\!\cdot\!A_{us}(x_-).$$
- **Status:** VL (exact tree identity).
- **Used in:** `prop:scet-lagrangian`.

### VF-SCET-4 — SCET Feynman 规则
- Collinear vertex: $igt^a\big[n^\mu+\frac{\gamma_\perp^\mu\slashed p_\perp}{\bar n\cdot p}+\frac{\slashed p'_\perp\gamma_\perp^\mu}{\bar n\cdot p'}-\frac{\slashed p'_\perp\slashed p_\perp\bar n^\mu}{\bar n\cdot p\,\bar n\cdot p'}\big]\frac{\bar{\slashed n}}2$.
- Usoft vertex: $igt^an^\mu\frac{\bar{\slashed n}}2$.
- Propagator: $i\frac{\slashed n}2\frac{\bar n\cdot p}{p^2+i0}$.
- **Status:** V (exact tree identity).
- **Used in:** `prop:scet-lagrangian`.

### VF-SCET-5 — 共线 Wilson 线
$$W_n(x)=W[x,x-\infty\bar n]=P\exp\Big(ig\!\int_{-\infty}^0\!ds\,\bar n\!\cdot\!A_n(x+s\bar n)\Big)=\sum_{\rm perms}\exp\Big[-\frac g{\bar{\mathcal P}}\bar n\!\cdot\!A_n\Big].$$
One-gluon rule: $-g\bar n^\mu t^a/(\bar n\cdot k+i0)$. No sign change of $g$ is needed relative to BFPS and BPS.
- **Status:** VL.
- **Used in:** `prop:scet-wilson`.

### VF-SCET-6 — 超软退耦
$$in\!\cdot\!D_{us}\,Y_n=Y_n\,in\!\cdot\!\partial,\qquad Y_n(x)=W[x,x-\infty n],\qquad \xi_n=Y_n\xi_n^{(0)},\ A_n=Y_nA_n^{(0)}Y_n^\dagger,\ c_n=Y_nc_n^{(0)}Y_n^\dagger .$$
Conditions: usoft-covariant gauge fixing, unit Jacobian, leading power, multipole expansion. The key identity was verified numerically for random su(3) fields to $2\times10^{-10}$.
- **Status:** V (BPS 2002 §IV read).
- **Source:** c_scet §2.4.
- **Used in:** `thm:scet-decoupling`.

### VF-SCET-7 — 无质量形状因子（裸，精确）
$$F^{(1)}_{\rm bare}=\frac{\alpha_sC_F}{4\pi}\Big(\frac{4\pi\mu_0^2}{Q^2}\Big)^{\varepsilon}c_\Gamma\Big[-\frac{2-\varepsilon+2\varepsilon^2}{\varepsilon^2(1-2\varepsilon)}\Big]$$
This is the same as VF-SUD-1.
- **Status:** V.
- **Used in:** `prop:scet-hard-matching`.

### VF-SCET-8 — 匹配系数与硬函数
$$C_V=1+a\big[-L^2+3L-8+\zeta_2\big],\quad L=\ln\frac{-q^2-i0}{\mu^2};\qquad H=1+a\Big[-2L_Q^2+6L_Q-16+\frac{7\pi^2}3\Big].$$
- **Status:** VL (BS 2008 App. B: $c_1^H=C_F(-16+\frac{7\pi^2}3)$, $\Gamma_0=4C_F$, $\gamma^H_0=-6C_F$).
- **Used in:** `prop:scet-hard-matching`, `prop:tmd-evolution-oneloop`.

### VF-SCET-9 — 喷注函数
$$J^{(1)}_{\rm bare}(p^2)=-\frac{\alpha_sC_F}{4\pi}(4\pi\mu_0^2)^{\varepsilon}\frac{4-\varepsilon}{\varepsilon}\frac{\Gamma(2-\varepsilon)}{\Gamma(2-2\varepsilon)}(p^2)^{-1-\varepsilon},$$
$$J=\delta(p^2)+a\Big\{(7-\pi^2)\delta(p^2)-3\Big[\frac1{p^2}\Big]_*+4\Big[\frac{\ln(p^2/\mu^2)}{p^2}\Big]_*\Big\},\qquad \tilde j=1+a\Big(2L^2-3L+7-\frac{2\pi^2}3\Big).$$
Use the explicitly normalized cut definition: Becher–Schwartz' literal formula carries an implicit $-\frac1{2N_c}{\rm tr}$ (c_scet §6 item 13).
- **Status:** VL (BS 2008: $c_1^J=C_F(7-\frac{2\pi^2}3)$, $\gamma^J_0=-3C_F$).
- **Used in:** `prop:scet-thrust-oneloop`.

### VF-SCET-10 — 推力软函数
$$S_T=\delta(k)+a\Big\{\frac{\pi^2}3\delta(k)-16\Big[\frac{\ln(k/\mu)}k\Big]_*\Big\},\qquad \tilde s_T=1+a(-8L^2-\pi^2).$$
- **Status:** VL (BS 2008: $c_1^S=-C_F\pi^2$).
- **Used in:** `prop:scet-thrust-oneloop`.

### VF-SCET-11 — RG 一致性
- The cusp terms cancel identically: $2L_Q-4L_J+4L_S=0$.
- The non-cusp anomalous dimensions satisfy $\gamma^S=\gamma^H-2\gamma^J$, with the BS normalization $d\ln H=\dots+2\gamma^H$, $d\ln\tilde j=\dots-2\gamma^J$, $d\ln\tilde s=\dots-2\gamma^S$.
- Two loops: $\gamma^S_1=C_FC_A(\frac{808}{27}-\frac{11\pi^2}9-28\zeta_3)+C_FT_Fn_f(-\frac{224}{27}+\frac{4\pi^2}9)$. The $C_F^2$ terms cancel.
- **Status:** VL (BS 2008 read).
- **Source:** c_scet §3.5, §6 item 1.
- **Used in:** `prop:scet-thrust-oneloop`.

### VF-SCET-12 — $O(\alpha_s)$ 推力分布的奇异项
$$\frac1{\sigma_0}\frac{d\sigma}{d\tau}=\delta(\tau)+\frac{C_F\alpha_s}{2\pi}\Big\{\Big(\frac{\pi^2}3-1\Big)\delta(\tau)-3\Big[\frac1\tau\Big]_+-4\Big[\frac{\ln\tau}\tau\Big]_+\Big\}+\text{nonsingular},$$
$$\text{cumulant: }1+\frac{C_F\alpha_s}{2\pi}\Big[-2\ln^2\tau-3\ln\tau+\frac{\pi^2}3-1\Big]+O(\tau\ln\tau).$$
The plus distributions are taken at $\tau=0$ on $[0,1]$. The $\delta$ coefficient from the sum rule is $2.289868133697$, against $\frac{\pi^2}3-1=2.289868133696$.
- **Status:** V (c_scet; critic c3, 20 digits).
- **Used in:** `prop:scet-thrust-oneloop`, `prop:jets-thrust-lo`, `ex:scet-thrust-oneloop`.

### VF-SCET-13 — 领头阶推力分布
$$\frac1{\sigma_0}\frac{d\sigma}{dT}=\frac{C_F\alpha_s}{2\pi}\Big[\frac{2(3T^2-3T+2)}{T(1-T)}\ln\frac{2T-1}{1-T}-\frac{3(3T-2)(2-T)}{1-T}\Big]$$
- **Status:** V (integrated from the matrix element, to $7\times10^{-15}$; DEFG 1978 recalled).
- **Used in:** `prop:jets-thrust-lo`.

### VF-SCET-14 — 领头对数指数
$$\ln\tilde t_{\rm LL}=\ell\,g_1(\lambda),\qquad g_1=-\frac{C_F}{\pi b\lambda}\big[(1-2\lambda)\ln(1-2\lambda)-2(1-\lambda)\ln(1-\lambda)\big],\qquad \lambda=b\alpha_s(Q)\ell,\ b=\frac{\beta_0}{4\pi}.$$
- **Status:** V (exact identity vs CTTW, recalled; `CataniEtAl1993`).
- **Used in:** `prop:scet-ll`.

### VF-SCET-15 — 推力与半球质量
For massless particles:
$$\frac{M_L^2+M_R^2}{Q^2}=\tau-\frac{\tau^2}2+\frac{(M_R^2-M_L^2)^2}{2Q^4}\ \text{exactly}.$$
For three partons the left-hand side equals $\tau$ exactly.
- **Status:** V.
- **Used in:** `prop:jets-thrust-lo`, `thm:scet-thrust`.

### VF-SCET-16 — 两圈 cusp（BS 的笔误）
This is the same as VF-CONV-23 for $\Gamma_1$. The BS arXiv App. A prints $\Gamma_1=4C_F[C_A(\frac{67}9-\frac{\pi^2}3)-\frac{20}9C_FT_Fn_f]$, where the $C_F$ inside the bracket is spurious.
- **Status:** VL.
- **Source:** c_scet §6 item 10.
- **Used in:** `prop:appB-cusp-oneloop`.

---------------------------------------------------------------------------------------------------

## NRQ — NRQCD

### VF-NRQ-1 — 速度标度规则
$\psi\sim(mv)^{3/2}$, $D\sim mv$, $D_t\sim mv^2$, $gE\sim m^2v^3$, $gB\sim m^2v^4$. The $1/m^2$ bilinears are $O(v^2)$. BBL use $D=\partial+igA$, so the signs of $c_{2,3,4}$ flip under CONTEXT's convention.
- **Status:** V.
- **Source:** c_scet §4.1.
- **Used in:** `def:heavy-nrqcd`.

### VF-NRQ-2 — $^3S_1\to e^+e^-$
$$\Gamma(^3S_1\to e^+e^-)=\frac{16\pi N_c}3\frac{e_Q^2\alpha^2|\psi(0)|^2}{M^2}=\frac{N_ce_Q^2\alpha^2|R(0)|^2}{3m_Q^2},\qquad M=2m_Q .$$
- **Status:** VL (BBL ${\rm Im}f_{ee}=\frac{\pi Q^2\alpha^2}3$ read; Van Royen–Weisskopf recalled).
- **Used in:** `prop:heavy-nrqcd-matching`.

### VF-NRQ-3 — $^1S_0\to\gamma\gamma$
$$\Gamma(^1S_0\to\gamma\gamma)=16\pi N_c\frac{e_Q^4\alpha^2|\psi(0)|^2}{M^2}=\frac{4N_ce_Q^4\alpha^2|R(0)|^2}{M^2}.$$
- **Status:** VL (BBL ${\rm Im}f_{\gamma\gamma}(^1S_0)=\pi Q^4\alpha^2$ read; para-positronium check).
- **Used in:** `prop:heavy-nrqcd-matching`.

### VF-NRQ-4 — 单圈 $c_v$
- Vertex at threshold: $a\big(\frac3\varepsilon-4+3\ln\frac{\mu^2}{m^2}\big)$.
- On-shell wave-function renormalization: $\delta Z_2^{\rm OS}=-a\big(\frac3\varepsilon+4+3\ln\frac{\mu^2}{m^2}\big)$.
- Result: $c_v=1-2C_F\frac{\alpha_s}\pi$, so $\Gamma(V\to e^+e^-)\propto1-\frac{16\alpha_s}{3\pi}$.
- **Status:** VL (BBL App. A read: ${\rm Im}f_{ee}=\frac{\pi Q^2\alpha^2}3[1-4C_F\frac{\alpha_s}\pi]$).
- **Used in:** `prop:heavy-nrqcd-matching`, `ex:heavy-cv`.

---------------------------------------------------------------------------------------------------

## BQ — QCD factorization in $B$ decays

### VF-BQ-1 — 单圈顶点项
$$V_M=12\ln\frac{m_b}\mu-18+\int_0^1g\,\Phi_M$$
The coefficient 12 is forced by the $\mu$-independence of $a_{1,2}$ for any $N_c$.
- **Status:** VL (BBNS 2001 eqs. (ai), (FM) read).
- **Used in:** `prop:heavy-qcdf-lp`.

### VF-BQ-2 — Gegenbauer 展开
$$\int_0^1g\,\Phi_M=-\frac12-3i\pi+\Big(\frac{11}2-3i\pi\Big)\alpha_1^M-\frac{21}{20}\alpha_2^M$$
- **Status:** VL ($10^{-20}$; BBNS 2001 eq. (vgegenb), in the BBNS Gegenbauer convention).
- **Used in:** `prop:heavy-qcdf-lp`.

### VF-BQ-3 — 端点发散积分
$$X_H=\int_0^1\frac{dy}{1-y}\Phi_p(y),\qquad X_A=\int_0^1\frac{dy}y\quad(\text{divergent}).$$
- **Status:** VL.
- **Used in:** `prop:heavy-qcdf-endpoint`.

### VF-BQ-4 — $X$ 模型
$$X=(1+\varrho e^{i\varphi})\ln\frac{m_B}{\Lambda_h},\qquad \varrho\le1,\ \Lambda_h=0.5\ {\rm GeV}.$$
This is a model. In the sources, "$X_H=\ln(m_M/\Lambda_h)$" is a typo for $m_B$.
- **Status:** VL.
- **Used in:** `prop:heavy-qcdf-endpoint`.

### VF-BQ-5 — 湮灭项
$$A_1^i\approx\pi\alpha_s\Big[18\Big(X_A-4+\frac{\pi^2}3\Big)+2r_\chi^2X_A^2\Big],\qquad A_3^f\approx12\pi\alpha_sr_\chi(2X_A^2-X_A)$$
Re-derived from the integrands. BN 2003 write $2\pi\alpha_s[9(\dots)+r_1r_2X_A^2]$.
- **Status:** VL.
- **Used in:** `prop:heavy-qcdf-endpoint`.

### VF-BQ-6 — $B\to D\pi$ 的归一化
$$\langle D\pi|O_{\bf0}|B\rangle=N\,F^{B\to D}(0)\int_0^1dx\,T(x,\mu)\phi_\pi(x,\mu),\qquad N=\frac i2m_BE_\pi f_\pi,\qquad O_{\bf0}=[\bar c\gamma^\mu P_Lb][\bar d\gamma_\mu P_Lu],\ P_L=\tfrac12(1-\gamma_5),$$
$O_{\bf8}$ the same with $T^a\otimes T^a$; at tree level $T=1$.
- **Status:** VL (c_scet row 23, BPS 2001 read). The spec audit re-derived $N$ at tree level from naive factorization ($m_B^2-m_D^2=2m_BE_\pi$ for a massless pion; each $P_L$ gives $\frac12$), up to the phase convention of $f_\pi$. With $(V-A)\otimes(V-A)$ operators instead of $P_L$ projectors, $N$ is 4 times larger.
- **Used in:** `thm:heavy-bdpi`.

---------------------------------------------------------------------------------------------------

## EXC — hard exclusive processes

Conventions: our $n_A$ is c_exclusive's $\bar n$, and our $n_B$ is its $n$. $f_\pi\approx130$ MeV.

### VF-EXC-1 — 介子分布振幅
$$\langle0|\bar d(z)\gamma^+\gamma_5W[z,-z]u(-z)|\pi^+(p)\rangle=if_\pi p^+\int_0^1dx\,e^{i(2x-1)p^+z^-}\phi_\pi(x),\qquad \int_0^1\phi_\pi=1,$$
where $x$ is the $u$-quark fraction and $\phi_\pi=6x\bar x\sum_na_nC_n^{3/2}(2x-1)$.
- **Status:** VL (BKM 2003 eq. (140) after translation).
- **Used in:** `def:excl-da`.

### VF-EXC-2 — $f_\pi$ 归一化
A tree-level extraction from $\Gamma(\pi\to\mu\nu)$ gives $131.7$ MeV. Use $f_\pi\approx130$ MeV, with $F_\pi=f_\pi/\sqrt2\approx92$ MeV. For VGG, $f_\pi^{\rm VGG}=92.4$ MeV $=f_\pi^{(130)}/\sqrt2$.
- **Status:** VL.
- **Used in:** `def:excl-da`.

### VF-EXC-3 — 单圈 ERBL 核
$$\mu^2\frac{d}{d\mu^2}\phi_\pi(x;\mu)=\frac{\alpha_s}{2\pi}\int_0^1dy\,V_0(x,y)\phi_\pi(y;\mu),\qquad V_0=C_F\Big[\frac xy\Big(1+\frac1{y-x}\Big)\theta(y-x)+\frac{\bar x}{\bar y}\Big(1+\frac1{x-y}\Big)\theta(x-y)\Big]_+$$
- **Status:** VL (BKM eqs. (141)–(143)).
- **Used in:** `prop:excl-erbl`.

### VF-EXC-4 — ERBL 反常维度
$$\gamma_n\equiv-\frac{4\pi}{\alpha_s}\mu\frac{d\ln a_n}{d\mu}=2C_F\Big[1-\frac2{(n+1)(n+2)}+4\sum_{j=2}^{n+1}\frac1j\Big],\qquad a_n\propto\alpha_s^{\gamma_n/(2\beta_0)},\qquad \gamma_0=0,\ \gamma_2=\frac{25}3C_F .$$
BKM's $\gamma^{(0)}_n=\gamma_n/2$.
- **Status:** VL.
- **Used in:** `prop:excl-erbl`.

### VF-EXC-5 — ERBL 本征值 = DGLAP 非单态矩
$$\int_0^1dy\,V_0(x,y)\,y\bar yC_n^{3/2}(2y-1)=v_n\,x\bar xC_n^{3/2}(2x-1),\qquad v_n=\int_0^1dz\,z^nP_{qq}(z)$$
A proof for all $n$ is given (hermiticity plus triangularity).
- **Status:** V.
- **Source:** c_exclusive §3.3.
- **Used in:** `prop:excl-erbl`.

### VF-EXC-6 — 介子形状因子的领头阶硬核
$$T_H=\frac{2\pi C_F\alpha_sf_\pi^2}{N_cQ^2}\Big[\frac{e_u}{\bar x\bar y}+\frac{e_{\bar d}}{xy}\Big],\qquad Q^2F_\pi=\frac{2\pi C_F}{N_c}\alpha_sf_\pi^2\Big[e_u\Big|\int\frac{\phi}{\bar x}\Big|^2+e_{\bar d}\Big|\int\frac\phi x\Big|^2\Big]\to8\pi\alpha_sf_\pi^2 .$$
There are four graphs in Feynman gauge; only the pairs A+B and C+D are gauge invariant.
- **Status:** VL (VGG eq. (65) after $f^{(130)}=\sqrt2f^{(93)}$).
- **Used in:** `prop:excl-pion-lo`, `ex:excl-pion-ff-lo`.

### VF-EXC-7 — 跃迁形状因子
$$Q^2F_{\gamma^*\gamma\pi}=\frac{\sqrt2f_\pi}3\int_0^1dx\frac{\phi_\pi(x)}x\to\sqrt2f_\pi$$
- **Status:** VL (BaBar 2009 eq. (2)).
- **Used in:** `thm:excl-transition`.

### VF-EXC-8 — DVCS 领头阶
$$T^{\mu\nu}=g_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,F^q\Big[\frac1{x-\xi+i0}+\frac1{x+\xi-i0}\Big]-i\epsilon_\perp^{\mu\nu}\sum_qe_q^2\!\int\!dx\,\tilde F^q\Big[\frac1{x-\xi+i0}-\frac1{x+\xi-i0}\Big]$$
In Ji's notation $\xi_{\rm Ji}=2\xi$. Ji's arXiv v1 prints the second denominator as "$x+\xi/2+i\epsilon$"; the correct prescription is $-i\epsilon$.
- **Status:** VL (Ji PRL 1997 eq. (15) read).
- **Used in:** `prop:excl-dvcs-lo`.

### VF-EXC-9 — 与 VGG 的比较
$H^{\mu\nu}_{\rm VGG}=-T^{\mu\nu}$, and VGG have the opposite $\epsilon$ sign. Both terms agree after this conversion.
- **Status:** VL.
- **Used in:** `prop:excl-dvcs-lo`.

### VF-EXC-10 — DIS 极限
The same kernel gives ${\rm Im}\,T^{11}=2\pi F_1$, with $F_1=\frac12\sum e_q^2(q+\bar q)$.
- **Status:** V (numerical at finite $i0$).
- **Used in:** `prop:excl-dvcs-lo`.

### VF-EXC-11 — 纵向光子产生赝标介子（领头阶）
$$\varepsilon_L\cdot A_\pi=-i\frac{C_F}{N_c}\frac{4\pi\alpha_sf_\pi}Q\int dz\,\phi_\pi(z)\int dx\Big[\frac{e_a}{\bar z(x-\xi+i0)}+\frac{e_b}{z(x+\xi-i0)}\Big]\tilde F^{ba}$$
- **Status:** VL (VGG eqs. (48), (59)).
- **Used in:** `thm:excl-meson-L`.

### VF-EXC-12 — GPD 定义、前向极限与多项式性
$$F^q=\frac12\!\int\!\frac{dz^-}{2\pi}e^{ix\bar P^+z^-}\langle p'|\bar q(-\tfrac z2)\gamma^+W[-\tfrac z2,\tfrac z2]q(\tfrac z2)|p\rangle=\frac1{2\bar P^+}\Big[H^q\bar u(p')\gamma^+u(p)+E^q\bar u(p')\frac{i\sigma^{+\alpha}\Delta_\alpha}{2M}u(p)\Big],\qquad \xi=\frac{p^+-p'^+}{p^++p'^+},$$
$$H^q(x,0,0)=q(x)\theta(x)-\bar q(-x)\theta(-x),\quad \int H=F_1(t),\quad \int xH=A+4\xi^2C,\quad \int x(H+E)=A+B,\quad J^q=\tfrac12[A^q(0)+B^q(0)].$$
- **Status:** VL (Ji PRL eqs. (12), (13), (17)–(19); model check; Gordon identity).
- **Used in:** `def:excl-gpd`, `prop:excl-polynomiality`.

### VF-EXC-13 — 共线 Fierz 分解
$$P_+MP_-=\tfrac14\big[{\rm Tr}(\gamma^+M)\gamma^-+{\rm Tr}(\gamma^+\gamma_5M)\gamma_5\gamma^-+\textstyle\sum_{j=1,2}{\rm Tr}(\gamma^+\gamma^jM)\gamma^-\gamma^j\big],\qquad P_+=\tfrac12\gamma^-\gamma^+,\ P_-=\tfrac12\gamma^+\gamma^- .$$
Leading-twist projections: $\langle0|\bar d_\beta(z)u_\alpha(0)|\pi^+\rangle\to\frac{if_\pi}4(\gamma_5\slashed p)_{\alpha\beta}\frac{\delta_{ij}}{N_c}\int dx\,e^{-i\bar xp\cdot z}\phi_\pi(x)$.
- **Status:** V (s1).
- **Source:** c_exclusive §1 (c_exclusive's $P_u,P_v$).
- **Used in:** `lem:appA-fierz`, `ex:intro-handbag`.

---------------------------------------------------------------------------------------------------

## POL — polarized DIS

### VF-POL-1 — Bjorken 求和规则（SU(3)，$\overline{\rm MS}$，HVBM–Larin）
$$\int_0^1dx\,[g_1^p-g_1^n](x,Q^2)=\frac{g_A}6\Big[1-a-\Big(\frac{55}{12}-\frac{n_f}3\Big)a^2+O(a^3)\Big],\qquad a=\frac{\alpha_s(Q^2)}\pi .$$
The $a^2$ coefficient is $-3.5833$ at $n_f=3$. Larin's finite renormalization of the non-singlet axial current is $Z_5^{\rm ns}=1-4C_F\frac{\alpha_s}{4\pi}+O(\alpha_s^2)$.
- **Status:** V for the sum-rule coefficients (critic c4). **T** for the $Z_5^{\rm ns}$ coefficient, which is quoted from `Larin:1993tq` and not re-derived.
- **Used in:** `thm:dis-bjorken`, `prop:appI-larin`.

### VF-POL-2 — Crewther 关系
$$C_{\rm Bjp}\,D_{\rm NS}=1+\beta_0\Big(\frac78-\zeta_3\Big)a^2+\dots,\qquad K_1=C_F\Big(-\frac{21}8+3\zeta_3\Big).$$
- **Status:** V (critic c4; this cross-validates VF-EE-10 and VF-POL-1).
- **Used in:** `rem:dis-crewther`.

### VF-POL-3 — 横度的领头阶演化核
$$\Delta_TP_{qq}(z)=C_F\Big[\frac{2z}{(1-z)_+}+\frac32\delta(1-z)\Big],\qquad \int_0^1\Delta_TP_{qq}=-\frac{C_F}2\ \Rightarrow\ \delta q(Q^2)\propto\alpha_s(Q^2)^{-2\gamma/\beta_0}=\alpha_s^{4/27}\ (n_f=3).$$
No gluon mixing for a spin-$\frac12$ target (helicity flip by two units).
- **Status:** C (standard; `ArtruMekhfi1990`; not derived by an agent). The spec audit checked only internal consistency: the first moment reproduces the known LO tensor-charge exponent $4/27$ (itself recalled). The writer re-derives the kernel or keeps 「（待核实）」.
- **Used in:** `prop:coll-transversity-evolution`.

---------------------------------------------------------------------------------------------------

## GLA — Glauber region and factorization breaking

Source: `research/c_glauber/DERIVATION.md`. **Update (spec audit):** §3 (diffraction) and §4 (space-like collinear limit, FSS pattern, super-leading logarithms) are now written (file of 13:33); all checks, including [D1a–e, D2a–f] and [S1–S7], pass (c_glauber §5: no check failed). VF-GLA-11/12 are therefore no longer log-only.

### VF-GLA-1 — Glauber 区是领头幂次
- Measure: $dk^+dk^-d^2k_T\sim\lambda^6Q^4$.
- Gluon propagator: $1/k_T^2\sim\lambda^{-2}$.
- Two spectator propagators: $\lambda^{-4}$.
- Numerator: $Q^2$.
- Product: $\lambda^0$. This agrees with the CSS review §8, "order $Q^0$ times logarithms".
- **Status:** V [P5].
- **Source:** c_glauber §1.1.
- **Used in:** App E, `prop:dy-regions`.

### VF-GLA-2 — 旁观者—旁观者核
$$\mathcal M^{(1)}_{SS}(p_A',p_B')=\int\frac{d^2k_T}{(2\pi)^2}V(k_T)\,\mathcal M^{(0)}(p_A'-k_T,p_B'+k_T),\qquad V(k_T)=\frac{-ie_Ae_B}{k_T^2+m_g^2}$$
The kernel is purely imaginary and even. Only the relative transverse momentum $\Delta$ shifts. In the non-abelian theory, $e_Ae_B\to g^2\mathbf T_A\cdot\mathbf T_B$.
- **Status:** V [SS1b–e].
- **Source:** c_glauber §1.5 Step 3.
- **Used in:** `lem:tmd-glauber`, `prop:dy-abelian-model`.

### VF-GLA-3 — 冲量参数空间相位与 $\Delta$ 积分后的相消
$$\int d^2\Delta\,2{\rm Re}\big[\mathcal M^{(1)}\mathcal M^{(0)*}\big]=\int\frac{d^2k}{(2\pi)^2}V(k)\big[C(k)-C(-k)\big]=0,\qquad \tilde{\mathcal M}^{(1)}(b)=i\chi(b)\tilde{\mathcal M}^{(0)}(b),\qquad \chi(b)=-\frac{e_Ae_B}{2\pi}K_0(m_gb),$$
and $\tilde{\mathcal M}=e^{i\chi}\tilde{\mathcal M}^{(0)}$ in the abelian eikonal limit. Point by point in $\Delta$ the sum is not zero.
- **Status:** V [SS3a–e, U3a–c].
- **Source:** c_glauber §1.5 Step 4.
- **Used in:** `lem:tmd-glauber`.

### VF-GLA-4 — 极点半平面规则
A line carrying $l+sk$ with large plus momentum has its $k^-$ pole in the lower half plane for $s=+1$ and in the upper half plane for $s=-1$. All poles lie on one side iff the lines through which $k$ is routed are all initial-state or all final-state.
- DY: only the spectator–spectator exchange is trapped in both variables.
- DIS: the target subgraph traps $k^-$, but the $k^+$ contour can be deformed (checked numerically to $2\times10^{-11}$).
- $e^+e^-$: nothing is trapped.
- **Status:** V [P1a–g, P4a–e, SS5a–b].
- **Source:** c_glauber §1.2–1.3.
- **Used in:** `prop:method-glauber-deformation`, `prop:dy-glauber-pinch`, `lem:disall-fsi`.

### VF-GLA-5 — 幺正性（割线位置求和）恒等式
$$\sum_{c=1}^{N}\Big[\prod_{f>c}\frac1{a_f-i\varepsilon}\Big]\frac{2\varepsilon}{a_c^2+\varepsilon^2}\Big[\prod_{f<c}\frac1{a_f+i\varepsilon}\Big]=i\prod_{f=1}^N\frac1{a_f+i\varepsilon}-i\prod_{f=1}^N\frac1{a_f-i\varepsilon}$$
After $\int dE/(2\pi)$ the right-hand side gives $1$ for $N=1$ and $0$ for $N\ge2$. Also verified: the Aybat–Sterman eikonal and causal identities.
- **Status:** V [U1, U2].
- **Source:** c_glauber §1.5 Step 5.
- **Used in:** `prop:method-fsi`, `lem:dy-fsi`.

### VF-GLA-6 — 胶子极强度
$$C_G=1+\frac{2\langle\mathbf T_a\cdot\mathbf T_b\rangle}{C_F}\quad(\text{SIDIS }+1,\ \text{DY }-1)$$
Channel values (SU(3) in brackets):
- $qq'\to qq'$, $tt^*$ and $uu^*$: $\frac{N^2-5}{N^2-1}$ $(\frac12)$;
- $tu^*$: $-\frac{N^2+3}{N^2-1}$ $(-\frac32)$;
- $q\bar q'\to q\bar q'$, $tt^*$: $-\frac{N^2-3}{N^2-1}$ $(-\frac34)$;
- $q\bar q\to q'\bar q'$, $ss^*$ and $st^*$: $\frac{N^2+1}{N^2-1}$ $(\frac54)$.

QVY graph by graph: $C_I/C_u=-\frac2{N^2-1}$, $C_{F1}/C_u=-\frac1{N^2-1}$, $C_{F2}/C_u=\frac{N^2-2}{N^2-1}$.
- **Status:** VL (BBMP Table I, eqs. (B5)–(B6); QVY Table I, eqs. (25)–(28); exact in $N$).
- **Source:** c_glauber §2.3 [C1–C5].
- **Used in:** `prop:break-colour`, `ex:break-colour`.

### VF-GLA-7 — Collins–Qiu 与 Collins 2007 的程函代数
$$E(l)=-\pi i(2g_2+g_1)\delta(l^+)-g_1{\rm PV}\frac1{l^+},\qquad E(l_1)E(l_2)^*\big|_{\rm anom}=4\pi^2g_2(g_2+g_1)\,\delta(l_1^+)\delta(l_2^+).$$
- **Status:** VL (CQ eqs. (4.1)–(4.3); C07 eqs. (2)–(4), (7), (8)).
- **Source:** c_glauber §2.2, §2.4 [A1–A3].
- **Used in:** `thm:break-tmd`.

### VF-GLA-8 — Collins 2007 标量模型中的反常贡献
$$I_1=\mathcal NF(k_T)^2,\qquad I_2=-\mathcal N\frac{G(k_T)}{k_T^2+m_q^2},\qquad \mathcal N=\frac{\lambda^2g_1^2g_2(g_2+g_1)x(1-x)}{256\pi^7},$$
$$F(k)=\frac{\pi}{\sqrt\Lambda}\ln\frac{s+\sqrt\Lambda}{s-\sqrt\Lambda},\qquad s=k^2+m_g^2+m_q^2,\ \Lambda=s^2-4m_g^2m_q^2,$$
$$\int d^2k_T(I_1+I_2)=0\ (\text{Parseval}),\qquad I_1(0)+I_2(0)<0\ (\text{Cauchy–Schwarz}).$$
C07 eq. (10) as printed carries a spurious factor $\prod_j(k_T^2+m_q^2)$.
- **Status:** V [A4a–f]. The Cauchy–Schwarz proof is c_glauber's own.
- **Source:** c_glauber §2.4.
- **Used in:** `ex:break-c07`.

### VF-GLA-9 — 梯形与交叉梯形的色因子
For $c\equiv\mathbf T_1\cdot\mathbf T_2$: ladder $L=c^2$, crossed $X=c^2+\frac{C_A}2c$. A Glauber phase does not commute with other soft exchanges: $[\mathbf T_A\cdot\mathbf T_B,\mathbf T_A\cdot\mathbf T_j]\ne0$.
- **Status:** V [U5a, SS4c].
- **Source:** c_glauber §1.6.
- **Used in:** `prop:break-fss`.

### VF-GLA-10 — 纠缠检验
$$\sum_{X,Y}C(X,Y)=C_F^2+\frac{4T_F^2(N^2-1)}{N^2}\ \neq\ \Big(\sum_XC_1(X)\Big)\Big(\sum_YC_2(Y)\Big)=C_F^2$$
For SU(3) this is $24/9$ vs. $16/9$. In the abelian case the two sides agree identically.
- **Status:** V [C6].
- **Source:** c_glauber §2.5.
- **Used in:** `thm:break-tmd`, `ex:break-colour`.

### VF-GLA-11 — 衍射：极点结构与间隙存活
- DDIS has a pinch in $r^-$ only and escapes via $r^+$; hadron–hadron diffraction is trapped in both variables.
- Dipole toy: unitarity holds for traces only. Singlet survival is $<1$ unless both constituents see the same phase.
- Singlet→octet leakage is quadratic in the phase difference, with coefficient $C_F/(2N)=\frac29$ for SU(3).
- Status of the physics statements (c_glauber §3.6): DDIS (and any lepton-induced hard process with a condition on the target fragmentation region) [A]; hadron–hadron hard diffraction [V]; diffractive photoproduction: resolved [V], direct covered in principle by Collins 1998 — the H1 2007 suppression also of the direct component is an unresolved tension (ZEUS differs).
- **Status:** V (c_glauber §3.2–3.4; checks [D1a–e], [D2a–f]).
- **Source:** c_glauber DERIVATION §3; `logs/diffraction.log`.
- **Used in:** `thm:break-ddis`, `prop:break-hh-diffraction`.

### VF-GLA-12 — 类空共线极限与 FSS 模式
- CdFR (68): $-\mathbf T_2\cdot\sum_j\mathbf T_j\,{\rm sign}(s_{j2})=\frac{C_{12}+C_2-C_1}2+2\mathbf T_2\cdot\mathbf T_3$.
- $\mathbf T_2\cdot\mathbf T_3\not\propto1$ for four coloured partons in the reduced amplitude; it is $\propto1$ for three partons.
- The one-loop breaking term is anti-Hermitian and cancels in $2{\rm Re}\langle M_0|M_1\rangle$.
- FSS: $\langle M|f_{abc}\mathbf T_i^a\mathbf T_j^b\mathbf T_k^c|M\rangle=0$ and $\langle M|[A,D]|M\rangle=0$ for real colour vectors, whereas $\langle M|[D,[D,A]]|M\rangle\ne0$.
- **Status:** V (c_glauber §4.1–4.2; checks [S1–S7]; CdFR eqs. (40), (42)–(44), (46), (68), (178)–(187) and FSS eqs. (5.5)–(5.9), (6.1) read). Order of first violation: amplitude, one loop (space-like, two incoming coloured partons); squared, $P^{(1)}$ strictly factorized; $P^{(2)}$ operator non-zero for $n\ge5$ QCD partons; pure-QCD expectation from three loops (c_glauber §4.3 table).
- **Source:** c_glauber DERIVATION §4; `logs/spacelike_colour.log`.
- **Used in:** `prop:break-spacelike`, `prop:break-fss`.

### VF-GLA-13 — 超领头对数：首项的阶与系数
First super-leading logarithm at $O(\alpha_s^4)$ relative to Born, $\propto\alpha_s^4L^5$ (FKS eq. (3.22)). For quark–quark scattering with one gluon outside the gap (FKS eq. (3.24)):
$$\sigma_{1,\rm SLL}=-\sigma_0\Big(\frac{2\alpha_s}\pi\Big)^4\ln^5\frac Q{Q_0}\,\pi^2\,Y\,\frac{3N^2-4}{480}.$$
All-order tower $\alpha_s^{n+3}L^{2n+3}$, $n\ge1$ (BNS 2021 eq. (14)), i.e. $\alpha_s^mL^{2m-3}$; absent at large $N_c$; requires two incoming coloured partons; $2\to1$ processes from four loops, $2\to0$ from five loops.
- **Status:** VL-quoted (c_glauber §4.5 read FKS 2006 and BNS 2021; coefficients quoted, not recomputed). Replaces the "(verify against the abstract)" of the outline.
- **Used in:** `prop:jets-sll`, `prop:break-fss`.

---------------------------------------------------------------------------------------------------

## MISC

### VF-MISC-1 — 调和和的解析延拓
$S_1(N)=\psi(N+1)+\gamma_E$, $S_2(N)=\zeta_2-\psi'(N+1)$, and $\int_0^1\frac{z^{N-1}-1}{1-z}dz=-S_1(N-1)$ for ${\rm Re}\,N>0$.
- **Status:** V.
- **Source:** c_dis §11; c_pdf §4.3.

### VF-MISC-2 — 矩反演的不稳定性
The moment Gram (Hilbert) matrix has ${\rm cond}_2\approx e^{3.5K}$: $4.8\times10^5$ at $K=5$ and $2.5\times10^{28}$ at $K=20$.
- **Status:** V.
- **Source:** c_pdf §7.2 (s6(c)).
- **Used in:** `rem:appK-counterexamples`.

### VF-MISC-3 — 逐点余项的反例
$R_Q(x)=\sin(Q^2x)$ satisfies $|Q^2\int_0^1x^nR_Q\,dx|\le c_n$ for all $n$, but $\sup|R_Q|=1$. $\delta'(x)$ has vanishing even moments.
- **Status:** V.
- **Source:** critic c5.
- **Used in:** `rem:dis-nonuniform`, `rem:appK-counterexamples`.

### VF-MISC-4 — BFKL 截距、BK 归一化与双对数极限
$$\omega_{\mathbb P}=\bar\alpha_s\chi(\tfrac12)=4\ln2\,\bar\alpha_s,\quad \chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma),\quad \bar\alpha_s=\frac{N_c\alpha_s}\pi;\qquad \partial_YN_{01}=\frac{\bar\alpha_s}{2\pi}\!\int\! d^2x_2\frac{x_{01}^2}{x_{02}^2x_{12}^2}\big[N_{02}+N_{12}-N_{01}-N_{02}N_{12}\big].$$
The linear part of the BK kernel has eigenvalue $\bar\alpha_s\chi(\gamma)$ on $(x_{01}^2)^\gamma$, so the BK normalization above and $\omega_{\mathbb P}=4\ln2\,\bar\alpha_s$ are consistent. Double-log limit: $\frac{\alpha_s}{2\pi}\gamma_{gg}(N)\to\frac{\bar\alpha_s}{N-1}$ as $N\to1$ (VF-PDF-8), hence at fixed coupling $xg\sim\exp\sqrt{4\bar\alpha_s\ln\frac1x\ln\frac{Q^2}{Q_0^2}}$ (saddle point of the inverse Mellin transform).
- **Status:** V (spec audit, `scratchpad/audit/checks1.py`, `checks3.py`: $\chi(\frac12)=4\ln2$; dipole-kernel eigenvalue $=\chi(\gamma)$ numerically at $\gamma=0.3,0.5,0.7$ to 8 digits; DLA saddle point analytic). The identification of this kernel with LL BK/BFKL is standard (`Balitsky1996`, `Kovchegov1999`), not re-derived.
- **Used in:** `thm:smallx-bfkl`, `thm:smallx-bk`, `ex:smallx-dla`.

### VF-MISC-5 — 单举湮灭的领头阶归一化与角分布
$$\frac{d\sigma^h}{dz}=\frac{4\pi\alpha^2}{3s}N_c\sum_qe_q^2\big[d_{h/q}(z)+d_{h/\bar q}(z)\big]\ (\text{LO}),\qquad \frac{d\sigma}{dz\,d\cos\theta}=\frac38(1+\cos^2\theta)\frac{d\sigma_T}{dz}+\frac34\sin^2\theta\frac{d\sigma_L}{dz}.$$
The angular weights integrate to $\frac{d\sigma}{dz}=\frac{d\sigma_T}{dz}+\frac{d\sigma_L}{dz}$. The momentum sum rule $\sum_h\int dz\,z\,d_{h/q}=1$ gives $\sum_h\int dz\,z\frac{d\sigma^h}{dz}=2\sigma_{\rm tot}$ at LO.
- **Status:** V (spec audit; elementary).
- **Used in:** `def:coll-sia`, `ex:coll-sia-lo`, `rem:coll-sia-nlo`.

---------------------------------------------------------------------------------------------------


# Part B — entries new in spec v2

---------------------------------------------------------------------------------------------------

## QCD — QCD basics for Ch2 (new in v2)

Source: `spec_v2/checks/vf_v2_checks.py` (log `vf_v2_checks.log`, 36/36 checks pass), unless stated.

### VF-QCD-1 — SU(N) 色代数
$$[t^a,t^b]=if^{abc}t^c,\quad {\rm Tr}(t^at^b)=\tfrac12\delta^{ab},\quad t^at^a=C_F\mathbb 1,\ C_F=\frac{N^2-1}{2N},\quad f^{acd}f^{bcd}=C_A\delta^{ab},\ C_A=N,$$
$$t^a_{ij}t^a_{kl}=\tfrac12\Big(\delta_{il}\delta_{kj}-\frac1N\delta_{ij}\delta_{kl}\Big),\qquad {\rm Tr}(t^at^bt^c)=\tfrac14\big(d^{abc}+if^{abc}\big),\quad d^{abc}=2\,{\rm Tr}(\{t^a,t^b\}t^c).$$
- **Status:** V (v2-check Q1a–Q1f: explicit SU(2) and SU(3) generators, all index values).
- **Used in:** Ch2 (`def:prelim-qcd`, colour-algebra example), App G.

### VF-QCD-2 — 协变导数、场强与规范变换
$$D_\mu=\partial_\mu-igA_\mu,\quad A_\mu=A^a_\mu t^a,\qquad [D_\mu,D_\nu]=-igG_{\mu\nu},\qquad G_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-ig[A_\mu,A_\nu],$$
$$G^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+gf^{abc}A^b_\mu A^c_\nu,\qquad A_\mu\to UA_\mu U^{-1}-\frac ig(\partial_\mu U)U^{-1}\ \Rightarrow\ G_{\mu\nu}\to UG_{\mu\nu}U^{-1},\ D_\mu\psi\to UD_\mu\psi .$$
- **Status:** V for the commutator and the component form (v2-check Q1g: $-ig[A_\mu,A_\nu]=gf^{abc}A^b_\mu A^c_\nu t^a$ for SU(2), SU(3); Q2: $[D_\mu,D_\nu]\psi=-igG_{\mu\nu}\psi$ symbolically with SU(2) fields of two variables). The transformation laws are those of VF-CONV-2 (V).
- **Used in:** Ch2 (gauge-invariance section, `def:prelim-qcd`), App B.

### VF-QCD-3 — 规范固定与 Faddeev–Popov 鬼场
$$\mathcal L_{\rm gf}=-\frac1{2\xi_g}(\partial^\mu A^a_\mu)^2,\qquad \mathcal L_{\rm FP}=\bar c^a\big(-\partial^\mu D^{ac}_\mu\big)c^c,\quad (D_\mu X)^a=\partial_\mu X^a+gf^{abc}A^b_\mu X^c,$$
with the propagators and the ghost vertex $-gf^{abc}p^\mu$ ($p$ = outgoing-ghost momentum) of VF-CONV-3; BRST transformations as in `def:prelim-brst` (signs to be re-derived against Peskin–Schroeder §16.4).
- **Status:** V (= VF-CONV-2/3; c_pdf §1, c_wilson §5).
- **Used in:** Ch2 (quantization section), App J.

### VF-QCD-4 — 单圈重整化常数与 Slavnov–Taylor 关系（单位 $\frac{\alpha_s}{4\pi\varepsilon}$，$\overline{\rm MS}$，协变规范参数 $\xi_g$）
$$\delta Z_2=-C_F\xi_g,\qquad \delta Z_3=\Big(\frac{13}6-\frac{\xi_g}2\Big)C_A-\frac43T_Fn_f,\qquad \delta Z_{1F}=-\Big(\xi_gC_F+\frac{3+\xi_g}4C_A\Big),$$
$$\delta\tilde Z_3=\frac{3-\xi_g}4C_A,\qquad \delta\tilde Z_1=-\frac{\xi_g}2C_A,\qquad \delta Z_1=\Big(\frac{17}{12}-\frac{3\xi_g}4\Big)C_A-\frac43T_Fn_f,\qquad \delta Z_4=\Big(\frac23-\xi_g\Big)C_A-\frac43T_Fn_f,$$
($Z_2$ quark field, $Z_3$ gluon field, $\tilde Z_3$ ghost field, $Z_{1F}$ quark–gluon vertex, $\tilde Z_1$ ghost–gluon vertex, $Z_1$ three-gluon vertex, $Z_4$ four-gluon vertex), and the four Slavnov–Taylor routes to the coupling renormalization
$$Z_g=\frac{Z_{1F}}{Z_2Z_3^{1/2}}=\frac{\tilde Z_1}{\tilde Z_3Z_3^{1/2}}=\frac{Z_1}{Z_3^{3/2}}=\frac{Z_4^{1/2}}{Z_3}\ \Rightarrow\ \delta Z_g=-\frac{\beta_0}{2},\qquad \beta_0=\frac{11}3C_A-\frac43T_Fn_f .$$
Feynman gauge ($\xi_g=1$): $\delta Z_2=-C_F$, $\delta Z_3=\frac53C_A-\frac43T_Fn_f$, $\delta Z_{1F}=-(C_F+C_A)$.
- **Status:** $\delta Z_2$, $\delta Z_3$: VL (VF-PDF-14, c_pdf §6, against Peskin–Schroeder ch. 16). The other five: **C** — recalled general-$\xi_g$ values; verified are the four Slavnov–Taylor identities, their $\xi_g$ independence and the reproduction of $\beta_0$ (v2-check Q3), and the Feynman-gauge values of $\delta Z_{1F}$, $\delta Z_2$, $\delta Z_3$. The Ch2 writer re-derives at least the Feynman-gauge quark–gluon vertex and reports it.
- **Used in:** Ch2 (`prop:prelim-beta`, vacuum-polarization example, `fig:qcd-vacuum-polarization`).

### VF-QCD-5 — $\beta$ 函数系数（本书归一化 $\mu^2\frac{d\alpha_s}{d\mu^2}=-\sum_{n\ge0}\beta_n\frac{\alpha_s^{n+2}}{(4\pi)^{n+1}}$）
$$\beta_0=\frac{11}3C_A-\frac43T_Fn_f,\qquad \beta_1=\frac{34}3C_A^2-4C_FT_Fn_f-\frac{20}3C_AT_Fn_f,$$
$$\beta_2=\frac{2857}{54}C_A^3+2C_F^2T_Fn_f-\frac{205}9C_FC_AT_Fn_f-\frac{1415}{27}C_A^2T_Fn_f+\frac{44}9C_FT_F^2n_f^2+\frac{158}{27}C_AT_F^2n_f^2 ;$$
SU(3): $\beta_0=11-\frac23n_f$, $\beta_1=102-\frac{38}3n_f$, $\beta_2=\frac{2857}2-\frac{5033}{18}n_f+\frac{325}{54}n_f^2$.
- **Status:** $\beta_0$: V (CONTEXT; VF-PDF-14; v2-check Q3–Q4a). $\beta_1$, $\beta_2$: **C** — group forms quoted from the literature (`Caswell1974`, `Jones1974`; `Tarasov:1980au`, `Larin:1993tp`); the reduction to the SU(3) numbers is verified (v2-check Q4b, Q4c). Four- and five-loop coefficients: literature only (`vanRitbergen:1997va`, `Czakon:2004bu`, `Baikov:2016tgj`, `Herzog:2017ohr`).
- **Used in:** Ch2 (`prop:prelim-beta`), Ch6 (VF-EE-9), Ch21.

### VF-QCD-6 — 跑动耦合：单圈与两圈解、$\Lambda$
One loop: $\displaystyle \alpha_s(Q^2)=\frac{\alpha_s(\mu^2)}{1+\frac{\beta_0}{4\pi}\alpha_s(\mu^2)\ln\frac{Q^2}{\mu^2}}=\frac{4\pi}{\beta_0\ln(Q^2/\Lambda^2)}$, i.e. $\frac1{\alpha_s(Q^2)}=\frac1{\alpha_s(\mu^2)}+\frac{\beta_0}{4\pi}\ln\frac{Q^2}{\mu^2}$.
Two loops, exact (separable): with $c=\beta_1/(4\pi\beta_0)$,
$$\ln\frac{Q^2}{\mu^2}=\frac{4\pi}{\beta_0}\Big[\frac1a-c\ln\frac{1+ca}{a}\Big]_{a=\alpha_s(\mu^2)}^{a=\alpha_s(Q^2)} .$$
Two loops, truncated explicit form (defines $\Lambda_{\overline{\rm MS}}$ at this order): $\displaystyle \alpha_s(Q^2)=\frac{4\pi}{\beta_0L}\Big[1-\frac{\beta_1}{\beta_0^2}\frac{\ln L}{L}\Big]$, $L=\ln(Q^2/\Lambda^2)$.
- **Status:** V (v2-check Q5: the exact two-loop solution is the analytic integral of the RGE, solved numerically; the truncated form agrees with it to 0.55 % on $5\le Q\le1000$ GeV for $n_f=5$).
- **Used in:** Ch2 (running-coupling section, `fig:qcd-running-coupling`).

### VF-QCD-7 — 数值：$\alpha_s(M_Z)$ 与 $n_f=5$ 的跑动
PDG 2024 world average $\alpha_s(m_Z^2)=0.1180\pm0.0009$ (`ParticleDataGroup:2024cfk`, review 9 "Quantum Chromodynamics", eq. (9.25), revised August 2023). With $M_Z=91.19$ GeV (rounded; the plot is insensitive to the last digit), $n_f=5$, $\beta_0=\frac{23}3$, $\beta_1=\frac{116}3$:

| $Q$/GeV | 5 | 10 | 20 | 50 | 91.19 | 200 | 500 | 1000 |
|---|---|---|---|---|---|---|---|---|
| one loop | 0.2028 | 0.1731 | 0.1510 | 0.1292 | 0.1180 | 0.1060 | 0.0948 | 0.0877 |
| two loop (exact) | 0.2123 | 0.1779 | 0.1533 | 0.1298 | 0.1180 | 0.1055 | 0.0940 | 0.0868 |
| two loop (truncated, $\Lambda^{(5)}=0.2262$ GeV) | 0.2135 | 0.1783 | 0.1534 | 0.1298 | 0.1180 | 0.1055 | 0.0940 | 0.0868 |

One-loop $\Lambda^{(5)}=0.0878$ GeV; slope of $1/\alpha_s$ in $\ln Q$: $\beta_0/(2\pi)=1.2202$.
- **Status:** VL for the PDG value (source read: `pdg.lbl.gov/2024/reviews/rpp2024-rev-qcd.pdf`, eq. (9.25)); V for the table (v2-check Q5).
- **Used in:** Ch2 (`fig:qcd-running-coupling`, running-coupling example). Do not quote other experimental numbers without a citation.

### VF-QCD-8 — 渐近自由的条件
$\beta_0>0\iff n_f<\frac{11C_A}{4T_F}=\frac{33}2$ (SU(3): $n_f\le16$). For SU(3), $\beta_1>0$ for $n_f\le8$ and $\beta_1<0$ for $9\le n_f\le16$.
- **Status:** V (v2-check Q4d, Q4e).
- **Used in:** Ch2 (asymptotic-freedom section, `fig:qcd-antiscreening`).

### VF-QCD-9 — 无量纲可观测量的重整化群方程
For a dimensionless observable $D(Q^2/\mu^2,\alpha_s(\mu))$ that is RG invariant, $\big[\mu^2\frac{\partial}{\partial\mu^2}+\beta(\alpha_s)\frac{\partial}{\partial\alpha_s}\big]D=0\Rightarrow D=D(1,\alpha_s(Q))$; at each order the coefficient of $\alpha_s^n(\mu)$ is a polynomial in $\ln(Q^2/\mu^2)$ fixed by lower orders and the $\beta_i$ (e.g. $d_2(\mu)=d_2+b_0d_1\ln\frac{\mu^2}{Q^2}$ in the $a=\alpha_s/\pi$ normalization of VF-EE-9).
- **Status:** A (characteristics; consistent with VF-EE-9, V).
- **Used in:** `prop:prelim-rg`.

---------------------------------------------------------------------------------------------------

## REF — reference-document analysis (refdoc S54; new in v2)

Source: `refdoc/REFDOC_ANALYSIS.md` §5.8 S54 and the reader notes. Formulas taken from the reference document were checked against its page images, never against `pdftotext` output; the reference document itself is **never cited** (WRITER_SPEC_v2 §6.10) — cite the primary literature or present the formula as our derivation.

### VF-REF-1 — 欧氏点在 $\omega$ 平面上的位置与投影算符
Rest frame, Euclidean $q=(iq^4,\mathbf q)$ with $|\mathbf q|\ge Q/2$: $\omega=2iMq^4/Q^2\in\mathcal I_Q=\{iy:|y|\le\sqrt3M/Q\}$, every point of $\mathcal I_Q$ attained; $\hat P^2=M^2\mathbf q^2/Q^2$; projector
$$T_2=\frac{3\nu}{2(\hat P^2)^2}\Big[\hat P_\mu\hat P_\nu-\frac{\hat P^2}3g_{\mu\nu}\Big]T^{\mu\nu},\qquad \hat P=P-\frac{P\cdot q}{q^2}q .$$
- **Status:** A (R5; re-derived by the refdoc synthesizer, both parts).
- **Used in:** `lem:dis-euclid-segment`, `lem:dis-ope-segment`, `fig:dis-euclid-segment`.

### VF-REF-2 — 离壳三角图的精确值与展开
$$Q^2I=\Phi^{(1)}(t,t)=\frac{4{\rm Li}_2(-\rho t)+\ln^2(\rho t)+\pi^2/3}{\sqrt{1-4t}},\qquad \rho=\frac2{1-2t+\sqrt{1-4t}},$$
$$Q^2I=L^2+\frac{\pi^2}3+t\Big(2L^2-4L-4+\frac{2\pi^2}3\Big)+t^2\big(6L^2-14L-11+2\pi^2\big)+O(t^3L^2),\qquad t=\frac{m^2}{Q^2},\ L=\ln\frac{Q^2}{m^2}.$$
- **Status:** V (R6; SYN `triangle_remainder.py`: closed form vs the one-dimensional integral to $<10^{-49}$, expansion residuals $O(t^3L^2)$; re-run in v2: `spec_v2/checks/fig_data.py`).
- **Used in:** `ex:sudakov-offshell`, `prop:appN-triangle-exact`, `fig:appN-triangle-remainder`.

### VF-REF-3 — 单圈三角图的 Collins 减除项、和与精确余项
Setting of `prop:appN-triangle-exact`: scalar triangle, massless internal lines, $p_1=(P,-\frac{m^2}{2P},\mathbf 0_T)$, $p_2=(\frac{m^2}{2P'},-P',\mathbf 0_T)$, $\tilde Q^2=2PP'$, $Q^2=(\tilde Q^2+m^2)^2/\tilde Q^2$; regions $\{S,C_1,C_2,H\}$, $\beta_S=\frac19$, $\beta_C=\frac13$.
$$\int C_H\Gamma=\tilde Q^{-2}\Big(\frac{\mu^2}{\tilde Q^2}\Big)^{\varepsilon}\mathcal A,\quad \int C_{C_1}\Gamma=\int C_{C_2}\Gamma=-\tilde Q^{-2}\Big(\frac{\mu^2}{m^2}\Big)^{\varepsilon}\mathcal A,\quad \int C_S\Gamma=\tilde Q^{-2}\Big(\frac{\mu^2\tilde Q^2}{m^4}\Big)^{\varepsilon}\mathcal B,$$
$$\mathcal A=\frac{\Gamma(1+\varepsilon)\Gamma(1-\varepsilon)^2}{\varepsilon^2\Gamma(1-2\varepsilon)},\qquad \mathcal B=\frac{\Gamma(1+\varepsilon)^2\Gamma(1-\varepsilon)}{\varepsilon^2};\qquad \sum_R\int C_R\Gamma\Big|_{\varepsilon\to0}=\tilde Q^{-2}\Big[\ln^2\frac{\tilde Q^2}{m^2}+\frac{\pi^2}3\Big],$$
$$\int r=-\frac{4m^2}{Q^4}+\frac{m^4}{Q^6}\Big(L^2-15+\frac{\pi^2}3\Big)+O\Big(\frac{m^6}{Q^8}L^2\Big)\quad(\text{no logarithm at NLP}).$$
Zero-bin in the light-cone representation $\propto\frac1{\varepsilon_{\rm UV}}-\frac1{\varepsilon_{\rm IR}}$ (set to zero, `asm:appN-values`); a parametric soft expansion over $[0,1]$ would give $-1/\varepsilon$.
- **Status:** V (R6 `check_remainder_d4.py`: remainder density integrates to $-0.0173434339581$ at $m^2=0.02$, $P=0.8$, $P'=1.3$; `check_algebra.py`; values (a) at $\varepsilon=0.3$ to 9–10 digits; SYN `triangle_remainder.py`; v2-check Q7 re-runs the remainder expansion).
- **Used in:** `ex:method-sudakov-subtraction`, `prop:appN-triangle-exact`, `fig:appN-triangle-remainder`, `fig:appN-triangle-regions`.

### VF-REF-4 — 有限减除色散关系与低阶矩
For every even $n_0>A+1$ ($A$ = polynomial growth exponent of $T_2$, independent of $Q$):
$$T_2(\omega)=\sum_{n<n_0}t_n\omega^{n-1}+4\omega^{n_0-1}\int_0^1dx\,\frac{x^{n_0-2}F_2(x)}{1-x^2\omega^2};\qquad t_n=4\!\int_0^1\!x^{n-2}F_2\ \text{for all even }2\le n<n_0\iff\lim_{y\to\infty}\frac{T_2(iy)}{iy}=0 .$$
- **Status:** A (R5); v2.3: threshold $n_0>A+1$ as in `prop:dis-dispersion-np` and App M §M.8 (X3 final report).
- **Used in:** `prop:dis-dispersion-np`, `prop:dis-low-moments`, App M §M.8.

### VF-REF-5 — $P^V_{q\bar q}$ 的积分
$\int_0^1P^{V(1)}_{q\bar q}=0.71931\,C_F\big(C_F-\frac{C_A}2\big)$ (in the normalization of the cited NLO kernels), so $P^+_{\rm NS}\neq P^-_{\rm NS}$ beyond LO.
- **Status:** V (R2 `check_Pplusminus.py`).
- **Used in:** `rem:pdf-ns-plusminus`.

### VF-REF-6 — 靶质量修正（$n$ 阶矩）
Leading target-mass correction to the $n$-th moment: $\frac{n(n-1)}{n+2}\frac{M^2}{Q^2}a_{n+2}$.
- **Status:** V (R4).
- **Used in:** `ex:dis-tmc-n2`, `prop:dis-tmc`.

### VF-REF-7 — Glauber 方向 $e_G$
$$e_G=n_B-n_A=(-1^+,+1^-,\mathbf 0_T),\quad e_G^2=-2,\quad n_A\cdot e_G=+1,\quad n_B\cdot e_G=-1,\qquad (l+it\sigma fe_G)^2-m^2=(l^2-m^2+2t^2f^2)+2it\sigma f(l^+-l^-).$$
- **Status:** V (R7, R8; v2-check Q8a, symbolic).
- **Used in:** `prop:method-glauber-deformation`, `rem:method-two-component`, App O §O.7, `fig:method-glauber-direction`, `fig:appO-deformation`.

### VF-REF-8 — 有质量入射线的分母（DFT 前提）
$(p_A-k)^2-m^2=-2p_A^+\Big(k^-+\frac{m^2}{2(p_A^+)^2}k^+\Big)+k^2$ for $p_A=(p_A^+,\frac{m^2}{2p_A^+},\mathbf 0_T)$.
- **Status:** A (elementary).
- **Used in:** `rem:dy-dft-premises`.

### VF-REF-9 — 程函线间的双胶子交换（box 与 crossed box）
Two infinite time-like eikonal lines, rapidity difference $Y>0$, gluon mass $m$, fixed transverse momenta, $a=\mathbf k_T^2+m^2$, $b=(\mathbf K-\mathbf k)_T^2+m^2$, $X=\mathbf T_A\cdot\mathbf T_B$:
$$J_{\rm box}=\frac{2\pi}{ab}(\pi+iY),\quad J_{\rm cross}=-\frac{2\pi iY}{ab},\quad c_{\rm box}=X^2,\quad c_{\rm cross}=X^2+\frac{C_A}2X,\qquad J_{\rm box}c_{\rm box}+J_{\rm cross}c_{\rm cross}=\frac{2\pi}{ab}\Big[\pi X^2-iY\frac{C_A}2X\Big],\quad p_{\rm opp}=-\frac{iY}\pi .$$
- **Status:** V (R3 `eikonal_box*.py`, $<5\times10^{-16}$ at 10 points, residues checked against brute-force $i\varepsilon$ quadrature; SYN rerun). Verify patch v2.3: claim N01 confirmed, but the result is known (`Meggiolaro:1996hf` eqs. (3.23)–(3.26), (3.34), (3.36); `Giordano:2006vv` eq. (4.24)): no novelty marker.
- **Used in:** `prop:dy-eikonal-twogluon`, `fig:dy-two-gluon-exchange`.

### VF-REF-10 — Glauber 算符参数化中的幺正性残差
$\mathcal V^\dagger\mathcal V-1=-\frac12C_A\chi^2({\rm Re}\,p_{\rm opp})X+O(\chi^3)$; with equal ordering weights $A_2=\frac12(-i\chi)^2(X^2+\frac14C_AX)$, i.e. a residual $-\frac14C_A\chi^2X$ (an artefact of the strict truncation; the exact value $p_{\rm opp}=-iY/\pi$ gives zero).
- **Status:** V (R3, R7, R8).
- **Used in:** `lem:appO-glauber-operator`.

### VF-REF-11 — 单个割图给出未来指向的 Wilson 线
$$\frac{iQ_a}{k^-+i0}+iQ_s\Big[\frac1{k^-+i0}-\frac1{k^--i0}\Big]=\frac{iQ_a}{k^--i0}\qquad(Q_s=-Q_a).$$
- **Status:** V (R8; v2-check Q8b).
- **Used in:** `ex:dy-future-vs-past`.

### VF-REF-12 — 等光锥时刻局域化的次序权重
Final group (all $k_e^+>0$, poles $z_e=\frac{k_{Te}^2}{2k_e^+}$ in the lower half-plane): $w_\pi=\prod_jz_j\big/\prod_m\sum_{l\ge m}z_{\pi(l)}$ ($N=2$: $w_{12}=\frac{z_1}{z_1+z_2}$); initial group (all $k_e^+<0$): **time-reversed**, $w_\pi=\prod_jz_j\big/\prod_m\sum_{l\le m}z_{\pi(l)}$; mixed signs: the weight of a sector is the product of the two groups' race weights (for $N=2$ with $k_1^+k_2^+<0$ the colour-order weight is 0 or 1); $\sum_\pi w_\pi=1$; as functions of $k^+$ the colour-order weights are continuous where at most one $k_e^+$ vanishes (with a kink there) and discontinuous where two or more vanish.
- **Status:** V (R8 `check_weights.py`; v2.3: X1 final report `checks_misc.py`, `refdoc/work_R7/check_weights_colour.py`, `fix_r2_scripts/l1_bound_quadrant.py`). The initial-group and mixed-sign forms correct the earlier entry (claim N13 refuted as stated: only the same-side lower-half-plane formula had been given); the race formula and $\sum w=1$ are classical (eikonal identity); never marked new.
- **Used in:** `lem:appO-joint-localization`.

### VF-REF-13 — 平方根构造是恒等式
With $\tilde f_A\equiv\tilde f_A^{\rm unsub}(y_B)\sqrt{\tilde S(y_A,y_n)/[\tilde S(y_A,y_B)\tilde S(y_n,y_B)]}$ and $\tilde f_B$ alike: $\tilde f_A\tilde f_B=\tilde f_A^{\rm unsub}\tilde f_B^{\rm unsub}/\tilde S(y_A,y_B)$ exactly, independent of $y_n$.
- **Status:** V (R6, symbolic).
- **Used in:** `lem:tmd-sqrt-identity`.

### VF-REF-14 — 未约化系数的例子
$-\frac{\kappa\pi^2}{2q^4}+O(m^2q^{-6}\ln q)$ (no logarithm, $m$-independent leading term).
- **Status:** V (R5).
- **Used in:** `ex:appM-unreduced`.

### VF-REF-15 — WW 近似中的 $g_\perp^{(v)}(0)$
$g_\perp^{(v)}(0)=\frac12\int_0^1du\,\phi_\parallel(u)/u\ne0$.
- **Status:** T (R3; literature `Mankiewicz:1999tt`).
- **Used in:** `prop:excl-meson-T`.

### VF-REF-16 — 全出射约定下的 Glauber 色因子
All-outgoing charges ($\sum_j\mathbf T_j=0$; initial lines $1/(n\cdot k+i0)$, final lines $1/(n\cdot k-i0)$, $k$ into the line): the Glauber part $\propto\mathbf T_b-\mathbf T_c-\mathbf T_d=\mathbf T_a+2\mathbf T_b$; Collins–Qiu factor $i\pi(g_1+2g_2)$.
- **Status:** V (R4 `checks_R4.py`; consistent with `prop:break-colour`, VF-GLA-7).
- **Used in:** `prop:break-colour`, Ch18.

### VF-REF-17 — 离壳三角形的 Symanzik 多项式与 Landau 解
$\mathcal F=m^2\alpha_0(\alpha_1+\alpha_2)+Q^2\alpha_1\alpha_2$; in Euclidean non-exceptional kinematics the only Landau solutions are at the simplex corners (zero-momentum massless lines).
- **Status:** A (R1).
- **Used in:** `rem:ir-euclid-corners`, `fig:ir-landau-simplex`.

### VF-REF-18 — 朴素归纳失败的显式表达式
$C_{C_2}\Gamma=\frac{m^2}{2PP'}\frac1{D_gD_2e_2}-\frac1{h_1D_2e_2}$; $(1-T_{C_1})T_S\Gamma=\frac1{D_ge_1}\Big(\frac1{e_2}-\frac1{h_2}\Big)$ (denominators as in App N §N.7).
- **Status:** V (R6 `check_algebra.py`).
- **Used in:** `ex:method-naive-induction`.

### VF-REF-19 — 类空正规子线的自能不可积
For on-shell $k$: $n_A(y_A)\cdot k=-\sqrt2\,|\mathbf k_T|e^{-y_A}\sinh(y_k-y_A)$, so the space-like line self-energy has a non-integrable $1/\sinh^2$ singularity inside the real-gluon phase space.
- **Status:** V (R6, c_tmd R4; re-derived by the refdoc synthesizer).
- **Used in:** `lem:tmd-soft-oneloop`.

---------------------------------------------------------------------------------------------------

## LAM — large-momentum effective theory (Ch22; new in v2)

Source: `frontier/lamet/LAMET.md` and its scripts `s1`–`s7` (190/190 pass, `logs/SUMMARY.txt`). Conventions: CONTEXT (the LaMET papers' $-ig$ Wilson lines converted; all one-loop kernels are even in $g$), WRITER_SPEC_v2 §3 rows 40–43. Paper claims marked *(read)* in the report were located in the arXiv sources.

### VF-LAM-0 — 记号
Ioffe time $\lambda\equiv P\cdot z=-P^zz$ for $z^\mu=z\hat e_z^\mu$; $a=\alpha_sC_F/(2\pi)$; $L_z=\ln(-z^2\mu^2e^{2\gamma_E}/4)$; $\ell_p=\ln(\mu^2/(4p_z^2))$, $p^z=|y|P^z$; $L_\zeta=\ln(\zeta_z/\mu^2)$, $\zeta_z=(2xP^z)^2$; plus distribution on a domain $D$: $\int_Dd\xi\,[g]^D_{+(1)}h=\int_Dd\xi\,g(\xi)[h(\xi)-h(1)]$. Dictionary: IJJSZ $\zeta=P^zz=-\lambda$, Radyushkin $\nu=-(p\cdot z)=-\lambda$, Ji et al. $\tilde\lambda=zP^z=-\lambda$.
- **Status:** V (LAMET §1.1).
- **Used in:** Ch22, Ch23.

### VF-LAM-1 — 准分布、准 ITD、赝分布
$$\tilde q_\Gamma(x,P^z;\mu)=N_\Gamma\int_{-\infty}^{\infty}\frac{dz}{4\pi}e^{ixP^zz}\langle P|[\bar\psi(z\hat e_z)\Gamma W[z\hat e_z,0]\psi(0)]_R|P\rangle,\quad N_{\gamma^z}=1,\ N_{\gamma^0}=\frac{P^z}{P^0};$$
$$\langle P|\bar\psi(z)\gamma^\alpha W[z,0]\psi(0)|P\rangle=2P^\alpha\mathcal M(\lambda,-z^2)+2z^\alpha\mathcal N(\lambda,-z^2),\quad \tilde q(x,P^z)=\int\frac{d\lambda}{2\pi}e^{-ix\lambda}\tilde h\Big(\lambda,-\frac{\lambda^2}{P_z^2}\Big),\quad \mathcal P(x,-z^2)=\int\frac{d\lambda}{2\pi}e^{-ix\lambda}\tilde h(\lambda,z^2),$$
light-cone ITD $I(\lambda,\mu)=\int_{-1}^1dx\,e^{ix\lambda}f(x,\mu)$; reduced ITD $\mathfrak M=\tilde h(\lambda,z^2)/\tilde h(0,z^2)$; support of $\mathcal P$ (diagram by diagram): $[-1,1]$, hence $\lambda\mapsto\tilde h(\lambda,z^2)$ is entire of exponential type $\le1$.
- **Status:** V (definitions, LAMET §1.2–1.3; support: Radyushkin's α-representation argument, [R] in PT as cited there).
- **Used in:** `def:lattice-quasi`, Ch22 definitions, `fig:lamet-ioffe`.

### VF-LAM-2 — 类空 Wilson 线算符的乘法重整化
$O^R_\Gamma(z,\mu)=Z_j^{-2}e^{-\delta m|z|}O^B_\Gamma(z)$ for $z\ne0$; in DR $\delta m=0$ and
$$Z_j=1+\frac{\alpha_sC_F}{4\pi}\frac{3}{2\varepsilon}+\dots,\qquad Z_O=Z_j^2=1+\frac{\alpha_sC_F}{4\pi}\frac3\varepsilon+\dots,\qquad \frac{d\ln O^R}{d\ln\mu^2}=\frac{3\alpha_sC_F}{4\pi}+O(\alpha_s^2);$$
no mixing with gluons or other flavours; lattice (chirally non-symmetric fermions): $O^R_\Gamma(z)=Z_\phi^2e^{-m|z|}O_{\Gamma'}(z)$, $\Gamma'=\Gamma+r_{\rm mix}{\rm sgn}(z)\{\slashed n,\Gamma\}+r_{\rm mix}^2\slashed n\Gamma\slashed n$ (no mixing for $\Gamma=\gamma^t$).
- **Status:** V for the one-loop anomalous dimension (LAMET s1 C: coefficient of $\ln\mu^2$ in $C_0$); TR for the all-order structure and the lattice mixing formula (`Ji:2017oey`, `Green:2017xeu`, `Ishikawa:2017faj`, `Constantinou:2017sej`, read). Grade of the theorem: [A].
- **Used in:** Ch22 renormalization theorem.

### VF-LAM-3 — 混合方案的换算
$\tilde h_{\rm hyb}=\tilde h_{\overline{\rm MS}}/C_0(z_S)=\tilde h_{\rm ratio}C_0(z)/C_0(z_S)$ for $|z|>z_S$, so $\mathcal C_{\rm hyb}(\alpha,z)=\mathcal C_{\rm ratio}(\alpha,z)+\frac{3a}2\delta(1-\alpha)\ln\frac{z^2}{z_S^2}\theta(|z|-z_S)$; $C_0=1+a(\frac32L_z+\frac52)$ ($\gamma^t$), $\frac72$ for $\gamma^z$.
- **Status:** V (LAMET §3.7, s1, s2).
- **Used in:** Ch22 schemes, `fig:lamet-hybrid`.

### VF-LAM-4 — 单圈坐标空间匹配核（$\overline{\rm MS}$，$\Gamma=\gamma^t$，$\sigma=0$；$\gamma^z$：$\sigma=1$）
$$\mathcal C(\alpha,L_z)=\Big[1+a\Big(\frac32L_z+\frac32\Big)\Big]\delta(1-\alpha)+a\Big\{\Big[\frac{1+\alpha^2}{1-\alpha}\Big]_+(-L_z-1)-\Big[\frac{4\ln(1-\alpha)}{1-\alpha}\Big]_++2(1+\sigma)(1-\alpha)\Big\}\theta(\alpha)\theta(1-\alpha),$$
moments $C_n=1+a\big[\big(\frac{3+2n}{2+3n+n^2}+2H_n\big)L_z+\frac{5+2n}{2+3n+n^2}+2(1-H_n)H_n-2H^{(2)}_n\big]$ ($+\frac{2a}{2+3n+n^2}$ for $\gamma^z$), $C_0=1+a(\frac32L_z+\frac52)$; RG: $\frac{d\mathcal C}{d\ln\mu^2}=a[\frac32\delta(1-\alpha)-B(\alpha)]$, $B=[\frac{1+\alpha^2}{1-\alpha}]_+$.
- **Status:** V (LAMET s1 A, $n\le10$ exact, vs `IzubuchiEtAl2018`; s1 C).
- **Used in:** Ch22 one-loop section.

### VF-LAM-5 — 比值（约化 ITD）核
$$\mathcal C^{\rm ratio}=\mathcal C-\delta(1-\alpha)C_0=a\Big\{\Big[\frac{1+\alpha^2}{1-\alpha}\Big]_+(-L_z-1)-\Big[\frac{4\ln(1-\alpha)}{1-\alpha}\Big]_++(1+\sigma)[2(1-\alpha)]_+\Big\},$$
identical to Radyushkin's reduced-ITD relation $\mathcal I(\nu,\mu^2)=\mathfrak M(\nu,z_3^2)+\frac{\alpha_sC_F}{2\pi}\int_0^1dw\,\mathfrak M(w\nu)\{B(w)[\ln(z_3^2\mu^2\frac{e^{2\gamma_E}}4)+1]+[4\frac{\ln(1-w)}{1-w}-2(1-w)]_+\}$ (his $\nu=-\lambda$).
- **Status:** VL (LAMET s1 B; `Radyushkin:2018cvn` read).
- **Used in:** Ch22.

### VF-LAM-6 — 坐标空间与动量空间因子化（部分子动量）
$$\tilde h(\lambda,z^2;\mu_R)=\int_{-1}^1d\alpha\,\mathcal C\Big(\alpha,-z^2\mu^2,\frac{\mu_R}\mu\Big)I(\alpha\lambda,\mu),\qquad \tilde q(x,P^z;\mu_R)=\int_{-1}^1\frac{dy}{|y|}C\Big(\frac xy,\frac{\mu_R}\mu,\frac{\mu}{|y|P^z}\Big)f(y,\mu),$$
$$C\Big(\xi,\frac\mu{p^z}\Big)=\int\frac{d\lambda}{2\pi}e^{-i\xi\lambda}\int_{-1}^1d\alpha\,e^{i\alpha\lambda}\,\mathcal C\Big(\alpha,\frac{\lambda^2\mu^2}{p_z^2}\Big);\qquad \int_{-1}^1dx\,x^n\mathcal P(x,-z^2)=C_n(-z^2\mu^2)a_{n+1}(\mu).$$
The argument of $C$ is the parton momentum $|y|P^z$; using $P^z$ is wrong at $O(\alpha_s)$.
- **Status:** V (algebraic consequence, LAMET §4.1; distributional Fourier identity checked at one loop to $10^{-9}$, s2).
- **Used in:** Ch22 matching theorem, `fig:lattice-matching`.

### VF-LAM-7 — 非物理区的单圈准 PDF（由 Feynman 规则直接计算）
On-shell massless quark $p=(p^z,0,0,p^z)$, $\Gamma=\gamma^0$, Feynman gauge; for $\xi\notin[0,1]$ all graphs are finite in $d=4$: vertex $a\int_0^1dy\frac{1-y}{|\xi-y|}$, sails $\frac a{1-\xi}\int_0^1dy\frac{\xi+y}{|\xi-y|}$, tadpole $-\frac a{|1-\xi|}$, sum
$$\xi>1:\ \tilde q^{(1)}=a\Big[\frac{1+\xi^2}{1-\xi}\ln\frac{\xi}{\xi-1}+1\Big],\qquad \xi<0:\ \tilde q^{(1)}=a\Big[-\frac{1+\xi^2}{1-\xi}\ln\frac{-\xi}{1-\xi}-1\Big].$$
- **Status:** V (LAMET s1 D1/D2, exact for 9 values; agrees with `IzubuchiEtAl2018` App. B and with the Fourier transform of the $\ln(-z^2)$ term of $\mathcal C$). "This work" result of the frontier agent (derivation from our Feynman rules) — not a new physics result.
- **Used in:** Ch22 one-loop section, `fig:lamet-oneloop`.

### VF-LAM-8 — 动量空间单圈核（$\overline{\rm MS}$ 与比值方案）
$$C^{\overline{\rm MS}}(\xi)=\delta(1-\xi)+a\begin{cases}\big[\frac{1+\xi^2}{1-\xi}\ln\frac\xi{\xi-1}+1+\frac3{2\xi}\big]^{[1,\infty]}_{+(1)}-\frac3{2\xi},&\xi>1\\[2pt]\big[\frac{1+\xi^2}{1-\xi}\big(-\ell_p+\ln(\xi(1-\xi))\big)-\frac{\xi(1+\xi)}{1-\xi}\big]^{[0,1]}_{+(1)},&0<\xi<1\\[2pt]\big[-\frac{1+\xi^2}{1-\xi}\ln\frac{-\xi}{1-\xi}-1+\frac3{2(1-\xi)}\big]^{[-\infty,0]}_{+(1)}-\frac3{2(1-\xi)},&\xi<0\end{cases}+a\,\delta(1-\xi)\Big(\frac32\ell_p+\frac52\Big),$$
$$C^{\rm ratio}(\xi)=\delta(1-\xi)+a\begin{cases}\big[\frac{1+\xi^2}{1-\xi}\ln\frac\xi{\xi-1}+1-\frac3{2(1-\xi)}\big]_{+(1)},&\xi>1\\[2pt]\big[\frac{1+\xi^2}{1-\xi}\big(-\ell_p+\ln(\xi(1-\xi))-1\big)+1+\frac3{2(1-\xi)}\big]_{+(1)},&0<\xi<1\\[2pt]\big[-\frac{1+\xi^2}{1-\xi}\ln\frac{-\xi}{1-\xi}-1+\frac3{2(1-\xi)}\big]_{+(1)},&\xi<0\end{cases}$$
each plus distribution on its own domain; for $\gamma^z$ add $2a(1-\xi)\theta(0<\xi<1)$ ($\overline{\rm MS}$) resp. $a[2(1-\xi)]^{[0,1]}_{+(1)}$ (ratio); $\delta$ functions at $\xi=\pm\infty$ dropped (they do not contribute for $f(y)\sim y^{-1+a'}$, $a'>0$).
- **Status:** VL (LAMET s2: pairing with Gaussian test functions equals the Fourier transform of the coordinate kernels to $10^{-9}$–$10^{-12}$, both $\Gamma$; `IzubuchiEtAl2018` eqs. (quasi-matching), (quasi-matching-alt) read).
- **Used in:** Ch22 one-loop section.

### VF-LAM-9 — 单圈核的尾部、矩与卷积定义域
$C^{\overline{\rm MS}}(\xi)\to-\frac{3a}{2|\xi|}$ and $C^{\rm ratio}(\xi)\to\mp\frac{4a}{3\xi^2}$ as $\xi\to\pm\infty$. Hence at $O(\alpha_s)$: the $\overline{\rm MS}$ quasi-PDF has no zeroth moment when $\int f\ne0$ ($\sim-\frac{3a}{2|x|}\int f$); in the ratio scheme $\int dx\,\tilde q=\int f$ but $\tilde q\to-\frac{4a}3{\rm sgn}(x)\langle y\rangle_{q+\bar q}/x^2$, so the first moment diverges logarithmically. Near $y=0$ the integrand of $\int\frac{dy}{|y|}C(\frac xy)f(y)$ is $-\frac{3a}{2|x|}f(y)(1+O(y))$ ($\overline{\rm MS}$), $\frac{3a}{2|x|}[\frac2\pi{\rm Si}(|x|z_SP^z)-1]f(y)(1+O(y))$ (hybrid, $\lambda_S=z_S|y|P^z$) and $O(|yf(y)|)$ (ratio): $\overline{\rm MS}$ and hybrid converge absolutely iff $\int_{|y|<\epsilon}|f|<\infty$, the ratio scheme needs only $\int|yf|<\infty$; for physical quark distributions (antiquarks at $y<0$) the $O(1)$ terms combine into $q-\bar q$, so all three schemes give finite quark quasi-PDFs when $q-\bar q$ and $y(q+\bar q)$ are integrable at small $y$ (e.g. a Regge-like sea $y^{-1-\delta}$, $\delta<1$).
- **Status:** V for the tails and moments (LAMET s1 E, s5 L2; tails also from the kernels of `IzubuchiEtAl2018`, who state the $\overline{\rm MS}$ condition $f\sim y^{-1+a}$, $a>0$). v2.3: the convolution-domain part was **corrected** — claim N09 refuted as originally stated (the planning text claimed that the hybrid kernel needs only $\int|yf|<\infty$ and that a Regge-like sea makes the $\overline{\rm MS}$ formula ill-defined); the corrected statement is that of `verify/claims/batch_N07_s1.md` §4.3 (one confirmation; numerical checks there: slopes $-5.0001$ vs $-5$ and $-2.26110$ vs $-2.26104$); no novelty marker.
- **Used in:** Ch22.

### VF-LAM-10 — 混合方案匹配核（修正形式）
$$C_{\rm hyb}(\xi)=C_{\rm ratio}(\xi)+\frac{3a}2\Big[-\frac1{|1-\xi|}+\frac{2\,{\rm Si}((1-\xi)\lambda_S)}{\pi(1-\xi)}\Big]^{[-\infty,\infty]}_{+(1)},\qquad \lambda_S=z_Sp^z,\qquad \int d\xi\,C_{\rm hyb}=1 .$$
The form printed in `Ji:2020brr` (eq. hybridm2) and `JiEtAl2021`, with $\frac1{|u|_+}\equiv\lim_{\beta\to0^+}[\theta(|u|-\beta)/|u|+2\delta(u)\ln\beta]$, gives $\int d\xi\,C_{\rm hyb}=1+3a\ln(\lambda_Se^{\gamma_E})$, i.e. it differs from the exact Fourier transform by $3a\ln(\lambda_Se^{\gamma_E})\delta(1-\xi)$; the later form of `Su:2022fiu` is correct.
- **Status:** V (LAMET s2: 24 checks to $10^{-12}$). Erratum confirmed: App Q row Q.8 (first corrected in print by `Chou:2022drv`).
- **Used in:** Ch22 schemes, `fig:lamet-hybrid`; App Q.

### VF-LAM-11 — 靶质量修正（$c=M^2/(4P_z^2)$）
$\gamma^z$: $\langle x^{N-1}\rangle_{\tilde q}=K_N\langle x^{N-1}\rangle_q$, $K_N=\sum_i\binom{N-i}ic^i$; with $f_\pm=\sqrt{1+4c}\pm1$,
$$\tilde q_{\gamma^z}(x)=\frac1{\sqrt{1+4c}}\Big[\frac{f_+}2q\Big(\frac{2x}{f_+}\Big)-\frac{f_-}2q\Big(-\frac{2x}{f_-}\Big)\Big]$$
(inverse series in LAMET §5.1). $\gamma^0$ (closed form of the frontier agent):
$$K^\perp_N=\sum_i\binom{N-i}i\frac{N-2i}Nc^i=K_N-\frac{2c}N\frac{dK_N}{dc},\qquad \tilde q_{\gamma^0}(x;c)=\tilde q_{\gamma^z}(x;c)-2c\int_0^1\frac{dy}y\,\partial_c\tilde q_{\gamma^z}\Big(\frac xy;c\Big),$$
so $K^\perp_1=K^\perp_2=1$ (no TMC for the normalization and for $\langle x\rangle$), $K^\perp_3=1+\frac23c$, $K^\perp_4=1+\frac32c$. At $O(c)$: $\tilde q_{\gamma^z}=q-c(xq'+q)$, $\tilde q_{\gamma^0}=q-c(xq'+3q)+2c\int_{|x|}^1\frac{dy}yq(\frac xy)$ (= `Braun:2018brg`). TMC commutes with the matching at fixed $P^z$.
- **Status:** V (LAMET s6, 40/40). $\gamma^z$ closed form: VL (`Chen:2016utp` read). $\gamma^0$ closed form: our derivation; claim N07 confirmed, known in part (`Chen:2016utp` helicity analogue, `Braun:2018brg` at $O(c)$, `Bhattacharya:2019cme` for the first two moments): no novelty marker.
- **Used in:** Ch22 power-correction section.

### VF-LAM-12 — Fourier 引理与端点二分
For a distribution $\rho$ supported in $[-1,1]$ and $r(\lambda)=\int d\alpha\,e^{i\alpha\lambda}\rho(\alpha)$, at fixed $P^z$ ($z^2=-\lambda^2/P_z^2$):
$$\int\frac{d\lambda}{2\pi}e^{-ix\lambda}\big[z^2\Lambda^2r(\lambda)\big]=+\frac{\Lambda^2}{P_z^2}\rho''(x);$$
if $q\sim(1-x)^b$ and $\rho_4\sim(1-x)^{b+\delta}$, the relative correction behaves as $\frac{\Lambda^2}{P_z^2}(1-x)^{\delta-2}$: $\delta=1$ gives $\Lambda^2/((1-x)P_z^2)$, $\delta=0$ gives $\Lambda^2/((1-x)^2P_z^2)$; near $x\to0$: $\Lambda^2/(x^2P_z^2)$.
- **Status:** V (LAMET s5 L1, $10^{-6}$). Our elementary reformulation; claim N08 confirmed, known in part (`Braun:2018brg` eq. (bR); both counting rules in `JiEtAl2021`): no novelty marker; the endpoint exponent $\delta$ itself is [C].
- **Used in:** Ch22 power-correction section, `fig:lamet-validity`.

### VF-LAM-13 — 扭度 4 的重整化子模型（大 $\beta_0$）
Leading IR renormalon at $w=1$: $B[H^\parallel]\to\frac{-4C_F}{1-w}[\alpha+\bar\alpha\ln\bar\alpha]X$, $B[H^\perp]\to\frac{-4C_F}{1-w}[\alpha+\bar\alpha\ln\bar\alpha+\alpha\bar\alpha]X$; model $\mathcal I^\parallel(\tau)=I(\tau)+\kappa z^2\Lambda^2\int_0^1d\alpha\,(\alpha+\bar\alpha\ln\bar\alpha)I(\alpha\tau)$, $|\kappa|\simeq\frac{\pi e^{5/3+2\gamma_E}}{4\beta_0}\simeq1.5$ (indicative, sign undetermined); momentum space
$$\mathcal Q^\parallel(x)=q(x)+\frac{\kappa\Lambda^2}{x^2P_z^2}\Big\{\int_{|x|}^1\frac{dy}y\frac{y^2}{[1-y]_+}q\Big(\frac xy\Big)+q(x)-|x|q'(x)\Big\}$$
with the $[0,1]$ plus distribution (so a term $q(x)\ln(1-x)$ appears when the integral is written over $[x,1]$). `Braun:2018brg` eq. (cR) omits $q(x)\ln(1-x)$ for both $R^\parallel_{\mathcal Q}$ and $R^\perp_{\mathcal Q}$; their eqs. (t4-Qparallel), (t4-Qperp) are correct.
- **Status:** V (LAMET s4, 20/20). The model is [P]/[C]. Erratum confirmed: App Q row Q.9.
- **Used in:** Ch22; App Q.

### VF-LAM-14 — 准 PDF 匹配核的阈值因子化（单圈成分）
$$C\Big(\xi,\frac{p^z}\mu\Big)\Big|_{\xi\to1}=H\Big(\frac{4p_z^2}{\mu^2}\Big)\,p^z\,J_f\Big(\frac{(1-\xi)p^z}\mu,\frac{4p_z^2}{\mu^2}\Big),\qquad H^{(1)}=a\Big(-2+\frac{\pi^2}{12}-\frac{L_\zeta^2}2+L_\zeta\Big),$$
$$\tilde J^{(1)}=a\Big(\frac{L_z^2}2+L_z+\frac{\pi^2}{12}+2\Big),\qquad {\rm Im}\,J_f^{(1)}=a\pi\,{\rm sgn}(z)(L_\zeta-1),$$
$$\frac{d\ln H}{d\ln\mu}=\Gamma_{\rm cusp}L_\zeta+\tilde\gamma_H,\quad \frac{d\ln\tilde J}{d\ln\mu}=\Gamma_{\rm cusp}L_z-\tilde\gamma_J,\quad \tilde\gamma_J=-\frac{\alpha_sC_F}\pi+O(\alpha_s^2);$$
here $L_\zeta=\ln(4p_z^2/\mu^2)$ (written $L_z$ by Ji–Liu–Su) and $L_z$ is the coordinate log (their $l_z$). The one-loop summed anomalous dimension $\Gamma_{\rm cusp}[\ln(\lambda^2e^{2\gamma_E})-i\pi\,{\rm sgn}z]$ is $\mu$ independent.
- **Status:** V at one loop (LAMET s3: coordinate space to $|\lambda|=10^5$, momentum space, phase sign). The all-order factorization is [A]; NNLO consistency with 41 singular terms (two constants fitted) TR (`Ji:2023pba` read).
- **Used in:** Ch23 `thm:yzliu-threshold`, `ex:yzliu-threshold-oneloop` (owner), `fig:yzliu-threshold`; Ch22 `prop:lamet-oneloop`(e) (endpoint structure). (v2.2: "Used in" lines aligned with FINAL_OUTLINE_v2, merge decision MD9.)

### VF-LAM-15 — 准 TMD 因子化（Collins–Soper 指数含因子 $\frac12$）
$$\tilde f(x,b_\perp,\mu,\zeta_z)\sqrt{S_r(b_\perp,\mu)}=H\Big(\frac{\zeta_z}{\mu^2}\Big)\exp\Big[\frac12\tilde K(b_\perp,\mu)\ln\frac{\zeta_z}\zeta\Big]f^{\rm TMD}(x,b_\perp,\mu,\zeta)\Big\{1+O\Big(\frac{\Lambda^2}{\zeta_z},\frac{M^2}{\zeta_z},\frac1{b_\perp^2\zeta_z}\Big)\Big\},$$
one loop ($a=\alpha_sC_F/(2\pi)$): $\tilde f^{(1)}=a[-\frac12L_b^2+L_b(\frac52-L_\zeta)-\frac32-\frac12L_\zeta^2+L_\zeta]$, $f^{{\rm TMD}(1)}=a[-\frac12L_b^2+(\frac32-\ln\frac\zeta{\mu^2})L_b+\frac12-\frac{\pi^2}{12}]$, $S_r^{(1)}=-2aL_b$, $\tilde K^{(1)}=-2aL_b$, hence $H^{(1)}=a(-2+\frac{\pi^2}{12}-\frac12L_\zeta^2+L_\zeta)$; momentum evolution $2\zeta_z\partial_{\zeta_z}\ln\tilde f=\tilde K+G$, $G^{(1)}=\frac{\alpha_sC_F}\pi(1-L_\zeta)$. The printed $e^{\tilde K\ln(\zeta_z/\zeta)}$ (`Ji:2019ewn` eq. (22), `JiEtAl2021`) leaves a residual $L_b(L_\zeta-\ln\frac\zeta{\mu^2})$ at one loop.
- **Status:** V (LAMET s4; YZLIU `check_qtmd_1loop.py`; independently re-checked by the spec-v2 drafter by hand). All-order statement [A]. Erratum confirmed: App Q row Q.11 (noted by the authors in PRD 105 (2022) 076014, footnote 1).
- **Used in:** Ch22 `thm:lamet-quasi-tmd`, `ex:lamet-qtmd-oneloop`, `prop:lattice-cs-kernel` (owner, MD9); Ch23 `prop:yzliu-qtmd-powercount`, `fig:yzliu-leading-region`; App Q.

### VF-LAM-16 — 由动量比值提取 Collins–Soper 核
$$\tilde K(b_\perp,\mu)=\frac1{\ln(P_1^z/P_2^z)}\ln\frac{C(\mu,xP_2^z)\,\tilde f(x,b_T,\mu,P_1^z)}{C(\mu,xP_1^z)\,\tilde f(x,b_T,\mu,P_2^z)}+\text{power corrections},$$
equivalently $\frac{\tilde f(\zeta_{z,1})}{\tilde f(\zeta_{z,2})}=\frac{H_1}{H_2}\big(\frac{\zeta_{z,1}}{\zeta_{z,2}}\big)^{\tilde K/2}=\frac{H_1}{H_2}\big(\frac{P_1^z}{P_2^z}\big)^{\tilde K}$; $S_r$ and all $\Gamma$-, flavour- and spin-independent factors cancel; $x$ independence tests leading power.
- **Status:** V at one loop (LAMET s4: returns $\tilde K^{(1)}=-2aL_b$). [A] given VF-LAM-15.
- **Used in:** Ch22 `prop:lattice-cs-kernel`, `prop:lamet-tmd-ratios` (owner, MD9); Ch23 (reference).

### VF-LAM-17 — Fourier 步骤：解析带、截断误差与可恢复模式数
If $|\tilde h(\lambda,-\lambda^2/P_z^2)|\le A(1+|\lambda|)^ke^{-m|\lambda|/P^z}$, then $\tilde q(x,P^z)$ is holomorphic in $|{\rm Im}\,x|<m/P^z$ (no endpoint singularities at finite $P^z$); with $k=0$ beyond $\lambda_L$:
$$\Big|\tilde q(x)-\int_{|\lambda|\le\lambda_L}\frac{d\lambda}{2\pi}e^{-ix\lambda}\tilde h\Big|\le\frac{AP^z}{\pi m}e^{-mz_L},\qquad z_L=\lambda_L/P^z;$$
numerically $e^{-mz_L}=0.079$ ($z_L=1$ fm) and $0.022$ ($1.5$ fm) for $m=0.5$ GeV. For data $|\lambda|\le\lambda_L$ of a support-$[-1,1]$ distribution, the time–frequency limiting operator has $\approx2\lambda_L/\pi$ eigenvalues near 1 (prolate spheroidal functions, `SlepianPollak1961`; Landau–Widom `LandauWidom1980`: $N(\epsilon)=\frac{2\lambda_L}\pi+\frac1{\pi^2}\ln\frac{1-\epsilon}\epsilon\ln\lambda_L+o(\ln\lambda_L)$): eigenvalues $>\frac12$: 3, 6, 10, 16 for $\lambda_L=5,10,15,25$.
- **Status:** V (LAMET s5 L3, s7 P1/P2). Lemma and bound: claim N10 confirmed, known in substance (Paley–Wiener type; applied to quasi-PDFs also in `Monahan:2026skv`): no novelty marker; the decay hypothesis for QCD Wilson-line correlators is [A]/[C].
- **Used in:** Ch22 Fourier section, `fig:lamet-fourier`.

### VF-LAM-18 — 类空关联函数的指数衰减（Ji–Liu–Su 2026，预印本）
Assumptions (spectrum with a gap $\Delta m$ above the external state; local tempered field with power bounds; locality). Then for the zero-momentum matrix element without one-particle intermediate states
$$f(0,\vec z)\equiv\langle\vec p=0|\phi(0,\vec z)\phi(0)|\vec p=0\rangle=2Z+O(e^{-\Delta m|\vec z|}),$$
with a sharp rate; QCD application (pion valence): $\tilde h^{\rm LA}=[A_2e^{i{\rm sgn}(z)\phi_2}+A_1e^{i{\rm sgn}(z)\phi_1}e^{-iP^zz}+A_3e^{i{\rm sgn}(z)\phi_3}e^{iP^zz}]e^{-\Lambda|z|}$, $\Lambda$ a heavy–light binding energy ($\approx0.5$ GeV).
- **Status:** TR (`Ji:2026vir`, arXiv only, read §§1–2, 5, 6). Theorem [R, R_cond] under the stated axioms; for QCD [A]/[C].
- **Used in:** Ch22 `thm:lamet-exp-decay`, `conj:lamet-decay-qcd` (owner); Ch23 `prop:yzliu-decay-extensions` (text only).

### VF-LAM-19 — 以强子动量代替部分子动量的 $O(\alpha_s)$ 差（早期匹配形式）
Replacing the parton momentum $|y|P^z$ by the hadron momentum $P^z$ in the one-loop $\overline{\rm MS}$ matching kernel changes it by
$$C\Big(\xi,\frac\mu{P^z}\Big)-C\Big(\xi,\frac\mu{|y|P^z}\Big)=-\frac{\alpha_sC_F}\pi\ln|y|\,\frac{1+\xi^2}{(1-\xi)_+}\,\theta(0<\xi<1)=-\frac{\alpha_s}\pi\ln|y|\Big[P_{qq}(\xi)-\frac32C_F\delta(1-\xi)\Big];$$
in the ratio scheme the difference is $-\frac{\alpha_s}\pi\ln|y|\,P_{qq}(\xi)$. The early range $\int_x^1$ also omits $|y|<|x|$ and $y<0$.
- **Status:** V (`verify/claims/batch_E01_s1.md` §7, `batch_E01_s2.md`; claim E06 confirmed; new in v2.3). The point is explicit in `IzubuchiEtAl2018` (text after eq. (27)); for quasi-GPDs `Ji:2015qla`.
- **Used in:** `rem:lamet-early-form`.

---------------------------------------------------------------------------------------------------

## YZL — Yizhuang Liu and collaborators (Ch23; new in v2)

Source: `frontier/yzliu/YZLIU.md` and its scripts. **Convention traps** (WRITER_SPEC_v2 §3 rows 4, 29, 31, 44, 45): their $D=\partial+igA$; $K$ = our $\tilde K$; three $\beta_0$ normalizations; $\Gamma_S$ vs $\gamma_{HH}$ sign conventions; $H$ multiplies $\tilde f$ in the RMP but $f^{\rm TMD}$ in PLB/APPB ($H_{\rm RMP}=H_{\rm PLB}^{-1}$); their $L_z\equiv\ln(\zeta_z/\mu^2)$ is our $L_\zeta$. Never print a Chinese name for Yizhuang Liu.

### VF-YZL-1 — 约定对照
$\beta_0^{\rm (JHEP\,2023/24)}=\beta_0^{\rm ours}/(2\pi)=-\beta_0^{\rm (PLB/APPB/RMP)}$; $\mu\,\frac d{d\mu}=2\mu^2\frac d{d\mu^2}$; $\gamma_{HH}$ defined by $\Gamma_{\rm cusp}(\alpha_s,\theta)=\theta\Gamma_{\rm cusp}(\alpha_s)+\gamma_{HH}(\alpha_s)+O(e^{-\theta})$ with $\Gamma_{\rm cusp}(\alpha_s,\theta)=\frac{\alpha_sC_F}\pi(\theta\coth\theta-1)+O(\alpha_s^2)$, $\gamma_{HH}^{(1)}=-\frac{\alpha_sC_F}\pi$; $\Gamma_S^{\rm PLB}=\gamma_{HH}$, $\Gamma_S^{\rm APPB}=-\gamma_{HH}$; $L_b=\ln(\mu^2/\mu_b^2)$ identical to ours; the heavy–light "Sudakov form factor $H_{HL}$" of JHEP 2023 is a *pair* of form factors, $H=|C_{HL}|^2$.
- **Status:** A (YZLIU §2; consistency checks in its scripts).
- **Used in:** Ch23 throughout.

### VF-YZL-2 — 离光锥软函数：HQET 形状因子、快度结构与本征软函数
$$S(b_\perp,Y,Y')=\lim_{t,t'\to\infty}\frac{W(t,t',b_\perp,Y,Y')}{\sqrt{Z(2t,b_\perp,Y)Z(2t',b_\perp,Y')}}={}_{v'}\langle Q\bar Q,\vec b_\perp|J(\vec b_\perp,v,v')|Q\bar Q,\vec b_\perp\rangle_v,\quad J=\eta^\dagger_{v'}(\vec b_\perp)\eta_v(\vec b_\perp)\psi^\dagger_{v'}(0)\psi_v(0),$$
$$\ln S(b_\perp,\mu,Y,Y')=(Y+Y')\tilde K(b_\perp,\mu)+\mathcal D(b_\perp,\mu)+O(e^{-(Y+Y')}),\qquad S_I\equiv e^{-\mathcal D},\qquad \mathcal D=2\mathcal D_1-\mathcal D_2,$$
on-light-cone form $\sqrt{S_I}=\lim_{\delta^+\to0}\sqrt{S(b_\perp,\mu,\delta^+,\delta^-=\delta^+)}/S(b_\perp,\mu,\delta^+,\hat z)$; one loop $S_I=1-\frac{\alpha_sC_F}\pi L_b$.
- **Status:** TR (`Ji:2019sxk`, `Liu:2022nnk` read in full); $\mathcal D_1=\frac12(\mathcal D+\mathcal D_2)$ checked by hand. Grade [A].
- **Used in:** Ch23 soft-function section, `fig:yzliu-soft-hqet`.

### VF-YZL-3 — $S_I$ 的反常维度与两圈结构（本书约定）
$$\mu^2\frac{d\ln S_I}{d\mu^2}=\gamma_{HH},\qquad \gamma_{HH}=-\frac{\alpha_sC_F}\pi+\frac{\alpha_s^2}{\pi^2}C_F\Big[C_A\Big(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}2\Big)+\frac59T_Fn_f\Big]+O(\alpha_s^3),$$
$$\ln S_I=-\frac{\alpha_sC_F}\pi L_b+\alpha_s^2\Big[-\frac{C_F\beta_0}{8\pi^2}L_b^2+\hat\gamma_{HH}L_b+c_2\Big]+O(\alpha_s^3),\qquad \hat\gamma_{HH}=\frac{C_F}{\pi^2}\Big[C_A\Big(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}2\Big)+\frac59T_Fn_f\Big],$$
$c_2$ not fixed by the RGE. The printed two-loop $\Gamma_S$ of `Liu:2022nnk` eq. (81) and `Ji:2021znw` eq. (72) has the wrong sign; the $L_b^2$ coefficient of `Liu:2022nnk` (81) and `JiEtAl2021` (208) is a factor 2 too large for their own $\beta_0$; `JiEtAl2021` eqs. (205)–(206) have inconsistent RGE signs.
- **Status:** V (YZLIU `check_GammaS2.py`: large-angle limit of the two-loop velocity-dependent cusp of `Becher:2009kw`/`KorchemskyRadyushkin1987`, zero-recoil check to $10^{-18}$; `check_RGE_structure.py`; the RGE consistency of the $L_b$ terms also re-checked by the spec-v2 drafter). Errata confirmed: App Q rows Q.12 (E08), Q.13 (E09), Q.15 (E11).
- **Used in:** Ch23; App Q.

### VF-YZL-4 — 双曲角与六种构型
$\theta(v_1,v_2)={\rm Arcosh}\frac{v_1\cdot v_2-i0}{\sqrt{v_1^2+i0}\sqrt{v_2^2+i0}}$; single-time-ordered subtracted soft functions are boundary values of one analytic function on $-\pi\le{\rm Im}\,\theta\le\pi$:

| $v_1$ | $v_2$ | orientation $v_1$ | orientation $v_2$ | $\theta$ |
|---|---|---|---|---|
| space-like | space-like | past | past | $Y$ |
| time-like | time-like | past | past | $Y-i\pi$ |
| time-like | time-like | past | future | $Y$ |
| space-like | space-like | past | future | $Y+i\pi$ |
| time-like | space-like | past | future | $Y+i\pi/2$ |
| time-like | space-like | past | past | $Y-i\pi/2$ |

Maps: $\cosh Y=\frac{1+z^2}{1-z^2}$ (DY) or $\frac{z^2+1}{z^2-1}$ (form factor); $\delta$ regulator: $S^+(\delta,\delta)=S^{-\dagger}(\frac{i\delta}{1+i0},\frac{i\delta}{1+i0})$, i.e. $\ln\frac{\mu^2}{2\delta^+\delta^-}\tilde K\to(\ln\frac{\mu^2}{2\delta^+\delta^-}+i\pi)\tilde K$.
- **Status:** TR (`Liu:2022nnk` §4.5–4.7, Table 1, App. F, H; transcribed from the rendered page). Grade [A] with explicit hypotheses (positive-norm gauge, Lorentz-invariant regulator with positive energy, regular spectral functions, uniform gap, order-by-order analyticity, uniform light-cone limit).
- **Used in:** Ch23 analyticity section, `fig:yzliu-theta-strip`.

### VF-YZL-5 — 准 TMD 因子化（与 VF-LAM-15 相同）与 CS 核比值
See VF-LAM-15; equivalently, in any on-light-cone regulator, $\tilde f=H\,\frac{f(x,b_\perp,\mu,\delta^-)}{S(b_\perp,\mu,\delta^+,\delta^-)}S(b_\perp,\mu,\delta^+,\hat z)$; $P^z\frac d{dP^z}\ln\tilde f=\tilde K+\mathcal G$, $\mathcal G^{(1)}=\frac{\alpha_sC_F}\pi(1-L_\zeta)$, $2\zeta_z\partial_{\zeta_z}\ln H=\mathcal G$; ratio $(\zeta_{z,1}/\zeta_{z,2})^{\tilde K/2}=(P_1^z/P_2^z)^{\tilde K}$.
- **Status:** V (YZLIU `check_qtmd_1loop.py`; LAMET s4). [A].
- **Used in:** Ch23 `prop:yzliu-qtmd-powercount`; Ch22 `thm:lamet-quasi-tmd` (the exponent; owner of the theorem, MD9).

### VF-YZL-6 — 硬核 $H$ 的单圈值与重—轻分解
$$H=1+\frac{\alpha_sC_F}{2\pi}\Big(-2+\frac{\pi^2}{12}-\frac{L_\zeta^2}2+L_\zeta\Big)=1+\frac{\alpha_sC_F}{4\pi}\Big(-L_\zeta^2+2L_\zeta-4+\frac{\pi^2}6\Big),\qquad H=C_{HL}^+C_{HL}^-,$$
$$C_{HL}^\pm=1+\frac{\alpha_sC_F}{8\pi}\Big(-4-\frac{5\pi^2}6+2L_\pm-L_\pm^2\Big),\quad L_\pm=L_\zeta\pm i\pi;\qquad \mu\frac d{d\mu}\ln H=\Gamma_{\rm cusp}L_\zeta+\gamma_C,\quad \gamma_C^{(1)}=-\frac{C_F}\pi\alpha_s .$$
The pair $(C_{HL}^\pm)^2$ is the LFWF kernel $H^\pm_{\rm LFWF}$; its one-loop phase is $\frac{\alpha_sC_F}2(1-L_\zeta)$ up to the ${\rm sgn}(z)$ convention.
- **Status:** V (YZLIU `check_HL_and_C1.py`; equal to the Ebert–Stewart–Zhao form). The product $C^+_{HL}C^-_{HL}$ was re-checked by hand by the spec-v2 drafter.
- **Used in:** Ch23.

### VF-YZL-7 — 两圈 $\tilde\gamma_H$、$\ln H^{(2)}$ 与 $c_H$（JHEP 2023 约定：$d/d\ln\mu$，$\beta_0^{\rm (b)}=\frac{11C_A}{6\pi}-\frac{n_f}{3\pi}$）
$$\tilde\gamma_H^{(1)}=-\frac{C_F}\pi,\qquad \tilde\gamma_H^{(2)}=\frac{1188\zeta_3-99\pi^2-1108}{432\pi^2}C_FC_A-\frac{36\zeta_3+6-7\pi^2}{12\pi^2}C_F^2+\Big(\frac1{24}+\frac{10}{27\pi^2}\Big)C_Fn_f,$$
$$\ln H^{(2)}=\frac{C_F\beta_0}{24\pi}L_\zeta^3-\frac14\Big(\Gamma^{(2)}_{\rm cusp}+\frac{C_F\beta_0}{2\pi}\Big)L_\zeta^2-\Big(\frac{C_F\beta_0}{4\pi}\Big(-2+\frac{\pi^2}{12}\Big)+\frac{\tilde\gamma_H^{(2)}}2\Big)L_\zeta+c_H,$$
$$c_H=\Big(\frac{241\zeta_3}{144\pi^2}+\frac{11\pi^2}{320}-\frac{559}{1728}-\frac{971}{324\pi^2}\Big)C_FC_A+\frac{-45\zeta_3-2\pi^4+30\pi^2-30}{24\pi^2}C_F^2+\frac{36\zeta_3+51\pi^2+1312}{1296\pi^2}C_Fn_fT_F$$
$=0.0725\,C_F^2-0.0840\,C_FC_A+0.1453\,C_Fn_fT_F$ (with $\beta_0\equiv\beta_0^{\rm (b)}$ and $\alpha_s$-expansion as in `Ji:2023pba`). The earlier $\gamma_C^{(2)}$ of `Ji:2019ewn` eq. (26) is wrong (corrected by the authors in `Ji:2023pba`).
- **Status:** V (YZLIU `check_gammaC2.py`, `check_RGE_structure.py`; $c_H$ numerics; $n_f$ parts agree with the large-$\beta_0$ results of `Liu:2023onm`); the full prediction agrees with 41 NNLO singular terms (TR, `Ji:2023pba`). Grade: RGE [A], two-loop values [P] (fixed order).
- **Used in:** Ch23.

### VF-YZL-8 — 准 TMD 的幂次计数（单线记号）
With $N(XY,d,s)$ the number of lines of mass dimension $d$ and spin $s$ between subgraphs $X,Y$ ($\ell$ = longitudinal collinear gluons) and power $\lambda_{\rm pc}^{F(H)+F(SC)}$, $\lambda_{\rm pc}\sim1/(b_\perp P^z)$:
$$F(H)=\sum_{s=0,1}[N(CH,1,s)+N(SH,1,s)]+N(CH,\tfrac32,\tfrac12)+\tfrac32\sum_{s=0,\frac12}N(SH,\tfrac32,s)-N(CH,1,\ell)-\tfrac72,\qquad F(SC)=\tfrac12N(SC,\tfrac32,\tfrac12)+N(SC,1,0);$$
leading region: $N(CH,\frac32,\frac12)=2$, $N(SH,\frac32,0)=1$, any number of longitudinal collinear gluons into $H$, any number of soft gluons into $C$: $F(H)=-\frac72+2+\frac32=0$; no super-leading regions.
- **Status:** A (YZLIU chk-hand; `Liu:2022nnk` eqs. (54)–(68) read).
- **Used in:** Ch23 quasi-TMD section, `fig:yzliu-leading-region`.

### VF-YZL-9 — 类空喷注函数与时空解析延拓
$\tilde J(\mu z)=\langle\Omega|\mathcal T\,W_{n,+}(zn_z)W_z^\dagger(zn_z)W_z(0)W_{n,-}(0)|\Omega\rangle$; to all orders in DR, $\tilde J(t=-i|z|,D)=\tilde J(z,D)$ (time-like heavy-quark jet function continued); one loop $\tilde J=1+\frac{\alpha_sC_F}{2\pi}(\frac12L_z^2+L_z+\frac{\pi^2}{12}+2)$, $\frac{d\ln\tilde J}{d\ln\mu}=\Gamma_{\rm cusp}L_z-\tilde\gamma_J$, $\tilde\gamma_J^{(1)}=-\frac{\alpha_sC_F}\pi$; two loops $\tilde\gamma_J^{(2)}=C_FC_A(-\frac{1396}{27}+\frac{23\pi^2}9+20\zeta_3)+C_Fn_f(\frac{232}{27}-\frac{2\pi^2}9)$ in units of $(\alpha_s/4\pi)^2$.
- **Status:** one loop V (= LAMET s3); continuation identity TR (`Ji:2023pba` App. C read), [A]; two-loop $\tilde\gamma_J$ A (YZLIU chk-hand from (A.4)–(A.5)).
- **Used in:** Ch23 threshold section.

### VF-YZL-10 — 反常维度代数
Basis $\{\Gamma_{\rm cusp},\gamma_F,\gamma_V,\gamma_s,\gamma_{HL}\}$:
$$\gamma_\phi=-\tfrac12\gamma_V-\tfrac12\gamma_s,\quad \gamma_J^{\rm thr}=\tfrac12\gamma_V-\tfrac12\gamma_s,\quad \tilde\gamma_J=2\gamma_{HL}-2\gamma_s,\quad \gamma_{HH}=2\gamma_{HL}-\gamma_s,\quad \tilde\gamma_H=\gamma_V+2\gamma_F+2\gamma_{HL}-\gamma_s;$$
DGLAP consistency at threshold: $2\gamma_\phi+\tilde\gamma_H-\tilde\gamma_J=2\gamma_F$ (endpoint form $P_{qq}\to\frac{2\Gamma_{\rm cusp}}{(1-z)_+}+2\gamma_\phi\delta(1-z)$).
- **Status:** V (YZLIU `check_gammaC2.py`; the DGLAP consistency is an identity of the relations, checked by the spec-v2 drafter by substitution). Structural relations [A]; two-loop values [P].
- **Used in:** Ch23.

### VF-YZL-11 — 重—轻 Sudakov 核的线性红外重整化子（大 $\beta_0$）
$${\rm Im}\,B(u)\to\frac{\mu}{p^z}\frac{C_Fe^{5/6}}{2\pi}\frac{{\rm sgn}(z)}{u-\frac12},\qquad A_{\rm asym}=-2\frac{\mu}{p^z}\sum_nr_n\alpha^{n+1},\ r_n=N_m\beta_0^n\Gamma(n+1),\qquad N_m=\frac{C_Fe^{5/6}}\pi\simeq0.977$$
($u=\beta_0t/2$ in Liu–Su's normalization); the real part has no linear renormalon; conjecture: the same $N_m$ beyond large $\beta_0$ ($0.622,\dots,0.524$ for $n_f=0,\dots,5$) [C].
- **Status:** A (YZLIU chk-hand: residue and numerical value); the statements are [P] (bubble chain).
- **Used in:** Ch23, `fig:yzliu-borel`.

### VF-YZL-12 — 时序无关性：末态求和恒等式与主等式
$$\int\frac{dE}{2\pi i}e^{-\nu|E|/\sqrt2}\Big[\prod_k\frac1{E-E_k-i\eta}-\prod_k\frac1{E-E_k+i\eta}\Big]=\sum_ke^{-\nu E_k/\sqrt2}\prod_{j\ne k}\frac1{E_k-E_j};$$
master equality (finite light-front lengths $L^\pm$, tilt $Y$, Z-factor subtractions, transverse links): $S^{\rm full}(L^+,L^-,b_\perp,\nu,Y,\varepsilon)=S_t^{\rm full}(-iL^-,-iL^+,b_\perp,\nu,Y,\varepsilon)$; invariant lengths below threshold, e.g. $x^2_{B,ij}=-\nu^2-b_\perp^2-\sqrt2i\nu(\lambda^L_i-\lambda^R_j)$ (real parts $\le-b_\perp^2-\nu^2<0$).
- **Status:** first identity V (YZLIU `check_HL_and_C1.py`, $n=2,3,4$); master equality TR (`Liu:2023pjb` read in full), [A] conditional on the perturbative Wightman structure of DR correlators.
- **Note (spec v2):** the proper complex Lorentz transformation relating $S_t$ and $S$ is $\Lambda(t,z)=(iz,it)$, the boost of rapidity $i\pi/2$ ($\cosh\frac{i\pi}2=0$, $\sinh\frac{i\pi}2=i$; determinant $+1$, preserves $t^2-z^2$), as in YZLIU §3.A6 and §6.3. YZLIU §3.A3 (summary of `Liu:2022nnk` App. F) writes $(it,iz)$: a slip — multiplication by $i$ reverses the sign of every interval and is not a Lorentz transformation. Checked by hand by the spec-v2 drafter.
- **Used in:** Ch23 time-ordering section, `fig:yzliu-complex-lorentz`.

### VF-YZL-13 — 二维 $U(N)$ Gross–Neveu 模型：扭度展开的绝对收敛
At $O(1/N)$ the twist expansion of the valence structure function $\mathcal E(z^2m^2,\lambda)$ converges absolutely, pointwise, for all $0<z^2<\infty$ and $\lambda\in i\mathbb R_{\ge0}$; renormalon poles at $t=n$ cancel between the hard function at power $p$ and the non-perturbative function at power $p+n$.
- **Status:** the four inequalities (4.2)–(4.5) behind the proof checked numerically on 4000 random points (YZLIU `check_GN_ineq.py`); the theorem TR (`Liu:2024omb` §§1–2.1, 4, 7 read). As a QCD statement [P] (model-exact).
- **Used in:** Ch23 models section.

### VF-YZL-14 — 超可重整二维 $O(N)$ 模型：动量空间 OPE 的阶乘增强
$$\mathcal H_{0,0,s_1=n}(p^2)\sim\frac1{(p^2)^n}\Big(\frac g{4\pi}\Big)^{n+1}\frac{d^n}{dt^n}\Big[\Big(\frac{m^2}{p^2}\Big)^t\psi(1-n-t)-\frac1t\Big]_{t=0}\xrightarrow{n\to\infty}-n!\frac{g^{n+1}}{(4\pi)^{n+1}}\frac{m^2}{(p^2)^{n+1}}+n!\frac{(-1)^ng^{n+1}}{(4\pi)^{n+1}}\frac1{m^2(p^2)^{n-1}}+\dots$$
the enhancements cancel only off-diagonally across powers; the momentum-space power expansion diverges, the coordinate-space one converges.
- **Status:** TR (`Liu:2025edu` eqs. (1.1)–(1.2), rendered page). [P] (model).
- **Used in:** Ch23 models section, Ch21 (pointer).

### VF-YZL-15 — 近阈重夸克偶素光生（修正后的归一化）
$$\mathcal M=\frac{8\sqrt2\pi\alpha_s(M_V)}{M_V^2}\phi^*(0)\,G(t,\xi)\,(\varepsilon_V^*\cdot\varepsilon),\quad G=\frac1{2\xi}\int_{-1}^1dx\,A(x,\xi)F_g(x,\xi,t),\quad A=\frac1{x+\xi-i0}-\frac1{x-\xi+i0},$$
$F_g=\frac1{(\bar P^+)^2}\int\frac{d\lambda}{2\pi}e^{i\lambda x}\langle P'|F^{a+i}(-\frac{\lambda n}2)F^{a+}{}_i(\frac{\lambda n}2)|P\rangle$; at $\xi\to1$: $|G|^2=\frac4{\xi^4}\{(1-\frac t{4M_N^2})E_2^2-2E_2(H_2+E_2)+(1-\xi^2)(H_2+E_2)^2\}$, $H_2=A^g_{2,0}+(2\xi)^2C^g_2$, $E_2=B^g_{2,0}-(2\xi)^2C^g_2$; $\frac{d\sigma}{dt}=\frac{\alpha_{\rm EM}e_Q^2}{4(W^2-M_N^2)^2}\frac{(16\pi\alpha_s)^2}{3M_V^3}|\psi_{\rm NR}(0)|^2|G|^2$. (`Guo:2023pqw` corrects a factor $\frac12$ in the gluon GPD of `Guo:2021ibg`.)
- **Status:** TR (`Guo:2021ibg`, `Guo:2023pqw` read). [P] (LO).
- **Used in:** Ch19 (owner of the topic), Ch23 pointer.

### VF-YZL-16 — Sivers 比值与介子形状因子
Sivers: the ratio of the quasi-Sivers to the unpolarized quasi-TMD at the same $(x,b_\perp,P^z)$ equals the light-cone ratio up to power corrections ($S_I$ and $H$ cancel; the sign follows the staple direction $\pm\hat z$). Meson form factor: $F(b_\perp,P,P',\mu)=S_I(b_\perp,\mu)\int dx\,dx'\,H(x,x')\tilde\psi^\dagger(x',b_\perp)\tilde\psi(x,b_\perp)+\dots$, $H=H_1/[H_2H_2]$, $H_1=H^{\rm Sud}(-Q^2)H^{\rm Sud}(-\bar Q^2)$, $Q^2=\sqrt{\zeta_z\zeta'_z}$.
- **Status:** TR (`Ji:2020jeb` §§I–II, `Ji:2019sxk`, `Liu:2022nnk` §5). [A]; one-loop checks [P].
- **Used in:** Ch23.

### VF-YZL-17 — 欧氏直角尖点与 $\gamma_{HH}$ 的两圈差
In units of $(\alpha_s/\pi)^2$: $\Gamma^{(2)}_{\rm cusp}(\frac\pi2)=C_FC_A(\frac{\pi^2}{24}-\frac{49}{36})+\frac59C_FT_Fn_f$ and $\gamma^{(2)}_{HH}=C_FC_A(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}2)+\frac59C_FT_Fn_f$, so
$$\Gamma^{(2)}_{\rm cusp}\big(\tfrac\pi2\big)-\gamma^{(2)}_{HH}=C_FC_A\Big(\frac{\zeta_3}2-\frac{\pi^2}{24}\Big)\approx0.190\,C_FC_A ;$$
at one loop both equal $-\alpha_sC_F/\pi$. The bent Euclidean soft functions (all cusps at Euclidean angle $\pi/2$) therefore give a wrong $\ln(\mu^2b^2)$ term at $O(\alpha_s^2)$.
- **Status:** V (`verify/claims/batch_E07_s1.md` §2.2, `batch_E07_s2.md`; claim E07(ii) confirmed; new in v2.3). The argument is that of `Ji:2019sxk`; the explicit value is our evaluation of the angle-dependent two-loop cusp anomalous dimension (`KorchemskyRadyushkin1987`).
- **Used in:** `thm:yzliu-soft-hqet` (status paragraph).

---------------------------------------------------------------------------------------------------

## FRO — other frontier results (Ch24 and others; new in v2)

Source: `frontier/others/OTHERS.md` and scripts `s1`–`s5` (36/36 pass). Items marked † in the report are unrefereed preprints: say so (WRITER_SPEC_v2 §6.11).

### VF-FRO-1 — Gordan 二择一与最小范数方向
For dual vectors $D_1,\dots,D_N$ on a finite-dimensional real space, exactly one of: (I) $\exists v$: $D_j\cdot v>0\ \forall j$; (II) $\exists\lambda_j\ge0$ not all zero with $\sum_j\lambda_jD_j=0$ (Landau point). If $0\notin K={\rm conv}\{D_j\}$, the min-norm point $w\in K$ satisfies $D_j\cdot w\ge|w|^2>0$.
- **Status:** V (OTHERS s1(a): 400 random instances, worst margin deficit $-10^{-14}$); classical (`Gordan1873`; the identification with Collins' geometric theorem: claim N02 confirmed, not found in print, elementary — a remark without novelty marker).
- **Used in:** Ch24 Landau section, `fig:front-gordan`; App D (pointer).

### VF-FRO-2 — Collins（2020，预印本）的物理区钳夹判据与符号条件
For $I(z)=\lim_{\epsilon\to0^+}\int_{\Gamma_0}d^dw\,B/\prod_j[A_j+i\epsilon]^{n_j}$ with $A_j$ at most quadratic and the sign condition: writing $A_j(w_S+\delta w)=D_j\cdot\delta w+\frac12\delta w\cdot E_j\cdot\delta w$, for every $v_0$ with $D_j\cdot v_0=0$ the non-zero $v_0\cdot E_j\cdot v_0$ of the relevant $j$ have one sign — the integration is trapped at $w_S$ iff the $D_j=\partial A_j(w_S)$ admit a Landau point. The sign condition holds for $k^2-m^2$ ($v_0\cdot E\cdot v_0=2\hat v^2\le0$), for eikonal (linear) denominators, non-relativistic propagators and approximated denominators quadratic in $k_T$ only.
- **Status:** V for where the sign condition holds (OTHERS s1(c)); theorem TR (`Collins:2020euz` read in full; arXiv only). Grade per FINAL_OUTLINE_v2 (D3: conservative; [R] only if re-derived in full).
- **Used in:** Ch24.

### VF-FRO-3 — 动量空间的 Coleman–Norton 方程（含无质量线与 Wilson 线）
Lines $k_j=\sum_L\eta_{jL}\ell_L+$(external), $\eta_{jL}\in\{0,\pm1\}$: trapped iff $\exists\lambda_j\ge0$ (not all zero, on the lines with $k_j^2=m_j^2$ resp. $n_j\cdot k_j=0$) with $\sum_j\eta_{jL}\lambda_j\Delta^\mu_j=0$ for every loop $L$, $\Delta_j=k_j$ (propagator) or $n_j$ (eikonal line); equivalently displacements $\Delta x_j=\lambda_j\Delta_j$ close around every loop (classical process).
- **Status:** V (OTHERS s1(b,d): collinear self-energy $(1-x,x)$, soft point, massive threshold, massive single on-shell line not trapped). Corollary (claim N03 confirmed, not new in substance: `Collins:2020euz` Thm 1 plus the Coleman–Norton closure); inherits the preprint status of VF-FRO-2.
- **Used in:** Ch24; `prop:ir-coleman-norton` (pointer).

### VF-FRO-4 — $\varphi^4_4$ 中 OPE 的收敛（Hollands–Kopper）
At fixed loop order $l$, massive Euclidean $g\varphi^4_4$, the remainder of the OPE summed over $[C]-[A]-[B]\le\Delta$ is bounded by $\ldots\times\frac1{\sqrt{\Delta!}}\big(\tilde Km|x|\sup(1,\frac{|\vec p|_n}m)^{n+2l+1}\big)^\Delta$ (full bound in OTHERS §2.5, their eq. (7)), so the OPE converges at every finite $|x|$.
- **Status:** TR (`Hollands:2011gf` read). [R] (model, fixed loop order).
- **Used in:** Ch24 OPE section, Ch21 (`thm:power-ope-convergence`).

### VF-FRO-5 — Jantzen 主恒等式（区域方法）
Under (1) disjoint covering domains $D_x$, (2) commuting expansions, (3) regularization of all integrals, (4) absolute convergence of each expansion on all of $D$ (+ exchange of summations):
$$\int_DI=\sum_xF^{(x)}-\sum_{\{x,x'\}}F^{(x,x')}+\sum_{\{x,x',x''\}}F^{(x,x',x'')}-\dots,\qquad F^{(x_1\cdots x_n)}=\int_DT^{(x_1)}\cdots T^{(x_n)}I;$$
overlap terms vanish when scaleless (the analogue of zero-bin subtractions).
- **Status:** TR (`Jantzen2011` §3 read). Identity [R](cond.); applicability [P].
- **Used in:** Ch24 regions section, Ch4 (`prop:ir-regions-minkowski`), Ch15 (zero-bin).

### VF-FRO-6 — Rothstein–Stewart 的 Glauber 拉氏量
$$\mathcal L_G^{\rm II(0)}=e^{-ix\cdot\mathcal P}\sum_{n,\bar n}\sum_{i,j=q,g}\mathcal O_n^{iB}\frac1{\mathcal P_\perp^2}\mathcal O_s^{BC}\frac1{\mathcal P_\perp^2}\mathcal O_{\bar n}^{jC}+e^{-ix\cdot\mathcal P}\sum_n\sum_{i,j=q,g}\mathcal O_n^{iB}\frac1{\mathcal P_\perp^2}\mathcal O_s^{j_nB},$$
$\mathcal O_n^{qB}=\bar\chi_nT^B\frac{\bar{\slashed n}}2\chi_n$, $\mathcal O_n^{gB}=\frac i2f^{BCD}\mathcal B^C_{n\perp\mu}\frac{\bar n}2\cdot(\mathcal P+\mathcal P^\dagger)\mathcal B^{D\mu}_{n\perp}$ (SCET conventions of Ch15).
- **Status:** TR (`RothsteinStewart2016` eq. (5.21) read). Construction [A].
- **Used in:** Ch15 (`rem:scet-glauber-dictionary`), Ch18, Ch24.

### VF-FRO-7 — 超领头对数的塔与闭式
$$\hat\sigma_n^{\rm SLL}=\Big(\frac{\alpha_s}{4\pi}\Big)^{n+3}L^{2n+3}\frac{(-4)^nn!}{(2n+3)!}\sum_{r=0}^n\frac{(2r)!}{4^r(r!)^2}C_{rn};\qquad \Delta\hat\sigma^{(S)}=-\hat\sigma_B\frac{4C_F}{3\pi}\alpha_s^3L^3\Delta Y\,{}_2F_2\Big(1,1;2,\frac52;-w\Big),\quad w=\frac{N_c\alpha_s}\pi L^2$$
($q\bar q$ singlet exchange, forward scattering); first SLL $\hat\sigma_1^{(S)}=\hat\sigma_B\frac4{15\pi^2}C_FN_c\alpha_s^4L^5\Delta Y$; ${}_2F_2(1,1;2,\frac52;-w)\simeq\frac32\frac{\ln w}w$ at large $w$ ($1.497$ at $w=10^8$).
- **Status:** V (OTHERS s4: term by term $n\le8$ from `Becher:2021zkk` eqs. (14), (19)). [A].
- **Used in:** Ch16 (`prop:jets-sll`), Ch24, `fig:front-sll`.

### VF-FRO-8 — 1-jettiness 中的相干性破坏对数（Banfi–Forshaw–Holguin）
$$\frac{d\sigma_1^{\rm CVL}}{dx_adx_bd\mathcal B}\simeq\sum_{a=q,g}\mathcal A_a\Big(\frac{\alpha_s}\pi\Big)^4(-i\pi)^2\frac1{480}\ln^6\frac1{\tau_1},\quad \mathcal A_q=\frac83N_c^2T_R^4f^q_Af^g_B\sigma^{(0)}_{qg},\quad \mathcal A_g=-\frac{32}3N_c^2T_R^4f^g_Af^q_B\sigma^{(0)}_{gq}$$
(PDFs at $\mu_F=\tau_1Q$; LL coherence-violation approximation).
- **Status:** TR (`Banfi:2025mra` read); v2.3: confirmed for the $qg\to q$ channel in SCET by `Becher:2026kbr` (two groups, different methods; claim E16). [V] for the standard exponentiation of $\tau_1$ at the level of this computation.
- **Used in:** Ch16, Ch24.

### VF-FRO-9 — $h\to\gamma\gamma$（$b$ 夸克圈）的端点因子化
Refactorization conditions $[\![\bar H_2(z)]\!]=-H_3J(zM_h^2)$, $[\![\langle O_2(z)\rangle]\!]=-\frac{g_\perp^{\mu\nu}}2\int_0^\infty\frac{d\ell_+}{\ell_+}J(-\bar n_1\cdot k_1\ell_+)S(\ell_+\ell_-)|_{z=\ell_-/\bar n_1\cdot k_1}$; renormalized theorem as in OTHERS §5.2 (`Liu:2020wbn` eq. (4.1)); leading double logarithms
$$\mathcal M_b\big|_{\rm LDL}=\mathcal M_0\hat L^2\sum_n\frac{n!}{(2n+2)!}\Big(-\frac{C_F\alpha_s}{2\pi}\hat L^2\Big)^n=\mathcal M_0\frac{\hat L^2}2\,{}_2F_2\Big(1,1;\frac32,2;-\frac{C_F\alpha_s}{8\pi}\hat L^2\Big).$$
- **Status:** series identity and its match to the NLO amplitude V (OTHERS s4); conditions and theorem TR (`Liu:2019oav`, `Liu:2020wbn` read). [A].
- **Used in:** Ch21 (NLP), Ch24, `fig:front-endpoint`.

### VF-FRO-10 — Yukawa 模型中单圈 $\overline{\rm MS}$ 分布可为负（Collins–Rogers–Sato）
$$f^{\rm renorm}_{q/p}(\xi;\mu)=a_\lambda(\mu)(1-\xi)\Big[\ln\frac{\mu^2}{\Delta(\xi)}-1+\frac{(m_q+\xi m_p)^2}{\Delta(\xi)}\Big]+O(a_\lambda^2),\quad \Delta(\xi)=\xi m_s^2+(1-\xi)m_q^2-\xi(1-\xi)m_p^2,\quad a_\lambda=\frac{\lambda^2}{16\pi^2};$$
for $m_q=0.3$, $m_p=1.0$, $m_s=1.5$ GeV: negative for $\xi>0.264$ at $\mu=0.8$ GeV (the OTHERS grid $0.02,\dots,0.98$ reports $[0.28,0.98]$), negative for $\xi>0.567$ at $\mu=1.2$ GeV, positive for all $\xi$ at $\mu=2.5$ GeV; $\xi\to1$ sign change at $\mu_*=m_s\exp\{\frac12[1-(m_q+m_p)^2/m_s^2]\}=1.70$ GeV; $\xi\to0$: bracket $\to\ln(\mu^2/m_q^2)$.
- **Status:** V (OTHERS s2: derivation of `CollinsRogersSato2022` eq. (55) from eq. (58), cut-off version; v2-check Q6: sign changes and $\mu_*$). [R] (model) — "MS-bar PDFs are positive at all scales" is [V].
- **Used in:** `conj:pdf-positivity` (Ch8, status paragraph), Ch24 positivity section, `fig:front-yukawa-pdf`.

### VF-FRO-11 — 由结构函数得到光子 PDF（LUXqed）
$$xf_{\gamma/p}(x,\mu^2)=\frac1{2\pi\alpha(\mu^2)}\int_x^1\frac{dz}z\Big\{\int_{\frac{x^2m_p^2}{1-z}}^{\frac{\mu^2}{1-z}}\frac{dQ^2}{Q^2}\alpha^2(Q^2)\Big[\Big(zp_{\gamma q}(z)+\frac{2x^2m_p^2}{Q^2}\Big)F_2\Big(\frac xz,Q^2\Big)-z^2F_L\Big(\frac xz,Q^2\Big)\Big]-\alpha^2(\mu^2)z^2F_2\Big(\frac xz,\mu^2\Big)\Big\},$$
$zp_{\gamma q}=1+(1-z)^2$, elastic parts $F_2^{\rm el}=\frac{G_E^2+\tau G_M^2}{1+\tau}\delta(1-x)$, $F_L^{\rm el}=\frac{G_E^2}\tau\delta(1-x)$, $\tau=Q^2/4m_p^2$. Point-like check: $xf_\gamma=\frac\alpha{2\pi}[1+(1-x)^2][\ln\frac{\mu^2}{m^2}-2\ln x-1]+\frac{\alpha m^2x^2(1-x)}{\pi\mu^2}$ (Frixione's $O(\alpha)$ result up to a power correction).
- **Status:** V (OTHERS s3); formula TR (`Manohar:2016nzj` eq. (6) read). [A].
- **Used in:** Ch11 (photon structure), Ch24.

### VF-FRO-12 — 领头阶 BK 方程
$$\frac{\partial S_Y(x,y)}{\partial Y}=\frac{\bar\alpha_s}{2\pi}\int d^2z\frac{(x-y)^2}{(x-z)^2(z-y)^2}\big[S_Y(x,z)S_Y(z,y)-S_Y(x,y)\big],\qquad \bar\alpha_s=\frac{\alpha_sN_c}\pi ;$$
the linearized kernel has eigenvalue $\bar\alpha_s\chi(\gamma)$ on $(x-y)^{2\gamma}$, $\chi(\gamma)=2\psi(1)-\psi(\gamma)-\psi(1-\gamma)$.
- **Status:** V (OTHERS s5; = VF-MISC-4). [A] within the eikonal (Regge) expansion.
- **Used in:** Ch17 (`thm:smallx-bk`), Ch24.

### VF-FRO-13 — 双部分子散射与重复计数的减除（Diehl–Gaunt–Schönwald）
$$\sigma=\sigma_{\rm SPS}+\sigma_{\rm DPS}-\sigma_{\rm sub},\qquad \frac{d\sigma_{\rm DPS}}{dx_1dx_2d\bar x_1d\bar x_2}=\sum\hat\sigma_{a_1b_1}\hat\sigma_{a_2b_2}\int d^2y\,\Phi^2(y\nu)F_{b_1b_2}(\bar x_i,y)F_{a_1a_2}(x_i,y),$$
$\Phi(u)\to1$ for $u\gg1$, $\Phi(u)=O(u^\delta)$ at small $u$, $\nu\sim Q$; $\sigma_{\rm sub}$ = the DPS formula with both DPDs replaced by their fixed-order splitting forms.
- **Status:** TR (`Diehl:2017kgu` §4.1 read). [A].
- **Used in:** Ch18 (`def:break-dpdf`), Ch24.

### VF-FRO-14 — 非全局可观测量的因子化（Becher–Neubert–Rothen–Shao）
$$\sigma(\beta,\delta)=\sum_{m\ge2}\big\langle\mathcal H_m(\{n\},Q,\delta)\otimes\mathcal S_m(\{n\},Q\beta,\delta)\big\rangle,\quad \mathcal S_m=\sum_{X_s}\langle0|S_1^\dagger\cdots S_m^\dagger|X_s\rangle\langle X_s|S_1\cdots S_m|0\rangle\,\theta(Q\beta-2E_{\rm out}),$$
$S_i(n_i)={\bf P}\exp(ig_s\int_0^\infty ds\,n_i\cdot A^a_s(sn_i){\bf T}_i^a)$ (their sign convention; convert $g\to-g$ for ours); RGEs $\frac d{d\ln\mu}\mathcal H_m=-\sum_{l\le m}\mathcal H_l\Gamma^H_{lm}$, $\frac d{d\ln\mu}\mathcal S_l=\sum_{m\ge l}\hat\Gamma^H_{lm}\otimes\mathcal S_m$.
- **Status:** TR (`Becher:2016mmh` §2 read). [A] ($e^+e^-$).
- **Used in:** Ch16 (`sec:jets-ngl`), Ch24.

### VF-FRO-15 — 双局域 PDF 算符的重整化：三角混合与矩约化
$$\begin{pmatrix}O\\A\\B\end{pmatrix}=\begin{pmatrix}Z_{OO}&Z_{OA}&Z_{OB}\\0&Z_{AA}&Z_{AB}\\0&0&Z_{BB}\end{pmatrix}\begin{pmatrix}O_{(0)}\\A_{(0)}\\B_{(0)}\end{pmatrix}\ \Rightarrow\ O=Z_{OO}O_{(0)}\ \text{in physical matrix elements};$$
moment reduction (OTHERS Prop. 8.1, hypotheses: local Joglekar–Lee/Henneaux classification for $\bar\psi\gamma^+(iD^+)^{N-1}\psi$, $F^{+\mu}(iD^+)^{N-2}F^+{}_\mu$; support in $[-1,1]$; generating-function identity): $\int_0^1dz\,z^{N-1}Z_{OO}(z)=Z^{(N)}_{\rm twist\text{-}2}$ for all $N$, $Z_{OO}$ fixed by its moments (Müntz–Szász for even/odd subsets).
- **Status:** triangular form TR (`Collins2011` eq. (11.20), pp. 407–412 read); Prop. 8.1 A (claim N04 confirmed, with prior art `Braun:2019qtp`; one-loop instance V in c_pdf §5.4). [A].
- **Used in:** `thm:prelim-composite-renorm` (remark), Ch8, Ch24 BRST section.

### VF-FRO-16 — 宽角振幅的红外森林公式（Ma 2020）
$$\Big[\sum_{F\in\mathcal F[A]}\prod_{\sigma\in F}(-t_\sigma)A\Big]_{\rm div}=0,$$
for massless wide-angle amplitudes with approximation operators $t_\sigma$ at the leading pinch surfaces (Feynman gauge); with the Ward identity this gives soft × jet × hard.
- **Status:** TR (`Ma2020` read). [A].
- **Used in:** Ch5 (pointer), Ch24.

### VF-FRO-17 — 小 $x$ 螺旋度演化：截距与 BER 的分歧（摘要层次）
Large-$N_c$ solution of the revised small-$x$ helicity evolution (Borden–Kovchegov): $\Delta\Sigma\sim\Delta G\sim g_1\sim(1/x)^{\alpha_h}$ with
$$\alpha_h\simeq3.66074\sqrt{\frac{\alpha_sN_c}{2\pi}}\quad(\text{BK}),\qquad \alpha_h^{\rm BER}\simeq3.66394\sqrt{\frac{\alpha_sN_c}{2\pi}}\quad(\text{infrared evolution equations});$$
the resummed $\Delta\gamma_{GG}(\omega)$ of BK agrees with the fixed-order anomalous dimensions through three loops and differs from BER from four loops on; the large-$N_c\&N_f$ analytic solution keeps a slight disagreement with BER and with Blümlein–Vogt.
- **Status:** T — transcribed from abstracts (OTHERS §9.5, abstract level); no computation by our agents. Grades: the BK results [A] (double-logarithmic approximation, large $N_c$ or large $N_c\&N_f$); the disagreement is an open problem, printed without a verdict (CLAIMS E34(iv), class Q3).
- **Literature:** `Kovchegov:2015pbl`, `Cougoulic:2022gbk`, `Borden:2023ugd`, `Adamiak:2023okq`, `Borden:2024bxa`, `Borden:2025ehe`; other side `Bartels:1995iu`, `Bartels:1996wc`, `Blumlein:1996hb` (identity fixed from the reference list of `Borden:2025ehe`).
- **Used in:** Ch24 small-$x$ section (Ch17 pointer).

---------------------------------------------------------------------------------------------------

## EXC — addition of spec v2.1

### VF-EXC-14 — 介子形状因子的软区份额（Isgur–Llewellyn Smith 型截断）
Fraction of the LO $u$-line integral of VF-EXC-6 that comes from gluon virtualities $\bar x\bar yQ^2<\mu_0^2$, with $c\equiv\mu_0^2/Q^2\le1$:
$$R(c)=\frac{\int_{\bar x\bar y<c}dx\,dy\,\frac{\phi(x)\phi(y)}{\bar x\bar y}}{\int_0^1\!\int_0^1dx\,dy\,\frac{\phi(x)\phi(y)}{\bar x\bar y}},\qquad R_{\rm as}(c)=c\big[5c-2(c+2)\ln c-4\big],$$
$$R_{\rm CZ}(c)=c\big[456c^3+352c^2-675c-132-(144c^3+768c^2+450c+36)\ln c\big],$$
for $\phi_{\rm as}=6x\bar x$ and $\phi_{\rm CZ}=30x\bar x(2x-1)^2$. Properties: $R(1)=1$, $R'(1)=0$, $R$ strictly increasing on $(0,1]$; $R_{\rm as}\simeq4c\ln\frac1c$ and $R_{\rm CZ}\simeq36c\ln\frac1c$ as $c\to0$ (the area of the region $\bar x\bar y<c$ is $c(1-\ln c)$). For $\mu_0^2=1$ GeV$^2$: $R_{\rm as}=0.87,\,0.62,\,0.15$ and $R_{\rm CZ}=0.98,\,0.90,\,0.48$ at $Q^2=4,\,10,\,100$ GeV$^2$. (Numerically the closed forms lose $\sim10^{-13}$ near $c=1$ by cancellation; evaluate $1-R$ there with care.)
- **Status:** V (c_exclusive `s4_pion_ff.py`, analytic = numerical; re-derived independently in spec v2.1 by `spec_v2/checks/vf_v21_checks.py` E1a–E1g: exact symbolic integration, the limits, 40-digit monotonicity, two-dimensional quadrature; log `vf_v21_checks.log`, 8/8 pass). The closed forms are a "derived here" result of the c_exclusive agent (CLAIMS N21, class K2 of WRITER_SPEC_v2 §6.5): no novelty wording (claim N21 confirmed; the 1989 Isgur–Llewellyn Smith papers could not be checked, so the novelty of the closed forms is not asserted); the soft-region argument itself is `IsgurLlewellynSmith1984`, `Isgur:1988iw`.
- **Used in:** `prop:excl-endpoint` (endpoint-area estimate combined with the exact curves, refdoc S40), optional `fig:excl-endpoint`.

---------------------------------------------------------------------------------------------------

## Verification register (outcomes of the verify patch v2.3)

Spec v2.1: keyed to the claims register `verify/CLAIMS.md` (E = erratum, N = new result, A = attribution) and to the proof extensions X1–X3; the classes are those of WRITER_SPEC_v2 §6.5 (K1–K5 for N-claims) and §6.13 (Q1–Q3 for E-claims). (v2.3: every claim is now decided; the column "outcome" records the decision.) **The formulas themselves may be used as stated** (with their own status code); what waits is the *claim* built on them (novelty wording, an erratum in App Q, a final appendix statement). Part A entries are not edited (v1 text); their pending claims are listed here only.

| VF ID | claim | class | outcome (verify patch v2.3) | target |
|---|---|---|---|---|
| VF-REF-9, VF-REF-10 | N01 | K1 | N01 confirmed but known (`Meggiolaro:1996hf`, `Giordano:2006vv`): printed without marker | Ch12, App O |
| VF-FRO-1 | N02 | K1 | N02 confirmed; remark without novelty marker (search-date sentence) | Ch24, App D |
| VF-FRO-3 | N03; E14 | K1; Q3 | N03 confirmed, not new in substance; E14 confirmed (Q3, attributed to `Collins:2020euz`) | Ch24, Ch4 |
| VF-FRO-15 | N04 | K1 | N04 confirmed as [A] with prior art `Braun:2019qtp` | Ch24, Ch8 |
| VF-LAM-11 | N07; E07(i) | K1; Q3 | N07 confirmed, known in part (no marker); E07(i) confirmed (Q3, attributed to `Chen:2016utp`); E07(ii): VF-YZL-17 (new) | Ch22 |
| VF-LAM-12 | N08 | K1 | N08 confirmed, known in part (no marker) | Ch22 |
| VF-LAM-9 | N09 | K1 | N09 refuted as stated; entry corrected (hybrid domain; $q-\bar q$ combination); no marker | Ch22 |
| VF-LAM-17 | N10 | K1 | N10 confirmed, known in substance (no marker) | Ch22 |
| VF-GLA-10 | N17 | K2 | N17 confirmed: attachment-sum form of `RogersMulders2010` eq. (34) (our derivation) | Ch18 |
| VF-GLA-6 | N18 | K2 | N18 confirmed: our compact derivation of known channel values | Ch18 |
| VF-TMD-9 | N20; E17 | K2; Q1 | N20 confirmed (no marker); E17 confirmed: App Q row Q.2 | Ch14; App Q |
| VF-EXC-14 | N21 | K2 | N21 confirmed; novelty of the closed forms not asserted (ILS 1989 unread) | Ch19 |
| VF-REF-2, VF-REF-3 | N12; X2 | K3 | N12 confirmed (never marked new); slot X2a delivered (`prop:appN-triangle-cs`) | App N, Ch5, Ch9 |
| VF-REF-12 | N13; X1 | K3 | N13 refuted as stated; entry corrected; final `lem:appO-joint-localization` | App O |
| VF-REF-14 | N15; X3 | K3 | N15 confirmed (never marked new) | App M |
| VF-REF-1, VF-REF-4 | X3 | — | X3 outcomes applied (FINAL_OUTLINE_v2 §00.4); VF-REF-4 threshold $n_0>A+1$ | App M, Ch7 |
| VF-REF-7, VF-REF-11 | X1 | — | X1 outcomes applied; formulas unchanged | App O, Ch9, Ch12 |
| VF-LAM-7 | N05 | K4 | N05 confirmed: our re-derivation of `IzubuchiEtAl2018` App. B | Ch22 |
| VF-LAM-14 | N06 | K4 | N06 confirmed: one-loop check of `Ji:2023pba` | Ch23 |
| VF-GLA-8 | N16; E18 | K4; Q1 | N16 confirmed (our proof of a statement of `Collins2007`); E18 confirmed: App Q row Q.4 | Ch18; App Q |
| VF-EE-8 | N24 | K4 | N24 confirmed (our derivation; the BM II hypotheses are met by massless QCD in covariant gauges) | Ch6 |
| VF-DY-12, VF-DY-13 | N25 | K4 | N25 confirmed (novelty not claimed) | Ch12 |
| VF-WL-2 | N26 | K4 | N26 confirmed (operator-level regulator: `Echevarria:2015byo`; novelty not claimed) | Ch3, App B |
| VF-LAM-8 | N27 | K4 | N27 confirmed (a verification) | Ch22 |
| VF-YZL-6, -9, -10, -11, -13 | N29 | K4 | N29 confirmed (cross-checks) | Ch23 |
| VF-GLA-9, VF-GLA-11 | N19 | K5 | N19 confirmed (auxiliary; not printed as results) | Ch18 |
| VF-BQ-3, VF-BQ-5 | N22 | K5 | N22 refuted (the illustrative shift was wrong: $-\pi^2$, independent of $X_A$); no illustration printed | Ch20 |
| VF-FRO-7, VF-FRO-11 | N28 | K5 | N28 confirmed (checked transcriptions) | Ch16, Ch24 |
| VF-LAM-10, VF-LAM-3 | E01 | Q1 | E01 confirmed: App Q row Q.8 (first corrected by `Chou:2022drv`) | App Q, Ch22 |
| VF-LAM-15, VF-YZL-5, VF-LAM-16 | E02 | Q1 | E02 confirmed: App Q row Q.11 (noted by the authors, PRD 105 footnote 1) | App Q, Ch23 |
| VF-LAM-13 | E03 | Q1 | E03 confirmed: App Q row Q.9 | App Q, Ch22 |
| VF-LAM-0 | E04 | Q1 (minor) | E04 confirmed: App Q row Q.10 | App Q |
| VF-LAM-2 | E05 | Q3 | E05 confirmed (Q3; the proviso is printed in Ch22) | Ch22 |
| VF-LAM-6 | E06 | Q2 | E06 confirmed: author correction (`tab:appQ-errata-b`); the exact $O(\alpha_s)$ difference is VF-LAM-19 (new) | App Q, Ch22 |
| VF-YZL-3 | E08, E09, E11 | Q1 | E08, E09, E11 confirmed: App Q rows Q.12, Q.13, Q.15 | App Q, Ch23 |
| VF-YZL-7 | E10; N29 | Q2; K4 | E10 confirmed: App Q row Q.14 (the correct value appears in `Ji:2023pba` without noting the discrepancy); N29 confirmed | App Q, Ch23 |
| VF-YZL-12 | E13; N29 | Q1 (terminology); K4 | E13 confirmed: App Q row Q.16; N29 confirmed | App Q, Ch23 |
| VF-YZL-15 | E12 | Q2 | E12 confirmed: author correction (`tab:appQ-errata-b`) | App Q, Ch19 |
| VF-FRO-2 | E15; A08 | Q3 | E15 confirmed (Q3, attributed to Collins); A08 confirmed | Ch24, App D |
| VF-FRO-8 | E16 | Q3 | E16 confirmed, now by two groups (`Banfi:2025mra`, `Becher:2026kbr`) | Ch16, Ch24 |
| VF-EXC-8 | E20 | Q1 | E20 confirmed: App Q row Q.5 | App Q, Ch19 |
| VF-REF-15 | E21 | Q1 (minor) | E21 confirmed: App Q row Q.6 | App Q, Ch19 |
| VF-CONV-23, VF-SCET-16 | E23 | Q1 | E23 confirmed (also in the journal version): App Q row Q.1 | App Q |
| VF-SCET-9 | E24 | Q3 | E24 confirmed (Q3) | Ch15 |
| VF-SCET-6 | E25 | Q1 (minor) | E25 confirmed: App Q row Q.3 | App Q, Ch15 |
| VF-BQ-4 | E26; N22 | Q1 (minor); K5 | E26 confirmed: App Q row Q.7; N22 refuted (no illustration printed) | App Q; Ch20 |
| VF-WL-10 | E27 | Q2 | E27 confirmed: the author's errata list (`tab:appQ-errata-b`) | App Q, Ch9, App F |
| VF-EE-12 | E28 | Q1 (conditional) | E28 confirmed as a convention remark (no App Q row) | Ch16 |
| VF-EE-10 | E29 | Q2 | E29 confirmed: author correction (`tab:appQ-errata-b`) | App Q, Ch6 |
| VF-DIS-8, VF-DIS-14 | E32 | Q3 (Q1 if a printed source is found) | E32 refuted (no printed source of the variant): nothing printed | Ch7 |
| VF-FRO-10 | E35; N28 | Q3; K5 | E35 confirmed (Q3); N28 confirmed | Ch8, Ch24 |
| VF-FRO-9, VF-FRO-12 | E34; N28 | Q3; K5 | E34: reported disagreements, no verdict (item (iii) withdrawn by its authors, `Balitsky:2009xg`); N28 confirmed | Ch21, Ch24 |
| VF-FRO-17 | E34(iv) | Q3 | E34(iv): no verdict (2026 status `Borden:2025ehe`) | Ch24 |

## CHANGELOG

**2026-10-10 — v2 assembled (spec-v2 writer-spec/figures/bibliography drafter).**
1. All 187 v1 entries (incl. the unused heading VF-EE-2) copied verbatim; three chapter numbers converted to v2 (VF-CONV-20, VF-CONV-22, VF-PDF-10); VF-CONV-5 gets a v2 note (SU(3) reduction of $\beta_1$ verified, status unchanged).
2. New group VF-QCD (9 entries) for Ch2, checked by `spec_v2/checks/vf_v2_checks.py` (36/36 pass; colour algebra, field-strength commutator, Slavnov–Taylor consistency of the one-loop $Z$ factors, $\beta$ coefficients, running-coupling numbers); PDG 2024 $\alpha_s(M_Z)$ read in the source.
3. New group VF-REF (19 entries) from refdoc S54, with the statuses given there; VF-REF-2/3/7/11 additionally re-checked by the spec-v2 checks.
4. New frontier groups VF-LAM (19), VF-YZL (16), VF-FRO (16), each with its verification status (V / VL / A / TR / C) and script or reading reference; the new code TR introduced; the LaMET/Liu notation $L_z=\ln(\zeta_z/\mu^2)$ rewritten as $L_\zeta$ throughout.
5. Pending-verification register added.

**2026-10-10 (later) — spec v2.1 (resumed writer-spec/figures/bibliography drafter).**
1. Pending-verification register rewritten and keyed to `verify/CLAIMS.md` (E/N/A IDs) and to X1–X3, with the classes K1–K5 / Q1–Q3 of WRITER_SPEC_v2 §6.5, §6.13; it now also lists the Part A entries tied to claims (VF-TMD-9, VF-GLA-6/-8/-9/-10/-11, VF-EXC-8, VF-REF-15, VF-CONV-23, VF-SCET-6/-9/-16, VF-BQ-3/-4/-5, VF-WL-2/-10, VF-EE-8/-10/-12, VF-DIS-8/-14, VF-DY-12/-13); Part A text unchanged.
2. New VF-EXC-14 (Isgur–Llewellyn Smith soft fractions, exact closed forms; status V, re-derived by `spec_v2/checks/vf_v21_checks.py`, 8/8 pass; CLAIMS N21, K2) and VF-FRO-17 (small-$x$ helicity intercepts and the BER disagreement; status T, abstract level; CLAIMS E34(iv)).
3. VF-LAM-17 cites `SlepianPollak1961` and `LandauWidom1980` (added to the bibliography in v2.1); group index updated (EXC 13 + 1, FRO 17).

**2026-10-10 (merge) — revision v2.2 (spec-v2 integrator).** "Used in" lines of VF-LAM-14, VF-LAM-15, VF-LAM-16, VF-LAM-18 and VF-YZL-5 aligned with the ownership of FINAL_OUTLINE_v2 (Ch22 owns the quasi-TMD theorem, the lattice CS kernel and TMD ratios; Ch23 owns the threshold factorization; merge decision MD9). No formula, status or check was changed.

**2026-10-11 — revision v2.3 (spec patcher; verify patch).** All pending flags resolved: the outcome is written in the status of VF-REF-9, VF-LAM-9, VF-LAM-10, VF-LAM-11, VF-LAM-12, VF-LAM-13, VF-LAM-15, VF-LAM-17, VF-YZL-3, VF-FRO-1, VF-FRO-3, VF-FRO-15, VF-EXC-14; **VF-LAM-9 corrected** (convolution domain of the hybrid kernel, $q-\bar q$ combination; claim N09 refuted as stated), **VF-REF-12 corrected** (initial group time-reversed, mixed signs give products, continuity with a kink; claim N13), VF-REF-4 threshold $n_0>A+1$ (X3 final report); VF-FRO-8 status (E16 confirmed by two groups); **new entries VF-LAM-19** (E06 difference) **and VF-YZL-17** (E07(ii) two-loop mismatch), group index updated; the register at the end now records the outcomes. No other formula changed.

