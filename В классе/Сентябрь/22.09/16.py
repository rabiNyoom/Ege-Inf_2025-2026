import sys

sys.setrecursionlimit(100000)

def f(n):
    if n < 7:
        return 7
    if n >= 7 and n % 3 != 0:
        return 5 - f(n-1)
    if n >= 7 and n % 3 == 0:
        return 3 + f(n-1)
print(f(3015))

# 3016