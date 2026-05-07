with open("primes33.txt") as f:
    primes = list(map(int, f.read().split()))
    primes_set = set(primes)


def check(n):
    for d in primes:
        if d > n:
            return 0
        if n % d == 0:
            r = n // d
            if r in primes_set:
                return max(d, r)
            else:
                return 0
    return 0


c = 0
n = 8996453
while c != 5:
    r = check(n)
    if r:
        c += 1
        print(n, r)
    n += 1
