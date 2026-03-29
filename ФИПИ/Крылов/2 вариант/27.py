from math import dist


def centr(cl):
    s = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        s.append([sm, p])
    return min(s)[1]


def a():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27A.txt')]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]

            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    # print('Clusters:', *map(len, clus))
    clus = [cl for cl in clus if len(cl) > 1]
    centrs = [centr(cl) for cl in clus]

    px = int(abs(min(x for x, y in centrs) * 10000))
    py = int(abs(min(y for x, y in centrs) * 10000))

    print(px, py)


def b():
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open('27B.txt')]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 0.1]

            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    # print('Clusters:', *map(len, clus))
    clus = [cl for cl in clus if len(cl) > 1]
    lens = list(map(len, clus))

    q1 = min(lens)
    q2 = max(lens)

    print(q1, q2)


a()
b()
