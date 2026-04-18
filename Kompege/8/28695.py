from re import compile
from itertools import *
c = 0
odd = set('13579b')
r = compile(r'([13579b])\1{2}')
for p in product('0123456789abc', repeat=6):
    if p[0] == '0':
        continue
    s = ''.join(p)
    if sum(1 for d in s if d in odd) == 3 and r.search(s):
        c += 1
print(c)
