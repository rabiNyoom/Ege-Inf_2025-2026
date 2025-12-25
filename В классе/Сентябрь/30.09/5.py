def algo(n: int):
    nb = bin(n)[2:]
    if n % 3 == 0:
        nb += '010'
    else:
        nb += bin(5 * (n % 3))[2:]
    return int(nb, 2)
for n in range(1, 1000):
    r = algo(n)
    if r > 300 and r % 2 == 0:
        print(n)
        break
# 39