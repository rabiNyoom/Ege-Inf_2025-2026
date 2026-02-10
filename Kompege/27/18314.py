from math import dist
files = ['18314_A.txt', '18314_B.txt']


def manh(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(manh(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


for f in files:
    data = [list(map(float, l.split())) for l in open(f)]
    clusters = []
    while data:
        clusters.append([data.pop()])
        for p in clusters[-1]:
            close_by = [p1 for p1 in data if dist(p, p1) < 1.2]

            for p1 in close_by:
                data.remove(p1)
            clusters[-1].extend(close_by)
    # print('Clusters:', *map(len, clusters))
    centroids = [centroid(cl) for cl in clusters]
    px = int(abs(sum([x for x, y in centroids]) / len(centroids) * 1000))
    py = int(abs(sum([y for x, y in centroids]) / len(centroids) * 1000))
    print(px, py)
