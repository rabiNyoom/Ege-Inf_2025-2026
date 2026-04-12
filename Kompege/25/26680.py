with open('primes.txt') as f:
    primes = list(map(int, f.read().strip().split()))
    primes_set = set(primes)


def F(n):
    sqrt = n**0.5
    for d in primes:
        if d > sqrt:
            return 0
        if d % 2 == 1 and n % d == 0:
            dd = n // d
            if d != dd and dd % 2 == 1 and dd in primes_set and abs(dd-d) in primes_set:
                return max(d, dd)


c = 0
n = 5000001
while c != 5:
    d = F(n)
    if d:
        print(n, d)
        c += 1
    n += 2
