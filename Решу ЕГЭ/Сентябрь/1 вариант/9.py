c = 0

for l in open('9.txt'):
    s = sorted([int(i) for i in l.split()])

    if len(set(s)) == len(s) and 3 * (s[0] + s[-1]) <= 2 * sum(s[1:4]):
        c += 1

print(c)

# 853