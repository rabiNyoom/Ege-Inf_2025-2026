from itertools import product
c = 0
for p in product('01234', repeat=6):
    if p[0] not in '01' and p[-1] not in '34':
        c += 1
print(c)
