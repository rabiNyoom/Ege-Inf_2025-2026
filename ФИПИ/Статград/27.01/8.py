from itertools import product
for i, p in enumerate(product('АДЛОСФЦЩ', repeat=4), 1):
    if i % 2 != 1:
        continue
    if p[0] == 'А' or p[3] == 'А':
        continue
    if p.count('Л') >= 3:
        print(i)
        break

# 659
