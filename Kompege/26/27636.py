f = open("27636.txt")
carry_limit = int(f.readline().split()[0])
masses = sorted([int(l) for l in f])
f.close()

amount = 0
carried = 0
for mass in masses:
    if mass + carried > carry_limit:
        break
    carried += mass
    amount += 1


print(len(masses) - amount, sum(masses) - carried)
