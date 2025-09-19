c = 0

for l in open('40F07C.txt'):
    s = sorted([int(i) for i in l.split()])

    rep3 = [i for i in s if s.count(i) == 3]
    rep1 = [i for i in s if s.count(i) == 1]

    if len(rep3) == 3 and len(rep1) == 3 and 3 * (rep3[0]**2) > rep1[0]**2 + rep1[1]**2 + rep1[2]**2:
        c += 1

print(c)

# 245