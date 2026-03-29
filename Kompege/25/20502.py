from re import compile

regex = compile("20[13579]{2}22[02468]*")

c = 0
for n in range(0, 10**10, 10980):
    if regex.match(str(n)):
        print(n, n//10980)
        c += 1
        if c == 5:
            break
