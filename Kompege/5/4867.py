def algo(n):
    s = str(n)
    a = sum(map(int, filter(lambda x: int(x) % 2 == 0, s)))
    b = sum(map(int, s[1:len(s)+1:2]))
    return abs(a-b)


n = 2
while (r := algo(n)) != 9:
    n += 1
print(n)
