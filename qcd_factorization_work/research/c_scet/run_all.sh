#!/bin/sh
# Re-run all c_scet verification scripts; logs in logs/, summary in logs/SUMMARY.txt
cd "$(dirname "$0")/scripts" || exit 1
: > ../logs/SUMMARY.txt
for s in common.py s1_scet_algebra.py s1_wilson_decoupling.py s2_thrust_oneloop.py s2_thrust_rg.py s3_nrqcd.py s4_bbns.py; do
  b=$(basename "$s" .py)
  python3 -I "$s" > "../logs/$b.log" 2>&1
  echo "$(tail -2 "../logs/$b.log" | head -1)" >> ../logs/SUMMARY.txt
done
cat ../logs/SUMMARY.txt
