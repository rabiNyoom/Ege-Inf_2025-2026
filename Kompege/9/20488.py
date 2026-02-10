c = 0
for l in open('20488.txt'):
    ns = list(map(int, l.split()))
    rep = [n for n in ns if ns.count(n) > 1]
    norep = [n for n in ns if ns.count(n) == 1]

    fst = len(rep) > 0 and len(norep) > 0
    snd = max(ns) in norep
    thd = sum(norep) >= 3 * sum(rep)

    if fst and snd and thd:
        c += 1
print(c)

# 1382
