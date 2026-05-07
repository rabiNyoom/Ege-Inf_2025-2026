from math import dist


def dbscan(filename):
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open(filename)]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    return clus


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    clus = dbscan('27780_A.txt')
    clus.sort(key=len)

    centrs = [centr(cl) for cl in clus]

    a1 = len(clus[-1])
    a2 = int(abs(sum(dist(c, [1.0, 1.5]) for c in centrs) * 10000))
    print(a1, a2)


def b():
    clus = dbscan('27780_B.txt')
    clus.sort(key=len)

    cen_b = centr(clus[2])
    cen_m = centr(clus[1])

    b1 = sum(1 for p in clus[1] if dist(p, cen_m) <= 1.2) - 1
    b2_dists = set(dist(p, cen_b) for p in clus[2])
    b2_dists.remove(0)
    b2 = int(abs(min(b2_dists) * 10000))
    print(b1, b2)


a()
b()
