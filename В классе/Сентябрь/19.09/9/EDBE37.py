c = 0
for l in open('EDBE37_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()
    
    if s[3] < sum(s) - s[3] and (s[0] + s[1] == s[2] + s[3] or s[0] + s[2] == s[1] + s[3] or s[0] + s[3] == s[1] + s[2]):
        c += 1
print(c)

# 118