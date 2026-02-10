ns = [int(i) for i in open('2399.txt')]
summa = []
for n in ns:
    if n % 35 == 0:
        summa.extend(list(map(int, list(str(n)))))

summa = sum(summa)
c = 0
m = float('inf')
for a, b in zip(ns, ns[1:]):
    if (a > summa and b <= summa and hex(b).endswith('EF')) or (b > summa and a <= summa and hex(a).endswith('EF')):
        c += 1
        m = min(m, a + b)
print(c, m)
