c = 0

for l in open('82E1FA.txt'):
    s = sorted([int(i) for i in l.split()])

    if s[3] < sum(s) - s[3] and s[0] + s[1] == s[2] + s[3] or s[0] + s[2] == s[1] + s[3] or s[0] + s[3] == s[1] + s[2]:
        c += 1

print(c)

# 116