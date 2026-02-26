def f(a, b, fl=False):
    if a > b or a in [17, 28]:
        return 0
    if a == b and fl:
        return 1
    if a in [14, 18]:
        fl = True
    return f(a+2, b, fl) + f(a+3, b, fl) + f(a*2, b, fl)


print(f(8, 48))

# 10800
