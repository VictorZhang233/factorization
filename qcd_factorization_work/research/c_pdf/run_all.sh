#!/bin/sh
# Re-run every verification script of research/c_pdf and collect the summaries.
# Usage:  sh run_all.sh      (from any directory; paths are resolved relative to this file)
cd "$(dirname "$0")" || exit 1
mkdir -p logs
for s in s1_free_field s2_oneloop_qq s3_splitting s4_moments_local s5_anomalous_dims s5b_gauge_independence s6_uniqueness; do
  start=$(date +%s)
  python3 -I "scripts/$s.py" > "logs/$s.log" 2>&1
  echo "$s  exit=$?  $(( $(date +%s) - start ))s  :  $(grep SUMMARY "logs/$s.log")"
done | tee logs/SUMMARY.txt
