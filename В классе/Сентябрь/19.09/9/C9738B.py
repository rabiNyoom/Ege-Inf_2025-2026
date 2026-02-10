c = 0
for l in open('C9738B_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()
    
    if s[2]**2 > 2 * (s[0] * s[1]):
        c += 1
print(c)
# 2715