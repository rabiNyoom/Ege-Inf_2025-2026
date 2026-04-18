from itertools import product
from re import compile
r = compile(r'[abc]{2}')
c = 0
for p in product('0123456789abc', repeat=6):
    if p[0] == '0':
        continue
    s = ''.join(p)
    if s.count('0') >= 2 and sum(s.count(d) for d in 'abc') == 2 and r.search(s):
        c += 1
print(c)
