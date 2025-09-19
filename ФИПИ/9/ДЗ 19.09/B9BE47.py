c = 0

for l in open('B9BE47.txt'):
    s = sorted([int(i) for i in l.split()])

    if (s[4] + s[0])**2 > s[1]**2 + s[2]**2 + s[3]**2:
        c += 1

print(c)

# 2623