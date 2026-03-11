def DEL(a, b):
    return a % b == 0


def check(a):
    for x in range(1, 5000):
        if not ((DEL(x, 13) <= (not DEL(x, 21))) or (x + a >= 500)):
            return False
    return True


for a in range(1, 1000):
    if check(a):
        print(a)
        break

# 227
