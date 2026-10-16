# VERIFIED_FORMULAS — formulas verified by the research agents

The monograph is 《QCD 因子化定理：严格证明、全阶论证与适用边界》. This file was built by the spec synthesizer on 2026-10-10.

## How to use this file

**Writers copy formulas from this file.** Each entry gives:
- the exact LaTeX in the binding conventions (`CONTEXT.md`, completed by `WRITER_SPEC.md` §3);
- its verification status;
- the path of the source that verified it.

The IDs `VF-<GROUP>-<n>` are the ones cited in `FINAL_OUTLINE.md`.

**If a formula you need is not here:**
1. Derive it yourself.
2. Mark it in your final report as "writer-derived".
3. List the check you made (limit, sum rule, numerical test).

Never copy a formula from memory or from a paper with different conventions without converting it and saying so.

**Status codes**

| code | meaning |
|---|---|
| **V** | derived and checked by a research agent with scripts (exact algebra or high-precision numerics), in the binding conventions |
| **VL** | as V, and also compared with the literature value after an explicit conversion (the agent read the source) |
| **A** | re-derived by the architect (`research/architect/BLUEPRINT.md` §0.4, §18.3, S1–S9) and consistent with the agents where they overlap, but not script-checked |
| **C** | general-group or general form recalled; only a special case (e.g. SU(3) numbers) is verified |
| **T** | **to verify** — preliminary, recalled, or convention-dependent (as of the spec audit, no c_tmd or c_glauber entry remains T for lack of a derivation file). The writer must re-derive or cross-check it and mark it as such in the text if the check cannot be completed |

**Source abbreviations**
- `c_x §k` is `research/c_x/DERIVATION.md` §k.
- `critic cN` is `research/critic/REVIEW.md` §10 (scripts in `research/critic/checks/`).
- `BP` is `research/architect/BLUEPRINT.md`.
- Check IDs in square brackets (e.g. [SS3e]) are the agents' script check labels.
- Logs are in `research/c_x/logs/`.

Common notation:
- $a_s$ denotes whichever expansion parameter the entry states.
- $L$ is defined in each entry.
- $\mathcal D_k(z)=[\ln^k(1-z)/(1-z)]_+$.
- $S_k\equiv S_k(N)=\sum_{j=1}^Nj^{-k}$, with $S_1(N)=\psi(N+1)+\gamma_E$ and $S_2(N)=\zeta_2-\psi'(N+1)$.
- $\bar N=Ne^{\gamma_E}$.

---------------------------------------------------------------------------------------------------

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
- **Used in:** Ch14, Ch15.

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
- **Used in:** Ch14 only.

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
| local operators, App L / Ch7: $\frac{dO}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\Gamma O$ | $\Gamma_{qq}=\gamma_{qq}$, $\Gamma_{q_kg}=2\gamma_{qg}$, $\Gamma_{gq}=\gamma_{gq}$, $\Gamma_{gg}=\gamma_{gg}$ |
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

## CHANGELOG

**2026-10-10 — spec audit (auditor agent).**
1. **TMD block upgraded from T.** `research/c_tmd/DERIVATION.md` (written 14:07, after this file was built; 17/17 scripts pass) was read in full. VF-TMD-1, -3, -4, -5, -6, -7 and -8 now carry c_tmd result numbers [R1]–[R12] and literature cross-checks. Added: the full $\mu,\zeta$ dependence of $\tilde C_{q/q}$, $\tilde C_{q/g}$; the SIDIS hard factor; $C^{(1)}_{qg}$; the small-$b$ error term $O((mb_T)^p)$. New entries VF-TMD-9 (ζ normalization; order of limits; space-like regulator lines) and VF-TMD-10 (small-$q_T$ asymptotics).
2. **VF-CONV-11** upgraded to V. Sign note made precise: Collins' $e^{+ik\cdot b}$ (his eq. (13.35)) concerns the soft factor and TMD FFs; for TMD PDFs the Collins-scheme papers use our forward convention.
3. **VF-CONV-23** $\Gamma(\beta)$ upgraded from T to V (c_tmd R4 + auditor structural check). Noted that the formula includes the line self-energies.
4. **VF-CONV-4:** source of the Collins section number stated.
5. **VF-GLA-11/12** no longer log-only: c_glauber §3, §4 are written. Status of diffractive photoproduction split (resolved [V]; direct covered by the DDIS proof in principle; H1/ZEUS tension).
6. **New entries:** VF-CONV-24 (Larin $\gamma^\mu\gamma_5$ replacement in the binding $\epsilon$ convention; the literature form has the opposite sign of $\epsilon$); VF-SUD-5 (dipole-formula normalization, ordered pairs, checked against VF-SCET-8); VF-BQ-6 ($B\to D\pi$ normalization with $P_L$ operators); VF-POL-3 (transversity kernel, status C); VF-GLA-13 (SLL order and FKS coefficient, quoted via c_glauber §4.5); VF-MISC-4 (BFKL intercept, BK kernel eigenvalue normalization, DLA; numerically verified); VF-MISC-5 (SIA LO normalization and angular decomposition).
7. **VF-CONV-17 corrected (later the same day).** Hadron-frame prefactor $z^{1-2\varepsilon}/(4N_c)$ instead of $1/(4N_cz)$ (the parton-frame value); found by the reference-document readers (REFDOC_ANALYSIS §2.4 OUR-1) and re-derived by the audit from the frame-change Jacobian.

