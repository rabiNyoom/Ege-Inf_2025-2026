from math import ceil
def f(a,b):
    if a > b or a == 36:
        return 0
    if a == b:
        return 1
    return f(a+2,b) + f(a+5,b) + f(ceil(a*2.5), b)

print(f(5, 53) * f(53, 122))