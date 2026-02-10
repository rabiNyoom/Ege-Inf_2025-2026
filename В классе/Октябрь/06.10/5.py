def algo(n):
    nb = bin(n)[2:]
    if nb.count('1') % 2 == 0:
        nb = '10' + nb[2:] + '0'
    else:
        nb = '11' + nb[2:] + '1'
    return int(nb, 2)
for n in range(1, 1000):
    if algo(n) > 50:
        print(n)
        break
# 19