def algo(n):
    nb = f'{n:b}'
    if n % 3 == 0:
        nb += nb[-3:]
    else:
        nb += f'{(3*(n % 3 + 1)):b}'
    return int(nb, 2)


m = 0
for n in range(1, 10000):
    r = algo(n)
    if r <= 416:
        m = max(m, r)
print(m)

# 411
