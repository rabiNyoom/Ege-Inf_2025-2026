d = '0123456789'
for a in d:
    for b in d:
        n = int(f'12345{a}6{b}8')
        if n % 17 == 0:
            print(n, n//17)
