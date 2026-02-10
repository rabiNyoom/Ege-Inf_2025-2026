def algo(n):
    nb = list(f'{n:b}')
    ones = nb[1:len(nb)+1:2].count('1')
    zeros = nb[0:len(nb)+1:2].count('0')

    return abs(ones-zeros)


n = 0
while (r := algo(n)) != 5:
    n += 1
print(n)
