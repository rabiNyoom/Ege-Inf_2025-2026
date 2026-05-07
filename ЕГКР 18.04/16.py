from functools import lru_cache
import threading
import sys

sys.setrecursionlimit(30000000)


def main():
    @lru_cache(None)
    def g(n):
        if n >= 22560:
            return n / 23 + 33
        else:
            return g(n+11) - 4

    @lru_cache(None)
    def f(n):
        if n >= 21:
            return f(n-8) + 1095
        else:
            return 10 * (g(n-7) - 36)

    for x in range(20, 500):
        print(f(x))


threading.stack_size(1 << 23)
threading.Thread(target=main).start()
