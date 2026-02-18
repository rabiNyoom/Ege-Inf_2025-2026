from itertools import product
c = 0
for p in product('ПУЛЯ', repeat=6):
    if p.count('У') == 2:
        c += 1
print(c)
