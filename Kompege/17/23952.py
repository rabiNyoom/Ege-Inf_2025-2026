ns = [int(n) for n in open('23952.txt')]
maxi = max([n for n in ns if str(n).endswith('93')])
c = m = 0

for i in range(1, len(ns)):
    a, b = ns[i-1:i+1]
    if len([x for x in [a,b] if x > maxi]) != 1:
        continue
    if len([x for x in [a,b] if str(abs(x)).startswith('9')]) == 0:
        continue
    c += 1
    m += sum([x for x in [a,b] if x > maxi])
print(c,m)