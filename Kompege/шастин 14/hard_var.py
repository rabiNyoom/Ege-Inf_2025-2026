def t24():
    from itertools import product

    for a in range(3):
        for p in product("0123456789", repeat=a):
            p = "".join(p)
            for p1 in product("0123456789", repeat=a):
                p1 = "".join(p1)
                n = int(f"42{p}11{p1}24")
                if n % 3421 == 0:
                    print(n, n // 3421)


def t27():
    from math import dist

    def centr(cl):
        m = []
        for p in cl:
            sm = sum(dist(p, p1) for p1 in cl)
            m.append([sm, p])
        return min(m)[1]

    def solve(fname):
        data = [
            tuple(map(float, line.replace(",", ".").split())) for line in open(fname)
        ]
        clus = []
        while data:
            clus.append([data.pop()])
            for p in clus[-1]:
                close = [p1 for p1 in data if dist(p, p1) < 0.5]
                for p1 in close:
                    data.remove(p1)
                clus[-1].extend(close)
        # print(*map(len, clus))
        centers = [centr(cl) for cl in clus]
        px = int(abs(sum(p[0] for p in centers) / len(centers) * 10000))
        py = int(abs(sum(p[1] for p in centers) / len(centers) * 10000))
        print(px, py)

    solve("27A_har.txt")
    solve("27B_har.txt")
