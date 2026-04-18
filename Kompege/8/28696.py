from re import compile
from itertools import product
odd = set('13579bd')
c = 0
r = compile(r'([13579bd]).\1')
for p in product('0123456789abcd', repeat=5):
    if p[0] == '0':
        continue
    s = ''.join(p)
    if sum(1 for d in s if d in odd) == 2 and r.search(s):
        c += 1
print(c)
