with open("20910.txt") as f:
    n, rows, sits = map(int, f.readline().split())
    taken = [list(map(int, l.split())) for l in f]

matrix = [[True] * sits for _ in range(rows)]
for row, sit in taken:
    matrix[row - 1][sit - 1] = False


def check_pair(sit):
    c = 0
    for row in matrix:
        sit1 = row[sit]
        sit2 = row[sit + 1]
        if sit1 and sit2:
            c += 1
        else:
            return c


maxrow, minsit = 0, 0
for sit in range(sits - 1):
    r = check_pair(sit)
    if r > maxrow:
        maxrow = r
        minsit = sit + 1
print(maxrow, minsit)
