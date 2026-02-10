def to5(n):
    s = []
    while n != 0:
        s.append(str(n % 5))
        n //= 5
    return ''.join(reversed(s))


def algo(n):
    n5 = to5(n)
    if int(n5[-1]) % 2 == 0:
        n5 = n5 + '2'
    else:
        n5 = '2' + n5 + '3'
    return int(n5, 5)


n = 0
for i in range(1, 5000):
    r = algo(i)
    if r < 1000:
        n = i
print(n)
