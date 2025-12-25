from itertools import product
c = 0
for n in product('0123456789ABCDE', repeat=4):
    if n[0] != '0' and n.count('8') == 1 and n[0] != n[1] and n[1] != n[2] and n[2] != n[3]:
        c += 1
print(c)

# 9295