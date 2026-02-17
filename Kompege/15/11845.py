def check_a(a):
    for x in range(1, 50000):
        if not(((a % x) == 0) <= (x == a) or (x == 1)):
            return False
    return True

c = 0
for a in range(1, 11112):
    if check_a(a):
        c += 1
print(c)

# 1346