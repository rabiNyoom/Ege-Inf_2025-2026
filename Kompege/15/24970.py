def get_c(n):
    return [d for d in range(2, n) if n % d == 0]

def check_y(y, de):
    C = de
    for x in range(1, 1000):
        if not ((not (4 <= x <= 82)) <= (not(x in C))):
            return False
    return True

maxd = 0
yy = 0
for y in range(1, 10000):
    de = get_c(y)
    if not de:
        continue
    if check_y(y, de):
        if len(de) > maxd:
            maxd = len(de)
            yy = y
print(yy)

# 385