c = 0

for l in open('DF08FE_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()

    n = min(s) + max(s)
    if len(s) == len(set(s)) and 2 * n <= sum(s) - n:
        c += 1

print(c)

# 607