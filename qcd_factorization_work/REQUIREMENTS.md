# User requirements (binding, accumulated; Chinese originals quoted)

1. (2026-10-08) "用 LaTeX 写一个 PDF 文件，严格、完整、详细地证明 QCD 因子化定理（包含各种情况，严格的和不严格的），
   同样要求费曼图（用 TikZ 画）、公式、论证清晰。这将是个更困难更大的任务，尽全力、不计成本去做。"

2. (2026-10-10) Reference document `factorization_qcd-2.pdf` in the project root (238 pp):
   "仔细的完整阅读，这份文件应该比较粗糙，仅供参考（不必模仿），然后完整的理解学习，融会贯通，写出并优化我们的
   最完整级别的证明文档，尽全力去做。查缺补漏，有则改之，无则加勉。"
   → Read completely (8-segment deep reading → refdoc/REFDOC_ANALYSIS.md); adopt and surpass its strengths
     (numbered-assumption conditional theorems; App C OPE proof; App D precise Collins subtraction; App E Glauber
     cancellation via LCPT), correct its errors, fill its gaps.

3. (2026-10-10) "我们的最终文档要求更加完整，多次检查有无物理问题，目标是作为有史以来最完整的、最清晰的，对于人类
   已证明所有过程的因子化定理综述，最后还要加上因子化的前沿进展，包含 Yizhuang Liu 的相关严格因子化研究，
   Xiangdong Ji 的 LaMET 因子化证明，一切都做到详尽严格完整。参考文档不完整的地方（比如只证明了特定的情况），
   我们也都要补全，做到真正的最完整。类比一下，类似于“数学中的 Lean 形式化”，我们也要真正的做到 formalism 和
   严格分级程度（但我并不排斥你在研究过程中，如果发现了新的严格性定理，这将是很好的事情）。开头可以采取类似于
   证明 furry 定理时的 qcd 引入，从基础的内容过渡到深层次，保证可读性。"
   → Consequences for the design:
     a. Coverage: every process for which factorization has been proven (and all important unproven/violated cases),
        as a complete review; physics checked multiple times (≥ 2 physics-focused review rounds).
     b. Frontier chapter(s): Yizhuang Liu's rigorous factorization work; Xiangdong Ji's LaMET factorization proofs
        (Izubuchi–Ji–Jin–Stewart–Zhao etc.); other recent rigorous progress (frontier/ research notes).
     c. Where the reference document proves only special cases, complete them where possible (new proofs must be
        adversarially verified and marked as such with honest grades); genuinely open problems are stated as
        numbered open assumptions — never claimed as proven.
     d. "Lean-like" formalism: every definition / assumption / lemma / theorem numbered and labelled, with explicit
        hypotheses, rigor grade, and recorded dependencies (`\uses{...}`); an automatically generated
        "formal blueprint" appendix (dependency graph + status table).
     e. Readability: start, like the Furry monograph, with a pedagogical QCD introduction (Lagrangian, gauge
        invariance, Feynman rules, renormalization, running coupling/asymptotic freedom, IR divergences), moving
        gradually to the deep material.

4. Practical constraints: account usage limits interrupt long runs; all intermediate work lives in this persistent
   directory so that every phase can resume from files.

5. (2026-10-10) "好的，最后嘱咐一句，每个部分都应该尽全力去做" — every part (research, spec, each chapter, figures,
   verification, review, integration) must be done with maximum effort; no part may be treated as minor.

6. (2026-10-14) "这挺好的，我希望是个大全式的，每个章节都写完整。章节前说没有证明的部分，可以补上的都尽量补上。目前证明非阿贝尔多次插入
   的相消了吗？所有细微的部分都需要配备证明。" — the book is encyclopedic (≈800–900 pp accepted; no length cap); every chapter
   complete; for every item a box lists as not proved, supply a proof wherever one can be supplied (full / restricted to an
   order, model or subclass / conditional on numbered assumptions / explicit counterexample for [V]); every subtle step gets a
   proof; deep research on the cancellation of non-abelian multiple Glauber insertions in inclusive DY (X4).
   → proofs/ (inventory, triage, verified proof documents), verify/research/X4-nonabelian-glauber/; results are inserted
     into the chapters after their writing pipelines (spec sync v2.5 + insertion stage).

7. (2026-10-14) Usage policy: "5小时滚动窗口额度使用不超过80%（超过就先暂停，等到下一个5小时滚动窗口再恢复运行），本周额度用量不超过70%
   （超过就等下周在跑），除非我明确指令现在可以把额度用完…关键在于cache不要丢失，一定不要丢失之前已经完成的任务进度。" and
   "质量优先，完整第一，时间不用着急". → writing/state/GUARD.md (usage guard reading the user's "Claude Usage" app),
   tools/usage_guard.py, tools/run_state.py; quality is never traded for speed.
