from itertools import product
c = 0
for p in product('ЛОДКА', repeat=4):
    if p.count('О') >= 2:
        c += 1
print(c)
