#!/bin/sh
# Build a test document for one figure part and render its first page.
#   sh build_one.sh <part basename without .tex> [dpi]
# Output: one/<name>.pdf, png/<name>-1.png (110 dpi) and png/<name>-z.png (zoom, default 220 dpi)
cd "$(dirname "$0")" || exit 1
name="$1"; zdpi="${2:-220}"
mkdir -p one png
python3 -I mkdummy.py "parts/$name.tex" > /dev/null
cp dummy_labels.tex "one/dummy_$name.tex"
cat > "one/$name.tex" <<EOF
\\input{../preamble_fact.tex}
\\AfterEndEnvironment{figure}{\\clearpage}
\\begin{document}
\\refstepcounter{chapter}\\thispagestyle{plain}
\\input{../parts/$name.tex}
\\input{dummy_$name.tex}
\\end{document}
EOF
cd one || exit 1
# preamble is one level up: TeX resolves \input{../preamble_fact.tex} relative to cwd
xelatex -interaction=nonstopmode -halt-on-error "$name.tex" > "$name.stdout" 2>&1
xelatex -interaction=nonstopmode -halt-on-error "$name.tex" > "$name.stdout" 2>&1
st=$?
grep -n -E "^!|Overfull|Undefined control|Missing character|LaTeX Error" "$name.log" | head -20
grep -n "Reference .* undefined" "$name.log" | head -5
[ $st -ne 0 ] && { echo "BUILD FAILED"; tail -25 "$name.log"; exit 1; }
cd ..
pdftoppm -r 110 -png -f 1 -l 1 "one/$name.pdf" "png/$name"
pdftoppm -r "$zdpi" -png -f 1 -l 1 "one/$name.pdf" "png/$name-z"
ls png | grep "^$name"
