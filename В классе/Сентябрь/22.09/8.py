def to9(n):
    b = []
    while n != 0:
        b.append(str(n % 9))
        n //= 9
    b.reverse()
    
    return ''.join(b)
c = 0
for i in range(1000000, 10000000):
    n = to9(i)
    if n[0] in ['2', '4', '6', '8'] and n[-1] in ['1', '2', '4', '5', '7', '8'] and '6' in n:
        c += 1
print(c)

# 959490