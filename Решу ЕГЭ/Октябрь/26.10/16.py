from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    if n <= 10:
        return n
    else:
        return n - 12 + f(n-21)
print((f(224356) - f(224272)) / f(59))

# 12125