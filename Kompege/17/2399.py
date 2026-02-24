ns = [int(i) for i in open('2399.txt')]
summ = []
for n in ns:
    if n % 35 == 0:
        summ.extend(list(map(int, list(str(n)))))

summa = sum(summ)
c = 0
m = float('inf')
for a, b in zip(ns, ns[1:]):
    if (a > summa and b <= summa and hex(b).endswith('ef')) or (b > summa and a <= summa and hex(a).endswith('ef')):
        c += 1
        m = min(m, a + b)
print(c, m)
