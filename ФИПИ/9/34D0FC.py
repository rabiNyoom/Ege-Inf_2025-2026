c = 0

for l in open('34D0FC.txt'):
    s = sorted([int(i) for i in l.split()])

    n = s[3] + s[4]
    if len(s) == len(set(s)) and s[3] + s[4] <= s[0] + s[1] + s[2]:
        c += 1

print(c)

# 1922