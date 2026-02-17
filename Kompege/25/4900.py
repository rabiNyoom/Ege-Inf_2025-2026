from fnmatch import fnmatch
r = []
for n in range(10**7, 0, -1):
    if fnmatch(str(n), '9?*55*7'):
        r.append([n, sum(d for d in range(1, n+1) if n % d == 0) % 21])
        if len(r) == 5:
            break
for res in reversed(r):
    print(*res)
