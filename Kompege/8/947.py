'''
ABCD -> 1234
и сравниваем числа
'''
from itertools import product
c = 0
for p in product([1, 2, 3, 4], repeat=4):
    if p[0] <= p[1] <= p[2] <= p[3]:
        c += 1
print(c)
