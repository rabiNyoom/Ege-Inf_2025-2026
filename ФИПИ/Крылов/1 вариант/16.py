from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(300000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return 3 * f(n-1) - n


print((f(2025) - f(2023) - 1) / 3**2022)

# 6
