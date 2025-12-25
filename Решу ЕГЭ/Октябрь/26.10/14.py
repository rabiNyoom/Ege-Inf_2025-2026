al = '0123456789ABCDEFGHIJKLMNOPQRS'
def to29(n):
    b = []
    while n != 0:
        b.append(al[n % 29])
        n //= 29
    b.reverse()
    return ''.join(b)
max0 = 0
for x in range(1, 8410+1):
    n = 29**293 + 29**271 - x
    if (c := to29(n).count('0')) > max0:
        max0 = c
print(max0)

# 24