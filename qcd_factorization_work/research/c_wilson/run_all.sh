#!/bin/bash
# Re-runs every check of research/c_wilson and writes logs/<script>.log ; prints the PASS summaries.
# Usage:  cd "<this directory>" && ./run_all.sh
cd "$(dirname "$0")/scripts" || exit 1
for s in s1_wilson_rules s2_eikonal_identity s3_eikonal_approx s4_ward_tree s5_grammer_yennie s6_i0_poles; do
  python3 -I -u "$s.py" > "../logs/$s.log" 2>&1
  tail -1 "../logs/$s.log"
done
