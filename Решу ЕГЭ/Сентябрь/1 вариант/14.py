n = 125 + 25 ** 3 + 5 ** 9
s = ''

while n != 0:
    s += str(n % 5)

    n //= 5

print(s.count('0'))

# 7