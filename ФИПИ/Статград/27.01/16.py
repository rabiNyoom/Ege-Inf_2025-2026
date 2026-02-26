from functools import lru_cache
import sys

sys.setrecursionlimit(1 << 30)


@lru_cache(None)
def f(n):
    if n >= 20:
        return f(n-4) + 4620
    return 8 * (g(n-12) - 21)


@lru_cache(None)
def g(n):
    if n >= 384242:
        return n / 4 + 18
    return 12 + g(n + 41)


print(f(913))

# 2703082
