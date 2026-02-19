conv = '0123456789ABCDEFGHIJKLMNOPQ'


def to_27(n):
    s = ''
    while n != 0:
        s = conv[n % 27] + s
        n //= 27
    return s


n = 3 * 2187**1801 + 729**2000 - 4*243**2100 + 81**2200 - 2*27**2400 - 13122
r = to_27(n)
print(sum([1 for d in r if d not in '012345678']))

# 3432
