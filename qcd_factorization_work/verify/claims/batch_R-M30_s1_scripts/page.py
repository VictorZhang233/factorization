import sys
# usage: page.py first [last]  -> prints pages of refdoc.txt split by form feed (page 1 = before first FF)
path = "/Users/hao-cheng/Desktop/theorem proof/qcd_factorization_work/refdoc/refdoc.txt"
txt = open(path, encoding='utf-8').read()
pages = txt.split('\f')
a = int(sys.argv[1]); b = int(sys.argv[2]) if len(sys.argv) > 2 else a
for p in range(a, b+1):
    print(f"=================== PAGE {p} ===================")
    print(pages[p-1])
