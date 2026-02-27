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
            for l in open('25441_A.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    # print('Clusters:',  *map(len, clusters))
    ca, cb = centroid(clusters[0]), centroid(clusters[1])

    px = int(abs(ca[0] - cb[0]) * 10000)
    py = int(abs(ca[1] - cb[1]) * 10000)

    print(px, py)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('25441_B.txt')]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 0.2]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    clusters = [cl for cl in clusters if len(cl) > 1]
    # print('Clusters:',  *map(len, clusters))
    clusters.sort(key=len)
    ca, cb = centroid(clusters[0]), centroid(clusters[2])

    q1 = int(dist(ca, cb) * 10000)
    q2 = int(max(maxd(cl) for cl in clusters) * 10000)

    print(q1, q2)


a()
b()

# 18236 93042
# 9163 1646
