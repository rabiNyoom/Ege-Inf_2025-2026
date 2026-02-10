from itertools import *
def f(x,y,z,w):
    return ((x <= y) and (y <= z) and (z <= w))
print('x y z w F')
for a1,a2,a3,a4 in product([0,1], repeat=4):
    if f(a1,a2,a3,a4):
        print(a1,a2,a3,a4,1)
# zywx