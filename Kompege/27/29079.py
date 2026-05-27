from math import hypot
from re import fullmatch


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def dbscan(fname):
    data = []
    for l in open(fname):
        x, y, spec = l.replace(",", ".").split()
        p = (float(x), float(y), spec)
        data.append(p)
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


clus = dbscan("29079_A.txt")
c1, c2 = centr(clus[0]), centr(clus[1])
osg1, osg2 = [[p for p in cl if fullmatch(r"N\d*IV", p[2])] for cl in clus]
dists = []
for p in osg2:
    dists.append(dist(c1, p))
for p in osg1:
    dists.append(dist(c2, p))
a1 = int(min(dists) * 10000)
a2 = int(max(dists) * 10000)
print(a1, a2)

#

clus = sorted(dbscan("29079_B.txt"), key=len)
zqb1, zqb2 = [[p for p in cl if fullmatch(r"J\d*V", p[2])] for cl in (clus[2], clus[0])]
b1 = int(abs(max(p[0] for p in zqb1) * 10000))
b2 = int(abs(max(p[1] for p in zqb2) * 10000))
print(b1, b2)
