def isInc(n):
    return (n[0] < n[1] < n[2] < n[3] < n[4])


c = 0
for l in open('9.txt'):
    ns = list(map(int, l.split()))
    mima = min(ns) + max(ns)
    if isInc(ns) and mima <= (sum(ns) - mima):
        c += 1
print(c)
