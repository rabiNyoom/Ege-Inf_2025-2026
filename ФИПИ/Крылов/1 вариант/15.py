a = list(range(3, 61))
b = [d for d in range(2, 177) if 177 % d == 0]


def check_y(y):
    c = [d for d in range(2, y) if y % d == 0]
    if len(c) == 0:
        return False
    for x in range(1, 10000):
        if not ((x in c) <= (x in a and (x not in b))):
            return False
    return True


for y in range(10000, 0, -1):
    if check_y(y):
        print(y)
        break

# 2809
