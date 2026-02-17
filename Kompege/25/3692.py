from fnmatch import fnmatch
for n in range(0, 10**9, 169):
    if fnmatch(str(n), '123*567?'):
        print(n, n // 169)
