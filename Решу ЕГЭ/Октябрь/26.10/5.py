def algo(n):
    nb = f'{n:b}'
    if n % 5 == 0:
        nb += '11'
    else:
        nb += f'{(n // 5):b}'
    return int(nb, 10)
for n in range(1, 100000):
    if n % 2 == 1 and algo(n) >= 783:
        print(n)
        break

# 5