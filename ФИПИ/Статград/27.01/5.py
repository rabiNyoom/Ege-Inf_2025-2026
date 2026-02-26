def to_3(n):
    s = ''
    while n != 0:
        s = str(n % 3) + s
        n //= 3
    return s


def algo(n):
    nt = to_3(n)
    if n % 3 == 0:
        nt += nt[-2:]
    else:
        nt += to_3(3*sum(list(map(int, nt))))
    return int(nt, 3)


res = 0
dt = 1000
for n in range(1, 1000):
    r = algo(n)
    delta = abs(826 - r)
    if delta < dt:
        dt = delta
        res = r
print(res)

# 840
