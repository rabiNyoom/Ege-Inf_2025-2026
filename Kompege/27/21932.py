# 21932
from math import dist
f = open('21932_A.txt')

data = [list(map(float, l.split())) for l in f]
clusters = []
while data:
    clusters.append([data.pop()])
    lastc = clusters[-1]
    for p in lastc:
        close_by = [p1 for p1 in data if dist(p, p1) < 1]

        for p1 in close_by:
            data.remove(p1)
        lastc.extend(close_by)

# print(*map(len, clusters))


def centroid(cl):
    m = []
    for p in cl:
        sm = sum(dist(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


px = int(abs(centroid(min(clusters, key=len))[0] * 10000))
py = int(abs(centroid(max(clusters, key=len))[1] * 10000))

print(px, py)

# 32865 70666
# 144062 61170
