def algo(n):
    s = str(n)
    a = sum(map(int, s[1:len(s)+1:2]))
    b = sum(map(int, filter(lambda x: int(x) % 2 == 0, s)))
    return abs(a-b)


n = 2
while (r := algo(n)) != 13:
    n += 1
print(n)
