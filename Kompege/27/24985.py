from math import dist

def anticentroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return max(m)[1]

data = [list(map(float, l.replace(',','.').split())) for l in open('24985_A.txt')]
clusters = []

while data:
    clusters.append([data.pop()])
    for p in clusters[-1]:
        close_by = [p1 for p1 in data if dist(p, p1) < 1.5]

        for p1 in close_by:
            data.remove(p1)
        clusters[-1].extend(close_by)
# print('Clusters:', *map(len,clusters))
clusters = [cl for cl in clusters if len(cl) > 1]
anticentroids = [anticentroid(cl) for cl in clusters]
px = int(abs(max([x for x, y in anticentroids]) * 10000))
py = int(abs(max([y for x, y in anticentroids]) * 10000))
