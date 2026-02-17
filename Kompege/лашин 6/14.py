a = '0123456789ABCDEFGHIJKLMNO'
def to25(n):
    s = ''
    while n != 0:
        s = a[n % 25] + s
        n //= 25
    return s

ns = [64**678 + 55**123 - x for x in range(1, 232)]
print(max(map(lambda x: to25(x).count('0'), ns)))