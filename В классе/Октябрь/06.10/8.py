def to8(n):
    buf = []
    while n != 0:
        buf.append(str(n%8))
        n //= 8
    buf.reverse()
    return ''.join(buf)
c = 0
for n in range(1, 1000000):
    no = to8(n)
    if len(no) == 5 and no[0] in '24680' and no[-1] not in '26' and no.count('7') <= 2:
        c += 1
print(c)
# 9135