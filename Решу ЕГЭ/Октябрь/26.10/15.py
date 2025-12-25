m = 0
for A in range(1, 300):
    flag = True
    for x in range(1, 1000+1):
        for y in range(1, 1000+1):
            if not ((y > A) or (152 != 2 * y + 3 * x) or (A < x)):
                flag = False
    if flag and m < A:
        m = A

print(m)

# 30