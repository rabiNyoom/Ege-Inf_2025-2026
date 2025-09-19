c = 0

for l in open('90D64F.txt'):
    s = sorted([int(i) for i in l.split()])

    rep2 = [i for i in s if s.count(i) == 2]
    rep1 = [i for i in s if s.count(i) == 1]

    if len(rep2) == 4 and len(rep1) == 3 and sum(rep2) / 4 < sum(rep1) / 3:
        c += 1

print(c)

# 96