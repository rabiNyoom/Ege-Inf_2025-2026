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


primes = sieve(2000000)
primes_set = set(primes)


def F(n):
    for d in primes:
        if d > n:
            return 0, 0
        if n % d == 0 and str(d).count("5") == 1:
            dd = n // d
            if dd in primes_set and str(dd).count("5") == 1:
                return d, dd


c = 0
n = 1324728
while c != 5:
    d, dd = F(n)
    if d:
        print(n, max(d, dd))
        c += 1
    n += 1
