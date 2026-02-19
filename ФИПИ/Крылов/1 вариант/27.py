from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def distss(cl1, cl2) -> list[float]:
    centr = centroid(cl1)
    m = []
    for p in cl2:
        d = dist(centr, p)
        if d != 0:
            m.append(d)
    return m


def a():
    data = [list(map(float, l.split())) for l in open('27_A.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    # print('Clusters:', *map(len, clusters))

    dists = distss(clusters[0], clusters[1]) + distss(clusters[1], clusters[0])
    p1 = int(abs(min(dists) * 10000))
    p2 = int(abs(max(dists) * 10000))
    print(p1, p2)


def b():
    data = [list(map(float, l.split())) for l in open('27_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    clusters.sort(key=len)
    dists1 = distss(clusters[0], clusters[0])
    dists2 = distss(clusters[2], clusters[2])

    q1 = int(abs(sum(dists1) / len(dists1) * 10000))
    q2 = int(abs(sum(dists2) / len(dists2) * 10000))
    print(q1, q2)


a()
b()
