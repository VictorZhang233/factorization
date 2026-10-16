#!/bin/zsh
# Assemble the W14 parts (explicit order) into the unit file and copy it into the test directory.
W="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work"
P="$W/writing/work/W14/parts"
OUT="$W/chapters/ch12_dy.tex"
: > "$OUT"
for f in p0_intro p1_born p2_regions p3_orientation p4_glauber p5_model p6_theorem p7_nlo p8_other p9_twist p10_summary; do
  cat "$P/$f.tex" >> "$OUT"; printf '\n' >> "$OUT"
done
cp "$OUT" "$W/writing/test/W14/ch12_dy.tex"
echo "assembled $(wc -l < "$OUT") lines"
