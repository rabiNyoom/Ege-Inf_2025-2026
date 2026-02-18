from itertools import product
c = 0
for p in product('01234567', repeat=5):
    if p[0] == '0':
        continue
    if p.count('1') != 0:
        continue
    if len(set(p)) != len(p):
        continue
    s = ''.join(['eo'[int(ch) % 2] for ch in p])
    if 'ee' in s or 'oo' in s:
        continue
    c += 1
print(c)
