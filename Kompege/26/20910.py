with open("20910.txt") as f:
    n, rows, sits_per_row = map(int, f.readline().split())
    sits = [list(map(int, l.split())) for l in f]
    matrix = [[True] * sits_per_row for _ in range(rows)]

for row, sit in sits:
    matrix[row - 1][sit - 1] = False


def check_pair(i):
    c = 0
    for row in matrix:
        sit1 = row[i]
        sit2 = row[i + 1]
        if sit1 and sit2:
            c += 1
        else:
            return c


maxrow, minsit = 0, 0
for i in range(0, len(matrix[0]) - 1):
    r = check_pair(i)
    if r > maxrow:
        maxrow = r
        minsit = i + 1
print(maxrow, minsit)
