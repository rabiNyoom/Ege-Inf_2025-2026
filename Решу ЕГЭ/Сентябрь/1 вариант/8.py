from itertools import *

count = 0

for p in product('ИВАН', repeat=5):
    if 'И' in p:
        count += 1

print(count)

# 781