from itertools import product
c = 0
for p in product('ГЕПАРД', repeat=5):
    if p.count('Г') == 1 and p[0] != 'А' and p[-1] != 'Е':
        c += 1
print(c)
