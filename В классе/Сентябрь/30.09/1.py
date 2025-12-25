from itertools import *
t = '12 14 16 21 23 24 25 32 35 41 42 46 47 52 53 57 61 64 67 74 75 76'
g = 'АВ ВА ВЕ ЕВ ЕК КЕ КД ДК ДБ БД АБ БА ВГ ГВ ГД ДГ АГ ГА БГ ГБ ДЕ ЕД'
print(*range(1,8))
for p in permutations('АБВГДЕК'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*p)
# 36