from math import hypot


def dist(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])


o_giant = None


def dbscan(fname):
    global o_giant
    data = []
    for l in open(fname):
        x, y, attr = l.replace(',', '.').split()
        p = [float(x), float(y), attr]
        data.append(p)
        if attr == 'N9I':
            o_giant = p

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
    clus = dbscan('29077_A.txt')
    centrs = [centr(cl) for cl in clus]

    dists = [dist(o_giant, p) for p in centrs]
    a1 = int(abs(min(dists) * 10000))
    a2 = int(abs(max(dists) * 10000))
    print(a1, a2)


def b():
    clus = dbscan('29077_B.txt')
    clus.sort(key=len)

    b1 = sum(1 for p in clus[2] if p[2][1].isdigit() and int(p[2][1]) > 7)
    b2 = sum(1 for p in clus[1] if p[2][1].isdigit() and int(p[2][1]) < 4)
    print(b1, b2)


a()
b()
