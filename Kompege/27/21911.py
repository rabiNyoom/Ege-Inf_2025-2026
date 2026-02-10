# 21911
from math import dist
f = open('21911_B.txt')

data = [list(map(float, l.split())) for l in f]
clusters = []
while data:
    clusters.append([data.pop()])
    lastc = clusters[-1]
    for p in lastc:
        close_by = [p1 for p1 in data if dist(p, p1) < 2]

        for p1 in close_by:
            data.remove(p1)
        lastc.extend(close_by)


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centroids = [centroid(cl) for cl in clusters]
px = int(abs(sum(x for x, _ in centroids) / len(centroids) * 10000))
py = int(abs(sum(y for _, y in centroids) / len(centroids) * 10000))

print(px, py)

# 26216 24182
# 150891 63754
