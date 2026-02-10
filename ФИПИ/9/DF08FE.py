c = 0

for l in open('DF08FE.txt'):
    s = sorted([int(i) for i in l.split()])

    if len(s) == len(set(s)) and 2 * (s[0] + s[4]) <= s[1] + s[2] + s[3]:
        c += 1

print(c)

# 607