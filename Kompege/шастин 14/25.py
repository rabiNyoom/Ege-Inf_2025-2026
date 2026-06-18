with open("out.txt") as f:
    primes = list(map(int, f.read().split()))


def check(n):
    mn = []
    i = 0
    while n >= (p := primes[i]):
        if n % p == 0:
            mn.append(p)
            n //= p
        else:
            i += 1
    if len(mn) == 3 and n == 1:
        return max(mn)
    else:
        return 0


c = 0
for n in range(5_000_001, 10_000_000):
    r = check(n)
    if r:
        print(n, r)
        c += 1
        if c == 5:
            break
