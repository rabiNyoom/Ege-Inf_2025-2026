def algo(n):
    isOdd = n % 2 == 1
    b = []
    while n != 0:
        b.append(n // 3)
        n //= 3
    b.reverse()
    b = list(map(str, b))
    c = ''.join(b)
    if isOdd:
        c += '3'
    else:
        c = '2' + c + str(int(c[-1]*2))
    return int(c, 3)

for x in range(1, 1000):
    if algo(x) > 100:
        print(x)
        break
