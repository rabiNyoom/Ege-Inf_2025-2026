c = 0

for l in open('9EF0FE.txt'):
    s = sorted([int(i) for i in l.split()])

    if len(s) == len(set(s)) and 3 * s[0] * s[4] <= 2 * s[1] * s[2] * s[3]:
        c += 1

print(c)

# 9829