from itertools import *
c = 0
for p in product('01234567', repeat=5):
    s = ''.join(p)
    if s[0] in '2468' and s[-1] not in '26' and s.count('7') <= 2:
        c += 1
print(c)