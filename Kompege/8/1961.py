from itertools import product
for i, p in enumerate(product('ЕЛМРУ', repeat=4), 1):
    if p[0] == 'Л':
        print(i)
        break
