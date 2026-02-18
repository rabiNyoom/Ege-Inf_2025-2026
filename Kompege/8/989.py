from itertools import product
for i, p in enumerate(product('АИМРЯ', repeat=4), 1):
    if i == 211:
        print(''.join(p))
        break
