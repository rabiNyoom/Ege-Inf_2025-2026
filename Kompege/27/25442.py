from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def maxd(cl):
    c = centroid(cl)
    d = []
    for p in cl:
        di = dist(p, c)
        if di != 0:
            d.append(di)
    return max(d)


def a():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('25442_A.txt')]
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
    centroids = [centroid(cl) for cl in clusters]

    p1 = int(dist(centroids[0], centroids[1]) * 10000)
    p2 = int(max(maxd(cl) for cl in clusters) * 10000)

    print(p1, p2)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('25442_B.txt')]
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
    centroids = [centroid(cl) for cl in clusters]
    dists = [dist(centroids[0], centroids[1]), dist(
        centroids[0], centroids[2]), dist(centroids[1], centroids[2])]
    q1 = int(min(dists) * 10000)
    q2 = int(max(dists) * 10000)

    print(q1, q2)


a()
b()

# 69301 21668
# 70628 149088
