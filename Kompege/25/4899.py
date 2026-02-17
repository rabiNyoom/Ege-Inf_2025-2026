from fnmatch import fnmatch
c = 0
n = 0
while c != 7:
    if fnmatch(str(n), '6*97*5?') and len((chdel := [d for d in range(2, n+1, 2) if n % d == 0])) >= 4:
        c += 1
        print(n, sum(chdel))
    n += 1
