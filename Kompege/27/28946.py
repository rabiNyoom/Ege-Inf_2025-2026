from math import dist


def dbscan(filename):
    data = [list(map(float, l.replace(',', '.').split()))
            for l in open(filename)]
    clus = []
    while data:
        clus.append([data.pop()])
        for p in clus[-1]:
            close = [p1 for p1 in data if dist(p, p1) < 1]
            for p1 in close:
                data.remove(p1)
            clus[-1].extend(close)
    # print(*map(len, clus))
    return clus


def centr(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


def a():
    clus = dbscan('28946_A.txt')
    clus.sort(key=len)

    centrsm = centr(clus[0])
    centrbig = centr(clus[1])
    a1 = sum(1 for p in clus[1] if p[1] < centrbig[1])
    a2 = int(abs((centrsm[0] - centrbig[0]) * 10000))
    print(a1, a2)


def b():
    clus = dbscan('28946_B.txt')
    clus.sort(key=len)

    centrmin = centr(clus[0])
    b1 = sum(1 for p in clus[0] if abs(centrmin[0] -
             p[0]) < 0.9 and abs(centrmin[1] - p[1]) < 0.9)
    b2 = int(abs((centr(clus[1])[1] - centr(clus[2])[1]) * 10000))
    print(b1, b2)


a()
b()
