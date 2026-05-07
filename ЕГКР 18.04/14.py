from string import printable
for x in printable[:23]:
    n = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if n % 22 == 0:
        print(n // 22)
        break
