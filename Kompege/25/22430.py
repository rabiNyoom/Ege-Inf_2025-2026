n = 10000000
ns = list(range(n+1))

ns[1] = 0
for i in range(2, n+1):
    if ns[i] != 0:
        j = 2 * i
        while j <= n:
            ns[j] = 0
            j += i

pr = set(ns)
pr.remove(0)


def dels(n):
    prim = []
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            if d in pr:
                prim.append(d)
            if d * d != n:
                if (n//d) in pr:
                    prim.append(n//d)
    prim.sort()
    if len(prim) < 4:
        M = 0
    else:
        M = prim[0] + prim[1] + prim[-2] + prim[-1]
    return M


c = 0
n = 456790
while c != 5:
    m = dels(n)
    if m % 114 == 39:
        print(n, m)
        c += 1
    n += 1
