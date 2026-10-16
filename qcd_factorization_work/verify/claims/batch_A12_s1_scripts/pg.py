import sys
# usage: pg.py file.txt firstbookpage page [page2]
f, first, a = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
b = int(sys.argv[4]) if len(sys.argv) > 4 else a
pages = open(f, encoding='utf-8', errors='replace').read().split('\f')
for p in range(a, b+1):
    i = p - first
    print(f"========== BOOK PAGE {p} (pdf idx {i+1}) ==========")
    print(pages[i])
