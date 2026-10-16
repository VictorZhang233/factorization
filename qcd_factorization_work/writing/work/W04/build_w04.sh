#!/bin/zsh
# build_w04.sh (writer W04): assemble Ch04 from its parts, copy the three units into the test directory,
# run xelatex + bibtex + xelatex x2 for each driver, and print the log checks of WRITER_SPEC_v2 Sec. 10.4.
set -u
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
P="$W/writing/work/W04/parts"
T="$W/writing/test/W04"
cat "$P/ch04_p0_intro.tex" "$P/ch04_p1_landau.tex" "$P/ch04_p2_cn.tex" "$P/ch04_p3_pinch.tex" \
    "$P/ch04_p4_power.tex" "$P/ch04_p5_glauber.tex" "$P/ch04_p6_cancel.tex" "$P/ch04_p7_regions.tex" \
    > "$W/chapters/ch04_ir.tex"
cp "$W/chapters/ch04_ir.tex" "$W/chapters/appD_landau.tex" "$W/chapters/appE_powercount.tex" "$T/"
cd "$T"
drivers=("$@"); if (( ${#drivers} == 0 )); then drivers=(test_ir test_appD test_appE test_all); fi
for drv in $drivers; do
  xelatex -interaction=nonstopmode $drv.tex > /dev/null 2>&1
  bibtex $drv > $drv.bibtex.out 2>&1
  xelatex -interaction=nonstopmode $drv.tex > /dev/null 2>&1
  xelatex -interaction=nonstopmode $drv.tex > /dev/null 2>&1
  echo "== $drv: pages $(pdfinfo $drv.pdf | awk '/Pages/{print $2}')"
  echo "   errors: $(grep -c 'LaTeX Error\|Undefined control sequence\|Emergency stop' $drv.log)"
  echo "   missing chars: $(grep -c 'Missing character' $drv.log)"
  echo "   overfull: $(grep -c 'Overfull' $drv.log)  $(grep 'Overfull' $drv.log | sed -e 's/^.*(\([0-9.]*pt\) too wide.*$/\1/' | tr '\n' ' ')"
  echo "   underfull hbox: $(grep -c 'Underfull \\hbox' $drv.log)"
  echo "   undefined citations: $(grep -c 'Citation .* undefined' $drv.log)"
  echo "   multiply defined: $(grep -c 'multiply defined' $drv.log)"
  echo "   undefined refs: $(grep 'Reference .* undefined' $drv.log | sed -e "s/.*Reference \`\([^']*\)'.*/\1/" | sort -u | wc -l | tr -d ' ')"
  echo "   bibtex warnings: $(grep -c 'Warning--' $drv.blg)"
done
