c = 0

for l in open('B42173.txt'):
    s = sorted([int(i) for i in l.split()])
    
    if (s[0] + s[4])**2 > s[1]**2 + s[2]**2 + s[3]**2:
        c += 1

print(c)

# 2640