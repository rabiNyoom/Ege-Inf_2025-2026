with open('primes.txt') as f:
    prim = set(map(int, f.read().strip().split()))


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
