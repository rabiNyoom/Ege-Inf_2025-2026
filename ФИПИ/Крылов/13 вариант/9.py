c = 0
for l in open('9.txt'):
    ns = list(map(int, l.split()))
    ns.sort()

    A = (sum(ns) - ns[3]) / ns[3] > 2
    B = (ns[0] + ns[3] == ns[1] + ns[2]) or (ns[0] + ns[1] ==
                                             ns[2] + ns[3]) or (ns[0] + ns[2] == ns[1] + ns[3])
    if A and B:
        c += 1
print(c)

# 1
