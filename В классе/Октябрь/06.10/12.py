def algo(n):
    while '18' in n or '388' in n or '888' in n:
        if '18' in n:
            n = n.replace('18', '8', 1)
        if '388' in n:
            n = n.replace('388', '81', 1)
        if '888' in n:
            n = n.replace('888', '3', 1)
    return n
for n in range(4, 9999+1):
    p = '1' + '8' * n
    if algo(p).count('1') == 3:
        print(n)
        break
# 33