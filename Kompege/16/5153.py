from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n < 4:
            return 1
        if n % 2 == 1:
            return n
        return f(n-1) + f(n-2) + f(n-3)

    print(f(2254) - f(2252))


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
