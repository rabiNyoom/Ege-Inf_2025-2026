with open('primes.txt') as f:
    primes = set(map(int, f.read().strip().split()))


def F(n):
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
    return int(sum(d) / len(d))


c = 0
n = 9500001
while c != 5:
    f = F(n)
    if f and f % 813 == 0:
        print(n, f)
        c += 1
    n += 1
