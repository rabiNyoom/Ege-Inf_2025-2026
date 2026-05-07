with open('primes.txt') as f:
    primes = list(map(int, f.read().split()))
    primes_set = set(primes)


def algo(n):
    sqrt = n ** 0.5
    for d in primes:
        if d > sqrt:
            return 0
        if n % d == 0:
            dd = n // d
            if dd in primes_set:
                return max(dd, d)
    return 0


c = 0
n = 8996453
while c != 5:
    r = algo(n)
    if r:
        print(n, r)
        c += 1
    n += 1
