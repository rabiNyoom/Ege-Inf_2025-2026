from itertools import permutations

t = '14 15 25 27 35 36 41 47 51 52 53 56 63 65 72 74'
g = 'АБ БА АГ ГА БГ ГБ ВГ ГВ ГД ДГ ДК КД ВЕ ЕВ ЕК КЕ'

for p in permutations('АБВГДЕК'):
    tc = t
    for i in range(1, len(p)+1):
        tc = tc.replace(str(i), p[i-1])
    if set(tc.split()) == set(g.split()):
        print(*range(1, len(p)+1))
        print(*p)
        break

# 32
