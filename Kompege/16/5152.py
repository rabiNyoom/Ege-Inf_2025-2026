from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n == 1:
            return 2
        return 2 * f(n-1)
    print(f(1900) / 2**1890)


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
