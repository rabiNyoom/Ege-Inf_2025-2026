def to3(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s


def algo(n):
    nt = to3(n)
    if n % 3 == 0:
        nt += nt[-2:]
    else:
        nt += to3(sum(map(int, nt)) * 2)
    return int(nt, 3)


r = float('inf')
for n in range(1, 1000):
    res = algo(n)
    if res < r and res > 520 and res % 2 == 1:
        r = res
print(r)
