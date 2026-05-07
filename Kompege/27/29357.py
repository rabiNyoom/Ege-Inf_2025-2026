from math import hypot
from re import fullmatch


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def dbscan(fname):
    data = []
    for l in open(fname):
        x, y, attr = l.replace(",", ".").split()
        p = [float(x), float(y), attr]
        data.append(p)
        if fullmatch(r"M\d*III", p[2]):
            red_giants.append(p)
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    # print(*map(len, clus))
    return clus


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def max_yc_dist(cl):
    m = 0
    ycs = [p for p in cl if fullmatch(r"G\d*V", p[2])]
    for p in ycs:
        for p1 in ycs:
            d = dist(p, p1)
            m = max(m, d)
    return m


red_giants = []

clus_a = sorted(dbscan("29357_A.txt"), key=len)
centr_min = centr(clus_a[0])
minn = min(red_giants, key=lambda x: dist(centr_min, x))
ax = int(abs(minn[0] * 10000))
ay = int(abs(minn[1] * 10000))
print(ax, ay)

clus_b = sorted(dbscan("29357_B.txt"), key=len)
og_to_cl = [[sum(1 for p in cl if fullmatch(r"K\d*III", p[2])), cl] for cl in clus_b]
b1 = int(abs(dist(centr(min(og_to_cl)[1]), centr(max(og_to_cl)[1])) * 10000))
b2 = int(abs(max(max_yc_dist(cl) for cl in clus_b) * 10000))
print(b1, b2)
