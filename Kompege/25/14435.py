from re import compile
r = compile('^71[13579]{3}39.28$')
for n in range(0, 10**10, 2024):
    if r.match(str(n)):
        print(n, n//2024)
