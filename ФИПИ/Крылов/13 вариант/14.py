a = '01234'


def to5(n):
    s = ''
    while n != 0:
        s = a[n % 5] + s
        n //= 5
    return s


n = 4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3 * 5**100 - 660
r = to5(n)
print(r.count('4'))

# 3028
