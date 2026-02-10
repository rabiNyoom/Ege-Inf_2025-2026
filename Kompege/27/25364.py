from math import dist


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def points(cl, disst):
    return sum(1 for p in cl if dist(centroid(cl), p) <= disst)


def a():
    data = [list(map(float, l.split())) for l in open('25364_A.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    centroids = [centroid(cl) for cl in clusters]
    rasst = [dist([1.0, 1.0], cen) for cen in centroids]

    px = int(abs(min(rasst) * 10000))
    py = int(abs(max(rasst) * 10000))
    print(px, py)


def b():
    data = [list(map(float, l.split())) for l in open('25364_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))

    q1 = points(max(clusters, key=len), 1.2)
    q2 = points(max(clusters, key=len), 0.75)
    print(q1, q2)


a()
b()
