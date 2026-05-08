def sieve(n):
    a = [True] * (n + 1)
    a[0] = False
    a[1] = False
    for i in range(2, n + 1):
        if a[i]:
            for j in range(i * i, n + 1, i):
                a[j] = False
    b = [
        i
        for i in range(2, n + 1)
        if a[i] and (str(i).count("4") == 1 or str(i).count("7") == 1)
    ]
    return b


primes = sieve(3000000)


def check(n):
    c = 0
    l = 0
    for d in primes:
        if d > n:
            break
        if n % d == 0:
            c += 1
            l = d
            n //= d
    if c == 3 and n == 1:
        return l
    return 0


c = 0
n = 2400001
while c != 5:
    r = check(n)
    if r:
        c += 1
        print(n, r)
    n += 1
