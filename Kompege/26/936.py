with open('936.txt') as f:
    s, _ = map(int, f.readline().split())
    weights = [int(l) for l in f]
    weights.sort(reverse=True)

r = 0
mass = 0
while weights:
    g = s
    mass = 0
    while g > 0:
        if not weights:
            break
        for i in range(0, len(weights)+1):
            if i < len(weights) and g >= weights[i]:
                break
        if i == len(weights):
            break
        g -= weights[i]
        mass += weights[i]
        weights.remove(weights[i])
    r += 1
print(r, mass)
