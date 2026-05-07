from math import dist


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27_A_28946.txt')]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)

    max_cl = max(clus, key=len)
    min_cl = min(clus, key=len)
    cen_max = centr(max_cl)
    cen_min = centr(min_cl)
    a1 = sum(1 for p in max_cl if p[1] < cen_max[1])
    a2 = int(abs((cen_max[0] - cen_min[0]) * 10000))
    print(a1, a2)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27_B_28946.txt')]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)

    clus.sort(key=len)
    min_cl = clus[0]
    min_cen = centr(min_cl)
    b1 = sum(1 for p in min_cl if abs(
        p[0] - min_cen[0]) < 0.9 and abs(
        p[1] - min_cen[1]) < 0.9)
    c1, c2 = centr(clus[1]), centr(clus[2])
    b2 = int(abs((c1[1] - c2[1]) * 10000))
    print(b1, b2)


a()
b()
