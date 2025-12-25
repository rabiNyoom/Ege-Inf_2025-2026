c = 0
for l in open('8E4395_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()
    
    if (s[0] + s[4])**2 > s[1]**2 + s[2]**2 + s[3]**2:
        c += 1
print(c)

# 2585