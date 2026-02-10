c = 0
for l in open('AAAD85_in.txt'):
    s = [int(i) for i in l.split()]
    s.sort()
    
    rep1 = [i for i in s if s.count(i) == 3]
    rep2 = [i for i in s if s.count(i) == 1]
    
    if len(rep1) == 3 and len(rep2) == 4 and rep1[0] <= sum(rep2) / 4:
        c += 1
print(c)

# 34