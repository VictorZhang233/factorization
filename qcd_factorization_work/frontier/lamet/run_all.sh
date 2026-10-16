#!/bin/sh
# Re-run every numerical/symbolic check of LAMET.md and write logs/SUMMARY.txt
# usage:  sh run_all.sh      (from this directory; python3 with sympy/numpy/scipy/mpmath required)
cd "$(dirname "$0")" || exit 1
mkdir -p logs
: > logs/SUMMARY.txt
TOTP=0; TOTF=0
for s in s1_kernels s2_ft_testfunctions s3_threshold s4_tmd_bvz s5_lemmas s6_tmc s7_fourier; do
  python3 -I "scripts/$s.py" > "logs/$s.log" 2>&1
  P=$(grep -c '^PASS' "logs/$s.log"); F=$(grep -c '^FAIL' "logs/$s.log")
  TOTP=$((TOTP+P)); TOTF=$((TOTF+F))
  printf '%-22s %4d PASS %4d FAIL\n' "$s" "$P" "$F" | tee -a logs/SUMMARY.txt
done
printf '%-22s %4d PASS %4d FAIL\n' "TOTAL" "$TOTP" "$TOTF" | tee -a logs/SUMMARY.txt
date >> logs/SUMMARY.txt
