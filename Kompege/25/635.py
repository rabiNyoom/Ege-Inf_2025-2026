with open('primes.txt') as f:
    primes = set(map(int, f.read().strip().split()))
low = int(106732567**0.25)+1
up = int(152673836**0.25)

for n in range(low, up+1):
    if n in primes:
        print(n**4, n**3)