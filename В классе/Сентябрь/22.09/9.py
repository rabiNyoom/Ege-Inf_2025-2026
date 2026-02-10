sum_ = 0
for l in open('9.txt'):
    s = sorted(map(int, l.split()))
    rep2 = [i for i in s if s.count(i) == 2]
    rep1 = [i for i in s if s.count(i) == 1]
    if len(rep1) == 2 and len(rep2) == 4 and rep1 + rep2 < sum(s) - rep2 - rep1:
        sum_ = sum(s)
print(sum_)