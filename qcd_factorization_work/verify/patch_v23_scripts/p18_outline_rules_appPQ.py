import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import src
ln = src.ln
TARGET = 'FINAL_OUTLINE_v2.md'

S004 = r'''### 00.4 Outcomes of the proof extensions X1, X2, X3 (verify patch v2.3)

The verification workflow (`verify/`) ran three proof extensions: **X1 Glauber** (App O), **X2 subtraction** (App N), **X3 OPE** (App M); final reports `verify/extend_reports/X1-glauber_final.md`, `X2-subtraction_final.md`, `X3-ope_final.md` (each with an independent second review). Decision rules (applied):
- **PASS** = two independent confirmations recorded in `verify/` (WRITER_SPEC_v2 §6.5 item 2) and, for a novelty claim, a literature check: the statement is inserted with its tag, the dependent status lines, the assumption register and `tab:appX-status`/App P are updated.
- **PARTIAL** = the extension holds in a restricted setting: the statement is inserted with the restriction in its first sentence and tag [P] (or [R, R_PT] for an explicit fixed-order statement whose first sentence states the order; a model theorem is [P] as a QCD statement, WRITER_SPEC_v2 §4.3 item 4).
- **FAIL / not delivered** = the reserved slot label is withdrawn (named below only by its slot ID; §10), the fallback stays, no claim is printed.

| slot | planned content (short) | outcome | inserted statements (tags) | fallback in force / remaining gap |
|---|---|---|---|---|
| X3a | `asm:appM-remainder` from a published momentum-space OPE theorem via `lem:appM-uniqueness` | not delivered (the uniqueness route is circular; the sources were not read) | `rem:appM-remainder-reduction` (reduction to the zero-momentum matching estimate (CTp); the DR route needs no such remainder) | `asm:appM-remainder` stays `\tagA` |
| X3b | the cited Euclidean expansion theorems cover QCD with quarks, ghosts and gauge-variant operators | not passed (`Smirnov:1990rz` checked: scope too short) | `def:appM-blocks`, `lem:appM-ne` (数学), revised `lem:appM-uniqueness`, `prop:appM-zero-momentum-insertion` [A] | `prop:dis-ope-euclid` stays [A] (decision D3), now via (A1)–(A4) |
| X3c | `asm:appM-forward` at $O(\alpha_s)$ for all $N$ | not delivered (superseded by X3e) | — | `ex:appM-forward-oneloop` |
| X3d | (B1)(B2) of `asm:appM-brst-ope` in pure Yang–Mills and, for QCD, under a cohomology condition | partial | `asm:appM-brst-ope` rewritten ((B1) retired, (B2) ≡ (Eε)); `thm:appM-brst-reduction` [R, R_cond]; `lem:appM-lbc-formal` (数学) | (Eε) stays `\tagA`; Joglekar read at abstract level, Hollands' QCD scope not verified |
| X3e | forward on-shell expansion theorem, per graph | PASS per graph | `lem:appM-forward-forests`, `thm:appM-forward-expansion`, `lem:appM-t2-projector` [R, R_PT]; `lem:appM-newton`, `lem:appM-matroid` (数学); `cor:appM-forward-ope`, `cor:appM-cut-plane` [A]; `asm:appM-oswi` `\tagA`; `lem:appM-gluon-regularity` [R, R_cond]; `ex:appM-forward-triangle`, `ex:appM-forward-nonuniform` | `asm:appM-forward` stays (reduced by `cor:appM-forward-ope`); novelty check open (marker withheld) |
| X2a | (CS1)–(CS3) for the one-loop off-shell triangle | delivered | `prop:appN-triangle-cs` [R, R_PT] (part (a) the only 「本书新结果」 of the book; part (c) an implication pending the second confirmation of the $\Gamma$-identification); `def:appN-fibered`, `thm:appN-fibered-subtraction`, `lem:appN-identification`, `lem:appN-lp-certificate` (数学), `lem:appN-lc-positivity` [R, R_PT], `asm:appN-lce` `\tagA`, `cor:appN-cs3-fibered` [R, R_cond] | — |
| X2b | (CS1)–(CS3) for every one-loop graph of Sudakov type | not delivered | partial evidence: `prop:appN-phi36-dis`, `prop:appN-massive-photon` [R, R_PT]; `rem:appN-m1-infrared` | `thm:appN-subtraction` stays [R, R_cond] |
| X2c | (CS1)–(CS3) for the two-rung DIS ladder | not delivered | `prop:appN-twoloop-algebra` [R, R_PT]; `asm:appN-analytic-reg` `\tagA`; `prop:appN-twoloop-remainder` [R, R_cond]; `rem:appN-fibered-allorders` | grouping statement `prop:appN-ladder` only |
| X2d | the (Abs) edge case | open | — | `rem:appN-abs-edge` kept as a plausible gap; the case is put into `asm:appN-collins` |
| X1a | eikonal spectators: unitarity to all orders | not delivered | — | `rem:dy-common-ordering`(ii) stays a remark |
| X1b | all $O(g^4)$ eikonal graphs | not delivered (cited instead: `Meggiolaro:1996hf` eqs. (3.28)–(3.34)) | — | `prop:dy-eikonal-twogluon` cites the other graphs |
| X1c | side-independent windows remove the window-edge terms | PASS (both final reviewers), grade [R, R_cond] instead of the planned [R, R_PT] | `lem:appO-side-independent-windows` [R, R_cond]; `def:appO-family` extended | out-of-window parts and wee lines stay in `asm:appO-deformation`(c) |
| X1d | compatibility for $\mathcal G_0$ | not delivered | — | `asm:appO-deformation`(b) stays, also for $\mathcal G_0$ |
| X1e | explicit $O(\alpha_s^2)$ check of `asm:appO-mixing`(c) with Lipatov-vertex graphs | not delivered | related: `prop:appO-g6-ladder` [A] | `ex:appO-two-exchange` |
| X1f | two SS exchanges with exact connecting propagators | PARTIAL (model theorem; uncut lines only) | `def:appO-sectors`, `def:appO-glob-model`, `def:appO-regulator-class`; `lem:appO-multipole-localization`, `lem:appO-quadrant-residues`, `lem:appO-preintegration-localization`, `prop:appO-strict-window-shape` [R, R_PT]; `lem:appO-kplus-rotation`, `lem:appO-ray-identity`, `lem:appO-two-insertion-bounds` (数学); `lem:appO-halfcoinc-colour` [R, R_def]; `prop:appO-twoexch-spectator`, `prop:appO-twoexch-regulated`, `prop:appO-pergraph-weights`, `prop:appO-halfcoinc-sensitivity` [P]; `asm:appO-adjacent-swap`, `asm:appO-real-jets` `\tagP`, `asm:appO-collinear-ends` `\tagA`; `rem:appO-halfcoinc`, `rem:appO-cut-ss`, `rem:appO-onshell-unitarity`, `rem:appO-literature-comparison` | cut direct lines open (`rem:appO-cut-ss`); `asm:appO-mixing`(c) keeps its content, now with clause (a′) |

Novelty markers (WRITER_SPEC_v2 §6.5, final): the only 「本书新结果」 of the book is `prop:appN-triangle-cs`(a), with the wording 「本书新结果（据我们截至 2026 年 10 月的文献检索…）」. `prop:dy-eikonal-twogluon` is printed without marker (claim N01: the result is in `Meggiolaro:1996hf`, `Giordano:2006vv`); `thm:appM-forward-expansion` is 「本书给出的严格证明」 with the marker withheld (novelty check open; closest prior result `Semenova:2018cwy` §7 Prop. 6); the App O model theorems carry no marker (the check of `CollinsSoperSterman1988` and Collins 2011 §14.4 for non-commuting coincident exchanges is open). Sharpened results never marked new: `prop:appN-triangle-exact`(d) (N12), `lem:appO-joint-localization` (N13), `ex:appM-unreduced` (N15), `lem:appJ-cut-hermiticity` (N14).'''

ERR_S1B = r'''| ERR-S1b | App O §O.5 | for composite spectators the strict-window residual was expected "not to vanish within $\mathcal G_0$": contradicted for the **uncut-line** part in the global two-time model (`prop:appO-twoexch-spectator`, a model theorem, [P] as a QCD statement); the near-shell mechanism was correctly identified, the error is the expectation of insufficiency; the complete $\mathcal G_0$ form (cut direct lines, `rem:appO-cut-ss`) is open |'''

APPQ_TABLES = r'''**Final rows** (verify patch v2.3; class Q1; numbered by first use in the book; record paths relative to `verify/claims/`; VF IDs in `%` comments of the written table). Credit: the first published correction of E01 is `Chou:2022drv`; E02 was noted by the authors themselves (PRD 105 (2022) 076014, footnote 1).

`tab:appQ-errata`:

| 编号 | claim | 来源（文献键 + 式/节） | 原文形式 | 正确形式（本书约定） | 核实 | 后续文献中的状态 | 本书依赖之处 |
|---|---|---|---|---|---|---|---|
| Q.1 | E23 | `BecherSchwartz2008` eq. (A.10) (journal; also arXiv v1, v2, App. A) | $\Gamma_1=4C_F[C_A(\frac{67}9-\frac{\pi^2}3)-\frac{20}9C_FT_Fn_f]$ | $\Gamma_1=4C_F[(\frac{67}9-\frac{\pi^2}3)C_A-\frac{20}9T_Fn_f]=36.8436$ ($n_f=5$; `KorchemskyRadyushkin1987`, `MochVermaserenVogt2004` eq. (3.11)) | `batch_E19_s1.md`, `batch_E19_s2.md` | not reported (no erratum) | Ch5, Ch15, App B |
| Q.2 | E17 | `AybatRogers2011` eqs. (3), (4) (arXiv:1101.5057v2) | $\zeta_F=2M_p^2x^2e^{2(y_P-y_s)}$, $\zeta_D=2(M_H^2/z^2)e^{2(y_s-y_h)}$ | factor-free: $\zeta_F=M_p^2x^2e^{2(y_P-y_s)}=2(xP^+)^2e^{-2y_s}$, $\zeta_D=(M_h^2/z^2)e^{2(y_s-y_h)}$, so $\sqrt{\zeta_F\zeta_D}=Q^2$ | `batch_E13_s1.md`, `batch_E13_s2.md` | implicitly corrected (the same authors use the factor-free form in `Aybat:2011ge`; also `Collins:2012uy`); no erratum | Ch14 |
| Q.3 | E25 | `BauerPirjolStewart2002`, sentence after eq. (24) | field-strength and ghost terms "invariant under collinear gauge transformations" | field-strength term collinear and ultrasoft invariant; gauge-fixing and ghost terms each only ultrasoft invariant; only their sum (and $\mathcal L_c^{(g)}$) is BRST invariant | `batch_E25_s1.md`, `batch_E19_s2.md` | not reported | Ch15 |
| Q.4 | E18 | `Collins2007` eq. (10), second line (arXiv:0708.4410v1, unpublished) | spurious numerator $\prod_{j=1,2}(k_T^2+m_q^2)$ | $I_1=\mathcal NF^2$, $I_2=-\mathcal NG/(k_T^2+m_q^2)$, $\mathcal N=\lambda^2g_1^2g_2(g_2+g_1)x(1-x)/(256\pi^7)$ (note Q.3) | `batch_E13_s1.md`, `batch_E13_s2.md` | not recorded (preprint, v1 only) | Ch18 |
| Q.5 | E20 | `Ji1997a`, arXiv:hep-ph/9603249v1 eq. (15) | second denominators $1/(x+\xi_{\rm Ji}/2+i\epsilon)$ | $1/(x+\xi_{\rm Ji}/2-i\epsilon)$, $\xi_{\rm Ji}=2\xi$ (u-channel propagator; ${\rm Im}\,T^{11}=2\pi F_1$) | `batch_E19_s1.md`, `batch_E19_s2.md` | correct in `Ji1997b` eq. (4) and `Vanderhaeghen:1999xj` eq. (38); the PRL text was not accessible (attributed to arXiv v1) | Ch19 |
| Q.6 | E21 | `Mankiewicz:1999tt`, text after eq. (10) | integrands $\sim12/\tau$ and $9/\tau$ for $\phi_\parallel=6\tau\bar\tau$ | $12/\tau$ and $6/\tau$; in general $8g^v(0)/\tau$, $4g^v(0)/\tau$, $g^v(0)=\frac12\int_0^1du\,\phi_\parallel(u)/u$ (ratio $2{:}1$ for every DA) | `batch_E19_s1.md`, `batch_E19_s2.md` | not reported | Ch19 |
| Q.7 | E26 | `BenekeEtAl2001` after eq. (71); `BenekeNeubert2003` after eq. (63) | "$X_H$" resp. "$X_A=\ln(m_M/\Lambda_h)\approx2.4$" | $\ln(m_B/\Lambda_h)=2.36$, $\Lambda_h=0.5$ GeV | `batch_E25_s1.md`, `batch_E26_s2.md` | no erratum; the correct value appears elsewhere in `BenekeEtAl2001` | Ch20 |
| Q.8 | E01 | `Ji:2020brr` eqs. (33)–(34) (arXiv eq. hybridm2); `JiEtAl2021` eqs. (120)–(121) | hybrid kernel with $\frac1{|1-\xi|_+}\equiv\lim_\beta[\theta(|1-\xi|-\beta)/|1-\xi|+2\delta(1-\xi)\ln\beta]$: $\int d\xi\,C_{\rm hyb}=1+3a\ln(\lambda_Se^{\gamma_E})$ | the printed form minus $3a\ln(\lambda_Se^{\gamma_E})\delta(1-\xi)$, i.e. the bracket with the plus prescription on $\mathbb R$, $\lambda_S=z_S|p^z|$: $\int d\xi\,C_{\rm hyb}=1$ (`prop:lamet-hybrid-kernel`) | `batch_E01_s1.md`, `batch_E01_s2.md` | **first corrected by `Chou:2022drv` eq. (35)**; also `Su:2022fiu` eq. (A.14) | Ch22 |
| Q.9 | E03 | `Braun:2018brg` eqs. (63)–(64) (arXiv eq. cR; $x>0$) | $R^{\parallel,\perp}_{\mathcal Q}$ without $q(x)\ln(1-x)$ in the braces | $R^{\parallel,\perp}_{\mathcal Q}=R^{\parallel,\perp}_{\mathcal Q}({\rm printed})+(1-x)\ln(1-x)$ (from their eqs. (61)–(62) with the $[0,1]$ plus distribution of eq. (55)) | `batch_E01_s1.md`, `batch_E01_s2.md` | not reported | Ch22 |
| Q.10 | E04 | `IzubuchiEtAl2018` eqs. (2), (5) | light-cone link $P\exp(-ig\int A^+)$ and space-like link $P\exp(-ig\int dz'A^z)$ with one covariant derivative | for the vertex of their eq. (41) the space-like link is $P\exp(+ig\int_0^zdz'A^z)$; the published one-loop results are unaffected (their integrands use the consistent link) | `batch_E01_s1.md`, `batch_E01_s2.md` | not found | Ch22 (conventions) |
| Q.11 | E02 | `Ji:2019ewn` eq. (22); `JiEtAl2021` eqs. (209)–(210); `Liu:2022nnk` eqs. (53), (75); arXiv:2106.05310v1 of `Ji:2021znw` | exponent $e^{\tilde K\ln(\zeta_z/\zeta)}$; ratio $(\zeta_{z1}/\zeta_{z2})^{\tilde K}$ | $\tilde f\sqrt{S_r}=H\,e^{\frac12\tilde K\ln(\zeta_z/\zeta)}f^{\rm TMD}$; ratio $(\zeta_{z1}/\zeta_{z2})^{\tilde K/2}=(P^z_1/P^z_2)^{\tilde K}$ (`EbertStewartZhao2019` eqs. (24), (27)) (note Q.11) | `batch_E01_s1.md`, `batch_E01_s2.md` | **noted by the authors** in the journal version of `Ji:2021znw` (PRD 105 (2022) 076014, footnote 1), which is correct; correct form also `Ebert:2022fmh` and `Liu:2022nnk` eq. (52) | Ch22, Ch23 |
| Q.12 | E08 | `Liu:2022nnk`, display below eq. (81); `Ji:2021znw` eq. (73) (= (72) of arXiv v1) | $\Gamma_S^{(2)}=\frac{\alpha_s^2}{\pi^2}[C_FC_A(-\frac{49}{36}+\frac{\pi^2}{12}-\frac{\zeta_3}2)+\frac5{18}C_Fn_f]$ | $\Gamma_S^{(2)}=-\gamma^{(2)}_{HH}=\frac{\alpha_s^2}{\pi^2}C_F[C_A(\frac{49}{36}-\frac{\pi^2}{12}+\frac{\zeta_3}2)-\frac59T_Fn_f]$ (their convention $\mu^2d\ln S_I/d\mu^2=-\Gamma_S$) | `batch_E07_s1.md`, `batch_E07_s2.md` | correct in `JiEtAl2021` and `Ji:2023pba` (A.6), which however asserts agreement with the earlier formulas; no erratum | Ch23 |
| Q.13 | E09 | `JiEtAl2021` eqs. (205)–(206) (arXiv:2004.03543v2 numbering) | $\mu^2\frac{d\ln S_r}{d\mu^2}=\Gamma_S$; $\mu^2\frac{d\ln S_{\rm DY}}{d\mu^2}=-(Y+Y')\Gamma_{\rm cusp}-\Gamma_S$ | $-\Gamma_S$ resp. $-(Y+Y')\Gamma_{\rm cusp}+\Gamma_S$ (convention-free: $\mu^2d\ln S_r/d\mu^2=\gamma_{HH}$) | `batch_E07_s1.md`, `batch_E07_s2.md` | not found | Ch23 |
| Q.14 | E10 | `Ji:2019ewn` eq. (26) and the values below it | $\gamma_C^{(2)}$ with $a_1=60\zeta_3-\frac{19\pi^2}3+\frac{68}{27}$, $a_3=\frac{2\pi^2}3-\frac{62}{27}$ (0.7494 for $n_f=4$) | $\gamma_C^{(2)}=\frac{1188\zeta_3-99\pi^2-1108}{432\pi^2}C_FC_A-\frac{36\zeta_3+6-7\pi^2}{12\pi^2}C_F^2+(\frac1{24}+\frac{10}{27\pi^2})C_Fn_f$ ($T_F=\frac12$; 0.1034 for $n_f=4$) | `batch_E07_s1.md`, `batch_E07_s2.md` | correct value in `Ji:2023pba` (A.12)–(A.13) and `delRio:2023pse`, without noting the discrepancy | Ch23 |
| Q.15 | E11 | `Liu:2022nnk` eq. (81); `JiEtAl2021` eq. (208) | $O(\alpha_s^2)$ $L_b^2$ coefficient of $\ln S_I$ twice the correct value; in (81) also the sign of the single log | $\ln S_I=-\frac{\alpha_sC_F}\pi L_b+\alpha_s^2[-\frac{C_F\beta_0}{8\pi^2}L_b^2+\hat\gamma_{HH}L_b+c_2]$, $\beta_0=\frac{11}3C_A-\frac43T_Fn_f$ (note Q.15) | `batch_E07_s1.md`, `batch_E07_s2.md` | not found | Ch23 |
| Q.16 | E13 | `Liu:2022nnk` App. F | "edge of the wedge" theorem for complex Lorentz covariance; the map "$\Lambda(t,z)\to(it,iz)$" | the Bargmann–Hall–Wightman theorem (`Streater:1989vi` Thm. 2-11; spectral condition and real Lorentz covariance suffice); the map $(t,z)\mapsto(iz,it)$; conclusion (F.6) unaffected | `batch_E13_s1.md`, `batch_E13_s2.md` | stated correctly by the author in `Liu:2023pjb` eq. (3.25) | Ch23 |

`tab:appQ-errata-b` (class Q2: corrected by the authors or superseded by the same group; cite the corrected version where used; printed for the reader's orientation, without verification column):

| 编号 | claim | 来源 | 原文形式 | 正确形式 | 更正 | 本书依赖之处 |
|---|---|---|---|---|---|---|
| Q.17 | E06 | `Ji2013` eq. (11) | $\tilde q=\int_x^1\frac{dy}yZ(\frac xy,\frac\mu{P^z})q(y)$ | $\int_{-1}^1\frac{dy}{|y|}C(\frac xy,\frac{\mu_R}\mu,\frac\mu{|y|P^z})q(y)$ | `IzubuchiEtAl2018` eq. (27); for quasi-GPDs `Ji:2015qla` | Ch22 |
| Q.18 | E12 | `Guo:2021ibg` eq. (16) | gluon GPD with a spurious $\frac12$ (cross section ×¼) | standard normalization; $\vert G\vert^2$ four times eq. (26) | `Guo:2023pqw` §II, eqs. (1), (5) | Ch19 |
| Q.19 | E27 | `Collins2011` Fig. 7.10; eqs. (11.4)–(11.6) | right-of-cut gluon Wilson-line vertex $+g_0n^\mu f_{k\alpha j}$; indices interchanged | $-g_0n^\mu f_{k\alpha j}$; $K_{\mu\nu}=k_\mu w_{2\nu}/(k\cdot w_2-i0)$ | the author's errata list (22 May 2026, §3) | Ch9, App B, App F |
| Q.20 | E29 | GKL 1988 ($O(\alpha_s^3)$ coefficient of $R$) | the incorrect $r_3$ | $r_3=-6.63694-1.20013n_f-0.00518n_f^2-1.2395\eta$ | `GorishniiKataevLarin1991`, `SurguladzeSamuel1991` | Ch6 |
| Q.21 | E30 | `Collins1993`, appendix | the T-invariance argument that the Sivers function vanishes | the Wilson line gives $f_{1T}^\perp|_{\rm SIDIS}=-f_{1T}^\perp|_{\rm DY}$ | `Collins2002` after `BrodskyHwangSchmidt2002` | Ch14 |

Not in App Q (verify patch v2.3): E22 and E32 (refuted: nothing printed), E19 (withdrawn; never printed), E28 (convention remark, Ch2/Ch16), E31 (quotation of Collins 2011, Ch12), E33 (rule: corrected versions are used); class Q3 items go to status paragraphs with attribution: E05 (Ch22), E07 (Ch22, Ch23), E14, E15 (Ch4, App D, Ch24), E16 (Ch16, Ch24), E24 (Ch15), E34 (Ch21, Ch24; no verdict), E35 (Ch8, Ch24), E36 (Ch18, Ch24). Slips in our own working files and the reference document's errors are never listed (§00.5 is internal).

**Notes for `sec:appQ-notes`** (one each; formulas in our conventions): Q.3 — $F(k)=\int\frac{d^2l}{(l^2+m_g^2)((k-l)^2+m_q^2)}$, $G$ the two-loop analogue; $\int d^2k_T(I_1+I_2)=0$ exactly, while $I_1(0)+I_2(0)<0$ (Ch18; the first line of the same equation also lacks two squares and carries $+i\epsilon$ on the conjugate side). Q.8 — the full corrected kernel as in `prop:lamet-hybrid-kernel`. Q.11 — for the LFWF, consistency with the one-loop results of PRD 105 requires $\tilde\psi^\pm\sqrt{S_r}=H^\pm e^{\frac12\ln((\mp\zeta_z+i0)/\zeta)\tilde K}\psi^\pm$, as written in `Liu:2023onm`; the "$-i0$" of PRD 105 eqs. (49), (74) is inconsistent for $\psi^+$ (no published note found). Q.15 — with their $\beta_0=-(11C_A/3-4n_fT_F/3)/(2\pi)$ the correct coefficient in $\ln S_I$ is $\alpha_s^2\beta_0C_F/(4\pi)$; the single-log error of (81) follows from the sign of Q.12.'''

def _fix_pipes(text):
    """inside table rows, replace | within $...$ math by \\vert (table-safe)"""
    out = []
    for line in text.split('\n'):
        if line.startswith('|'):
            parts = line.split('$')
            for i in range(1, len(parts), 2):
                parts[i] = parts[i].replace('|', '\\vert ')
            line = '$'.join(parts)
        out.append(line)
    return '\n'.join(out)

APPQ_TABLES = _fix_pipes(APPQ_TABLES)
S004 = _fix_pipes(S004)

OPS = [
 # ---------------- 00.2 item 7: the fibered error type
 ('sub', 'has the column 「误差类型」 with E-S / E-P / E-F / E-N / E-W, and each', 'has the column 「误差类型」 with E-S / E-P / E-F / E-N / E-N$^\\varphi$ (fibered integral norm, `def:appN-fibered`; v2.3) / E-W, and each', '7. **Error types.** Each status table'),
 # ---------------- 00.3: tags of the new App O assumptions
 ('sub', '`asm:appN-brst-nonlocal` (`\\tagC`, named gap, merge decision MD1), and all `asm:appO-*`;', '`asm:appN-brst-nonlocal` (`\\tagC`, named gap, merge decision MD1), and all `asm:appO-*` except `asm:appO-adjacent-swap` and `asm:appO-real-jets` (`\\tagP`: proven in the scalar spectator model, argued for QCD jets; they enter only the QCD transfer of the App O model theorems, which are [P], and are premises of no [A] statement; v2.3);', 'this applies to all `asm:appM-*`, all `asm:appN-*` except'),
 # ---------------- 00.4 rewritten
 ('range', '### 00.4 [PENDING-VERIFY] slots for the proof extensions X1, X2, X3\n', '### 00.5 Corrections of the reference that the appendices implement', S004 + '\n\n', False),
 # ---------------- 00.5 ledger
 ('sub', '(`prop:dy-eikonal-twogluon`, `lem:appO-glauber-operator`, `ex:appO-two-exchange`) |', '(`prop:dy-eikonal-twogluon`, `lem:appO-glauber-operator`, `ex:appO-two-exchange`; known result, `Meggiolaro:1996hf`) |\n' + ERR_S1B, '| ERR-S1 | App O §O.5, §O.8 |'),
 ('sub', 'fixed-order assumption (c1) replaced by `lem:appO-joint-localization` (ordering weights); the non-analytic $k^+$ dependence of the weights joins the H-emission obstruction in `asm:appO-deformation`(d) |',
  'fixed-order assumption (c1) replaced by `lem:appO-joint-localization` (ordering weights: continuous with a kink at $k_j^+=0$ for spectator insertions, the initial group time-reversed, mixed signs give products; error bound with $\\sum_\\sigma\\vert w_\\sigma\\vert$); the non-analytic $k^+$ dependence of the weights joins the H-emission obstruction in `asm:appO-deformation`(d); per-graph weights are not fixed by window data (`prop:appO-pergraph-weights`) |',
  '| ERR-S3 | App O §O.5–§O.6 |'),
 ('sub', 'discharge slots X3a, X3d |', 'discharge slots X3a (not delivered: reduction to (CTp), `rem:appM-remainder-reduction`) and X3d (partial: (B1) retired, (B2) ≡ (Eε), `thm:appM-brst-reduction`) |', '| ERR-M26 | App M §M.4–§M.6 |'),
 # ---------------- App P
 ('sub', 'Pending items (`[PENDING-VERIFY]`) are listed in `tab:appP-checks` until the verification patch removes them.', 'After the verify patch (v2.3) no pending-verification items remain; C-P13 checks this.', '6. **注 `rem:appP-limits` —'),
 ('sub', '`% errtype: E-S|E-P|E-F|E-N|E-W`, `% PENDING-VERIFY: <label> <claim/X-item>`.', '`% errtype: E-S|E-P|E-F|E-N|E-Nphi|E-W` (the pending-verification comment type is retired by the verify patch; C-P13).', '2. *Comments:* strip `%`-comments'),
 ('sub', '| C-P13 | no `% PENDING-VERIFY` comment and no reserved slot label of §10 (the X1–X3 slots of App M/N/O) remains | W (E with `--final`) |', '| C-P13 | no pending-verification comment and no withdrawn slot label of §10 (the undelivered X1–X3 slots of App M/N/O) remains | W (E with `--final`) |', '| C-P13 |'),
 # ---------------- App Q
 ('sub', '`\\label{app:appQ}` · `appQ_errata.tex` · **4 pp** · written after `verify/` completes · **[PENDING-VERIFY]** as a whole', '`\\label{app:appQ}` · `appQ_errata.tex` · **4 pp** · final rows from the verification records (verify patch v2.3)', '`\\label{app:appQ}` · `appQ_errata.tex`'),
 ('sub', '`tab:appQ-errata` (class Q1); optional `tab:appQ-errata-b` (class Q2, only if the patch decides)', '`tab:appQ-errata` (class Q1, 16 rows); `tab:appQ-errata-b` (class Q2, 5 rows; decided by the verify patch)', '| Q.2 | `sec:appQ-errata` 勘误表 |'),
 ('range', '**Pending candidate list**', '- **注 `rem:appQ-scope` — 附录 Q 不包含什么**', APPQ_TABLES + '\n\n', False),
]
