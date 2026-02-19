m = 0
for i, l in enumerate(open('9.txt'), 1):
    ns = sorted(map(int, l.split()))
    rep3 = [n for n in ns if ns.count(n) == 3]
    norep = [n for n in ns if ns.count(n) == 1]
    if len(rep3) == 3 and len(norep) == 4 and sum(norep) > sum(rep3):
        m = i
print(m)

# 11597
