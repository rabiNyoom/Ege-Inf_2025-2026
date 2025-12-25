from sys import setrecursionlimit

setrecursionlimit(100000)

def f(n):
    return g(n-50000) + g(n+50000)
def g(n):
    if n <= 6:
        return 5**n
    else:
        return g(n-3) + 2
print(f(100000))

# 152076