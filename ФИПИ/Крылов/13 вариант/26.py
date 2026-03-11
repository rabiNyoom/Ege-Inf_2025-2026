ns = [int(n) for n in open('26.txt')]
ns.sort(reverse=True)

c = 1
last = ns[0]
for n in ns[1:]:
    if last - n >= 7:
        last = n
        c += 1


print(c, last)

# 1196 2
