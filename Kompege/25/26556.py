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


primes = set(sieve(8000000))


def M(n):
    d = set()
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            if i in primes:
                d.add(i)
            ii = n // i
            if ii in primes:
                d.add(ii)
    if len(d) == 0:
        return 0
    return min(d) + max(d)


c = 0
n = 5700001
while c != 5:
    m = M(n)
    if m > 70000 and int((sqrt := m**0.5)) == sqrt:
        print(n, m)
        c += 1
    n += 1
