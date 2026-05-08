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


primes = sieve(4000000)


def check(n):
    pal = False
    cnt = 0
    i = 0
    last = 0
    while True:
        d = primes[i]
        if d > n:
            break
        if n % d == 0:
            cnt += 1
            n //= d
            last = d
            s = str(d)
            if len(s) == 2 and s[0] == s[1]:
                pal = True
        else:
            i += 1
    if cnt == 4 and n == 1 and pal:
        return last
    return 0


c = 0
n = 3502101
while c != 5:
    r = check(n)
    if r:
        print(n, r)
        c += 1
    n += 1
