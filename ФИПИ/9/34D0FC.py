c = 0

for l in open('34D0FC_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()

    n = s[3] + s[4]
    if len(s) == len(set(s)) and n <= sum(s) - n:
        c += 1

print(c)

# 1922