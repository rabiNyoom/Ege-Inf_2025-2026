from itertools import product
c = 0
for p in product('САЛО', repeat=6):
    if 1 <= p.count('О') <= 3:
        c += 1
print(c)
