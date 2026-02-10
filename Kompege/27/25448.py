from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    f = open('25448_A.txt')
    data = [list(map(float, l.split())) for l in f]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    print('Clusters:', *map(len, clusters))

    centroids = [centroid(cl) for cl in clusters]
    px = int(abs((centroids[0][0] - centroids[1][0]) * 10000))
    py = int(abs((centroids[0][1] - centroids[1][1]) * 10000))

    print(px, py)
    f.close()


def b():
    f = open('25448_B.txt')
    data = [list(map(float, l.split())) for l in f]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    print('Clusters:', *map(len, clusters))

    clmin = min(clusters, key=len)
    clmax = max(clusters, key=len)
    centmin = centroid(clmin)
    centmax = centroid(clmax)

    q1 = int(abs(sum(dist(centmin, p1)
                     for p1 in clmin) / (len(clmin) - 1) * 10000))
    q2 = int(abs(sum(dist(centmax, p1)
                     for p1 in clmax) / (len(clmax) - 1) * 10000))
    print(q1, q2)
    f.close()


a()
b()
