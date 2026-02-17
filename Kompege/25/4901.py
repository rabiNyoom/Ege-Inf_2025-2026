from fnmatch import fnmatch
c = 0
n = 0
while c != 7:
    if n % 6 == 0 and n % 7 == 0 and n % 8 == 0 and fnmatch(str(n), '?6*6*?6'):
        c += 1
        print(n, sum(d for d in range(1, n+1) if n % d == 0))
    n += 1
