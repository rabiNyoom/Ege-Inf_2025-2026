from sys import setrecursionlimit

setrecursionlimit(100000)

def g(n):
    if n < 100:
        return n
    else:
        return f(n-3) + 1
def f(n):
    return g(n-2)
print(f(5000))

# 1078