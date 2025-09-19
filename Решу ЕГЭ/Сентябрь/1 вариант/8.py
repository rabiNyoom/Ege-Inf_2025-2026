from itertools import *

c = 0

for p in product('ИВАН', repeat=5):
    if 'И' in p:
        c += 1

print(c)

# 781