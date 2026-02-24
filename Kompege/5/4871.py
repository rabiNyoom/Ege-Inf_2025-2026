def algo(n):
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1

    if n % 5 == 0:
        n //= 5
    else:
        n -= 1

    if n % 11 == 0:
        n //= 11
    else:
        n -= 1
    return n == 8


c = 0
for n in range(1, 10000000):
    if algo(n):
        c += 1
print(c)
