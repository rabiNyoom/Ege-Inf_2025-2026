from itertools import product


def isPrime(s: str):
    n = int(s)
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
        if d * d == n:
            return False
    return True


def algo(n):
    ns = set()
    digits = list(str(n))
    for p in product(digits, repeat=2):
        if p[0] != '0':
            ns.add(''.join(p))
    c = 0
    for n in ns:
        if isPrime(n):
            c += 1
    return c


m = 0
nn = 0
for n in range(100, 1000):
    r = algo(n)
    if r >= m:
        m = r
        nn = n
print(nn)
