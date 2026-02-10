from itertools import permutations


def algo(n):
    ns = set()
    digits = list(str(n))
    for p in permutations(digits, r=2):
        if p[0] != '0':
            ns.add(int(''.join(p)))
    return max(ns) - min(ns)


c = 0
for n in range(300, 401):
    if algo(n) == 20:
        c += 1
print(c)
