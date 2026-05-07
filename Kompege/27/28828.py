from math import hypot
from re import fullmatch


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


ybgs = []


def dbscan(fname):
    data = []
    for l in open(fname):
        x, y, attr = l.replace(",", ".").split()
        p = [float(x), float(y), attr]
        data.append(p)
        if fullmatch(r"Z\d*II", p[2]):
            ybgs.append(p)
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


clus_a = sorted(dbscan("28828_A.txt"), key=len)
cen_max = centr(clus_a[1])
cen_min = centr(clus_a[0])

a1 = int(abs(min([dist(cen_max, ybg) for ybg in ybgs]) * 10000))
a2 = int(abs(max([dist(cen_min, ybg) for ybg in ybgs]) * 10000))
print(a1, a2)

clus_b = sorted(dbscan("28828_B.txt"), key=len)
bc_to_cl = sorted(
    [[sum(1 for p in cl if fullmatch(r"L\d*V", p[2])), cl] for cl in clus_b]
)

bcs = [p for p in clus_b[2] if fullmatch(r"L\d*V", p[2])]
total = 0
for i in range(len(bcs)):
    for j in range(i, len(bcs)):
        total += dist(bcs[i], bcs[j])
b1 = int(abs(total * 10000))
b2 = int(abs(dist(centr(bc_to_cl[0][1]), centr(bc_to_cl[1][1])) * 10000))
print(b1, b2)
