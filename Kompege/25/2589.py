def dels(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if i % 3 == 0:
                d.add(i)
            ii = n // i
            if ii % 3 == 0:
                d.add(ii)
    return sorted(d)


c = 0
n = 300001
while c != 4:
    d = dels(n)
    if len(d) == 5:
        print(n, max(d))
        c += 1
    n += 1
