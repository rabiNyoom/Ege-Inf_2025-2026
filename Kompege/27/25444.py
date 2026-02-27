from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def minmaxd(cl0, cl):
    d = []
    c = centroid(cl0)
    for p in cl:
        di = dist(p, c)
        d.append(di)
    return min(d), max(d)


def a():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('25444_A.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:',  *map(len, clusters))
    clusters = [cl for cl in clusters if len(cl) > 1]

    dists = [*minmaxd(clusters[0], clusters[1]),
             *minmaxd(clusters[1], clusters[0])]

    p1 = int(min(dists) * 10000)
    p2 = int(max(dists) * 10000)

    print(p1, p2)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('25444_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 0.2]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:',  *map(len, clusters))
    clusters = [cl for cl in clusters if len(cl) > 1]
    centroids = [centroid(cl) for cl in clusters]
    dists = [dist(centroids[0], centroids[1]), dist(
        centroids[0], centroids[2]), dist(centroids[1], centroids[2])]

    q1 = int(min(dists) * 10000)
    q2 = int(max(dists) * 10000)

    print(q1, q2)


a()
b()

# 59674 83769
# 5651 9761
