count = 0

for l in open('9_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()
    
    if len(set(s)) == len(s) and 3 * (s[0] + s[-1]) <= 2 * sum(s[1:4]):
        count += 1

print(count)

# 853