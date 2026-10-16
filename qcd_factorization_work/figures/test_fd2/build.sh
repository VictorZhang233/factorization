#!/bin/sh
# usage: build.sh [label-substring]   (no argument: the whole set)
# assembles ../figset_D.tex, checks the blocks, writes the test document,
# compiles it twice with XeLaTeX and renders every page at 110 dpi.
cd "$(dirname "$0")" || exit 1
python3 -I split_check.py || { printf '%s\n' "SPLIT ERROR"; exit 1; }
if [ -n "$1" ]; then DOC=test_one; python3 -I mkdoc.py "$1" || exit 1; else DOC=test_fd2; python3 -I mkdoc.py || exit 1; fi
xelatex -interaction=nonstopmode -halt-on-error $DOC.tex > build_$DOC.log 2>&1 || { printf '%s\n' "LaTeX ERROR"; grep -n -A8 "^!" $DOC.log | head -40; exit 1; }
xelatex -interaction=nonstopmode -halt-on-error $DOC.tex > build_$DOC.log 2>&1 || { printf '%s\n' "LaTeX ERROR (2nd run)"; grep -n -A8 "^!" $DOC.log | head -40; exit 1; }
grep -n -E "Overfull|Underfull|undefined|multiply|Missing character|Error|Warning: Reference|Citation" $DOC.log | grep -v "Font shape" | head -30
P=png/$DOC; rm -f $P-*.png; pdftoppm -r 110 -png $DOC.pdf $P
printf 'pages: %s\n' "$(ls $P-*.png | wc -l | tr -d ' ')"
