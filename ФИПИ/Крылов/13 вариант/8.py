from itertools import product
c = 0
for p in product('01234567', repeat=5):
    if p[0] == '0':
        continue
    s = ''.join(p)
    if s.count('4') != 2:
        continue
    s = s.replace('1', '*').replace('3', '*').replace('5',
                                                      '*').replace('7', '*').replace('9', '*')
    if '*4' not in s and '4*' not in s:
        c += 1
print(c)

# 612
