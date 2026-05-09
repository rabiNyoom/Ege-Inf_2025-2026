def f(a, b):
    if a < b or a == 73:
        return 0
    if a == b:
        return 1
    return f(a - 3, b) + f(a - 8, b) + f(a // 2, b)


print(f(76, 41) * f(41, 12))
