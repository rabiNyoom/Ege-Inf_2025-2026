from functools import lru_cache
from sys import setrecursionlimit
import threading


def main():
    @lru_cache(None)
    def f(n):
        if n == 1:
            return 1
        return (2*n-1) * f(n-1)
    print(f(3516)/f(3513))


setrecursionlimit(300000)
threading.stack_size(32 * 1024 * 1024)
threading.Thread(target=main).start()
