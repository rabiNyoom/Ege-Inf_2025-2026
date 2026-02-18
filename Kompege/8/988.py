from itertools import product
for i, p in enumerate(product('АИМРЯ', repeat=4), 1):
    s = ''.join(p)
    if s == 'АРИЯ':
        print(i)
        break
