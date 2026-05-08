def sieve(n):
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    for i in range(2, n + 1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    b = [i for i in range(2, n + 1) if a[i]]
    return b


prim = set(sieve(500000))


def S(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if i in prim:
                d.add(i)
            ii = n // i
            if ii in prim:
                d.add(ii)
    if len(d) == 0:
        return 0
    return sum(d)


c = 0
n = 499999
while c != 7:
    s = S(n)
    if s and s % 10 == 0:
        print(n, s)
        c += 1
    n -= 1
