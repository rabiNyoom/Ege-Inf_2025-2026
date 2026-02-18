from itertools import product
c = 0
for p in product('ВИШНЯ', repeat=6):
    if p.count('В') > 1:
        continue
    if p[0] == 'Ш':
        continue
    if p[-1] in 'ИЯ':
        continue
    c += 1
print(c)
