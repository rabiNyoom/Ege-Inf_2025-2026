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


primes = sieve(8000000)
primes_set = set(primes)


def F(n):
    sqrt = n**0.5
    for d in primes:
        if d > sqrt:
            return 0
        if d % 2 == 1 and n % d == 0:
            dd = n // d
            if (
                d != dd
                and dd % 2 == 1
                and dd in primes_set
                and abs(dd - d) in primes_set
            ):
                return max(d, dd)


c = 0
n = 5000001
while c != 5:
    d = F(n)
    if d:
        print(n, d)
        c += 1
    n += 2
