r = []


def check_n(n):
    a = 0
    for d in range(1, int(n**0.5)+1):
        if n % d == 0:
            a += 1
            if d * d != n:
                a += 1
    if (n - a) % 23 == 0:
        r.append(n)


n = 999999999
while len(r) != 5:
    check_n(n)
    n -= 1

print(*reversed(r))

# 999999690 999999731 999999740 999999789 999999961
