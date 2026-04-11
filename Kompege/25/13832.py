from re import compile
r = compile('^[02468][13579][02468]{2}[13579][02468][13579]77$')
for n in range(0, 10**9, 7777):
    if r.match(str(n)):
        print(n, n//7777)
