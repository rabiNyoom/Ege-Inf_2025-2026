def to5(n):
    buf = []
    while n != 0:
        buf.append(str(n%5))
        n //= 5
    buf.reverse()
    return ''.join(buf)
for x in range(4*625**1920):
    n = 4*625**1920 + 4*125**x - 4*25**1940 - 3*5**1950 - 1960
    if to5(n).count('0') == 1891:
        print(x)
        break
# 20