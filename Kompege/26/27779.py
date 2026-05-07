diams = [int(l) for l in open('27779.txt')]
diams.sort(reverse=True)

c = 1
curd = diams[0]
for di in diams:
    if curd - di >= 8:
        curd = di
        c += 1
print(c, curd)
