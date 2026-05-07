from re import fullmatch

for n in range(0, 10**10, 9874):
    if fullmatch(r"89.*6.7.9.", str(n)):
        print(n, n // 9874)
