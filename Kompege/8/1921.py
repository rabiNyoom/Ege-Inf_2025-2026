from itertools import product
c = 0
for p in product(range(10), repeat=3):
    if p[0] == 0:
        continue
    if p[0] <= p[1] <= p[2]:
        c += 1
print(c)
