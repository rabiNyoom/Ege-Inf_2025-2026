def S(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if i % 2 == 0:
                d.add(i)
            ii = n // i
            if ii % 2 == 0:
                d.add(ii)
    if len(d) == 0:
        return 0
    return sum(d)


for n in range(1204300, 1204381):
    s = S(n)
    if s and s % 10 == 0:
        print(n, s)
