def f(x, y, ff):
    if x == 14 or x == 18:
        ff = True
    if x > y:
        return 0
    if x == y and ff:
        return 1
    if x == y:
        return 0
    return f(x+1,y,ff) + f(x*2,y,ff) + f(x*3, y,ff)
print(f(6, 48, False))

# 69