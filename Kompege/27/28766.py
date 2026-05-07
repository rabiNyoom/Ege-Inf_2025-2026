import re
from math import hypot


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def count_ygs(cl):
    return sum(1 for p in cl if re.match(r"^Z\d*I$", p[2]))


def yg_inner_dist(cl):
    ygs = [p for p in cl if re.match(r"^Z\d*I$", p[2])]
    min_dist = float("inf")
    for p in ygs:
        for p1 in ygs:
            d = dist(p, p1)
            if d != 0 and d < min_dist:
                min_dist = d
    return min_dist


def a():
    data = []
    for l in open("28766_A.txt"):
        x, y, s = l.replace(",", ".").split()
        data.append([float(x), float(y), s])
    red_giants = [p for p in data if re.match(r"^Y\d*III$", p[2])]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    mi_cen = centr(min(clus, key=len))
    red_dists = [dist(mi_cen, p) for p in red_giants]
    a1 = int(abs(min(red_dists) * 10000))
    a2 = int(abs(max(red_dists) * 10000))
    print(a1, a2)


def b():
    data = []
    for l in open("28766_B.txt"):
        x, y, s = l.replace(",", ".").split()
        data.append([float(x), float(y), s])
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)

    ygs_to_cl = [(count_ygs(cl), cl) for cl in clus]
    mi_cen = centr(min(ygs_to_cl)[1])
    ma_cen = centr(max(ygs_to_cl)[1])

    b1 = int(abs(min(yg_inner_dist(cl) for cl in clus) * 10000))
    b2 = int(abs(dist(mi_cen, ma_cen) * 10000))
    print(b1, b2)


a()
b()
