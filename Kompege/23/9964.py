def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(a*3, b) + f(a+5, b)

print(f(3, 8) * f(8, 24) * f(24, 26) * f(26, 69))