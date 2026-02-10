from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    data = [list(map(float, l.split())) for l in open('25439_A.txt')]
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
    centroids = [centroid(cl) for cl in clusters]

    px = int(abs(min([x for x, y in centroids]) * 10000))
    py = int(abs(min([y for x, y in centroids]) * 10000))
    print(px, py)


def b():
    data = [list(map(float, l.split())) for l in open('25439_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 0.1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    # print('Clusters:', *map(len, clusters))
    cllen = list(map(len, clusters))

    q1 = min(cllen)
    q2 = max(cllen)
    print(q1, q2)


a()
b()
