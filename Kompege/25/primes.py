n = 10_000_000

a = [True] * (n+1)
a[0] = False
a[1] = False
for i in range(2, n+1):
    if a[i]:
        for j in range(i*i, n+1, i):
            a[j] = False
prim = [str(d) for d in range(2, n+1) if a[d]]
with open('primes.txt', 'w') as f:
    f.write(' '.join(prim))
