#!/bin/zsh
# rerun_all.sh (X3 final2): re-run
#   (1) the 9 author scripts (scripts/) and compare with the stored logs in logs/,
#   (2) the final reviewer's scripts (review_final_scripts/: NE rank tests, triangle quadrature) and compare with
#       review_final_scripts/logs/,
#   (3) the five final2 scripts (final2_scripts/: fix1_bm_illustration, fix1_homogeneity, fix3_tail, fix4_ne_demand,
#       fix6_rg_legs) and compare with final2_logs/.
# Fresh logs go to final2_logs/rerun/; a one-line summary per script (sha256 prefixes) to final2_logs/rerun_all.log.
# Run:  zsh "<path>/final2_scripts/rerun_all.sh"
BASE="/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/verify/extend/X3-ope"
OUT="$BASE/final2_logs/rerun"
mkdir -p "$OUT"
SUM="$BASE/final2_logs/rerun_all.log"
: > "$SUM"
echo "rerun started $(date)" >> "$SUM"
run_one () {   # $1 = script dir, $2 = script stem, $3 = stored-log dir
  ( cd "$1" && python3 -I "$2.py" > "$OUT/$2.log" 2>&1 )
  new=$(shasum -a 256 "$OUT/$2.log" | cut -c1-16)
  old=$(shasum -a 256 "$3/$2.log" | cut -c1-16)
  if [ "$new" = "$old" ]; then st="IDENTICAL"; else st="DIFFERENT"; fi
  echo "$2  new=$new  stored=$old  $st  ($(tail -1 "$OUT/$2.log" | cut -c1-60))" >> "$SUM"
}
for s in f1_forward_graphs f2_triangle f3_matroid_lemma f4_projector_laurent f5_sd_signs f6_evanescent_tree f7_clifford_slots h1_hadronic_checks e1_ee_checks; do
  run_one "$BASE/scripts" "$s" "$BASE/logs"
done
for s in fr_ne_rank fr_ne_rank_allr fr_triangle; do
  run_one "$BASE/review_final_scripts" "$s" "$BASE/review_final_scripts/logs"
done
for s in fix1_bm_illustration fix1_homogeneity fix3_tail fix4_ne_demand fix6_rg_legs; do
  run_one "$BASE/final2_scripts" "$s" "$BASE/final2_logs"
done
echo "done $(date)" >> "$SUM"
