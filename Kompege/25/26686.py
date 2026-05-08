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


primes = sieve(100000000)
# print("found primes!")


def check(n):
    n_original = n
    dels = []
    i = 0
    while (d := primes[i]) <= n:
        if n % d == 0:
            dels.append(d)
            n //= d
        else:
            i += 1
    if n == 1 and len(dels) >= 6 and n_original % (summ := sum(dels)) == 0:
        return summ
    return 0


c = 0
n = 89428305
while c != 6:
    r = check(n)
    if r:
        print(n, r)
        c += 1
    n += 1
