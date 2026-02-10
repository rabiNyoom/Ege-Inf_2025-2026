def sumdiv(n):
    return sum(d for d in range(1, n+1) if n % d == 0)

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return f(a+1, b) + f(sumdiv(a), b)

print(f(2, 24))

# 1912