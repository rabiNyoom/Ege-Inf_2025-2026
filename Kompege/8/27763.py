from itertools import product
c = 0
for p in product('0123456', repeat=5):
    if p[0] == '0':
        continue
    if p.count('0') == 1 and p.count('1') <= 2:
        c += 1
print(c)
