def dels(n):
    d = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(n // i)
    return sorted(d)


c = 0
n = 500001
while c != 5:
    d = dels(n)
    mi = None
    for de in d:
        if de % 10 == 8 and de != 8 and de != n:
            mi = de
            break
    if mi:
        print(n, mi)
        c += 1
    n += 1
