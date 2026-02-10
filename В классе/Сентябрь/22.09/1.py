from itertools import *

t = '13 14 17 23 24 25 26 31 32 34 35 41 42 43 47 52 53 56 62 65 71 74'
g = 'AB BA BC CB AC CA AD DA CD DC CE EC DE ED DF FD FG GF FE EF EG GE'
print(*range(1, 8))
for p in permutations('ABCDEFG'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*p)

# 24