from itertools import product
last = 0
for i, v in enumerate(product('АЕЛПРЬ', repeat=5), 1):
    if i % 2 == 0 and v[0] not in 'РЬ' and v.count('Л') >= 2:
        last = i
print(last)