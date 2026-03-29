a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def to27(n):
    s = ''
    while n != 0:
        s = a[n % 27] + s
        n //= 27
    return s


n = 4 * 2187**2101 + 729**2000 - 5 * 243**2100 + 81**2200 - 3 * 27**2250 - 26244
print(len([d for d in to27(n) if d not in '0123456789']))
