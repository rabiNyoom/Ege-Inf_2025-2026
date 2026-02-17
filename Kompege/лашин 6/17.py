ns = [int(l) for l in open('17.txt')]
co = 0
m = 0
mini = min([n for n in ns if 1000 <= n <= 9999 and n % 100 == 30])
for a, b, c in zip(ns, ns[1:], ns[2:]):
    if (a+b+c) <= mini:
        continue
    if len([n for n in [a,b,c] if 1000 <= abs(n) <= 9999 and abs(n) % 2 == 0]) != 2:
        continue
    co += 1
    m = max(m, a+b+c)
print(co,m)