from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n <= 3:
            return n
        if n % 2 == 1:
            return 2 * n + f(n-2)
        return n*n + f(n-1)
    print(f(10000) - f(9995))


setrecursionlimit(300000)
threading.stack_size(1 << 24)
threading.Thread(target=main).start()
