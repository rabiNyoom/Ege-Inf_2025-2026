from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(1000000)


@lru_cache(None)
def f(n):
    if n == 1:
        return 15
    return 2 * f(n-1) - n


print((f(2025) - f(2023) - 2) // 2**2022)
