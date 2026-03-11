def algo(n):
    nb = f'{n:b}'
    if n % 2 == 0:
        nb += '0'
    else:
        nb += '1'
    if nb.count('1') % 3 == 0:
        nb = '11' + nb[2:]
    else:
        nb = '10' + nb[2:]
    return int(nb, 2)


for n in range(1, 1000):
    r = algo(n)
    if r >= 26:
        print(n)
        break

# 9
