from itertools import *
t = '12 14 17 21 24 28 35 37 38 41 42 46 53 58 64 67 71 73 76 82 83 85'
g = 'AB BA AE EA EC CE DC CD DF FD HF FH BH HB AH HA EG GE GC CG GF FG'
print(*range(1, 8+1))
for p in permutations('ABCDEFGH'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*p)
# 38