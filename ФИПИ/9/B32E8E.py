c = 0

for l in open('B32E8E.txt'):
    s = sorted([int(i) for i in l.split()])

    if s[3] < sum(s) - s[3] and len(s) == len(set(s)):
        c += 1

print(c)

# 2322