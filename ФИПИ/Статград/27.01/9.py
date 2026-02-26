for l in open('9.txt'):
    ns = list(map(int, l.split()))
    ns.sort()

    rep3 = [n for n in ns if ns.count(n) == 3]
    rep2 = [n for n in ns if ns.count(n) == 2]
    norep = [n for n in ns if ns.count(n) == 1]

    if len(rep3) != 3 or len(rep2) != 2 or len(norep) != 2:
        continue
    mini = min(min(rep3), min(rep2))
    if sum(norep) <= mini:
        print(abs(mini))

# 448
