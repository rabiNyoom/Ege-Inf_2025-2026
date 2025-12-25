c = 0
for l in open('9.txt'):
    s = sorted([int(i) for i in l.split()])
    repmin = [i for i in s if i == min(s)]
    norep = [i for i in s if s.count(i) == 1]
    if (len(repmin) == 2 and len(norep) == 6 or len(repmin) == 3 and len(norep) == 5) and min(norep)**2 + max(norep)**2 <= (sum(norep) - min(norep) - max(norep))**2:
        c += 1
print(c)

# 752