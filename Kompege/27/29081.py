from math import hypot
from re import match


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def brights(cl):
    return [p for p in cl if p[2][1] in "89"]


def dbscan(fname: str) -> list:
    data = []
    for l in open(fname):
        x, y, spec = l.replace(",", ".").split()
        point = (float(x), float(y), spec)
        data.append(point)
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


clus = dbscan("29081_A.txt")
c1, c2 = centr(clus[0]), centr(clus[1])
dists = []
for p in clus[0]:
    if p[2] != "VII":
        continue
    d = dist(c1, p)
    if d:
        dists.append(d)
for p in clus[1]:
    if p[2] != "VII":
        continue
    d = dist(c2, p)
    if d:
        dists.append(d)
a1 = int(abs(min(dists) * 10000))
a2 = int(abs(max(dists) * 10000))
print(a1, a2)

#

clus = dbscan("29081_B.txt")
br1, br2, br3 = [brights(cl) for cl in clus]
mi = min(
    dist(p, p1) for x, y in [(br1, br2), (br2, br3), (br1, br3)] for p in x for p1 in y
)
b1 = int(abs(mi * 10000))
dists = [
    dist(cl[i], cl[j])
    for cl in (br1, br2, br3)
    for i in range(len(cl))
    for j in range(i + 1, len(cl))
]
b2 = int(sum(dists) / len(dists) * 10000)
print(b1, b2)
