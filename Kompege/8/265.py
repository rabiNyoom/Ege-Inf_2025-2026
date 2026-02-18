from itertools import product
last = 0
for i, p in enumerate(product('АГИЛМОРТ', repeat=4), 1):
    if ''.join(p).endswith('ИМ'):
        last = i
print(last)
