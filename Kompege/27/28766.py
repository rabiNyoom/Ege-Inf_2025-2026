import re
from math import hypot


def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def count_yg(cl):
    return sum(1 for p in cl if re.match(r'^Z\d*I$', p[2]))


def min_yg_d(cl):
    ygs = [p for p in cl if re.match(r'^Z\d*I$', p[2])]
    md = set()
    for p in ygs:
        for p1 in ygs:
            md.add(dist(p, p1))
    md.remove(0)
    if len(md) == 0:
        return float('inf')
    return min(md)


def a():
    red_giants = []
    data = []
    for l in open('28766_A.txt'):
        l = l.replace(',', '.')
        x, y, s = l.split()
        point = [float(x), float(y), s]
        data.append(point)
        if re.match(r'^Y\d*III$', s):
            red_giants.append(point)
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    centrmin = centr(min(clus, key=len))
    rg_dists = [dist(centrmin, p) for p in red_giants]
    a1 = int(abs(min(rg_dists) * 10000))
    a2 = int(abs(max(rg_dists) * 10000))
    print(a1, a2)


def b():
    data = []
    for l in open('28766_B.txt'):
        l = l.replace(',', '.')
        x, y, s = l.split()
        point = [float(x), float(y), s]
        data.append(point)
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    clus_to_yg = [(count_yg(cl), cl) for cl in clus]
    b1 = int(abs(min(min_yg_d(cl) for cl in clus)) * 10000)
    b2 = int(
        abs(dist(centr(min(clus_to_yg)[1]), centr(max(clus_to_yg)[1]))) * 10000)
    print(b1, b2)


a()
b()
