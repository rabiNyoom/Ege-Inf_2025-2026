from re import compile

regex = compile(r'\w+@\w+\.\w+')
s = open('19969.txt').read().strip()
found = regex.findall(s)
print(max(map(len, found)))
