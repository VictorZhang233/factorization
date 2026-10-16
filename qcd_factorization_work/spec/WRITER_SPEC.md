# WRITER_SPEC — binding rules for the chapter writers

This file covers the monograph 《QCD 因子化定理：严格证明、全阶论证与适用边界》. The spec synthesizer wrote it on 2026-10-10.

**Companion files in `spec/`:**
- `FINAL_OUTLINE.md`: what each chapter must contain;
- `VERIFIED_FORMULAS.md`: which formulas to copy;
- `FIGURES_INDEX.md`: which figures to use or draw;
- `refs_merged.bib`, `key_aliases.tsv` and `REFS_NOTES.md`: what may be cited, and how.

**Order of authority** when documents conflict:
1. this file;
2. `FINAL_OUTLINE.md` (content, labels, tags);
3. `VERIFIED_FORMULAS.md` (formulas);
4. `CONTEXT.md`;
5. research files.

A writer who finds an actual error in a higher-ranked file fixes it in the chapter, explains the fix in the final report (§12), and never silently changes a tag or a canonical label.

---------------------------------------------------------------------------------------------------

## 1. Deliverable format

1. **One file per unit.** The files are `front.tex`, `ch01_intro.tex` … `ch22_summary.tex`, and `appA_lightfront.tex` … `appL_lightray.tex` (names in FINAL_OUTLINE §0.2).
2. **File structure.**
   - A chapter file starts with `\chapter{<中文标题>}\label{ch:<key>}`.
   - An appendix file starts with `\chapter{<中文标题>}\label{app:<key>}`. The master file issues `\appendix`, not the appendix file.
   - No `\documentclass`, `\usepackage`, `\begin{document}` or `\part` (the master file places the six `\part`s), and no `\bibliography` or `\bibliographystyle`.
   - `front.tex` contains the abstract, the reading guide and the notation table (FINAL_OUTLINE Front matter). It uses `\chapter*` with `\addcontentsline`.
3. **Macros.**
   - Use only the packages and macros of `common/preamble_fact.tex`. That file must not be modified.
   - No `\newcommand` or `\def` at file level. If a local abbreviation is indispensable, define it inside a group or environment, and report it.
   - If you need a macro that does not exist, ask in your report; until then write the expansion out.
4. **Encoding and comments.** Use UTF-8 and LaTeX `%` comments only. Do not put TODOs in the output. Use the placeholder protocols of §7 (figures) and §8 (citations) instead.
5. **Self-containment.** Each chapter must read correctly on its own. The first paragraph says what the chapter proves and at which level, using the tag vocabulary. Material from other chapters is cited with `\cref`, never repeated at length.

---------------------------------------------------------------------------------------------------

## 2. Language, typography, macros

1. **Language.**
   - Write in simplified Chinese, in an academic monograph style: complete sentences and no bullet-point prose inside the main text, except for lists of hypotheses and steps.
   - At first use of a technical term, add the English in parentheses, e.g. 「钳夹（pinch）」「程函线（eikonal line）」「快度发散（rapidity divergence）」. After that use the Chinese term consistently.
   - Glossary of preferred terms:

     | English | 中文 |
     |---|---|
     | factorization | 因子化 |
     | leading power | 领头幂次 |
     | power correction | 幂次修正 |
     | Wilson line | Wilson 线 |
     | soft factor | 软因子 |
     | collinear | 共线 |
     | ultrasoft | 超软 |
     | Glauber region | Glauber 区 |
     | coefficient function | 系数函数 |
     | hard part | 硬部分 |
     | parton distribution | 部分子分布 |
     | fragmentation function | 碎裂函数 |
     | splitting function | 分裂函数 |
     | anomalous dimension | 反常维度 |
     | subtraction | 减除 |
     | reduced diagram | 约化图 |
     | pinch surface | 钳夹面 |
     | rigorous / all-order argument / partial / conjecture / violated | 严格 / 全阶论证 / 部分 / 猜想 / 破坏 |
2. **Punctuation.**
   - In Chinese prose use full-width punctuation: ，。；：？！（）“”「」、.
   - Inside math use ASCII.
   - A displayed equation ends with ASCII punctuation inside the display (`,` or `.` before `\end{equation}`, preceded by `\,` or `\quad` if needed). Never put a full-width 「，」 inside math.
3. **Spacing.**
   - Do not put a space between Chinese text and `\cite`, `\cref` or inline math: 「见\cref{thm:dis-ope}的证明」, 「文献\cite{Collins2011}指出」, 「其中$x$为」.
   - The preamble inserts the CJK–Latin glue automatically, including after `\cref`.
   - Use `~` only in Western contexts and in location arguments (§8).
4. **Cross-references.**
   - Always use `\cref{...}`. Do not use `\ref` (except inside captions of tables referring to tables, where `\ref` is acceptable) and do not use hard-coded numbers.
   - Do not put several *section* labels in one `\cref`: the preamble lacks the multi-format and prints English. Write 「\cref{sec:a}与\cref{sec:b}」 instead (c_scet §6 item 18).
5. **Macros from the preamble.**
   - Symbols: `\as`, `\MSbar`, `\dd`, `\ii`, `\ee`, `\order{…}`, `\Tr`, `\TrD`, `\Trc`, `\sla{p}`, `\pT`, `\kT`, `\bT`, `\qT`, `\Lqcd`, `\Real`, `\Imag`, `\Disc`.
   - Tags: `\tagR`, `\tagA`, `\tagP`, `\tagC`, `\tagV`.
   - Environments: `\uses{…}`, `proofsketch`.
   - Use either the macros or the explicit forms, consistently within a chapter. Recommended: `\as` for $\alpha_s$, `\MSbar`, `\dd` in integrals, `\ii` for $i$ in exponentials and propagators, `\ee` for Euler's number.
6. **Notation for parts of a cut.** Use $H$, $J$ and $S$ for the hard, jet and soft subgraphs. A *reduced diagram* is 「约化图」.
7. **Numbers and units.** Write 「$\alpha_s(M_Z)=0.118$」 and GeV in roman (`\,\mathrm{GeV}`). Do not quote experimental numbers without a citation.
8. **Harmless warning.** The `cremark` head font produces "Font shape `TU/FandolKai-Regular(0)/m/it' undefined". This warning is harmless and is not to be "fixed" in chapter files.

---------------------------------------------------------------------------------------------------

## 3. Notation and conventions (decision D4; typeset in `front.tex` as `tab:front-notation`)

These conventions are binding for every chapter. The column "VF" refers to `VERIFIED_FORMULAS.md`. When quoting literature in other conventions, convert, and say so in a footnote or remark: 「（换算到本书约定：…）」.

| # | object | convention of this book | remarks / conversions | VF |
|---|---|---|---|---|
| 1 | metric, light front | $(+,-,-,-)$; $v^\pm=(v^0\pm v^3)/\sqrt2$; $v\cdot w=v^+w^-+v^-w^+-\mathbf v_T\cdot\mathbf w_T$ ($\mathbf v_T\cdot\mathbf w_T$ Euclidean) | hadron $A$ along $+z$, hadron $B$ along $-z$ | CONV-1 |
| 2 | light-like vectors (all chapters except Ch14) | $n_A=(1^+,0^-,\mathbf 0_T)$, $n_A\cdot v=v^-$; $n_B=(0^+,1^-,\mathbf 0_T)$, $n_B\cdot v=v^+$ | $n_B$ = Collins' $w_2$; the PDF line of $A$ runs along $n_B$ ($n_B\cdot A=A^+$). c_exclusive's $\bar n,n$ are our $n_A,n_B$ | CONV-1 |
| 3 | SCET vectors (Ch14 only) | $n=(1,0,0,1)$, $\bar n=(1,0,0,-1)$, $n\cdot\bar n=2$, $\bar n\cdot p=\sqrt2p^+$, $n\cdot p=\sqrt2p^-$; scalings for $(\bar n\cdot p,n\cdot p,p_\perp)$ | Rothstein–Stewart and the blueprint use the swapped order; convert | CONV-22 |
| 4 | covariant derivative, couplings | $D_\mu=\partial_\mu-igA^a_\mu t^a$, vertex $ig\gamma^\mu t^a$, ${\rm Tr}(t^at^b)=\frac12\delta^{ab}$, $C_F=\frac{N_c^2-1}{2N_c}$, $C_A=N_c$, $T_F=\frac12$ | **Collins 2011 uses $g\to-g$ relative to us** (his $D_\mu=\partial_\mu+igA_\mu$); BBL (NRQCD) use $D=\partial+igA$, so their $c_{2,3,4}$ signs flip | CONV-2/3, NRQ-1 |
| 5 | Feynman rules | quark $\frac{i(\slashed p+m)}{p^2-m^2+i0}$; gluon $\frac{-i}{k^2+i0}[g^{\mu\nu}-(1-\xi_g)\frac{k^\mu k^\nu}{k^2}]$; ghost $\frac{i}{p^2+i0}$; three-gluon $gf^{abc}[g^{\mu\nu}(k-p)^\rho+\dots]$ (incoming); ghost vertex $-gf^{abc}p^\mu$ ($p$ outgoing ghost) | = Peskin–Schroeder ch. 16 | CONV-3 |
| 6 | dimensional regularization | $D=4-2\varepsilon$, CDR ($\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$, $g^\mu{}_\mu=D$, ${\rm Tr}\,1=4$); bare scale $\mu_0$ ($g_0^2=4\pi\alpha_s\mu_0^{2\varepsilon}$) | pole origin always stated: $\varepsilon_{\rm UV}$ vs $\varepsilon_{\rm IR}$ (C14) | CONV-4 |
| 7 | $\overline{\rm MS}$ | $g_0^2=4\pi\alpha_s(\mu)\mu^{2\varepsilon}S_\varepsilon^{-1}Z_g^2$, $S_\varepsilon=(4\pi)^\varepsilon e^{-\varepsilon\gamma_E}$ | **Collins 2011: $S^{\rm C}_\varepsilon=(4\pi)^\varepsilon/\Gamma(1-\varepsilon)$**; ratio $S_\varepsilon/S^{\rm C}_\varepsilon=1+\frac{\pi^2}{12}\varepsilon^2$; changes constants multiplying $1/\varepsilon^2$ (TMD $\mathcal H$, $\tilde C$) | CONV-4, TMD-5 |
| 8 | running coupling | $\mu^2\frac{d\alpha_s}{d\mu^2}=-\frac{\beta_0}{4\pi}\alpha_s^2-\frac{\beta_1}{(4\pi)^2}\alpha_s^3$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$ | for $a=\alpha_s/\pi$: $b_0=\beta_0/4$, $b_1=\beta_1/16$ (Ch5); SCET/BS: $b=\beta_0/(4\pi)$ | CONV-5, EE-9 |
| 9 | expansion parameters | stated at the head of every formula block: $\frac{\alpha_s}{2\pi}$ (DIS, DY, PDFs), $a=\frac{\alpha_s}\pi$ ($e^+e^-$, CSS), $a=\frac{C_F\alpha_s}{4\pi}$ (SCET), $\frac{\alpha_s}{4\pi}$ (cusp $\Gamma_n$) | never mix within one display | — |
| 10 | power counting | $\lambda=m/Q$ (or $q_T/Q$); scalings in $(k^+,k^-,k_T)$: $A$-coll. $(1,\lambda^2,\lambda)$, $B$-coll. $(\lambda^2,1,\lambda)$, soft $(\lambda,\lambda,\lambda)$, usoft $(\lambda^2,\lambda^2,\lambda^2)$, Glauber $(\lambda^2,\lambda^2,\lambda)$ | **Sterman units:** $\omega$ = power of $\lambda_S=\lambda^2$; Libby–Sterman "soft" = our ultrasoft | CONV-19, REG-7/8 |
| 11 | e.m. current, $\Pi$, $R$ | $j^\mu=\sum e_q\bar q\gamma^\mu q$; $i\int e^{iqx}\langle Tj^\mu j^\nu\rangle=(q^\mu q^\nu-q^2g^{\mu\nu})\Pi$; $R=12\pi\,{\rm Im}\,\Pi(s+i0)$; $\sigma_{\mu\mu}=\frac{4\pi\alpha^2}{3s}$ | $\Pi_{\rm PS}=-e^2\Pi$ | CONV-12 |
| 12 | hadronic tensor | $W^{\mu\nu}=\frac1{4\pi}\int e^{iqz}\langle P|[j^\mu(z),j^\nu(0)]|P\rangle=(-g+\frac{qq}{q^2})F_1+\frac{\tilde P\tilde P}{P\cdot q}F_2$ | **general $F_L=(1+\frac{4M^2x^2}{Q^2})F_2-2xF_1$** (CONTEXT's $F_2-2xF_1$ is $M\to0$) | CONV-13 |
| 13 | Compton amplitude | $T^{\mu\nu}=i\int e^{iqz}\langle P|Tj^\mu j^\nu|P\rangle$; ${\rm Im}\,T_i=2\pi F_i$; $T_1$ even, $T_2$ odd in $\omega=1/x$ | free quark $T_2=4e_q^2\omega/(1-\omega^2)$ | CONV-14 |
| 14 | quark PDF | $f_{q/H}(\xi;\mu)=\int\frac{dw^-}{4\pi}e^{-i\xi P^+w^-}\langle P|\bar\psi(w)\gamma^+W[w,0]\psi(0)|P\rangle_c$, $w=(0^+,w^-,\mathbf 0_T)$; colour summed, target averaged; $f_{\rm ren}=Z\otimes f_{\rm bare}$ | support $|\xi|\le1$ (PT [R]; hadrons [A]) | PDF-1, PDF-4 |
| 15 | antiquark PDF | $f_{\bar q}(\xi)=-f_q(-\xi)$; $q(x)=f_q(x)$, $\bar q(x)=-f_q(-x)$ ($x>0$) | equivalent to the $\psi^c$ definition | PDF-1 |
| 16 | gluon PDF | $f_{g/H}(\xi)=\sum_j\int\frac{dw^-}{2\pi\xi P^+}e^{-i\xi P^+w^-}\langle P|G^{+j}_aW^{(A)}_{ab}G^{+j}_b|P\rangle_c$; $f_g(-\xi)=-f_g(\xi)$ | **CDR: partonic gluons averaged over $D-2=2-2\varepsilon$ polarizations** (averaging over 2 shifts $C_2^g,\Delta_{qg}$ by $+P_{qg}$) | PDF-2, CONV-6 |
| 17 | DGLAP | $\frac{\partial f_i}{\partial\ln\mu^2}=\sum_j\mathcal P_{ij}\otimes f_j$, $\mathcal P_{ij}=\frac{\alpha_s}{2\pi}P_{ij}+\dots$; $P_{ij}$ = LO kernel; $(f\otimes g)(x)=\int_x^1\frac{d\xi}\xi f(\xi)g(x/\xi)$ | MVV: $P^{(0)}_{\rm MVV}=2P$ | PDF-7, PDF-10 |
| 18 | anomalous dimensions | $\gamma_{ij}(N)=\int_0^1z^{N-1}P_{ij}$; local operators $\frac{dA^{(n)}}{d\ln\mu^2}=\frac{\alpha_s}{2\pi}\gamma(n)A^{(n)}$; $\Gamma_{q_kg}=2\gamma_{qg}$ | $\gamma^{(0)}_{\rm MVV}=-2\gamma$; Gross–Wilczek $\gamma_O=-\frac{\alpha_s}\pi\gamma$ | CONV-16, PDF-8 |
| 19 | twist-2 operators | $\langle P|O_i^{\mu_1\cdots\mu_n}|P\rangle=2A_i^{(n)}(P\cdots P-{\rm tr})$; $O_g^{+\cdots+}=\sum_jG^{+j}(iD^+)^{n-2}G^{+j}$ | $A_q^{(n)}=\int_0^1x^{n-1}[q+(-1)^n\bar q]$ | CONV-15, PDF-11 |
| 20 | fragmentation function | hadron frame $\mathbf p_{h,T}=0$, $w=(0^+,w^-,\mathbf 0_T)$: $d_{h/q}(z)=\frac{z^{1-2\varepsilon}}{4N_c}\sum_X\int\frac{dw^-}{2\pi}e^{ik^+w^-}{\rm Tr}[\gamma^+\langle0|W[\infty n_B,w]\psi(w)|hX\rangle\langle hX|\bar\psi(0)W[0,\infty n_B]|0\rangle]$, future-pointing lines; parton frame: $\frac1{4N_cz}$ with an explicit $\int d^{2-2\varepsilon}\mathbf p_{h,T}$ | **Audit correction:** the first version paired $\frac1{4N_cz}$ with the hadron frame, which is off by $z^{-2}$ (VF-CONV-17; REFDOC_ANALYSIS OUR-1). For massless partons in pure DR the bare partonic FF is $\delta(1-z)$ whatever the prefactor, so partonic coefficient functions are unaffected; the $z^{-2\varepsilon}$ fixes the scheme of the hadron-level definition | CONV-17 |
| 21 | plus distributions | $\int_0^1[g]_+h=\int_0^1g(h-h(1))$; $\mathcal D_k=[\ln^k(1-z)/(1-z)]_+$; **product convention** $g(z)\mathcal D_k=g(1)\mathcal D_k+\frac{g(z)-g(1)}{1-z}\ln^k(1-z)$ | $(1+z^2)\mathcal D_1=[\frac{(1+z^2)\ln(1-z)}{1-z}]_++\frac74\delta(1-z)$ | CONV-7, DY-12 |
| 22 | event-shape distributions | star distributions $[\cdot]_*$ (jet: reference $\mu^2$, soft: $\mu$); $\tau$-space plus distributions subtract at $\tau=0$; written $[\frac1\tau]_+$ with the sentence 「此处加号分布在 $\tau=0$ 处减除」 | never mix with row 21 in one formula | CONV-20 |
| 23 | Mellin transform | $\tilde f(N)=\int_0^1z^{N-1}f$; $S_1(N)=\psi(N+1)+\gamma_E$; $\bar N=Ne^{\gamma_E}$; $\langle\mathcal D_0\rangle=-S_1(N-1)$, $\langle\mathcal D_1\rangle=\frac12[S_1^2+S_2](N-1)$ | continuation from even $N$ unique under polynomial bounds (App K) | CONV-8, MISC-1 |
| 24 | Laplace transform (Ch14) | $\tilde t(\nu)=\int d\tau\,e^{-\nu\tau}\frac1{\sigma_0}\frac{d\sigma}{d\tau}$, $s=1/(e^{\gamma_E}\nu)$, $\ell=\ln(\nu e^{\gamma_E})$ | Becher–Schwartz | CONV-21 |
| 25 | $\gamma_5$, $\epsilon$ tensor | $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, $\epsilon^{0123}=+1$, ${\rm Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\gamma_5)=-4i\epsilon^{\mu\nu\rho\sigma}$; DR: HVBM + Larin finite renormalization | VGG use $\varepsilon_{0123}=+1$ (opposite sign). Larin's replacement in **our** convention: $\gamma^\mu\gamma_5=-\frac i6\epsilon^{\mu\nu\rho\sigma}\gamma_\nu\gamma_\rho\gamma_\sigma$ (the literature's $+\frac i6\epsilon_{\mu\nu\rho\sigma}\gamma^\nu\gamma^\rho\gamma^\sigma$ assumes $\epsilon_{0123}=+1$) | CONV-10, CONV-24, POL-1 |
| 26 | transverse tensors | $g_\perp^{\mu\nu}=g^{\mu\nu}-n_A^\mu n_B^\nu-n_B^\mu n_A^\nu$, $\epsilon_\perp^{\mu\nu}=\epsilon^{\mu\nu\rho\sigma}n_{A\rho}n_{B\sigma}$, $\epsilon_\perp^{12}=+1$ | | CONV-10 |
| 27 | Wilson lines | $W[b,a]=P\exp(ig\int_a^bdz\cdot A)$, later points left, $W\to U(b)WU^\dagger(a)$; $A(x)=\int\frac{d^4k}{(2\pi)^4}e^{-ikx}\tilde A(k)$, $k$ flows **into** the line; adjoint $W^{(A)}_{ab}=2{\rm Tr}[t^aWt^bW^\dagger]$ | | CONV-9 |
| 28 | eikonal rules | vertex $igt^av^\mu$, propagator $\frac i{v\cdot\ell+i0}$ (ℓ along the orientation); past-pointing $W[0,-\infty n]$: $\prod\frac{i}{n\cdot(k_1+\dots+k_j)+i0}$; future-pointing $W[\infty n,0]$: $\prod\frac{-i}{n\cdot(k_j+\dots+k_m)-i0}$; future − past for the two lines **attached at the same point**: $W[\infty n,0]-W[-\infty n,0]\ni2\pi i\,gt^an^\mu\delta(n\cdot k)\tilde A_\mu(k)$, where $W[-\infty n,0]=W[0,-\infty n]^\dagger$ (with $W[0,-\infty n]$ in place of $W[-\infty n,0]$ the difference is a principal value, not a $\delta$) | DIS: future-pointing ($-i0$); DY: past-pointing ($+i0$); conjugate lines: complex conjugate | WL-1, WL-12 |
| 29 | cusp, CS kernel | $\Gamma_{\rm cusp}=\sum(\frac{\alpha_s}{4\pi})^{n+1}\Gamma_n$, $\Gamma_0=4C_F$; $\gamma_K=2\Gamma_{\rm cusp}=\frac{2\alpha_sC_F}\pi+\dots$; $\tilde K=-\frac{\alpha_sC_F}\pi\ln\frac{\mu^2b_T^2}{b_0^2}$; one-loop cusp with Minkowskian angle $\beta$: $\Gamma(\beta)=\frac{\alpha_sC_F}\pi(\beta\coth\beta-1)$ (line self-energies included) | BS arXiv $\Gamma_1$ misprint | CONV-18/23, TMD-1/2 |
| 30 | TMD Fourier transform | $\tilde f(x,b_T)=\int d^{2-2\varepsilon}k_T\,e^{-ik_T\cdot b_T}f(x,k_T)$; $b_0=2e^{-\gamma_E}$, $\mu_b=b_0/b_T$; cross sections $\int\frac{d^2b_T}{(2\pi)^2}e^{+iq_T\cdot b_T}\tilde f_A\tilde f_B$ | **sign note (made precise by the audit):** Collins 2011 eq. (13.35) defines the soft factor and the TMD *fragmentation* functions with $e^{+ik_T\cdot b_T}$ (survey §0.3, read in the book); the Collins-scheme TMD-*PDF* papers (Aybat–Rogers 2011 eqs. (11), (27); c_tmd §2.1) use our forward convention. Any source with $e^{+ik_T\cdot b_T}$ differs by $b_T\to-b_T$, which flips $b_T$-odd (T-odd/spin) structures; check the sign at each transcription | CONV-11 |
| 31 | TMD scheme | Collins' definition (`def:tmd-collins`), $\zeta=M^2x^2e^{2(y_P-y_n)}=2(xP^+)^2e^{-2y_n}$, **$\zeta_A\zeta_B=Q^4$** in cross sections; space-like regulator lines; order of limits: light-like limit at fixed $\varepsilon$, then $\overline{\rm MS}$, then $\varepsilon\to0$ | other schemes in `rem:tmd-schemes`; Aybat–Rogers eq. (3) has a spurious factor 2 in $\zeta$ | TMD-3/4/9 |
| 32 | spin conventions (TMD) | Trento conventions (`BacchettaEtAl2004`) for $f_{1T}^\perp$, $h_1$, Collins and Boer–Mulders functions | Sivers sign (SIDIS) negative for attractive FSI in the spectator model (verified: c_tmd R12 = Bacchetta–Conti–Radici 2008) | TMD-8 |
| 33 | DY normalization | $\sigma_0=\frac{4\pi\alpha^2}{3N_cQ^2}$; $\hat s\,d\hat\sigma_{ij}/dQ^2=\sigma_0e_q^2\Delta_{ij}(z)$; $\Delta_{qg}$ per one (anti)quark and one gluon; TMD cross sections carry $\sigma_0/s$ (`thm:tmd-factorization`) | c_tmd writes $\sigma_0$ for our $\sigma_0/s$ | DY-1, DY-8, TMD-10 |
| 34 | exclusive | $f_\pi\approx130$ MeV ($F_\pi=f_\pi/\sqrt2$); DA with $x$ = quark fraction; GPD $\xi=\frac{p^+-p'^+}{p^++p'^+}$ ($\xi_{\rm Ji}=2\xi$); Diehl-2003 light-front normalization | VGG: $f_\pi=92.4$ MeV | EXC-1/2/12 |
| 35 | NRQCD | $\Gamma=\sum_n\frac{2{\rm Im}f_n}{m_Q^{d_n-4}}\langle O_n\rangle$, $m_Q$ = heavy-quark pole mass; meson mass $M=2m_Q$ only where stated | BBL sign flips (row 4) | NRQ-1…4 |
| 36 | Borel transform | $R=\sum r_n\alpha_s^{n+1}$, $B[R](t)=\sum r_nt^n/n!$, $u=\beta_0t/(4\pi)$; pole at $u_0$ ⇒ ambiguity $(\Lambda^2/Q^2)^{u_0}$ | | `def:power-borel` |
| 37 | sums over colour, spin | averages: quark spin $\frac12$, colour $\frac1{N_c}$; gluon polarization $\frac1{D-2}$, colour $\frac1{N_c^2-1}$; polarization sums $-g_{\mu\nu}$ only where the Ward identity allows (one external gluon), otherwise with ghost subtraction | | CONV-6, WL-9 |

---------------------------------------------------------------------------------------------------

## 4. Theorem environments, tags, qualifiers, status paragraphs

1. **Environments.**
   - `definition`, `theorem`, `lemma`, `proposition`, `corollary`, `conjecture`, `assumption`, `example`, `remark`.
   - `proof`, and `proofsketch` (the latter prints 「证明概要」).
   - Use the type given in the outline ("定义/定理/引理/命题/推论/猜想/例/注").
2. **Tag in the title.**
   - `\begin{theorem}[DIS 结构函数矩的因子化 \tagR]\label{thm:dis-moments}`. The title is the Chinese title of the outline.
   - Pure mathematics has **no tag**: `\begin{lemma}[偶数矩决定函数]`.
   - Definitions carry no tag.
   - A remark carries a tag only if the outline gives one, e.g. `rem:ir-landau-status` [A].
3. **The tag is the outline's.** It may be weakened only with a justification in the report; it may **never be strengthened**.
4. **[R] qualifiers.** The first sentence inside every `\tagR` environment is exactly one of the following, verbatim:
   - R_PT: 「（$R_{\mathrm{PT}}$：在重整化微扰论中对红外正规化的部分子态严格。）」
   - R_def: 「（$R_{\mathrm{def}}$：由算符定义直接推出。）」
   - OPE: 「（以 OPE 为前提：在 QCD 中，含夸克的 OPE 被普遍假定成立，严格证明只对标量理论与纯 Yang–Mills 规范不变算符给出，见\cref{thm:dis-ope}。）」 After the first use in a chapter, the short form 「（以 OPE 为前提。）」 is allowed.
5. **Meta-assumptions.** Every statement about hadrons ends its hypotheses with the sentence 「非微扰地位：MA…（\cref{def:intro-MA}）。」, listing the MAs given in the outline (including those marked "(MA: audit)"). If the outline lists none, the statement is about partonic states, operators or models only; say so. If you find a hadron-level statement without an MA line, add the MAs of the corresponding master-table row (or MA0 for operator identities between hadron states) and report it.
6. **「地位与缺口」 paragraph.**
   - Required immediately after every [A], [P], [C] or [V] environment, starting with `\paragraph{地位与缺口}` or a bold run-in 「地位与缺口：」.
   - It names: the weakest step; the literature location where the gap is acknowledged, e.g. 「\cite[第~14.4.8~节]{Collins2011}」; and what would upgrade the tag.
   - For [V], it says whether the evidence is an explicit perturbative counterexample (model or QCD), an explicit calculation, or experiment (critic O17).
7. **Proofs.**
   - "Proof: full" in the outline means a complete `proof` environment: every step justified, nothing deferred except standard mathematics with a citation.
   - "Proof: sketch" means a `proofsketch` with the numbered steps given in the outline. It ends with 「完整论证见…」: a citation with location, or `\cref{app:…}` when the full proof is in an appendix of this book.
   - [A] statements always get a `proofsketch`, never a `proof`. For deductions from stated hypotheses (`thm:method-template` and the process theorems deduced from it) the deduction itself is written out completely inside the `proofsketch`, and the 「地位与缺口」 paragraph names the weakest ingredient (FINAL_OUTLINE §0.8).
   - A [P] statement whose first sentence states its restriction (a model, a limit such as large $\beta_0$, or a finite order) may get a full `proof` of that restricted claim; the 「地位与缺口」 paragraph then states the general claim and why it is only partially established (e.g. `prop:dy-abelian-model`, `prop:power-adler-large-beta0`, `prop:power-thooft-model`).
8. **Dependencies.** Inside every theorem, proposition, lemma and corollary, write `\uses{label1,label2}` with the canonical labels the proof uses. Take them from "Depends on" and the proof plan. The preamble prints them, and the lead author generates a dependency table from them.
9. **Status sentences in running text.** When a theorem of another chapter is used, repeat its tag in words the first time it appears in your chapter: 「由\cref{thm:dy-factorization}（全阶论证，[A]）…」.
10. **Forbidden phrasing.** Never write 「严格证明了」 or 「已被证明」 for an [A] statement. Use 「给出了全阶论证」 or 「在…假设下论证了」. Never write 「证明」 for the general claim of a [P], [C] or [V] statement; for the restricted claim of a [P] statement write 「在…模型（极限、阶）中证明了」.
11. **Composite statements.** When the outline gives two tags for parts of one statement (e.g. `prop:sudakov-kg` "[A]; one-loop content [R, R_PT]"; `prop:heavy-quarkonium-fragmentation` "[A] … [C] …"; `prop:scet-ll` "[A] … (b) [R, R_def]"), the environment title carries the **first** tag (the one in the registry). The other part is a separate item inside the statement with its status in words and macro, e.g. 「(b)（单圈内容，\tagR，$R_{\mathrm{PT}}$）…」. The [R]-qualifier rule of item 4 then applies to that item, not to the first sentence of the environment.
12. **Dependency order.** `\uses{}` may contain only labels of your own chapter, of earlier chapters and of the appendices. A label of a later chapter may appear only as a forward pointer in running text (「其一般形式见\cref{…}（第~N~章）」), never as a proof step. Chapter 1 and the front matter are overviews and may point forward freely. If your proof plan seems to need a later result, report it instead of using it (FINAL_OUTLINE §0.8).

---------------------------------------------------------------------------------------------------

## 5. Labels (decision D7)

1. **Canonical labels.** The canonical labels of FINAL_OUTLINE are mandatory, spelled exactly as given:
   - chapters `ch:<key>`, appendices `app:<key>`;
   - sections `sec:<key>-<name>`;
   - statements `def|thm|lem|prop|cor|conj|rem|ex:<key>-<name>`;
   - tables `tab:<key>-<name>`;
   - figures per FIGURES_INDEX.
2. **Additional labels.** You may add your own labels with the same scheme and your chapter key: equations `eq:<key>-<name>`, subsections `sec:<key>-<name>`, extra remarks. Never reuse a canonical label for a different object. Never label anything with another chapter's key.
3. **Equation labels are chapter-internal.** Label displays you refer to (`eq:<key>-<name>`), but other chapters cannot know your equation labels, and the label-check script treats any external `eq:` label as non-canonical. Cross-chapter references therefore always point to the **statement** (or section, figure, table) that contains the formula: 「\cref{thm:dis-moments}中的矩关系」, not 「式\eqref{eq:dis-moments}」.
4. **External labels.** Cross-chapter references use canonical labels only. In a standalone compile these appear as "??". This is allowed, but every external label you use must be listed in the report (§12) and must appear in FINAL_OUTLINE (statement labels are in the §08 registry; `ex:` and `sec:` labels in the chapter entries).
5. **Definition ownership.** Each definition is written once, by the chapter that owns it, and \cref'd everywhere else; do not restate a definition owned by another chapter beyond one sentence of reminder. Owners (from the registry; audit):

   | owner | definitions |
   |---|---|
   | Ch01 | `def:intro-hard-process` (硬过程与幂次展开); `def:intro-factorization` (共线因子化陈述); `def:intro-tags` (严格性标签); `def:intro-MA` (元假设 MA0–MA4) |
   | Ch02 | `def:prelim-qcd` (QCD 拉氏量与规范变换); `def:prelim-feynman-rules` (Feynman 规则); `def:prelim-brst` (BRST 变换); `def:prelim-lightfront` (光锥坐标与 Sudakov 分解); `def:prelim-wilson` (Wilson 线); `def:prelim-msbar` ($\overline{\rm MS}$ 方案); `def:prelim-gamma5` ($\gamma_5$ 与 $\varepsilon$ 张量); `def:prelim-plus` (加号分布); `def:prelim-mellin` (Mellin 变换与卷积); `def:prelim-cut` (割图) |
   | Ch03 | `def:ir-landau-setup` (Feynman 参数表示与 Symanzik 多项式); `def:ir-pinch-surface` (钳夹面、内禀坐标与法坐标); `def:ir-scalings` (区域标度); `def:ir-glauber` (Glauber 区); `def:ir-safe` (红外安全可观测量); `def:ir-regions` (区域方法) |
   | Ch04 | `def:sudakov-ff` (夸克形状因子); `def:sudakov-cusp` (cusp 反常维度) |
   | Ch05 | `def:ee-R` ($R$ 比); `def:ee-adler` (Adler 函数) |
   | Ch06 | `def:dis-kinematics` (DIS 运动学与强子张量); `def:dis-compton` (前向 Compton 振幅); `def:dis-twist` (扭度与扭度 2 算符) |
   | Ch07 | `def:pdf-quark` (夸克分布); `def:pdf-antiquark` (反夸克分布); `def:pdf-gluon` (胶子分布); `def:pdf-lightray` (光线算符); `def:pdf-ff` (碎裂函数); `def:pdf-polarized` (螺旋度与横度分布) |
   | Ch08 | `def:method-regions` (区域的偏序); `def:method-collinear-approx` (共线近似子); `def:method-soft-approx` (软近似子); `def:method-subtraction` (减除项) |
   | Ch09 | `def:disall-breit` (Breit 系与投影算符) |
   | Ch10 | `def:coll-sia` (单举湮灭的运动学); `def:coll-g1` (极化结构函数); `def:coll-transversity` (横度分布) |
   | Ch11 | `def:dy-kin` (DY 运动学) |
   | Ch12 | `def:thr-limit` (部分子阈值与强子阈值) |
   | Ch13 | `def:tmd-kin` (小 $q_T$ 区域); `def:tmd-unsub` (未减除的 TMD 关联函数); `def:tmd-soft` (软因子); `def:tmd-collins` (Collins 的 TMD 定义); `def:tmd-etqs` (Qiu–Sterman (ETQS) 关联函数) |
   | Ch14 | `def:scet-modes` (模式); `def:scet-zero-bin` (零箱减除) |
   | Ch15 | `def:jets-algorithms` (红外安全的喷注定义与事件形状) |
   | Ch16 | `def:smallx-regge` (高能极限) |
   | Ch17 | `def:break-generalized-tmd` (标准与广义 TMD 因子化); `def:break-diffraction` (衍射 DIS 与衍射部分子分布); `def:break-dpdf` (双部分子分布与双 Drell–Yan) |
   | Ch18 | `def:excl-da` (介子分布振幅); `def:excl-gpd` (广义部分子分布) |
   | Ch19 | `def:heavy-nrqcd` (NRQCD 及其幂次计数) |
   | Ch20 | `def:power-borel` (Borel 变换与重整化子) |
   | Ch21 | `def:lattice-quasi` (准分布、赝分布与格点截面) |
   | AppI | `def:appI-hvbm` (HVBM 方案) |

   Objects defined inside theorem statements are owned by that theorem: (H1)–(H5) by `thm:method-template` (Ch8); the MA0–MA4 by `def:intro-MA` (Ch1); the rigor tags and $R$-qualifiers by `def:intro-tags` (Ch1); the soft factor of collinear factorization by `lem:method-soft-unitarity` (Ch8), the TMD soft factor by `def:tmd-soft` (Ch13).

---------------------------------------------------------------------------------------------------

## 6. Content obligations

1. **Every canonical statement of your chapter in FINAL_OUTLINE appears** with:
   - its label, type, tag and qualifier, and MA line;
   - its precise content: formulas from VERIFIED_FORMULAS where cited;
   - the requested proof type;
   - the literature locations given.
2. **Worked examples are in the text**, not deferred. They show the computation step by step, with intermediate results checked against VERIFIED_FORMULAS.
3. **Promised appendix proofs.** The chapters announce the following, and the appendix writers must deliver them:

   | appendix | promised content |
   |---|---|
   | A | `lem:prelim-boost`, `lem:prelim-plus-expansion`, `lem:prelim-mellin`, the Fierz decomposition |
   | B | `prop:prelim-wilson-rules`, `lem:prelim-eikonal-identity`, the one-loop cusp |
   | C | DR integrals and phase spaces used in Ch5, Ch9, Ch11 |
   | D | `thm:ir-landau-alpha`, `thm:ir-landau-momentum`, `prop:ir-coleman-norton` |
   | E | `prop:ir-power-counting` |
   | F | `prop:method-ward-one`, `prop:method-ward-tree`, outline of `lem:method-ward-multi` |
   | G | detailed one-loop calculations of Ch5, Ch6 (`prop:dis-c-oneloop`, via `sec:appG-dis`), Ch7, Ch9, Ch11, Ch13 (c_tmd §3) |
   | I | Larin scheme |
   | J | `lem:prelim-brst-nilpotent`, `thm:prelim-slavnov-taylor` details, ghost cuts, `thm:prelim-composite-renorm` context |
   | K | `rem:dis-uniqueness`, `rem:pdf-ns-plusminus` lemmas |
   | L | `thm:pdf-moments-local` |
4. **Citations of formulas.** Each formula from VERIFIED_FORMULAS with status **T** must be accompanied in the text by a hedge 「（待核实）」 or, better, re-derived by the writer. A writer who re-derives such a formula reports "writer-verified: VF-… (method)".
5. **No new results.** Do not add theorems that are not in the outline, except auxiliary lemmas needed for a full proof. Label these `lem:<key>-…` and report them.
6. **Honesty checklist.** Address explicitly, in text or in a remark, the critic items allocated to your chapter:

   | ch | critic C | critic O | misconceptions (M#) |
   |---|---|---|---|
   | 1 | C1, C2, C3 (preview) | O1, O2 | box of 12: M28, M1, M2, M3, M4, M7, M8, M9, M10, M15, M18, M24 |
   | 2 | — | — | "DR removes IR divergences" |
   | 3 | C5, C15 | O11, O12 | M8, M9, M19, M20 |
   | 4 | — | O11 (corrected: massive *exchange* needs analytic regulators) | M16, M21 (preview) |
   | 5 | — | O3, O21 (part) | M27 |
   | 6 | C4, C15 | O4, O5, O6, O7 | M3, M4, M5, M6; Adler sum rule; Bloom–Gilman |
   | 7 | C1, C2, C3, C13, C14 | O6, O8, O9 | M2, M6, M11, M23, M24 |
   | 8 | C2, C7, C14 | O10, O13 | M15, M24, M25 |
   | 9 | — | O7 | M4, M25, M26 |
   | 10 | — | — | Christ–Lee; M23; "diffractive PDFs universal" |
   | 11 | C8, C11 | O13, O14 | M7, M25 |
   | 12 | — | — | (prescriptions are not theorems) |
   | 13 | C8, C9, C10 | O15 | M12, M13, M14, M15, M16, M17 |
   | 14 | C6 | — | M18, M19 |
   | 15 | — | — | M8, M9, M10 |
   | 16 | — | — | (non-uniformity at small $x$) |
   | 17 | C8 | O16, O17 | M7, M21 |
   | 18 | — | O18 | — |
   | 19 | — | O19 | — |
   | 20 | C11 | O20, O21 | M10, M22, M28 |
   | 21 | C12 | — | — |
   | 22 | all (summary) | — | — |

   The texts of the C, O and M items are in `research/critic/REVIEW.md` §2, §3.2 and §7.
7. **Overclaims to avoid** (each has occurred in drafts or in the literature):
   - 「Rothstein–Stewart (2016) 证明了 Drell–Yan 因子化」. False: RS state that the S–S cancellation "taken alone is far from a proof".
   - 「软因子等于 1」 without 「对共线单举截面」.
   - 「Glauber 胶子在单举截面中总是相消」. Write instead: inclusive in the spectators, and the measurement must not obstruct the deformation (C8).
   - 「SCET 独立于区域分析证明了因子化」 (C6, M18).
   - 「Collins (2011) 证明了非定域算符的 BRST 分类」. False: it is assumed (§11.3.2).
   - 「偶极子公式对所有阶精确」. It fails at three loops.
   - 「$\overline{\rm MS}$ PDF 是正的」. This is [C].
   - 「Sivers 符号反转已被实验确认」. Experiment is consistent but not decisive.
   - 「$B\to\pi\pi$ 的 QCD 因子化已全阶证明」. It is [P].
   - 「NRQCD 产生的因子化已证明」. It is [C].
   - 「格点检验了因子化」 (C12).
   - 「DY 的幂次修正是 $1/Q^2$」 as a theorem. This is [C]; renormalon analyses only suggest it.
   - Attributing to RS 2016 an $e^+e^-$-specific statement (c_scet §6 item 14).
   - Citing `SenIndumathiChoudhury2019` as a QCD paper. It reproduces the Grammer–Yennie formulae; cite it only next to `GrammerYennie1973`.
   - 「$\overline{\rm MS}$ PDF 在所有标度上非负」. False: explicit one-loop Yukawa-model counterexample (`CollinsRogersSato2022`); only positivity above a non-perturbative scale is conjectured (`conj:pdf-positivity`).
   - 「Soffer 不等式对 $\overline{\rm MS}$ 分布成立」 as a theorem. Only its preservation by LO evolution is proved (`prop:coll-soffer`).
   - 「衍射 DIS 只有一个强子，因而没有 Glauber 问题」. Wrong argument: the $r^-$ contour is trapped and the proof escapes through $r^+$ (`thm:break-ddis`; c_glauber §6 item 6).
   - 「区域 = Newton 多面体的下表面」 as a general statement in Minkowski kinematics. False at three loops (hidden regions, `Gardi:2024axt`).
   - 「推力的领头对数重求和在微扰论中已严格证明」. It inherits [A] from `thm:scet-thrust` (`prop:scet-ll`).
8. **Literature locations.**
   - Use the section numbers that the survey or the agents verified (listed in FINAL_OUTLINE and REFS_NOTES).
   - When a location is not verified, write the claim without the location or add 「（位置待核实）」.
   - Never invent equation numbers. c_glauber could not access the text of Collins 2011, so equation numbers of that book are quoted only where the survey verified them.

---------------------------------------------------------------------------------------------------

## 7. Figures

`FIGURES_INDEX.md` is binding. In summary:
1. **Owned existing figures.** Include all of them by copying the `%%% BEGIN/END` block verbatim from `research/tikz{1,2,3}/figures{1,2,3}.tex`. tikz2 and tikz3 are being redone, so copy the version current at writing time.
2. **Required new figures.** Draw them per the description, in plain TikZ with the preamble styles. Wrap each one in `%%% BEGIN fig:<label>` / `%%% END fig:<label>`.
3. **Optional figures.** Draw them only if within the page budget.
4. **Missing figures.** Use the placeholder protocol (FIGURES_INDEX §0.4) when a figure is not available, and report it.
5. **Inspection.** Inspect every figure page as a rendered PNG before submitting (§9).
6. **Floats.** Use `[htbp]` placement. Each caption is self-contained, in Chinese, 1–4 sentences, and states the conventions that matter (directions, $\pm i0$, which subgraph is which).
7. **Tables.** Use `table` with `tabular` or `tabularx`; `longtable` is not loaded. Split large tables (e.g. the master table) into several `table` floats with "（续）" captions. `booktabs`, `array`, `multirow` and `tabularx` are loaded: use `\toprule`, `\midrule` and `\bottomrule`, and no vertical rules.
8. **Float barriers.** `placeins` is loaded with `[section]`, so floats do not cross `\section` boundaries. Keep figures near their first reference.
9. **Ownership is first use; caption notation.** Figures are owned by the first chapter that uses them (FIGURES_INDEX §1 notes, revised by the audit); later chapters refer back. Some existing captions use $n,\bar n$ outside Ch14 with different meanings (FIGURES_INDEX §1 notes): add the one-sentence conversion to $n_A,n_B$ in the text at the first reference.

---------------------------------------------------------------------------------------------------

## 8. Citations (decision D6)

1. **Bibliography.**
   - Cite only keys present in `spec/refs_merged.bib` (646 entries after the audit, all verified). The compile uses BibTeX with style `unsrt`.
   - If you know a survey or agent label (e.g. `Collins:2011zzd`, `Nayak:2005rt`), look it up in `spec/key_aliases.tsv` (columns: alias, merged_key, origin) and use the merged key. One alias maps to two keys: `Collins:2011zzd` (the 2011 book and its 2023 OA reissue). Use `Collins2011`.
   - Never cite a key that is not in the bib.
   - If a needed reference is missing, write the claim with 「（文献待补：<author year, journal>）」 and list it in the report.
2. **Syntax.**
   - Attach `\cite` with no space: 「文献\cite{Collins2011}」, 「（见\cite{CollinsSoperSterman1989}）」.
   - Locations: `\cite[第~14.4~节]{Collins2011}`, `\cite[第~5.9.2~节]{Collins2011}`, `\cite[式~(64)]{Sterman:1995fz}`, `\cite[第~112~页]{EdenEtAl1966}`.
3. **What a citation may support.**
   - Attribute to a paper only what `REFS_NOTES.md`, `SURVEY.md` or the agents document for it. The quotations marked [txt], [abs] or [bib] in SURVEY.md say what was actually read.
   - Statements marked "(recall)" or "(verify)" in the sources must be hedged or re-checked.
   - Direct quotations (English) are allowed when the survey or an agent verified them. Put them in 「“…”」 with location, followed by a Chinese paraphrase.
4. **Known warnings.** `REFS_NOTES.md` "Binding warnings". Examples:
   - `Collins2023` is the Open Access reissue of `Collins2011`; quote section numbers from `Collins2011`.
   - `QiuSterman1992` is about direct photons; the pion paper is `Qiu:1998ia`.
   - `SenIndumathiChoudhury2019` only next to `GrammerYennie1973`.
   - `Collins2007` is an unpublished preprint, `Collins:2020euz` a preprint, and `Beneke:2026miy` a preprint. Say so when citing them.
   - Radyushkin 1996 (JINR), cited in c_ee's snippet, is not in the bib. Use `KrasnikovPivovarov1982` or `KataevStarshenko1995` instead.
5. **Citation density.** Every [A], [P], [C] or [V] statement cites at least one primary source and one location of the gap. Every [R] statement that is not proved in full cites the source of the proof.

---------------------------------------------------------------------------------------------------

## 9. Compile and quality assurance (mandatory before submission)

1. **Test directory.** Work in a scratch directory of your own (not in `spec/`). Copy into it `common/preamble_fact.tex`, `spec/refs_merged.bib`, `spec/FINAL_OUTLINE.md` (read by the label-check script of item 6) and your chapter file.
2. **Driver.** Create the driver `test_<key>.tex`:
   ```latex
   \input{preamble_fact.tex}
   \begin{document}
   % \appendix        % uncomment for appendix files
   \input{ch05_ee.tex}
   \bibliographystyle{unsrt}
   \bibliography{refs_merged}
   \end{document}
   ```
3. **Build.** Run `xelatex -interaction=nonstopmode test_<key>.tex && bibtex test_<key> && xelatex -interaction=nonstopmode test_<key>.tex && xelatex -interaction=nonstopmode test_<key>.tex`.
4. **Log checks.** Each check must pass.
   - `grep -c "LaTeX Error\|Undefined control sequence\|Emergency stop" test_<key>.log` → **0**.
   - `grep "Missing character" test_<key>.log` → **none** (a missing glyph means a wrong character, e.g. U+202F; replace it).
   - `grep "Overfull \\\\hbox" test_<key>.log` → none above 1 pt. Fix by rewording or display breaking, never by `\sloppy` for the whole chapter.
   - `grep "Citation .* undefined" test_<key>.log` → **none**.
   - `grep "multiply defined" test_<key>.log` → **none**.
   - `grep "Reference .* undefined" test_<key>.log` → only labels of other chapters. List them in the report.
   - `test_<key>.blg` has **no** warnings for the entries you cite.
5. **Renders.** Render every page that contains a figure, a table or a long display: `pdftoppm -r 110 -png -f N -l N test_<key>.pdf pg`. Look at each PNG: overlaps, clipped labels, unreadable fonts, wrong arrows, colours in greyscale. Then fix and re-render.
6. **Label check.** Run this script with `python3 -I`:
   ```python
   import re,sys
   t=open(sys.argv[1],encoding='utf-8').read()
   lab=set(re.findall(r'\\label\{([^}]+)\}',t)); ref=set(sum([x.split(',') for x in re.findall(r'\\(?:c?ref|cref\*?|uses)\{([^}]+)\}',t)],[]))
   o=open('FINAL_OUTLINE.md',encoding='utf-8').read(); canon=set(re.findall(r'`((?:def|thm|lem|prop|cor|conj|rem|ex|sec|fig|tab):[A-Za-z0-9-]+)`',o))
   key=sys.argv[2]
   mine={c for c in canon if re.match(r'(def|thm|lem|prop|cor|conj|rem|ex|sec|tab):'+key+'-',c)}
   print('canonical labels of this chapter missing:',sorted(mine-lab))
   print('external refs:',sorted(r.strip() for r in ref if r.strip() not in lab))
   print('external refs not canonical:',sorted(r.strip() for r in ref if r.strip() not in lab and r.strip() not in canon))
   ```
   The usage is `python3 -I check_labels.py ch05_ee.tex ee`. Required results:
   - missing = ∅, except for labels deliberately omitted and justified in the report;
   - "external refs not canonical" = ∅.
7. **Tag check.** Every `\tagR` environment's first sentence is one of the three qualifiers. Every [A], [P], [C] or [V] statement is followed by 「地位与缺口」.
8. **Page count.** Count the pages from your chapter title to the start of the bibliography. They must lie within the budget of FINAL_OUTLINE §0.2, with tolerance −15 % / +10 %.

---------------------------------------------------------------------------------------------------

## 10. Page budgets and density

| unit | pp | | unit | pp | | unit | pp |
|---|---|---|---|---|---|---|---|
| front | 5 | | Ch8 | 16 | | Ch16 | 8 |
| Ch1 | 12 | | Ch9 | 12 | | Ch17 | 12 |
| Ch2 | 14 | | Ch10 | 12 | | Ch18 | 10 |
| Ch3 | 14 | | Ch11 | 14 | | Ch19 | 9 |
| Ch4 | 12 | | Ch12 | 8 | | Ch20 | 12 |
| Ch5 | 12 | | Ch13 | 14 | | Ch21 | 8 |
| Ch6 | 14 | | Ch14 | 12 | | Ch22 | 12 |
| Ch7 | 14 | | Ch15 | 9 | | App A–L | 3,4,3,4,3,3,4,2,2,2,3,2 |

The total is 300 pp (A4, 11 pt, 2.5 cm margins).

**Short chapters** (12, 15, 16, 18, 19, 21): each main result in the form **precise statement + status (tag, MA, evidence) + proof idea (`proofsketch`) + one worked example**. Do not shorten the statements; shorten the discussion.

**Core chapters:** about 60 % statements and proofs, 25 % worked examples, 15 % motivation and status discussion.

---------------------------------------------------------------------------------------------------

## 11. Interaction with the research files

1. **Ready-made Chinese drafts.** Several research agents left Chinese TeX drafts in the monograph style:
   - `research/c_dis/dis_oneloop.tex`;
   - `research/c_dy/dy_oneloop.tex`;
   - `research/c_ee/ee_total.tex`;
   - `research/c_regions/{landau,powercounting,regions}.tex`;
   - `research/c_wilson/tex/*`;
   - `research/c_pdf/tex/*`;
   - `research/c_exclusive/tex/*`;
   - `research/c_scet/tex/*`.

   You may adapt them, but you must:
   - relabel to the canonical labels;
   - convert their conventions, in particular $\bar n,n$ to $n_A,n_B$ outside Ch14;
   - remove their local `\newcommand`s;
   - check every formula against VERIFIED_FORMULAS.
2. **Status of the derivations (audit update, 2026-10-10).** `research/c_tmd/DERIVATION.md` (17/17 scripts pass; drafts in `research/c_tmd/tex/`) and `research/c_glauber/DERIVATION.md` §3–§4 (drafts in `research/c_glauber/tex/c_glauber_snippets.tex`) now exist; VERIFIED_FORMULAS has been upgraded from them. Use them as sources (add them to the list in item 1). If a derivation contradicts a VF entry, the derivation wins only if its checks pass; report the discrepancy.
3. **Read-only.** Do not modify research files, `CONTEXT.md`, `common/preamble_fact.tex` or anything in `spec/`.

---------------------------------------------------------------------------------------------------

## 12. Final report (return to the lead author)

Report in this order:
1. **File:** path, page count, compile status (errors 0; overfull > 1 pt 0; undefined citations 0; BibTeX warnings 0).
2. **Canonical labels:** implemented / missing (with reasons).
3. **Additional labels** defined.
4. **External labels** referenced (all canonical).
5. **Tags:** each canonical statement with its final tag. Any weakening is justified.
6. **Formulas:**
   - VF IDs used;
   - writer-derived formulas, with the check made;
   - T-status formulas and how they were handled (re-derived / hedged).
7. **Citations:**
   - keys used;
   - aliases resolved;
   - missing references (「文献待补」 items);
   - locations marked 「位置待核实」.
8. **Figures:** existing figures copied (with source file and timestamp); new figures drawn; placeholders used; figure issues found.
9. **Deviations** from FINAL_OUTLINE or this spec, with justification. Any errors found in the spec files.
10. **Open items** for the lead author.

---------------------------------------------------------------------------------------------------

## CHANGELOG

**2026-10-10 — spec audit (auditor agent).**
1. Notation table: row 7 (direction of the $S_\varepsilon$ ratio), row 20 (scope of the FF $D$-dimensional factor), row 25 (Larin replacement in our $\epsilon$ convention, VF-CONV-24 — the literature form has the opposite sign convention), row 28 (future − past identity holds for lines attached at the same point; with $W[0,-\infty n]$ it would be a principal value), row 29 (one-loop cusp angle), row 30 (Collins' $e^{+ik\cdot b}$ concerns his soft factor and TMD FFs, eq. (13.35); TMD-PDF papers in his scheme use our convention), row 31 (ζ normalization, space-like regulator lines, order of limits), row 32 (Sivers model sign now verified), row 33 ($\sigma_0/s$ in TMD cross sections).
2. §4: rules for proofs of [A] deductions and of [P] restricted claims (item 7); phrasing for [P] (item 10); new item 11 (composite statements) and item 12 (dependency order, no later labels in `\uses{}`); item 5 (MA lines added by the audit).
3. §5: item 3 (equation labels are chapter-internal; cross-chapter references point to statements); item 4 (where canonical labels are listed); new item 5 (definition-ownership table, generated from the registry).
4. §6: App G also serves Ch6; five more forbidden overclaims (all-scale PDF positivity, Soffer for $\overline{\rm MS}$, the wrong DDIS argument, regions = facets, thrust LL as [R]).
5. §7 item 9 (first-use ownership; caption notation). §11 item 2 (c_tmd and c_glauber §3–§4 now exist).
6. §9 item 1: copy `FINAL_OUTLINE.md` into the test directory (the label-check script reads it). §8: 646 bib entries.
7. Row 20 corrected (later the same day): the fragmentation function in the hadron frame carries $z^{1-2\varepsilon}/(4N_c)$; $1/(4N_cz)$ belongs to the parton frame with an explicit $\int d^{2-2\varepsilon}p_{hT}$ (REFDOC_ANALYSIS §2.4 OUR-1; re-derived by the audit).

