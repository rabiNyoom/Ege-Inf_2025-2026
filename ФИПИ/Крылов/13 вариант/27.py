from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def md(cl):
    c = centroid(cl)
    mid = 0
    for p in cl:
        d = dist(c, p)
        if d != 0:
            mid = max(mid, d)
    return mid


def a():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27A.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    clusters = [cl for cl in clusters if len(cl) > 1]
    centroids = [centroid(cl) for cl in clusters]

    px = int(abs(max(x for x, y in centroids) * 10000))
    py = int(abs(max(y for x, y in centroids) * 10000))
    print(px, py)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    clusters = [cl for cl in clusters if len(cl) > 1]
    clusters.sort(key=len)
    mids = [md(cl) for cl in clusters]

    q1 = int(dist(centroid(clusters[0]), centroid(clusters[2])) * 10000)
    q2 = int(max(mids) * 10000)

    print(q1, q2)


a()
b()
