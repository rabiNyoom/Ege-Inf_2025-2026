def dels(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)


n = 250201
c = 0
while c != 5:
    d = dels(n)
    if len(d) != 0:
        s = d[0] + d[-1]
        if s % 123 == 17:
            print(n, s)
            c += 1
    n += 1
