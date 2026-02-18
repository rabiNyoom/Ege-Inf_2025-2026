from fnmatch import fnmatch

for n in range(0, 10**9+1, 17):
    if fnmatch(str(n), '12345?6?8'):
        print(n, n//17)
    if n > 200000000:
        break
