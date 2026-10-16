#!/bin/sh
# Re-runs every check script of research/c_exclusive and writes logs/*.log and logs/SUMMARY.txt
cd "$(dirname "$0")/scripts" || exit 1
: > ../logs/SUMMARY.txt
for s in s1_da s2_erbl_kernel s3_erbl_eigen s4_pion_ff s5_tff s6_gpd s7_dvcs s8_meson; do
  python3 -I "$s.py" > "../logs/$s.log" 2>&1
  tail -n 40 "../logs/$s.log" | grep -E "^s[0-9].*PASS" >> ../logs/SUMMARY.txt || echo "$s: CRASHED (see logs/$s.log)" >> ../logs/SUMMARY.txt
done
cat ../logs/SUMMARY.txt
