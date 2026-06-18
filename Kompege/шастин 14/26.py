with open("26_30474.txt") as f:
    amount = int(f.readline())
    load = [0] * (amount + 1)
    for l in f:
        start, end = map(int, l.split())
        load[start:end] = (x + 1 for x in load[start:end])

max_load = max(load)
load_length = sum(1 for i in load if i == max_load)
print(max_load, load_length)
