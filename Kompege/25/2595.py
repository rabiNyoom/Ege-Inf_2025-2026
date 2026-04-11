def dels(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    if len(d) < 5:
        return None
    return sorted(d)


n = 400_000_001
c = 0
while c != 5:
    d = dels(n)
    if d:
        p = d[0] * d[1] * d[2] * d[3] * d[4]
        if p <= n and p % 100 == 17:
            print(p, d[4])
            c += 1
    n += 1
