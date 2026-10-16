"""Builds the assumption register table (FINAL_OUTLINE_v2 §08 `### Assumptions` = ASSUMPTIONS.md §1) for spec v2.3.
Rows: the original rows (pre-patch backup), with the seven rows whose math cells were broken by unescaped `|` rebuilt from
the full entries, the rows whose status changed in the verify patch overridden, and the six new entries added.
"used by" is recomputed from the final `\\uses` data of the outline text passed in."""
import os, re, importlib.util
import src

CHK = '/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/spec_v2/checks/check_final_outline_v2.py'
_spec = importlib.util.spec_from_file_location('chk_fo2', CHK)
chk = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(chk)

OWNER_ORDER = ['Ch01', 'AppM', 'AppN', 'AppO', 'Ch22', 'Ch23', 'Ch24']
OWNER_NAME = {'Ch01': 'Ch1', 'AppM': 'AppM', 'AppN': 'AppN', 'AppO': 'AppO', 'Ch22': 'Ch22', 'Ch23': 'Ch23', 'Ch24': 'Ch24'}

def orig_rows():
    rows = {}
    in_tab = False
    for line in src.lines('FINAL_OUTLINE_v2.md'):
        if line.startswith('### Assumptions'):
            in_tab = True; continue
        if in_tab and line.startswith('Total:'):
            break
        if in_tab:
            m = re.match(r'^\|\s*`(asm:[A-Za-z0-9\-]+)`\s*\|(.*)$', line)
            if m:
                cells = [c.strip() for c in m.group(2).split('|')]
                rows[m.group(1)] = cells
    return rows

# --- (1) the seven rows broken by `|` inside math: rebuilt from the full entries (ASSUMPTIONS.md §3)
BROKEN = {
 'asm:intro-np-ope': dict(content=r'(O1) direction-uniform Euclidean OPE to every finite level $N$ between the vacuum and hadron states, remainder $O(\vert q\vert^{2-N-\delta}\ln^k\vert q\vert)$ with bounds on all $q$-derivatives, Lorentz-covariant coefficients; (O2) odd-twist coefficients $\propto m_q/\vert q\vert$',
                          status='open, widely assumed; vacuum part `conj:ee-np-ope` [C]; asymptotic only (renormalons, instantons)',
                          upgrade='a non-perturbative definition of the OPE (OP-A3)'),
 'asm:intro-af-coeff': dict(content=r'at $\mu=\vert q\vert$ the OPE coefficients are asymptotic to their $\overline{\rm MS}$ series: $\tilde C_i(q;\vert q\vert)=\vert q\vert^{2-d_i}[\sum_{k\le K}c_{i,k}(\hat q)\alpha_s(\vert q\vert)^k+O(\alpha_s^{K+1})]$; light-quark masses as higher-dimension terms',
                            status='open; compatible with renormalons and instantons',
                            upgrade='as for `asm:intro-np-ope` (OP-A3)'),
 'asm:appM-remainder': dict(content=r'massive Euclidean model, each order: every $h\in\mathcal H_{a,\Gamma}$ (derivatives, multiplications by $p$ and $m\partial_m$ of the frozen-$q$ normal product $\tilde N_{a,\Gamma}$) obeys $\vert h\vert\le K_h\vert q\vert^{D-1-a}(\ln\vert q\vert)^k$, uniformly in $q/\vert q\vert$',
                            status='open in the stated form; reduced to the zero-momentum matching estimate (CTp), `rem:appM-remainder-reduction` (slot X3a not delivered: the uniqueness route is circular)',
                            upgrade='prove (CTp) by sector estimates, or a momentum-space OPE theorem whose scope is verified'),
 'asm:appM-forward': dict(content=r'massless QCD, DR, on-shell parton target: $T^{\mu\nu}_j-\sum_{d_O\le N}\tilde C^{\mu\nu}_O\langle p\vert[O]\vert p\rangle=O(\vert q\vert^{1-N}\ln^k\vert q\vert)$ at each order, uniformly in the Euclidean direction',
                          status=r'open; per graph the forward expansion is proved (`thm:appM-forward-expansion`); `cor:appM-forward-ope` reduces it to (A3), (Eε), the Joglekar–Lee triangularity and `asm:appM-oswi`; one loop exact in $\varepsilon$ for $N\le8$ (VF-DIS-13)',
                          upgrade='discharge the inputs of `cor:appM-forward-ope` (OP-A5)'),
 'asm:appN-envelope': dict(content=r'envelopes $\Phi_{R_0}$ on $U_{R_0}$ with $\int\Phi_{R_0}\le CL^K$ dominating every partially approximated integrand; uniform integrability at $\Vert k\Vert\ge1$; pointwise boost bound $\vert f_i-T_{R_0}f_i\vert\le C(s_{R_0}/t_{R_0})g_i$',
                           status='open (never written in integral form at all orders); fibered version for the scalar models (`thm:appN-fibered-subtraction`)',
                           upgrade='an integral version of the Sterman–Collins power counting (sector decomposition per region)'),
 'asm:appN-separation': dict(content=r'virtuality $\ge c\,t_R^2$ on $\mathsf H_R$ lines; $\vert l^+\vert\ge c\,t_R$ on jet lines changed by $T_R$; for soft momenta $\vert k^+k^-\vert\ge c\,\mathbf k_T^2$ and $\vert\tilde D\vert\ge c(\vert p^+\vert\vert k^-\vert+v_A(p))$',
                             status='open in general; verified in the one-loop triangle; the exponent 2 in (i) is an independent (Łojasiewicz-type) assumption',
                             upgrade='Łojasiewicz inequalities for the Landau varieties of leading regions plus a deformation theorem (App O for the Glauber part)'),
 'asm:lamet-large-z': dict(content=r'(LZ1) the region $\vert\lambda\vert>z_0P^z$ contributes $o(1)$ to the Fourier transform of $\tilde h-\tilde h_{\rm tw2}$ at fixed $x\in(0,1)$; (LZ2) the same with $\tilde h-\tilde h_{\rm tw2}-\tilde h_{\rm tw4}$ is $o(P_z^{-2})$',
                           status='open; `thm:lamet-exp-decay` gives decay under `asm:lamet-gap` but no usable constants',
                           upgrade='quantitative exponential decay of hadronic matrix elements with constants uniform in $P^z$'),
}

# --- (2) rows whose status changed in the verify patch (v2.3)
CHANGED = {
 'asm:appM-brst-ope': dict(title='OPE 的 BRST 结构：带一个复合旁观者的欧氏展开 (Eε)',
                           content='(B2) ≡ (Eε): in bare DR at generic $\\varepsilon$, the large-$q$ expansion with one composite spectator $Z=s\\phi$ holds with the coefficients of the expansion without $Z$ plus merged coefficients $C^Z_{O\'}$ polynomial in $p_Z$; (B1) retired',
                           status='open; slot X3d partial: the reduction to gauge-invariant operators is proved under (Eε) (`thm:appM-brst-reduction`); Joglekar read at abstract level, Hollands\' QCD scope not verified',
                           upgrade='prove (Eε) (graph-by-graph DR expansion with one composite spectator)'),
 'asm:appN-collins': dict(status='[A]-level (Collins 2011 ch. 10); complete for the one-loop off-shell triangle (`prop:appN-triangle-cs`, slot X2a); fibered framework `thm:appN-fibered-subtraction`; slots X2b, X2c not delivered',
                          upgrade='grouped power counting under (Com)(Abs); the fibered programme `rem:appN-fibered-allorders`'),
 'asm:appO-lcopt': dict(status='open; partial results in the light-front literature (`Schoonderwoerd:1998qj`, `Schoonderwoerd:1998iy`); Hermiticity of the cut rules: `lem:appJ-cut-hermiticity` (corrected in v2.3)'),
 'asm:appO-envelope': dict(content='envelope $\\hat\\Phi_R$ for all fibre-integration errors of the equal-time rewriting, uniform in $\\varepsilon$ and $\\eta_0$; boundary layers; for coincident connections imposed on side-summed families',
                           status='open; Glauber specific; the per-graph version cannot hold within the class of `prop:appO-pergraph-weights`'),
 'asm:appO-mixing': dict(content="(a′) pre-integration localization with envelope bounds (incl. $\\sum_\\sigma\\vert w_\\sigma\\vert$ and the exceptional sets $E_j$); (b) cut compatibility of $S$; (c) for coincident connections the complete graph set gives $\\mathcal W'^\\dagger\\mathcal W=1+O(\\lambda^a)$ weakly",
                         status='(a′)(b) automatic for $\\mathcal G_0$; (c) holds for two-gluon exchange between eikonal lines at $O(g^4)$ (`prop:dy-eikonal-twogluon`); model evidence for the uncut lines of composite spectators (`prop:appO-twoexch-spectator`, slot X1f partial); cut direct lines, $O(g^6)$ (`prop:appO-g6-ladder`) open',
                         upgrade='all-order unitarity argument for the complete graph set incl. cut direct lines; the matching `asm:appO-collinear-ends`'),
 'asm:appO-deformation': dict(content='(a) deformation targets for general configurations; (b) compatibility with the region set algebra; (c) (CS1)(CS2) on the soft-angle region incl. the out-of-window parts and wee-line endpoints of the side-independent windows; (d) H-emission endpoints and coincident SA/AS insertions',
                              status='(a) proved for $\\mathcal G_0$ and graded configurations; window-edge terms vanish identically (`lem:appO-side-independent-windows`, slot X1c); (b)(c)(d) open, needed even for abelian $\\mathcal G_0$ (slot X1d not delivered)',
                              upgrade='soft-scale treatment of spectator couplings; analyticity of the ordering weights near $k^+=0$'),
}

# --- (3) the six new entries
NEW = {
 'asm:appM-oswi': dict(owner='AppM', tag='[A]', title='前向在壳胶子振幅的 Ward 恒等式',
                       content=r'$p^aM_{ab}\varepsilon^b=0=\varepsilon^aM_{ab}p^b$ for the amputated forward on-shell gluon Compton amplitude at each order in DR, for all $\varepsilon\cdot p=0$ (incl. $\varepsilon=p$); equivalently $p^aM_{ab}\propto p_b$',
                       status='[A] (BRST Ward identity of the forward amplitude; the zero-momentum subtleties of `rem:appM-forward-aliens` are the reason it is stated separately)',
                       upgrade='a proof of the forward on-shell Ward identity at all orders'),
 'asm:appN-lce': dict(owner='AppN', tag='[A]', title='光锥序表示与协变值的等同（LCE）',
                      content=r'for graphs of the scalar models (M1), (M2) satisfying the hypotheses of `lem:appN-lc-positivity` and (IRF), the fibered value equals the covariant value, $\int_B\rho_G\,d\mu_\varepsilon=I_G$',
                      status='[A]: proved for each graph by `lem:appN-identification` once (FR) is checked; open as a statement for all graphs',
                      upgrade='a general proof of (FI) for the scalar models (light-front perturbation theory)'),
 'asm:appN-analytic-reg': dict(owner='AppN', tag='[A]', title='两圈图样积分的辅助解析正规化',
                               content=r'(RA1) the analytically regularized pattern integrals of the two-loop planar vertex are meromorphic in $(\varepsilon,\delta)$; (RA2) the nine single-approximator integrals are regular at $\delta=0$ for small $\varepsilon\ne0$ with their DR values as limits',
                               status='[A]: analytic renormalization covers quadratic propagators, not the eikonal-type linear factors',
                               upgrade='meromorphy for linear (eikonal) factors'),
 'asm:appO-adjacent-swap': dict(owner='AppO', tag='[P]', title='相邻交换对称性（ADJ）',
                                content='(ADJ) of `def:appO-sectors` for the leading-power cut-summed LCOPT jet factors of QCD graphs with two spectator insertions',
                                status='proved in the scalar spectator model; argued, not proved, for spin-summed QCD jets; enters only the QCD transfer of the model theorems',
                                upgrade='a proof for leading-power LCOPT jets'),
 'asm:appO-real-jets': dict(owner='AppO', tag='[P]', title='旁观者喷注函数的实性（REAL）',
                            content='(REAL) of `def:appO-sectors`: every colour-stripped jet function is a fixed phase times a rational function with real coefficients',
                            status='proved in the scalar spectator model; argued for spin-summed QCD jets; enters only the QCD transfer of the model theorems',
                            upgrade='a proof for leading-power LCOPT jets'),
 'asm:appO-collinear-ends': dict(owner='AppO', tag='[A]', title='共线端点的匹配',
                                 content='with two-sided analytic rapidity regulators on the SS windows, the $A$- and $B$-collinear ends (and the cut contributions located there) are reproduced by collinear factorization with no leftover Hermitian $C_AX$ (fully coincident) or $[X_1,X_2]$ (half-coincident) term',
                                 status='open; relocates, not removes, the content of `asm:appO-mixing`(c) for coincident $O(g^4)$ patterns; the half-coincident part is proved in the model with a $k^-$ regulator alone (`prop:appO-halfcoinc-sensitivity`); not a premise of `thm:appO-main`',
                                 upgrade='compute the cut direct-line contributions or prove their suppression (`rem:appO-cut-ss`)'),
}

COLS = ['owner', 'tag', 'title', 'content', 'status', 'usedby', 'upgrade']

def build(outline_text):
    ST = chk.parse(outline_text)
    order = [s['label'] for s in ST]
    asm_entries = [s for s in ST if s['pfx'] == 'asm']
    unit_of = {s['label']: s['unit'] for s in asm_entries}
    users = {s['label']: [] for s in asm_entries}
    for s in ST:
        for u in s['uses']:
            if u in users and s['label'] not in users[u]:
                users[u].append(s['label'])
    orig = orig_rows()
    rows = []
    for owner in OWNER_ORDER:
        for s in asm_entries:
            if s['unit'] != owner:
                continue
            lab = s['label']
            if lab in NEW:
                d = dict(NEW[lab])
            else:
                c = orig[lab]
                if lab in BROKEN:
                    d = dict(owner=c[0], tag=c[1], title=c[2])
                    d.update(BROKEN[lab])
                else:
                    d = dict(owner=c[0], tag=c[1], title=c[2], content=c[3], status=c[4], upgrade=c[6] if len(c) > 6 else '')
                if lab in CHANGED:
                    d.update(CHANGED[lab])
            d['usedby'] = ', '.join('`%s`' % u for u in users[lab]) if users[lab] else '—'
            rows.append((lab, d))
    lines = ['| label | owner | tag | 中文标题 | content (one line) | status | used by (direct, computed) | upgrade path |',
             '|---|---|---|---|---|---|---|---|']
    for lab, d in rows:
        for k in ('content', 'status', 'upgrade', 'title'):
            assert '|' not in d[k].replace('\\vert', ''), (lab, k)
            assert all(ord(ch) >= 32 for ch in d[k]), ('control character', lab, k)
        lines.append('| `%s` | %s | %s | %s | %s | %s | %s | %s |' % (lab, d['owner'], d['tag'], d['title'], d['content'], d['status'], d['usedby'], d['upgrade']))
    cnt = {}
    for lab, d in rows:
        cnt[d['owner']] = cnt.get(d['owner'], 0) + 1
    tags = {}
    for lab, d in rows:
        tags[d['tag']] = tags.get(d['tag'], 0) + 1
    n_glob = sum(1 for lab, d in rows if lab.startswith('asm:intro-'))
    total = ('Total: **%d** entries (%d global; %d App M; %d App N; %d App O; %d Ch22; %d Ch23; %d Ch24). Tags: [A] %d, [C] %d, [P] %d, — %d.'
             % (len(rows), n_glob, cnt.get('AppM', 0), cnt.get('AppN', 0), cnt.get('AppO', 0), cnt.get('Ch22', 0), cnt.get('Ch23', 0),
                cnt.get('Ch24', 0), tags.get('[A]', 0), tags.get('[C]', 0), tags.get('[P]', 0), tags.get('—', 0)))
    return '\n'.join(lines), total, rows

LABLIST = re.compile(r'`(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9\-]+`(?:,\s*`(?:def|asm|thm|lem|prop|cor|conj|rem|ex):[A-Za-z0-9\-]+`)*')
HEADS = [re.compile(r'^\s*(?:[*-]|\d+\.)\s+\*\*(?:假设\s+)?`(asm:[A-Za-z0-9\-]+)`'), re.compile(r'^####\s+`(asm:[A-Za-z0-9\-]+)`')]

def users_map(outline_text):
    ST = chk.parse(outline_text)
    users = {s['label']: [] for s in ST if s['pfx'] == 'asm'}
    for s in ST:
        for u in s['uses']:
            if u in users and s['label'] not in users[u]:
                users[u].append(s['label'])
    return users

def update_users(text, users):
    """replace the first label list after '被使用于' inside each assumption entry by the computed users"""
    lines = text.split('\n')
    cur = None
    changed = []
    for i, l in enumerate(lines):
        for h in HEADS:
            m = h.match(l)
            if m:
                cur = m.group(1)
                break
        else:
            if l.startswith('#') or (l.strip() and not l.startswith(' ') and not l.startswith('-') and not l.startswith('*') and not re.match(r'^\d+\.', l)):
                pass
        if cur and '被使用于：' in l and cur in users:
            k = l.find('被使用于：')
            m = LABLIST.search(l, k)
            if m:
                us = users[cur]
                if '`def:intro-MA` refers to all six global entries' in l:
                    us = [u for u in us if u != 'def:intro-MA']
                new = ', '.join('`%s`' % u for u in us) if us else '—'
                if m.group(0) != new:
                    changed.append(cur)
                lines[i] = l[:m.start()] + new + l[m.end():]
    return '\n'.join(lines), changed
