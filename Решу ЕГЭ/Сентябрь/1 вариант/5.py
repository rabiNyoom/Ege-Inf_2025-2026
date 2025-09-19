def algo(n):
    nbin = bin(n)[2:]

    if n % 2 == 0:
        nbin = '1' + nbin + '0'
    else:
        nbin = '11' + nbin + '11'

    return int(nbin, 2)

for i in range(1, 1_000):
    if algo(i) > 52:
        print(i)
        break

# 3