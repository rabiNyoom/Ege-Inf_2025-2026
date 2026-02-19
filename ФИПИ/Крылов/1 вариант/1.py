from itertools import permutations
t = '12 13 14 17 21 26 31 35 38 41 45 47 53 54 58 62 67 68 71 74 76 83 85 86'
g = 'AB BA BE EB EH HE HC CH CA AC CF FC FD DF AD DA DB BD DG GD GE EG GH HG'

for p in permutations('ABCDEFGH'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*range(1, len(p)+1))
        print(*p)

# 14
