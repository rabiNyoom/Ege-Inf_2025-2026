f = open('27636.txt')
s = int(f.readline().split()[0])
masses = sorted([int(l) for l in f])
f.close()

a = 0
u = 0
for v in masses:
    if v + u <= s:
        u += v
        a += 1
    else:
        break

print(len(masses)-a, sum(masses)-u)
