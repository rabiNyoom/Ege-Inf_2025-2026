def check_a(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not ((x + y <= 30) or (y <= (x + 2)) or (y >= a)):
                return False
    return True

for a in range(1000, 0, -1):
    if check_a(a):
        print(a)
        break

# 17