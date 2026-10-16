#!/bin/bash
# Concatenate parts into the unit file, copy to the test dir, compile.
set -e
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
P="$W/writing/work/W26/parts"
OUT="$W/chapters/ch23_yzliu.tex"
T="$W/writing/test/W26"
python3 -I "$W/writing/work/W26/assemble.py"
cp "$OUT" "$T/ch23_yzliu.tex"
cd "$T"
cat > test_yzliu.tex <<'EOT'
\input{preamble_fact.tex}
\begin{document}
\input{ch23_yzliu.tex}
\bibliographystyle{unsrt}
\bibliography{refs_merged_v2}
\end{document}
EOT
xelatex -interaction=nonstopmode test_yzliu.tex > run1.log 2>&1 || true
bibtex test_yzliu > bib.log 2>&1 || true
xelatex -interaction=nonstopmode test_yzliu.tex > run2.log 2>&1 || true
xelatex -interaction=nonstopmode test_yzliu.tex > run3.log 2>&1 || true
echo "errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop\|^!' test_yzliu.log)"
grep -n '^!' test_yzliu.log | head -20 || true
echo "overfull:"; grep -n 'Overfull \\hbox' test_yzliu.log | head -30 || true
echo "missing chars:"; grep -c 'Missing character' test_yzliu.log || true
echo "undefined citations:"; grep 'Citation .* undefined' test_yzliu.log | sort -u | head || true
echo "multiply defined:"; grep 'multiply defined' test_yzliu.log | head || true
grep -c 'Reference .* undefined' test_yzliu.log || true
pdfinfo test_yzliu.pdf 2>/dev/null | grep Pages || true
