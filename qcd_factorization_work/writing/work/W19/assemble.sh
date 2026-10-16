#!/bin/zsh
# assemble the unit file from the parts (W19, Ch16)
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
cat "$W/writing/work/W19/parts/p0_intro.tex" "$W/writing/work/W19/parts/p1_irsafe.tex" "$W/writing/work/W19/parts/p2_hadronization.tex" "$W/writing/work/W19/parts/p3_ngl.tex" "$W/writing/work/W19/parts/p4_sll.tex" > "$W/chapters/ch16_jets.tex"
T="$W/writing/test/W19"
cp "$W/chapters/ch16_jets.tex" "$T/"
