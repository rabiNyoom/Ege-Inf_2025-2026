a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for x in range(21):
    n = a[x]
    r = int(f'2496{n}2', 21) + \
        int(f'8{n}223', 21) + int(f'2331768{n}3', 21)
    if r % 20 == 0:
        print(r // 20)
        break

# 4066120204
