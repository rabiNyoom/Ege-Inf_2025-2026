from fnmatch import fnmatch
r = []
c = 0
for n in range(10000000, 0, -1):
    if n % 217 == 0 and fnmatch(str(n), '14?4*'):
        r.append([n, sum(d for d in range(1, n+1, 2) if n % d == 0)])
        c += 1
        if c == 7:
            break
for s in reversed(r):
    print(*s)
