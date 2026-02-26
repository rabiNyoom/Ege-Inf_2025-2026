from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    data = [list(map(float, l.split())) for l in open('27_A.txt')]
    datacopy = data.copy()
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 2]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    clusters.sort(key=len)
    most = centroid(clusters[-1])
    least = centroid(clusters[0])

    p1 = len([p for p in datacopy if dist(most, p) <= 0.7])
    p2 = len([p for p in datacopy if dist(least, p) >= 1.3])
    print(p1, p2)


def b():
    data = [list(map(float, l.split())) for l in open('27_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 2]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    centroids = [centroid(cl) for cl in clusters]

    q1 = int(min([dist([1.7, 2.3], c) for c in centroids]) * 10000)
    q2 = int(max([dist([1.7, 2.3], c) for c in centroids]) * 10000)

    print(q1, q2)


a()
b()

# 5 189
# 261162 371295
