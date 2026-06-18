from itertools import combinations
from math import hypot
from re import fullmatch


def dist(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def dbscan(fname):
    data = []
    for l in open(fname):
        x, y, attr = l.replace(",", ".").split()
        data.append((float(x), float(y), attr))
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) <= 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    # print(*map(len, clus))
    return clus


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append((sm, p))
    return min(m)[1]


def b2_helper(cl):
    wsg = [p for p in cl if fullmatch(r"A\d*I", p[2])]
    return max(dist(p, p1) for p, p1 in combinations(wsg, 2))


#

clus_a = sorted(dbscan("27A_30475.txt"), key=len)

naib = clus_a[1]
cen_naib = centr(naib)
gol_c = [p for p in naib if fullmatch(r"O\d*V", p[2])]
dist_to_p = [(dist(p, cen_naib), p) for p in gol_c]

ax = int(abs(min(dist_to_p)[1][0] * 10000))
ay = int(abs(min(dist_to_p)[1][1] * 10000))
print(ax, ay)

#

clus_b = sorted(dbscan("27B_30475.txt"), key=len)
subg_to_cl = [
    (tuple(p for p in cl if fullmatch(r"\w\d*IV", p[2])), cl) for cl in clus_b
]
subg_to_cl.sort(key=lambda x: len(x[0]))
b1 = int(dist(centr(subg_to_cl[0][1]), centr(subg_to_cl[-1][1])) * 10000)
b2 = int(max(map(b2_helper, clus_b)) * 10000)
print(b1, b2)
