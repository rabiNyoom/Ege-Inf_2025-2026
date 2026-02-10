c = 0

for l in open('AAAD85.txt'):
    s = sorted([int(i) for i in l.split()])

    rep3 = [i for i in s if s.count(i) == 3]
    rep2 = [i for i in s if s.count(i) == 1]

    if len(rep3) == 3 and len(rep2) == 4 and rep3[0] <= sum(rep2) / 4:
        c += 1

print(c)

# 34