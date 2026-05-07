from itertools import product
ans = 0
for i, p in enumerate(product('ВИЛМОС', repeat=5), 1):
    if i % 2 == 0:
        continue
    if p[0] not in 'ОС' and p.count('В') == 1 and p.count('С') <= 1:
        ans = i
print(ans)
