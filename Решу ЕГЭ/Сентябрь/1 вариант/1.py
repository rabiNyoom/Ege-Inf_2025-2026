from itertools import *

t = '16 17 23 24 26 32 34 42 43 45 54 57 61 62 67 71 75 76'
g = 'АГ ГА ГД ДГ ДЖ ЖД ЕЖ ЖЕ ВЕ ЕВ БВ ВБ АБ БА АВ ВА ДЕ ЕД'

print(*range(1, 8))

for p in permutations('АБВГДЕЖ'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*p)

# 26