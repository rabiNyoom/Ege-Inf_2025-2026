from itertools import product
for a, b, c in product(range(10), repeat=3):
    n = int(f'12{a}345{b}67089{c}')
    if n % 206 == 0:
        print(n, n//206)
