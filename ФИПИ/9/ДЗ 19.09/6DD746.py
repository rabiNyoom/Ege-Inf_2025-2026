c = 0

for l in open('6DD746.txt'):
    s = sorted([int(i) for i in l.split()])

    rep3 = [i for i in s if s.count(i) == 3]
    rep1 = [i for i in s if s.count(i) == 1]

    if len(rep3) == 3 and len(rep1) == 3 and sum(rep3) ** 2 > sum(rep1) ** 2:
        c += 1

print(c)

# 273