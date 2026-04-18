from itertools import product
from re import compile
even = set('02468a')
r = compile(r'([02468a])\1')
c = 0
for p in product('0123456789ab', repeat=5):
    if p[0] == '0':
        continue
    s = ''.join(p)
    if sum(1 for d in s if d in even) == 2 and r.search(s):
        c += 1
print(c)
