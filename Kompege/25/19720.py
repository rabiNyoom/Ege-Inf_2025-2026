from re import compile
r = compile('^1[13579]*2[24680]3[13579]*45$')
for n in range(0, 10**8, 153):
    if r.match(str(n)):
        print(n, n//153)
