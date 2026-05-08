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


primes = set(sieve(20000000))

low = int(106732567**0.25) + 1
up = int(152673836**0.25)

for n in range(low, up + 1):
    if n in primes:
        print(n**4, n**3)
